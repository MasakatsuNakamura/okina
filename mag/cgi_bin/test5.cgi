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
#####3��ʾ�ְ㤨�����ɤ��������å�#####
if ($mis >= 3) {
	# 3��ʾ�ְ㤨��ȡ����ʤΥ�å�������Ф���
	$msg = <<"EOK";
Content-type: text/html

<HTML>
<HEAD>
   <TITLE>�������</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=SHIFT_JIS">
</HEAD>
<BODY BGCOLOR="#FFFFFF">
<P>
<HR>
<FONT COLOR="#FF0000">���������פ��ޤ���</FONT><BR>
<HR>
  3��ְ㤨�ޤ����Τǡ�����ʾ塢��������Ǥ������ˤ�ã���ޤ��󡣤ޤ����󡢹ֵ��򤪼����ˤʤꡢ�����󥸤��ƤߤƲ�������Ĺ���֡����դ��礤ĺ������ͭ���񤦤������ޤ�����<BR>
��<BR>
<HR>
<A HREF="http://www2.mahoroba.ne.jp/~kazu-y/i-mode.html" accesskey=1>1�����Υۡ���ڡ�����</A><BR>
</P>
</BODY>
</HTML>
EOK
	&jcode'convert(*msg, "sjis", "euc");
	print $msg;
} else {
	# ���������ɽ��
	$msg = <<"EOM";
Content-type: text/html

<HTML>
<HEAD>
   <TITLE>��5��</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=SHIFT_JIS">
</HEAD>
<BODY BGCOLOR="#FFFFFF" TEXT="#000000" LINK="#0000FF">
<P>
<HR>
��5��<BR>
<HR>
�����˴ؤ�������ʸ���椫����������Τ�������ǲ���������­�����������Ǹ���������Ȥ�����������������Ȥ��줿�������������Ȥϸ��߹�������Ū�˻Ȥ��Ƥ������Ѵ�������Ѵ���������ʤɤ�ؤ��ޤ�������ʳ������ְ��̤����Ѥ��Ƥ�������Τ�������������������Ʊ����̣����Ĥ�Τ�¸�ߤ�����������ƻ���¯���ȸ����ޤ���</P>
<P><FORM ACTION="$cgipath/test6.cgi" METHOD=POST>
   <P><INPUT TYPE=radio NAME=ans VALUE=1 CHECKED>���ƻ���¯�����������Ǥ��äƤ⡢���Ҥ���Ͽ���줿������ͥ�褹��Τǡ�ɬ������������Ƚ�ꤹ��ɬ�פϤʤ���<BR>
   <INPUT TYPE=radio NAME=ans VALUE=2>�����μ������鷺��������Ѥ��Ƥ����Τ��褺��Ƚ�ꤷ�����˵������Ƚ�ꤷ�ơ�2�Ĥ���Ӥ��ʤ������Ū�˴������Ƥ�Ƚ�Ǥ��롣<BR>
   <INPUT TYPE=radio NAME=ans VALUE=3>�ɤΤ褦�ʴ����Ǥ��졢�������������ˤϡ����β����Ŭ�Ѥ��롣���ƻ���¯���������β���ʵ����������ˤϤ���ˤ�Ŭ�Ѥ��롣<BR>
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
}
__end__
