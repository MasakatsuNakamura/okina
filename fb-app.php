<?php
header('Content-type: text/html; charset=utf-8;');

date_default_timezone_set('Asia/Tokyo');

require 'vendor/autoload.php';

require 'php/seimei.php';
require 'php/reii.php';
require 'php/kenkou.php';
require 'php/seikaku.php';
require 'php/meimei.php';
require 'php/kanji.php';
require 'php/snipets.php';

use Facebook\FacebookSession;
use Facebook\FacebookRedirectLoginHelper;
use Facebook\FacebookCanvasLoginHelper;
use Facebook\FacebookRequest;
use Facebook\FacebookResponse;
use Facebook\FacebookSDKException;
use Facebook\FacebookRequestException;
use Facebook\FacebookOtherException;
use Facebook\FacebookAuthorizationException;
use Facebook\GraphObject;
use Facebook\GraphSessionInfo;
use Facebook\GraphUser;
use Facebook\GraphLocation;
// start session
session_start();

// init app with app id and secret
FacebookSession::setDefaultApplication('302472033280532', '88fd5d418dee3d04721f1ca97cd1bcea');

echo '<html>';

$helper = new FacebookCanvasLoginHelper();
try {
	$session = $helper->getSession();
} catch(Exception $ex) {
	echo "Exception occured, code: " . $ex->getCode();
	echo " with message: " . $ex->getMessage();
}

if ($session) {
	try {
		$graphObject = (new FacebookRequest($session, 'GET', '/me?locale=ja_JP'))->execute()->getGraphObject();
		$graphObject = (new FacebookRequest($session, 'GET', '/me/friends?locale=ja_JP'))->execute()->getGraphObject();
		
		$seimei = New Seimei();
		$seimei->sei = $graphObject->getProperty('last_name');
		$seimei->mei = $graphObject->getProperty('first_name');
		$seimei->sex = ($graphObject->getProperty('gender') == '女性' ? 'F' : 'M');
		
		$seimei->shindan();

		if (count($seimei->error) == 0) {
			seimeiHeader($seimei);
			seimeiBody($seimei);
		} else {
			echo '<body>判定できない文字が名前に含まれます：' . implode(', ', $seimei->error) . "</body>";
		}
	} catch (Exception $ex) {
		echo "Exception occured, code: " . $ex->getCode();
		echo " with message: " . $ex->getMessage();
	}
}
echo '</html>';
?>
