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
######���ϥǡ�������������######
if ($email ne "") {
	$email =~ s/\s*//g;
	#���ѱѿ����򤹤٤�Ⱦ�ѱѿ����ˤ��롣
	$email = &zen2han($email);
} 
#####���ϥ��顼�Υ����å�#####
if ($name =~ /^\s*$/){
	&CgiError("̾���ε���������ޤ���",
	"�֥饦���Ύ�Back���ܥ������äƺ����Ϥ��Ƥ���������");
	exit;
}
if ($email =~ /^\s*$/){
	&CgiError("�᡼�륢�ɥ쥹�ε���������ޤ���",
	"�֥饦���Ύ�Back���ܥ������äƺ����Ϥ��Ƥ���������");
	exit;
}
elsif (($email) and (not $email =~ /.+\@.+\..+/)) {
	&CgiError("���ϥ��顼",
		"�᡼�륢�ɥ쥹�ν������ְ�äƤ��ޤ���",$email,
		"�֥饦���Ύ�Back���ܥ������äƺ����Ϥ��Ƥ���������");
	exit;
}
#####���ʤ�ʸ�ϲ�#####
if ($order eq "change") {
	$order ="��̾�����̡�̾�����Ѥ�������";
}
if ($order eq "pen") {
	$order ="��̾�ΰ���ʤ��Ż���Τ�̾������桢�ڥ�͡��ࡢ��̾�ʤɡ�";
}
if ($order eq "corp") {
	$order ="���̾����̾";
}
&jcode'convert(*order, 'jis', 'euc');
#####��������Base64�᡼��#####
##### �ܥǥ�����ʸ��������######
@body = (
	"=====================================", 
	"���ܲ��ؤΡ֤����̡פ�����ե�����", 
	"�����΢���򤴵����ξ塢���ֿ��פ��Ʋ�������", 
	"�������ͤλ�̾��", 
	"��", 
	"�������ͤ�E�᡼�륢�ɥ쥹��", 
	"��", 
	"���������ơ�",
	"��",
	"����˾����ʶ���Ū�ˡˡ�", 
	"��", 
	"", 
	"̾�����դ��������ξ���ʲ�̾����̾�ξ���", 
	"���ʤߤ礦����ɬ�������Ǥ��ꤤ�פ��ޤ��ˡ�", 
	"��", 
	"̾��", 
	"��", 
	"��ǯ������", 
	"��", 
	"���̡�", 
	"��", 
	"�����Ȥޤ��ϡ���̳���ơ�", 
	"��", 
    "",
	"��Ҥξ���ʲ��̾�ξ���", 
	"��Ҥζ�̳���ơʶ���Ū�ˡˡ�", 
    "��",
	"", 
	"", 
	"����塢������򿽹��ͤ��ޤˤ�Ϣ���פ��ޤ���", 
    "��������߳�ǧ�塢2-3���Ƿ�̤��Τ餻���ޤ���",
	"====================================="
);
foreach(@body) {
	&jcode'convert(*_, "sjis", "euc");
}
#######Sub������(Base64���󥳡���)#######
$subject = "���ؤ�����(j�ե���Ver.1)";
&jcode'convert(*subject, 'jis', 'euc');
$subject = encode_base64($subject);
chop($subject);
$subject = "=?iso-2022-jp?B?" . $subject . "?=";
####### �إå������#########
$mail_header = <<"EOM6";
From: $okina_email
To: $email
MIME-Version: 1.0
Content-Type: text/plain;
	charset="x-sjis-jp"
Content-Transfer-Encoding: base64
Subject: $subject
EOM6
####### ��å������ܥǥ�������########
$body[4] .= $name;
$body[6] .= $email;
$body[8] .= $order;
$mailbody = join("\n", @body);
$encoded = encode_base64($mailbody);
######## �᡼������#########
open(MAIL, "|$sendmail $okina_email");
print MAIL $mail_header;
for ($i = 0; $i < length($encoded); $i += 76) {
	print MAIL substr($encoded, $i, 76);
}
close(MAIL);
#####�ʾ夬Base64�᡼��#####
$msg1 = "������ͽ��λ\n";
$msg2 = "�ä����ޤ��ȡ��������ѻ椬�᡼����Ϥ��ޤ���\n";
$msg3 = "1�����Τ餻����롣\n";
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