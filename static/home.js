$(document).ready(() => {
    let led_status = false; // false -> off, true -> on
    $("#switch-btn").click(function(){
        if(led_status){
            // Turn OFF
            $.ajax({
                url: "/turn-off",
                method: "post"
            }).done((data) => {
                if(data.status == "success"){
                    led_status = false;
                    $("#switch-btn").text("Turn ON").removeClass("btn-on").addClass("btn-off");
                }
            });
        }
        else{
            // Turn ON
            $.ajax({
                url: "/turn-on",
                method: "post"
            }).done((data) => {
                if(data.status == "success"){
                    led_status = true;
                    $("#switch-btn").text("Turn OFF").removeClass("btn-off").addClass("btn-on");
                }
            });
        }
    });
});