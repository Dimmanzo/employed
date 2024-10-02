// Wait for the DOM to fully load before executing the script
document.addEventListener('DOMContentLoaded', function() {
    // Select the prefill button using its ID
    const prefillButton = document.getElementById('prefill-btn');

    // Check if the prefill button exists (if the user has access)
    if (prefillButton) {
        // Add a click event listener to the prefill button
        prefillButton.addEventListener('click', function() {
            // Fill the form fields with the user's profile information
            document.getElementById('full_name').value = '{{ user.profile.full_name }}';
            document.getElementById('email').value = '{{ user.profile.email }}';
            document.getElementById('phone').value = '{{ user.profile.phone }}';
            document.getElementById('address').value = '{{ user.profile.address }}';
        });
    }
});