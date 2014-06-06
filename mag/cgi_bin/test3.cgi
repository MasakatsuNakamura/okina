#!/usr/local/bin/perl
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
if ($ans ne "2") {
    $mis = $mis + 1;
    #正解でない場合、misカウントに1を加算
}
#####第3問の出題#####
$msg = <<"EOM";
Content-type: text/html

<HTML>
<HEAD>
   <TITLE>第3問</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=SHIFT_JIS">
</HEAD>
<BODY BGCOLOR="#FFFFFF" TEXT="#000000" LINK="#0000FF">
<P>
<HR>
第3問<BR>
<HR>
<IMG SRC="$root/test3.gif" WIDTH=94 HEIGHT=99 ALIGN=bottom>は「陰陽五行の法則」に関する図である。次の説明文の中から間違っているものを一つ選んで下さい。</P>
<P><FORM ACTION="$cgipath/test4.cgi" METHOD=POST>
   <P><INPUT TYPE=radio NAME=ans VALUE=1 CHECKED>1と2は「木」、3と4は「火」、5と6は「土」、7と8は「金」、9と10は「水」を表し、偶数は陰、奇数は陽である。<BR>
   <INPUT TYPE=radio NAME=ans VALUE=2>点線で結ばれている陰陽配列の場合は、比較的弱く作用しますが、直線で結ばれている陰陽配列の場合はその作用が最も強く現れるから注意が必要である。<BR>
   <INPUT TYPE=radio NAME=ans VALUE=3>天画、人画、地画の陰陽五行の配列を三才の配置と言い、名付けでは最も重要視すべきポイントである。<BR>
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
__end__