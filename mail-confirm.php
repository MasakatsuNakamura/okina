<?php
if ($_SERVER["SERVER_NAME"] == "okina.herokuapp.com") {
	header("HTTP/1.1 301 Moved Permanently");
	header("Location: http://www.seimei.asia" . $_SERVER[REQUEST_URI]);
} else {
	header('Content-type: text/html; charset=utf-8;');
}

date_default_timezone_set('Asia/Tokyo');

require 'vendor/autoload.php';

$authcode = rand(10000, 99999);
?>
<html>
<head>
<meta charset="UTF-8">
<LINK REL="SHORTCUT ICON" HREF="favicon.ico">
<meta name="description" content="あじあ姓名うらないへようこそ！赤ちゃんの名まえをつけたり（選名）、じぶんの運勢をうらなったり、どしどし使ってね！">
<meta name="keywords" content="<?php echo $seimei->sei ?> <?php echo $seimei->mei ?> 翁 占い 姓名判断 姓名うらない 姓名占い 命名 選名 名前 新生児 赤ちゃん 出産準備 改名 DQNネーム 改姓 結婚相談 芸名 雅号 会社名 人事相談 熊崎式 だいぶつ あじあ">
<meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>あじあ姓名うらない</title>
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" href="http://code.jquery.com/mobile/1.4.2/jquery.mobile-1.4.2.min.css" />
	<link rel="stylesheet" href="css/default.css" />
	<script type="text/javascript" src="http://code.jquery.com/jquery-2.0.3.min.js"></script>
	<script type="text/javascript" src="http://code.jquery.com/mobile/1.4.2/jquery.mobile-1.4.2.min.js"></script>
	<script type="text/javascript" src="js/okina.js"></script>
	<script>
	  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
	  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
	  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
	  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');
	  ga('create', 'UA-26314420-4', 'auto');
	  ga('require', 'displayfeatures');
	  ga('send', 'pageview');
	</script>
	</head>
<body>
	<div data-role="page" id="top" data-theme="a">
		<div data-role="header">
			<h1>あじあ姓名うらない <span class="ui-mini"><a href="#mit-lisense">Copyright &copy; 2014 だいぶつ</a></span></h1>
			<a href="/#top" data-icon="home" data-ajax="false">ホーム</a>
			<a href="" data-icon="mail" class="ui-disabled">問い合わせ</a>
		</div>
		<div data-role='content'>
			<h2>お問い合わせフォーム(確認)</h2>
			<p>なりすましを防ぐため、認証コードの入力をお願いします。認証コードはメールで送信されます。</p>
			<div data-role="fieldcontain">
				<form action="mail.php" data-ajax="false" method="POST">
					<label for="email">メールアドレス</label>
					<input type="text" name="email" value="<?php echo $_POST['email'];?>" readonly="readonly">
					<label for="subject">タイトル</label>
					<input type="text" name="subject" value="<?php echo $_POST['subject'];?>" readonly="readonly">
					<label for="query-content">お問い合わせ内容</label>
					<textarea name="query-content" id="query-content" readonly="readonly"><?php echo $_POST['query-content'];?></textarea>
					<label for="query-content">認証コード</label>
					<input type="text" name="authcode">
					<input type="hidden" name="authcode-hash" value="<?php echo hash("haval160,4", $authcode);?>">
					<input type="submit" value="投稿">
				</form>
			</div>
		</div>
		<div data-role='footer' data-position='fixed'>
			<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
			<!-- あじあ姓名うらない -->
			<ins class="adsbygoogle"
			     style="display:inline-block;width:320px;height:100px"
			     data-ad-client="ca-pub-0413343113584981"
			     data-ad-slot="6868632444"></ins>
			<script>
			(adsbygoogle = window.adsbygoogle || []).push({});
			</script>
		</div>
	</div>
</body>

</html>
<?php
$sendgrid = new SendGrid('app26677709@heroku.com', 'xec1eqoo');
$message = new SendGrid\Email();
$message->
	addTo($_POST['email'])->
	setFrom('info@seimei.asia')->
	setSubject('[あじあ姓名うらない]認証コード')->
	setText('下記の認証コードをWeb画面に入力してください。' . PHP_EOL . PHP_EOL . 
			'　認証コード: ' . $authcode . PHP_EOL . PHP_EOL . 
			'このメールアドレスは送信専用です。このメールに返信しても届きませんのでご注意ください。' . PHP_EOL . PHP_EOL .
			'--' . PHP_EOL .
			'あじあ姓名うらない' . PHP_EOL .
			'http://www.seimei.asia/'
	);
$response = $sendgrid->send($message);
?>