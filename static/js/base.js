$(function () {
    if ($(window).width() < 1200) { // janky attempt to cater to mobile users
        $('body').css('width', '95%');
        $('body').css('padding', '20px');
    }
    $('.link-nt').click(function () {
        if (!$(this).attr('class').includes('deactivate')) {
            let win = window.open($(this).attr('uri'), '_blank');
            win.focus();
        }
    });
});
