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
$tokuten = (10 - $mis)*10;
    #得点の計算
#####3問以上間違えたかどうかチェック#####
if ($mis >= 3) {
    # 3問以上間違えると、失格のメッセージを出す。
	$msg = <<"EOK";
Content-type: text/html

<HTML>
<HEAD>
   <TITLE>不合格</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=SHIFT_JIS">
</HEAD>
<BODY BGCOLOR="#FFFFFF">
<P>
<HR>
<FONT COLOR="#FF0000">残念でした。</FONT><BR>
<HR>
  3問間違えましたので、70点となり合格点には達しません。おし~いです。また次回、講義をお受けになり、チャレンジしてみて下さい。長い間、お付き合い頂き誠に有り難うございました。<BR>
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
   #合格番号を生成
   $countfile = "count.txt";
   open COUNTER,"$countfile"
    or &CgiError("$countfile オープン失敗1\n");
   $GONO = <COUNTER>;
   close COUNTER;
   ++$GONO;
   open COUNTER,">$countfile"
    or &CgiError("$countfile オープン失敗2\n");
   print COUNTER $GONO;
   close COUNTER;
    # 合格文章を表示
   $msg = <<"EOM";
Content-type: text/html

<HTML>
<HEAD>
   <TITLE>おめでとう</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=SHIFT_JIS">
</HEAD>
<BODY BGCOLOR="#FFFFFF">
<P>
<HR>
合格通知<BR>
<HR>
  お疲れさまでした。試験は無事終了致しました。<BR>
貴方の得点は、\$tokuten点です。<BR>
貴方は、通算\$GONO番目の合格者です。<BR>
(昨年度は18名の合格者がありました。)</P>
<P><FORM ACTION="$cgipath/n_mail.cgi" METHOD=POST>
   <P><INPUT TYPE=hidden NAME=name VALUE="\$name" size=10 maxlength=10>
   <INPUT TYPE=hidden NAME=email VALUE="\$email" size=10 maxlength=50>
   <INPUT TYPE=hidden NAME=tokuten VALUE="\$tokuten" size=10 maxlength=3><INPUT TYPE=hidden NAME=GONO VALUE="\$GONO" size=10 maxlength=5>
   <INPUT TYPE=submit NAME="送信" VALUE="翁へ送信"><BR>

</FORM>

<HR>

</P>
</BODY>
</HTML>
EOM
	&jcode'convert(*msg, "sjis", "euc");
	$msg =~ s/\$name/$name/g;
	$msg =~ s/\$email/$email/g;
	$msg =~ s/\$tokuten/$tokuten/g;
	$msg =~ s/\$GONO/$GONO/g;
	print $msg;
}
__END__
