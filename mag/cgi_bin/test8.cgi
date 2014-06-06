#!/usr/local/bin/perl
$|=1;
require "jcode.pl";
require "cgi-lib.pl";

$root = "/~kazu-y/mag";
$cgipath = "/~kazu-y/mag/cgi_bin";
$baseurl = "http://www2.mahoroba.ne.jp";

##### CGI変数取りこみ#####
&ReadParse();
$ans = $in{'ans'};
$mis = $in{'mis'};
$name = $in{'name'};
$email = $in{'email'};
#####正解の確認#####
if ($ans ne "3") {
    $mis = $mis + 1;
    #正解でない場合、misカウントに1を加算
}
#####3問以上間違えたかどうかチェック#####
if ($mis >= 3) {
	# 3問以上間違えると、失格のメッセージを出す。
	$msg = <<"EOK";
Content-type: text/html

<HTML>
<HEAD>
   <TITLE>検定中止</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=SHIFT_JIS">
</HEAD>
<BODY BGCOLOR="#FFFFFF">
<P>
<HR>
<FONT COLOR="#FF0000">検定を中止致します。</FONT><BR>
<HR>
  3問間違えましたので、これ以上、全問正解でも合格点には達しません。また次回、講義をお受けになり、チャレンジしてみて下さい。長い間、お付き合い頂き誠に有り難うございました。<BR>
翁<BR>
<HR>
<A HREF="http://www2.mahoroba.ne.jp/~kazu-y/i-mode.html" accesskey=1>1→翁のホームページへ</A><BR>
</P>
</BODY>
</HTML>
EOK
	&jcode'convert(*msg, "sjis", "euc");
	print $msg;
} else {
	# 次の問題を表示
	$msg = <<"EOM";
Content-type: text/html

<HTML>
<HEAD>
   <TITLE>第8問</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=SHIFT_JIS">
</HEAD>
<BODY BGCOLOR="#FFFFFF" TEXT="#000000" LINK="#0000FF">
<P>
<HR>
第8問<BR>
<HR>
三才の配置(天画・人画・地画の陰陽五行配列)に関する説明文の中から間違っているものを一つ選んで下さい。</P>
<P><FORM ACTION="$cgipath/test9.cgi" METHOD=POST>
   <P><INPUT TYPE=radio NAME=ans VALUE=1 CHECKED>天画、地画、人画すべてが「火」で揃う場合、才能や能力を発揮し仕事運や成功運は旺盛なれど、愛情面や異性問題に不安定の凶意あり。<BR>
   <INPUT TYPE=radio NAME=ans VALUE=2>天画=「火」、人画=「木」、地画=「土」の場合、万事順調・心身健和で成功運が強く、実力以上の発展をする。<BR>
   <INPUT TYPE=radio NAME=ans VALUE=3>天画=「土」、人画=「木」、地画=「金」の場合、相関関係の吉兆と相俟って発展し、内心強固で外面温和な人柄で人望厚く、成功運が強い。<BR>
   <INPUT TYPE=hidden NAME=mis VALUE="\$mis" size=10 maxlength=1>
   <INPUT TYPE=hidden NAME=name VALUE="\$name" size=10 maxlength=10>
   <INPUT TYPE=hidden NAME=email VALUE="\$email" size=10 maxlength=50>
   <INPUT TYPE=submit NAME="送信" VALUE="次の問題へ"><BR>
</FORM>
<HR>
</P>
</BODY>
</HTML>
EOM
	&jcode'convert(*msg, "sjis", "euc");
	$msg =~ s/\$ans/$ans/g;
	$msg =~ s/\$mis/$mis/g;
	$msg =~ s/\$name/$name/g;
	$msg =~ s/\$email/$email/g;
	print $msg;
}
__end__
