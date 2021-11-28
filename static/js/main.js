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

      alert("Nice");
    });
  });

