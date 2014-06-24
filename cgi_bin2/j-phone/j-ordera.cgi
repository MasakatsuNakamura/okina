#!/usr/local/bin/perl
$|=1;
##########################
$sendmail = "/usr/lib/sendmail";
$okina_email = 'okina@e-mail.ne.jp ';
##########################
require "cgi-lib.pl";
require "jcode.pl";
require "zenhan.pl";
use MIME::Base64;
&ReadParse();
#####データの取り込み#####
$name = $in{'name'};
$email = $in{'email'};
$email2 = $in{'email2'};
$fax = $in{'fax'};
$method = $in{'method'};
######入力データの整形処理######
if ($fax ne "") {
	$fax =~ s/\s*//g;
	#全角英数字をすべて半角英数字にする。
	$fax = &zen2han($fax); 
}
if ($email ne "") {
	$email =~ s/\s*//g;
	#全角英数字をすべて半角英数字にする。
	$email = &zen2han($email);
} 
if ($email2 ne "") {
	$email2 =~ s/\s*//g;
	#全角英数字をすべて半角英数字にする。
	$email2 = &zen2han($email);
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
if ($method eq "fax") {
	if ($fax eq "") {
		&CgiError("送り先のファックス番号が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
}
if ($method eq "mail") {
	if ($email2 =~ /^\s*$/){
	&CgiError("結果連絡先のメールアドレスの記入がありません。",
	"ブラウザの「Back」ボタンで戻って再入力してください。");
	exit;
    }
    elsif (($email2) and (not $email2 =~ /.+\@.+\..+/)) {
	&CgiError("入力エラー",
		"結果連絡先のメールアドレスの書き方が間違っています。",$email2,
		"ブラウザの「Back」ボタンで戻って再入力してください。");
	exit;
    }
}
#####手段を文章化#####
if ($method eq "fax") {
	$method ="ファックスでの受信を希望";
}
if ($method eq "mail") {
	$method ="パソコンからメール受信を希望";
}
&jcode'convert(*method, 'jis', 'euc');
#####ここからBase64メール#####
##### ボディ基本文字列の定義######
@body = (
	"=====================================", 
	"山本翁への「新生児命名」ご依頼フォーム", 
	"下記の※欄を全てご記入の上、「返信」して下さい。", 
	"申込人様の氏名：", 
	"※", 
	"申込人様のEメールアドレス：", 
	"※",  
	"命名のご依頼内容について", 
	"姓(みょうじ：必ず漢字でご記入下さい。)：", 
	"※", 
	"出産予定日（未定の方はおおよそで結構です）：", 
	"※", 
    "結果の送信手段：",
    "※",
    "ファックスの番号（ご希望者のみ）：",
    "※",
    "パソコンのEメールアドレス（ご希望者のみ）：",
    "※",
	"今まで「翁の命名」をご利用なさいましたか？：", 
	"", 
	"兄姉のお名前（差し支えなければ）：", 
	"", 
	"ご要望事項：", 
	"", 
	"", 
	"", 
	"お急ぎの方は、その旨ご記入下さい。", 
	"", 
	"受注後、振込先を申込人さまにご連絡致します。", 
	"お振り込み確認後、2-3日で結果をお知らせします。", 
	"====================================="
);
foreach(@body) {
	&jcode'convert(*_, "sjis", "euc");
}
#######Subの生成(Base64エンコード)#######
$subject = "翁へご注文(jフォンVer.1)";
&jcode'convert(*subject, 'jis', 'euc');
$subject = encode_base64($subject);
chop($subject);
$subject = " . $subject . "?=";
####### ヘッダの定義#########
$mail_header = <<"EOM5";
From: $okina_email
To: $email
MIME-Version: 1.0
Content-Type: text/plain;
	charset="x-sjis-jp"
Content-Transfer-Encoding: base64
Subject: $subject
EOM5
####### メッセージボディの生成########
$body[4] .= $name;
$body[6] .= $email;
$body[13] .= $method;
$body[15] .= $fax;
$body[17] .= $email2;
$mailbody = join("\n", @body);
$encoded = encode_base64($mailbody);
######## メール送信#########
open(MAIL, "|$sendmail $okina_email");
print MAIL $mail_header;
for ($i = 0; $i < length($encoded); $i += 76) {
	print MAIL substr($encoded, $i, 76);
}
close(MAIL);
#####以上がBase64メール#####
$msg1 = "ご依頼予約完了\n";
$msg2 = "暫くしますと、ご依頼用紙がメールで届きます。\n";
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
print "<A HREF=\"/~kazu-y/j-info.html\" DIRECTKEY="1">$msg3</A><BR>\n";
print "</BODY>\n";
print "</HTML>\n";
__END__