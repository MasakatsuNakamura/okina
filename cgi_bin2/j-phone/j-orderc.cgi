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
$order = $in{'order'};
######入力データの整形処理######
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
#####手段を文章化#####
if ($order eq "change") {
	$order ="改名の相談（名前を変えたい）";
}
if ($order eq "pen") {
	$order ="選名の依頼（お仕事上のお名前、雅号、ペンネーム、芸名など）";
}
if ($order eq "corp") {
	$order ="会社名の選名";
}
&jcode'convert(*order, 'jis', 'euc');
#####ここからBase64メール#####
##### ボディ基本文字列の定義######
@body = (
	"=====================================", 
	"山本翁への「ご相談」ご依頼フォーム", 
	"下記の※欄をご記入の上、「返信」して下さい。", 
	"申込人様の氏名：", 
	"※", 
	"申込人様のEメールアドレス：", 
	"※", 
	"ご依頼内容：",
	"※",
	"ご要望事項（具体的に）：", 
	"※", 
	"", 
	"名前を付けられる方の情報（改名・選名の場合）", 
	"姓（みょうじ：必ず漢字でお願い致します）：", 
	"※", 
	"名：", 
	"※", 
	"生年月日：", 
	"※", 
	"性別：", 
	"※", 
	"ご職業または、業務内容：", 
	"※", 
    "",
	"会社の情報（会社名の場合）", 
	"会社の業務内容（具体的に）：", 
    "※",
	"", 
	"", 
	"受注後、振込先を申込人さまにご連絡致します。", 
    "お振り込み確認後、2-3日で結果をお知らせします。",
	"====================================="
);
foreach(@body) {
	&jcode'convert(*_, "sjis", "euc");
}
#######Subの生成(Base64エンコード)#######
$subject = "翁へご相談(jフォンVer.1)";
&jcode'convert(*subject, 'jis', 'euc');
$subject = encode_base64($subject);
chop($subject);
$subject = " . $subject . "?=";
####### ヘッダの定義#########
$mail_header = <<"EOM6";
From: $okina_email
To: $email
MIME-Version: 1.0
Content-Type: text/plain;
	charset="x-sjis-jp"
Content-Transfer-Encoding: base64
Subject: $subject
EOM6
####### メッセージボディの生成########
$body[4] .= $name;
$body[6] .= $email;
$body[8] .= $order;
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
$msg1 = "ご相談予約完了\n";
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
print "<A HREF=\"/~kazu-y/j-info2.html\" DIRECTKEY="1">$msg3</A><BR>\n";
print "</BODY>\n";
print "</HTML>\n";
__END__