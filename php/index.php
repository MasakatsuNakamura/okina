<?php 
header("Content-Type: application/json; charset=utf-8");
require 'seimei.php';
require 'reii.php';
require 'kenkou.php';
require 'seikaku.php';
require 'meimei.php';
require 'kanji.php';
date_default_timezone_set('UTC');

$return = [];

if (count($_REQUEST) > 0) {
	$seimei = New Seimei();
	$seimei->sei = $_REQUEST['sei'];
	$seimei->mei = $_REQUEST['mei'];
	$seimei->sex = $_REQUEST['sex'];
	$seimei->marry = $_REQUEST['marry'];
	$seimei->shindan();
	
	$return['header'] = $seimei->sei . " " . $seimei->mei . "さんへのアドバイス";

	$return['content'] = 
		"<h2>主運:" . $seimei->jinkaku ."画</h2>" .
		"<p>当人の一生の中心を司ります。結婚により姓が変わると主運も変わりますが、中年以降に強く現れます。</p>" .
		"<p>" . $seimei->mongon('jinkaku') . "</p>" .
		"<h2>対人運・社交運:" . $seimei->gaikaku . "画</h2>" .
		"<p>対人関係や家族・夫婦関係、友達関係に現れてきます。<br />" . $seimei->mongon('gaikaku') . "</p>" .
		"<h2>性格</h2>" .
		"<p>当人の外面的な性格を現します。自分が他人からどう見えているのか参考になります。</p>" . 
		"<p>" . $seimei->mongon('seikaku') . "</p>" .
		"<h2>健康運(体調・精神)</h2>" .
		"<p>例え吉数揃いの姓名であっても、健康に恵まれなければ活かさせません。（△は単独での判断が難しい）</p>" .
		"<p>" . $seimei->mongon('kenkou') . "</p>" .
		"<h2>基礎運:" . $seimei->chikaku . "画</h2>" .
		"<p>幼少年期の運勢の吉凶を支配し、青年期まで最も強く作用します。(若年者の判断はこちらが有効)</p>" .
		"<p>" . $seimei->mongon('chikaku') . "</p>" .
		"<h2>晩年運:" . $seimei->soukaku . "画</h2>" .
		"<p>50歳前後から強く現れてきます。ただし、主運と基礎運に左右されますので注意して下さい。</p>" .
		"<p>" . $seimei->mongon('soukaku') . "</p>" .
		"<h2>男児に付けるなら</h2>" .
		"<p>" . $seimei->meimei('M') . "</p>" .
		"<h2>女児に付けるなら</h2>" .
		"<p>" . $seimei->meimei('F') . "</p>";
}
echo json_encode($return);
?>
