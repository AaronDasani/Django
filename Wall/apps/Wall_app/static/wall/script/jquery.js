



$(document).ready(function () {

    $(".replies").hide();

    $(".viewButton").click(function () {
        // $(this).next('.replies').slideToggle("slow");
        $(this).next().next('.replies').slideToggle();

        

    })
   
    $(".postCom").hide();

    $(".viewPostElement").click(function () {
        // $(this).next('.replies').slideToggle("slow");
        $(this).next().next('.postCom').slideToggle();

        

    })
})