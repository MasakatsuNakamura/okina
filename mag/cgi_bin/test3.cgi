#!/usr/local/bin/perl
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
if ($ans ne "2") {
    $mis = $mis + 1;
    #����Ǥʤ���硢mis������Ȥ�1��û�
}
#####��3��ν���#####
$msg = <<"EOM";
Content-type: text/html

<HTML>
<HEAD>
   <TITLE>��3��</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=SHIFT_JIS">
</HEAD>
<BODY BGCOLOR="#FFFFFF" TEXT="#000000" LINK="#0000FF">
<P>
<HR>
��3��<BR>
<HR>
<IMG SRC="$root/test3.gif" WIDTH=94 HEIGHT=99 ALIGN=bottom>�ϡֱ��۸޹Ԥ�ˡ§�פ˴ؤ���ޤǤ��롣��������ʸ���椫��ְ�äƤ����Τ�������ǲ�������</P>
<P><FORM ACTION="$cgipath/test4.cgi" METHOD=POST>
   <P><INPUT TYPE=radio NAME=ans VALUE=1 CHECKED>1��2�ϡ��ڡס�3��4�ϡֲСס�5��6�ϡ��ڡס�7��8�ϡֶ�ס�9��10�ϡֿ�פ�ɽ���������ϱ���������ۤǤ��롣<BR>
   <INPUT TYPE=radio NAME=ans VALUE=2>�����Ƿ�Ф�Ƥ��뱢������ξ��ϡ����Ū�夯���Ѥ��ޤ�����ľ���Ƿ�Ф�Ƥ��뱢������ξ��Ϥ��κ��Ѥ��Ǥ⶯������뤫����դ�ɬ�פǤ��롣<BR>
   <INPUT TYPE=radio NAME=ans VALUE=3>ŷ�衢�Ͳ衢�ϲ�α��۸޹Ԥ�����򻰺ͤ����֤ȸ�����̾�դ��ǤϺǤ���׻뤹�٤��ݥ���ȤǤ��롣<BR>
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