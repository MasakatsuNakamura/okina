<?php
header('Content-type: text/html; charset=utf-8;');

function cmp($a, $b)
{
	if ($a['grand_score'] == $b['grand_score']) {
		return 0;
	}
	return ($a['grand_score'] < $b['grand_score']) ? 1 : -1;
}

function seimei_translate (Seimei $seimei, $gender, $desc) {
	return [
		'name'          => $seimei->sei . " " . $seimei->mei . " (". $desc . ")",
		'sei'           => $seimei->sei,
		'mei'           => $seimei->mei,
		'sex'			=> $seimei->sex,
		'gender'        => $gender,
		'jinkaku'       => $seimei->jinkaku,
		'jinkaku_disc'  => $seimei->reii_description($seimei->jinkaku),
		'jinkaku_score' => $seimei->score($seimei->jinkaku),
		'gaikaku'       => $seimei->gaikaku,
		'gaikaku_disc'  => $seimei->reii_description($seimei->gaikaku),
		'gaikaku_score' => $seimei->score($seimei->gaikaku),
		'tenkaku'       => $seimei->tenkaku,
		'tenkaku_disc'  => $seimei->reii_description($seimei->tenkaku),
		'tenkaku_score' => $seimei->score($seimei->tenkaku),
		'soukaku'       => $seimei->soukaku,
		'soukaku_disc'  => $seimei->reii_description($seimei->soukaku),
		'soukaku_score' => $seimei->score($seimei->soukaku),
		'kenkou'        => mb_substr($seimei->kenkou_description(), 6, 1),
		'grand_score'   => round($seimei->grand_score())
	];
}

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
		
		$seimei = New Seimei();
		$seimei->sei = $graphObject->getProperty('last_name');
		$seimei->mei = $graphObject->getProperty('first_name');
		$gender = $graphObject->getProperty('gender');
		$seimei->sex = ($gender == '女性' ? 'F' : 'M');
		$seimei->shindan();
		$meimei = $seimei->meimei();

		seimeiHeader($seimei);
		
		$seimei_list = [];
		if (count($seimei->error) == 0) {
			array_push($seimei_list, seimei_translate($seimei, $gender, "あなたの名前"));
		}
		
		foreach (['M', 'F'] as $sex) {
			foreach ($meimei[$sex] as $name) {
				$seimei->mei = $name[0];
				$seimei->sex = $sex;
				$seimei->shindan();
				array_push($seimei_list, seimei_translate($seimei, $sex == 'M' ? '男性' : '女性', $name[1]));
			}
		}
		usort($seimei_list, "cmp");

		echo "<body>";
		fbRoot();
?>
<div><img src="images/CoverImage.png" alt="あじあ姓名うらない バックグラウンドイメージはハウステンボス"></div>
<?php
		fbLike();
		echo "<h2>命名・改名アドバイザー</h2><p>あじあ姓名うらないオススメの、あなたのいまの姓にピッタリのお名前です。お子様につけていただいてもかまいませんが、その場合は戸籍上の姓で占う必要があります(配偶者の姓を名乗られている場合は、配偶者に占ってもらってください)。</p>";
		echo "<table>";
		echo "<tr><th>" . implode("</th><th>", ["氏名", "性別", "総合得点", "人画(基礎運)", "外画(外交運)", "健康運", "天画(若年期運)", "総画(晩年運)"]) . "</th></tr>";

		$count = 1;
		foreach ($seimei_list as $name) {
			echo "<tr><td><a style='font-size:large;text-decoration:none;color:" . ($name['sex'] == 'M' ? "blue" : "red"). ";' href='http://www.seimei.asia/?sei=" . $name['sei'] . "&mei=" . $name['mei'] . "sex=" . $name['sex'] . "'>" . $name['name'] . "</a></td>";
			echo "<td>" . $name['gender'] . "</td>";
			echo "<td style='text-align:center;'>" . $name['grand_score'] . "点</td>";
			echo "<td><p style='font-size:x-large;'>" . $name['jinkaku'] . "画：" . $name['jinkaku_score'] . "点</p><p style='font-size:small;'" . $name['jinkaku_disc'] . "</p></td>";
			echo "<td><p style='font-size:x-large;'>" . $name['gaikaku'] . "画：" . $name['gaikaku_score'] . "点</p><p style='font-size:small;'" . $name['gaikaku_disc'] . "</p></td>";
			echo "<td style='text-align:center;font-size:x-large;'>" . $name['kenkou'] . "</td>";
			echo "<td><p style='font-size:x-large;'>" . $name['tenkaku'] . "画：" . $name['tenkaku_score'] . "点</p><p style='font-size:small;'" . $name['tenkaku_disc'] . "</p></td>";
			echo "<td><p style='font-size:x-large;'>" . $name['soukaku'] . "画：" . $name['soukaku_score'] . "点</p><p style='font-size:small;'" . $name['soukaku_disc'] . "</p></td>";
			$count++;
		}
		echo "</table>";
		echo "</body>";
		
	} catch (Exception $ex) {
		echo "Exception occured, code: " . $ex->getCode();
		echo " with message: " . $ex->getMessage();
	}
}
?>
</html>
