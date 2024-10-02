// Wait for the DOM to fully load before executing the script
document.addEventListener('DOMContentLoaded', function() {
    // Select the prefill button using its ID
    const prefillButton = document.getElementById('prefill-btn');

    // Check if the prefill button exists (if the user has access)
    if (prefillButton) {
        // Add a click event listener to the prefill button
        prefillButton.addEventListener('click', function() {
            // Get the data attributes from the button
            const fullName = prefillButton.getAttribute('data-fullname');
            const email = prefillButton.getAttribute('data-email');
            const phone = prefillButton.getAttribute('data-phone');
            const address = prefillButton.getAttribute('data-address');

            // Fill the form fields with the user's profile information
            document.getElementById('full_name').value = fullName;
            document.getElementById('email').value = email;
            document.getElementById('phone').value = phone;
            document.getElementById('address').value = address;
        });
    }
});