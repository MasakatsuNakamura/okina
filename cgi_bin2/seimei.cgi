#!/usr/local/bin/perl
require "jcode.pl";
require "cgi-lib.pl";
require "kakusu.pl";
require "reii.pl";
require "seikaku.pl";
require "kenkou.pl";

# ��ҴĶ��ƥ�����
#$root = "/~nakamura/test/seimei2/public_html";
#$cgipath = "/~nakamura/test/seimei2/cgi_bin";
#$baseurl = "http://ppd.sf.nara.sharp.co.jp";

# ����Ķ���
$root = "/~kazu-y";
$cgipath = "/~kazu-y/cgi_bin2";
$baseurl = "http://www2.mahoroba.ne.jp";

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

if ($sei eq "" || $mei eq "") {
	print "Location: $baseurl$root/input.html\n\n";
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

# ��̾����
$kyoku = $jinshimo;
$kyoku = 10 if ($kyoku == 0);
$kyoku -= 1;
$kyoku -= $kyoku % 2;
$kyoku /= 2;
$kyoku++;

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

if ($#error >= 0) {
	# ���顼��������ʸ���Ǥ⤢��Х��顼ɽ��
	$msg = <<"EOK";
Content-type: text/html

<HTML>
<HEAD>
   <TITLE>���顼��å�����</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=x-sjis">
</HEAD>

<BODY BGCOLOR="#FFFFFF" BACKGROUND="$root/image/wall.jpg">
<P><HTML><HEAD><TITLE>���顼��å�����</TITLE></HEAD></P>

<P><TABLE BORDER=0 WIDTH=640>
   <TR>
      <TD>
         <CENTER><FONT SIZE="+3"><B>���Ϥ��줿���� ��\$error��
         ��Ƚ�̤Ǥ��ޤ���</B></FONT>
         
         <P>���˶�������ޤ�����<A HREF="#form" TARGET="_self"><B>�����Υե�����</B></A>�Τˤ������ξ塢�����ܥ���򲡤��Ƥ���������<BR>
         �����ǡ����١����ν�������λ���ޤ����顢������Υ᡼�륢�ɥ쥹�ޤǤ�Ϣ�����夲�ޤ����ޤ����������Ҥ餫�ʡ��������ʰʳ��α�ʸ������������ʸ��������ʤɤϻ��ܼ���̾Ƚ�ǤǤϰ��äƤ���ޤ���Τǡ�Ϣ������פǤ��������Ρ֤⤦���ٴ��ꤹ��פ򲡤��Ʋ�������</P></CENTER>
         
         <P>
         
         <HR>
         
         </P>
      </TD>
   </TR>
   <TR>
      <TD>
         <CENTER><FONT SIZE="+3"><B>������Τ��ͤ�</B></FONT></CENTER>
         
         <P><U>ʸ���β���ǡ����١����ˤĤ���</U></P>
         
         <P>���ߡ�̾�����Ѥ���������ϡ����Ѵ����ȿ�̾�����Ǥ�������ʳ��ˤ�ºݤ˻Ȥ��Ƥ�����̾�ˤϤ���˳������ʤ���Τ����Ĥ⤢��ޤ������ߡ��������椫��4580ʸ��(2003.9����)��ǡ����١�������Ͽ���Ƥ���ޤ��������ϡ����ܲ��δ�����50ǯ�ηи��˴�Ť���ΤǤ����������ʤ��顢�ޤ����Ƥ���Ͽ����Ƥ���Ȥϸ����񤯡��ޤ���Ͽϳ�줬�ʤ��Ȥ�¤�ޤ���</P>
         
         <P>����Ϥ������ä����ʥ������Ǥ���Ȼפ��ޤ������ˤ�����Ǥ����������Υե�����ˤ�����ĺ���ޤ����顢�������������̤�Ϣ�����Ƥ��������ޤ�������Υǡ����١�����ȿ�Ǥ�����ĺ�������ȹͤ��ޤ��Τǡ������ϵ��������ꤤ�����夲�ޤ���<BR>
         ���ꤤ����̤Τ��Τ餻��ɬ�פǤʤ����ϡ��᡼�륢�ɥ쥹�����Τޤ��������������ְ�ä����ɥ쥹��������ޤ���¾�����˸����Ǥ�������ޤ���</P>
         
         <CENTER><FORM ACTION="$cgipath/n_mail2.cgi" METHOD=POST>
            <BLOCKQUOTE><BLOCKQUOTE><CENTER><A NAME=form></A><TABLE BORDER=0 CELLSPACING=10 CELLPADDING=0>
                     <TR>
                        <TD>
                           <P ALIGN=right>���顼�ˤʤä�����</P>
                        </TD>
                        <TD>
                           <P><INPUT TYPE=hidden NAME=kanji VALUE="\$error" size=10 maxlength=10>\$error</P>
                        </TD>
                     </TR>
                     <TR>
                        <TD>
                           <P ALIGN=right>��̾��</P>
                        </TD>
                        <TD>
                           <P><INPUT TYPE=text NAME=name2 VALUE="\$seimei" SIZE=20 MAXLENGTH=10></P>
                        </TD>
                     </TR>
                     <TR>
                        <TD>
                           <P ALIGN=right>�᡼�륢�ɥ쥹</P>
                        </TD>
                        <TD>
                           <P><INPUT TYPE=text NAME=email2 VALUE="" SIZE=40></P>
                        </TD>
                     </TR>
                     <TR>
                        <TD>
                           <P></P>
                        </TD>
                        <TD>
                           <P><INPUT TYPE=submit NAME="����" VALUE="����"><INPUT TYPE=reset VALUE="���ä�"></P>
                        </TD>
                     </TR>
                  </TABLE>
                  </CENTER></BLOCKQUOTE></BLOCKQUOTE>
         </FORM>
         
         <P><FONT SIZE="+2">
         
         <HR>
         
         </FONT><A HREF="$root/input.html" TARGET="_self"><FONT SIZE="+1">�⤦���ٴ��ꤹ��</FONT></A></P></CENTER>
         
         <P>
         
         <HR>
         
         </P>
      </TD>
   </TR>
   <TR>
      <TD>
         <P><TABLE BORDER=0 WIDTH=640>
            <TR>
               <TD>
                  <CENTER><A HREF="$root/index.html" TARGET="_self">�ȥåץڡ���</A></CENTER>
               </TD>
               <TD>
                  <CENTER><A HREF="$root/book.html" TARGET="_self">����Υ����ʡ�</A></CENTER>
               </TD>
               <TD>
                  <CENTER><A HREF="$root/baby.html" TARGET="_self">̿̾�Υ����ʡ�</A></CENTER>
               </TD>
            </TR>
            <TR>
               <TD>
                  <CENTER><A HREF="$root/consul.html">�����̤Υ����ʡ�</A></CENTER>
               </TD>
               <TD>
                  <CENTER><A HREF="$root/info.html">������Τ��Τ餻</A></CENTER>
               </TD>
               <TD>
                  <CENTER><A HREF="$root/link.html">���ꤤľ���ء�</A></CENTER>
               </TD>
            </TR>
         </TABLE>
         
         <HR>
         
         </P>
      </TD>
   </TR>
   <TR>
      <TD>
         <CENTER>����
         <FONT SIZE="-2">��󥯤ϴ��ޤ��ޤ�����ɬ��</FONT><A HREF="$root/index.html" TARGET="_self"><FONT SIZE="-2"><I>TOP�ڡ���</I></FONT></A><FONT SIZE="-2">�ؤ��ꤤ���ޤ���<BR>
         ���Υ���ƥ�Ĥξ������Ѥʤ�Ӥ�̵��ž�ܤϤ��Ǥ��פ��ޤ���<BR>
         <I>CopyRight. K.Yamamoto.1998.9.1</I></FONT></CENTER>
      </TD>
   </TR>
</TABLE>
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
   <TITLE>���ܲ��δ�����</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=x-sjis">
</HEAD>

<BODY BGCOLOR="#FFFFFF" BACKGROUND="$root/image/wall.jpg" onload="scll()">
<P><SCRIPT LANGUAGE=JavaScript>var cnt = -2;//ʸ������
var speed = 500;//ư�������ԡ���(1/1000��ñ��)
var msg = "              Web�ǽ��ơ� �����̤ˤ�äƲ��ڤ�5�̤���Ѳ����ޤ�������κ������������ɤ���������ˡ�ˤĤ��Ƥϡ�����������������������̤���ܤ����Τꤿ��������̾���˾������������뺧��ͽ��Τ������ϡ�ͭ���Τ����̥����ʡ��Ⳬ�ߤ��Ƥ���ޤ��Τǡ������Ѳ��������ޤ����ѡ��ȥʡ���õ�������ϡ����Υڡ����ι���򤴻��Ȳ�������"; //��å���������
timeID=setTimeout('',1); //IE�к��ʤˤ⤷�ʤ�;�����ޡ����å�

//��ʸ�����ư������
function scll()
{
 status = msg.substring(cnt=cnt+2,msg.length+2);//���ܸ��2ʸ���Ť�ư����
 if (cnt>msg.length){cnt=-2};
 clearTimeout(timeID);//�����ޡ��򥯥ꥢ
 timeID = setTimeout('scll()',speed);
  }</SCRIPT></P>

<P><HTML><HEAD><TITLE>���ܲ��δ�����</TITLE></HEAD></P>

<CENTER><TABLE BORDER=0 CELLSPACING=0 WIDTH=640>
   <TR>
      <TD>
         <P><TABLE BORDER=0 CELLSPACING=0 CELLPADDING=0 WIDTH="100%">
            <TR>
               <TD VALIGN=top WIDTH=320 HEIGHT=240 BGCOLOR="#CCCC99">
                  <CENTER><FONT SIZE="+2" COLOR="#0033FF"><B><TABLE BORDER=0 CELLSPACING=0 CELLPADDING=0 WIDTH=320 HEIGHT=240>
                     <TR>
                        <TD VALIGN=bottom BACKGROUND="$root/image/result.jpg">
                           <CENTER><FONT SIZE="+2" COLOR="#9933FF"><B>\$seimei����ؤν���</B></FONT></CENTER>
                        </TD>
                     </TR>
                  </TABLE>
                   </B></FONT></CENTER>
               </TD>
               <TD VALIGN=top WIDTH=320 HEIGHT=240 BGCOLOR="#CCCC99">
                  <CENTER><B><U>���ܲ����</U></B></CENTER>
                  
                  <P>���籿���пͱ������ñ�����ǯ���Ȱ츫̷�⤹��褦�ʷ�̤򼨤����Ȥ⤢��ޤ�������Ͽʹ֤Ȥ�����Τϡ��������ܿ����㤦�Τ��Ǥ������������Ȥ���������Ȥ������Ȥǡ������̤ˤ⤽��ϸ���Ƥ��Ƥ���Ȥ����򲼤��������äơ��ޤ����������Τ�į���ĺ�������˸ġ�����ʬ�ˤĤ��Ƽ�ʬ�ʤ��ʬ�Ϥ���Ƥߤ�������ᤷ�ޤ����ʤ��������δ���Ȥ����Τϡ����ҤΤ褦�ʿͤ��줾��ζ�������δĶ������Ū�˲�̣����Ƚ�Ǥ���ΤǤ��������󥿡��ͥåȤǤϤ����ޤǤλ�������ޤ���Τǡ��������餺��λ����������</P>
               </TD>
            </TR>
         </TABLE>
         </P>
         
         <P><IMG SRC="$root/image/line_j.gif" WIDTH=640 HEIGHT=17 ALIGN=bottom></P>
         
         <P></P>
      </TD>
   </TR>
   <TR>
      <TD>
         <P><TABLE BORDER=3 CELLSPACING=10 WIDTH="100%">
            <TR>
               <TD VALIGN=top>
                  <P><FONT SIZE="+2" COLOR="#B30000"><B><U>�籿</U></B></FONT>
                  <FONT SIZE="-1" COLOR="#B30000">�����ͤΰ������濴��ʤ�ޤ����뺧�ˤ�������Ѥ��ȼ籿���Ѥ��ޤ�������ǯ�ʹߤ˶�������ޤ���</FONT></P>
                  
                  <BLOCKQUOTE>$kakusu{'jinkaku'}�衧$res{'jinkaku'}</BLOCKQUOTE>
                  
                  <P></P>
               </TD>
               <TD VALIGN=top>
                  <P><FONT SIZE="+2" COLOR="#1D00B3"><B><U>�пͱ����Ҹ�</U></B></FONT>
                  <FONT SIZE="-1" COLOR="#1D00B3">���пʹط����²�����شط���ͧã�ط��˸���Ƥ��ޤ���</FONT></P>
                  
                  <BLOCKQUOTE>$kakusu{'gaikaku'}�衧$res{'gaikaku'}</BLOCKQUOTE>
                  
                  <P></P>
               </TD>
            </TR>
            <TR>
               <TD VALIGN=top>
                  <P><FONT SIZE="+2" COLOR="#007F1F"><B><U>�򹯱�(��Ĵ������)</U></B></FONT>
                  <FONT SIZE="-1" COLOR="#007F1F">���㤨�ȿ�·������̾�Ǥ��äƤ⡢�򹯤˷äޤ�ʤ���г褫�����ޤ��󡣡ʢ���ñ�ȤǤ�Ƚ�Ǥ��񤷤���</FONT></P>
                  
                  <BLOCKQUOTE>$res{'kenkou'}</BLOCKQUOTE>
                  
                  <P></P>
               </TD>
               <TD VALIGN=top>
                  <P><FONT SIZE="+2" COLOR="#B35900"><B><U>����</U></B></FONT>
                  <FONT SIZE="-1" COLOR="#B35900">�����ͤγ���Ū�����ʤ򸽤��ޤ�����ʬ��¾�ͤ���ɤ������Ƥ���Τ����ͤˤʤ�ޤ���</FONT></P>
                  
                  <BLOCKQUOTE>$res{'seikaku'}</BLOCKQUOTE>
                  
                  <P></P>
               </TD>
            </TR>
            <TR>
               <TD VALIGN=top>
                  <P><FONT SIZE="+2" COLOR="#7F0260"><B><U>���ñ�</U></B></FONT>
                  <FONT SIZE="-1" COLOR="#7F0260">���ľ�ǯ���α����εȶ�����ۤ�����ǯ���ޤǺǤ⶯�����Ѥ��ޤ���(��ǯ�Ԥ�Ƚ�ǤϤ����餬ͭ��)</FONT></P>
                  
                  <BLOCKQUOTE>$kakusu{'chikaku'}�衧$res{'chikaku'}</BLOCKQUOTE>
                  
                  <P></P>
               </TD>
               <TD VALIGN=top>
                  <P><FONT SIZE="+2" COLOR="#B30068"><B><U>��ǯ��</U></B></FONT>
                  <FONT SIZE="-1" COLOR="#B30068">��50�����夫�鶯������Ƥ��ޤ������������籿�ȴ��ñ��˺�������ޤ��Τ���դ��Ʋ�������</FONT></P>
                  
                  <BLOCKQUOTE>$kakusu{'soukaku'}�衧$res{'soukaku'}</BLOCKQUOTE>
                  
                  <P></P>
               </TD>
            </TR>
         </TABLE>
         <BR>
         <IMG SRC="../../image/line_a1.gif" WIDTH=640 HEIGHT=3 ALIGN=bottom></P>
         
         <P>����̤�ǡ���Ǥ��礦���������ܲ��Ǥ��͡���<FONT COLOR="#FF0000">ͭ�������ӥ�</FONT>��»ܤ��Ƥ���ޤ��Τǡ��������Ф�����⤴���Ѳ��������ޤ�������Ū���ɤ�ʹ����뤴����ˤĤ���<A HREF="$root/info.html">�����Τ餻�����ʡ���</A>��Ż��Ƥ��ޤ��Τǡ�ʻ���Ƥ�����������</P>
         
         <CENTER><IMG SRC="$root/image/line_a2.gif" WIDTH=640 HEIGHT=3 ALIGN=bottom>
         
         <P><TABLE BORDER=0 WIDTH="61%">
            <TR>
               <TD COLSPAN=5>
                  <CENTER><B>¾�Υڡ����⤼�Ҹ��˹ԤäƤ���������</B></CENTER>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=68>
                  <CENTER><A HREF="$root/input.html" TARGET="_self"><FONT SIZE="+1" FACE="�楴���å���"><IMG SRC="$root/image/seimei.gif" WIDTH=57 HEIGHT=71 BORDER=3 ALIGN=bottom></FONT></A></CENTER>
               </TD>
               <TD WIDTH=70>
                  <CENTER><A HREF="$root/book.html" TARGET="_self"><FONT SIZE="+1" FACE="�楴���å���"><IMG SRC="$root/image/chosyo.gif" WIDTH=57 HEIGHT=71 BORDER=3 ALIGN=bottom></FONT></A></CENTER>
               </TD>
               <TD WIDTH=73>
                  <CENTER><A HREF="$root/baby.html" TARGET="_self"><FONT SIZE="+1" FACE="�楴���å���"><IMG SRC="$root/image/baby-name.gif" WIDTH=57 HEIGHT=71 BORDER=3 ALIGN=bottom></FONT></A></CENTER>
               </TD>
               <TD WIDTH=72>
                  <CENTER><A HREF="$root/consul.html"><IMG SRC="$root/image/consul.gif" WIDTH=57 HEIGHT=71 BORDER=3 ALIGN=bottom></A></CENTER>
               </TD>
               <TD>
                  <CENTER><A HREF="$root/link.html"><IMG SRC="$root/image/d-rink.gif" WIDTH=57 HEIGHT=71 BORDER=3 ALIGN=bottom></A></CENTER>
               </TD>
            </TR>
         </TABLE>
         </P>
         
         <P><IMG SRC=".$root/image/line_a2.gif" WIDTH=640 HEIGHT=3 ALIGN=bottom></P>
         
         <P><B><U>��������ϡ�����Ǥ���</U></B></P>
         
         <P>���ʤ��ο����Υѡ��ȥʡ��Ϥ⤦���Ĥ���ޤ������������餷���в񤤤򸫤Ĥ��Ʋ�������<BR>
         <A HREF="http://love.nozze-deai.com/guest/SZX00101/" TARGET="_blank"><IMG SRC="$root/image/nozze3.gif" WIDTH=468 HEIGHT=60 BORDER=0 ALIGN=bottom></A></P>

         <P><CENTER>
<TABLE BORDER=0 WIDTH=468 HEIGHT=80 CELLPADDING=0 CELLSPACING=0 BGCOLOR="#FFFFFF">
<TR><TD ALIGIN="center">
<A HREF="http://lovely.dd-c.net/w5/txlink.cgi/DDC000411_00/105/" TARGET="_top">
</A></TD></TR>
<TR><TD ALIGN=CENTER VALIGN=TOP>
<A HREF="http://lovely.dd-c.net/cgi-bin/dd/hb/banner/w5slink.cgi?uid=DDC000411_00 &bid=ONW5.210" TARGET="_top">
<IMG SRC="$root/image/o_net210.gif" WIDTH=468 HEIGHT=60 BORDER=0> </A></TD></TR>
</TABLE>
</CENTER></P>

         <P>��ʳ��ǥ��ڵ��Ѥ�ͥ��Ƥ����ɾȽ�γƥ���˥å��ͤǤ���<A HREF="http://cgi.din.or.jp/~toa-ad/tsw021a/jump.cgi?053102" TARGET="_blank"><IMG SRC="$root/image/sasamoto.gif" WIDTH=380 HEIGHT=30 BORDER=0 ALIGN=bottom></A>
         <A HREF="http://cgi.din.or.jp/~toa-ad/tsir99c/jump.cgi?053102">
         </A><A HREF="http://cgi.din.or.jp/~toa-ad/tsir99c/jump.cgi?053102" TARGET="_blank"><IMG SRC="$root/image/airu.gif" WIDTH=380 HEIGHT=30 BORDER=0 ALIGN=bottom></A>
         <A HREF="http://cgi.din.or.jp/~toa-ad/taka/seisin/lucky/jump.cgi?053102">
         </A><A HREF="http://cgi.din.or.jp/~toa-ad/taka/seisin/lucky/jump.cgi?053102" TARGET="_blank"><IMG SRC="$root/image/seisin.gif" WIDTH=380 HEIGHT=30 BORDER=0 ALIGN=bottom></A>
         <A HREF="http://cgi.din.or.jp/~toa-ad/tsak00k/sakai/jump.cgi?053102">
         </A><A HREF="http://cgi.din.or.jp/~toa-ad/tsak00k/sakai/jump.cgi?053102" TARGET="_blank"><IMG SRC="$root/image/sakai.gif" WIDTH=380 HEIGHT=30 BORDER=0 ALIGN=bottom></A>
         <A HREF="http://cgi.din.or.jp/~toa-ad/ane20a/jump.cgi?053102">
         </A><A HREF="http://cgi.din.or.jp/~toa-ad/ane20a/jump.cgi?053102" TARGET="_blank"><IMG SRC="$root/image/anesis.gif" WIDTH=380 HEIGHT=30 BORDER=0 ALIGN=bottom></A></P>
         
         <P>
<IFRAME frameBorder="0" height="60" width="468" marginHeight="0" scrolling="no" src="http://ad.jp.ap.valuecommerce.com/servlet/htmlbanner?sid=5358&pid=870014383" MarginWidth="0">
         <SCRIPT LANGUAGE=javascript src="http://ad.jp.ap.valuecommerce.com/servlet/jsbanner?sid=5358&pid=870014383"></SCRIPT>
<noscript> <A HREF="http://ck.jp.ap.valuecommerce.com/servlet/referral?sid=5358&pid=870014383" TARGET="_blank"><IMG SRC="http://ad.jp.ap.valuecommerce.com/servlet/gifbanner?sid=5358&pid=870014383" WIDTH=468 HEIGHT=60 BORDER=0 ALIGN=bottom></A>
</noscript> </IFRAME></P>
         
         <P>
<IFRAME frameBorder="0" height="60" width="468" marginHeight="0" scrolling="no" src="http://ad.jp.ap.valuecommerce.com/servlet/htmlbanner?sid=5358&pid=870014434" MarginWidth="0">
         <SCRIPT LANGUAGE=javascript src="http://ad.jp.ap.valuecommerce.com/servlet/jsbanner?sid=5358&pid=870014434"></SCRIPT>
<noscript> <A HREF="http://ck.jp.ap.valuecommerce.com/servlet/referral?sid=5358&pid=870014434" TARGET="_blank"><IMG SRC="http://ad.jp.ap.valuecommerce.com/servlet/gifbanner?sid=5358&pid=870014434" WIDTH=468 HEIGHT=60 BORDER=0 ALIGN=bottom></A>
</noscript> </IFRAME></P>
         
         <P><IMG SRC="$root/image/line_a2.gif" WIDTH=640 HEIGHT=3 ALIGN=bottom></P></CENTER>
      </TD>
   </TR>
   <TR>
      <TD>
         <CENTER>��
         
         <P><TABLE BORDER=1 WIDTH="100%">
            <TR>
               <TD>
                  <CENTER><A HREF="$root/index.html" TARGET="_self">�ȥåץڡ���</A></CENTER>
               </TD>
               <TD>
                  <CENTER><A HREF="$root/book.html" TARGET="_self">����Υ����ʡ�</A></CENTER>
               </TD>
               <TD>
                  <CENTER><A HREF="$root/baby.html" TARGET="_self">̿̾�Υ����ʡ�</A></CENTER>
               </TD>
            </TR>
            <TR>
               <TD>
                  <CENTER><A HREF="$root/consul.html">�֤����̥����ʡ���</A></CENTER>
               </TD>
               <TD>
                  <CENTER><A HREF="$root/info.html" TARGET="_self">������Τ��Τ餻</A></CENTER>
               </TD>
               <TD>
                  <CENTER><A HREF="$root/link.html">���ꤤľ���ء�</A></CENTER>
               </TD>
            </TR>
         </TABLE>
         </P>
         
         <P><IMG SRC="$root/image/line_a1.gif" WIDTH=640 HEIGHT=3 ALIGN=bottom></P></CENTER>
      </TD>
   </TR>
   <TR>
      <TD>
         <CENTER>��
         
         <P>��ʹ���ζʤˤĤ��Ƥϡ�<A HREF="$root/info.html#midi">������</A>������������</P>
         
         <P><IMG SRC="$root/image/line_a1.gif" WIDTH=640 HEIGHT=3 ALIGN=bottom></P></CENTER>
      </TD>
   </TR>
   <TR>
      <TD>
         <CENTER>��
         
         <P><FONT SIZE="-2">���η�̤򸫤ƤΤ��ո��䤴���ۤ�ʹ��������������<IMG SRC="$root/image/mail_a2.gif" WIDTH=20 HEIGHT=18 ALIGN=bottom></FONT><A HREF="mailto:okina\@e-mail.ne.jp"><FONT SIZE="-2">okina\@e-mail.ne.jp</FONT></A><FONT SIZE="-2"><I><BR>
         </I>��󥯤ϴ��ޤ��ޤ�����ɬ��</FONT><A HREF="$root/index.html" TARGET="_self"><FONT SIZE="-2">TOP�ڡ���</FONT></A><FONT SIZE="-2">�ؤ��ꤤ���ޤ���<BR>
         ���Υ���ƥ�Ĥξ������Ѥʤ�Ӥ�̵��ž�ܤϤ��Ǥꤤ�����ޤ������δ����̵���Ǥ���<BR>
         <I>CopyRight. K.Yamamoto. 1998.9.1</I></FONT></P></CENTER>
      </TD>
   </TR>
</TABLE>
</CENTER>

<P>��</P>

<P><FONT SIZE="-1">��</FONT></P>

<CENTER>������ ������</CENTER>
</BODY>
</HTML>

EOM
	&jcode'convert(*msg, "sjis", "euc");
	$msg =~ s/\$seimei/$sei $mei/g;
	print $msg;
}
