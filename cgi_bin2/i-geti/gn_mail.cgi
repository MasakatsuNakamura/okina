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

#####��ʸ�᡼�������#####
$com = <<"MESSAGE";
From: $email
Subject: ���ܲ��ؤΤ���ʸ(i-geti/Ver.4)

=====================================
�������ͤλ�̾��
$name
�������ͤ�E�᡼�륢�ɥ쥹��
$email
����ʸ���ơ�
$order1
$order2
$order3

���Ҥ�������ޤ��Ϥ�Ϣ����
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
print "<html>\n";
print "<head>\n";
#������URL�ϡ����ʤ��Υ��ݥСݤˤ��碌�Ʋ�������
print "<META HTTP-EQUIV=\"Refresh\" CONTENT=\"5;URL=/~kazu-y/i-geti.html\">\n";
print "<title>����ʸ���մ�λ</title></head>\n";
print "<body bgcolor=\"ffffff\" TEXT=\"000000\" link=\"fb02ee\" vlink=\"fb02ee\">\n";
print "<p>\n";
print "<br>\n";
print "<br>\n";
print "<center>\n";
print "<font size=\"6\" color=\"000000\"><b>���꤬�Ȥ��������ޤ�����</b></font><br>\n";
print "</center>\n";
print "</body>\n";
print "</html>\n";
