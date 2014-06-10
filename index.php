<?php 
header("Content-Type: text/html; charset=utf-8");

require 'seimei.php';
	
$seimei = New Seimei();
$seimei->kakusu('中村', '昌克', 'male', 'yes', 'yes');

?>
<html>
	<head>
		<title>	<?php echo $seimei->sei ?> <?php echo $seimei->mei ?> さんへのアドバイス</title>
	</head>

	<body>
		<h1><?php echo $seimei->sei ?> <?php echo $seimei->mei ?> さんへのアドバイス</h1>

		<h2>主運:当人の一生の中心を司ります。結婚により姓が変わると主運も変わりますが、中年以降に強く現れます。</h2>
		<p><?php echo $seimei->jinkaku ?>画<br /><?php echo $seimei->mongon('jinkaku') ?></p>

		<h2>対人運・社交運；対人関係や家族・夫婦関係、友達関係に現れてきます。</h2>
		<p><?php echo $seimei->gaikaku ?>画<br /><?php echo $seimei->mongon('gaikaku') ?></p>

		<h2>性格:当人の外面的な性格を現します。自分が他人からどう見えているのか参考になります。</h2>
		<p><?php echo $seimei->mongon('seikaku') ?></p>

		<h2>健康運(体調・精神)；例え吉数揃いの姓名であっても、健康に恵まれなければ活かさせません。（△は単独での判断が難しい）</h2>
		<p><?php echo $seimei->mongon('kenkou') ?></p>
		
		<h2>基礎運:幼少年期の運勢の吉凶を支配し、青年期まで最も強く作用します。(若年者の判断はこちらが有効):</h2>
		<p><?php echo $seimei->chikaku ?>画<br /><?php echo $seimei->mongon('chikaku') ?></p>
		
		<h2>晩年運 ；50歳前後から強く現れてきます。ただし、主運と基礎運に左右されますので注意して下さい。</h2>
		<p><?php echo $seimei->soukaku ?>画<br /><?php echo $seimei->mongon('soukaku') ?></p>

		<h2>エラー漢字: <?php echo implode(",", $seimei->error); ?></h2>
	</body>
</html>
