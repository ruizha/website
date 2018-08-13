const copyToClipboard = str => {
	const el = document.createElement('textarea');
	el.value = str;
	document.body.appendChild(el);
	el.select();
	document.execCommand('copy');
	document.body.removeChild(el);
    $(".fadeInOut").fadeTo(1, 1000, function () {
        $('.fadeInOut').css('visibility', 'visible');
    });
    $('.fadeInOut').fadeTo(1000, 0, function () {
        $('.fadeInOut').css('visibility', 'hidden');
    });
};

$(function () {
    $('#email').click(function () {
        copyToClipboard($('#email-text').text());
    });
});
