// FIX GLOBAL para el TOKEN en las peticiones ajaxs
function getCookie(name)
{
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

$.ajaxSetup({
     beforeSend: function(xhr, settings) {
         // doing_ajax(true);
         if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
             // Only send the token to relative URLs i.e. locally.
             xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
         }
     },
     complete: function () {
         // doing_ajax(false);
    }
});

function doing_ajax(start) {
    if(start) {$.LoadingOverlay("show");}
    else {$.LoadingOverlay("hide");}
}

function checkboxChange(key, checkbox) {
    attr_id = $(checkbox).attr('id');
    check_id = key + "." + attr_id.substr(2);
    //$('input[name="' + key + '.' + checkbox.attr(id) + '"]').val($(checkbox).is(':checked') ? 'on' : 'off');
    $("input[id='" + check_id + "']").val($(checkbox).is(':checked') ? 'on' : 'off');
    return $("input[id='" + check_id +"']");
};


$(function() { // DOM Ready
    $('form').submit(function() {
       $.LoadingOverlay("show");
       return true;
    });
    $('[data-toggle="tooltip"]').tooltip();
});
