$(document).ready(function() {
    var counter = 0;
    var prevrow = counter ;
    var objs = {"asset_items":[]};

   


    $("#addrow").on("click", function() {
        var newRow = $("<tr>");
        var cols = "";
        


        cols += '<td><input type="text" class="form-control" name="owner_driver_name_address_' + counter +'" id="owner_driver_name_address_'+counter+'" /></td>';
        cols += '<td><input type="text" class="form-control" name="reg_number_' + counter + '" id="reg_number_' + counter + '"/></td>';
        cols += '<td><input type="text" class="form-control" name="apparent_damage_' + counter + '" id="apparent_damage_' + counter + '"/></td>';
        cols += '<td><input type="text" class="form-control" name="insurers_and_policy_no_' + counter + '" id="insurers_and_policy_no_' + counter + '"/></td>';


        cols += '<td><input type="button" class="ibtnDel btn btn-md btn-danger "  value="Delete"></td>';
        newRow.append(cols);
        $("table.order-list").append(newRow);

  
        counter++;
     
        
    });


    // on done button click  add final row to array 
    $("#btnassetdone").on("click", function() {
        // check if add row is clicked

        var the_id;
        for (the_id = 0; the_id < counter; the_id++) {

            var obj = 
            {
                "asset_id" : the_id,
                "owner_driver_name_address" : $("#owner_driver_name_address_"+the_id).val() , 
                "reg_number" : $("#reg_number_"+the_id).val(),
                "apparent_damage" : $("#apparent_damage_"+the_id).val(),
                "insurers_and_policy_no" : $("#insurers_and_policy_no_"+the_id).val(),
                
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


z