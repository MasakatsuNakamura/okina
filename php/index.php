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
	echo $seimei->tenkaku . '<br />' . $reii->mongon[$seimei->tenkaku];
	echo $seimei->jinkaku . '<br />' . $reii->mongon[$seimei->jinkaku];
	echo $seimei->chikaku . '<br />' . $reii->mongon[$seimei->chikaku];
	echo $seimei->soukaku . '<br />' . $reii->mongon[$seimei->soukaku];
	echo $seimei->seikaku . '<br />' . $seikaku->mongon[$seimei->seikaku];
	echo $seimei->kenkou . '<br />' . $kenkou->mongon[$seimei->kenkou];
?>