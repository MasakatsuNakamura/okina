#!/usr/local/bin/perl
$|=1;
#########################
$sendmail = "/usr/lib/sendmail";
$okina_email = 'okina@e-mail.ne.jp';
#########################
require 'cgi-lib.pl';
require 'jcode.pl';
require "zenhan.pl";
use MIME::Base64;
&ReadParse();
#########################
$name = $in{'name'};
$email = $in{'email'};
$order1 = $in{'order1'};
$order2 = $in{'order2'};
$order3 = $in{'order3'};
$zipcord = $in{'zipcord'};
$address = $in{'address'};
$tel = $in{'tel'};
$fullname = $in{'fullname'};
$familyname = $in{'familyname'};
$brthday = $in{'brthday'};
$user = $in{'user'};
$brother = $in{'brother'};
$request = $in{'request'};
$exp = $in{'exp'};
######入力データの整形処理######
if ($zipcord ne "") {
	$zipcord =~ s/\s*//g;
	#全角英数字をすべて半角英数字にする。
	$zipcord = &zen2han($zipcord); 
}
if ($tel ne "") {
	$tel =~ s/\s*//g;
	#全角英数字をすべて半角英数字にする。
	$tel = &zen2han($tel); 
}
if ($familyname ne "") {
	$familyname =~ s/\s*//g;
}
if ($brthday ne "") {
	$brthday =~ s/\s*//g;
}
if ($email ne "") {
	$email =~ s/\s*//g;
	#全角英数字をすべて半角英数字にする。
	$email = &zen2han($email);
} 
#####入力エラーのチェック#####
if ($name =~ /^\s*$/){
	&CgiError("名前の記入がありません。",
	"ブラウザの「Back」ボタンで戻って再入力してください。");
	exit;
}
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
if (($order1 eq "" ) and ($order2 eq "" ) and ($order3 eq ""))  {
	&CgiError("入力エラー",
		"ご注文が何も指示されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
	exit;
}	
if ($order2 ne "") {
	if ($zipcord eq "") {
		&CgiError("郵便番号が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
	elsif ($address eq "") {
		&CgiError("住所が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}	
	elsif ($fullname eq "") {
		&CgiError("受取人が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
	elsif ($tel eq "") {
		&CgiError("電話番号が入力されていません。固定電話が無い時に限り携帯番号でも結構です。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
}
if ($order3 ne "") {
	if ($familyname eq "") {
		&CgiError("苗字(姓)が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
	elsif ($brthday eq "") {
		&CgiError("予定日(誕生日)が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
}
if ($exp ne "") {
	if ($tel eq "") {
		&CgiError("電話番号が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
	elsif ($zipcord eq "") {
		&CgiError("郵便番号が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
    elsif ($address eq "") {
		&CgiError("住所が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}	
}
#####ここからBase64メール#####
##### ボディ基本文字列の定義######
@body = (
	"=====================================", 
	"山本翁さまへ、以下の注文を致したく。", 
	"", 
	"申込人様の氏名：", 
	"", 
	"申込人様のEメールアドレス：", 
	"", 
	"ご注文内容：",
	"",
	"", 
	"",  
	"書籍の送付先または連絡先", 
	"郵便番号：", 
	"", 
	"ご住所：", 
	"", 
	"お電話番号：", 
	"", 
	"受取人様：", 
	"", 
	"命名のご依頼内容：", 
	"", 
	"姓(みょうじ)：", 
	"", 
	"出産予定日：", 
	"", 
	"今までの利用：", 
	"", 
	"兄姉のお名前：", 
	"", 
	"ご要望事項：", 
	"", 
	"====================================="
);
foreach(@body) {
	&jcode'convert(*_, "sjis", "euc");
}
#######Subの生成(Base64エンコード)#######
$subject = "翁へご注文(Ver.7)";
&jcode'convert(*subject, 'jis', 'euc');
$subject = encode_base64($subject);
chop($subject);
$subject = " . $subject . "?=";
####### ヘッダの定義#########
$mail_header = <<"EOM";
From: $email
To: $okina_email
MIME-Version: 1.0
Content-Type: text/plain;
	charset="x-sjis-jp"
Content-Transfer-Encoding: base64
Subject: $subject
EOM
####### メッセージボディの生成########
$body[4] .= $name;
$body[6] .= $email;
$body[8] .= $order1;
$body[9] .= $order2;
$body[10] .= $order3;
$body[13] .= $zipcord;
$body[15] .= $address;
$body[17] .= $tel;
$body[19] .= $fullname;
$body[21] .= $exp;
$body[23] .= $familyname;
$body[25] .= $brthday;
$body[27] .= $user;
$body[29] .= $brother;
$body[31] .= $request;
$mailbody = join("\r\n", @body);
$encoded = encode_base64($mailbody);
######## メール送信#########
open(MAIL, "|$sendmail $okina_email");
print MAIL $mail_header;
for ($i = 0; $i < length($encoded); $i += 76) {
	print MAIL substr($encoded, $i, 76);
}
close(MAIL);
#####以上がBase64メール#####
print "Content-type: text/html\n\n";
print "<html>\n";
print "<head>\n";
print "<META HTTP-EQUIV=\"Refresh\" CONTENT=\"5;URL=/~kazu-y/index.html\">\n";
print "<title>ご注文受付完了</title></head>\n";
print "<body bgcolor=\"ffffff\" TEXT=\"000000\" link=\"fb02ee\" vlink=\"fb02ee\">\n";
print "<p>\n";
print "<br>\n";
print "<br>\n";
print "<center>\n";
print "<font size=\"6\" color=\"000000\"><b>ありがとうございました。</b></font><br>\n";
print "</center>\n";
print "</body>\n";
print "</html>\n";