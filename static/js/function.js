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
    
    
    $(".delete-product").on("click", function(){

        let product_id = $(this).attr("data-product")
        let this_val = $(this)


        console.log("Product Id:" , product_id);
        $.ajax({
            url: "/delete-from-cart",
            data: {
                "id": product_id
            },
            dataType: "json",
            beforeSend: function(){
                this_val.hide()
            },
            success: function(response){
                this_val.show()
                $(".cart-items-count").text(response.totalcartitems)
                $("#cart-list").html(response.data)
            }
        })
    
    })



    $(".update-product").on("click", function(){

        let product_id = $(this).attr("data-product")
        let this_val = $(this)
        let product_quantity = $(".product-qty-"+product_id).val()

        console.log("Product Id:" , product_id);
        console.log("Product qty:" , product_quantity);

        $.ajax({
            url: "/update-cart",
            data: {
                "id": product_id,
                "qty": product_quantity,
            },
            dataType: "json",
            beforeSend: function(){
                this_val.hide()
            },
            success: function(response){
                this_val.show()
                $(".cart-items-count").text(response.totalcartitems)
                $("#cart-list").html(response.data)
            }
        })
    
    })


    // making default adresses
    $(document).on("click", ".make-default-adress", function(){
        let id = $(this).attr("data-adress-id")
        let this_val = $(this)

        console.log("id is:", id);
        console.log("element is:", this_val);

        $.ajax({
            url: "/make-default-adress",
            data: {
                "id":id
            },
            dataType: "json",
            success: function(response){
                console.log("adress made default...");
                if (response.boolean == true){
                    $(".check").hide()
                    $(".action_btn").show()

                    $(".check"+id).show()
                    $(".button"+id).hide()

                }
            }
        })
    })

    $(document).on("submit", "#contactFormajax", function(e){
        e.preventDefault()
        console.log("submited...");

        let full_name = $("#full_name").val()
        let email = $("#email").val()
        let phone = $("#phone").val()
        let subject = $("#subject").val()
        let message = $("#message").val()

        console.log("name:", full_name);
        console.log("name:", email);
        console.log("name:", phone);
        console.log("name:", subject);
        console.log("name:", message);

        $.ajax({
            url: "/ajax-contact-form",
            data: {
                "full_name": full_name,
                "email": email,
                "phone": phone,
                "subject": subject,
                "message": message,
            },
            dataType:"json",
            beforeSend: function(){
                console.log("sending data to server...");
            },
            success: function(res){
                console.log("sent data to server");
                $("#contactFormajax").hide()
                $("#message-response").html(".نظر با موفقیت ارسال شد")
            }
        })
    })
    
})


