from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from startside.models import Lanse, Lansetype, Verdata, langtidslagring
from django.views.decorators import csrf
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.decorators import login_required
from modules.lanse import getSData, wetbulb
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
import time

import sys, os

# Create your views here.

@login_required     #er en side som returnerer data om alle lanser
@ensure_csrf_cookie
def info(request):
    if request.method == 'GET':
        return(render(request, 'Info/Info.html')) #viser infosiden
    if request.method == 'POST':            #skal returnere all data
        lanser_objhold = Lanse.objects.all()
        verdata = Verdata.objects.get(id=1)
        lanser = {}
        for x in range(len(lanser_objhold)):
            if lanser_objhold[x].lokal_maling == 0:
                lanser_objhold[x].luftfukt = verdata.hum
                lanser_objhold[x].temperatur_luft = verdata.temp_2

            lanser[x] = vars(lanser_objhold[x])
            del lanser[x]['_state']
        return JsonResponse(lanser)

@login_required
def master(request):
    if request.method == 'GET':
        return(render(request, 'Master/Master.html')) #viser mastersiden
    elif request.method == 'POST':
        if request.POST['auto_man_samtlige'] == '1':
            print("alle i auto")
            allelanser = Lanse.objects.all()
            allelanser.update(auto_man=1)
        elif request.POST['auto_man_samtlige'] == '0':
            print("alle i man")
            allelanser = Lanse.objects.all()
            allelanser.update(auto_man=0)
        return JsonResponse({'timestamp':time.time()})

@ensure_csrf_cookie
def startside(request):
    return(render(request, 'startside/startside.html')) #viser startsiden

@ensure_csrf_cookie     
def csrf(request):      #enkel side som gir ut csrf tag
    return HttpResponse('csrftag')


@login_required
#@ensure_csrf_cookie
def lanser(request):        #lansesiden, hoster bildet
    if request.method == 'GET':
        return(render(request, 'startside/lanser.html'))
    elif request.method == 'POST':
        x = int(request.POST['lanse'])
        lanse = Lanse.objects.get(lanse_nr = x)
        lanse = vars(lanse)
        del lanse['_state']
        return JsonResponse(lanse)


@ensure_csrf_cookie
def valgtlanse(request):    #siden som henter inn spesifikk lanse
    if request.method == 'GET':
        return JsonResponse({'info': 'dette var en get'})
    if request.method == 'POST':
        try:
            args = {}
            bronn = request.POST['bronnid']
            print(bronn)
            bronn_nr = int(bronn[(bronn.find('bronn'))+5:])
            lanse = Lanse.objects.all().order_by('plassering_bronn')[bronn_nr-1]
            lansetype = Lansetype.objects.get(lansetype= lanse.lanse_kategori)
            ant_steg = lansetype.ant_steg
            verstasjon = Verdata.objects.get(id=1)

            verstasjon = vars(verstasjon)
            del verstasjon['_state']
            lanse = vars(lanse)
            del lanse['_state']
            lansetype = vars(lansetype)
            del lansetype['_state']

            for x in lanse:
                args[x] = lanse[x]
            for x in lansetype:
                args[x] = lansetype[x]
            for x in verstasjon:
                if x == 'timestamp':
                    pass
                else:
                    args[x] = verstasjon[x]

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            args[bronn] = 'ingen lanse'
            args[ant_steg] = 0

        finally:
            #return JsonResponse(args)
            return(render(request, 'lansestyring/lansestyring.html', args))
    else:
        return HttpResponse('')

#@ensure_csrf_cookie
def data(request):  
    if request.method == 'GET':
        return HttpResponse('')
    elif request.method == 'POST': 
        bronn = request.POST['bronnid']
        #print(bronn)
        bronn_nr = int(bronn[(bronn.find('bronn'))+5:])
        #print(bronn_nr)
        lanse = Lanse.objects.all().order_by('plassering_bronn')[bronn_nr-1]
        lansetype = Lansetype.objects.get(lansetype=lanse.lanse_kategori)
        ts = time.time()
        if request.POST.__contains__('timestamp'):
            lanse.timestamp = ts
            lanse.save()
            logg = langtidslagring(lanse_id=lanse.plassering_bronn, steg=lanse.modus, timestamp=ts, vanntrykk=lanse.vanntrykk)
            logg.save()

        get = request.POST['get']
        if get == '1':
            if lanse.lokal_maling == 0:
                try:
                    #vdata = getSData()
                    ver = Verdata.objects.get(id = 1)
                    lanse.luftfukt = lfukt = ver.hum
                    lanse.ltrykk = ver.press
                    lanse.temperatur = ver.temp_2
                    lanse.save()
                    
                    ver = vars(ver)
                    del ver['_state']
                except:
                    print('Værserver er nede')

            lanse = vars(lanse)
            lansetype = vars(lansetype)
            del lanse['_state']
            del lansetype['_state']

            data = {'lanse':lanse, 'lansetype':lansetype, 'verstasjon':ver}

            return JsonResponse(data)
        elif get == '0':
            for x in request.POST:
                if hasattr(lanse,x):
                    if x == 'lanse_kategori':
                        if Lansetype.objects.filter(lansetype=request.POST[x]).exists():
                            lanse.lanse_kategori = Lansetype.objects.get(lansetype=request.POST[x])
                    else:
                        setattr(lanse, x, request.POST[x] )
                
            lanse.save()

            lanse = vars(lanse)
            lansetype = vars(lansetype)
            del lanse['_state']
            del lansetype['_state']

            data = {'timestamp': ts}
            return JsonResponse(data)
        else:
            return JsonResponse({'error':-1})
    else:
        return HttpResponse('')


def mylogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            print('bg, nologin')
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

def mylogout(request):
    logout(request)
    return HttpResponseRedirect('/')