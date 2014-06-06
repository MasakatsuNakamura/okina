<?php
include("./jcode.php");
include("./point.php");

$password = "windom";

if (strstr($HTTP_POST_VARS["password"], $password)) {

switch ($HTTP_POST_VARS["mode"]) {

case "meimei" :
    $sei = trim($HTTP_POST_VARS["sei"]);
    $birthmonth = trim($HTTP_POST_VARS["birthmonth"]);
    $birthday = trim($HTTP_POST_VARS["birthday"]);
    $sex = trim($HTTP_POST_VARS["sex"]);
	$confirm = trim($HTTP_POST_VARS["confirm"]);
	$sei = HANtoZEN($sei, 2);

	if (strstr($confirm, "no")) {
		echo "<body>利用規約にご同意いただけない場合、ご利用はご遠慮いただいております。<br>";
		echo "<form action=baby.php method=POST><input type=hidden name=mode value=form><input type=hidden name=password value=" . $password . "><input type=submit value=フォームに戻る></form></body>";
		exit();
	}
	if ($sei == "") {
		echo "<body>姓の欄をご入力いただけないと、命名が出来ません。<br>";
		echo "<form action=baby.php method=POST><input type=hidden name=mode value=form><input type=hidden name=password value=" . $password . "><input type=submit value=フォームに戻る></form></body>";
 		exit();
	}
	if ((($birthmonth == 4 or $birthmonth == 6 or $birthmonth == 9 or $birthmonth == 11) and 
		$birthday == 31) or ($birthmonth == 2 and $birthday >29)) {
		echo "<body>" . $birthmonth . "月" . $birthday . "日：正しい誕生日が入力されていません。<br>";
		echo "<form action=baby.php method=POST><input type=hidden name=mode value=form><input type=hidden name=password value=" . $password . "><input type=submit value=フォームに戻る></form></body>";
		exit();
	}

	$sei1 = substr($sei, 0, 2);
	$sei2 = substr($sei, strlen($sei)-2, 2);

	$sei1array = unpack("C2chars", $sei1);
	$sei1code = $sei1array{"chars1"} *256 + $sei1array{"chars2"};
	$sei2array = unpack("C2chars", $sei2);
	$sei2code = $sei2array{"chars1"} *256 + $sei2array{"chars2"};

	$db = pg_connect("dbname=keishinsya host=rdb.mahoroba.ne.jp port=5432 user=keishinsya password=C7tH6v");

	if (ereg("[0-9][0-9]", $sei1)) {
		$kakusu1[0] = (int) ereg_replace("^0", "", $sei1);
	} else {
		$request = pg_query($db, "select kakusu from kanji where kanji=" . $sei1code . ";");
		$rows = pg_num_rows($request);
		for ($i = 0; $i < $rows; $i++) {
			$kakusu1 = pg_fetch_row($request, $i);
		}
	}

	if (ereg("[0-9][0-9]", $sei2)) {
		$kakusu2[0] = (int) ereg_replace("^0", "", $sei2);
	} else {
		$request = pg_query($db, "select kakusu from kanji where kanji=" . $sei2code . ";");
		$rows = pg_num_rows($request);
		for ($i = 0; $i < $rows; $i++) {
			$kakusu2 = pg_fetch_row($request, $i);
		}
	}
	if ($kakusu1[0] == 0 or $kakusu2[0] == 0) {
		echo "<body>姓に使用されている漢字がデータベースにありません。ご入力内容をご確認の上、間違いがなければハンドメイドでのご依頼をお願いいたします<br>";
		echo "<a href=index.html>戻る</a></body>";
	}

	$sei1kaku = $kakusu1[0];
	$sei2kaku = $kakusu2[0];

	$request = pg_query($db, "select priority,mei1,mei2 from newname where sei1=" . $sei1kaku. " and sei2=" . $sei2kaku. " and sex ='" . $sex . "';");
	$rows = pg_num_rows($request);
	for ($i = 0; $i < $rows; $i++) {
		$row = pg_fetch_row($request, $i);
		$newname{$row[0] . ",1"} = $row[1];
		$newname{$row[0] . ",2"} = $row[2];
	}
	$numbers = 0;
	for ($i = 1; $i <= 4; $i++) {
		$mei1 = $newname{$i . ",1"};
		$mei2 = $newname{$i . ",2"};
		$points[$i] = point($sei1kaku,$sei2kaku,$mei1,$mei2,$sex);
		if ($mei1 != "") {
			$request = pg_query($db, "select kanji1,kanji2,kanji3,kanji4,yomi from meimei_sample where mei1=" . $mei1 . " and mei2=" . $mei2 . " and sex ='" . $sex . "';");
			$rows = pg_num_rows($request);
			$sample = "";
			for ($j = 0; $j < $rows; $j++) {
				$row = pg_fetch_row($request, $j);
				for ($k = 0; $k < 4; $k++) {
					$value = $row[$k];
					if ($value > 0) {
						$kanji1 = floor($value / 256);
						$kanji2 = $value % 256;
						$sample .= pack("C", $kanji1) . pack("C", $kanji2);
					}
				}
				$sample .= "=" . JcodeConvert($row[4], 1, 2) . " ";
			}
			$samplerows[$i] = $rows;
			if ($rows <= 5) {
				$price[$i] = 1000;
			} else if ($rows <= 19) {
				$price[$i] = 3000;
			} else {
				$price[$i] = 5000;
			}
			$numbers += $rows;
		}
	}
	if ($numbers > 0) {
		include("./meimei.html");
	} else {
		include("./noresult.html");
	}
	break;

case "kakunin" :
	$sei = trim($HTTP_POST_VARS["sei"]);
	$birthmonth = trim($HTTP_POST_VARS["birthmonth"]);
	$birthday = trim($HTTP_POST_VARS["birthday"]);
	$sex = trim($HTTP_POST_VARS["sex"]);
	$mail = trim($HTTP_POST_VARS["mail"]);
	$mailconf = trim($HTTP_POST_VARS["mailconf"]);
	$select = trim($HTTP_POST_VARS["select"]);
	$points[1] = trim($HTTP_POST_VARS["points1"]);
	$points[2] = trim($HTTP_POST_VARS["points2"]);
	$points[3] = trim($HTTP_POST_VARS["points3"]);
	$points[4] = trim($HTTP_POST_VARS["points4"]);
	$price[1] = trim($HTTP_POST_VARS["price1"]);
	$price[2] = trim($HTTP_POST_VARS["price2"]);
	$price[3] = trim($HTTP_POST_VARS["price3"]);
	$price[4] = trim($HTTP_POST_VARS["price4"]);
	$samplerows[1] = trim($HTTP_POST_VARS["samplerows1"]);
	$samplerows[2] = trim($HTTP_POST_VARS["samplerows2"]);
	$samplerows[3] = trim($HTTP_POST_VARS["samplerows3"]);
	$samplerows[4] = trim($HTTP_POST_VARS["samplerows4"]);

	if (strstr($mail, $mailconf)) {
		include("./kakunin.html");
	} else {
		echo "<body>メールアドレスが正しくありません</body>\n";
	}
	break;

case "kekka" :
	$sei = trim($HTTP_POST_VARS["sei"]);
	$birthmonth = trim($HTTP_POST_VARS["birthmonth"]);
	$birthday = trim($HTTP_POST_VARS["birthday"]);
	$sex = trim($HTTP_POST_VARS["sex"]);
	$mail = trim($HTTP_POST_VARS["mail"]);
	$select = trim($HTTP_POST_VARS["select"]);
	include("./kekka.html");
	break;

case "form" :
	include("./form.html");
	break;

} # end switch

} else {
?>

<html>
<body>
<meta http-equiv="Context-Type" content="text/html;charset=SJIS">
<title>パスワード入力</title></head>
<body bgcolor="white">

パスワードを入力してください
<form action="./baby.php" method="post">
<input type=password name=password>
<input type="hidden" name="mode" value="form">
<input value= "実行" type="submit">

<br>
</body>
</html>

<?php
}
?>
