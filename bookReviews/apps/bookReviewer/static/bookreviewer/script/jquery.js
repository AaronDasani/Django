

$(document).ready(function () {

    $(".reviewForm").hide();

    $("#addReview").click(function () {
        
        $(this).parent().next().next(".reviewForm").slideToggle();

    })
   
 
})