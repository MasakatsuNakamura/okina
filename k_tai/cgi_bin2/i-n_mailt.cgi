#!/usr/local/bin/perl
$|=1;
#############################
$sendmail = "/usr/lib/sendmail";
$youraddress = 'kazu-y@mahoroba.ne.jp ';
#############################
require "cgi-lib.pl";
require "jcode.pl";
require "zenhan.pl";
use MIME::Base64;
&ReadParse();
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
#####ここからBase64メール#####
##### ボディ基本文字列の定義######
@body = (
	"=====================================", 
	"鑑定できない漢字コード(SJIS)：", 
	"", 
	"連絡人のEメールアドレス：", 
	"", 
	"連絡人の氏名(参考)：", 
	"", 
	"エラー漢字(参考)：",
	"",
	"参考：エラーが発生する可能性が高い。", 
	"====================================="
);
foreach(@body) {
	&jcode'convert(*_, "sjis", "euc");
}
#######Subの生成(Base64エンコード)#######
$subject = "判定出来ない漢字(ケータイネットVer.1)";
&jcode'convert(*subject, 'jis', 'euc');
$subject = encode_base64($subject);
chop($subject);
$subject = "=?iso-2022-jp?B?" . $subject . "?=";
####### ヘッダの定義#########
$mail_header = <<"EOM6";
From: $email2
To: $youraddress
MIME-Version: 1.0
Content-Type: text/plain;
	charset="x-sjis-jp"
Content-Transfer-Encoding: base64
Subject: $subject
EOM6
####### メッセージボディの生成########
$body[2] .= $kanjicode;
$body[4] .= $email2;
$body[6] .= $name2;
$body[8] .= $kanji;
$mailbody = join("\n", @body);
$encoded = encode_base64($mailbody);
######## メール送信#########
open(MAIL, "|$sendmail $youraddress");
print MAIL $mail_header;
for ($i = 0; $i < length($encoded); $i += 76) {
	print MAIL substr($encoded, $i, 76);
}
close(MAIL);
#####以上がBase64メール#####
$msg1 = "エラー送信完了\n";
$msg2 = "ご協力ありがとうございました。\n";
$msg3 = "1→もう一度鑑定する。\n";
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
print "<A HREF=\"http://www2.mahoroba.ne.jp/~kazu-y/k_tai/i-mode2t.shtml\" accesskey=1>$msg3</A><BR>\n";
print "</BODY>\n";
print "</HTML>\n";
__END__