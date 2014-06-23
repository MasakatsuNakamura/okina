#!/usr/local/bin/perl
$|=1;
#########################
$sendmail = "/usr/lib/sendmail";
$okina_email = 'okina@e-mail.ne.jp';
#########################
require "cgi-lib.pl";
require "jcode.pl";
require "zenhan.pl";
use MIME::Base64;
&ReadParse();
#########################
$name = $in{'name'};
$email = $in{'email'};
$order4 = $in{'order4'};
$familyname1 = $in{'familyname1'};
$firstname1 = $in{'firstname1'};
$birthday1= $in{'birthday1'};
$sex1 = $in{'sex1'};
$trade1 = $in{'trade1'};
$request1 = $in{'request1'};
$order5 = $in{'order5'};
$familyname2 = $in{'familyname2'};
$firstname2 = $in{'firstname2'};
$family = $in{'family'};
$request2 = $in{'request2'};
$order6 = $in{'order6'};
$familyname3 = $in{'familyname3'};
$firstname3 = $in{'firstname3'};
$birthday3= $in{'birthday3'};
$sex3 = $in{'sex3'};
$trade3 = $in{'trade3'};
$familyname4 = $in{'familyname4'};
$firstname4 = $in{'firstname4'};
$birthday4= $in{'birthday4'};
$sex4 = $in{'sex4'};
$trade4 = $in{'trade4'};
$sei = $in{'sei'};
$request3 = $in{'request3'};
$order7 = $in{'order7'};
$familyname5 = $in{'familyname5'};
$firstname5 = $in{'firstname5'};
$birthday5= $in{'birthday5'};
$sex5 = $in{'sex5'};
$trade5 = $in{'trade5'};
$request5 = $in{'request5'};
######入力データの整形処理######
if ($familyname1 ne "") {
	$familyname1 =~ s/\s*//g;
}
if ($familyname2 ne "") {
	$familyname2 =~ s/\s*//g;
}
if ($familyname3 ne "") {
	$familyname3 =~ s/\s*//g;
}
if ($familyname4 ne "") {
	$familyname4 =~ s/\s*//g;
}
if ($familyname5 ne "") {
	$familyname5 =~ s/\s*//g;
}
if ($firstname1 ne "") {
	$familyname1 =~ s/\s*//g;
}
if ($firstname2 ne "") {
	$familyname2 =~ s/\s*//g;
}
if ($firstname3 ne "") {
	$familyname3 =~ s/\s*//g;
}
if ($firstname4 ne "") {
	$familyname4 =~ s/\s*//g;
}
if ($firstname5 ne "") {
	$familyname5 =~ s/\s*//g;
}
if ($birthday1 ne "") {
	$birthday1 =~ s/\s*//g;
}
if ($birthday3 ne "") {
	$birthday3 =~ s/\s*//g;
}
if ($birthday4 ne "") {
	$birthday4 =~ s/\s*//g;
}
if ($birthday5 ne "") {
	$birthday5 =~ s/\s*//g;
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
if (($order4 eq "" ) and ($order5 eq "" ) and ($order6 eq "") and ($order7 eq ""))  {
	&CgiError("入力エラー",
		"ご依頼事項が何も指示されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
	exit;
}	
if ($order4 ne "") {
	if ($familyname1 eq "") {
		&CgiError("姓が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
	elsif ($firstname1 eq "") {
		&CgiError("名が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}	
	elsif ($birthday1 eq "") {
		&CgiError("生年月日が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
    elsif ($sex1 eq "") {
		&CgiError("性別が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
    elsif ($trade1 eq "") {
		&CgiError("業種・ご職業が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
   elsif ($request1 eq "") {
		&CgiError("ご依頼内容の詳細が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
}
if ($order5 ne "") {
	if ($familyname2 eq "") {
		&CgiError("姓が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
	elsif ($firstname2 eq "") {
		&CgiError("名が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}	
}
if ($order6 ne "") {
	if ($familyname3 eq "") {
		&CgiError("依頼者側の姓が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
   elsif ($firstname3 eq "") {
		&CgiError("依頼者側の名が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
   elsif ($birthday3 eq "") {
		&CgiError("依頼者側の生年月日が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
   elsif ($sex3 eq "") {
		&CgiError("依頼者側の性別が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
   elsif ($trade3 eq "") {
		&CgiError("依頼者側のご職業が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
   elsif ($familyname4 eq "") {
		&CgiError("相手側の姓が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
   elsif ($firstname4 eq "") {
		&CgiError("相手側の名が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
   elsif ($birthday4 eq "") {
		&CgiError("相手側の生年月日が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
   elsif ($sex4 eq "") {
		&CgiError("相手側の性別が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
   elsif ($trade4 eq "") {
		&CgiError("相手側のご職業が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
   elsif ($sei eq "") {
		&CgiError("ご結婚後の姓が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
}
if ($order7 ne "") {
	if ($familyname5 eq "") {
		&CgiError("姓が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
   elsif ($firstname5 eq "") {
		&CgiError("名が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
   elsif ($birthday5 eq "") {
		&CgiError("生年月日が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
   elsif ($sex5 eq "") {
		&CgiError("性別が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
   elsif ($trade5 eq "") {
		&CgiError("ご職業が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
   elsif ($request5 eq "") {
		&CgiError("ご相談内容が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
}
#####ここからBase64メール#####
##### ボディ基本文字列の定義######
@body = (
	"=====================================",
    "山本翁さまへ、以下のご相談を致したく。",
    "",
    "申込人様の氏名：",
    "",
    "申込人様のEメールアドレス：",
    "",
    "",
    "ご依頼内容：",
    "", 
    "姓：",
    "",
    "名：",
    "",
    "生年月日：",
    "",
    "性別：",
    "",
    "業種・職業：",
    "",
    "ご要望事項：",
    "", 
    "",
    "ご依頼内容：",
    "",
    "姓：",
    "",
    "名：",
    "",
    "ご家族のお名前と続き柄：",
    "", 
    "ご要望事項：",
    "",
    "",
    "ご依頼内容：",
    "",
    "依頼者側の姓：",
    "",
    "依頼者側の名：",
    "",
    "依頼者側の生年月日：",
    "",
    "依頼者側の姓別：",
    "",
    "依頼者側のご職業：",
    "",
    "相手側の姓：",
    "",
    "相手側の名：",
    "",
    "相手側の生年月日：",
    "",
    "相手側の性別：",
    "",
    "相手側のご職業：",
    "",
    "結婚後の姓：",
    "",
    "ご要望事項：",
    "",
    "",
    "ご依頼事項：",
    "",
    "姓：",
    "",
    "名：",
    "", 
    "生年月日：",
    "",
    "性別：",
    "",
    "ご職業：",
    "", 
    "ご依頼事項：",
    "", 
    "====================================="
);
foreach(@body) {
	&jcode'convert(*_, "sjis", "euc");
}
#######Subの生成(Base64エンコード)#######
$subject = "翁へのご相談(Ver.3)";
&jcode'convert(*subject, 'jis', 'euc');
$subject = encode_base64($subject);
chop($subject);
$subject = " . $subject . "?=";
####### ヘッダの定義#########
$mail_header = <<"EOM3";
From: $email
To: $okina_email
MIME-Version: 1.0
Content-Type: text/plain;
	charset="x-sjis-jp"
Content-Transfer-Encoding: base64
Subject: $subject
EOM3
####### メッセージボディの生成########
$body[4] .= $name;
$body[6] .= $email;
$body[9] .= $order4;
$body[11] .= $familyname1;
$body[13] .= $firstname1;
$body[15] .= $birthday1;
$body[17] .= $sex1;
$body[19] .= $trade1;
$body[21] .= $request1;
$body[24] .= $order5;
$body[26] .= $familyname2;
$body[28] .= $firstname2;
$body[30] .= $family;
$body[32] .= $request2;
$body[35] .= $order6;
$body[37] .= $familyname3;
$body[39] .= $firstname3;
$body[41] .= $birthday3;
$body[43] .= $sex3;
$body[45] .= $trade3;
$body[47] .= $familyname4;
$body[49] .= $firstname4;
$body[51] .= $birthday4;
$body[53] .= $sex4;
$body[55] .= $trade4;
$body[57] .= $sei;
$body[59] .= $request3;
$body[62] .= $order7;
$body[64] .= $familyname5;
$body[66] .= $firstname5;
$body[68] .= $birthday5;
$body[70] .= $sex5;
$body[72] .= $trade5;
$body[74] .= $request5;
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
#下記のURLは、あなたのサ−バ−にあわせて下さい。
print "<META HTTP-EQUIV=\"Refresh\" CONTENT=\"5;URL=/~kazu-y/index.html\">\n";
print "<title>ご相談受付完了</title></head>\n";
print "<body bgcolor=\"ffffff\" TEXT=\"000000\" link=\"fb02ee\" vlink=\"fb02ee\">\n";
print "<p>\n";
print "<br>\n";
print "<br>\n";
print "<center>\n";
print "<font size=\"6\" color=\"000000\"><b>ありがとうございました。</b></font><br>\n";
print "</center>\n";
print "</body>\n";
print "</html>\n";