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

/*Funksjon for å generere radioknapper for stegvalg*/
function leggtilknapper() {

    /*Henter hvor mange steg lansen har fra database*/
    antknapper = document.getElementById("ant_steg").value;
        
        /*Sletter knapper som var på siden fra før av*/ 
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
            stegvalgknapper.setAttribute("onClick", "window.ktrykk = 1; oppd_server(String(document.getElementById('lansenummer').value), { 'man_steg': document.getElementById('"+iknapper+"').id })")

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

    var posting = $.post("test", data);

    posting.done();
}

function hent_server_data(id) {
    token = getCookie('csrftoken');
    data = {
        'csrfmiddlewaretoken': token,
        'get': 1,
        'bronnid': 'bronn' + id

    };

    var posting = $.post("test", data);

    posting.done(function (data) {
        window.content = $(data);
        d = $(data);
       
    })

    return 0
}

function oppd_side() {
    window.ktrykk = 0
    token = getCookie('csrftoken');
    data = {
        'csrfmiddlewaretoken': token,
        'get': 1,
        'bronnid': 'bronn' + document.getElementById('lansenummer').value.toString()

    };

    var posting = $.post("test", data);

    posting.done(function (data) {
        window.content = $(data);
        sidedata = $(data);
        if (window.ktrykk == 1) { console.log('ikkekjør'); return 0}

        document.getElementById('temperatur').value = sidedata[0].lanse.temperatur.toString() + '℃';
        document.getElementById('vtrykk').value = sidedata[0].lanse.vtrykk.toString() + ' Bar';
        document.getElementById('lfukt').value = sidedata[0].lanse.luftfukt + '%';
        m_steg = sidedata[0].lanse.man_steg.toString();
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
    })
    return 0
}

if (window.kjoroppdater !== 1) {
    setTimeout(function () { setInterval(oppd_side, 4000) }, 500);
    window.kjoroppdater = 1;
}

function anbefaldyse() {

    /*	document.getElementById("dysevalg").value=anbefalingdyse;*/
    rh = Number(window.content[0].lanse.luftfukt);
    tdb = Number(window.content[0].lanse.temperatur);
    mbpressure = Number(window.content[0].lanse.ltrykk);

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
