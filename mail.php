<?php
if ($_SERVER["SERVER_NAME"] == "okina.herokuapp.com") {
	header("HTTP/1.1 301 Moved Permanently");
	header("Location: http://www.seimei.asia" . $_SERVER[REQUEST_URI]);
} else {
	header('Content-type: text/html; charset=utf-8;');
}

// 指定されたサーバー環境変数を取得する
function getServer($key, $default = null)
{
	return (isset($_SERVER[$key])) ? $_SERVER[$key] : $default;
}

// クライアントのIPアドレスを取得する
function getClientIp($checkProxy = true)
{
	/*
	 *  プロキシサーバ経由の場合は、プロキシサーバではなく
	*  接続もとのIPアドレスを取得するために、サーバ変数
	*  HTTP_CLIENT_IP および HTTP_X_FORWARDED_FOR を取得する。
	*/
	if ($checkProxy && getServer('HTTP_CLIENT_IP') != null) {
		$ip = getServer('HTTP_CLIENT_IP');
	} else if ($checkProxy && getServer('HTTP_X_FORWARDED_FOR') != null) {
		$ip = getServer('HTTP_X_FORWARDED_FOR');
	} else {
		// プロキシサーバ経由でない場合は、REMOTE_ADDR から取得する
		$ip = getServer('REMOTE_ADDR');
	}
	return $ip;
}

require 'vendor/autoload.php';
date_default_timezone_set('JST');
?>
<html>
<head>
<meta http-equiv="refresh" content="5;URL=/"></head>
<body>
<?php
if (hash("haval160,4", $_POST["authcode"]) == $_POST["authcode-hash"]) {
	$sendgrid = new SendGrid('app26677709@heroku.com', 'xec1eqoo');
	$message = new SendGrid\Email();
	$message->
		addTo('nakamuramasakatsu+heroku@gmail.com')->
		setFrom($_POST['email'])->
		setSubject('[あじあ姓名うらない]' . $_POST['subject'])->
		setText('あじあ姓名うらないに問い合わせがありました。' . PHP_EOL . PHP_EOL . 
				'IPアドレス: ' . getClientIp() . PHP_EOL . 
				'サーバー時刻: ' . date('c') . PHP_EOL . PHP_EOL .
				'メールアドレス: ' . $_POST['email'] . PHP_EOL .
				'サブジェクト: ' . $_POST['subject'] . PHP_EOL . PHP_EOL .
				'問い合わせ内容:' . PHP_EOL . $_POST['query-content']);
	$response = $sendgrid->send($message);
?>
問い合わせを送信しました。
</body>
</html>
<?php
} else {
?>
<body>
認証コードが違います。
</body>
</html>
