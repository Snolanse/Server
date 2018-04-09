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

function leggtilknapper() {

    antknapper = document.getElementById("ant_steg").value;

    for (kslett = 0; kslett < stegvalgknapper.value; kslett++) {

        document.getElementById(kslett).remove();
        document.getElementById("mark" + kslett).remove();

    }

    for (iknapper = 0; iknapper < antknapper; iknapper++) {

        node = document.createElement("LI");
        node.setAttribute("id", "mark" + iknapper);
        node.setAttribute("name", "mark");

        stegvalgknapper = document.createElement("INPUT");
        stegvalgknapper.setAttribute("type", "radio");
        stegvalgknapper.setAttribute("name", "radiogruppe");
        stegvalgknapper.setAttribute("class", "radiogruppene");
        stegvalgknapper.setAttribute("value", iknapper + 1);
        stegvalgknapper.setAttribute("id", iknapper);

        nodelabel = document.createElement("LABEL");
        nodelabel.setAttribute("id", "container" + iknapper);
        nodelabel.setAttribute("class", "container");

        nodespan = document.createElement("SPAN");
        nodespan.setAttribute("id", "checkmark" + iknapper);
        nodespan.setAttribute("class", "checkmark");

        document.getElementById("tekstfelt").appendChild(node);
        document.getElementById("mark" + iknapper).appendChild(nodelabel);
        document.getElementById("container" + iknapper).appendChild(stegvalgknapper);
        document.getElementById("container" + iknapper).appendChild(nodespan);

        document.getElementById("container" + iknapper).innerHTML += "Steg nr. " + stegvalgknapper.value;

    }
}

function oppdatervalgtsteg() {
    steg = document.getElementsByName("radiogruppe");

    for (jsjekk = 0; jsjekk < steg.length; jsjekk++) {
        if (steg[jsjekk].checked == true) {
            valgtsteg = steg[jsjekk].value;
        }
    }
    document.getElementById("demo").innerHTML = "valgt steg: " + valgtsteg;
}

function automan() {

    hentstegknapper = document.getElementsByName("radiogruppe");

    if (document.getElementById("auto").checked === true ) {

        for (psjekk = 0; psjekk < hentstegknapper.length; psjekk++) {

            document.getElementById(psjekk).setAttribute("disabled", "disabled");

        }
    }
    if (document.getElementById("manuell").checked === true) {

        for (psjekk = 0; psjekk < hentstegknapper.length; psjekk++) {

            document.getElementById(psjekk).removeAttribute("disabled", "disabled");

        }
    }
}

function onload() {
    if (document.getElementById("auto").value === "True") { document.getElementById("auto").checked = true }
    if (document.getElementById("auto").value === "False") { document.getElementById("manuell").checked = true }
    automan()

}
setTimeout(onload, 0)


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