$(document).ready(function() {
    $("#wishlist-icon").click(function(e) {
         
        var bookId = $(this).data("bookid");
        var csrfToken = $(this).data("csrf");

        $.ajax({
            type: "POST",
            url: "/wishlist/add_to_wishlist/",
            headers: {
                "X-CSRFToken": csrfToken
            },
            data: {
                bookid: bookId,
                csrfmiddlewaretoken: csrfToken,
            },
            crossDomain: true,
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