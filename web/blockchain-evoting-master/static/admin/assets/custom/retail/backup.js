$(document).ready(function() {
    var counter = 0;
    var prevrow = counter ;
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


        // add previous row to json
        prevrow = counter-1 ;

        if(prevrow != -1) {
            var obj = 
            {
                "asset_id" : prevrow,
                "location" : $("#location_"+prevrow).val() , 
                "buildings" : $("#buildings_"+prevrow).val(),
                "plant" : $("#plant_"+prevrow).val(),
                "furniture" : $("#furniture_"+prevrow).val(),
                "stock" : $("#stock_"+prevrow).val(),
            };

            objs['asset_items'].push(obj);
        }

  
        counter++;
        // assign latest value to counter
 
        $("#asset_counter").val(JSON.stringify(objs))
        console.log($("#asset_counter").val()) ;

        
    });


    // on done button click  add final row to array 
    $("#btnassetdone").on("click", function() {
        // check if add row is clicked
        if(prevrow != counter){
            var newval = counter-1
            var obj = 
            {
                "asset_id" : newval,
                "location" : $("#location_"+newval).val() , 
                "buildings" : $("#buildings_"+newval).val(),
                "plant" : $("#plant_"+newval).val(),
                "furniture" : $("#furniture_"+newval).val(),
                "stock" : $("#stock_"+newval).val(),
            };

            objs['asset_items'].push(obj);
            // disable add assets button untill reload
            $('#btnaddasset').prop('disabled', true);
            console.log(counter);
        }
        
           
    });


    $("table.order-list").on("click", ".ibtnDel", function(event) {
        $(this).closest("tr").remove();
        counter -= 1
    });


});



function calculateRow(row) {
    var price = +row.find('input[name^="price"]').val();

}

function calculateGrandTotal() {
    var grandTotal = 0;
    $("table.order-list").find('input[name^="price"]').each(function() {
        grandTotal += +$(this).val();
    });
    $("#grandtotal").text(grandTotal.toFixed(2));
}