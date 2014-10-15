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

require '../vendor/autoload.php';

FacebookSession::setDefaultApplication('302472033280532', '88fd5d418dee3d04721f1ca97cd1bcea');

$helper = new FacebookRedirectLoginHelper('http://www.seimei.asia/fb/');
$loginUrl = $helper->getLoginUrl();
// Use the login url on a link or button to redirect to Facebook for authentication

require '../php/seimei.php';
require '../php/reii.php';
require '../php/kenkou.php';
require '../php/seikaku.php';
require '../php/meimei.php';
require '../php/kanji.php';
date_default_timezone_set('UTC');

$seimei = New Seimei();
$seimei->sei = $_GET['sei'];
$seimei->mei = $_GET['mei'];
$seimei->sex = $_GET['sex'];
$seimei->shindan();

?>
<html>
<head>
<meta charset="UTF-8">
<LINK REL="SHORTCUT ICON" HREF="favicon.ico"> 
<meta name="description" content="<?php echo $kantei ?
	"あじあ姓名うらないへようこそ！赤ちゃんの名まえをつけたり（選名）、じぶんの運勢をうらなったり、どしどし使ってね！" :
	$seimei->sei . " " . $seimei->mei . "さんの運勢 主運" . $seimei->jinkaku . "画 " . preg_replace("/<[^>]*>/","", $seimei->mongon('jinkaku')) .
	"対人運・社交運:" . $seimei->gaikaku . "画 " . preg_replace("/<[^>]*>/","", $seimei->mongon('gaikaku')) . "・・・" ?>">
<meta name="keywords" content="<?php echo $seimei->sei ?> <?php echo $seimei->mei ?> 翁 占い 姓名判断 姓名うらない 姓名占い 命名 選名 名前 新生児 赤ちゃん 出産準備 改名 DQNネーム 改姓 結婚相談 芸名 雅号 会社名 人事相談 熊崎式 だいぶつ あじあ">
<meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>あじあ姓名うらない</title>
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" href="http://code.jquery.com/mobile/1.4.2/jquery.mobile-1.4.2.min.css" />
	<link rel="stylesheet" href="css/default.css" />
	<script type="text/javascript" src="http://code.jquery.com/jquery-2.0.3.min.js"></script>
	<script type="text/javascript" src="http://code.jquery.com/mobile/1.4.2/jquery.mobile-1.4.2.min.js"></script>
	<script type="text/javascript" src="js/okina.js"></script>
	<script>
	  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
	  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
	  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
	  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');
	
	  ga('create', 'UA-26314420-4', 'auto');
	  ga('send', 'pageview');
	
	</script>
</head> 
<body>

	<div data-role="page" id="top" data-theme="a">
		<div data-role="header">
			<h1>あじあ姓名うらない <span class="ui-mini"><a href="#mit-lisense">Copyright &copy; 2014 だいぶつ</a></span></h1>
		</div><!-- /header -->
	
		<div data-role="content">
			<h2><?php echo $seimei->sei ?>さんの子どもに名前を付けるなら・・・</h2>
			<div data-role="collapsible" data-collapsed="false">
				<h2>【命名例】男の子につけるなら・・・</h2>
				<div><?php echo $seimei->meimei('M') ?></div>
			</div>
			<div data-role="collapsible" data-collapsed="false">
				<h2>【命名例】女の子につけるなら・・・</h2>
				<div><?php echo $seimei->meimei('F') ?></div>
			</div>
			<h2><?php echo $seimei->sei . " " . $seimei->mei ?>さんの運勢</h2>
			<p>※ 鑑定文言について、一部を山本哲生氏（故人：生没年不明）の編著「名前で読める自己の運命A・B・C」（ISBN不明）から引用しています。</p>
			<div data-role="collapsible" data-collapsed="false">
				<h2>基礎運(人画）　<span class="ui-mini">一生の運勢を司ります。結婚により姓が変わると基礎運も変化しますが、この場合中年以降に強く現れます。</span></h2>
				<div><?php echo $seimei->jinkaku ?>画<br><?php echo $seimei->mongon('jinkaku') ?></div>
			</div>
			<div data-role="collapsible" data-collapsed="false">
				<h2>対人運（外画）　<span class="ui-mini">対人関係および、家族・夫婦関係、友達関係など、外交面をあらわします。</span></h2>
				<div><?php echo $seimei->gaikaku ?>画<br><?php echo $seimei->mongon('gaikaku') ?></div>
			</div>
			<div data-role="collapsible" data-collapsed="false">
				<h2>性格(人画の下一桁）　<span class="ui-mini">外面から見た性格を現しています。他人から自分がどう見えているのかの参考にしてください。</span></h2>
				<div><?php echo $seimei->jinshimo . "画:" . $seimei->mongon('seikaku') ?></div>
			</div>
			<div data-role="collapsible" data-collapsed="false">
				<h2>健康運（陰陽５行３才の組み合わせにより算出）<span class="ui-mini">吉数揃いの姓名も、健康に恵まれなければ活かされません。他の画数と合わせて判断してください。</span></h2>
				<div><?php echo $seimei->mongon('kenkou') ?></div>
			</div>
			<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
			<div data-role="collapsible" data-collapsed="false">
				<h2>基礎運（天画）<span class="ui-mini">幼少年期の運勢を支配し、青年期まで強くあらわれます。</span></h2>
				<div><?php echo $seimei->chikaku ?>画：<?php echo $seimei->mongon('chikaku') ?></p>
				</div>
			</div>
			<div data-role="collapsible" data-collapsed="false">
				<h2>晩年運（総画）<span class="ui-mini">50歳前後からの運勢を支配します。ただし、基礎運の影響も残ります。</span></h2>
				<div><?php echo $seimei->soukaku ?>画：<?php echo $seimei->mongon('soukaku') ?></div>
			</div>
		</div>
	</div>
</body>
</html>
