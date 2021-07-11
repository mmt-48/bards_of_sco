$(function() {
    $('audio').on('play', function() {
       $('audio').addClass('stoped').removeClass('playing');
        $(this).removeClass('stoped').addClass('playing');
        $('.stoped').each(function() {
            $(this).trigger('pause');
            $(this)[0].currentTime = 0;
        })
    })
})