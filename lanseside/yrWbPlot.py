from modules import yrdata
from modules import lanse
import matplotlib.pyplot as mpl

def yrplot():
    wb = []

    data = yrdata.yrdata()
    for x in data:
        for y in data[x]:
            data[x][y]
            wb.append(lanse.wetbulb(int(data[x][y]['temp']),int(data[x][y]['luftfukt'][0:-1])))

    t = list(range(len(wb)))

    mpl.plot(t,wb)

    mpl.xlabel('Timer fra '+ data[0][0]['time'])
    mpl.ylabel('Wetbulb Temperatur [C]')
    mpl.title('Wetbulb fram i tid, Granåsen skisenter')
    mpl.grid(True)

    mpl.savefig('startside/static/lansestyring/yrwb.png')
