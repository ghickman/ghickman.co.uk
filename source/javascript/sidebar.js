$(function() {
    $('a.categories').click(function() {
        if($('a.categories').hasClass('hidden')) {
            $('div.categories').slideDown()
            $('a.categories').removeClass('hidden')
        } else {
            $('div.categories').slideUp()
            $('a.categories').addClass('hidden')
            // add a bottom border AFTER the slideUp event.
            $('div.categories').css('border-bottom: 1px solid black')
        }
    });

    $('a.archives').click(function() {
        if($('a.archives').hasClass('hidden')) {
            $('div.archives').slideDown()
            $('a.archives').removeClass('hidden')
        } else {
            $('div.archives').slideUp()
            $('a.archives').addClass('hidden')
        }
    });

    $('a.twitter').click(function() {
        if($('a.twitter').hasClass('hidden')) {
            $('div.twitter').slideDown()
            $('a.twitter').removeClass('hidden')
        } else {
            $('div.twitter').slideUp()
            $('a.twitter').addClass('hidden')
        }
    });
});