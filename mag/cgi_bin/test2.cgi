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
#####第2問の出題#####
$msg = <<"EOM";
Content-type: text/html

<HTML>
<HEAD>
   <TITLE>第2問</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=SHIFT_JIS">
</HEAD>
<BODY BGCOLOR="#FFFFFF" TEXT="#000000" LINK="#0000FF">
<P>
<HR>
第2問<BR>
<HR>
  次の図は「吉川」さんの姓名判断を行う途中である。<IMG SRC="$root/test2.gif" WIDTH=94 HEIGHT=189 ALIGN=bottom>    「守」の一文字名に関する画数計算の説明文の中から正しいものを一つ選んで下さい。</P>
<P><FORM ACTION="$cgipath/test3.cgi" METHOD=POST>
   <P><INPUT TYPE=radio NAME=ans VALUE=1 CHECKED>地画は6画、外画は7画、総画は15画である。<BR>
   <INPUT TYPE=radio NAME=ans VALUE=2>地画は7画、外画も7画、総画は15画である。<BR>
   <INPUT TYPE=radio NAME=ans VALUE=3>地画は7画、外画も7画、総画は16画である。<BR>
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
