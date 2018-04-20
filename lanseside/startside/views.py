from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from startside.models import Lanse, Lansetyper, Verdata
from django.views.decorators import csrf
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.decorators import login_required
from modules.lanse import getSData, wetbulb
import time

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

##@ensure_csrf_cookie
#def test(request):  #testside, skal fjernes
#    if request.method == 'GET':
#        led = LED.objects.all()[0]
#        state = led.stat
#        args = {
#            'state': state}
#        return(render(request, 'test/test.html',args))
#    elif request.method == 'POST':                          #denne må flyttes til /data 
#        bronn = request.POST['bronnid']
#        #print(bronn)
#        bronn_nr = int(bronn[(bronn.find('bronn'))+5:])
#        #print(bronn_nr)
#        lanse = Lanse.objects.all().order_by('plassering_bronn')[bronn_nr-1]
#        lansetype = Lansetyper.objects.all().order_by('lanseid')[lanse.lanse_kategori-1]
#        ts = time.time()

#        if request.POST.__contains__('timestamp'):
#            lanse.timestamp = ts
#            lanse.save()

#        get = request.POST['get']
#        if get == '1':
#            if lanse.lokal_maling == 0:
#                try:
#                    #vdata = getSData()
#                    ver = Verdata.objects.get(id = 1)
#                    lanse.luftfukt = lfukt = ver.hum
#                    lanse.ltrykk = ver.press
#                    lanse.temperatur = ver.temp_2
#                    lanse.save()
                    
#                    ver = vars(ver)
#                    del ver['_state']
#                except:
#                    print('Værserver er nede')

#            lanse = vars(lanse)
#            lansetype = vars(lansetype)
#            del lanse['_state']
#            del lansetype['_state']

#            data = {'lanse':lanse, 'lansetype':lansetype, 'verstasjon':ver}

#            return JsonResponse(data)
#        elif get == '0':
#            for x in request.POST:
#                if hasattr(lanse,x):
#                    setattr(lanse, x, request.POST[x] )
#            lanse.save()

#            lanse = vars(lanse)
#            lansetype = vars(lansetype)
#            del lanse['_state']
#            del lansetype['_state']

#            data = {'timestamp': ts}
#            return JsonResponse(data)
#        else:
#            return JsonResponse({'error':-1})
#    else:
#        return HttpResponse('')

@ensure_csrf_cookie
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
            print(bronn_nr)
            lanse = Lanse.objects.all().order_by('plassering_bronn')[bronn_nr-1]
            lansetype = Lansetyper.objects.all().order_by('lanseid')[lanse.lanse_kategori-1]
            ant_steg = lansetype.ant_steg

            lanse = vars(lanse)
            del lanse['_state']
            lansetype = vars(lansetype)
            del lansetype['_state']

            for x in lanse:
                args[x] = lanse[x]
            for x in lansetype:
                args[x] = lansetype[x]
        except:
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
        lansetype = Lansetyper.objects.all().order_by('lanseid')[lanse.lanse_kategori-1]
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