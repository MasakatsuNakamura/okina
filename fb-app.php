<?php
header('Content-type: text/html; charset=utf-8;');

function cmp(Seimei $a, Seimei $b)
{
	if ($a->grand_score() == $b->grand_score()) {
		return 0;
	}
	return ($a->grand_score() < $b->grand_score()) ? -1 : 1;
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
		$seimei->sex = ($graphObject->getProperty('gender') == '女性' ? 'F' : 'M');
		$seimei->shindan();
		$meimei = $seimei->meimei();

		seimeiHeader($seimei);
		
		$seimei_list = [];
		if (count($seimei->error) == 0) {
			array_push($seimei_list, $seimei);
		}
		
		foreach ($meimei[$seimei->sex] as $name) {
			$seimei->mei = $name[0];
			$seimei->shindan();
			array_push($seimei_list, $seimei);
		}
		usort($seimei_list, "cmp");

?>
<body>
<?php fbRoot(); ?>
<div><img src="images/CoverImage.png" alt="あじあ姓名うらない バックグラウンドイメージはハウステンボス"></div>
<?php
		fbLike();
		echo "<h2>運勢ランキング</2>";
		echo "<table>";
		echo "<tr><th>" . implode("</th><th>", ["No.", "氏名", "性別", "総合得点", "人画(基礎運)", "外画(外交運)", "健康運", "天画(若年期運)", "総画(晩年運)"]) . "</th></tr>";

		$count = 1;
		foreach ($seimei_list as $seimei) {
			echo "<tr><td>" . $count . "</td>";
			echo "<td>" . $seimei->sei . " " . $seimei->mei . "</td>";
			echo "<td>" . ($seimei->sex == 'M' ? '男性' : '女性') . "</td>";
			echo "<td>" . $seimei->grand_score() . "点</td>";
			echo "<td>" . $seimei->jinkaku . "画:" . $seimei->score($seimei->jinkaku) . "点<br>" . $seimei->reii_description($seimei->jinkaku) . "</td>";
			echo "<td>" . $seimei->gaikaku . "画：" . $seimei->score($seimei->gaikaku) . "点<br>" . $seimei->reii_description($seimei->gaikaku) . "</td>";
			echo "<td>" . ["◎" => "すごく良い", "○" => "良い", "△" => "ふつう", "×" => "悪い"][mb_substr($seimei->kenkou_description(), 6, 1)] . "</td>";
			echo "<td>" . $seimei->tenkaku . "画：" . $seimei->score($seimei->tenkaku) . "点<br>" . $seimei->reii_description($seimei->tenkaku) . "</td>";
			echo "<td>" . $seimei->soukaku . "画：" . $seimei->score($seimei->soukaku) . "点<br>" . $seimei->reii_description($seimei->soukaku) . "</td></tr>";
			$count++;
		}
		echo "</table>";
		
	} catch (Exception $ex) {
		echo "Exception occured, code: " . $ex->getCode();
		echo " with message: " . $ex->getMessage();
	}
}
?>
</body>
</html>
