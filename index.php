<?php
if ($_SERVER["SERVER_NAME"] == "okina.herokuapp.com") {
	header("HTTP/1.1 301 Moved Permanently");
	header("Location: http://www.seimei.asia" . $_SERVER[REQUEST_URI]);
} else {
	header('Content-type: text/html; charset=utf-8;');
}

require 'vendor/autoload.php';

require 'php/seimei.php';
require 'php/reii.php';
require 'php/kenkou.php';
require 'php/seikaku.php';
require 'php/meimei.php';
require 'php/kanji.php';
date_default_timezone_set('UTC');

$kantei = true;
if (count($_GET) > 0) {
	$seimei = New Seimei();
	$seimei->sei = $_GET['sei'];
	$seimei->mei = $_GET['mei'];
	$seimei->sex = $_GET['sex'];
	$seimei->marry = $_GET['marry'];
	if (strlen($seimei->sei) > 0 && strlen($seimei->mei) > 0 && ($seimei->sex == 'M' || $seimei->sex == 'F') && ($seimei->marry == 'yes' || $seimei->marry == 'no')) {
		$seimei->shindan();
		$kantei = false;
	}
} elseif (count($_POST) > 0) {
	Dotenv::load(__DIR__);
	$sendgrid = new SendGrid(process.env.SENDGRID_USERNAME, process.env.SENDGRID_PASSWORD);
	$message = new SendGrid\Email();
	$message->
		addTo('nakamuramasakatsu+heroku@gmail.com')->
		setFrom($_POST['email'])->
		setSubject('Query from www.seimei.asia')->
		setText('IP Address' . $$_POST['query-content']);
	$response = $sendgrid->send($message);
	$kantei=false;
}

?>
<html>
<head>
<meta charset="UTF-8">
<LINK REL="SHORTCUT ICON" HREF="favicon.ico"> 
<meta name="description" content="<?php echo $kantei ?
	"あじあ姓名うらないへようこそ！赤ちゃんの名まえをつけたり（選名）、じぶんの運勢をうらなったり、どしどし使ってね！" :
	$seimei->sei . " " . $seimei->mei . "さんの運勢 主運" . $seimei->jinkaku . "画 " . preg_replace("/<[^>]*>/","", $seimei->mongon('jinkaku')) .
	"対人運・社交運:" . $seimei->gaikaku . "画 " . preg_replace("/<[^>]*>/","", $seimei->mongon('gaikaku')) . "・・・" ?>">
<meta name="keywords" content="<?php echo $seimei->sei ?> <?php echo $seimei->mei ?> 翁 占い 姓名判断 姓名うらない 姓名占い 命名 選名 名前 新生児 赤ちゃん 出産準備 改名 改姓 結婚相談 芸名 雅号 会社名 人事相談 熊崎式 だいぶつ あじあ">
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
	  ga('send', 'pageview');
	
	</script>
</head> 
<body> 
	<div id="fb-root"></div>
	<script>(function(d, s, id) {
	  var js, fjs = d.getElementsByTagName(s)[0];
	  if (d.getElementById(id)) return;
	  js = d.createElement(s); js.id = id;
	  js.src = "//connect.facebook.net/ja_JP/sdk.js#xfbml=1&appId=482407305223650&version=v2.0";
	  fjs.parentNode.insertBefore(js, fjs);
	}(document, 'script', 'facebook-jssdk'));</script>
