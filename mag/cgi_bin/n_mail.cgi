#!/usr/local/bin/perl
$|=1;
#############################
$sendmail = "/usr/lib/sendmail";
$youraddress = 'kazu-y@mahoroba.ne.jp ';
#############################
require "cgi-lib.pl";
require "jcode.pl";
use MIME::Base64;
&ReadParse();
#############################
$name = $in{'name'};
$email = $in{'email'};
$tokuten = $in{'tokuten'};
$GONO = $in{'GONO'};
#####��������Base64�᡼��#####
##### �ܥǥ�����ʸ��������######
@body = (
	"=====================================",
	"��ʼԤΤ�̾����",
	"",
	"E�᡼�륢�ɥ쥹��",
	"",
	"������",
	"",
	"��ʼ��ֹ桧",
	"",
	"====================================="
);
foreach(@body) {
	&jcode'convert(*_, "sjis", "euc");
}
#######Sub������(Base64���󥳡���)#######
$subject = "�ƥ��ȹ�ʼ�(i�⡼��Ver.1)";
&jcode'convert(*subject, 'jis', 'euc');
$subject = encode_base64($subject);
chop($subject);
$subject = "=?iso-2022-jp?B?" . $subject . "?=";
####### �إå������#########
$mail_header = <<"EOM6";
From: $email
To: $youraddress
MIME-Version: 1.0
Content-Type: text/plain;
	charset="ISO-2022-JP"
Content-Transfer-Encoding: base64
Subject: $subject
EOM6
####### ��å������ܥǥ�������########
$body[2] .= $name;
$body[4] .= $email;
$body[6] .= $tokuten;
$body[8] .= $GONO;
$mailbody = join("\n", @body);
$encoded = encode_base64($mailbody);
######## �᡼������#########
open(MAIL, "|$sendmail $youraddress");
print MAIL $mail_header;
for ($i = 0; $i < length($encoded); $i += 76) {
	print MAIL substr($encoded, $i, 76);
}
close(MAIL);
#####�ʾ夬Base64�᡼��#####
$msg1 = "������λ\n";
$msg2 = "�����������᡼�뺹���夲�ޤ���\n";
$msg3 = "1�����Υۡ���ڡ����ء�\n";
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
print "<A HREF=\"http://www2.mahoroba.ne.jp/~kazu-y/i-mode.html\" ACCESSKEY=1>$msg3</A><BR>\n";
print "</BODY>\n";
print "</HTML>\n";
__END__
