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
Subject: Ƚ�����ʤ�����(i-geti2)

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
print "<html>\n";
print "<head>\n";
#������URL�ϡ����ʤ��Υ��ݥСݤˤ��碌�Ʋ�������
print "<META HTTP-EQUIV=\"Refresh\" CONTENT=\"5;URL=/~kazu-y/g-input.html\">\n";
#print "<META HTTP-EQUIV=\"Refresh\" CONTENT=\"5;URL=http://ppd.sf.nara.sharp.co.jp/~nakamura/test/seimei2/public_html/input.html\">\n";
print "<title>������λ</title></head>\n";
print "<body bgcolor=\"ffffff\" TEXT=\"000000\" link=\"fb02ee\" vlink=\"fb02ee\">\n";
print "<p>\n";
print "<br>\n";
print "<br>\n";
print "<center>\n";
print "<font size=\"6\" color=\"000000\"><b>�����Ϥ��꤬�Ȥ��������ޤ�����</b></font><br>\n";
print "</center>\n";
print "</body>\n";
print "</html>\n";
