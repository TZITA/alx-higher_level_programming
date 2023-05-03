$('DIV#toggle_header').on('click', function () {
  if ($('header').hasClass('red')) { $('header').html('<header class="green"> First HTML page </header>'); } else { $('header').html('<header class="red"> First HTML page </header>'); }
});
