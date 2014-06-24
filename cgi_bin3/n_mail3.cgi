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
require "zenhan.pl";
&ReadParse;

###############下記の項目は、無制限に追加出来ます。
#################
$email = $in{'email'};
$name = $in{'name'};
$tel = $in{'tel'};
$adress = $in{'adress'};
$price = $in{'price'};
$order = $in{'order'};
######入力データの整形処理######
if ($tel ne "") {
	$tel =~ s/\s*//g;
	#全角英数字をすべて半角英数字にする。
	$tel = &zen2han($tel); 
}
if ($email ne "") {
	$email =~ s/\s*//g;
	#全角英数字をすべて半角英数字にする。
	$email = &zen2han($email);
} 
#####入力エラーのチェック#####
if ($email =~ /^\s*$/){
	&CgiError("メールアドレスの記入がありません。",
	"ブラウザの「Back」ボタンで戻って再入力してください。");
	exit;
}
elsif (($email) and (not $email =~ /.+\@.+\..+/)) {
	&CgiError("入力エラー",
		"メールアドレスの書き方が間違っています。",$email,
		"ブラウザの「Back」ボタンで戻って再入力してください。");
	exit;
}
if ($name eq ""){
	&CgiError("名前の記入がありません。",
	"ブラウザの「Back」ボタンで戻って再入力してください。");
	exit;
}
if ($adress eq "") {
    &CgiError("住所が入力されていません。",
    "ブラウザの「Back」ボタンで戻って再入力してください。");
    exit;
}	
if ($tel eq "") {
	&CgiError("電話番号が入力されていません。",
	"ブラウザの「Back」ボタンで戻って再入力してください。");
	exit;
}
#####注文メールの送信#####
$com = <<MESSAGE;
From: $email
Subject: 物件のお問い合わせ

=====================================
お名前：
$name
メールアドレス：
$email
電話番号：
$tel
住所：
$adress
希望価格：
$price
連絡事項：
$order
=====================================
MESSAGE
#&jcode'convert(*com,"sjis","euc");
#$com =~ s/\$name/$name/;
#$com =~ s/\$email/$email/;
#$com =~ s/\$tel/$tel/;
#$com =~ s/\$adress/$adress/;
#$com =~ s/\$price/$price/;
#$com =~ s/\$order/$order/;
#&jcode'convert(*com,"jis","sjis");
&jcode'convert(*com,"jis");
open(MAIL, "|$sendmail $youraddress");
print MAIL $com;
close(MAIL);
print "Content-type: text/html\n\n";
print "<html>\n";
print "<head>\n";
#下記のURLは、あなたのサ−バ−にあわせて下さい。
print "<META HTTP-EQUIV=\"Refresh\" CONTENT=\"5;URL=http://www.sikasenbey.or.jp/haibara/haibara.htm\">\n";
#print "<META HTTP-EQUIV=\"Refresh\" CONTENT=\"5;URL=http://ppd.sf.nara.sharp.co.jp/~nakamura/test/seimei2/public_html/input.html\">\n";
print "<title>送信完了</title></head>\n";
print "<body bgcolor=\"ffffff\" TEXT=\"000000\" link=\"fb02ee\" vlink=\"fb02ee\">\n";
print "<p>\n";
print "<br>\n";
print "<br>\n";
print "<center>\n";
print "<font size=\"6\" color=\"000000\"><b>後日、こちらからご連絡差し上げます。</b></font><br>\n";
print "</center>\n";
print "</body>\n";
print "</html>\n";
