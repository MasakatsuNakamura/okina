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

$kantei = true;
if (count($_GET) > 0) {
	$seimei = New Seimei();
	$seimei->sei = $_GET['sei'];
	$seimei->mei = $_GET['mei'];
	$seimei->sex = $_GET['sex'];
	if (strlen($seimei->sei) > 0 && strlen($seimei->mei) > 0 && ($seimei->sex == 'M' || $seimei->sex == 'F')) {
		$seimei->shindan();
		if (count($seimei->error) == 0) {
			$kantei = false;
		} else {
			
		}
	}
}

?>
<html>
<head>
<meta charset="UTF-8">
<LINK REL="SHORTCUT ICON" HREF="favicon.ico"> 
<meta name="description" content="<?php echo $kantei ?
	"あじあ姓名うらないへようこそ！赤ちゃんの名まえをつけたり（選名）、キラキラネームの改名案を探したり、じぶんの運勢をうらなうなど、どしどし使ってね！" :
	$seimei->sei . " " . $seimei->mei . "さんの運勢 総合得点：" . $seimei->grand_score() . "点/" .
	"人画（基礎運）" . $seimei->jinkaku . "画 " . $seimei->score($seimei->jinkaku) . "点/" .
	"外画（外交運）" . $seimei->gaikaku . "画 " . $seimei->score($seimei->gaikaku) . "点/" .
	"性格" . $seimei->seikaku_description() . "/" .
	"健康運" . ["◎" => "すごく良い", "○" => "良い", "△" => "ふつう", "×" => "悪い"][mb_substr($seimei->kenkou_description(), 6, 1)] . "/" .
	"天画（若年期運）" . $seimei->tenkaku . "画 " . $seimei->score($seimei->tenkaku) . "点/" .
	"総画（晩年期運）" . $seimei->soukaku . "画 " . $seimei->score($seimei->soukaku) . "点" ?>">
<meta name="keywords" content="<?php echo $seimei->sei ?> <?php echo $seimei->mei ?> 翁 占い 姓名判断 姓名うらない 姓名占い 命名 選名 名前 新生児 赤ちゃん 出産準備 改名 DQNネーム キラキラネーム 改名 改姓 結婚相談 芸名 雅号 会社名 人事相談 熊崎式 だいぶつ あじあ">
<meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>あじあ姓名うらない</title>
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" href="http://code.jquery.com/mobile/1.4.2/jquery.mobile-1.4.2.min.css" />
	<link rel="stylesheet" href="css/default.css" />
	<script type="text/javascript" src="http://code.jquery.com/jquery-2.0.3.min.js"></script>
	<script type="text/javascript" src="http://code.jquery.com/mobile/1.4.2/jquery.mobile-1.4.2.min.js"></script>
	<script type="text/javascript" src="js/okina.js"></script>
	<?php googleAnalytics() ?>
</head>

