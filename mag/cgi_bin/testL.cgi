#!/usr/local/bin/perl
$|=1;
require "jcode.pl";
require "cgi-lib.pl";

$root = "/~kazu-y/mag";
$cgipath = "/~kazu-y/mag/cgi_bin";
$baseurl = "http://www2.mahoroba.ne.jp";

#####CGI�ѿ���ꤳ��#####
&ReadParse();
$ans = $in{'ans'};
$mis = $in{'mis'};
$name = $in{'name'};
$email = $in{'email'};
#####����γ�ǧ#####
if ($ans ne "3") {
    $mis = $mis + 1;
    #����Ǥʤ���硢mis������Ȥ�1��û�
}
$tokuten = (10 - $mis)*10;
    #�����η׻�
#####3��ʾ�ְ㤨�����ɤ��������å�#####
if ($mis >= 3) {
    # 3��ʾ�ְ㤨��ȡ����ʤΥ�å�������Ф���
	$msg = <<"EOK";
Content-type: text/html

<HTML>
<HEAD>
   <TITLE>�Թ��</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=SHIFT_JIS">
</HEAD>
<BODY BGCOLOR="#FFFFFF">
<P>
<HR>
<FONT COLOR="#FF0000">��ǰ�Ǥ�����</FONT><BR>
<HR>
  3��ְ㤨�ޤ����Τǡ�70���Ȥʤ������ˤ�ã���ޤ��󡣤���~���Ǥ����ޤ����󡢹ֵ��򤪼����ˤʤꡢ�����󥸤��ƤߤƲ�������Ĺ���֡����դ��礤ĺ������ͭ���񤦤������ޤ�����<BR>
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
   #����ֹ������
   $countfile = "count.txt";
   open COUNTER,"$countfile"
    or &CgiError("$countfile �����ץ���1\n");
   $GONO = <COUNTER>;
   close COUNTER;
   ++$GONO;
   open COUNTER,">$countfile"
    or &CgiError("$countfile �����ץ���2\n");
   print COUNTER $GONO;
   close COUNTER;
    # ���ʸ�Ϥ�ɽ��
   $msg = <<"EOM";
Content-type: text/html

<HTML>
<HEAD>
   <TITLE>����ǤȤ�</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=SHIFT_JIS">
</HEAD>
<BODY BGCOLOR="#FFFFFF">
<P>
<HR>
�������<BR>
<HR>
  ����줵�ޤǤ��������̵����λ�פ��ޤ�����<BR>
�����������ϡ�\$tokuten���Ǥ���<BR>
�����ϡ��̻�\$GONO���ܤι�ʼԤǤ���<BR>
(��ǯ�٤�18̾�ι�ʼԤ�����ޤ�����)</P>
<P><FORM ACTION="$cgipath/n_mail.cgi" METHOD=POST>
   <P><INPUT TYPE=hidden NAME=name VALUE="\$name" size=10 maxlength=10>
   <INPUT TYPE=hidden NAME=email VALUE="\$email" size=10 maxlength=50>
   <INPUT TYPE=hidden NAME=tokuten VALUE="\$tokuten" size=10 maxlength=3><INPUT TYPE=hidden NAME=GONO VALUE="\$GONO" size=10 maxlength=5>
   <INPUT TYPE=submit NAME="����" VALUE="��������"><BR>

</FORM>

<HR>

</P>
</BODY>
</HTML>
EOM
	&jcode'convert(*msg, "sjis", "euc");
	$msg =~ s/\$name/$name/g;
	$msg =~ s/\$email/$email/g;
	$msg =~ s/\$tokuten/$tokuten/g;
	$msg =~ s/\$GONO/$GONO/g;
	print $msg;
}
__END__