<?php
if ($kantei) {
?>
	<div data-role="page" id="top" data-theme="a">
		<div data-role="header">
			<h1>あじあ姓名うらない<span class="ui-mini"><a href="#mit-lisense">Copyright &copy; 2014 だいぶつ</a></span></h1>
			<a href="#top" data-icon="home" class='ui-disabled'>ホーム</a>
			<a href="#query" data-icon="mail">問い合わせ</a>
		</div>
		<div data-role="content">
			<h2>あじあ姓名うらないへようこそ！ <span class="fb-share-button" data-href="/" data-type="button_count"></span></h2>
			<div class="ninja_onebutton">
			<script type="text/javascript">
			//<![CDATA[
			(function(d){
			if(typeof(window.NINJA_CO_JP_ONETAG_BUTTON_0f8b16741da01b4bf2d81552e11cc4d6)=='undefined'){
			    document.write("<sc"+"ript type='text\/javascript' src='http:\/\/omt.shinobi.jp\/b\/0f8b16741da01b4bf2d81552e11cc4d6'><\/sc"+"ript>");
			}else{
			    window.NINJA_CO_JP_ONETAG_BUTTON_0f8b16741da01b4bf2d81552e11cc4d6.ONETAGButton_Load();}
			})(document);
			//]]>
			</script><span class="ninja_onebutton_hidden" style="display:none;"></span><span style="display:none;" class="ninja_onebutton_hidden"></span>
			</div>
			<h2>鑑定入力</h2>
			<form data-ajax="false" method="GET">
				<div data-role="fieldcontain">
					<label for="sei">姓</label>
					<input type="text" name="sei" id="sei" />
				</div>
				<div data-role="fieldcontain">
					<label for="mei">名</label>
					<input type="text" name="mei" id="mei" />
				</div>
				<div data-role="fieldcontain">
					<label for="sex">性別</label>
					<fieldset name="sex" data-role="controlgroup" data-type="horizontal" data-role="fieldcontain">
						<input type="radio" name="sex" id="sex-2" value="F" checked="checked" />
						<label for="sex-2">女性</label>
						<input type="radio" name="sex" id="sex-1" value="M"/>
						<label for="sex-1">男性</label>
					</fieldset>
				</div>
				<div data-role="fieldcontain">
					<label for="marry">結婚</label>
					<fieldset name="marry" data-role="controlgroup" data-type="horizontal" data-role="fieldcontain">
						<input type="radio" name="marry" id="marry-1" value="yes" />
						<label for="marry-1">している</label>
						<input type="radio" name="marry" id="marry-2" value="no"  checked="checked" />
						<label for="marry-2">していない</label>
					</fieldset>
				</div>
				<input type="submit" value="鑑定" data-role="button" />
			</form>
			<p>
			<strong>
			<h2>説明</h2>
			<span style="color:red">姓名（名まえ）から運勢なんてわかるものなんでしょうか？同姓同名で違う人生をたどる人がいっぱいいるのだから、もちろんそんなことはありえません。だけど、運命が完全に導き出されるわけではないにしろ、名まえが運勢に影響を与えると言う現象はしばしば見られます。<br>
			たとえば人の名前を聞いたときに「雰囲気どおりの名まえだ」と感じることはありませんか？<br>
			つまり、名まえは運命を決定付けるものではないにしろ、何らかの影響力を持っているものだと考えてもいいんじゃないでしょうか？<br>
			そして、運勢の傾向を事前に知っておけば、対策を立てることも容易になります。山にハイキングに出かけ、何も知らずに突然スズメバチの巣に出くわすのと、向こうから来た人に「もうすぐスズメバチの巣があるよ」と教えてもらうのと、どちらが良いでしょうか？<br>
			<a href="http://ja.wikipedia.org/wiki/%E7%86%8A%E5%B4%8E%E5%81%A5%E7%BF%81" target="_blank">熊崎健翁</a>らは多くの人々の名まえを調べ、その人の運命との関連を体系づけました。<br>
			この姓名うらないは、これらの先人たちの知恵の結晶であり、人類共有の宝です。<br>
			このサイトでは<a href="http://ja.wikipedia.org/wiki/%E7%86%8A%E5%B4%8E%E5%81%A5%E7%BF%81" target="_blank">熊崎健翁</a>の弟子、山本哲生氏が熊崎式姓名学に基づいて編纂した本を参考にして、結果を表示しています。<br>
			私は、この宝を多くの人に体験してもらいたいと考え、無料占いを公開することにしました。<br>
			さらに、この姓名うらないでは、苗字に基づき、優れた名まえを自動で選ぶうことの出来る<span style="color:red">新生児命名アドバイス機能</span>までついています。
			あじあ姓名うらないのノウハウを利用し、赤ちゃんにつける名前、また芸名などの選定、DQNネームの解明など、ご活用ください。これらの機能は無料です。ぜひお試しください。
			</strong>
			</p>
			<h2>あじあ姓名うらないAPI準備中</h2>
			<p>
				あじあ姓名うらないをコンピューターからご利用いただけるAPIを準備中です。Twitterアプリ・facebookアプリなど幅広くご利用いただけるよう考えております。
				ご興味のある方は<a href="#query">お問い合わせフォーム</a>からお問い合わせください。
			</p>
		</div>
<?php
} else {
?>
		<div data-role="page" id="kantei" data-theme="a">
			<div data-role="header">
				<h1>あじあ姓名うらない <span class="ui-mini"><a href="#mit-lisense">Copyright &copy; 2014 だいぶつ</a></span></h1>
				<a href="./#top" data-icon="home" data-ajax="false">ホーム</a>
				<a href="./#query" data-icon="mail">問い合わせ</a>
			</div><!-- /header -->
			<div data-role="content">
				<h2><?php echo $seimei->sei ?>さんの子どもに名前を付けるなら・・・</h2>
				<div class="ninja_onebutton">
				<script type="text/javascript">
				//<![CDATA[
				(function(d){
				if(typeof(window.NINJA_CO_JP_ONETAG_BUTTON_0f8b16741da01b4bf2d81552e11cc4d6)=='undefined'){
				    document.write("<sc"+"ript type='text\/javascript' src='http:\/\/omt.shinobi.jp\/b\/0f8b16741da01b4bf2d81552e11cc4d6'><\/sc"+"ript>");
				}else{
				    window.NINJA_CO_JP_ONETAG_BUTTON_0f8b16741da01b4bf2d81552e11cc4d6.ONETAGButton_Load();}
				})(document);
				//]]>
				</script><span class="ninja_onebutton_hidden" style="display:none;"></span><span style="display:none;" class="ninja_onebutton_hidden"></span>
				</div>
				<p>結果をみんなにシェアしましょう！ <span class="fb-share-button" data-href="/?sei=<?php echo urlencode($seimei->sei) . "&mei=" . urlencode($seimei->mei) . "&sex=" . $seimei->sex . "&marry=" . $seimei->marry ?>" data-type="button_count"></span></p>
				<div data-role="collapsible" data-collapsed="false">
					<h2>【命名例】男の子につけるなら・・・</h2>
					<div><?php echo $seimei->meimei('M') ?></div>
				</div>
				<div data-role="collapsible" data-collapsed="false">
					<h2>【命名例】女の子につけるなら・・・</h2>
					<div><?php echo $seimei->meimei('F') ?></div>
				</div>
				<h2><?php echo $seimei->sei . " " . $seimei->mei ?>さんの運勢</h2>
				<p>※ 鑑定文言について、一部を山本哲生氏（故人：生没年不明）の編著「名前で読める自己の運命A・B・C」（ISBN不明）から引用しています。</p>
				<div data-role="collapsible" data-collapsed="false">
					<h2>基礎運(人画）　<span class="ui-mini">一生の運勢を司ります。結婚により姓が変わると基礎運も変化しますが、この場合中年以降に強く現れます。</span></h2>
					<div><?php echo $seimei->jinkaku ?>画<br><?php echo $seimei->mongon('jinkaku') ?></div>
				</div>
				<div data-role="collapsible" data-collapsed="false">
					<h2>対人運（外画）　<span class="ui-mini">対人関係および、家族・夫婦関係、友達関係など、外交面をあらわします。</span></h2>
					<div><?php echo $seimei->gaikaku ?>画<br><?php echo $seimei->mongon('gaikaku') ?></div>
				</div>
				<div data-role="collapsible" data-collapsed="false">
					<h2>性格(人画の下一桁）　<span class="ui-mini">外面から見た性格を現しています。他人から自分がどう見えているのかの参考にしてください。</span></h2>
					<div><?php echo $seimei->jinshimo . "画:" . $seimei->mongon('seikaku') ?></div>
				</div>
				<div data-role="collapsible" data-collapsed="false">
					<h2>健康運（陰陽５行３才の組み合わせにより算出）<span class="ui-mini">吉数揃いの姓名も、健康に恵まれなければ活かされません。他の画数と合わせて判断してください。</span></h2>
					<div><?php echo $seimei->mongon('kenkou') ?></div>
				</div>
				<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
				<div data-role="collapsible" data-collapsed="false">
					<h2>基礎運（天画）<span class="ui-mini">幼少年期の運勢を支配し、青年期まで強くあらわれます。</span></h2>
					<div><?php echo $seimei->chikaku ?>画：<?php echo $seimei->mongon('chikaku') ?></p>
					</div>
				</div>
				<div data-role="collapsible" data-collapsed="false">
					<h2>晩年運（総画）<span class="ui-mini">50歳前後からの運勢を支配します。ただし、基礎運の影響も残ります。</span></h2>
					<div><?php echo $seimei->soukaku ?>画：<?php echo $seimei->mongon('soukaku') ?></div>
				</div>
<?php
}
?>
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
	</div>
	<div data-role="page" id="query" data-theme="a">
		<div data-role="header">
			<h1>あじあ姓名うらない <span class="ui-mini"><a href="#mit-lisense">Copyright &copy; 2014 だいぶつ</a></span></h1>
			<a href="#top" data-icon="home">ホーム</a>
			<a href="#query" data-icon="mail" class="ui-disabled">問い合わせ</a>
		</div>
		<div data-role='content'>
			<h2>お問い合わせフォーム</h2>
			<div data-role="fieldcontain">
				<form data-ajax="false" method="POST">
					<label for="email">メールアドレス</label>
					<input type="text" name="email">
					<label for="query-content">お問い合わせ内容</label>
					<textarea name="query-content" id="query-content"></textarea>
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
