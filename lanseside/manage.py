#!/usr/bin/env python
import os
import sys

#import schedule
import time
import threading
import yrWbPlot

def yrgraf():
    print('graf er i gang')
    yrWbPlot.yrplot()
    #schedule.every(1).minutes.do(yrWbPlot.yrplot)
    #while True:
        #schedule.run_pending()
        #time.sleep(1)
    time.sleep(3600)
    yrgraf()

if os.environ.get('RUN_MAIN') != 'true':
        t = threading.Thread(target=yrgraf, daemon=True)
        t.start()

if __name__ == "__main__":
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

    
