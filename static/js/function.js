console.log("working fine");

const monthNames = [
    "Jan", "Feb", "Mar", "April", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"
];

$("#commentForm").submit(function(e){
    e.preventDefault();
    
    let dt = new Date();
    let time = dt.getDay() + " " + monthNames[dt.getUTCMonth()] + ", " + dt.getFullYear()
    
    $.ajax({
        data: $(this).serialize(),
        method: $(this).attr("method"),
        url : $(this).attr("action"),
        dataType : "json",


        success: function(res){
            console.log("comment saved to DB...");

            if(res.bool == true){
                
                $("#review-response").html(".نظر شما با موفقیت ثبت شد");
                $(".hide-comment-form").hide();

                let _html = '<div class="col-md-6 comment-list">'
                    _html +='<div class="media mb-4">'
                    _html +='<img src="https://pixabay.com/vectors/blank-profile-picture-mystery-man-973460/" alt="Image" class="img-fluid mr-3 mt-1" style="width: 45px;">'
                    _html +='<div class="media-body">'
                    _html +='<h6>'+ res.context.user +'<small> - <i>'+ time +'</i></small></h6>'
                    
                    
                    for(let i = 1; i <= res.context.rating; i++ ){
                        _html += '<i class="fas fa-star text-warning"></i>'
                    }
                    _html +='<p>'+ res.context.review +'</p>'
                    

                    _html +='</div>'

                    _html +='</div>'
                    _html +='</div>'
            
                    $(".comment-list").prepend(_html)
                

                }
                




        }
        })
})


$(document).ready(function (){
    $(".filter-checkbox").on("click", function(){
        console.log("a checkbox have been clicked");

        let filter_object = {}

        $(".filter-checkbox").each(function(){
            let filter_value = $(this).val()
            let filter_key = $(this).data("filter")
            
            

            filter_object[filter_key] = Array.from(document.querySelectorAll('input[data-filter=' + filter_key + ']:checked')).map(function(element){
                return element.value
            })

        })

        console.log("filter object is", filter_object);

        $.ajax({
            url: '/filter-products',
            data: filter_object,
            dataType: 'json',
            beforeSend: function(){
                console.log("trying to filter product...");
            },
            success: function(response){
                console.log(response);
                console.log("data filtered successfully...")
                $("#filtered-product").html(response.data)
            }
        })
    })

})


// add to cart btn
$(".add-to-cart-btn").on("click", function(){

    let this_val = $(this)
    let index = this_val.attr("data-index")


    let quantity = $(".product-quantity-" + index).val()
    let product_title = $(".product-title-" + index).val()
    let product_id = $(".product-id-" + index).val()
    let product_price = $(".current-product-price-" + index).text()
    let product_pid = $(".product-pid-" + index).val()
    let product_image = $(".product-image-" + index).val()

    console.log("Quantity:", quantity);
    console.log("Title:", product_title);
    console.log("Price:", product_price);
    console.log("ID:", product_id);
    console.log("PID:", product_pid);
    console.log("Image:", product_image);
    console.log("Index:", index);

    console.log("Current Element:", this_val);


    $.ajax({

        url: '/add-to-cart',
        data: {
            'id' : product_id,
            'pid' : product_pid,
            'image' : product_image,
            'qty' : quantity,
            'title' : product_title,
            'price' : product_price,

        },
        dataType: 'json',
        beforeSend: function(){
            console.log("adding product to cart...");
        },
        success: function(response){
            this_val.html("✔")
            console.log("added product to cart!");
            $(".cart-items-count").text(response.totalcartitems)
            
        }
    })


})

// // add to cart btn
// $("#add-to-cart-btn").on("click", function(){
//     let quantity = $("#product-quantity").val()
//     let product_title = $(".product-title").val()
//     let product_id = $(".product-id").val()
//     let product_price = $("#current-product-price").text()
//     let this_val = $(this)

//     console.log("Quantity:", quantity);
//     console.log("Title:", product_title);
//     console.log("Price:", product_price);
//     console.log("ID:", product_id);
//     console.log("Current Element:", this_val);


//     $.ajax({

//         url: '/add-to-cart',
//         data: {
//             'id' : product_price,
//             'qty' : quantity,
//             'title' : product_title,
//             'price' : product_price,

//         },
//         dataType: 'json',
//         beforeSend: function(){
//             console.log("adding product to cart...");
//         },
//         success: function(response){
//             this_val.html("item addet to cart")
//             console.log("added product to cart!");
//             $(".cart-items-count").text(response.totalcartitems)
            
//         }
//     })

