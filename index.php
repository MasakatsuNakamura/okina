<?php
header('Content-type: text/html; charset=utf-8;');
require 'php/seimei.php';
require 'php/reii.php';
require 'php/kenkou.php';
require 'php/seikaku.php';
require 'php/meimei.php';
require 'php/kanji.php';
date_default_timezone_set('UTC');

$kantei = true;
if (count($_GET) > 0) {
	$seimei = New Seimei();
	$seimei->sei = $_GET['sei'];
	$seimei->mei = $_GET['mei'];
	$seimei->sex = $_GET['sex'];
	$seimei->marry = $_GET['marry'];
	if (strlen($seimei->sei) > 0 && strlen($seimei->mei) > 0 && ($seimei->sex == 'M' || $seimei->sex == 'F') && ($seimei->marry == 'yes' || $seimei->marry == 'no')) {
		$seimei->shindan();
		$kantei = false;
	}
}

?>
<html>
<head>
<meta charset="UTF-8">
<LINK REL="SHORTCUT ICON" HREF="favicon.ico"> 
<meta name="description" content="<?php echo $kantei ?
	"あじあ姓名診断へようこそ。<br>姓名診断とは、統計哲学です。姓名から運勢が、一意に導き出されるわけではありませんが、姓名が運勢に影響を与えるという事実は、観測額的に明らかです。人の名前を聞いたときに、「雰囲気どおりの名だ」と感じることは少なくありません。これらの関係に一定の法則を見出ため、われわれの先人（熊崎翁ら）は多くの人々の姓名を鑑定し、またその結果をフィードバック・蓄積してきました。この姓名診断は、これらの先人たちの知恵の結晶であり、人類共有の宝です。私は、この宝を多くの人に体験してもらいたいと考え、無料占いを公開することにしました。さらに、この姓名診断には新生児命名アドバイス機能がついています。あじあ式姓名診断のノウハウを利用し、お子様につける名前、また芸名などの選定にもご利用いただけます。これらの機能は無料です。ぜひお試しください。" :
	$seimei->sei . " " . $seimei->mei . "さんの運勢 主運" . $seimei->jinkaku . "画 " . preg_replace("/<[^>]*>/","", $seimei->mongon('jinkaku')) .
	"対人運・社交運:" . $seimei->gaikaku . "画 " . preg_replace("/<[^>]*>/","", $seimei->mongon('gaikaku')) . "・・・" ?>">
<meta name="keywords" content="<?php echo $seimei->sei ?> <?php echo $seimei->mei ?> 翁 占い 姓名判断 姓名診断 命名 選名 名前 新生児 赤ちゃん 出産準備 改名 改姓 結婚相談 芸名 雅号 会社名 人事相談 熊崎式 だいぶつ">
<meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>あじあ姓名診断</title>
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
	<div id="fb-root"></div>
	<script>(function(d, s, id) {
	  var js, fjs = d.getElementsByTagName(s)[0];
	  if (d.getElementById(id)) return;
	  js = d.createElement(s); js.id = id;
	  js.src = "//connect.facebook.net/ja_JP/sdk.js#xfbml=1&appId=482407305223650&version=v2.0";
	  fjs.parentNode.insertBefore(js, fjs);
	}(document, 'script', 'facebook-jssdk'));</script>
