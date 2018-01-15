$(function () {
    $('.text-link').click(function () {
        console.log($(this).attr('uri'));
        window.location.href = $(this).attr('uri');
    });
});
