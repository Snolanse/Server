import requests
from bs4 import BeautifulSoup as soup

def yrdata():
    page = requests.get("https://www.yr.no/sted/Norge/Tr%C3%B8ndelag/Trondheim/Gran%C3%A5sen~211388/time_for_time_detaljert.html") # Laster ned nettside fra yr
    page_html = page.content # henter ut nettsidekoden fra nedlastingen
    page_soup = soup(page_html, 'html.parser')  # Går gjennom koden og tolker den for å gjøre den søkbar
    radata = page_soup.find("div",{"id": "Div1"}).findAll("table",{"id": "detaljert-tabell"}) # Finner og plukker ut tabell som har ønsket data

    json = {}
    for count,dag in enumerate(radata): #sorter gjennom data og lagrer
        data = dag.tbody.findAll('tr')
        dagsholder = {}
        for nr,dat in enumerate(data):
            dataholder = {}
        
            time = dat.find('th').text[1:-1]
            temp = dat.findAll('td')[1].text[:-1]
            trykk = dat.findAll('td')[4].text
            luftfukt = dat.findAll('td')[5].text
        
            dataholder["time"] = time
            dataholder["temp"] = temp
            dataholder["trykk"] = trykk
            dataholder["luftfukt"] = luftfukt
        
            dagsholder[nr] = dataholder
        
        json[count] = dagsholder

    return json