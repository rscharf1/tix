$(function() {
    $('#submit').on('click', function(e) {
      console.log("tix")
        var data = {
            "email": $("#email").val(),
            "home": $("#home").val(),
            "opponent": $("#opponent").val(),
            "date": $("#date").val(),
            "time": $("#time").val(),
            "section": $("#section").val(),
            "row": $("#row").val(),
            "seat": $("#seat").val(),
            "entry": $("#entry").val()
        }

      $.ajax({
        type: "POST",
        url: "/make_tix",
        data: JSON.stringify(data),
        contentType: "application/json",
        dataType: 'json' 
      });
    });
  });

$(function() {
    $('a#create').on('click', function(e) {
      console.log("create")
      e.preventDefault()
      $.getJSON('/create_file',
          function(data) {
        //do nothing
      });
      return false;
    });
  });

  $(function() {
    $('a#delete').on('delete', function(e) {
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
    $('a#send-email').on('email', function(e) {
      console.log("here")
      e.preventDefault()
      $.getJSON('/send_email',
          function(data) {
        //do nothing
      });
      return false;
    });
  });

