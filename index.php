<?php 
header("Content-Type: text/html; charset=utf-8");
require 'seimei.php';

if (count($_POST) == 0) {
?>
<html>
	<head>
		<title>山本式姓名判断</title>
	</head>

	<body>
		<h1>山本式姓名判断</h1>

		<form action="" method="POST">
		姓：<input type="text" name="sei" size="4">
		名:<input type="text" name="mei" size="4">
		<input type="submit" value="鑑定">
		</form>
	</body>
</html>
<?php
} else {
	$seimei = New Seimei();
	$seimei->shindan($_POST['sei'], $_POST['mei'], 'male', 'yes', 'yes');
?>
<html>
	<head>
		<title>	<?php echo $seimei->sei ?> <?php echo $seimei->mei ?> さんへのアドバイス</title>
	</head>

	<body>
		<h1><?php echo $seimei->sei ?> <?php echo $seimei->mei ?> さんへのアドバイス</h1>

		<h2>主運:<?php echo $seimei->jinkaku ?>画</h2>
		<p>当人の一生の中心を司ります。結婚により姓が変わると主運も変わりますが、中年以降に強く現れます。<br /><?php echo $seimei->mongon('jinkaku') ?></p>

		<h2>対人運・社交運:<?php echo $seimei->gaikaku ?>画</h2>
		<p>対人関係や家族・夫婦関係、友達関係に現れてきます。<br /><?php echo $seimei->mongon('gaikaku') ?></p>

		<h2>性格</h2>
		<p>当人の外面的な性格を現します。自分が他人からどう見えているのか参考になります。<br /><?php echo $seimei->mongon('seikaku') ?></p>

		<h2>健康運(体調・精神)</h2>
		<p>例え吉数揃いの姓名であっても、健康に恵まれなければ活かさせません。（△は単独での判断が難しい）<br /><?php echo $seimei->mongon('kenkou') ?></p>
		
		<h2>基礎運:<?php echo $seimei->chikaku ?>画</h2>
		<p>幼少年期の運勢の吉凶を支配し、青年期まで最も強く作用します。(若年者の判断はこちらが有効):<br /><?php echo $seimei->mongon('chikaku') ?></p>
		
		<h2>晩年運:<?php echo $seimei->soukaku ?>画</h2>
		<p>50歳前後から強く現れてきます。ただし、主運と基礎運に左右されますので注意して下さい。<br /><?php echo $seimei->mongon('soukaku') ?></p>
		
		<h2>男児に付けるなら</h2>
		<p><?php echo $seimei->meimei('M') ?></p>

		<h2>女児に付けるなら</h2>
		<p><?php echo $seimei->meimei('F') ?></p>
	</body>
</html>
<?php
}
?>