<?php
if ($kantei) {
?>
	<div data-role="page" id="top" data-theme="a">
		<div data-role="header">
				<a href="#top" data-icon="home" class='ui-disabled'>ホーム</a>
				<h1>あじあ姓名診断</h1>
			</div>
			<div data-role="content">
				<h2>あじあ姓名診断 <span class="fb-share-button" data-href="/" data-type="button_count"></span></h2>
				<div class="ninja_onebutton">
				<script type="text/javascript">
				//<![CDATA[
				(function(d){
				if(typeof(window.NINJA_CO_JP_ONETAG_BUTTON_0f8b16741da01b4bf2d81552e11cc4d6)=='undefined'){
				    document.write("<sc"+"ript type='text\/javascript' src='http:\/\/omt.shinobi.jp\/b\/0f8b16741da01b4bf2d81552e11cc4d6'><\/sc"+"ript>");
				}else{
				    window.NINJA_CO_JP_ONETAG_BUTTON_0f8b16741da01b4bf2d81552e11cc4d6.ONETAGButton_Load();}
				})(document);
				//]]>
				</script><span class="ninja_onebutton_hidden" style="display:none;"></span><span style="display:none;" class="ninja_onebutton_hidden"></span>
				</div>
				<p>あじあ姓名診断へようこそ。<br>
				姓名診断とは、統計哲学です。姓名から運勢が一意に導き出されるわけではありませんが、姓名が運勢に影響を与えるという事実は、観測学的に明らかです。<br>
				たとえば人の名前を聞いたときに、「雰囲気どおりの名だ」と感じることは少なくありません。<br>
				したがって、姓名は運勢を決定付けるものではないにしろ、何らかの影響力を持っているものだと考えるのが合理的です。<br>
				これらの関係に一定の法則を見出ため、われわれの先人（熊崎翁ら）は多くの人々の姓名を鑑定し、またその結果をフィードバック・蓄積してきました。<br>
				この姓名診断は、これらの先人たちの知恵の結晶であり、人類共有の宝です。<br>
				私は、この宝を多くの人に体験してもらいたいと考え、無料占いを公開することにしました。<br>
				さらに、この姓名診断には新生児命名アドバイス機能がついています。
				あじあ姓名診断のノウハウを利用し、お子様につける名前、また芸名などの選定にもご利用いただけます。これらの機能は無料です。ぜひお試しください。</p>
				<form data-ajax="false" method="GET">
					<div data-role="fieldcontain">
						<label for="sei">姓</label>
						<input type="text" name="sei" id="sei" />
					</div>
					<div data-role="fieldcontain">
						<label for="mei">名</label>
						<input type="text" name="mei" id="mei" />
					</div>
					<div data-role="fieldcontain">
						<label for="sex">性別</label>
						<fieldset name="sex" data-role="controlgroup" data-type="horizontal" data-role="fieldcontain">
							<input type="radio" name="sex" id="sex-2" value="F" checked="checked" />
							<label for="sex-2">女性</label>
							<input type="radio" name="sex" id="sex-1" value="M"/>
							<label for="sex-1">男性</label>
						</fieldset>
					</div>
					<div data-role="fieldcontain">
						<label for="marry">結婚</label>
						<fieldset name="marry" data-role="controlgroup" data-type="horizontal" data-role="fieldcontain">
							<input type="radio" name="marry" id="marry-1" value="yes" />
							<label for="marry-1">している</label>
							<input type="radio" name="marry" id="marry-2" value="no"  checked="checked" />
							<label for="marry-2">していない</label>
						</fieldset>
					</div>
					<input type="submit" value="鑑定" data-role="button" />
					</form>
<?php
} else {
?>
		<div data-role="page" id="kantei" data-theme="a">
			<div data-role="header">
				<a href="?" data-icon="home" data-ajax="false">ホーム</a>
				<h1><?php echo $seimei->sei ?>さんの子どもに名前を付けるなら・・・</h1>
			</div><!-- /header -->
			<div data-role="content">
				<h2><?php echo $seimei->sei ?>さんの子どもに名前を付けるなら・・・</h2>
				<div class="ninja_onebutton">
				<script type="text/javascript">
				//<![CDATA[
				(function(d){
				if(typeof(window.NINJA_CO_JP_ONETAG_BUTTON_0f8b16741da01b4bf2d81552e11cc4d6)=='undefined'){
				    document.write("<sc"+"ript type='text\/javascript' src='http:\/\/omt.shinobi.jp\/b\/0f8b16741da01b4bf2d81552e11cc4d6'><\/sc"+"ript>");
				}else{
				    window.NINJA_CO_JP_ONETAG_BUTTON_0f8b16741da01b4bf2d81552e11cc4d6.ONETAGButton_Load();}
				})(document);
				//]]>
				</script><span class="ninja_onebutton_hidden" style="display:none;"></span><span style="display:none;" class="ninja_onebutton_hidden"></span>
				</div>
				<p>結果をみんなにシェアしましょう！ <span class="fb-share-button" data-href="/?sei=<?php echo urlencode($seimei->sei) . "&mei=" . urlencode($seimei->mei) . "&sex=" . $seimei->sex . "&marry=" . $seimei->marry ?>" data-type="button_count"></span></p>
				<div data-role="collapsible" data-collapsed="false">
					<h2>【命名例】男の子につけるなら・・・</h2>
					<div><?php echo $seimei->meimei('M') ?></div>
				</div>
				<div data-role="collapsible" data-collapsed="false">
					<h2>【命名例】女の子につけるなら・・・</h2>
					<div><?php echo $seimei->meimei('F') ?></div>
				</div>
				<h2><?php echo $seimei->sei . " " . $seimei->mei ?>さんの運勢</h2>
				<div data-role="collapsible" data-collapsed="false">
					<h2>主運　<span class="ui-mini">当人の一生の中心を司ります。結婚により姓が変わると主運も変わりますが、中年以降に強く現れます。</span></h2>
					<div><?php echo $seimei->jinkaku ?>画：<?php echo $seimei->mongon('jinkaku') ?></div>
				</div>
				<div data-role="collapsible" data-collapsed="false">
					<h2>対人運・社交運　<span class="ui-mini">対人関係や家族・夫婦関係、友達関係に現れてきます。</span></h2>
					<div><?php echo $seimei->gaikaku ?>画：<?php echo $seimei->mongon('gaikaku') ?></div>
				</div>
				<div data-role="collapsible" data-collapsed="false">
					<h2>性格　<span class="ui-mini">当人の外面的な性格を現します。自分が他人からどう見えているのか参考になります。</span></h2>
					<div><?php echo $seimei->mongon('seikaku') ?></div>
				</div>
				<div data-role="collapsible" data-collapsed="false">
					<h2>健康運(体調・精神)　<span class="ui-mini">例え吉数揃いの姓名であっても、健康に恵まれなければ活かさせません。（△は単独での判断が難しい）</span></h2>
					<div><?php echo $seimei->mongon('kenkou') ?></div>
				</div>
				<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
				<div data-role="collapsible" data-collapsed="false">
					<h2>基礎運　<span class="ui-mini">幼少年期の運勢の吉凶を支配し、青年期まで最も強く作用します。(若年者の判断はこちらが有効)</span></h2>
					<div><?php echo $seimei->chikaku ?>画：<?php echo $seimei->mongon('chikaku') ?></p>
					</div>
				</div>
				<div data-role="collapsible" data-collapsed="false">
					<h2>晩年運　<span class="ui-mini">50歳前後から強く現れてきます。ただし、主運と基礎運に左右されますので注意して下さい。</span></h2>
					<div><?php echo $seimei->soukaku ?>画：<?php echo $seimei->mongon('soukaku') ?></div>
				</div>
<?php
}
?>
			</div>
			<div data-role='footer' data-position='fixed'>
				<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
				<!-- あじあ姓名診断 -->
				<ins class="adsbygoogle"
				     style="display:inline-block;width:320px;height:100px"
				     data-ad-client="ca-pub-0413343113584981"
				     data-ad-slot="6868632444"></ins>
				<script>
				(adsbygoogle = window.adsbygoogle || []).push({});
				</script>
			</div>
		</div>
	</div>
</body>
</html>
