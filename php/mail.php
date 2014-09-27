<?php
header('Content-type: text/html; charset=utf-8;');
require 'vendor/autoload.php';
$sendgrid = new SendGrid(process.env.SENDGRID_USERNAME, process.env.SENDGRID_PASSWORD);

$message = new SendGrid\Email();
$message->addTo('nakamuramasakatsu+heroku@gmail.com')->
setFrom($_POST['email'])->
setSubject('Query from seimei.asia')->
setText($_POST['email'] . "\n" . $_POST['query']);
$response = $sendgrid->send($message);
?>
<meta http-equiv="refresh" content="0;URL=/">
