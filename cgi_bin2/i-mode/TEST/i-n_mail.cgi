#!/usr/local/bin/perl
$|=1;
#############################
$sendmail = "/usr/lib/sendmail";
$youraddress = 'kazu-y@mahoroba.ne.jp ';
#############################
require "cgi-lib.pl";
require "jcode.pl";
require "zenhan.pl";
&ReadParse;
#############################
$kanji = $in{'kanji'};
$name2 = $in{'name2'};
$email2 = $in{'email2'};

#####�ǡ�������������#####
if ($email2 ne "") {
	$email2 =~ s/\s*//g;
	#���ѱѿ����򤹤٤�Ⱦ�ѱѿ����ˤ��롣
	$email2 = &zen2han($email2);
} 

#####���������ɤ�����#####
$kanjicode = $kanji;
$kanjicode =~ s/ //g;
$kanjicode =~ s/(.)/sprintf("%02X",unpack("c",$1) >= 0 ? unpack("c",$1)
: 256 + unpack("c",$1))/eg;
$kanjicode =~ s/(....)/$1 /g;

#####��ʸ�᡼�������#####
$com = <<"MESSAGE";
From: $email2
Subject: Ƚ�����ʤ�����(i�⡼��2)

=====================================
����Ǥ��ʤ�����������(SJIS)��
$kanjicode
Ϣ��ͤ�E�᡼�륢�ɥ쥹��
$email2
Ϣ��ͤλ�̾(����)��
$name2
���顼����(����)��
$kanji
���͡����顼��ȯ�������ǽ�����⤤��
=====================================
MESSAGE

&jcode'convert(*com,"jis");
open(MAIL, "|$sendmail $youraddress");
print MAIL $com;
close(MAIL);

print "Content-type: text/html\n\n";
print "<HTML>\n";
print "<HEAD>\n";
print "<TITLE>���顼������λ</TITLE>\n";
print "<META HTTP-EQUIV=\"Content-Type\" CONTENT=\"text/html;CHARSET=SHIFT_JIS\">\n";
print "</HEAD>\n";
print "<BODY BGCOLOR=\"#FFFFFF\" TEXT=\"#000000\" LINK=\"#0000FF\">\n";
print "<P>\n";
print "<BR>\n";
print "<BR>\n";
print "<FONT COLOR=\"#FF0000\"><B>�����Ϥ��꤬�Ȥ��������ޤ�����</B></FONT><BR>\n";
print "<A HREF=\"/~kazu-y/i-mode.html\" accesskey=1>1���⤦���ٴ��ꤹ�롣</A><BR>\n";
print "</BODY>\n";
print "</HTML>\n";
