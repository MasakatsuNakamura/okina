#!/usr/local/bin/perl
#�������perl�Υѥ����ǧ���Ƥ���������

use Socket;

require "./dclick_perl.pl";
#use dclick_perl;

#dclick SSI �б�
#�������

#��ա�ɬ�������Ȥι���ID���ѹ����Ƥ���������
$id = "B00369";

#ɽ��������������������Ϥ��Ƥ�������(1��3)
$number = 1;

#ɽ����������html����˰ʲ��Υ��ޥ�ɤ��������Ƥ���������
#<!--#exec cgi="./dclick_ssi.cgi"-->
#�⤷���� <!--#include file="./dclick_ssi.cgi"-->

#�������ID,�������
@banner=&dclick_perl'dclick($id,$number);

print "Content-type: text/html\n\n";
for($i = 0;$i < $number;$i++){
	print "$banner[$i]<br>";
}