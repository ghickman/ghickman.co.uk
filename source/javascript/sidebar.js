$(function() {
    $('.categories.sidebar_title').click(function() {
        if($('.categories.sidebar_title').hasClass('hidden')) {
            $('.categories.sidebar_content').slideDown()
            $('.categories.sidebar_title').removeClass('hidden')
        } else {
            $('.categories.sidebar_content').slideUp()
            $('.categories.sidebar_title').addClass('hidden')
        }
    });

    $('.archives.sidebar_title').click(function() {
        if($('.archives.sidebar_title').hasClass('hidden')) {
            $('.archives.sidebar_content').slideDown()
            $('.archives.sidebar_title').removeClass('hidden')
        } else {
            $('.archives.sidebar_content').slideUp()
            $('.archives.sidebar_title').addClass('hidden')
        }
    });

    $('.twitter.sidebar_title').click(function() {
        if($('.twitter.sidebar_title').hasClass('hidden')) {
            $('.twitter.sidebar_content').slideDown()
            $('.twitter.sidebar_title').removeClass('hidden')
        } else {
            $('.twitter.sidebar_content').slideUp()
            $('.twitter.sidebar_title').addClass('hidden')
        }
    });
});