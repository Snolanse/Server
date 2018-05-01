/*Deklarering av de variablene som blir brukt i koden*/
var iknapper;
var jsjekk;
var kslett;
var stegvalgknapper = "";
var valgtsteg;
var steg;
var node = "";
var nodelabel = "";
var nodespan = "";
var antknapper;
var markertlanse = "";
var bestemmarkering;
var hentstegknapper;
var psjekk;

/*Funksjon for aa generere radioknapper for stegvalg*/
function leggtilknapper() {

    /*Henter hvor mange steg lansen har fra database*/
    antknapper = document.getElementById("ant_steg").value;
        
        /*Sletter knapper som var på siden fra foor av*/ 
        for (kslett = 0; kslett < stegvalgknapper.value; kslett++) {

            document.getElementById(kslett).remove();
            document.getElementById("mark" + kslett).remove();

        }

        /*Legger til riktig antall knapper*/ 
        for (iknapper = 0; iknapper < antknapper; iknapper++) {

            /*LI gjør at knappene blir plassert under hverandre*/
            node = document.createElement("LI");
            node.setAttribute("id", "mark" + iknapper);
            node.setAttribute("name", "mark");

            /*Lager knapper til å være radiogruppe*/
            stegvalgknapper = document.createElement("INPUT");
            stegvalgknapper.setAttribute("type", "radio");
            stegvalgknapper.setAttribute("name", "radiogruppe");
            stegvalgknapper.setAttribute("class", "radiogruppene");
            stegvalgknapper.setAttribute("value", iknapper + 1);
            stegvalgknapper.setAttribute("id", iknapper);
            stegvalgknapper.setAttribute("onClick", "window.ktrykk = 1; oppd_server(String(document.getElementById('lansenummer').value), { 'modus': document.getElementById('"+iknapper+"').id })")

            /*Legger til Tekst som står ved siden av knappene*/
            nodelabel = document.createElement("LABEL");
            nodelabel.setAttribute("id", "container" + iknapper);
            nodelabel.setAttribute("class", "container");

            /*Span gjør det mulig å endre på stilen til knappene*/
            nodespan = document.createElement("SPAN");
            nodespan.setAttribute("id", "checkmark" + iknapper);
            nodespan.setAttribute("class", "checkmark");

            /*Kode som setter inn label, span, li og input i riktig rekkefølge og plasserer koden riktig mens knappene legges til på nettsiden*/
            document.getElementById("tekstfelt").appendChild(node);
            document.getElementById("mark" + iknapper).appendChild(nodelabel);
            document.getElementById("container" + iknapper).appendChild(stegvalgknapper);
            document.getElementById("container" + iknapper).appendChild(nodespan);

            if (stegvalgknapper.id === "0") {
                /*Steg 0 er av*/
                document.getElementById("container0").innerHTML += "Av";
            }

            else if (antknapper === "2") {

                /*Dersom det bare er 2 steg kan man bytte mellom av og på*/
                document.getElementById("container1").innerHTML += "På";
                
                 /*Viser tekstfelt over anbefalt dysevalg for 2-stegslanser*/
                document.getElementById("anbefaltdysetekst").setAttribute("style", "visibility: visible");
            }
            else {
                document.getElementById("container" + iknapper).innerHTML += "Steg nr. " + stegvalgknapper.id;
                
                 /*Viser ikke anbefalt dysevalg dersom lansen har flere steg*/
                document.getElementById("anbefaltdysetekst").setAttribute("style", "visibility: hidden");
                //document.getElementById('anbefaltdysetekst').remove()
            }

            if (stegvalgknapper.id === man_steg.toString()) {
                
                /*Markerer steget som er valgt av databasen etter knappene har blitt generert*/
                document.getElementById(iknapper).checked = True
            }

        }

}

/*Funksjon som finner ut hvilken knapp som er valgt*/
function oppdatervalgtsteg() {
    
    steg = document.getElementsByName("radiogruppe");

    /*Ser gjennom alle knappene for å finne hvilken knapp som er valgt*/
    for (jsjekk = 0; jsjekk < steg.length; jsjekk++) {
        if (steg[jsjekk].checked == true) {
            valgtsteg = steg[jsjekk].value;
        }
    }
}

/*Funksjon for hva som skjer om lansen blir satt i auto eller manuell*/
function automan() {

    hentstegknapper = document.getElementsByName("radiogruppe");

    if (document.getElementById("auto").checked === true ) {

        /*Dersom lansen blir satt i auto, er det ikke mulig å bytte mellom steg på lansen*/
        for (psjekk = 0; psjekk < hentstegknapper.length; psjekk++) {

            document.getElementById(psjekk).setAttribute("disabled", "disabled");

        }
    }
    if (document.getElementById("manuell").checked === true) {

        /*Gjør det mulig å endre på steg når lansen er satt i manuell*/
        for (psjekk = 0; psjekk < hentstegknapper.length; psjekk++) {

            document.getElementById(psjekk).removeAttribute("disabled", "disabled");

        }
    }
}

/*Leser fra databasen om lansen er i auto eller manuell*/
function onload() {
    if (document.getElementById("auto").value === "True") { document.getElementById("auto").checked = true }
    if (document.getElementById("auto").value === "False") { document.getElementById("manuell").checked = true }
    //automan()

}
onload()
setTimeout(automan,0);

//sender informasjon til serveren
function oppd_server(id, datainnput) {
    token = getCookie('csrftoken');
    data = {
        'csrfmiddlewaretoken': token, 
        'get': 0,
        'bronnid': 'bronn' + id

    };

    for (var i = 0; i < Object.keys(datainnput).length; i++) {
        data[Object.keys(datainnput)[i]] = datainnput[Object.keys(datainnput)[i]];
    };

    var posting = $.post("data", data);

    posting.done();
}

