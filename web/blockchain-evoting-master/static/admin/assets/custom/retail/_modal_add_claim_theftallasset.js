$(document).ready(function() {
    var counter = 0;
 
    var objs = {"asset_items":[]};

   


    $("#addrow").on("click", function() {
        var newRow = $("<tr>");
        var cols = "";
        


        cols += '<td><input type="text" class="form-control" name="item_' + counter +'" id="item_'+counter+'" /></td>';
        cols += '<td><input type="text" class="form-control" name="replacement_value_' + counter + '" id="replacement_value_' + counter + '"/></td>';


        cols += '<td><input type="button" class="ibtnDel btn btn-md btn-danger "  value="Delete"></td>';
        newRow.append(cols);
        $("table.order-list").append(newRow);


   
  
        counter++;
     

        
    });


    // on done button click  add final row to array 
    $("#btnassetdone").on("click", function() {

        var the_id;
        for (the_id = 0; the_id < counter; the_id++) {

            var obj = 
            {
                "asset_id" : the_id,
                "item" : $("#item_"+the_id).val() , 
                "replacement_value" : $("#replacement_value_"+the_id).val(),
            };

            objs['asset_items'].push(obj);
          
           
        }
        $("#asset_counter").val(JSON.stringify(objs))
        $('#btnaddasset').prop('disabled', true);
        
           
    });


    $("table.order-list").on("click", ".ibtnDel", function(event) {
        $(this).closest("tr").remove();
        counter -= 1
    });


});



