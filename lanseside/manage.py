#!/usr/bin/env python
import os
import sys

import schedule
import time
import threading
import yrWbPlot

from modules import lanse
import sqlite3

def hentDataFraVerstasjon():
    verstasjonData = lanse.getSData()   #henter data fra værstasjon
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    c.execute('SELECT * FROM startside_verdata')
    names = list(map(lambda x: x[0], c.description)) #henter ut navn i rad fra database

    for x in names: #om verdata stemmer overends med database, lagre data
        if x in verstasjonData:
            c.execute('UPDATE startside_verdata SET {}={}'.format(x,verstasjonData[x]))

    conn.commit()
    conn.close() #lagre inn i database

def planlagtArbeid(): #denne threaden skal ta seg av alle tidsbestemte oppgaver
    print('thread er i gang')
    yrWbPlot.yrplot()
    hentDataFraVerstasjon()
    schedule.every(60).minutes.do(yrWbPlot.yrplot)
    schedule.every(1).minutes.do(hentDataFraVerstasjon)
    while True:
        print("arbeidsthread")
        schedule.run_pending()
        time.sleep(10)
    #time.sleep(3600)
    #yrgraf()

if os.environ.get('RUN_MAIN') != 'true':        #sjekker hvilken 'thread' man kjører i for å unngå dobbelkjøring
    t = threading.Thread(target=planlagtArbeid, daemon=True)
    t.start()

if __name__ == "__main__":  #starter utviklingsserveren
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lanseside.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

    

    #os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lanseside.settings")

    #from django.core.management import call_command
    #from django.core.wsgi import get_wsgi_application 
    #application = get_wsgi_application()
    #call_command('runserver',  '127.0.0.1:8000')

    
