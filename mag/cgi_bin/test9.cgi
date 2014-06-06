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
<HEAD>
   <TITLE>第9問</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=SHIFT_JIS">
</HEAD>
<BODY BGCOLOR="#FFFFFF" TEXT="#000000" LINK="#0000FF">
<P>
<HR>
第9問<BR>
<HR>
「数の霊位」に関する説明文の中から間違っているものを一つ選んで下さい。</P>
<P><FORM ACTION="$cgipath/test10.cgi" METHOD=POST>
   <P><INPUT TYPE=radio NAME=ans VALUE=1 CHECKED>15画  陰陽和合の天恵ある霊位を示す吉祥数で、長男でなくとも跡取になることが多い。温和な人柄で、着実に努力して次第に富貴、繁栄する吉祥数ですが、強運数だけにワンマン的になり易く、お坊ちゃん気質になりますと運気が衰えますから順和雅量を養うと強い発達をします。女性の場合は長男に嫁が多い特徴があり、相手が長男の時は幸運な生涯を得ます。<BR>
   <INPUT TYPE=radio NAME=ans VALUE=2>31画  陰陽和合の輪郭ある霊位を示す大吉数で、温和、雅量に富み、協調性と積極性のある人柄が、大物として人望を集めて富栄名声を得て、家庭的・社会的にも恵まれ、実業家・教育家などいずれの社会でも頭角をあらわし、おごることなく安泰発展の大吉祥数とされています。女性にも良く、円満タイプ・才色兼備のラッキー型が多い。<BR>
   <INPUT TYPE=radio NAME=ans VALUE=3>47画  忠実精励、開花の霊位を示す大吉祥数。温和でまじめな努力家で、努力の末に花開く強運数で、世渡り上手と誠実な人柄が敵を作らず、衆人の信頼を集めまして晩年盛運・幸慶を享くる大吉祥数とされています。真面目な努力家で、女性にも大吉祥の幸運数、良縁玉のこしに乗る。<BR>
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
