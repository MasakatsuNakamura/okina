#!/usr/local/bin/perl
$|=1;
require "cgi-lib.pl";
require "jcode.pl";
require "zenhan.pl";

$root = "/~kazu-y";
$cgipath = "/~kazu-y/cgi_bin2";
$baseurl = "http://www2.mahoroba.ne.jp";

&ReadParse;
#####�ǡ����μ�����#####
$name = $in{'name'};
$email = $in{'email'};
$order3 = $in{'order3'};
$familyname = $in{'familyname'};
$brthday = $in{'brthday'};
$user = $in{'user'};
$brother = $in{'brother'};

######���ϥǡ�������������######
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
if ($order3 eq "")  {
	&CgiError("���ϥ��顼",
		"����ʸ������ؼ�����Ƥ��ޤ���",
		"�֥饦���Ύ�Back���ܥ������äƺ����Ϥ��Ƥ���������");
	exit;
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

#####��ʸɼ����ɽ��#####
$msg = <<"ORDER2";
Content-type: text/html

<HTML>
<HEAD>
   <TITLE>̿̾�Τ�����(1/2)</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=SHIFT_JIS">
</HEAD>
<BODY BGCOLOR="#FFFFFF" TEXT="#000000" LINK="#0000FF">
<P><FORM ACTION="$cgipath/j-order.cgi" METHOD=GET>
   <P><INPUT TYPE=hidden NAME=name VALUE="\$name">
   <INPUT TYPE=hidden NAME=email VALUE="\$email">
   <INPUT TYPE=hidden NAME=order3 VALUE="\$order3">
   <INPUT TYPE=hidden NAME=familyname VALUE="\$familyname">
   <INPUT TYPE=hidden NAME=brthday VALUE="\$brthday">
   <INPUT TYPE=hidden NAME=user VALUE="\$user">
   <INPUT TYPE=hidden NAME=brother VALUE="\$brother"></P>
   
   <P><B><U>����˾����</U></B><U>��(�����Ԥ�ź���ʤ����⤢��ޤ�����λ����������)</U><BR>
   <TEXTAREA NAME=request ROWS=6 COLS=10 WRAP=virtual></TEXTAREA></P>
   
   <P><B><U>��̤Τ�Ϣ����ˡ</U></B><BR>
   <INPUT TYPE=radio NAME=method VALUE=fax CHECKED>�ե��å����Ǽ���������1.�ˤ������ֹ�򤴵�����������<BR>
   <INPUT TYPE=radio NAME=method VALUE=mail>E�᡼��Ǽ���<FONT COLOR="#FF0000">�ʥѥ����������餴�����������������äϼ����Բ�)</FONT>������2.�˥��ɥ쥹�򤴵�����������</P>
   
   <P><B><U>1.�ե��å����ֹ�</U></B><BR>
   <INPUT TYPE=text NAME=fax VALUE="" SIZE=16 MODE=numeric></P>
   
   <P><B><U>2.E�᡼�륢�ɥ쥹<BR>
   </U></B><INPUT TYPE=text NAME=email2 VALUE="" SIZE=16 MAXLENGTH=80 MODE=alphabet></P>
   
   <P><FONT COLOR="#FF0000"><B>���Ϥϰʾ�Ǥ������Ƥ򤴳�ǧ�ξ塢����ʸ�ܥ����1���������å����Ʋ�������<BR>
   ����ʸ���ո塢�����꤬�Ȥ��������ޤ������β��̤�ɽ�����졢TOP�ڡ��������ޤ���</B></FONT></P>
   
   <P><FONT COLOR="#FF0000"><B>�ʤ�������ʸ�Υ���󥻥�Ͻ���ޤ���Τǡ��褯���Τ��᲼������</B></FONT></P>
   
   <P><B><INPUT TYPE=submit NAME="����" VALUE="����ʸ"></B><INPUT TYPE=reset VALUE="�ꥻ�å�">
</FORM></P>

<P><B>����꤯��ʸ�Ǥ��ʤ����ˤϡ��嵭���Ƥ�</B><A HREF="mailto:okina\@e-mail.ne.jp" DIRECTKEY="0"><B>�᡼��(0�ܥ���򲡤��Ʋ�������)</B></A>(okina\@e-mail.ne.jp)<B>�ˤ����ղ�������</B></P>
</BODY>
</HTML>
ORDER2
	&jcode'convert(*msg, "sjis", "euc");
	$msg =~ s/\$name/$name/g;
	$msg =~ s/\$email/$email/g;
	$msg =~ s/\$order3/$order3/g;
	$msg =~ s/\$familyname/$familyname/g;
	$msg =~ s/\$brthday/$brthday/g;
	$msg =~ s/\$user/$user/g;
	$msg =~ s/\$brother/$brother/g;
	print $msg;
__END__


