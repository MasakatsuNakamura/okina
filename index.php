<?php
header('Content-type: text/html; charset=utf-8;');
date_default_timezone_set('UTC');
?>
<html>
<head>
<meta charset="UTF-8">
<meta name="description" content="ズバリよくあたる無料の姓名判断、新生児の命名、改名、改姓、ご結婚の相談を引受ます。">
<meta name="keywords" content="翁 占い 姓名判断 命名 選名 名前 新生児 赤ちゃん 出産準備 改名 改姓 結婚相談 芸名 雅号 会社名 人事相談 熊崎式">
<title>山本式姓名判断　for モバイル</title>
	<meta name="viewport" content="width=device-width, initial-scale=1"> 
	<link rel="stylesheet" href="http://code.jquery.com/mobile/1.4.2/jquery.mobile-1.4.2.min.css" />
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
	  js.src = "//connect.facebook.net/ja_JP/sdk.js#xfbml=1&appId=251118258422878&version=v2.0";
	  fjs.parentNode.insertBefore(js, fjs);
	}(document, 'script', 'facebook-jssdk'));</script>

<?php
if (count($_GET) == 0) {
?>
	<div data-role="page" id="top" data-theme="a">
		<div data-role="header">
			<a href="#top" data-icon="home" class='ui-disabled'>ホーム</a>
			<h1>山本式姓名判断 for モバイル</h1>
		</div>
		<div data-role="content">
			<h2>山本式姓名診断 <div class="fb-share-button" data-href="http://okina.herokuapp.com/" data-type="button_count"></div></h2>
			<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
			<!-- 山本翁 -->
			<ins class="adsbygoogle"
			     style="display:inline-block;width:320px;height:100px"
			     data-ad-client="ca-pub-0413343113584981"
			     data-ad-slot="6868632444"></ins>
			<script>
			(adsbygoogle = window.adsbygoogle || []).push({});
			</script>
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
			<p>山本式姓名判断へようこそ。このモバイル版だけに<b>新生児命名アドバイス機能がついています！</b>ぜひお試しください。</p>
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
	require 'php/seimei.php';
	require 'php/reii.php';
	require 'php/kenkou.php';
	require 'php/seikaku.php';
	require 'php/meimei.php';
	require 'php/kanji.php';

	$seimei = New Seimei();
	$seimei->sei = $_GET['sei'];
	$seimei->mei = $_GET['mei'];
	$seimei->sex = $_GET['sex'];
	$seimei->marry = $_GET['marry'];
	$seimei->shindan();
?>
		<div id="fb-root"></div>
		<script>(function(d, s, id) {
		  var js, fjs = d.getElementsByTagName(s)[0];
		  if (d.getElementById(id)) return;
		  js = d.createElement(s); js.id = id;
		  js.src = "//connect.facebook.net/ja_JP/sdk.js#xfbml=1&appId=251118258422878&version=v2.0";
		  fjs.parentNode.insertBefore(js, fjs);
		}(document, 'script', 'facebook-jssdk'));</script>
		<div data-role="page" id="kantei" data-theme="a">
		<div data-role="header">
			<a href="?" data-icon="home" data-ajax="false">ホーム</a>
			<h1><?php echo $seimei->sei . " " . $seimei->mei ?>さんの運勢</h1>
		</div><!-- /header -->
		<div data-role="content">
		<h2><?php echo $seimei->sei . " " . $seimei->mei ?>さんの運勢 <div class="fb-share-button" data-href="http://okina.herokuapp.com/?<?php echo urlencode($seimei->sei) . "&mei=" . urlencode($seimei->mei) . "&sex=" . $seimei->sex . "&marry=" . $seimei->marry ?>" data-type="button_count"></div></h1>
			<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
			<!-- 山本翁 -->
			<ins class="adsbygoogle"
			     style="display:inline-block;width:320px;height:100px"
			     data-ad-client="ca-pub-0413343113584981"
			     data-ad-slot="6868632444"></ins>
			<script>
			(adsbygoogle = window.adsbygoogle || []).push({});
			</script>
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
			<p>結果をみんなにシェアしてみましょう！</p>
			<h3>主運: <?php echo $seimei->jinkaku ?>画</h3>
			<p>当人の一生の中心を司ります。結婚により姓が変わると主運も変わりますが、中年以降に強く現れます。</p>
			<p><?php echo $seimei->mongon('jinkaku') ?></p>
			<h3>対人運・社交運: <?php echo $seimei->gaikaku ?>画</h3>
			<p>対人関係や家族・夫婦関係、友達関係に現れてきます。</p>
			<p><?php echo $seimei->mongon('gaikaku') ?></p>
			<h3>性格</h3>
			<p>当人の外面的な性格を現します。自分が他人からどう見えているのか参考になります。</p>
			<p><?php echo $seimei->mongon('seikaku') ?></p>
			<h3>健康運(体調・精神)</h3>
			<p>例え吉数揃いの姓名であっても、健康に恵まれなければ活かさせません。（△は単独での判断が難しい）</p>
			<p><?php echo $seimei->mongon('kenkou') ?></p>
			<h3>基礎運: <?php echo $seimei->chikaku ?>画</h3>
			<p>幼少年期の運勢の吉凶を支配し、青年期まで最も強く作用します。(若年者の判断はこちらが有効)</p>
			<p><?php echo $seimei->mongon('chikaku') ?></p>
			<h3>晩年運: <?php echo $seimei->soukaku ?>画</h3>
			<p>50歳前後から強く現れてきます。ただし、主運と基礎運に左右されますので注意して下さい。</p>
			<p><?php echo $seimei->mongon('soukaku') ?></p>
			<h3>新生児命名アドバイス</h3>
			<p><strong>男の子にオススメ！</strong> <?php echo $seimei->meimei('M') ?></p>
			<p><strong>女の子にオススメ！</strong> <?php echo $seimei->meimei('F') ?></p>
<?php
}
?>
			<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
		</div>
		<div data-role='footer'>
			<h4>Copyright&reg;2014 <a href="http://daibutsuda.github.io/">だいぶつ</a> &amp; 山本翁</h4>
		</div>
	</div>

</body>
</html>