<body data-ajax="false">
<?php
fbRoot();
if ($kantei) {
?>
	<div data-role="page" id="top" data-theme="a">
		<div data-role="header">
			<h1>あじあ姓名うらない <span class="ui-mini"></h1>
			<a href="#top" data-icon="home" class='ui-disabled'>ホーム</a>
			<a href="#query" data-icon="mail">問い合わせ</a>
		</div>
		<div data-role="content">
			<h2>うらなうには、名まえと性別を入力してね！</h2>
			<form data-ajax="false" method="GET">
				<div data-role="fieldcontain">
					<label for="sei">みょう字</label>
					<input type="text" name="sei" id="sei" />
				</div>
				<div data-role="fieldcontain">
					<label for="mei">名まえ</label>
					<input type="text" name="mei" id="mei" />
				</div>
				<div data-role="fieldcontain">
					<label for="sex">性別</label>
					<fieldset name="sex" data-role="controlgroup" data-type="horizontal" data-role="fieldcontain">
						<input type="radio" name="sex" id="sex-1" value="M" />
						<label for="sex-1">おとこ</label>
						<input type="radio" name="sex" id="sex-2" value="F" checked="checked" />
						<label for="sex-2">おんな</label>
						<input type="radio" name="sex" id="sex-3" value="M" />
						<label for="sex-3">それいがい</label>
					</fieldset>
				</div>
				<input type="submit" value="うらなう！" data-role="button" />
			</form>
			<p><a href="#mit-lisense">Copyright &copy; 2014 だいぶつ</a></p>
			<div class="ninja_onebutton">
			<h2>気に入ったらシェアをお願いします！</h2>
			<?php ninjaTools() ?>
			<a href="#setsumei" data-role="button">あじあ姓名うらないについて</a>
			<a href="#kaimei" data-role="button">改名について</a>
			<a href="http://daibutsuda.github.io/" data-role="button">だいぶつのホームページ</a>
			<a href="http://tsume.hateblo.jp/" data-role="button">(ブログ)隠すほどの爪なら無い</a>
		</div>
<?php
} else {
?>
		<div data-role="page" id="kantei" data-theme="a">
			<div data-role="header">
				<h1>あじあ姓名うらない</h1>
				<a href="./#top" data-icon="home" data-ajax="false">ホーム</a>
				<a href="./#query" data-icon="mail">問い合わせ</a>
			</div><!-- /header -->
			<div data-role="content">
				<h2><?php echo $seimei->sei ?>さんの命名・改名例</h2>
				<?php ninjaTools(); ?>
				<div data-role="collapsible" data-collapsed="true">
					<h2>男子（男性）の場合</h2>
					<div><?php echo $seimei->meimei('M') ?></div>
				</div>
				<div data-role="collapsible" data-collapsed="true">
					<h2>女子（女性）の場合</h2>
					<div><?php echo $seimei->meimei('F') ?></div>
				</div>
				
				<h2><?php echo $seimei->sei . " " . $seimei->mei ?>さんの運勢 (総合得点：<?php echo $seimei->grand_score() ?>点)</h2>
				<?php ninjaTools(); ?>
				<div data-role="collapsible" data-collapsed="true">
					<h2>人画 <?php echo $seimei->jinkaku . "画 (" . $seimei->score($seimei->jinkaku) . "点)" ?></h2>
					<p style="color:blue;font-weight:bold;">基礎運。一生の運勢を司ります。結婚により姓が変わると基礎運も変化しますが、この場合中年以降に強く現れます。</p>
					<p><?php echo $seimei->jinkaku . "画:" . $seimei->reii_description($seimei->jinkaku) . " (" . $seimei->score($seimei->jinkaku) . "点)" ?></p>
					<p style="font-size:x-large;font-weight:bold;"><?php echo $seimei->mongon('jinkaku') ?></p>
					<p style="font-size:small;">※ 鑑定文言について、山本哲生氏（故人：生没年不明）の編著「名前で読める自己の運命A・B・C」（ISBN不明）から引用しています。</p>
				</div>
				<div data-role="collapsible" data-collapsed="true">
					<h2>外画 <?php echo $seimei->gaikaku . "画 (" . $seimei->score($seimei->gaikaku) . "点)" ?></h2>
					<p style="color:blue;font-weight:bold;">対人運。対人関係および、家族・夫婦関係、友達関係など、外交面をあらわします。</p>
					<p><?php echo $seimei->gaikaku . "画：" . $seimei->reii_description($seimei->gaikaku) . " (" . $seimei->score($seimei->gaikaku) . "点)" ?></p>
					<p style="font-size:x-large;font-weight:bold;"><?php echo $seimei->mongon('gaikaku') ?></p>
					<p style="font-size:small;">※ 鑑定文言について、山本哲生氏（故人：生没年不明）の編著「名前で読める自己の運命A・B・C」（ISBN不明）から引用しています。</p>
				</div>
				<div data-role="collapsible" data-collapsed="true">
					<h2>人画の下一桁 <?php echo $seimei->jinshimo . "画" ?></h2>
					<p style="color:blue;font-weight:bold;">性格。外面から見た性格を現しています。他人から自分がどう見えているのかの参考にしてください。</p>
					<p><?php echo $seimei->jinshimo . "画：" . $seimei->seikaku_description() ?></p>
					<p style="font-size:x-large;font-weight:bold;"><?php echo $seimei->mongon('seikaku') ?></p>
				</div>
				<div data-role="collapsible" data-collapsed="true">
					<h2>健康運 (<?php echo ["◎" => "すごく良い", "○" => "良い", "△" => "ふつう", "×" => "悪い"][mb_substr($seimei->kenkou_description(), 6, 1)] ?>)</h2>
					<p style="color:blue;font-weight:bold;">健康運は三才の配置により決定します。吉数揃いの姓名も、健康に恵まれなければ活かされません。他の画数と合わせて判断してください。</p>
					<p>三才の配置：<?php echo mb_substr($seimei->kenkou_description(), 0, 5) ?></p>
					<p style="font-size:x-large;font-weight:bold;"><?php echo $seimei->mongon('kenkou') ?></p>
					<p style="font-size:small;">※ 鑑定文言について、山本哲生氏（故人：生没年不明）の編著「名前で読める自己の運命A・B・C」（ISBN不明）から引用しています。</p>
				</div>
				<div data-role="collapsible" data-collapsed="true">
					<h2>天画 <?php echo $seimei->tenkaku . "画 (" . $seimei->score($seimei->tenkaku) . "点)" ?></h2>
					<p style="color:blue;font-weight:bold;">若年期の基礎運。幼少年期の運勢を支配し、青年期まで強くあらわれます。</p>
					<p><?php echo $seimei->tenkaku . "画：" . $seimei->reii_description($seimei->tenkaku) . " (" . $seimei->score($seimei->tenkaku) . "点)" ?></p>
					<p style="font-size:x-large;font-weight:bold;"><?php echo $seimei->mongon('tenkaku') ?></p>
					<p style="font-size:small;">※ 鑑定文言について、山本哲生氏（故人：生没年不明）の編著「名前で読める自己の運命A・B・C」（ISBN不明）から引用しています。</p>
				</div>
				<div data-role="collapsible" data-collapsed="true">
					<h2>総画 <?php echo $seimei->soukaku . "画 (" . $seimei->score($seimei->soukaku) . "点)" ?></h2>
					<p style="color:blue;font-weight:bold;">晩年運。50歳前後からの運勢を支配します。ただし、基礎運の影響も残ります。</span><br>
					<p><?php echo $seimei->soukaku . "画：" . $seimei->reii_description($seimei->soukaku) . " (" . $seimei->score($seimei->soukaku) . "点)" ?></p>
					<p style="font-size:x-large;font-weight:bold;"><?php echo $seimei->mongon('soukaku') ?></p>
					<p style="font-size:small;">※ 鑑定文言について、山本哲生氏（故人：生没年不明）の編著「名前で読める自己の運命A・B・C」（ISBN不明）から引用しています。</p>
				</div>
			</div>
<?php
}
?>
			<div data-role='footer' data-position='fixed'>
			</div>
		</div>
	</div>
	<!-- 改名について -->
	<div data-role="page" id="kaimei" data-theme="a">
		<div data-role="header">
			<h1>あじあ姓名うらない <span class="ui-mini"><a href="#mit-lisense">Copyright &copy; 2014 だいぶつ</a></span></h1>
			<a href="#top" data-icon="home">ホーム</a>
			<a href="#query" data-icon="mail">改名について</a>
		</div>
		<div data-role='content'>
			<h2>改名について</h2>
			<p style="font-weight:bold;line-height:180%;">
				親に変な名前を付けられたせいで困っている、そんな方はいらっしゃいませんか。<br>
				その名前は改名できます。<br>
				名前の変更には、家庭裁判所に対して「名の変更許可の申し立て」を行います。<br>
				これには「正当な事由」が必要とされていますが、「珍奇な名、外国人に紛らわしい名又は難解、難読の文字を用いた名で社会生活上甚だしく支障のあること」という要件を満たせば「正当な事由」にあたるという、最高裁事務局の見解があります。<br>
				さあ、「<a href="#top">あじあ姓名うらない</a>」で改名にチャレンジしてみてください。
				もしいい名前が見つからなかった場合、「<a href="#query">問い合わせフォーム</a>」からお問い合わせください。
			</p>
		</div>
		<div data-role='footer' data-position='fixed'>
			<?php googleAdsense() ?>
		</div>
	</div>
	<!-- 説明 -->
	<div data-role="page" id="setsumei" data-theme="a">
		<div data-role="header">
			<h1>あじあ姓名うらない <span class="ui-mini"><a href="#mit-lisense">Copyright &copy; 2014 だいぶつ</a></span></h1>
			<a href="#top" data-icon="home">ホーム</a>
			<a href="#query" data-icon="mail">あじあ姓名うらないについて</a>
		</div>
		<div data-role='content'>
			<h2>あじあ姓名うらないについて</h2>
			<p style="font-weight:bold;line-height:180%;">
				<span style="color:red">姓名（名まえ）から運勢なんてわかるものなんでしょうか？</span>同姓同名で違う人生をたどる人がいっぱいいるのだから、もちろんそんなことはありえません。だけど、運命が完全に導き出されるわけではないにしろ、名まえが運勢に影響を与えると言う現象はしばしば見られます。<br>
				たとえば人の名前を聞いたときに「雰囲気どおりの名まえだ」と感じることはありませんか？<br>
				つまり、名まえは運命を決定付けるものではないにしろ、何らかの影響力を持っているものだと考えてもいいんじゃないでしょうか？<br>
				そして、運勢の傾向を事前に知っておけば、対策を立てることも容易になります。山にハイキングに出かけ、何も知らずに突然スズメバチの巣に出くわすのと、向こうから来た人に「もうすぐスズメバチの巣があるよ」と教えてもらうのと、どちらが良いでしょうか？<br>
				<a href="http://ja.wikipedia.org/wiki/%E7%86%8A%E5%B4%8E%E5%81%A5%E7%BF%81" target="_blank">熊崎健翁</a>らは多くの人々の名まえを調べ、その人の運命との関連を体系づけました。<br>
				このサイトでは<a href="http://ja.wikipedia.org/wiki/%E7%86%8A%E5%B4%8E%E5%81%A5%E7%BF%81" target="_blank">熊崎健翁</a>の弟子、山本哲生氏が熊崎式姓名学に基づいて編纂した本を参考にして、結果を表示しています。<br>
				さらに、この姓名うらないでは、苗字にあわせて優れた名まえを自動で選ぶうことの出来る<span style="color:red">新生児命名アドバイス機能</span>までついています。<br>
				あじあ姓名うらないのノウハウを利用し、赤ちゃんにつける名前、また芸名などの選定、キラキラネームの改名など、ご活用ください。これらの機能は無料です。ぜひお試しください。
			</p>
		</div>
		<div data-role='footer' data-position='fixed'>
			<?php googleAdsense() ?>
		</div>
	</div>
	<!-- 問い合わせフォーム -->
	<div data-role="page" id="query" data-theme="a">
		<div data-role="header">
			<h1>あじあ姓名うらない <span class="ui-mini"><a href="#mit-lisense">Copyright &copy; 2014 だいぶつ</a></span></h1>
			<a href="#top" data-icon="home">ホーム</a>
			<a href="#query" data-icon="mail" class="ui-disabled">問い合わせ</a>
		</div>
		<div data-role='content'>
			<h2>お問い合わせフォーム</h2>
			<div data-role="fieldcontain">
				<form action="mail-confirm.php" data-ajax="false" method="POST">
					<label for="email">メールアドレス</label>
					<input type="text" name="email">
					<label for="subject">タイトル</label>
					<input type="text" name="subject">
					<label for="query-content">お問い合わせ内容</label>
					<textarea name="query-content" id="query-content"></textarea>
					<input type="submit" value="投稿">
				</form>
			</div>
		</div>
		<div data-role='footer' data-position='fixed'>
			<?php googleAdsense() ?>
		</div>
	</div>
	<!-- 著作権表示 -->
	<div data-role='page' id='mit-lisense'>
		<div data-role='header'>
			<h1>著作権表示</h1>
			<a href="#top" data-icon="home">ホーム</a>
			<a href="#top" data-icon="back">戻る</a>
		</div>
		<div data-role='content'>
			<h2>著作権表示</h2>
			<p>このソフトウェアの、下記MITライセンスにかかる以外の部分については、「だいぶつ」が著作権を保持しています。転載・剽窃等は法律で禁じられています。</p>
			<h2>jQuery MobileおよびjQueryの著作権について</h2>
			<p>このソフトウェアは、MITライセンスに基づいて配布されているjQuery MobileおよびjQueryを含みます。これらのソフトウェアのライセンスは下記のとおりです。</p>
			<h2>The MIT License (MIT)</h2>
			<p>Copyright &copy; 2014 Daibutsu</p>
			<p>Permission is hereby granted, free of charge, to any person obtaining a copy
			of this software and associated documentation files (the "Software"), to deal
			in the Software without restriction, including without limitation the rights
			to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
			copies of the Software, and to permit persons to whom the Software is
			furnished to do so, subject to the following conditions:</p>
			
			<p>The above copyright notice and this permission notice shall be included in
			all copies or substantial portions of the Software.</p>
			
			<p>THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
			IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
			FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
			AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
			LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
			OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
			THE SOFTWARE.</p>
			<h2>MITライセンス(日本語訳)</h2>
			<p>Copyright&copy; 2014 だいぶつ</p>
			<p>以下に定める条件に従い、本ソフトウェアおよび関連文書のファイル（以下「ソフトウェア」）の複製を取得するすべての人に対し、ソフトウェアを無制限に扱うことを無償で許可します。これには、ソフトウェアの複製を使用、複写、変更、結合、掲載、頒布、サブライセンス、および/または販売する権利、およびソフトウェアを提供する相手に同じことを許可する権利も無制限に含まれます。</p>
			<p>上記の著作権表示および本許諾表示を、ソフトウェアのすべての複製または重要な部分に記載するものとします。</p>
			<p>ソフトウェアは「現状のまま」で、明示であるか暗黙であるかを問わず、何らの保証もなく提供されます。ここでいう保証とは、商品性、特定の目的への適合性、および権利非侵害についての保証も含みますが、それに限定されるものではありません。 作者または著作権者は、契約行為、不法行為、またはそれ以外であろうと、ソフトウェアに起因または関連し、あるいはソフトウェアの使用またはその他の扱いによって生じる一切の請求、損害、その他の義務について何らの責任も負わないものとします。</p>
			<h2>鑑定文言について</h2>
			<p>※ 鑑定文言について、一部を山本哲生氏（故人：生没年不明）の編著「（名前で読める自己の運命A・B・C）」（ISDN不明）から引用しています。</p>
			</div>
		<div data-role='footer' data-position='fixed'>
			<?php googleAdsense() ?>
		</div>
	</div>
	</body>
</html>
