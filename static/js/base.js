$(function () {
    const isMobile = /iphone|ipad|ipod|android/i.test(navigator.userAgent.toLowerCase());
    const origWidth = $('body').css("width");
    const origPadding = $('body').css("padding");
    $(window).resize(() => {
        if (($(window).width() < 1000) || isMobile) { // janky attempt to cater to mobile users
            console.log("Resizing...");
            $('body').css('width', '95%');
            $('body').css('padding', '20px');
        } else if (!isMobile)  {
            console.log("Resizing orig...");
            $('body').css('width', origWidth);
            $('body').css("padding", origPadding);
        }
    });
});
