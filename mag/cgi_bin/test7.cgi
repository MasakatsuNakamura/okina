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
   <TITLE>��7��</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=SHIFT_JIS">
</HEAD>
<BODY BGCOLOR="#FFFFFF" TEXT="#000000" LINK="#0000FF">
<P>
<HR>
��7��<BR>
<HR>
���Ρֿ���(���)�Τ���ޤ���
�˴ؤ�������ʸ���椫��ְ�äƤ����Τ�������ǲ�������</P>
<P><FORM ACTION="$cgipath/test8.cgi" METHOD=POST>
   <P><INPUT TYPE=radio NAME=ans VALUE=1 CHECKED>5,6,11,13,15,24,31,32,41,45,47,48,52,63,65�ϡ��˽����˱��������ο��Ǥ��롣<BR>
   <INPUT TYPE=radio NAME=ans VALUE=2>9,10,19,20,28�ϡ��������Ρ��¼�ʤɤΰż���������Ǥ��롣<BR>
   <INPUT TYPE=radio NAME=ans VALUE=3>21,23,29,33,39�ϡ��˲����ο��Ǥ��롣<BR>
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
