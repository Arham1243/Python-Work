<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {

    $from = $_POST['email'] ?? '';
    $subject = "Leads Brand Name";

    $name = $_POST['name'] ?? '';
    $referer = $_POST['referer'] ?? '';
    $email = $_POST['email'] ?? '';
    $number = $_POST['phone'] ?? '';
    $message_desc = $_POST['message'] ?? '';

    //begin of HTML message 
    $message = "
            <html> 
              <body> 
                <div>
                    <h4>Leads - Brand Name</h4><br>";
    if (isset($referer) && !empty($referer)) {
        $message .= "<b>Page URL:</b> " . $referer . "<br/>";
    }
    if (isset($name) && !empty($name)) {
        $message .= "<b>Name:</b> " . $name . "<br/>";
    }
    if (isset($email) && !empty($email)) {
        $message .= "<b>Email:</b> " . $email . "<br/>";
    }
    if (isset($number) && !empty($number)) {
        $message .= "<b>Phone: </b> " . $number . "<br/>";
    }
    if (isset($message_desc) && !empty($message_desc)) {
        $message .= "<b>Message: </b> " . $message_desc . "<br/>";
    }
    $message .= "<b>Date:</b> " . date('d-M-Y') . "<br/>";
    $message .= "<b>Day:</b> " . date('D') . "<br/>";


    $message .= "</div>";
    $message .= "</body>";
    $message .= "</html>";

    //end of message 
    $to = "info@test.com";
    $subject = 'Leads - Brand Name';

    $headers  = "From: admin@test.com\r\n";
    $headers .= "Reply-To: admin@test.com\r\n";
    $headers .= "Content-type: text/html\r\n";
    $headers .= 'X-Mailer: PHP/' . phpversion();

    // Send email
    $mailSent = mail($to, $subject, $message, $headers);
    // Save Data
    // $con = mysqli_connect("localhost", "brand_user", "12345678", "brand_db") or die('Not Connected');
    // $query = "INSERT INTO leads(ip, referer, name, email, phone, message) VALUES ('" . $ip . "','" . $referer . "','" . $name . "','" . $email . "','" . $number . "','" . $message_desc . "')";

    // $row = mysqli_query($con, $query);

    if ($mailSent) {
        $thank_you_url = "thank-you.php";
        header('location:' . $thank_you_url);
        exit(); // Exit to prevent further execution
    }
} else {
    // Form is not submitted via POST method
    header('location: index.php');
    exit();
}