//henter data fra serveren
function hent_server_data(id) {
    token = getCookie('csrftoken');
    data = {
        'csrfmiddlewaretoken': token,
        'get': 1,
        'bronnid': 'bronn' + id

    };

    var posting = $.post("data", data);

    posting.done(function (data) {
        window.content = $(data);
        d = $(data);
       
    })

    return 0
}

//henter data fra serveren og oppdaterer siden
function oppd_side() {
    window.oppd_tid = new Date().getTime()
    window.ktrykk = 0
    token = getCookie('csrftoken');
    data = {
        'csrfmiddlewaretoken': token,
        'get': 1,
        'bronnid': 'bronn' + document.getElementById('lansenummer').value.toString()

    };

    var posting = $.post("data", data);

    posting.done(function (data) {
        window.content = $(data);
        sidedata = $(data);
        if (window.ktrykk == 1) { console.log('ikkekjør'); return 0 }

        if (sidedata[0].lanse.lokal_maling) {
            document.getElementById('lufttemperatur').value = sidedata[0].lanse.temperatur_luft.toString() + '℃';
            document.getElementById('lfukt').value = sidedata[0].lanse.luftfukt + '%';
        }
        else {
            document.getElementById('lufttemperatur').value = sidedata[0].verstasjon.temp_2.toString() + '℃';
            document.getElementById('lfukt').value = sidedata[0].verstasjon.hum.toString() + '%';
        }

        document.getElementById('vtrykk').value = sidedata[0].lanse.vanntrykk.toString() + ' Bar';
        m_steg = sidedata[0].lanse.modus.toString();
        auto = sidedata[0].lanse.auto_man;

        document.getElementById(m_steg).checked = True

        if (auto === true) {
            document.getElementById("auto").value = "True"
        }
        else {
            document.getElementById("auto").value = "False"
        }

        onload()
        automan()

        setTimeout(oppd_side, 1000)
    })

    posting.fail(function () {
        console.log('feil ved henting av data')
        setTimeout(function () { alert("Ingen kontakt med server\nTrykk ok for å prøve på nytt") },1); 
        setTimeout(oppd_side, 3000)
    })
    return 0
    
}

//kjører oppdateringen av siden og sikrer at denne ikke kjører flere ganger
if (window.kjoroppdater !== 1) {
    setTimeout(oppd_side, 200)
    window.kjoroppdater = 1;
}

setTimeout(function () {    //starter oppdatering om det ser ut som oppdateringen har sluttet
    setInterval(function () {
        if ((new Date().getTime() - window.oppd_tid) > 15000) {
            oppd_side();
        }
        }, 500)
},200)

//kjører oppdateringen av siden og sikrer at denne ikke kjører flere ganger
//if (window.kjoroppdater !== 1) {
//    setTimeout(function () { setInterval(oppd_side, 1200) }, 500);
//    window.kjoroppdater = 1;
//}

//håndterer anbefalingen av dyser
function anbefaldyse() {

    /*	document.getElementById("dysevalg").value=anbefalingdyse;*/
    if (Number(window.content[0].lanse.lokal_maling)) {
        rh = Number(window.content[0].lanse.luftfukt);
        tdb = Number(window.content[0].lanse.temperatur_luft);
    }
    else {
        rh = Number(window.content[0].verstasjon.hum);
        tdb = Number(window.content[0].verstasjon.temp_2);
    }
    mbpressure = Number(window.content[0].verstasjon.press);

    es = Number(6.112 * Math.exp((17.67 * tdb) / (tdb + 243.5)));
    e = Number(es * (rh / 100));

    edifference = 1;
    previousign = 1;
    incr = 10;
    twguess = 0;

    dewpoint = Number(243.5 * Math.log((e) / (6.112)) / (17.67 - Math.log((e / 6.112))));

    while (Math.abs(edifference) > 0.005) {
        ewguess = 6.112 * Math.exp((17.67 * twguess) / (twguess + 243.5));
        eguess = ewguess - mbpressure * (tdb - twguess) * 0.00066 * (1 + (0.00115 * twguess));
        edifference = e - eguess;

        if (edifference === 0) {
            break;
        }
        else {
            if (edifference < 0) {
                cursign = -1;

                if (cursign !== previousign) {
                    previousign = cursign;
                    incr = incr / 10;
                }
                else {
                    incr = incr;
                }
            }
            else {
                cursign = 1;

                if (cursign !== previousign) {
                    previousign = cursign;
                    incr = incr / 10;
                }
                else {
                    incr = incr;
                }

            }
        }
        twguess = twguess + incr * previousign;

    }
    twb = Math.round(twguess * 100) / 100;

    //document.getElementById("wetbulb").value = twb;


    if ((twb <= -5) && (twb > -7)) {
        document.getElementById("dysevalg").value = "Bruk 10-dyse";

    }

    if ((twb <= -7) && (twb > -9)) {
        document.getElementById("dysevalg").value = "Bruk 20-dyse";

    }

    if (twb <= -9) {
        document.getElementById("dysevalg").value = "Bruk 40-dyse";

    }
    if (twb > -5) {
        document.getElementById("dysevalg").value = "Lager ikke snø nå";

    }



    /*Andre metoden å regne ut Wet-Bulb*/
    /*twb= (tdb* Math.atan(0.151977 * Math.pow((rh + 8.313659),0.5))) +(Math.atan(tdb + rh)) - (Math.atan(rh - 1.676331)) + (0.00391838*Math.pow((rh),1.5) *Math.atan(0.023101*rh)) -4.686035;*/


}
setTimeout(function () { setInterval(anbefaldyse, 1000) }, 2000);
//setInterval(anbefaldyse, 1000);
