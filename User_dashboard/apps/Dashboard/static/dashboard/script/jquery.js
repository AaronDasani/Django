$(document).ready(function () {


    $("#Delete").on('show.bs.modal',function(event){

        button=$(event.relatedTarget)
        user_id=button.data('userid')
 
        modal=$(this)
        $(this).find(".modal-body #user_id").val(user_id);


    })


})