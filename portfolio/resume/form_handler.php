<?php
// form_handler.php

// Start the session (if not already started)
session_start();

// Check if the form has been submitted
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    // Perform form validation (e.g., check required fields, email validity, etc.)

    // Check if the form has already been submitted (using a session flag)
    if (!isset($_SESSION["form_submitted"])) {
        // Process the form data and send the email

        // Set a flag to indicate that the form has been submitted
        $_SESSION["form_submitted"] = true;

        // Send the email and handle the form data
        // ...

        // Optionally, you can redirect the user to a "thank you" page after successful submission
        header("Location: thank_you_page.php");
        exit();
    } else {
        // The form has already been submitted, show a message or take appropriate action
        // ...
    }
}
?>
