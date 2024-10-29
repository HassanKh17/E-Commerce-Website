// Function to open the overlay
function openOverlay(productId) {
    document.getElementById('overlay' + productId).style.display = 'flex';
}

// Function to close the overlay
function closeOverlay(productId) {
    document.getElementById('overlay' + productId).style.display = 'none';
}

// Event listener for the "Edit" buttons
document.addEventListener('DOMContentLoaded', function () {
    var editButtons = document.querySelectorAll('.btn-edit');

    editButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            // Extract the product ID from the 'data-product-id' attribute
            var productId = button.getAttribute('data-product-id');

            // Call the openOverlay function with the product ID
            openOverlay(productId);
        });
    });
});

// Function to handle sorting
function sortProducts(sortBy) {
    // Make an AJAX request to the Flask server with the sorting parameter
    $.ajax({
        url: '/sort_products',
        type: 'GET',
        data: { sort_by: sortBy },
        success: function (data) {
            $('body').html(data);
        }
    });
}

// Function to handle category filtering
function filterProductsByCategory() {
    var selectedCategory = $('#categoryFilter').val();

    // Make an AJAX request to the Flask server with the selected category
    $.ajax({
        url: '/filter_products',
        type: 'GET',
        data: { category_filter: selectedCategory },
        success: function (data) {
            $('body').html(data);
        }
    });
}
