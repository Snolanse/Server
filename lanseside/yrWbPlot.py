from modules import yrdata
from modules import lanse
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import datetime

def yrplot(): #lager et plot av wetbulb med data fra yr
    wb = []

    data = yrdata.yrdata() #henter data fra yr
    for x in data:
        for y in data[x]:
            data[x][y]
            #wb.append(lanse.wetbulb(int(data[x][y]['temp']),int(data[x][y]['luftfukt'][0:-1]))) #sorterer data
            wb.append(lanse.wetBulbMedAtmTrykk(int(data[x][y]['luftfukt'][0:-1]),int(data[x][y]['temp']),int(data[x][y]['trykk'][0:-4]))) #sorterer data

    t = list(range(len(wb)))

    plt.plot(t,wb)
    
    plt.xlabel('Timer fra '+ data[0][0]['time']+ ', ' +  str(datetime.date.today().day) + '/' + str(datetime.date.today().month) + '-' +str(datetime.date.today().year) + '\nVervarsel fra Yr levert av Meteorologisk institutt og NRK')
    plt.ylabel('Wetbulb Temperatur [C]')
    plt.title('Wetbulb fram i tid, Granåsen skisenter')
    plt.grid(True)
    plt.tight_layout()

    plt.savefig('startside/static/lansestyring/yrwb.png') #lagrer
    plt.clf()
