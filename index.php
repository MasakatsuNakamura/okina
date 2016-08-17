<?php
header('Content-type: text/html; charset=utf-8;');

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
	<?php seimeiWebHeader(); ?>
	<body>
	<?php
	fbRoot();

	if (array_key_exists('sei', $_POST) && array_key_exists('mei', $_POST) && array_key_exists('sex', $_POST)) {
		$seimei = New Seimei();
		$seimei->sei = $_POST['sei'];
		$seimei->mei = $_POST['mei'];
		$seimei->sex = ($_POST['sex'] == 'F' ? 'F' : 'M');
		if (mb_strlen($seimei->sei) > 0 || mb_strlen($seimei->mei) > 0) {
			$seimei->shindan();
			if (count($seimei->error) == 0) {
				seimeiBody($seimei);
			} else {
				errorKanji($seimei->error);
			}
		}
	}
	seimeiWebForm();
	?>
	</body>
</html>
