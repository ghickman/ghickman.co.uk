jQuery(document).ready(function($) {
  /**
   * Slide takes the selector for one element in the side bar
   * For example .categories
   */
  function slide(selector) {
    $(selector + '.sidebar_title').click(function() {
      if($(selector + '.sidebar_title').hasClass('hidden')) {
        $(selector + '.sidebar_content').slideDown();
        $(selector + '.sidebar_title').removeClass('hidden');
      } else {
        $(selector + '.sidebar_content').slideUp('slow', function() {
          $(selector + '.sidebar_title').addClass('hidden');
        });
      }
    });
  }

  slide('.categories');
  slide('.archives');
  slide('.linkroll');
  slide('.blogroll');
  slide('.twitter');
});
