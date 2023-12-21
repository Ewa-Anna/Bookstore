function toggleCart(bookid) {
    const form = document.createElement("form");
    form.action = `/cart/toggle/${bookid}/`;
    form.method = "post";

    const csrfInput = document.createElement("input");
    csrfInput.type = "hidden";
    csrfInput.name = "csrfmiddlewaretoken";
    csrfInput.value = csrfToken; 
    
    const quantityInput = document.createElement("input");
    quantityInput.type = "hidden";
    quantityInput.name = "quantity";
    quantityInput.value = 1; 

    form.appendChild(csrfInput);
    form.appendChild(quantityInput);
    
    document.body.appendChild(form);
    form.submit();
}

const cartIcons = document.querySelectorAll(".cart-icon");
cartIcons.forEach(cartIcon => {
    cartIcon.addEventListener("click", () => {
        const bookid = cartIcon.getAttribute("data-bookid");
        toggleCart(bookid);

        const iconElement = cartIcon.querySelector("i");
        iconElement.classList.toggle("fa-basket-shopping");
        iconElement.classList.toggle("fa-check");
    });
});
