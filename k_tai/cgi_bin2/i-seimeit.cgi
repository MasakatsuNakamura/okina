#!/usr/local/bin/perl
$|=1;
require "jcode.pl";
require "cgi-lib.pl";
require "kakusu.pl";
require "reii.pl";
require "seikaku.pl";
require "kenkou.pl";

#û�̥ѥ����
#�ǥ��쥯�ȥ�.~kazu-y/k_tai�Υ��������ϡ�http://k-tai.net/acg.asp����Τߵ���
$root = 'http://k-tai.net/acg.asp?U=http://www2.mahoroba.ne.jp/~kazu-y/k_tai';
$cgipath = 'http://k-tai.net/acg.asp';
$baseurl = 'http://www2.mahoroba.ne.jp/~kazu-y/k_tai';

# CGI�ѿ���ꤳ��
&ReadParse();
$sei = $in{'sei'};
$mei = $in{'mei'};
$sex = $in{'sex'};
$marry = $in{'marry'};

$seimei = $sei.$mei;
$incode = &jcode'getcode(*seimei);
if ($incode ne "sjis") {
&jcode'convert(*sei, "sjis", $incode);
&jcode'convert(*mei, "sjis", $incode);
}

$sei =~ s/\s//g;
$mei =~ s/\s//g;

$sei =~ s/\x81\x40//g;
$mei =~ s/\x81\x40//g;

#��̾�����Ϥ��ʤ����ϡ����ϲ��̤����
if ($sei eq "" || $mei eq "") {
	print "Location: $root/i-mode2.shtml\n\n";
	exit;
}

$sei1 = $sei;
$mei1 = $mei;

# ���ν���
$sei1 =~ s/(..)\x81\x58/$1$1/;
$mei1 =~ s/(..)\x81\x58/$1$1/;

# ���ν���
$sei1 =~ s/(..)\x81\x54/$1$1/;
$mei1 =~ s/(..)\x81\x54/$1$1/;

# ���ν���
$sei1 =~ s/(..)\x81\x57/$1$1/;
$mei1 =~ s/(..)\x81\x57/$1$1/;

# ŷ�衦�Ͳ衦�ϲ衦���衦���λ���(�빽��䤳����)
$kakusu{'tenkaku'} = 0;
$kakusu{'chikaku'} = 0;
$kakusu{'gaikaku'} = 0;
$kakusu{'soukaku'} = 0;
@error = ();

# ŷ��λ���
for ($i = 0; $i<length($sei1); $i+=2) {
	$kanji = substr($sei1, $i, 2);
	$kakusu = &kakusu($kanji);
	if ($kakusu == 0) {
		push (@error, $kanji);
	}
	$kakusu{'tenkaku'} += $kakusu;
}

# ��ʸ�����ν���
if (length($sei1) == 2) {
	$kakusu{'tenkaku'}++; # ���ڤ��
	$kakusu{'gaikaku'}++;
	$kakusu{'soukaku'}--; # ����֤�
}

# �Ͳ�λ���
$kakusu{'jinkaku'} = &kakusu(substr($sei1, length($sei1)-2, 2)) + &kakusu(substr($mei1, 0, 2));

# �ϲ�λ���
for ($i = 0; $i<length($mei1); $i+=2) {
	$kanji = substr($mei1, $i, 2);
	$kakusu = &kakusu($kanji);
	if ($kakusu == 0) {
		push (@error, $kanji);
	}
	$kakusu{'chikaku'} += $kakusu;
}

# ��ʸ��̾�ν���
if (length($mei1) == 2) {
	$kakusu{'chikaku'}++; # ���ڤ��
	$kakusu{'gaikaku'}++;
	$kakusu{'soukaku'}--; # ����֤�
}

# ��衦����λ���
$kakusu{'soukaku'} += $kakusu{'tenkaku'} + $kakusu{'chikaku'};
$kakusu{'gaikaku'} += $kakusu{'soukaku'} - $kakusu{'jinkaku'};

# �����С��ե����� - ���ʤߤ� > 81�ϴְ㤤�ǤϤʤ���
foreach (keys %kakusu) {
	$kakusu{$_} %= 80 if ($kakusu{$_} > 81);
}

# ŷ�衦�Ͳ衦�ϲ�β����λ���(10�ǳ�ä�;��������)
$tenshimo = $kakusu{'tenkaku'} % 10;
$jinshimo = $kakusu{'jinkaku'} % 10;
$chishimo = $kakusu{'chikaku'} % 10;

# ���ʿ��Ǥν���
$kakusu{'seikaku'} = $jinshimo;

# ���۸޹ԤΥ��ꥢ���ֹ�λ���(�ܤ�����kenkou.pl�򻲾�)
$kakusu{'kenkou'} = &f($tenshimo)*25 + &f($jinshimo) *5 + &f($chishimo);

