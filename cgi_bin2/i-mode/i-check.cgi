#!/usr/local/bin/perl
$|=1;
#########################
require 'cgi-lib.pl';
require 'jcode.pl';
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
	$method ="�Żҥ᡼������äƤ���������";
}
&jcode'convert(*method, 'jis', 'euc');
######������������Ѥ������������ɽ������######
#########���ҤΤ���ʸ##########
if ($order2 ne "")  {
	$msg = <<"ORDER020";
Content-type: text/html

<HTML>
<HEAD>
<TITLE>���ҤΤ���ʸ</TITLE>
<META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=x-sjis">
</HEAD>
<BODY BGCOLOR="#FFFFFF">
<P>
<CENTER><B><U>����ʸ���ƤΤ���ǧ</U></B></CENTER>        
<BLOCKQUOTE>���β��̤ϡ�����ʸ���Ƥ򤴳�ǧĺ������Τ�ΤǤ������Ƥ˸�꤬������ϡ��֥饦���Ρ����ץܥ���򲡤��Ǝ����ϥե����������齤�����Ʋ�����������ǵ�������С���ʸ�ץܥ���򲡤��Ʋ�������</BLOCKQUOTE>         
<CENTER><B>����ʸ����</B></CENTER><BR>
<HR>
���ʤ��Τ�̾���ʤ������͡�<BR>
\$name<BR>
�᡼�륢�ɥ쥹<BR>
\$email<BR>
���Ҥ�������ˤĤ���<BR>
͹���ֹ�<BR>
\$zipcord<BR>
������<BR>
\$address<BR>
������Τ������ֹ�<BR>
\$tel<BR>
����ͤ���̾<BR>
\$fullname<BR>
<HR>         
<BLOCKQUOTE><B>����ǧ���Ѥߤޤ�����</B><FONT COLOR="#FF0000"><B>��������ʸ���ܥ����1����������Ƥ�ȯ��</B></FONT><B>����������<BR>
�ʤ������ʤ����ʾ塢����ʹߤΤ���ʸ�μ��ä������ʤϰ��ڽ���ޤ���Τ�ͽ�ᤴλ����������(ˬ������ˡ�Υ�����󥰥��դ�Ŭ�Ѥ���ޤ��󡣡�</B></BLOCKQUOTE>        
����ʸ�������ϡ��֥饦���Ύ���뎣�ǎ����ϥե�������������ľ���Ʋ�������<BR>          <P><FORM ACTION="/~kazu-y/cgi_bin2/in-order.cgi" METHOD=POST>
            <P><INPUT TYPE="hidden" NAME="name" VALUE="\$name">
            <INPUT TYPE="hidden" NAME="email" VALUE="\$email">
            <INPUT TYPE="hidden" NAME="email2" VALUE="">
            <INPUT TYPE="hidden" NAME="order2" VALUE="\$order2">
            <INPUT TYPE="hidden" NAME="order3" VALUE="">
            <INPUT TYPE="hidden" NAME="zipcord" VALUE="\$zipcord">
            <INPUT TYPE="hidden" NAME="address" VALUE="\$address">
            <INPUT TYPE="hidden" NAME="tel" VALUE="\$tel">
            <INPUT TYPE="hidden" NAME="fax" VALUE="">
            <INPUT TYPE="hidden" NAME="fullname" VALUE="\$fullname">
            <INPUT TYPE="hidden" NAME="familyname" VALUE="">
            <INPUT TYPE="hidden" NAME="brthday" VALUE="">
            <INPUT TYPE="hidden" NAME="method" VALUE="">
            <INPUT TYPE="hidden" NAME="user" VALUE="">
            <INPUT TYPE="hidden" NAME="brother" VALUE="">
            <INPUT TYPE="hidden" NAME="request" VALUE="">
            <INPUT TYPE="hidden" NAME="kgak" VALUE="1,810">
            <CENTER><INPUT TYPE=submit NAME="����" VALUE="��ʸ">
         </FORM></P>
</P>
</BODY>
</HTML>
ORDER020
&jcode'convert(*msg, "sjis", "euc");
	$msg =~ s/\$name/$name/g;
	$msg =~ s/\$email/$email/g;
	$msg =~ s/\$order2/$order2/g;		
	$msg =~ s/\$zipcord/$zipcord/g;
	$msg =~ s/\$address/$address/g;
	$msg =~ s/\$tel/$tel/g;
	$msg =~ s/\$fullname/$fullname/g;
	print $msg;
}
###########̿̾�Τ߰���############
elsif ($order3 ne "")  {
	$msg = <<"ORDER003";
Content-type: text/html

<HTML>
<HEAD>
<TITLE>̿̾�Τ�����</TITLE>
<META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=x-sjis">
</HEAD>
<BODY BGCOLOR="#FFFFFF">
<P>
<CENTER><B><U>����ʸ���ƤΤ���ǧ</U></B></CENTER>         
<BLOCKQUOTE>���β��̤ϡ�����ʸ���Ƥ򤴳�ǧĺ������Τ�ΤǤ������Ƥ˸�꤬������ϡ��֥饦���Ρ����ץܥ���򲡤��Ǝ����ϥե����������齤�����Ʋ�����������ǵ�������С���ʸ�ץܥ���򲡤��Ʋ�������</BLOCKQUOTE>
<CENTER><B>����ʸ����</B><BR></CENTER>
<HR>
���ʤ��Τ�̾���ʤ������͡�<BR>
\$name<BR>
�᡼�륢�ɥ쥹<BR>
\$email<BR>
���������Ļ�(��)<BR>
\$familyname<BR>
���л�ͽ����<BR>
\$brthday<BR>
�����Ѳ��<BR>
\$user<BR>
�����ФΤ�̾��<BR>
\$brother<BR>
����˾����<BR>
\$request<BR>
��̤Τ�Ϣ����ˡ<BR>
\$method<BR>
�ե��å����ֹ�<BR>
\$fax<BR>
�ѥ������E�᡼�륢�ɥ쥹<BR>
\$email2<BR>
<HR>
<BLOCKQUOTE><B>����ǧ���Ѥߤޤ�����</B><FONT COLOR="#FF0000"><B>��������ʸ���ܥ����1����������Ƥ�ȯ��</B></FONT><B>����������<BR>
�ʤ������ʤ����ʾ塢����ʹߤΤ���ʸ�μ��ä������ʤϰ��ڽ���ޤ���Τ�ͽ�ᤴλ����������(ˬ������ˡ�Υ�����󥰥��դ�Ŭ�Ѥ���ޤ��󡣡�</B></BLOCKQUOTE>         
����ʸ�������ϡ��֥饦���Ύ���뎣�ǎ����ϥե�������������ľ���Ʋ�������        
         <P><FORM ACTION="/~kazu-y/cgi_bin2/in-order.cgi" METHOD=POST>
            <P><INPUT TYPE="hidden" NAME="name" VALUE="\$name">
            <INPUT TYPE="hidden" NAME="email" VALUE="\$email">
            <INPUT TYPE="hidden" NAME="order2" VALUE="">
            <INPUT TYPE="hidden" NAME="order3" VALUE="\$order3">
            <INPUT TYPE="hidden" NAME="zipcord" VALUE="">
            <INPUT TYPE="hidden" NAME="address" VALUE="">
            <INPUT TYPE="hidden" NAME="tel" VALUE="\$tel">
            <INPUT TYPE="hidden" NAME="method" VALUE="\$method">
            <INPUT TYPE="hidden" NAME="email2" VALUE="\$email2">
            <INPUT TYPE="hidden" NAME="fax" VALUE="\$fax">
            <INPUT TYPE="hidden" NAME="fullname" VALUE="">
            <INPUT TYPE="hidden" NAME="familyname" VALUE="\$familyname">
            <INPUT TYPE="hidden" NAME="brthday" VALUE="\$brthday">
            <INPUT TYPE="hidden" NAME="user" VALUE="\$user">
            <INPUT TYPE="hidden" NAME="brother" VALUE="\$brother">
            <INPUT TYPE="hidden" NAME="request" VALUE="\$request">
            <INPUT TYPE="hidden" NAME="kgak" VALUE="10,000">
            <CENTER><INPUT TYPE=submit NAME="����" VALUE="��ʸ">
         </FORM></P>
</P>
</BODY>
</HTML>
ORDER003
&jcode'convert(*msg, "sjis", "euc");
	$msg =~ s/\$name/$name/g;
	$msg =~ s/\$email/$email/g;	
	$msg =~ s/\$order3/$order3/g;
	$msg =~ s/\$tel/$tel/g;
	$msg =~ s/\$method/$method/g;
	$msg =~ s/\$email2/$email2/g;
	$msg =~ s/\$fax/$fax/g;	
	$msg =~ s/\$familyname/$familyname/g;
	$msg =~ s/\$brthday/$brthday/g;
	$msg =~ s/\$user/$user/g;
	$msg =~ s/\$brother/$brother/g;
	$msg =~ s/\$request/$request/g;
	print $msg;
}
__end__
