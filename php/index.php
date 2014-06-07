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

	echo $seimei->sei . ' ' . $seimei->mei . 'さんへのアドバイス<br />';
	echo $seimei->kanji['中'] . "<br />";
	echo $seimei->kanji['村'] . "<br />";
	echo $seimei->kanji['昌'] . "<br />";
	echo $seimei->kanji['克'] . "<br />";
	echo '天画:' . $seimei->tenkaku . '<br />' . $reii->mongon[$seimei->tenkaku] . '<br />';
	echo '人画:' . $seimei->jinkaku . '<br />' . $reii->mongon[$seimei->jinkaku] . '<br />';
	echo '地画:' . $seimei->chikaku . '<br />' . $reii->mongon[$seimei->chikaku] . '<br />';
	echo '総画:' . $seimei->soukaku . '<br />' . $reii->mongon[$seimei->soukaku] . '<br />';
	echo '性格:' . $seimei->seikaku . '<br />' . $seikaku->mongon[$seimei->seikaku] . '<br />';
	echo '健康:' . $seimei->kenkou . '<br />' . $kenkou->mongon[$seimei->kenkou] . '<br />';
?>