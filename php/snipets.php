<?php
function googleAnalytics() {
?>
<script>
(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
	(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
	m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','//www.google-analytics.com/analytics.js','ga');
ga('create', 'UA-26314420-4', 'auto');
ga('require', 'displayfeatures');
ga('send', 'pageview');
</script>
<?php
}

function fbRoot() {
?>
<div id="fb-root"></div>
<script>(function(d, s, id) {
  var js, fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) return;
  js = d.createElement(s); js.id = id;
  js.src = "//connect.facebook.net/ja_JP/sdk.js#xfbml=1&appId=482407305223650&version=v2.0";
  fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));</script>
<?php
}

function ninjaTools() {
?>
<div class="ninja_onebutton">
<script type="text/javascript">
//<![CDATA[
(function(d){
if(typeof(window.NINJA_CO_JP_ONETAG_BUTTON_971b6531abd1b36d9c48f0245802d633)=='undefined'){
    document.write("<sc"+"ript type='text\/javascript' src='http:\/\/omt.shinobi.jp\/b\/971b6531abd1b36d9c48f0245802d633'><\/sc"+"ript>");
}else{
    window.NINJA_CO_JP_ONETAG_BUTTON_971b6531abd1b36d9c48f0245802d633.ONETAGButton_Load();}
})(document);
//]]>
</script><span class="ninja_onebutton_hidden" style="display:none;"></span><span style="display:none;" class="ninja_onebutton_hidden"></span>
</div>
<?php
}

function googleAdsense() {
?>
<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- あじあ姓名うらない -->
<ins class="adsbygoogle"
     style="display:inline-block;width:320px;height:100px"
     data-ad-client="ca-pub-0413343113584981"
     data-ad-slot="6868632444"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>
<?php
}

function seimeiHeader(Seimei $seimei) {
?>
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no">
	<meta property="og:locale" content="ja_JP" />
	<meta name="description" content="<?php echo $seimei->sei . " " . $seimei->mei . "さんの運勢 総合得点：" . $seimei->grand_score() . "点/" .
		"人画（基礎運）" . $seimei->jinkaku . "画 " . $seimei->score($seimei->jinkaku) . "点/" .
		"外画（外交運）" . $seimei->gaikaku . "画 " . $seimei->score($seimei->gaikaku) . "点/" .
		"性格" . $seimei->seikaku_description() . "/" .
		"健康運" . ["◎" => "すごく良い", "○" => "良い", "△" => "ふつう", "×" => "悪い"][mb_substr($seimei->kenkou_description(), 6, 1)] . "/" .
		"天画（若年期運）" . $seimei->tenkaku . "画 " . $seimei->score($seimei->tenkaku) . "点/" .
		"総画（晩年期運）" . $seimei->soukaku . "画 " . $seimei->score($seimei->soukaku) . "点" ?>">
	<title><?php echo $seimei->sei ?> <?php echo $seimei->mei ?></title>
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" href="css/default.css" />
	<script type="text/javascript" src="js/okina.js"></script>
	<?php googleAnalytics() ?>
</head>
<?php
}

function seimeiBody(Seimei $seimei) {
?>
<body>
	<h2>あなた(<?php echo $seimei-sei . "さん (" . ($seimei->sei == 'M' ? '男性' : '女性'); ?>)の改名例</h2>
	<a href="http://www.seimei.asia/" target="blank">結果が表示されない場合や、もっと占いたい場合は「あじあ姓名うらない（本家サイト）」までどうぞ！赤ちゃんの命名にも使えます</a>
	<div><?php echo $seimei->meimei($seimei->sei) ?></div>
	<hr />
	
	<h2>あなた(<?php echo $seimei->sei . " " . $seimei->mei . "さん (" . ($seimei->sei == 'M' ? '男性' : '女性'); ?>の運勢 (総合得点：<?php echo $seimei->grand_score() ?>点)</h2>
	<h3>人画 <?php echo $seimei->jinkaku . "画 (" . $seimei->score($seimei->jinkaku) . "点)" ?></h3>
	<p style="color:blue;font-weight:bold;">基礎運。一生の運勢を司ります。結婚により姓が変わると基礎運も変化しますが、この場合中年以降に強く現れます。</p>
	<p><?php echo $seimei->jinkaku . "画:" . $seimei->reii_description($seimei->jinkaku) . " (" . $seimei->score($seimei->jinkaku) . "点)" ?></p>
	<p style="font-size:large;font-weight:bold;"><?php echo $seimei->mongon('jinkaku') ?></p>
	<hr />

	<h3>外画 <?php echo $seimei->gaikaku . "画 (" . $seimei->score($seimei->gaikaku) . "点)" ?></h3>
	<p style="color:blue;font-weight:bold;">対人運。対人関係および、家族・夫婦関係、友達関係など、外交面をあらわします。</p>
	<p><?php echo $seimei->gaikaku . "画：" . $seimei->reii_description($seimei->gaikaku) . " (" . $seimei->score($seimei->gaikaku) . "点)" ?></p>
	<p style="font-size:large;font-weight:bold;"><?php echo $seimei->mongon('gaikaku') ?></p>
	<hr />

	<h3>人画の下一桁 <?php echo $seimei->jinshimo . "画" ?></h3>
	<p style="color:blue;font-weight:bold;">性格。外面から見た性格を現しています。他人から自分がどう見えているのかの参考にしてください。</p>
	<p><?php echo $seimei->jinshimo . "画：" . $seimei->seikaku_description() ?></p>
	<p style="font-size:large;font-weight:bold;"><?php echo $seimei->mongon('seikaku') ?></p>
	<hr />
	
	<h3>健康運 (<?php echo ["◎" => "すごく良い", "○" => "良い", "△" => "ふつう", "×" => "悪い"][mb_substr($seimei->kenkou_description(), 6, 1)] ?>)</h3>
	<p style="color:blue;font-weight:bold;">健康運は三才の配置により決定します。吉数揃いの姓名も、健康に恵まれなければ活かされません。他の画数と合わせて判断してください。</p>
	<p>三才の配置：<?php echo mb_substr($seimei->kenkou_description(), 0, 5) ?></p>
	<p style="font-size:large;font-weight:bold;"><?php echo $seimei->mongon('kenkou') ?></p>
	<hr />
	
	<h3>天画 <?php echo $seimei->tenkaku . "画 (" . $seimei->score($seimei->tenkaku) . "点)" ?></h3>
	<p style="color:blue;font-weight:bold;">若年期の基礎運。幼少年期の運勢を支配し、青年期まで強くあらわれます。</p>
	<p><?php echo $seimei->tenkaku . "画：" . $seimei->reii_description($seimei->tenkaku) . " (" . $seimei->score($seimei->tenkaku) . "点)" ?></p>
	<p style="font-size:large;font-weight:bold;"><?php echo $seimei->mongon('tenkaku') ?></p>
	<hr />

	<h3>総画 <?php echo $seimei->soukaku . "画 (" . $seimei->score($seimei->soukaku) . "点)" ?></h3>
	<p style="color:blue;font-weight:bold;">晩年運。50歳前後からの運勢を支配します。ただし、基礎運の影響も残ります。</span><br>
	<p><?php echo $seimei->soukaku . "画：" . $seimei->reii_description($seimei->soukaku) . " (" . $seimei->score($seimei->soukaku) . "点)" ?></p>
	<p style="font-size:large;font-weight:bold;"><?php echo $seimei->mongon('soukaku') ?></p>
	<hr />
	<p style="font-size:small;">※ 鑑定文言については一部、山本哲生氏（故人：生没年不明）の編著「名前で読める自己の運命A・B・C」（ISBN不明）から引用しています。</p>
</body>
<?php
}
?>
