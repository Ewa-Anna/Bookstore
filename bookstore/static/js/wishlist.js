$(document).ready(function() {
    $(".wishlist-icon").click(function(e) {
        e.preventDefault();  
        
        var wishlistIcon = $(this);
        var bookId = $(this).data("bookid");

        $.ajax({
            type: "POST",
            url: "/wishlist/add_to_wishlist/",
            data: {
                bookid: bookId,
                csrfmiddlewaretoken: "{{ csrf_token }}"
            },

            success: function(data) {
                if (data.success) {
                    wishlistIcon.find("i").removeClass("fa-regular").addClass("fa-solid");
                } else {
                    console.error("Error adding/removing book to wishlist");
                }
            },
            error: function(error) {
                console.error("Error adding/removing book to wishlist", error);
            }
        });
    });
});