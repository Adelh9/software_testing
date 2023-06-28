$(document).ready(function() {
        $('form').submit(function(event) {
          event.preventDefault();
          $.ajax({
            url: '/solve',
            type: 'POST',
            data: $('form').serialize(),
            success: function(response) {
              $('#result').empty();
              $.each(response.result, function(index, value) {
                $('#result').append('<li>' + value + '</li>');
              });
            }
          });
        });
      });