# �ꤤ��̤���������
foreach (keys %kakusu) {
	if ($_ eq "kenkou") {
		$res{$_} = $kenkou[$kakusu{$_}];
	} elsif ($_ eq "seikaku") {
		$res{$_} = $seikaku[$kakusu{$_}];
	} else {
		$res{$_} = $reii[$kakusu{$_}];
	}
	$res{$_} =~ s/\+n/<BR>/g;
	$res{$_} =~ s/\+w.*-w//g if ($sex ne "female");
	$res{$_} =~ s/\+m.*-m//g if ($sex ne "male");
	$res{$_} =~ s/\+k.*-k//g if ($marry ne "yes");
	$res{$_} =~ s/\+u.*-u//g if ($marry ne "no");
	$res{$_} =~ s/\+j.*-j//g if ($_ ne "jinkaku");
	$res{$_} =~ s/\+s.*-s//g if ($_ ne "soukaku");
	$res{$_} =~ s/\+o.*-o//g if ($_ ne "gaikaku");
	$res{$_} =~ s/\+e.*-e//g if ($kakusu{'chikaku'} != 11);
	$res{$_} =~ s/\+t.*-t//g if ($kakusu{'jinkaku'} != 26);
	$res{$_} =~ s/\+g.*-g//g if ($kakusu{'jinkaku'} != 10 && $kakusu{'jinkaku'} != 20);
	$res{$_} =~ s/[\-\+][a-z]//g;
	$res{$_} =~ s/<BR>$//g;
}

#�ʲ����HTMLʸɽ��
if ($#error >= 0) {
	# ���顼��������ʸ���Ǥ⤢��Х��顼ɽ��
	$msg = <<"EOK";
Content-type: text/html
<HTML>
<HEAD>
   <TITLE>���顼��å�����</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=SHIFT_JIS">
</HEAD>
<BODY BGCOLOR="#FFFFFF" TEXT="#000000" LINK="#0000FF">
<P>
<HR>

<FONT COLOR="#FF0000">���Ϥ��줿������\$error����Ƚ�̤Ǥ��ޤ���</FONT><BR>

<HR>
���˶�������ޤ����������������ե�����򤴳�ǧ�塢���������ܥ���򲡤��Ʋ�������<BR>
���Τʲ��Ƚ���Ԥ����ģ¤�������������Υ᡼�륢�ɥ쥹�ޤ�Ϣ�����夲�ޤ���</P>

<P><FORM ACTION="$baseurl/cgi_bin2/i-n_mailt.cgi" METHOD=POST>
   <P>���顼�ˤʤä�������<INPUT TYPE=hidden NAME=kanji VALUE="\$error" size=10 maxlength=10>\$error<BR>
   ���ʤ��ͤΤ�̾����<INPUT TYPE=text NAME=name2 VALUE="\$seimei" ISTYLE="1" SIZE=10 MAXLENGTH=10><BR>
   �᡼�륢�ɥ쥹��<INPUT TYPE=text NAME=email2 VALUE="" ISTYLE="3" SIZE=16 MAXLENGTH=256><BR></P>
   <INPUT TYPE=submit NAME="����" VALUE="����"><BR>
   <INPUT TYPE=reset VALUE="���ä�">
</FORM></P>

<P>
<HR>
<A HREF="$baseurl/i-mode2t.shtml" accesskey=1>1���⤦���ٴ��ꤹ�롣</A><BR>
<A HREF="$baseurl/i-info.html" accesskey=3>3��������Τ��Τ餻���ɤࡣ</A><BR>
</P>

</BODY>
</HTML>
EOK
	&jcode'convert(*msg, "sjis", "euc");
	$msg =~ s/\$seimei/$sei $mei/g;
	$msg =~ s/\$error/@error/g;
	print $msg;
} else {
	# Ƚ����ɽ��
	$msg = <<"EOM";
Content-type: text/html
<HTML>
<HEAD>
   <TITLE>���ܲ��δ�����(1/6)</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=SHIFT_JIS">
</HEAD>
<BODY BGCOLOR="#FFFFFF" TEXT="#000000" LINK="#0000FF">
<P>
<HR>

\$seimei����ؤν���(1/6)<BR>

<HR>
<FONT COLOR="#FF0000"><U>�籿</U>
�����ͤΰ������濴��ʤ�ޤ����뺧�ˤ�������Ѥ��ȼ籿���Ѥ��ޤ��������ξ�����ǯ�ʹߤ˶�������ޤ����ޤ����㤤���ϵ��������Ϥ��ƤߤƲ�������</FONT></P>

<P>$kakusu{'jinkaku'}�衧$res{'jinkaku'}</P>

<P><FORM ACTION="$baseurl/cgi_bin2/i2seimeit.cgi" METHOD=POST>
   <P><INPUT TYPE=hidden NAME=sei VALUE="\$sei" size=10 maxlength=10>
   <INPUT TYPE=hidden NAME=mei VALUE="\$mei" size=10 maxlength=10>
   <INPUT TYPE=hidden NAME=sex VALUE="\$sex" size=10 maxlength=10>
   <INPUT TYPE=hidden NAME=marry VALUE="\$marry" size=10 maxlength=10></P>
   <INPUT TYPE=submit NAME="����" VALUE="�п͡��Ҹ򱿤�"><BR>
</FORM></P>

<P>
<HR>
<A HREF="$baseurl/i-mode2t.shtml" accesskey=1>1���������ľ����</A><BR>
</P>
</BODY>
</HTML>
EOM
	&jcode'convert(*msg, "sjis", "euc");
	$msg =~ s/\$seimei/$sei $mei/g;
	$msg =~ s/\$sei/$sei/g;
	$msg =~ s/\$mei/$mei/g;
	$msg =~ s/\$sex/$sex/g;
	$msg =~ s/\$marry/$marry/g;
	print $msg;
}
_END_