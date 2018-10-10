



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

    $(".editPasswordSection").hide();

    $("#passswordButton").click(function(){
        $(".editInfoSection").hide();
        $(".editPasswordSection").show("slide",{ direction: "right" });
    })
    $("#editButton").click(function(){

        $(".editInfoSection").show("slide");
        $(".editPasswordSection").hide();

    })
})