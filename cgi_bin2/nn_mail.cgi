#!/usr/local/bin/perl
$|=1;
#########################
$sendmail = "/usr/lib/sendmail";
$okina_email = 'kazu-y@mahoroba.ne.jp';
$okina_email2 = 'okina@e-mail.ne.jp';
#########################
require 'cgi-lib.pl';
require 'jcode.pl';
require "zenhan.pl";
use MIME::Base64;
&ReadParse();
#########################
$name = $in{'name'};
$email = $in{'email'};
$order1 = $in{'order1'};
$order2 = $in{'order2'};
$order3 = $in{'order3'};
$zipcord = $in{'zipcord'};
$address = $in{'address'};
$tel = $in{'tel'};
$fullname = $in{'fullname'};
$familyname = $in{'familyname'};
$brthday = $in{'brthday'};
$user = $in{'user'};
$brother = $in{'brother'};
$request = $in{'request'};
$exp = $in{'exp'};
$kgak = $in{'kgak'};
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
#####�Ż��ܥѥ���ɤ�������#####
if ($order1 ne "" ) {
	$order1 ="�Ż��ܤ���ʸ�ʥѥ���ɤ�19580723�Ǥ�����";
    &jcode'convert(*order1, 'jis', 'euc');
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
if (($order1 eq "" ) and ($order2 eq "" ) and ($order3 eq ""))  {
	&CgiError("���ϥ��顼",
		"����ʸ������ؼ�����Ƥ��ޤ���",
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
	elsif ($tel eq "") {
		&CgiError("�����ֹ椬���Ϥ���Ƥ��ޤ��󡣸������ä�̵�����˸¤�����ֹ�Ǥ�빽�Ǥ���",
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
if ($exp ne "") {
	if ($tel eq "") {
		&CgiError("�����ֹ椬���Ϥ���Ƥ��ޤ���",
		"�֥饦���Ύ�Back���ܥ������äƺ����Ϥ��Ƥ���������");
		exit;
	}
	elsif ($zipcord eq "") {
		&CgiError("͹���ֹ椬���Ϥ���Ƥ��ޤ���",
		"�֥饦���Ύ�Back���ܥ������äƺ����Ϥ��Ƥ���������");
		exit;
	}
    elsif ($address eq "") {
		&CgiError("���꤬���Ϥ���Ƥ��ޤ���",
		"�֥饦���Ύ�Back���ܥ������äƺ����Ϥ��Ƥ���������");
		exit;
	}	
}
#####��������Base64�᡼��#####
#####��ʬ������ʸ�᡼������#####
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
	"̿̾�Τ��������ơ�", 
	"", 
	"��(�ߤ礦��)��", 
	"", 
	"�л�ͽ������", 
	"", 
	"���ޤǤ����ѡ�", 
	"", 
	"���ФΤ�̾����", 
	"", 
	"����˾���ࡧ", 
	"", 
	"=====================================",
);
foreach(@body) {
	&jcode'convert(*_, "sjis", "euc");
}
#######Sub������(Base64���󥳡���)#######
$subject = "���ؤ���ʸ(Ver.8)";
&jcode'convert(*subject, 'jis', 'euc');
$subject = encode_base64($subject);
chop($subject);
$subject = "=?iso-2022-jp?B?" . $subject . "?=";
####### �إå������#########
$mail_header = <<"EOM";
From: $email
To: $okina_email
MIME-Version: 1.0
Content-Type: text/plain;
	charset="x-sjis-jp"
Content-Transfer-Encoding: base64
Subject: $subject
EOM
####### ��å������ܥǥ�������########
$body[4] .= $name;
$body[6] .= $email;
$body[8] .= $order1;
$body[9] .= $order2;
$body[10] .= $order3;
$body[13] .= $zipcord;
$body[15] .= $address;
$body[17] .= $tel;
$body[19] .= $fullname;
$body[21] .= $exp;
$body[23] .= $familyname;
$body[25] .= $brthday;
$body[27] .= $user;
$body[29] .= $brother;
$body[31] .= $request;
$mailbody = join("\r\n", @body);
$encoded = encode_base64($mailbody);
######## �᡼������#########
open(MAIL, "|$sendmail $okina_email");
print MAIL $mail_header;
for ($i = 0; $i < length($encoded); $i += 76) {
	print MAIL substr($encoded, $i, 76);
}
close(MAIL);
#####�����褴����᡼��#####
##### �ܥǥ�����ʸ��������######
@body2 = (
	"", 
	"���ޡ����ܲ��Ǥ���", 
	"���Τ��Ӥϡ��ʲ��Τ������ĺ�����꤬�Ȥ��������ޤ���", 
	"", 
	"", 
	"", 
	"���ι�׶��(�ǹ���)", 
	"",
	"�ߤϲ����θ��¤ˤ��������ĺ���ޤ��褦���ꤤ�����夲�ޤ���",
	"͹�ذ��ء������ֹ桡00930-9-136431", 
	"����̾�����ÿ���",  
	"�ʤ�������������Ϥ����ͤ���ô�Ǥ��ꤤ�פ��ޤ���", 
);
foreach(@body2) {
	&jcode'convert(*_, "jis", "euc");
}
#######Sub������(Base64���󥳡���)#######
$subject = "����ʸ�򾵤�ޤ�����";
&jcode'convert(*subject, 'jis', 'euc');
$subject = encode_base64($subject);
chop($subject);
$subject = "=?iso-2022-jp?B?" . $subject . "?=";
####### �إå������#########
$mail_header = <<"EOM2";
From: $okina_email2
To: $email
MIME-Version: 1.0
Content-Type: text/plain;
	charset="ISO-2022-JP"
Content-Transfer-Encoding: base64
Subject: $subject
EOM2
####### ��å������ܥǥ�������########
$body2[0] .= $name;
$body2[3] .= $order1;
$body2[4] .= $order2;
$body2[5] .= $order3;
$body2[7] .= $kgak;
$mailbody = join("\r\n", @body2);
$encoded = encode_base64($mailbody);
######## �᡼������#########
open(MAIL, "|$sendmail $email");
print MAIL $mail_header;
for ($i = 0; $i < length($encoded); $i += 76) {
	print MAIL substr($encoded, $i, 76);
}
close(MAIL);
#####�ʾ夬Base64�᡼��#####
print "Content-type: text/html\n\n";
print "<html>\n";
print "<html lang=\"ja\">\n";
print "<head>\n";
print "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=EUC-JP\">\n";
print "<META HTTP-EQUIV=\"Refresh\" CONTENT=\"5;URL=/~kazu-y/index.html\">\n";
print "<title>����ʸ���մ�λ</title></head>\n";
print "<body bgcolor=\"ffffff\" TEXT=\"000000\" link=\"fb02ee\" vlink=\"fb02ee\">\n";
print "<p>\n";
print "<br>\n";
print "<br>\n";
print "<center>\n";
print "<font size=\"6\" color=\"000000\"><b>���꤬�Ȥ��������ޤ���</b></font><br>\n";
print "<font size=\"3\" color=\"000000\"><b>��������ΰ���᡼������餻��ĺ���ޤ�����</b></font><br>\n";
print "</center>\n";
print "</body>\n";
print "</html>\n";