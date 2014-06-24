<?php 
header("Content-Type: text/html; charset=utf-8");
require 'seimei.php';
require 'reii.php';
require 'kenkou.php';
require 'seikaku.php';
require 'meimei.php';
require 'kanji.php';
date_default_timezone_set('UTC');

if (count($_POST) == 0) {
?>
<html>
	<head>
		<title>$B;3K\<0@+L>H=CG(B</title>
	</head>

	<body>
		<h1>$B;3K\<0@+L>H=CG(B</h1>

		<?php echo date(DATE_RFC2822) ?>
		<form action="" method="POST">
		$B@+!'(B<input type="text" name="sei" size="4">
		$BL>(B:<input type="text" name="mei" size="4">
		<input type="submit" value="$B4UDj(B">
		</form>
	</body>
</html>
<?php
} else {
	$seimei = New Seimei();
	$seimei->shindan($_POST['sei'], $_POST['mei'], 'male', 'yes', 'yes');
?>
<html>
	<head>
		<title>	<?php echo $seimei->sei ?> <?php echo $seimei->mei ?> $B$5$s$X$N%"%I%P%$%9(B</title>
	</head>

	<body>
		<h1><?php echo $seimei->sei ?> <?php echo $seimei->mei ?> $B$5$s$X$N%"%I%P%$%9(B</h1>

		<h2>$B<g1?(B:<?php echo $seimei->jinkaku ?>$B2h(B</h2>
		<p>$BEv?M$N0l@8$NCf?4$r;J$j$^$9!#7k:'$K$h$j@+$,JQ$o$k$H<g1?$bJQ$o$j$^$9$,!"CfG/0J9_$K6/$/8=$l$^$9!#(B<br /><?php echo $seimei->mongon('jinkaku') ?></p>

		<h2>$BBP?M1?!&<R8r1?(B:<?php echo $seimei->gaikaku ?>$B2h(B</h2>
		<p>$BBP?M4X78$d2HB2!&IWIX4X78!"M'C#4X78$K8=$l$F$-$^$9!#(B<br /><?php echo $seimei->mongon('gaikaku') ?></p>

		<h2>$B@-3J(B</h2>
		<p>$BEv?M$N30LLE*$J@-3J$r8=$7$^$9!#<+J,$,B>?M$+$i$I$&8+$($F$$$k$N$+;29M$K$J$j$^$9!#(B<br /><?php echo $seimei->mongon('seikaku') ?></p>

		<h2>$B7r9/1?(B($BBND4!&@:?@(B)</h2>
		<p>$BNc$(5H?tB7$$$N@+L>$G$"$C$F$b!"7r9/$K7C$^$l$J$1$l$P3h$+$5$;$^$;$s!#!J"$$OC1FH$G$NH=CG$,Fq$7$$!K(B<br /><?php echo $seimei->mongon('kenkou') ?></p>
		
		<h2>$B4pAC1?(B:<?php echo $seimei->chikaku ?>$B2h(B</h2>
		<p>$BMD>/G/4|$N1?@*$N5H6'$r;YG[$7!"@DG/4|$^$G:G$b6/$/:nMQ$7$^$9!#(B($B<cG/<T$NH=CG$O$3$A$i$,M-8z(B):<br /><?php echo $seimei->mongon('chikaku') ?></p>
		
		<h2>$BHUG/1?(B:<?php echo $seimei->soukaku ?>$B2h(B</h2>
		<p>50$B:PA08e$+$i6/$/8=$l$F$-$^$9!#$?$@$7!"<g1?$H4pAC1?$K:81&$5$l$^$9$N$GCm0U$7$F2<$5$$!#(B<br /><?php echo $seimei->mongon('soukaku') ?></p>
		
		<h2>$BCK;y$KIU$1$k$J$i(B</h2>
		<p><?php echo $seimei->meimei('M') ?></p>

		<h2>$B=w;y$KIU$1$k$J$i(B</h2>
		<p><?php echo $seimei->meimei('F') ?></p>
	</body>
</html>
<?php
}
?>
