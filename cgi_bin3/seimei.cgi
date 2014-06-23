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

# �ޤۤ��WWW2��
$root = "/~kazu-y";
$cgipath = "/~kazu-y/cgi_bin3";
#$baseurl = "http://www2.mahoroba.ne.jp";



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

#����1������2��̾��1��̾��2�λ���
$seijib = &kakusu(substr($sei1, length($sei1)-2, 2));
$meijia = &kakusu(substr($mei1, 0, 2));
if (length($mei1) == 2) {
	$seijia = $kakusu{'soukaku'} - $kakusu{'jinkaku'};
}else {
	$seijia = $kakusu{'soukaku'} - $kakusu{'chikaku'} - $seijib;
}
$meijib = $kakusu{'soukaku'} - $kakusu{'jinkaku'} - $seijia;


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
#$kyoku = $jinshimo;
#$kyoku = 10 if ($kyoku == 0);
#$kyoku -= 1;
#$kyoku -= $kyoku % 2;
#$kyoku /= 2;
#$kyoku++;

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

<P><TABLE BORDER=0 CELLSPACING=0 CELLPADDING=0 WIDTH=640>
   <TR>
      <TD>
         <CENTER><FONT SIZE="+3" COLOR="#FF0000"><B>���Ϥ��줿������
         \$error ����Ƚ�̤Ǥ��ޤ���</B></FONT>
         
         <P>���˶�������ޤ����������������ե�����򤴳�ǧ�塢���������ܥ���򲡤��Ʋ�������<BR>
         ���ܲ������Τ˴����β��Ƚ���Ԥ��������᡼�륢�ɥ쥹�ޤǤ�Ϣ�����夲�ޤ���</P>
         
         <P>���ޤ��ξ��ˤϡ�������������β����2���<B>Ⱦ��</B>���ѿ��������Ϥ��Ʋ�������<BR>
         �㡢������Ϻ��������14�ʡ�Ϻ�פ˥��顼��å��������Ф���硣��</P>
         
         <P>������˴�Ť��ǡ����١����ι�����Ȼ��ˤϡ�����Υ��顼������ȿ�Ǥ�����ĺ���ޤ���</P></CENTER>
         
         <P>
         
         <HR>
         
         </P>
      </TD>
   </TR>
   <TR>
      <TD>
         <CENTER><FONT SIZE="+3"><B>������Τ��ͤ�</B></FONT></CENTER>
         
         <P><U>ʸ���β���ǡ����١����ˤĤ���</U></P>
         
         <P>���ߡ�̾�����Ѥ���������ϡ����Ѵ����ȿ�̾�����Ǥ�����Ͽ����
         �Ϥ���4000ʸ���ʾ�����夷�Ƥ���ޤ��������餢����̾�ˤϤ���˳������ʤ���Τ����Ĥ⤢��ޤ������ܲ��ηи�����������ܤ������ȤΤ�����̾�ˤĤ��ƤϽ���뤫����ǡ����١����ˤ���Ͽ���Ƥ���ޤ����������ʤ��顢���Ƥ���Ͽ����Ƥ���Ȥϸ����񤯡��ޤ���Ͽϳ�줬�ʤ��Ȥ�¤�ޤ���</P>
         
         <P>����Ϥ������ä����ʥ������Ǥ���Ȼפ��ޤ������ˤ�����Ǥ��������������Ƥ򤴳�ǧĺ��(�᡼�륢�ɥ쥹�ϴ����Ԥλؼ��˽��äƤ�������)����������ĺ����С�����������������β�����Τ餻�פ��ޤ�������Υǡ����١�����ȿ�Ǥ�����ĺ���ޤ���</P>
         
         <CENTER><FORM ACTION="$cgipath/n_mail2.cgi" METHOD=POST>
            <BLOCKQUOTE><BLOCKQUOTE><CENTER><TABLE BORDER=0 CELLSPACING=10 CELLPADDING=0>
                     <TR>
                        <TD>
                           <P ALIGN=right>���顼�ˤʤä�����</P>
                        </TD>
                        <TD>
                           <P><INPUT TYPE=hidden NAME=kanji VALUE="\$error" SIZE=10 MAXLENGTH=10>\$error</P>
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
         </FORM></CENTER>
         
         <P>
         
         <HR>
         
         </P>
      </TD>
   </TR>
   <TR>
      <TD>
         <CENTER><A HREF="$root/input3.html" TARGET="_self"><B>�⤦���ٴ��ꤹ��</B></A>
         
         <P><B>
         
         <HR>
         
         </B></P></CENTER>
      </TD>
   </TR>
   <TR>
      <TD>
         <CENTER><FONT SIZE="-2">���Υץ����ϴ�ȸ�������ȥ�ͥå��ǤǤ���WWW�Ǥξ������ѤϤǤ��ޤ���<BR>
         ���Υץ����Υ饤���󥹤��������Ȱʳ����軰�Ԥ�ž�䡢�����դ�ػߤ��ޤ���<BR>
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
<BODY BGCOLOR="#FFFFFF" BACKGROUND="$root/image/wall.jpg">
<P><HTML><HEAD><TITLE>���ܲ�����̾Ƚ��</TITLE></HEAD></P>

