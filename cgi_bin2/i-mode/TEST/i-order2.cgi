#!/usr/local/bin/perl
$|=1;
#########################
$sendmail = "/usr/lib/sendmail";
$youraddress = 'okina@e-mail.ne.jp';
#########################
require "cgi-lib.pl";
require "jcode.pl";
require "zenhan.pl";
&ReadParse;
#########################
$name = $in{'name'};
$email = $in{'email'};
$order4 = $in{'order4'};
$order6 = $in{'order6'};
$order7 = $in{'order7'};
$familyname1 = $in{'familyname1'};
$firstname1 = $in{'firstname1'};
$birthday1= $in{'birthday1'};
$sex1 = $in{'sex1'};
$trade1 = $in{'trade1'};
$familyname2 = $in{'familyname2'};
$firstname2 = $in{'firstname2'};
$birthday2= $in{'birthday2'};
$sex2 = $in{'sex2'};
$trade2 = $in{'trade2'};
$request = $in{'request'};

######���ϥǡ�������������######
if ($familyname1 ne "") {
	$familyname1 =~ s/\s*//g;
}
if ($familyname2 ne "") {
	$familyname2 =~ s/\s*//g;
}
if ($firstname1 ne "") {
	$familyname1 =~ s/\s*//g;
}
if ($firstname2 ne "") {
	$familyname3 =~ s/\s*//g;
}
if ($birthday1 ne "") {
	$birthday1 =~ s/\s*//g;
}
if ($birthday2 ne "") {
	$birthday3 =~ s/\s*//g;
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
if ($order4 ne "") {
	if ($familyname1 eq "") {
		&CgiError("�������Ϥ���Ƥ��ޤ���",
		"�֥饦���Ύ�Back���ܥ������äƺ����Ϥ��Ƥ���������");
		exit;
	}
	elsif ($firstname1 eq "") {
		&CgiError("̾�����Ϥ���Ƥ��ޤ���",
		"�֥饦���Ύ�Back���ܥ������äƺ����Ϥ��Ƥ���������");
		exit;
	}	
	elsif ($birthday1 eq "") {
		&CgiError("��ǯ���������Ϥ���Ƥ��ޤ���",
		"�֥饦���Ύ�Back���ܥ������äƺ����Ϥ��Ƥ���������");
		exit;
	}
	elsif ($trade1 eq "") {
		&CgiError("���Ż����Ƥޤ��ϡ�̾�������Ӥ����Ϥ���Ƥ��ޤ���",
		"�֥饦���Ύ�Back���ܥ������äƺ����Ϥ��Ƥ���������");
		exit;
	}
}
if ($order6 ne "") {
	if ($familyname1 eq "") {
		&CgiError("�����¦���������Ϥ���Ƥ��ޤ���",
		"�֥饦���Ύ�Back���ܥ������äƺ����Ϥ��Ƥ���������");
		exit;
	}
   elsif ($firstname1 eq "") {
		&CgiError("�����¦��̾�����Ϥ���Ƥ��ޤ���",
		"�֥饦���Ύ�Back���ܥ������äƺ����Ϥ��Ƥ���������");
		exit;
	}
   elsif ($birthday1 eq "") {
		&CgiError("�����¦����ǯ���������Ϥ���Ƥ��ޤ���",
		"�֥饦���Ύ�Back���ܥ������äƺ����Ϥ��Ƥ���������");
		exit;
	}
   elsif ($trade1 eq "") {
		&CgiError("�����¦�Τ����Ȥ����Ϥ���Ƥ��ޤ���",
		"�֥饦���Ύ�Back���ܥ������äƺ����Ϥ��Ƥ���������");
		exit;
	}
   elsif ($familyname2 eq "") {
		&CgiError("���¦���������Ϥ���Ƥ��ޤ���",
		"�֥饦���Ύ�Back���ܥ������äƺ����Ϥ��Ƥ���������");
		exit;
	}
   elsif ($firstname2 eq "") {
		&CgiError("���¦��̾�����Ϥ���Ƥ��ޤ���",
		"�֥饦���Ύ�Back���ܥ������äƺ����Ϥ��Ƥ���������");
		exit;
	}
   elsif ($birthday2 eq "") {
		&CgiError("���¦����ǯ���������Ϥ���Ƥ��ޤ���",
		"�֥饦���Ύ�Back���ܥ������äƺ����Ϥ��Ƥ���������");
		exit;
	}
   elsif ($trade2 eq "") {
		&CgiError("���¦�Τ����Ȥ����Ϥ���Ƥ��ޤ���",
		"�֥饦���Ύ�Back���ܥ������äƺ����Ϥ��Ƥ���������");
		exit;
	}
   elsif ($request eq "") {
		&CgiError("���������Ƥ򤪽񤭲�������",
		"�֥饦���Ύ�Back���ܥ������äƺ����Ϥ��Ƥ���������");
		exit;
	}
}
if ($order7 ne "") {
	if ($familyname1 eq "") {
		&CgiError("�������Ϥ���Ƥ��ޤ���",
		"�֥饦���Ύ�Back���ܥ������äƺ����Ϥ��Ƥ���������");
		exit;
	}
   elsif ($firstname1 eq "") {
		&CgiError("̾�����Ϥ���Ƥ��ޤ���",
		"�֥饦���Ύ�Back���ܥ������äƺ����Ϥ��Ƥ���������");
		exit;
	}
   elsif ($birthday1 eq "") {
		&CgiError("��ǯ���������Ϥ���Ƥ��ޤ���",
		"�֥饦���Ύ�Back���ܥ������äƺ����Ϥ��Ƥ���������");
		exit;
	}
   elsif ($trade1 eq "") {
		&CgiError("�����Ȥ����Ϥ���Ƥ��ޤ���",
		"�֥饦���Ύ�Back���ܥ������äƺ����Ϥ��Ƥ���������");
		exit;
	}
   elsif ($request eq "") {
		&CgiError("���������Ƥ򤪽񤭲�������",
		"�֥饦���Ύ�Back���ܥ������äƺ����Ϥ��Ƥ���������");
		exit;
	}
}

#####��ʸ�᡼�������#####
$com = <<"MESSAGE3";
From: $email
Subject: ���ؤ�����(i�⡼��v.1)

=====================================
���ܲ����ޤء��ʲ��Τ����̤��פ�������

�������ͤλ�̾��
$name
�������ͤ�E�᡼�륢�ɥ쥹��
$email
���������ơ�
$order4 
$order6 
$order7 
����˾���ࡧ
$request

������Ԥξ���
����
$familyname1
̾��
$firstname1
��ǯ������
$birthday1
���̡�
$sex1
�����ȡ���̳���ơ�
$trade1
�뺧�������
$sei

������ξ���
����
$familyname2 
̾��
$firstname2
��ǯ������
$birthday2
���̡�
$sex2 
�����ȡ�
$trade2

=====================================
MESSAGE3

&jcode'convert(*com,"jis");
open(MAIL, "|$sendmail $youraddress");
print MAIL $com;
close(MAIL);

print "Content-type: text/html\n\n";
print "<HTML>\n";
print "<HEAD>\n";
print "<TITLE>�����̼��մ�λ</TITLE>\n";
print "<META HTTP-EQUIV=\"Content-Type\" CONTENT=\"text/html;CHARSET=SHIFT_JIS\">\n";
print "</HEAD>\n";
print "<BODY BGCOLOR=\"#FFFFFF\" TEXT=\"#000000\" LINK=\"#0000FF\">\n";
print "<P>\n";
print "<BR>\n";
print "<BR>\n";
print "<FONT COLOR=\"#FF0000\"><B>���꤬�Ȥ��������ޤ�����</B></FONT><BR>\n";
print "<A HREF=\"/~kazu-y/i-info2.html\" accesskey=1>1�����Τ餻����롣</A><BR>\n";
print "</BODY>\n";
print "</HTML>\n";
