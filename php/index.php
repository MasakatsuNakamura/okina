<?php 
	require 'seimei.php';
	
	$seimei = New Seimei();
	$seimei->kakusu('中村', '昌克');

?>
<html>
	<head>
		<title>	<?php echo $seimei->sei ?> <?php echo $seimei->mei ?> さんへのアドバイス</title>
	</head>
	<body>
		<?php echo $seimei->sei ?> <?php echo $seimei->mei ?> さんへのアドバイス<br />
		天画: <?php echo $seimei->tenkaku ?><br /><?php echo $seimei->mongon('tenkaku') ?><br />
		人画: <?php echo $seimei->jinkaku ?><br /><?php echo $seimei->mongon('jinkaku') ?><br />
		地画: <?php echo $seimei->chikaku ?><br /><?php echo $seimei->mongon('chikaku') ?><br />
		外画: <?php echo $seimei->gaikaku ?><br /><?php echo $seimei->mongon('gaikaku') ?><br />
		総画: <?php echo $seimei->soukaku ?><br /><?php echo $seimei->mongon('soukaku') ?><br />
		性格: <?php echo $seimei->seikaku ?><br /><?php echo $seimei->mongon('seikaku') ?><br />
		健康: <?php echo $seimei->kenkou ?><br /><?php echo $seimei->mongon('kenkou') ?><br />
		エラー漢字: <?php echo implode(",", $seimei->error); ?>
	</body>
</html>
