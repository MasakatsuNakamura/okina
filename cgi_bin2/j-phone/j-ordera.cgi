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
#####�ǡ����μ�����#####
$name = $in{'name'};
$email = $in{'email'};
$email2 = $in{'email2'};
$fax = $in{'fax'};
$method = $in{'method'};
######���ϥǡ�������������######
if ($fax ne "") {
	$fax =~ s/\s*//g;
	#���ѱѿ����򤹤٤�Ⱦ�ѱѿ����ˤ��롣
	$fax = &zen2han($fax); 
}
if ($email ne "") {
	$email =~ s/\s*//g;
	#���ѱѿ����򤹤٤�Ⱦ�ѱѿ����ˤ��롣
	$email = &zen2han($email);
} 
if ($email2 ne "") {
	$email2 =~ s/\s*//g;
	#���ѱѿ����򤹤٤�Ⱦ�ѱѿ����ˤ��롣
	$email2 = &zen2han($email);
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
if ($method eq "fax") {
	if ($fax eq "") {
		&CgiError("������Υե��å����ֹ椬���Ϥ���Ƥ��ޤ���",
		"�֥饦���Ύ�Back���ܥ������äƺ����Ϥ��Ƥ���������");
		exit;
	}
}
if ($method eq "mail") {
	if ($email2 =~ /^\s*$/){
	&CgiError("���Ϣ����Υ᡼�륢�ɥ쥹�ε���������ޤ���",
	"�֥饦���Ύ�Back���ܥ������äƺ����Ϥ��Ƥ���������");
	exit;
    }
    elsif (($email2) and (not $email2 =~ /.+\@.+\..+/)) {
	&CgiError("���ϥ��顼",
		"���Ϣ����Υ᡼�륢�ɥ쥹�ν������ְ�äƤ��ޤ���",$email2,
		"�֥饦���Ύ�Back���ܥ������äƺ����Ϥ��Ƥ���������");
	exit;
    }
}
#####���ʤ�ʸ�ϲ�#####
if ($method eq "fax") {
	$method ="�ե��å����Ǥμ������˾";
}
if ($method eq "mail") {
	$method ="�ѥ����󤫤�᡼��������˾";
}
&jcode'convert(*method, 'jis', 'euc');
#####��������Base64�᡼��#####
##### �ܥǥ�����ʸ��������######
@body = (
	"=====================================", 
	"���ܲ��ؤΡֿ�����̿̾�פ�����ե�����", 
	"�����΢�������Ƥ������ξ塢���ֿ��פ��Ʋ�������", 
	"�������ͤλ�̾��", 
	"��", 
	"�������ͤ�E�᡼�륢�ɥ쥹��", 
	"��",  
	"̿̾�Τ��������ƤˤĤ���", 
	"��(�ߤ礦����ɬ�������Ǥ�������������)��", 
	"��", 
	"�л�ͽ������̤������Ϥ����褽�Ƿ빽�Ǥ��ˡ�", 
	"��", 
    "��̤��������ʡ�",
    "��",
    "�ե��å������ֹ�ʤ���˾�ԤΤߡˡ�",
    "��",
    "�ѥ������E�᡼�륢�ɥ쥹�ʤ���˾�ԤΤߡˡ�",
    "��",
	"���ޤǡֲ���̿̾�פ����Ѥʤ����ޤ���������", 
	"", 
	"���ФΤ�̾���ʺ����٤��ʤ���Сˡ�", 
	"", 
	"����˾���ࡧ", 
	"", 
	"", 
	"", 
	"���ޤ������ϡ����λݤ�������������", 
	"", 
	"����塢������򿽹��ͤ��ޤˤ�Ϣ���פ��ޤ���", 
	"��������߳�ǧ�塢2-3���Ƿ�̤��Τ餻���ޤ���", 
	"====================================="
);
foreach(@body) {
	&jcode'convert(*_, "sjis", "euc");
}
#######Sub������(Base64���󥳡���)#######
$subject = "���ؤ���ʸ(j�ե���Ver.1)";
&jcode'convert(*subject, 'jis', 'euc');
$subject = encode_base64($subject);
chop($subject);
$subject = "=?iso-2022-jp?B?" . $subject . "?=";
####### �إå������#########
$mail_header = <<"EOM5";
From: $okina_email
To: $email
MIME-Version: 1.0
Content-Type: text/plain;
	charset="x-sjis-jp"
Content-Transfer-Encoding: base64
Subject: $subject
EOM5
####### ��å������ܥǥ�������########
$body[4] .= $name;
$body[6] .= $email;
$body[13] .= $method;
$body[15] .= $fax;
$body[17] .= $email2;
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
print "<A HREF=\"/~kazu-y/j-info.html\" DIRECTKEY="1">$msg3</A><BR>\n";
print "</BODY>\n";
print "</HTML>\n";
__END__