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

	echo $seimei->sei . ' ' . $seimei->mei . 'さんへのアドバイス<br />\n';
	echo "天画:" . $seimei->tenkaku . "<br />\n" . $reii->mongon[$seimei->tenkaku] . "<br />\n";
	echo "人画:" . $seimei->jinkaku . "<br />\n" . $reii->mongon[$seimei->jinkaku] . "<br />\n";
	echo "地画:" . $seimei->chikaku . "<br />\n" . $reii->mongon[$seimei->chikaku] . "<br />\n";
	echo "外画:" . $seimei->gaikaku . "<br />\n" . $reii->mongon[$seimei->gaikaku] . "<br />\n";
	echo "総画:" . $seimei->soukaku . "<br />\n" . $reii->mongon[$seimei->soukaku] . "<br />\n";
	echo "性格:" . $seimei->seikaku . "<br />\n" . $seikaku->mongon[$seimei->seikaku] . "<br />\n";
	echo "健康:" . $seimei->kenkou . "<br />\n" . $kenkou->mongon[$seimei->kenkou] . "<br />\n";
	echo "エラー漢字:" . implode(",", $seimei->error);
?>