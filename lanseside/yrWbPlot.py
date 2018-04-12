from modules import yrdata
from modules import lanse
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

def yrplot():
    wb = []

    data = yrdata.yrdata()
    for x in data:
        for y in data[x]:
            data[x][y]
            wb.append(lanse.wetbulb(int(data[x][y]['temp']),int(data[x][y]['luftfukt'][0:-1])))

    t = list(range(len(wb)))

    plt.plot(t,wb)

    plt.xlabel('Timer fra '+ data[0][0]['time'])
    plt.ylabel('Wetbulb Temperatur [C]')
    plt.title('Wetbulb fram i tid, Granåsen skisenter')
    plt.grid(True)

    plt.savefig('startside/static/lansestyring/yrwb.png')
    plt.clf()