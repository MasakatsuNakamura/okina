<?php
if ($_SERVER["SERVER_NAME"] == "okina.herokuapp.com") {
	header("HTTP/1.1 301 Moved Permanently");
	header("Location: http://www.seimei.asia" . $_SERVER[REQUEST_URI]);
} else {
	header('Content-type: text/html; charset=utf-8;');
}

date_default_timezone_set('Asia/Tokyo');

require 'vendor/autoload.php';

require 'php/seimei.php';
require 'php/reii.php';
require 'php/kenkou.php';
require 'php/seikaku.php';
require 'php/meimei.php';
require 'php/kanji.php';
require 'php/snipets.php';

?>
<html>
<?php
if (array_key_exists('sei', $_POST) && array_key_exists('mei', $_POST) && array_key_exists('sex', $_POST)) {
	$seimei = New Seimei();
	$seimei->sei = $_POST['sei'];
	$seimei->mei = $_POST['mei'];
	$seimei->sex = ($_POST['sex'] == 'M' ? 'M' : 'F');
	if (mb_strlen($seimei->sei) > 0 || mb_strlen($seimei->mei) > 0) {
		$seimei->shindan();
		if (count($seimei->error) == 0) {
			seimeiWebHeader($seimei);
			echo '<body>';
			seimeiBody($seimei);
			seimeiWebForm();
			echo '</body>';
		} else {
			seimeiWebHeader(null);
			echo '<body>';
			fbRoot();
			echo '<div>';
			fbLike();
			echo '判定できない漢字が含まれます。<br>' . implode ('、', $seimei->error);
			echo '</div>';
			seimeiWebForm();
			echo '</body>';
		}
	} else {
		seimeiWebHeader(null);
		echo '<body>';
		seimeiWebForm();
		echo '</body>';
	}
} else {
	seimeiWebHeader(null);
	echo '<body>';
	seimeiWebForm();
	echo '</body>';
}
?>
	</body>
</html>
