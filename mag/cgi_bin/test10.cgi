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
if ($ans ne "1") {
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
   <TITLE>最終問題</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=SHIFT_JIS">
</HEAD>
<BODY BGCOLOR="#FFFFFF" TEXT="#000000" LINK="#0000FF">
<P>
<HR>
最終問題<BR>
<HR>
<IMG SRC="$root/test4.gif" WIDTH=94 HEIGHT=192 ALIGN=bottom>姓「小笠原」、名「加代子」さんに関する姓名判断の所見の中から間違っているものを一つ選んで下さい。</P>
<P><FORM ACTION="$cgipath/testL.cgi" METHOD=POST>
   <P><INPUT TYPE=radio NAME=ans VALUE=1 CHECKED>三才の配置に於て、相関関係の吉兆を得て万事平穏安泰で、目上の引き立てもあり成功発展する運勢である。<BR>
   <INPUT TYPE=radio NAME=ans VALUE=2>この方の問題は、外画22画で、神経質過ぎて人との和を欠きやすく、片意地な自己本位、調子の良い時はガラリと変わる二重人格のようなところである。<BR>
   <INPUT TYPE=radio NAME=ans VALUE=3>人画は31画となり、性格としては大人しく何事も斬新的で物事に筋道を立てて理性的な性格、温和に見えるが内心は不屈の精神と疑い妬む傾向にあり、あまり活動的でないが人の上に立素養はある。<BR>
   <INPUT TYPE=hidden NAME=mis VALUE="\$mis" size=10 maxlength=1>
   <INPUT TYPE=hidden NAME=name VALUE="\$name" size=10 maxlength=10>
   <INPUT TYPE=hidden NAME=email VALUE="\$email" size=10 maxlength=50>
   <INPUT TYPE=submit NAME="送信" VALUE="答案を提出する"><BR>
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
