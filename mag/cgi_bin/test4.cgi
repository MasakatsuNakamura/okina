#!/usr/local/bin/perl
$|=1;
require "jcode.pl";
require "cgi-lib.pl";

$root = "/~kazu-y/mag";
$cgipath = "/~kazu-y/mag/cgi_bin";
$baseurl = "http://www2.mahoroba.ne.jp";

##### CGI�ѿ���ꤳ��####
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
   <TITLE>��4��</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=SHIFT_JIS">
</HEAD>
<BODY BGCOLOR="#FFFFFF" TEXT="#000000" LINK="#0000FF">
<P>
<HR>
��4��<BR>
<HR>
��ʸ��������Ω�������פ˴ؤ�������ʸ���椫��ְ�äƤ����Τ�������ǲ�������</P>
<P><FORM ACTION="$cgipath/test5.cgi" METHOD=POST>
   <P><INPUT TYPE=radio NAME=ans VALUE=1 CHECKED>���󤺤��ؤ��<IMG SRC="$root/p19-2.gif" WIDTH=47 HEIGHT=45 ALIGN=bottom>�ΰ�̣��4��˼�롣�������10��Ǥ���11��˼�롣<BR>
   <INPUT TYPE=radio NAME=ans VALUE=2>�����ؤ��<IMG SRC="$root/p19-12.gif" WIDTH=47 HEIGHT=46 ALIGN=bottom>�ΰ�̣��6��˼�롣͵��12��˼��פ��Ǥ���13��Ǥ���<BR>
   <INPUT TYPE=radio NAME=ans VALUE=3>�����������<IMG SRC="$root/p20-8.gif" WIDTH=47 HEIGHT=47 ALIGN=bottom>�ΰ�̣��6��˼�롣�ɤϤ���������ˤ��餺���̤�13��Ǥ���<BR>
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
