#!/usr/local/bin/perl
#上のパスは、あなたのサ−バ−にあわせて下さい。
####################################################################
#N_Mail CGI
#Copyright 1992/1997                 K.Yamano 
#Scripts Archive at：          
#CGIの販売、転載、配布、無断利用厳禁。
####################################################################
#あなたのサ−バ−のsendmailのパスにあわせる。
$sendmail = "/usr/lib/sendmail";
#あなたのMailアドレスを記入。
$youraddress = 'kazu-y@mahoroba.ne.jp ';
#$youraddress = 'nakamura@ppd.sf.nara.sharp.co.jp ';
#####################################################################
require "cgi-lib.pl";
require "jcode.pl";
&ReadParse;

###############下記の項目は、無制限に追加出来ます。#################
$kanji = $in{'kanji'};
$name2 = $in{'name2'};
$email2 = $in{'email2'};


####下記の住所、氏名、TEL、FAXは、上の項目にあわせて追加する。######
####例えば、会社名を追加の場合は、会社名、$kaisya と記入。
####$kaisyaは、必ずロ−マ字コ−ドで打ち込む。
$kanjicode = $kanji;
$kanjicode =~ s/ //g;
$kanjicode =~ s/(.)/sprintf("%02X",unpack("c",$1) >= 0 ? unpack("c",$1)
: 256 + unpack("c",$1))/eg;
$kanjicode =~ s/(....)/$1 /g;

$com = <<MESSAGE;
From: $email2
Subject: 判定出来ない漢字(企業版)

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
#&jcode'convert(*com,"sjis","euc");
#$com =~ s/\$kanji/$kanji/;
#$com =~ s/\$name2/$name2/;
#$com =~ s/\$email2/$email2/;
#&jcode'convert(*com,"jis","sjis");
&jcode'convert(*com,"jis");
open(MAIL, "|$sendmail $youraddress");
print MAIL $com;
close(MAIL);
print "Content-type: text/html\n\n";
print "<html>\n";
print "<head>\n";
#下記のURLは、あなたのサ−バ−にあわせて下さい。
print "<META HTTP-EQUIV=\"Refresh\" CONTENT=\"5;URL=/~kazu-y/input3.html\">\n";
#print "<META HTTP-EQUIV=\"Refresh\" CONTENT=\"5;URL=http://ppd.sf.nara.sharp.co.jp/~nakamura/test/seimei2/public_html/input.html\">\n";
print "<title>送信完了</title></head>\n";
print "<body bgcolor=\"ffffff\" TEXT=\"000000\" link=\"fb02ee\" vlink=\"fb02ee\">\n";
print "<p>\n";
print "<br>\n";
print "<br>\n";
print "<center>\n";
print "<font size=\"6\" color=\"000000\"><b>ご協力ありがとうございました。</b></font><br>\n";
print "</center>\n";
print "</body>\n";
print "</html>\n";
