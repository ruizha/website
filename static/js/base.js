$(function () {
    $('.link-nt').click(function () {
        if (!$(this).attr('class').includes('deactivate')) {
            let win = window.open($(this).attr('uri'), '_blank');
            win.focus();
        }
    });
});
