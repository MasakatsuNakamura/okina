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
$order2 = $in{'order2'};
$order3 = $in{'order3'};
$zipcord = $in{'zipcord'};
$address = $in{'address'};
$tel = $in{'tel'};
$fax = $in{'fax'};
$fullname = $in{'fullname'};
$familyname = $in{'familyname'};
$brthday = $in{'brthday'};
$method = $in{'method'};
$user = $in{'user'};
$brother = $in{'brother'};
$request = $in{'request'};
######���ϥǡ�������������######
if ($zipcord ne "") {
	$zipcord =~ s/\s*//g;
	#���ѱѿ����򤹤٤�Ⱦ�ѱѿ����ˤ��롣
	$zipcord = &zen2han($zipcord); 
}
if ($tel ne "") {
	$tel =~ s/\s*//g;
	#���ѱѿ����򤹤٤�Ⱦ�ѱѿ����ˤ��롣
	$tel = &zen2han($tel); 
}
if ($fax ne "") {
	$fax =~ s/\s*//g;
	#���ѱѿ����򤹤٤�Ⱦ�ѱѿ����ˤ��롣
	$fax = &zen2han($fax); 
}
if ($familyname ne "") {
	$familyname =~ s/\s*//g;
}
if ($brthday ne "") {
	$brthday =~ s/\s*//g;
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
if ($order2 ne "") {
	if ($zipcord eq "") {
		&CgiError("͹���ֹ椬���Ϥ���Ƥ��ޤ���",
		"�֥饦���Ύ�Back���ܥ������äƺ����Ϥ��Ƥ���������");
		exit;
	}
	elsif ($address eq "") {
		&CgiError("���꤬���Ϥ���Ƥ��ޤ���",
		"�֥饦���Ύ�Back���ܥ������äƺ����Ϥ��Ƥ���������");
		exit;
	}	
	elsif ($fullname eq "") {
		&CgiError("����ͤ����Ϥ���Ƥ��ޤ���",
		"�֥饦���Ύ�Back���ܥ������äƺ����Ϥ��Ƥ���������");
		exit;
	}
}
if ($order3 ne "") {
	if ($familyname eq "") {
		&CgiError("�Ļ�(��)�����Ϥ���Ƥ��ޤ���",
		"�֥饦���Ύ�Back���ܥ������äƺ����Ϥ��Ƥ���������");
		exit;
	}
	elsif ($brthday eq "") {
		&CgiError("ͽ����(������)�����Ϥ���Ƥ��ޤ���",
		"�֥饦���Ύ�Back���ܥ������äƺ����Ϥ��Ƥ���������");
		exit;
	}
}
if (($order3 ne "") and ($method eq "fax")) {
	if ($fax eq "") {
		&CgiError("������Υե��å����ֹ椬���Ϥ���Ƥ��ޤ���",
		"�֥饦���Ύ�Back���ܥ������äƺ����Ϥ��Ƥ���������");
		exit;
	}
}
if (($order3 ne "") and ($method eq "mail")) {
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
	$method ="�ե��å��������äƤ���������";
}
if ($method eq "mail") {
	$method ="�᡼�뤷�Ʋ�������";
}
&jcode'convert(*method, 'jis', 'euc');
#####��������Base64�᡼��#####
##### �ܥǥ�����ʸ��������######
@body = (
	"=====================================", 
	"���ܲ����ޤء��ʲ�����ʸ���פ�������", 
	"", 
	"�������ͤλ�̾��", 
	"", 
	"�������ͤ�E�᡼�륢�ɥ쥹��", 
	"", 
	"����ʸ���ơ�",
	"",
	"",
    "",  
	"���Ҥ�������ޤ���Ϣ����", 
	"͹���ֹ桧", 
	"", 
	"�����ꡧ", 
	"", 
	"�������ֹ桧", 
	"", 
	"������͡�", 
	"", 
    "",
	"̿̾�Τ���������", 
	"��(�ߤ礦��)��", 
	"", 
	"�л�ͽ������", 
	"", 
    "��̤��������ʡ�",
    "",
    "�ե��å������ֹ桧",
    "",
    "���E�᡼����ֹ桧",
    "",
	"���ޤǤ����ѡ�", 
	"", 
	"���ФΤ�̾����", 
	"", 
	"����˾���ࡧ", 
	"", 
	"====================================="
);
foreach(@body) {
	&jcode'convert(*_, "sjis", "euc");
}
#######Sub������(Base64���󥳡���)#######
$subject = "���ؤ���ʸ(i�⡼��Ver.4)";
&jcode'convert(*subject, 'jis', 'euc');
$subject = encode_base64($subject);
chop($subject);
$subject = "=?iso-2022-jp?B?" . $subject . "?=";
####### �إå������#########
$mail_header = <<"EOM4";
From: $email
To: $okina_email
MIME-Version: 1.0
Content-Type: text/plain;
	charset="x-sjis-jp"
Content-Transfer-Encoding: base64
Subject: $subject
EOM4
####### ��å������ܥǥ�������########
$body[4] .= $name;
$body[6] .= $email;
$body[8] .= $order2;
$body[9] .= $order3;
$body[13] .= $zipcord;
$body[15] .= $address;
$body[17] .= $tel;
$body[19] .= $fullname;
$body[23] .= $familyname;
$body[25] .= $brthday;
$body[27] .= $method;
$body[29] .= $fax;
$body[31] .= $email2;
$body[33] .= $user;
$body[35] .= $brother;
$body[37] .= $request;
$mailbody = join("\r\n", @body);
$encoded = encode_base64($mailbody);
######## �᡼������#########
open(MAIL, "|$sendmail $okina_email");
print MAIL $mail_header;
for ($i = 0; $i < length($encoded); $i += 76) {
	print MAIL substr($encoded, $i, 76);
}
close(MAIL);
#####�ʾ夬Base64�᡼��#####
$msg1 = "��������մ�λ\n";
$msg2 = "���꤬�Ȥ��������ޤ�����\n";
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
print "<A HREF=\"/~kazu-y/i-info.html\" ACCESSKEY=1>$msg3</A><BR>\n";
print "</BODY>\n";
print "</HTML>\n";
__END__