// using jQuery get cookie
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

//set the header on AJAX request
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}






$(window).on('load', function () {
    //get session csrf cookie
    var csrftoken = getCookie('csrftoken');
    console.log(csrftoken)
    //update ajax header
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);

            }
        }
    });
    //post reuest to remove record and image from db
    $.ajax({
      type: 'POST',
      dataType: "html",
      url:'http://127.0.0.1:8000/imagecfr_app/delete/',
      success: function(){
        console.log("delete successful");
      },
      error: function(){
        console.log("delete failed");
      },
    });
});
