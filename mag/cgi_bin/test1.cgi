#!/usr/local/bin/perl
$|=1;
require "jcode.pl";
require "cgi-lib.pl";
require "zenhan.pl";

$root = "/~kazu-y/mag";
$cgipath = "/~kazu-y/mag/cgi_bin";
$baseurl = "http://www2.mahoroba.ne.jp";

#####CGI�ѿ���ꤳ��#####
&ReadParse();
$name = $in{'name'};
$email = $in{'email'};

#####�᡼�륢�ɥ쥹������#####
if ($email ne "") {
	$email =~ s/\s*//g;
	#���ѱѿ����򤹤٤�Ⱦ�ѱѿ����ˤ��롣
	$email = &zen2han($email);
}
######���ϥ��顼�Υ����å�#####
$msg1 = "̾���ε���������ޤ���";
$msg2 = "�᡼�륢�ɥ쥹�ε���������ޤ���";
$msg3 = "�᡼�륢�ɥ쥹�ν������ְ�äƤ��ޤ���";
$msg4 = "�֥饦���Ύ�Back���ܥ������äƺ����Ϥ��Ƥ���������";
&jcode'convert(*msg1, 'sjis', 'euc');
&jcode'convert(*msg2, 'sjis', 'euc');
&jcode'convert(*msg3, 'sjis', 'euc');
&jcode'convert(*msg4, 'sjis', 'euc');

if ($name =~ /^\s*$/){
	&CgiError("$msg1",
	"$msg4");
	exit;
}
if ($email =~ /^\s*$/){
	&CgiError("$msg2",
	"$msg4");
	exit;
}
elsif (($email) and (not $email =~ /.+\@.+\..+/)) {
	&CgiError("$msg3",$email,
	"$msg4");
	exit;
}
#####��1��ν���#####
$msg = <<"EOM";
Content-type: text/html

<HTML>
<HEAD>
   <TITLE>��1��</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=SHIFT_JIS">
</HEAD>
<BODY BGCOLOR="#FFFFFF" TEXT="#000000" LINK="#0000FF">
<P>
<HR>
��1��<BR>
<HR>
  ���οޤ򸫤ơ�<IMG SRC="$root/test1.gif" WIDTH=94 HEIGHT=164 ALIGN=bottom>���ܼ���̾Ƚ�Ǥ˱�����޲�ʬ��˴ؤ�������ʸ���椫����������Τ�������ǲ�������</P>
<P><FORM ACTION="$cgipath/test2.cgi" METHOD=POST>
   <P><INPUT TYPE=radio NAME=ans VALUE=1 CHECKED>A��ŷ��ȸ�������������Τ�Τǵȶ��αƶ���ľ�ܤʤ������ۤ����󤪤�����˱��ơ��ܿͤ��������ȷ򹯱��򺸱����롣<BR>
   <INPUT TYPE=radio NAME=ans VALUE=2>D�ϳ���Ȥ������Ҹ򱿤Ȥ�ƤФ졢���ء���ͧ���θʤα�̿�ڤӼ��Ϥα�̿�򺸱����롣<BR>
   <INPUT TYPE=radio NAME=ans VALUE=3>E�������ȸ���������������Ĺ�������͸��ȯŸ���Ȥ������<BR>
   <INPUT TYPE=hidden NAME=mis VALUE=0 size=10 maxlength=1>
   <INPUT TYPE=hidden NAME=name VALUE="\$name" size=10 maxlength=10>
   <INPUT TYPE=hidden NAME=email VALUE="\$email" size=10 maxlength=50>
   <INPUT TYPE=submit NAME="����" VALUE="���������"><BR>
</FORM>
<HR>
</P>
</BODY>
</HTML>
EOM
	&jcode'convert(*msg, "sjis", "euc");
	$msg =~ s/\$name/$name/g;
	$msg =~ s/\$email/$email/g;
print $msg;
