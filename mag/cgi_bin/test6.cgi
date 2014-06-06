#!/usr/local/bin/perl
$|=1;
require "jcode.pl";
require "cgi-lib.pl";

$root = "/~kazu-y/mag";
$cgipath = "/~kazu-y/mag/cgi_bin";
$baseurl = "http://www2.mahoroba.ne.jp";

#####CGI変数取りこみ#####
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
<!--This file created 03.1.13 11:12 AM by Home Page Pro version 3.0J v1-->
<HEAD>
   <TITLE>第6問</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=SHIFT_JIS">
</HEAD>
<BODY BGCOLOR="#FFFFFF" TEXT="#000000" LINK="#0000FF">
<P>
<HR>
第6問<BR>
<HR>
漢字の画数の数え方に関する説明文の中から間違っているものを一つ選んで下さい。</P>
<P><FORM ACTION="$cgipath/test7.cgi" METHOD=POST>
   <P><INPUT TYPE=radio NAME=ans VALUE=1 CHECKED>漢数字の一から十は、画数によらず呼数(四なら4画)で算定する。<BR>
   <INPUT TYPE=radio NAME=ans VALUE=2>ひらかなの画数は書き方の通りで、「す」「ぬ」は2画、「お」は3画、「ほ」は4画と数える。<BR>
   <INPUT TYPE=radio NAME=ans VALUE=3>佐々木や野々村の「々」は3画とは数えず、それぞれ「佐」「野」と同じ画数として扱う。<BR>
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
