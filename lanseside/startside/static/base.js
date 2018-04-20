//document.getElementById("hjem").setAttribute("class", 'notactive');
//document.getElementById("lanse").setAttribute("class", 'notactive');
//document.getElementById("info").setAttribute("class", 'notactive');

setTimeout(pressknapp, 20);

/*Markerer hvilken side man er på*/
function pressknapp() {
    document.getElementById(document.getElementById("tittel").innerHTML).setAttribute("class", 'active');
}

/*Henter cookie*/
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Starter stringen til cookien med navnet vi vil ha
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
