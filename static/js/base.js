$(function () {
    $('.navbar-item-element').click(function () {
        window.location.href = $(this).attr('uri');
    });
});
