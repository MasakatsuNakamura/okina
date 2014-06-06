#!/usr/local/bin/perl
$|=1;
require "jcode.pl";
require "cgi-lib.pl";
require "zenhan.pl";

$root = "/~kazu-y/mag";
$cgipath = "/~kazu-y/mag/cgi_bin";
$baseurl = "http://www2.mahoroba.ne.jp";

#####CGI変数取りこみ#####
&ReadParse();
$name = $in{'name'};
$email = $in{'email'};

#####メールアドレスの整形#####
if ($email ne "") {
	$email =~ s/\s*//g;
	#全角英数字をすべて半角英数字にする。
	$email = &zen2han($email);
}
######入力エラーのチェック#####
$msg1 = "名前の記入がありません。";
$msg2 = "メールアドレスの記入がありません。";
$msg3 = "メールアドレスの書き方が間違っています。";
$msg4 = "ブラウザの｢Back｣ボタンで戻って再入力してください。";
&jcode'convert(*msg1, 'sjis', 'euc');
&jcode'convert(*msg2, 'sjis', 'euc');
&jcode'convert(*msg3, 'sjis', 'euc');
&jcode'convert(*msg4, 'sjis', 'euc');

if ($name =~ /^\s*$/){
	&CgiError("$msg1",
	"$msg4");
	exit;
}
if ($email =~ /^\s*$/){
	&CgiError("$msg2",
	"$msg4");
	exit;
}
elsif (($email) and (not $email =~ /.+\@.+\..+/)) {
	&CgiError("$msg3",$email,
	"$msg4");
	exit;
}
#####第1問の出題#####
$msg = <<"EOM";
Content-type: text/html

<HTML>
<HEAD>
   <TITLE>第1問</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=SHIFT_JIS">
</HEAD>
<BODY BGCOLOR="#FFFFFF" TEXT="#000000" LINK="#0000FF">
<P>
<HR>
第1問<BR>
<HR>
  次の図を見て、<IMG SRC="$root/test1.gif" WIDTH=94 HEIGHT=164 ALIGN=bottom>山本式姓名判断に於ける五画分類に関する説明文の中から正しいものを一つ選んで下さい。</P>
<P><FORM ACTION="$cgipath/test2.cgi" METHOD=POST>
   <P><INPUT TYPE=radio NAME=ans VALUE=1 CHECKED>Aは天画と言い、先祖伝来のもので吉凶の影響は直接なく、陰陽の配列および総画に於て、本人の成功運と健康運を左右する。<BR>
   <INPUT TYPE=radio NAME=ans VALUE=2>Dは外画といい、社交運とも呼ばれ、夫婦・交友・知己の運命及び周囲の運命を左右する。<BR>
   <INPUT TYPE=radio NAME=ans VALUE=3>Eは伏運と言い、成人前は成長運、成人後は発展運とも言う。<BR>
   <INPUT TYPE=hidden NAME=mis VALUE=0 size=10 maxlength=1>
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
	$msg =~ s/\$name/$name/g;
	$msg =~ s/\$email/$email/g;
print $msg;
