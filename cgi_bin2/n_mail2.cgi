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
#####�ǡ�������������#####
if ($email2 ne "") {
	$email2 =~ s/\s*//g;
	#���ѱѿ����򤹤٤�Ⱦ�ѱѿ����ˤ��롣
	$email2 = &zen2han($email2);
} 
#####���������ɤ�����#####
$kanjicode = $kanji;
$kanjicode =~ s/ //g;
$kanjicode =~ s/(.)/sprintf("%02X",unpack("c",$1) >= 0 ? unpack("c",$1)
: 256 + unpack("c",$1))/eg;
$kanjicode =~ s/(....)/$1 /g;
#####��������Base64�᡼��#####
##### �ܥǥ�����ʸ��������######
@body = (
	"=====================================", 
	"����Ǥ��ʤ�����������(SJIS)��", 
	"", 
	"Ϣ��ͤ�E�᡼�륢�ɥ쥹��", 
	"", 
	"Ϣ��ͤλ�̾(����)��", 
	"", 
	"���顼����(����)��",
	"",
	"���͡����顼��ȯ�������ǽ�����⤤��", 
	"====================================="
);
foreach(@body) {
	&jcode'convert(*_, "sjis", "euc");
}
#######Sub������(Base64���󥳡���)#######
$subject = "Ƚ�����ʤ�����(Ver.4)";
&jcode'convert(*subject, 'jis', 'euc');
$subject = encode_base64($subject);
chop($subject);
$subject = "=?iso-2022-jp?B?" . $subject . "?=";
####### �إå������#########
$mail_header = <<"EOM2";
From: $email2
To: $youraddress
MIME-Version: 1.0
Content-Type: text/plain;
	charset="x-sjis-jp"
Content-Transfer-Encoding: base64
Subject: $subject
EOM2
####### ��å������ܥǥ�������########
$body[2] .= $kanjicode;
$body[4] .= $email2;
$body[6] .= $name2;
$body[8] .= $kanji;
$mailbody = join("\r\n", @body);
$encoded = encode_base64($mailbody);
######## �᡼������#########
open(MAIL, "|$sendmail $youraddress");
print MAIL $mail_header;
for ($i = 0; $i < length($encoded); $i += 76) {
	print MAIL substr($encoded, $i, 76);
}
close(MAIL);
#####�ʾ夬Base64�᡼��#####
print "Content-type: text/html\n\n";
print "<html>\n";
print "<head>\n";
#������URL�ϡ����ʤ��Υ��ݥСݤˤ��碌�Ʋ�������
print "<META HTTP-EQUIV=\"Refresh\" CONTENT=\"5;URL=/~kazu-y/input.html\">\n";
print "<title>������λ</title></head>\n";
print "<body bgcolor=\"ffffff\" TEXT=\"000000\" link=\"fb02ee\" vlink=\"fb02ee\">\n";
print "<p>\n";
print "<br>\n";
print "<br>\n";
print "<center>\n";
print "<font size=\"6\" color=\"000000\"><b>�����Ϥ��꤬�Ȥ��������ޤ�����</b></font><br>\n";
print "</center>\n";
print "</body>\n";
print "</html>\n";