function restartUpdate() {
    console.log("restartUpdate");
    if(! $("#restart_widget .inner").is(":hidden")) {
        $("#restart_widget #last_modified").load(restart_widget_updated);
    }
}

function showHide(event) {
    if($("#restart_widget .inner").is(":hidden")) {
        console.log("hidden");
        $("#restart_widget i").removeClass("icon-chevron-up");
        $("#restart_widget i").addClass("icon-chevron-down");
    } else {
        console.log("showing");
        $("#restart_widget i").removeClass("icon-chevron-down");
        $("#restart_widget i").addClass("icon-chevron-up");
    }
    $('#restart_widget .inner').slideToggle();
    event.preventDefault();
}

function restart(element, event) {
    if (! $(element).attr('restarting')) {
        try {
            var jqxhr = $.ajax({
                    url: restart_widget_call,
                    beforeSend: function() {
                        $("#restart_link").attr("restarting","restarting");
                        $("#restart_link").addClass("disabled");
                        $("#restart_link").html("restarting...");
                    }
                }).done(function(data) {
                    console.log( "success" );
                    $("#restart_widget #last_modified").html(data['last_modified']);
                    console.log(data);
                }).fail(function() {
                    console.log( "error" );
                }).always(function() {
                    console.log( "complete" );
                    $("#restart_link").removeClass("disabled");
                    $("#restart_link").removeAttr("restarting");
                    $("#restart_link").html("restart server");
            });
        }
        catch(err) {
            var jqxhr = $.ajax({
                    url: restart_widget_call,
                    beforeSend: function() {
                        $("#restart_link").attr("restarting","restarting");
                        $("#restart_link").addClass("disabled");
                        $("#restart_link").html("restarting...");
                    },
                    success: function(data){
                        console.log( "success" );
                        $("#restart_widget #last_modified").html(data['last_modified']);
                        console.log(data);
                    },
                    error: function(){
                        console.log( "error" );
                    },
                    complete: function(){
                        console.log( "complete" );
                        $("#restart_link").removeClass("disabled");
                        $("#restart_link").removeAttr("restarting");
                        $("#restart_link").html("restart server");
                    },
            });
        }
    }
}

$(document).ready(function() {
    // Create the container to load the AJAX request
    var base_div = $("<div id='restart_widget'></div>");
    $("body").append(base_div);
    $( "#restart_widget" ).load(restart_widget_url);
    console.log("done");
    
    // Show and hide the widget
    try {
        $("#restart_widget" ).on("click", "#toggle", function(event) {
            showHide(event);
        });
    }
    catch(err) {
        // Depricated old jQuery code
        $("#restart_widget #toggle").live("click", function(event) {
            showHide(event);
        });
    }
    
    // AJAX request for a server restart
    try {
        $("#restart_widget" ).on("click", "#restart_link", function(event) {
            restart(this, event);
        });
    }
    catch(err) {
        // Depricated old jQuery code
        $("#restart_widget #restart_link").live("click", function(event) {
            restart(this, event);
        });
    }
    
    // Continusly update the date the server was last restarted
    // will call refreshPartial every 3 seconds
    setInterval(restartUpdate, 3000);
});