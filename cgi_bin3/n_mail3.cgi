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
require "zenhan.pl";
&ReadParse;

###############�����ι��ܤϡ�̵���¤��ɲý���ޤ���
#################
$email = $in{'email'};
$name = $in{'name'};
$tel = $in{'tel'};
$adress = $in{'adress'};
$price = $in{'price'};
$order = $in{'order'};
######���ϥǡ�������������######
if ($tel ne "") {
	$tel =~ s/\s*//g;
	#���ѱѿ����򤹤٤�Ⱦ�ѱѿ����ˤ��롣
	$tel = &zen2han($tel); 
}
if ($email ne "") {
	$email =~ s/\s*//g;
	#���ѱѿ����򤹤٤�Ⱦ�ѱѿ����ˤ��롣
	$email = &zen2han($email);
} 
#####���ϥ��顼�Υ����å�#####
if ($email =~ /^\s*$/){
	&CgiError("�᡼�륢�ɥ쥹�ε���������ޤ���",
	"�֥饦���Ύ�Back���ܥ������äƺ����Ϥ��Ƥ���������");
	exit;
}
elsif (($email) and (not $email =~ /.+\@.+\..+/)) {
	&CgiError("���ϥ��顼",
		"�᡼�륢�ɥ쥹�ν������ְ�äƤ��ޤ���",$email,
		"�֥饦���Ύ�Back���ܥ������äƺ����Ϥ��Ƥ���������");
	exit;
}
if ($name eq ""){
	&CgiError("̾���ε���������ޤ���",
	"�֥饦���Ύ�Back���ܥ������äƺ����Ϥ��Ƥ���������");
	exit;
}
if ($adress eq "") {
    &CgiError("���꤬���Ϥ���Ƥ��ޤ���",
    "�֥饦���Ύ�Back���ܥ������äƺ����Ϥ��Ƥ���������");
    exit;
}	
if ($tel eq "") {
	&CgiError("�����ֹ椬���Ϥ���Ƥ��ޤ���",
	"�֥饦���Ύ�Back���ܥ������äƺ����Ϥ��Ƥ���������");
	exit;
}
#####��ʸ�᡼�������#####
$com = <<MESSAGE;
From: $email
Subject: ʪ��Τ��䤤��碌

=====================================
��̾����
$name
�᡼�륢�ɥ쥹��
$email
�����ֹ桧
$tel
���ꡧ
$adress
��˾���ʡ�
$price
Ϣ����ࡧ
$order
=====================================
MESSAGE
#&jcode'convert(*com,"sjis","euc");
#$com =~ s/\$name/$name/;
#$com =~ s/\$email/$email/;
#$com =~ s/\$tel/$tel/;
#$com =~ s/\$adress/$adress/;
#$com =~ s/\$price/$price/;
#$com =~ s/\$order/$order/;
#&jcode'convert(*com,"jis","sjis");
&jcode'convert(*com,"jis");
open(MAIL, "|$sendmail $youraddress");
print MAIL $com;
close(MAIL);
print "Content-type: text/html\n\n";
print "<html>\n";
print "<head>\n";
#������URL�ϡ����ʤ��Υ��ݥСݤˤ��碌�Ʋ�������
print "<META HTTP-EQUIV=\"Refresh\" CONTENT=\"5;URL=http://www.sikasenbey.or.jp/haibara/haibara.htm\">\n";
#print "<META HTTP-EQUIV=\"Refresh\" CONTENT=\"5;URL=http://ppd.sf.nara.sharp.co.jp/~nakamura/test/seimei2/public_html/input.html\">\n";
print "<title>������λ</title></head>\n";
print "<body bgcolor=\"ffffff\" TEXT=\"000000\" link=\"fb02ee\" vlink=\"fb02ee\">\n";
print "<p>\n";
print "<br>\n";
print "<br>\n";
print "<center>\n";
print "<font size=\"6\" color=\"000000\"><b>�����������餫�餴Ϣ�����夲�ޤ���</b></font><br>\n";
print "</center>\n";
print "</body>\n";
print "</html>\n";
