#!/usr/local/bin/perl
$|=1;
require "jcode.pl";
require "cgi-lib.pl";

$root = "/~kazu-y/mag";
$cgipath = "/~kazu-y/mag/cgi_bin";
$baseurl = "http://www2.mahoroba.ne.jp";

##### CGI�ѿ���ꤳ��#####
&ReadParse();
$ans = $in{'ans'};
$mis = $in{'mis'};
$name = $in{'name'};
$email = $in{'email'};
#####����γ�ǧ#####
if ($ans ne "1") {
    $mis = $mis + 1;
    #����Ǥʤ���硢mis������Ȥ�1��û�
}
#####��2��ν���#####
$msg = <<"EOM";
Content-type: text/html

<HTML>
<HEAD>
   <TITLE>��2��</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=SHIFT_JIS">
</HEAD>
<BODY BGCOLOR="#FFFFFF" TEXT="#000000" LINK="#0000FF">
<P>
<HR>
��2��<BR>
<HR>
  ���οޤϡֵ���פ������̾Ƚ�Ǥ�Ԥ�����Ǥ��롣<IMG SRC="$root/test2.gif" WIDTH=94 HEIGHT=189 ALIGN=bottom>    �ּ�פΰ�ʸ��̾�˴ؤ������׻�������ʸ���椫����������Τ�������ǲ�������</P>
<P><FORM ACTION="$cgipath/test3.cgi" METHOD=POST>
   <P><INPUT TYPE=radio NAME=ans VALUE=1 CHECKED>�ϲ��6�衢�����7�衢����15��Ǥ��롣<BR>
   <INPUT TYPE=radio NAME=ans VALUE=2>�ϲ��7�衢�����7�衢����15��Ǥ��롣<BR>
   <INPUT TYPE=radio NAME=ans VALUE=3>�ϲ��7�衢�����7�衢����16��Ǥ��롣<BR>
   <INPUT TYPE=hidden NAME=mis VALUE="\$mis" size=10 maxlength=1>
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
	$msg =~ s/\$ans/$ans/g;
	$msg =~ s/\$mis/$mis/g;
	$msg =~ s/\$name/$name/g;
	$msg =~ s/\$email/$email/g;
print $msg;
__end__
