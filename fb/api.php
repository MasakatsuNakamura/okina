<?php
if ($_SERVER["SERVER_NAME"] == "okina.herokuapp.com") {
	header("HTTP/1.1 301 Moved Permanently");
	header("Location: http://www.seimei.asia" . $_SERVER[REQUEST_URI]);
} elseif ($_SERVER["SERVER_NAME"] != "www.seimei.asia") {
	header("HTTP/1.1 400 Bad Request");
	header("Location: http://www.seimei.asia/");
} else {
	header('Content-type: application/json; charset=utf-8;');
}

date_default_timezone_set('UTC');

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

require '../vendor/autoload.php';
require '../php/seimei.php';
require '../php/reii.php';
require '../php/kenkou.php';
require '../php/seikaku.php';
require '../php/meimei.php';
require '../php/kanji.php';

$seimei = New Seimei();
$seimei->sei = $_POST['sei'];
$seimei->mei = $_POST['mei'];
$seimei->sex = $_POST['sex'];
$seimei->shindan();

echo json_encode(
	Array(
		'tenkaku' => $seimei->tenkaku,
		'jinkaku' => $seimei->jinkaku,
		'chikaku' => $seimei->chikaku,
		'gaikaku' => $seimei->gaikaku,
		'soukaku' => $seimei->soukaku,
		'seikaku' => $seimei->seikaku,
		'kenkou' => $seimei->kenkou,
		'error' => $seimei->error,
		'jinshimo' => $seimei->jinshimo,
		'tenkaku-mongon' => $seimei->mongon('tenkaku'),
		'chikaku-mongon' => $seimei->mongon('chikaku'),
		'gaikaku-mongon' => $seimei->mongon('gaikaku'),
		'soukaku-mongon' => $seimei->mongon('soukaku'),
		'jinkaku-mongon' => $seimei->mongon('jinkaku'),
		'seikaku-mongon' => $seimei->mongon('seikaku'),
		'ip' => getClientIp()
	)
);
