#!/usr/local/bin/perl
#��Υѥ��ϡ����ʤ��Υ��ݥСݤˤ��碌�Ʋ�������
####################################################################
#N_Mail CGI
#Copyright 1992/1997                 K.Yamano 
#Scripts Archive at��          
#CGI�����䡢ž�ܡ����ۡ�̵�����Ѹ��ء�
####################################################################
#���ʤ��Υ��ݥСݤ�sendmail�Υѥ��ˤ��碌�롣
$sendmail = "/usr/lib/sendmail";
#���ʤ���Mail���ɥ쥹������
$youraddress = 'kazu-y@mahoroba.ne.jp ';
#$youraddress = 'nakamura@ppd.sf.nara.sharp.co.jp ';
#####################################################################
require "cgi-lib.pl";
require "jcode.pl";
&ReadParse;

###############�����ι��ܤϡ�̵���¤��ɲý���ޤ���#################
$kanji = $in{'kanji'};
$name2 = $in{'name2'};
$email2 = $in{'email2'};


####�����ν��ꡢ��̾��TEL��FAX�ϡ���ι��ܤˤ��碌���ɲä��롣######
####�㤨�С����̾���ɲäξ��ϡ����̾��$kaisya �ȵ�����
####$kaisya�ϡ�ɬ����ݥ޻����ݥɤ��Ǥ����ࡣ
$kanjicode = $kanji;
$kanjicode =~ s/ //g;
$kanjicode =~ s/(.)/sprintf("%02X",unpack("c",$1) >= 0 ? unpack("c",$1)
: 256 + unpack("c",$1))/eg;
$kanjicode =~ s/(....)/$1 /g;

$com = <<MESSAGE;
From: $email2
Subject: Ƚ�����ʤ�����(�����)

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
#&jcode'convert(*com,"sjis","euc");
#$com =~ s/\$kanji/$kanji/;
#$com =~ s/\$name2/$name2/;
#$com =~ s/\$email2/$email2/;
#&jcode'convert(*com,"jis","sjis");
&jcode'convert(*com,"jis");
open(MAIL, "|$sendmail $youraddress");
print MAIL $com;
close(MAIL);
print "Content-type: text/html\n\n";
print "<html>\n";
print "<head>\n";
#������URL�ϡ����ʤ��Υ��ݥСݤˤ��碌�Ʋ�������
print "<META HTTP-EQUIV=\"Refresh\" CONTENT=\"5;URL=/~kazu-y/input3.html\">\n";
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
