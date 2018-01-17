$(function () {
    $('.navbar-item-element').click(function () {
        window.location.href = $(this).attr('uri');
    });
});

$(function () {
    $('.text-link').click(function () {
        if (!$(this).attr('class').includes('deactivate')) {
            window.location.href = $(this).attr('uri');
        }
    });

    $('.link-nt').click(function () {
        if (!$(this).attr('class').includes('deactivate')) {
            let win = window.open($(this).attr('uri'), '_blank');
            win.focus();
        }
    });
});
