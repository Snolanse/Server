function last_lansedata() {       //henter inn data om lanser
    token = getCookie('csrftoken');
    data = {
        'csrfmiddlewaretoken': token,
        'bronnid': 'samtlige'
    };
    var posting = $.post("info", data);

    posting.done(function (data) {      //plasserer hentet data ut på nettsiden
        var content = $(data);
        //console.log(content)
        console.log('data har blitt lastet')
        oppd_data(content);
        setTimeout(last_lansedata,1000)
    })

    posting.fail(function () {
        console.log('feil ved henting av data')
        setTimeout(function () { alert("Ingen kontakt med server\nTrykk ok for å prøve på nytt") }, 1); 
        setTimeout(last_lansedata, 3000)
    })
}

function oppd_data(content) {
    for (var i = 0; i < 27; i++) {
        
        document.getElementById("lansenrlanse" + (i + 1).toString()).innerHTML = "Lanse ID: " + content[0][i].id.toString()
        document.getElementById("lufttemplanse" + (i + 1).toString()).innerHTML = "Temperatur: " + content[0][i].temperatur_luft.toString()
        document.getElementById("relativhlanse" + (i + 1).toString()).innerHTML = "Relativ luftfuktighet: " + content[0][i].luftfukt.toString()
        document.getElementById("flowlanse" + (i + 1).toString()).innerHTML = "Flow: " + content[0][i].flow.toString()
        document.getElementById("trykklanse" + (i + 1).toString()).innerHTML = "Trykk: " + content[0][i].vanntrykk.toString()
        document.getElementById("valgtstegnrlanse" + (i + 1).toString()).innerHTML = "Valgt steg: " + content[0][i].modus.toString()

        if ((new Date().getTime() - (content[0][i].timestamp*1000)) > (20 * 1000)) {
            document.getElementById("oversiktlanse" + (i+1).toString()).style.background = "#F56666";
        }
        else {
            document.getElementById("oversiktlanse" + (i + 1).toString()).style.background = "white";
        }

    }
}

setTimeout(last_lansedata,100)