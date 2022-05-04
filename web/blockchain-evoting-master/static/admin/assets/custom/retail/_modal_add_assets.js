$(document).ready(function() {
    var counter = 0;
   
    var objs = {"asset_items":[]};

   


    $("#addrow").on("click", function() {
        var newRow = $("<tr>");
        var cols = "";
        


        cols += '<td><input type="text" class="form-control" name="location_' + counter +'" id="location_'+counter+'" /></td>';
        cols += '<td><input type="text" class="form-control" name="buildings_' + counter + '" id="buildings_' + counter + '"/></td>';
        cols += '<td><input type="text" class="form-control" name="plant_' + counter + '" id="plant_' + counter + '"/></td>';
        cols += '<td><input type="text" class="form-control" name="furniture_' + counter + '" id="furniture_' + counter + '"/></td>';
        cols += '<td><input type="text" class="form-control" name="stock_' + counter + '" id="stock_' + counter + '"/></td>';

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
                "location" : $("#location_"+the_id).val() , 
                "buildings" : $("#buildings_"+the_id).val(),
                "plant" : $("#plant_"+the_id).val(),
                "furniture" : $("#furniture_"+the_id).val(),
                "stock" : $("#stock_"+the_id).val(),
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



