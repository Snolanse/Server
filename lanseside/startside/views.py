from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from startside.models import Lanse, Lansetyper, Verdata
from django.views.decorators import csrf
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.decorators import login_required
from modules.lanse import getSData, wetbulb
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
import time

import sys, os

# Create your views here.

@login_required     #er en side som returnerer data om lanse 1, viser at man trenger å logge inn.
@ensure_csrf_cookie
def info(request):
    if request.method == 'GET':
        #lanse = Lanse.objects.all().order_by('plassering_bronn')[1]
        lanse = Lanse.objects.get(plassering_bronn = 1)
        lanse = vars(lanse)
        del lanse['_state']
        return JsonResponse(lanse)
    if request.method == 'POST':
        #lanse = Lanse.objects.get(lanse_nr = 1)
        lanse = Lanse.objects.get(plassering_bronn = 1)
        lanse = vars(lanse)
        del lanse['_state']
        return JsonResponse(lanse)

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
            lansetype = Lansetyper.objects.get(lansetype= lanse.lanse_kategori)
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
        lansetype = Lansetyper.objects.get(lansetype=lanse.lanse_kategori)
        ts = time.time()
        if request.POST.__contains__('timestamp'):
            lanse.timestamp = ts
            lanse.save()

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