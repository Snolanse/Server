from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from startside.models import Lanse, LED, Lansetyper
from django.views.decorators import csrf
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.decorators import login_required
from modules.lanse import getSData, wetbulb
import time
try:
    from modules.Blinky import on_off
except:
    print('Fikk ikke lasta blinky')


# Create your views here.

@login_required
@ensure_csrf_cookie
def info(request):
    if request.method == 'GET':
        lanse = Lanse.objects.get(lanse_nr = 1)
        lanse = vars(lanse)
        del lanse['_state']
        return JsonResponse(lanse)
    if request.method == 'POST':
        lanse = Lanse.objects.get(lanse_nr = 1)
        lanse = vars(lanse)
        del lanse['_state']
        return JsonResponse(lanse)

@ensure_csrf_cookie
def startside(request):
    return(render(request, 'startside/startside.html'))

#@ensure_csrf_cookie
def test(request):
    if request.method == 'GET':
        led = LED.objects.all()[0]
        state = led.stat
        args = {
            'state': state}
        return(render(request, 'test/test.html',args))
    elif request.method == 'POST':
        bronn = request.POST['bronnid']
        #print(bronn)
        bronn_nr = int(bronn[(bronn.find('bronn'))+5:])
        #print(bronn_nr)
        lanse = Lanse.objects.all().order_by('plassering_bronn')[bronn_nr-1]
        lansetype = Lansetyper.objects.all().order_by('lanseid')[lanse.lanse_kategori-1]
        ts = time.time()
        lanse.timestamp = ts
        lanse.save()
        get = request.POST['get']
        if get == '1':
            if lanse.lokal_maling == 0:
                vdata = getSData()
                lanse.luftfukt = lfukt = vdata['hum']
                lanse.ltrykk = vdata['press']
                lanse.temperatur = vdata['temp_2']
                lanse.save()

            lanse = vars(lanse)
            lansetype = vars(lansetype)
            del lanse['_state']
            del lansetype['_state']

            data = {'lanse':lanse, 'lansetype':lansetype}

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

@ensure_csrf_cookie
def lanser(request):
    if request.method == 'GET':
        return(render(request, 'startside/lanser.html'))
    elif request.method == 'POST':
        x = int(request.POST['lanse'])
        lanse = Lanse.objects.get(lanse_nr = x)
        lanse = vars(lanse)
        del lanse['_state']
        return JsonResponse(lanse)

@ensure_csrf_cookie
def valgtlanse(request):
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