<?php
header('Content-type: text/html; charset=utf-8;');

date_default_timezone_set('Asia/Tokyo');

require '../vendor/autoload.php';

require '../php/seimei.php';
require '../php/reii.php';
require '../php/kenkou.php';
require '../php/seikaku.php';
require '../php/meimei.php';
require '../php/kanji.php';
require '../php/snipets.php';

use Facebook\FacebookSession;
use Facebook\FacebookRequest;
use Facebook\GraphUser;
use Facebook\FacebookRequestException;

FacebookSession::setDefaultApplication('302472033280532', '88fd5d418dee3d04721f1ca97cd1bcea');
$helper = new FacebookCanvasLoginHelper();
try {
  $session = $helper->getSession();
} catch(FacebookRequestException $ex) {
	echo "Exception occured, code: " . $ex->getCode();
	echo " with message: " . $ex->getMessage();
	return;
} catch(\Exception $ex) {
	echo "Exception occured, code: " . $ex->getCode();
	echo " with message: " . $ex->getMessage();
	return;
}

if ($session) {

	try {
		$user_profile = (new FacebookRequest(
				$session, 'GET', '/me'
		))->execute()->getGraphObject(GraphUser::className());

		$seimei = New Seimei();
		$seimei->sei = $user_profile['last_name'];
		$seimei->mei = $user_profile['first_name'];
		$seimei->sex = ($user_profile['gender'] == '女性' ? 'F' : 'M');
		
		$seimei->shindan();

		if (count($seimei->error) == 0) {
?>
<html>
<head>
<meta charset="UTF-8">
<LINK REL="SHORTCUT ICON" HREF="favicon.ico"> 
<meta name="description" content="<?php echo $seimei->sei . " " . $seimei->mei . "さんの運勢 総合得点：" . $seimei->grand_score() . "点/" .
	"人画（基礎運）" . $seimei->jinkaku . "画 " . $seimei->score($seimei->jinkaku) . "点/" .
	"外画（外交運）" . $seimei->gaikaku . "画 " . $seimei->score($seimei->gaikaku) . "点/" .
	"性格" . $seimei->seikaku_description() . "/" .
	"健康運" . ["◎" => "すごく良い", "○" => "良い", "△" => "ふつう", "×" => "悪い"][mb_substr($seimei->kenkou_description(), 6, 1)] . "/" .
	"天画（若年期運）" . $seimei->tenkaku . "画 " . $seimei->score($seimei->tenkaku) . "点/" .
	"総画（晩年期運）" . $seimei->soukaku . "画 " . $seimei->score($seimei->soukaku) . "点" ?>">
<meta name="keywords" content="<?php echo $seimei->sei ?> <?php echo $seimei->mei ?>">
<meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title><?php echo $seimei->sei ?> <?php echo $seimei->mei ?></title>
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" href="http://code.jquery.com/mobile/1.4.2/jquery.mobile-1.4.2.min.css" />
	<link rel="stylesheet" href="../css/default.css" />
	<script type="text/javascript" src="http://code.jquery.com/jquery-2.0.3.min.js"></script>
	<script type="text/javascript" src="http://code.jquery.com/mobile/1.4.2/jquery.mobile-1.4.2.min.js"></script>
	<script type="text/javascript" src="../js/okina.js"></script>
	<?php googleAnalytics() ?>
</head>

<body data-ajax="false">
	<div data-role="page" id="top" data-theme="a">
		<div data-role="header">
			<h1>あじあ姓名うらない</h1>
		</div>
		<div data-role="content">
			<h2><?php echo $seimei->sei ?>さんの命名・改名例</h2>
			<div data-role="collapsible" data-collapsed="true">
				<h2>男子（男性）の場合</h2>
				<div><?php echo $seimei->meimei('M') ?></div>
			</div>
			<div data-role="collapsible" data-collapsed="true">
				<h2>女子（女性）の場合</h2>
				<div><?php echo $seimei->meimei('F') ?></div>
			</div>

			<h2><?php echo $seimei->sei . " " . $seimei->mei ?>さんの運勢 (総合得点：<?php echo $seimei->grand_score() ?>点)</h2>
			<div data-role="collapsible" data-collapsed="true">
				<h2>人画 <?php echo $seimei->jinkaku . "画 (" . $seimei->score($seimei->jinkaku) . "点)" ?></h2>
				<p style="color:blue;font-weight:bold;">基礎運。一生の運勢を司ります。結婚により姓が変わると基礎運も変化しますが、この場合中年以降に強く現れます。</p>
				<p><?php echo $seimei->jinkaku . "画:" . $seimei->reii_description($seimei->jinkaku) . " (" . $seimei->score($seimei->jinkaku) . "点)" ?></p>
				<p style="font-size:x-large;font-weight:bold;"><?php echo $seimei->mongon('jinkaku') ?></p>
				<p style="font-size:small;">※ 鑑定文言について、山本哲生氏（故人：生没年不明）の編著「名前で読める自己の運命A・B・C」（ISBN不明）から引用しています。</p>
			</div>
			<div data-role="collapsible" data-collapsed="true">
				<h2>外画 <?php echo $seimei->gaikaku . "画 (" . $seimei->score($seimei->gaikaku) . "点)" ?></h2>
				<p style="color:blue;font-weight:bold;">対人運。対人関係および、家族・夫婦関係、友達関係など、外交面をあらわします。</p>
				<p><?php echo $seimei->gaikaku . "画：" . $seimei->reii_description($seimei->gaikaku) . " (" . $seimei->score($seimei->gaikaku) . "点)" ?></p>
				<p style="font-size:x-large;font-weight:bold;"><?php echo $seimei->mongon('gaikaku') ?></p>
				<p style="font-size:small;">※ 鑑定文言について、山本哲生氏（故人：生没年不明）の編著「名前で読める自己の運命A・B・C」（ISBN不明）から引用しています。</p>
			</div>
			<div data-role="collapsible" data-collapsed="true">
				<h2>人画の下一桁 <?php echo $seimei->jinshimo . "画" ?></h2>
				<p style="color:blue;font-weight:bold;">性格。外面から見た性格を現しています。他人から自分がどう見えているのかの参考にしてください。</p>
				<p><?php echo $seimei->jinshimo . "画：" . $seimei->seikaku_description() ?></p>
				<p style="font-size:x-large;font-weight:bold;"><?php echo $seimei->mongon('seikaku') ?></p>
			</div>
			<div data-role="collapsible" data-collapsed="true">
				<h2>健康運 (<?php echo ["◎" => "すごく良い", "○" => "良い", "△" => "ふつう", "×" => "悪い"][mb_substr($seimei->kenkou_description(), 6, 1)] ?>)</h2>
				<p style="color:blue;font-weight:bold;">健康運は三才の配置により決定します。吉数揃いの姓名も、健康に恵まれなければ活かされません。他の画数と合わせて判断してください。</p>
				<p>三才の配置：<?php echo mb_substr($seimei->kenkou_description(), 0, 5) ?></p>
				<p style="font-size:x-large;font-weight:bold;"><?php echo $seimei->mongon('kenkou') ?></p>
				<p style="font-size:small;">※ 鑑定文言について、山本哲生氏（故人：生没年不明）の編著「名前で読める自己の運命A・B・C」（ISBN不明）から引用しています。</p>
			</div>
			<div data-role="collapsible" data-collapsed="true">
				<h2>天画 <?php echo $seimei->tenkaku . "画 (" . $seimei->score($seimei->tenkaku) . "点)" ?></h2>
				<p style="color:blue;font-weight:bold;">若年期の基礎運。幼少年期の運勢を支配し、青年期まで強くあらわれます。</p>
				<p><?php echo $seimei->tenkaku . "画：" . $seimei->reii_description($seimei->tenkaku) . " (" . $seimei->score($seimei->tenkaku) . "点)" ?></p>
				<p style="font-size:x-large;font-weight:bold;"><?php echo $seimei->mongon('tenkaku') ?></p>
				<p style="font-size:small;">※ 鑑定文言について、山本哲生氏（故人：生没年不明）の編著「名前で読める自己の運命A・B・C」（ISBN不明）から引用しています。</p>
			</div>
			<div data-role="collapsible" data-collapsed="true">
				<h2>総画 <?php echo $seimei->soukaku . "画 (" . $seimei->score($seimei->soukaku) . "点)" ?></h2>
				<p style="color:blue;font-weight:bold;">晩年運。50歳前後からの運勢を支配します。ただし、基礎運の影響も残ります。</span><br>
				<p><?php echo $seimei->soukaku . "画：" . $seimei->reii_description($seimei->soukaku) . " (" . $seimei->score($seimei->soukaku) . "点)" ?></p>
				<p style="font-size:x-large;font-weight:bold;"><?php echo $seimei->mongon('soukaku') ?></p>
				<p style="font-size:small;">※ 鑑定文言について、山本哲生氏（故人：生没年不明）の編著「名前で読める自己の運命A・B・C」（ISBN不明）から引用しています。</p>
			</div>
		</div>
	</body>
</html>
<?php

		} else {
			echo '判定できない文字が名前に含まれます：' . implode(', ', $seimei->error);
		}

	} catch(FacebookRequestException $e) {

		echo "Exception occured, code: " . $e->getCode();
		echo " with message: " . $e->getMessage();

	}
}
?>
