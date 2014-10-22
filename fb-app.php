<?php
header('Content-type: text/html; charset=utf-8;');

function cmp($a, $b)
{
	if ($a['grand_score'] == $b['grand_score']) {
		return 0;
	}
	return ($a['grand_score'] < $b['grand_score']) ? 1 : -1;
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
			array_push($seimei_list, [
				'name'          => $seimei->sei . " " . $seimei->mei . " (あなたの名前)",
				'sex'           => ($seimei->sex == 'M' ? '男性' : '女性'),
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
				'kenkou'        => ["◎" => "すごく良い", "○" => "良い", "△" => "ふつう", "×" => "悪い"][mb_substr($seimei->kenkou_description(), 6, 1)],
				'grand_score'   => $seimei->grandscore()
			]);
		}
		
		foreach ($meimei[$seimei->sex] as $name) {
			$seimei->mei = $name[0];
			$seimei->shindan();
			array_push($seimei_list, [
				'name'          => $seimei->sei . " " . $seimei->mei . " " . $name[1],
				'sex'           => ($seimei->sex == 'M' ? '男性' : '女性'),
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
				'kenkou'        => ["◎" => "すごく良い", "○" => "良い", "△" => "ふつう", "×" => "悪い"][mb_substr($seimei->kenkou_description(), 6, 1)],
				'grand_score'   => $seimei->grandscore()
			]);
		}
		usort($seimei_list, "cmp");

		echo "<body>";
		fbRoot();
?>
<div><img src="images/CoverImage.png" alt="あじあ姓名うらない バックグラウンドイメージはハウステンボス"></div>
<?php
		fbLike();
		echo "<h2>改名アドバイザー</h2><p>あじあ姓名うらないオススメの、あなたにピッタリのお名前です(お子様につけてもかまいません)。</p>";
		echo "<table>";
		echo "<tr><th>" . implode("</th><th>", ["氏名", "性別", "総合得点", "人画(基礎運)", "外画(外交運)", "健康運", "天画(若年期運)", "総画(晩年運)"]) . "</th></tr>";

		$count = 1;
		foreach ($seimei_list as $name) {
			echo "<tr><td>" . $name['name'] . "</td>";
			echo "<td>" . $name['sex'] . "</td>";
			echo "<td>" . $name['grand_score'] . "点</td>";
			echo "<td>" . $name['jinkaku'] . "画:" . $name['jinkaku_score'] . "点<br>" . $name['jinkaku_disc'] . "</td>";
			echo "<td>" . $name['gaikaku'] . "画:" . $name['gaikaku_score'] . "点<br>" . $name['gaikaku_disc'] . "</td>";
			echo "<td>" . $name['kenkou'] . "</td>";
			echo "<td>" . $name['tenkaku'] . "画:" . $name['tenkaku_score'] . "点<br>" . $name['tenkaku_disc'] . "</td>";
			echo "<td>" . $name['soukaku'] . "画:" . $name['soukaku_score'] . "点<br>" . $name['soukaku_disc'] . "</td>";
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
