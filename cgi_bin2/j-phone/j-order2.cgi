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
	"����˾���ࡧ", 
	"", 
	"", 
	"������Ԥξ���", 
	"����", 
	"", 
	"̾��", 
	"", 
	"��ǯ������", 
	"", 
	"���̡�", 
	"", 
	"�����Ȥޤ��ϡ���̳���ơ�", 
	"", 
    "",
	"�뺧�������", 
	"", 
    "������ξ���",
	"����", 
	"", 
	"̾��", 
    "",
    "��ǯ������",
    "",
    "���̡�",
    "",
	"�����ȡ�", 
    "",
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
$mail_header = <<"EOM5";
From: $email
To: $okina_email
MIME-Version: 1.0
Content-Type: text/plain;
	charset="x-sjis-jp"
Content-Transfer-Encoding: base64
Subject: $subject
EOM5
####### ��å������ܥǥ�������########
$body[4] .= $name;
$body[6] .= $email;
$body[8] .= $order4;
$body[9] .= $order6;
$body[10] .= $order7;
$body[12] .= $request;
$body[16] .= $familyname1;
$body[18] .= $firstname1;
$body[20] .= $birthday1;
$body[22] .= $sex1;
$body[24] .= $trade1;
$body[27] .= $sei;
$body[30] .= $familyname2;
$body[32] .= $firstname2;
$body[34] .= $birthday2;
$body[36] .= $sex2;
$body[38] .= $trade2;
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
$msg1 = "�����̼��մ�λ\n";
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
print "<A HREF=\"/~kazu-y/j-info2.html\" DIRECTKEY="1">$msg3</A><BR>\n";
print "</BODY>\n";
print "</HTML>\n";
__END__