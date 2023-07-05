$(document).ready(function() {
  $('.section-link').click(function(event) {
    event.preventDefault();
    var sectionTitle = $(this).data('section-title');
    var paragraphSet = $(this).data('paragraph-set');

    $('#section-text-container').text(sectionTitle);
    $('#sidebar-section-title').addClass('bg-sky-100')
    

    for (let i = 0; i < paragraphSet.length; i++) {
      $('#section-text-container').append(paragraphSet[i]);
    }
    
    
  });
});
