$(function() {
    $('a#create').on('click', function(e) {
      console.log("here")
      e.preventDefault()
      $.getJSON('/create_file',
          function(data) {
        //do nothing
      });
      return false;
    });
  });

  $(function() {
    $('a#delete').on('click', function(e) {
      console.log("here")
      e.preventDefault()
      $.getJSON('/delete_file',
          function(data) {
        //do nothing
      });
      return false;
    });
  });

  $(function() {
    $('a#email').on('click', function(e) {
      console.log("here")
      e.preventDefault()
      $.getJSON('/send_email',
          function(data) {
        //do nothing
      });
      return false;
    });
  });