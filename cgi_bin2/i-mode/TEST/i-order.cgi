#!/usr/local/bin/perl
$|=1;
##########################
$sendmail = "/usr/lib/sendmail";
$youraddress = 'okina@e-mail.ne.jp ';
##########################
require "cgi-lib.pl";
require "jcode.pl";
require "zenhan.pl";
&ReadParse;

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
	#͹���ֹ椬7��ʲ������Ϥ��줿��硢00���������ղä��롣
	$zipcord = $zipcord . "00000000";
	$zipcord = substr($zipcord, 0, 8);
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
#####��ʸ�᡼�������#####
$com = <<"MESSAGE";
From: $email
Subject: ���ؤ���ʸ(i�⡼��v.3)

=====================================
�������ͤλ�̾��
$name
�������ͤ�E�᡼�륢�ɥ쥹��
$email
����ʸ���ơ�
$order2
$order3

���Ҥ�������
͹���ֹ桧
$zipcord
�����ꡧ
$address
�������ֹ桧
$tel
������͡�
$fullname

̿̾�Τ���������
��(�ߤ礦��)��
$familyname
�л�ͽ������
$brthday
��̤��������ʡ�
$method
�ե��å������ֹ桧
$fax
���E�᡼����ֹ桧
$email2
���ޤǤ����ѡ�
$user
���ФΤ�̾����
$brother
����˾���ࡧ
$request

=====================================
MESSAGE

&jcode'convert(*com,"jis");
open(MAIL, "|$sendmail $youraddress");
print MAIL $com;
close(MAIL);

print "Content-type: text/html\n\n";
print "<HTML>\n";
print "<HEAD>\n";
print "<TITLE>��������մ�λ</TITLE>\n";
print "<META HTTP-EQUIV=\"Content-Type\" CONTENT=\"text/html;CHARSET=SHIFT_JIS\">\n";
print "</HEAD>\n";
print "<BODY BGCOLOR=\"#FFFFFF\" TEXT=\"#000000\" LINK=\"#0000FF\">\n";
print "<P>\n";
print "<BR>\n";
print "<BR>\n";
print "<FONT COLOR=\"#FF0000\"><B>���꤬�Ȥ��������ޤ�����</B></FONT><BR>\n";
print "<A HREF=\"/~kazu-y/i-info.html\" accesskey=1>1�����Τ餻����롣</A><BR>\n";
print "</BODY>\n";
print "</HTML>\n";
