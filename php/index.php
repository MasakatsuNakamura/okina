<?php 
	require 'seimei.php';
	require 'reii.php';
	require 'kenkou.php';
	require 'seikaku.php';
	
	$seimei = New Seimei();
	$reii = New Reii();
	$kenkou = New Kenkou();
	$seikaku = New Seikaku();
	print_r($seimei->kanji);
	
	$seimei->kakusu('中村', '昌克');

	echo $seimei->sei . ' ' . $seimei->mei . 'さんへのアドバイス<br />\n';
	echo '天画:' . $seimei->tenkaku . '<br />' . $reii->mongon[$seimei->tenkaku] . '<br />\n';
	echo '人画:' . $seimei->jinkaku . '<br />' . $reii->mongon[$seimei->jinkaku] . '<br />\n';
	echo '地画:' . $seimei->chikaku . '<br />' . $reii->mongon[$seimei->chikaku] . '<br />\n';
	echo '総画:' . $seimei->soukaku . '<br />' . $reii->mongon[$seimei->soukaku] . '<br />\n';
	echo '性格:' . $seimei->seikaku . '<br />' . $seikaku->mongon[$seimei->seikaku] . '<br />\n';
	echo '健康:' . $seimei->kenkou . '<br />' . $kenkou->mongon[$seimei->kenkou] . '<br />\n';
?>