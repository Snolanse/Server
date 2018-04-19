from modules import yrdata
from modules import lanse
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

def yrplot(): #lager et plot av wetbulb med data fra yr
    wb = []

    data = yrdata.yrdata() #henter data fra yr
    for x in data:
        for y in data[x]:
            data[x][y]
            wb.append(lanse.wetbulb(int(data[x][y]['temp']),int(data[x][y]['luftfukt'][0:-1]))) #sorterer data

    t = list(range(len(wb)))

    plt.plot(t,wb)

    plt.xlabel('Timer fra '+ data[0][0]['time'])
    plt.ylabel('Wetbulb Temperatur [C]')
    plt.title('Wetbulb fram i tid, Granåsen skisenter')
    plt.grid(True)

    plt.savefig('startside/static/lansestyring/yrwb.png') #lagrer
    plt.clf()