<CENTER><TABLE BORDER=0 CELLSPACING=0 WIDTH=640>
   <TR>
      <TD>
         <CENTER><FONT SIZE="+3" COLOR="#00CC00"><B>\$seimei����δ�����</B></FONT></CENTER>
         
         <P>
         
         <HR>
         
         </P>
         
         <P>���åǡ�������A=$seijia,����B=$seijib,��ŷ��=$kakusu{'tenkaku'},��̾A=$meijia,��̾B=$meijib
<FORM ACTION="seimei.cgi" METHOD=POST>
            <CENTER><TABLE BORDER=0 CELLSPACING=5 WIDTH=160>
               <TR>
                  <TD>
                     <CENTER>��<BR>
                     <INPUT TYPE=text NAME=sei VALUE="\$sei" SIZE=10 MAXLENGTH=10></CENTER>
                  </TD>
                  <TD>
                     <CENTER>̾<BR>
                     <INPUT TYPE=text NAME=mei VALUE="" SIZE=10 MAXLENGTH=10></CENTER>
                  </TD>
               </TR><INPUT TYPE=hidden NAME=sex VALUE="\$sex" size=10 maxlength=10>
       <INPUT TYPE=hidden NAME=marry VALUE="\$marry" size=10 maxlength=10>
               <TR>
                  <TD>
                     <CENTER><INPUT TYPE=submit NAME="����" VALUE="����"></CENTER>
                  </TD>
                  <TD>
                     <CENTER><A HREF="$root/input3.html">���</A></CENTER>
                  </TD>
               </TR>
            </TABLE>
            </CENTER>
         </FORM></P>
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
                  <FONT SIZE="-1" COLOR="#007F1F">���㤨�ȿ�·������̾�Ǥ��äƤ⡢�򹯤˷äޤ�ʤ���г褫�����ޤ���</FONT></P>
                  
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
         
         <HR>
         
         </P>
      </TD>
   </TR>
   <TR>
      <TD>
         <CENTER><A HREF="$root/input3.html" TARGET="_self"><B>�⤦���ٴ���򤹤�</B></A>
         
         <P><B>
         
         <HR>
         
         </B></P></CENTER>
      </TD>
   </TR>
   <TR>
      <TD>
         <CENTER><FONT SIZE="-2">���Υץ����ϴ�ȸ�������ȥ�ͥå��ǤǤ���WWW�Ǥξ������ѤϤǤ��ޤ���<BR>
         ���Υץ����Υ饤���󥹤��������Ȱʳ����軰�Ԥ�ž�䡢�����դ�ػߤ��ޤ���<BR>
         <I>CopyRight. K.Yamamoto.1999.3.21</I></FONT></CENTER>
      </TD>
   </TR>
</TABLE>
 <FONT SIZE="-1">��</FONT>������ ������</CENTER>
</BODY>
</HTML>


EOM
	&jcode'convert(*msg, "sjis", "euc");
	$msg =~ s/\$seimei/$sei $mei/g;
	$msg =~ s/\$sei/$sei/g;
	$msg =~ s/\$sex/$sex/g;
	$msg =~ s/\$marry/$marry/g;
	print $msg;
}
