<?php 
	require 'seimei.php';
	require 'reii.php';
	require 'kenkou.php';
	require 'seikaku.php';
	
	$seimei = New Seimei();
	$reii = New Reii();
	$kenkou = New Kenkou();
	$seikaku = New Seikaku();
	
	$seimei->kakusu('中村', '昌克');

?>
<html>
	<head>
		<title>	<?php echo $seimei->sei ?> <?php echo $seimei->mei ?> さんへのアドバイス</title>
	</head>
	<body>
		<?php echo $seimei->sei ?> <?php echo $seimei->mei ?> さんへのアドバイス<br />
		天画: <?php echo $seimei->tenkaku ?><br /><?php echo $reii->mongon[$seimei->tenkaku] ?><br />
		人画: <?php echo $seimei->jinkaku ?><br /><?php echo $reii->mongon[$seimei->jinkaku] ?><br />
		地画: <?php echo $seimei->chikaku ?><br /><?php echo $reii->mongon[$seimei->chikaku] ?><br />
		外画: <?php echo $seimei->gaikaku ?><br /><?php echo $reii->mongon[$seimei->gaikaku] ?><br />
		総画: <?php echo $seimei->soukaku ?><br /><?php echo $reii->mongon[$seimei->soukaku] ?><br />
		性格: <?php echo $seimei->seikaku ?><br /><?php echo $seikaku->mongon[$seimei->seikaku] ?><br />
		健康: <?php echo $seimei->kenkou ?><br /><?php echo $kenkou->mongon[$seimei->kenkou] ?><br />
		エラー漢字: <?php echo implode(",", $seimei->error); ?>
	</body>
</html>
