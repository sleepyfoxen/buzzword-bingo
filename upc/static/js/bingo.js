
$('item').click(function() {
    let elem = this;
    let buzz = this.childNodes[3].innerText;

    if ($(this).hasClass('score')) {
        $(this).removeClass('score');
        return;
    }
    else
        $(this).addClass('score');

    console.log(buzz);

    $.get('/click/' + buzz, data => {
        console.log(data);
        elem.childNodes[1].innerText = data;
    });

    
});