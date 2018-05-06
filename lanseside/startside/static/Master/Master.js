

//Skal justere på alle lansene
function Master_automan(automan) {
    window.oppd_tid = new Date().getTime()
    window.ktrykk = 0
    token = getCookie('csrftoken');
    data = {
        'csrfmiddlewaretoken': token,
        'auto_man_samtlige': automan
    };

    var posting = $.post("master", data);

    posting.done(function (data) {
        if (automan == 1) { alert("Alle lanser er satt i auto") }
        else if (automan == 0) { alert("Alle lanser er satt i manuell")}
    })

    posting.fail(function () {
        console.log('feil ved oppdatering av lanse')
        setTimeout(function () { alert("Ingen kontakt med server\nVennligst prøv på nytt") }, 1);
    })
    return 0

}