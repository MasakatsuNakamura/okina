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
$order6 = $in{'order6'};
$order7 = $in{'order7'};
$familyname1 = $in{'familyname1'};
$firstname1 = $in{'firstname1'};
$birthday1= $in{'birthday1'};
$sex1 = $in{'sex1'};
$trade1 = $in{'trade1'};
$familyname2 = $in{'familyname2'};
$firstname2 = $in{'firstname2'};
$birthday2= $in{'birthday2'};
$sex2 = $in{'sex2'};
$trade2 = $in{'trade2'};
$request = $in{'request'};
######入力データの整形処理######
if ($familyname1 ne "") {
	$familyname1 =~ s/\s*//g;
}
if ($familyname2 ne "") {
	$familyname2 =~ s/\s*//g;
}
if ($firstname1 ne "") {
	$familyname1 =~ s/\s*//g;
}
if ($firstname2 ne "") {
	$familyname3 =~ s/\s*//g;
}
if ($birthday1 ne "") {
	$birthday1 =~ s/\s*//g;
}
if ($birthday2 ne "") {
	$birthday3 =~ s/\s*//g;
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
	elsif ($trade1 eq "") {
		&CgiError("お仕事内容または、名前の用途が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
}
if ($order6 ne "") {
	if ($familyname1 eq "") {
		&CgiError("依頼者側の姓が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
   elsif ($firstname1 eq "") {
		&CgiError("依頼者側の名が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
   elsif ($birthday1 eq "") {
		&CgiError("依頼者側の生年月日が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
   elsif ($trade1 eq "") {
		&CgiError("依頼者側のご職業が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
   elsif ($familyname2 eq "") {
		&CgiError("相手側の姓が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
   elsif ($firstname2 eq "") {
		&CgiError("相手側の名が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
   elsif ($birthday2 eq "") {
		&CgiError("相手側の生年月日が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
   elsif ($trade2 eq "") {
		&CgiError("相手側のご職業が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
   elsif ($request eq "") {
		&CgiError("ご相談内容をお書き下さい。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
}
if ($order7 ne "") {
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
   elsif ($trade1 eq "") {
		&CgiError("ご職業が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
   elsif ($request eq "") {
		&CgiError("ご相談内容をお書き下さい。",
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
	"ご要望事項：", 
	"", 
	"", 
	"ご依頼者の情報", 
	"姓：", 
	"", 
	"名：", 
	"", 
	"生年月日：", 
	"", 
	"性別：", 
	"", 
	"ご職業または、業務内容：", 
	"", 
    "",
	"結婚後の姓：", 
	"", 
    "相手方の情報",
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
	"====================================="
);
foreach(@body) {
	&jcode'convert(*_, "sjis", "euc");
}
#######Subの生成(Base64エンコード)#######
$subject = "翁へご相談(iモードVer.2)";
&jcode'convert(*subject, 'jis', 'euc');
$subject = encode_base64($subject);
chop($subject);
$subject = " . $subject . "?=";
####### ヘッダの定義#########
$mail_header = <<"EOM5";
From: $email
To: $okina_email
MIME-Version: 1.0
Content-Type: text/plain;
	charset="x-sjis-jp"
Content-Transfer-Encoding: base64
Subject: $subject
EOM5
####### メッセージボディの生成########
$body[4] .= $name;
$body[6] .= $email;
$body[8] .= $order4;
$body[9] .= $order6;
$body[10] .= $order7;
$body[12] .= $request;
$body[16] .= $familyname1;
$body[18] .= $firstname1;
$body[20] .= $birthday1;
$body[22] .= $sex1;
$body[24] .= $trade1;
$body[27] .= $sei;
$body[30] .= $familyname2;
$body[32] .= $firstname2;
$body[34] .= $birthday2;
$body[36] .= $sex2;
$body[38] .= $trade2;
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
$msg1 = "ご相談受付完了\n";
$msg2 = "ありがとうございました。\n";
$msg3 = "1→お知らせに戻る。\n";
&jcode'convert(*msg1, 'sjis', 'euc');
&jcode'convert(*msg2, 'sjis', 'euc');
&jcode'convert(*msg3, 'sjis', 'euc');
print "Content-type: text/html\n\n";
print "<HTML>\n";
print "<HEAD>\n";
print "<TITLE>$msg1</TITLE>\n";
print "<META HTTP-EQUIV=\"Content-Type\" CONTENT=\"text/html;CHARSET=SHIFT_JIS\">\n";
print "</HEAD>\n";
print "<BODY BGCOLOR=\"#FFFFFF\" TEXT=\"#000000\" LINK=\"#0000FF\">\n";
print "<P>\n";
print "<BR>\n";
print "<BR>\n";
print "<FONT COLOR=\"#FF0000\"><B>$msg2</B></FONT><BR>\n";
print "<A HREF=\"/~kazu-y/i-info2.html\" ACCESSKEY=1>$msg3</A><BR>\n";
print "</BODY>\n";
print "</HTML>\n";
__END__