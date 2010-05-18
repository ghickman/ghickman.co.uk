$(function() {
    /**
     * Slide takes the selector for one element in the side bar
     * For example .categories
     */
    function slide(selector) {
        $(selector + '.sidebar_title').click(function() {
            if($(selector + '.sidebar_title').hasClass('hidden')) {
                $(selector + '.sidebar_content').slideDown()
                $(selector + '.sidebar_title')
                    .removeClass('hidden')
                    .css('border-bottom', 'none')
                    .css('border-bottom-left-radius', '0px')
                    .css('border-bottom-right-radius', '0px')
            } else {
                $(selector + '.sidebar_content').slideUp()
                
                // this needs to wait for slideUp to finish.
                $(selector + '.sidebar_title')
                    .addClass('hidden')
                    .css('border-bottom', '1px solid black')
                    .css('border-bottom-left-radius', '7px')
                    .css('border-bottom-right-radius', '7px')
            }
        });
    }
    
    slide('.categories')
    slide('.archives')
    slide('.twitter')
    
    
    // $('.outer').click(function () {
        // id = $('.outer').getClass()
        // if($('ul.inner').hasClass('hidden')) {
        //     $('ul.inner').slideDown()
        //     $('')
        // }
    
        //grab id of li.outer and compare to ul.inner's id
});