#!/usr/local/bin/perl
$|=1;
#############################
$sendmail = "/usr/lib/sendmail";
$youraddress = 'kazu-y@mahoroba.ne.jp ';
#############################
require "cgi-lib.pl";
require "jcode.pl";
require "zenhan.pl";
&ReadParse;
#############################
$kanji = $in{'kanji'};
$name2 = $in{'name2'};
$email2 = $in{'email2'};

#####データの整形処理#####
if ($email2 ne "") {
	$email2 =~ s/\s*//g;
	#全角英数字をすべて半角英数字にする。
	$email2 = &zen2han($email2);
} 

#####漢字コードの生成#####
$kanjicode = $kanji;
$kanjicode =~ s/ //g;
$kanjicode =~ s/(.)/sprintf("%02X",unpack("c",$1) >= 0 ? unpack("c",$1)
: 256 + unpack("c",$1))/eg;
$kanjicode =~ s/(....)/$1 /g;

#####注文メールの送信#####
$com = <<"MESSAGE";
From: $email2
Subject: 判定出来ない漢字(iモード2)

=====================================
鑑定できない漢字コード(SJIS)：
$kanjicode
連絡人のEメールアドレス：
$email2
連絡人の氏名(参考)：
$name2
エラー漢字(参考)：
$kanji
参考：エラーが発生する可能性が高い。
=====================================
MESSAGE

&jcode'convert(*com,"jis");
open(MAIL, "|$sendmail $youraddress");
print MAIL $com;
close(MAIL);

print "Content-type: text/html\n\n";
print "<HTML>\n";
print "<HEAD>\n";
print "<TITLE>エラー送信完了</TITLE>\n";
print "<META HTTP-EQUIV=\"Content-Type\" CONTENT=\"text/html;CHARSET=SHIFT_JIS\">\n";
print "</HEAD>\n";
print "<BODY BGCOLOR=\"#FFFFFF\" TEXT=\"#000000\" LINK=\"#0000FF\">\n";
print "<P>\n";
print "<BR>\n";
print "<BR>\n";
print "<FONT COLOR=\"#FF0000\"><B>ご協力ありがとうございました。</B></FONT><BR>\n";
print "<A HREF=\"/~kazu-y/i-mode.html\" accesskey=1>1→もう一度鑑定する。</A><BR>\n";
print "</BODY>\n";
print "</HTML>\n";
