console.log("working fine");

$("#commentForm").submit(function(e){
    e.preventDefault();

    $.ajax({
        data: $(this).serialize(),
        method: $(this).attr("method"),
        url : $(this).attr("action"),
        dataType : "json",


        success: function(response){
            console.log("comment saved to DB...");

            if(response.bool == true){
                $("#review-response").html("review added successfully.")

                

            }




        }
        })
})

// $("#commentForm").submit(function(element) {
//     element.preventDefault();

//     $.ajax({
//         data: $(this).serialize(),
//         method: $(this).attr("method"),
//         url: $(this).attr("action"),
//         dataType: "json",
//         success: function(response) {
//             console.log("comment saved to DB...");

//             if (response.bool == true) {
//                 $("#review-response").html("review added successfully.");
//             }
//         },
//         error: function(response) {
//             console.log("request failed:", response);
//             // Handle the error here
//         }
//     });
// });



