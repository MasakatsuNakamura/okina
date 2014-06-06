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

<BODY BGCOLOR="#FFFFFF">
<CENTER><FONT SIZE="+3"><B>���Ϥ��줿������\$error��
��Ƚ�̤Ǥ��ޤ���</B></FONT>

<P>���˶�������ޤ�����<A HREF="#form" TARGET="_self"><B>�����Υե�����</B></A>�Τˤ������ξ塢�����ܥ���򲡤��Ƥ���������<BR>
�����ǡ����١����ν�������λ���ޤ����顢������Υ᡼�륢�ɥ쥹�ޤǤ�Ϣ�����夲�ޤ���</P>

<P>

<HR>

<FONT SIZE="+3"><B>������Τ��ͤ�</B></FONT></P></CENTER>

<P><U>ʸ���β���ǡ����١����ˤĤ���</U></P>

<P>���ߡ�̾�����Ѥ���������ϡ����Ѵ����ȿ�̾�����Ǥ�����Ͽ����
�Ϥ�����2000ʸ�������夷�Ƥ���ޤ��������餢����̾�ˤϤ���˳������ʤ���Τ����Ĥ�����ޤ������ܲ��ηи�����������ܤ������ȤΤ�����̾�ˤĤ��ƤϽ���뤫����ǡ����١����ˤ���Ͽ���Ƥ���ޤ����������ʤ��顢���Ƥ���Ͽ����Ƥ���Ȥϸ����񤯡��ޤ���Ͽϳ�줬�ʤ��Ȥ�¤�ޤ���</P>

<P>����Ϥ������ä����ʥ������Ǥ���Ȼפ��ޤ������ˤ�����Ǥ����������Υե�����ˤ�����ĺ���ޤ����顢�������������̤�Ϣ�����Ƥ��������ޤ�������Υǡ����١�����ȿ�Ǥ�����ĺ�������ȹͤ��ޤ��Τǡ������ϵ��������ꤤ�����夲�ޤ���</P>

<CENTER><FORM ACTION="$cgipath/gn_mail2.cgi" METHOD=POST>
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

<P>

<HR>

<TABLE BORDER=1 WIDTH=600>
   <TR>
      <TD>
         <CENTER><A HREF="$root/g-index.html" TARGET="_self"><B>�ȥåץڡ���</B></A></CENTER>
      </TD>
      <TD>
         <CENTER><A HREF="$root/g-input.html" TARGET="_self"><B>�⤦���ٴ��ꤹ��</B></A></CENTER>
      </TD>
      <TD>
         <CENTER><A HREF="$root/g-book.html" TARGET="_self"><B>����Υ����ʡ�</B></A></CENTER>
      </TD>
      <TD>
         <CENTER><A HREF="$root/g-baby.html" TARGET="_self"><B>̿̾�Υ����ʡ�</B></A></CENTER>
      </TD>
      <TD>
         <CENTER><A HREF="$root/g-info.html"><B>������Τ��Τ餻</B></A></CENTER>
      </TD>
   </TR>
</TABLE>
 ���� <FONT SIZE="-2">

<HR>

��󥯤ϴ��ޤ��ޤ�����ɬ��</FONT><A HREF="$root/g-index.html" TARGET="_self"><FONT SIZE="-2"><I>TOP�ڡ���</I></FONT></A><FONT SIZE="-2">�ؤ��ꤤ���ޤ���<BR>
���Υ���ƥ�Ĥξ������Ѥʤ�Ӥ�̵��ž�ܤϤ��Ǥ��פ��ޤ���<BR>
<I>CopyRight. K.Yamamoto.1999.5.8</I></FONT></P></CENTER>
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

<BODY BGCOLOR="#FFFFFF">
<CENTER><TABLE BORDER=0 CELLSPACING=0 WIDTH=600>
   <TR>
      <TD>
         <P><TABLE BORDER=0 CELLSPACING=0 CELLPADDING=0 WIDTH="100%">
            <TR>
               <TD VALIGN=top WIDTH=300 HEIGHT=170 BGCOLOR="#CCCCCC">
                  <CENTER><FONT SIZE="+2" COLOR="#0033FF"><B><TABLE BORDER=0 CELLSPACING=0 CELLPADDING=0 WIDTH=300>
                     <TR>
                        <TD VALIGN=bottom>
                           <CENTER><IMG SRC="$root/image/g-result.jpg" WIDTH=300 HEIGHT=240 ALIGN=top></CENTER>
                        </TD>
                     </TR>
                     <TR>
                        <TD>
                           <CENTER><FONT SIZE="+2"><B>\$seimei����ؤν���</B></FONT></CENTER>
                        </TD>
                     </TR>
                  </TABLE>
                   </B></FONT></CENTER>
               </TD>
               <TD VALIGN=top WIDTH=300 HEIGHT=170 BGCOLOR="#CCCCCC">
                  <CENTER><B><U>���ܲ����</U></B></CENTER>
                  
                  <P>���籿���пͱ������ñ�����ǯ���Ȱ츫̷�⤹��褦�ʷ�̤򼨤����Ȥ⤢��ޤ�������Ͽʹ֤Ȥ�����Τϡ��������ܿ����㤦�Τ��Ǥ������������Ȥ���������Ȥ������Ȥǡ������̤ˤ⤽��ϸ���Ƥ��Ƥ���Ȥ����򲼤��������äơ��ޤ����������Τ�į���ĺ�������˸ġ�����ʬ�ˤĤ��Ƽ�ʬ�ʤ��ʬ�Ϥ���Ƥߤ�������ᤷ�ޤ����ʤ��������δ���Ȥ����Τϡ����ҤΤ褦�ʿͤ��줾��ζ�������δĶ������Ū�˲�̣����Ƚ�Ǥ���ΤǤ��������󥿡��ͥåȤǤϤ����ޤǤλ�������ޤ���Τǡ��������餺��λ����������</P>
               </TD>
            </TR>
         </TABLE>
         </P>
         
         <P>
         
         <HR>
         
         </P>
      </TD>
   </TR>
   <TR>
      <TD>
         <P><TABLE BORDER=3 CELLSPACING=10 WIDTH="100%">
            <TR>
               <TD VALIGN=top>
                  <P><FONT SIZE="+2"><B>�籿</B>
                  </FONT><FONT SIZE="-1"><U>�����ͤΰ������濴��ʤ�ޤ����뺧�ˤ�������Ѥ��ȼ籿���Ѥ��ޤ�������ǯ�ʹߤ˶�������ޤ���</U></FONT></P>
                  
                  <BLOCKQUOTE>$kakusu{'jinkaku'}�衧$res{'jinkaku'}</BLOCKQUOTE>
                  
                  <P></P>
               </TD>
               <TD VALIGN=top>
                  <P><FONT SIZE="+2"><B>�пͱ����Ҹ�</B></FONT><FONT SIZE="-1"><B>
                  </B><U>���пʹط����²�����شط���ͧã�ط��˸���Ƥ��ޤ���</U></FONT></P>
                  
                  <BLOCKQUOTE>$kakusu{'gaikaku'}�衧$res{'gaikaku'}</BLOCKQUOTE>
                  
                  <P></P>
               </TD>
            </TR>
            <TR>
               <TD VALIGN=top>
                  <P><FONT SIZE="+2"><B>�򹯱�(��Ĵ������)
                  </B></FONT><FONT SIZE="-1"><U>���㤨�ȿ�·������̾�Ǥ��äƤ⡢�򹯤˷äޤ�ʤ���г褫�����ޤ���</U></FONT></P>
                  
                  <BLOCKQUOTE>$res{'kenkou'}</BLOCKQUOTE>
                  
                  <P></P>
               </TD>
               <TD VALIGN=top>
                  <P><FONT SIZE="+2"><B>����
                  </B></FONT><FONT SIZE="-1"><U>�����ͤγ���Ū�����ʤ򸽤��ޤ�����ʬ��¾�ͤ���ɤ������Ƥ���Τ����ͤˤʤ�ޤ���</U></FONT></P>
                  
                  <BLOCKQUOTE>$res{'seikaku'}</BLOCKQUOTE>
                  
                  <P></P>
               </TD>
            </TR>
            <TR>
               <TD VALIGN=top>
                  <P><FONT SIZE="+2"><B>���ñ�
                  </B></FONT><FONT SIZE="-1"><U>���ľ�ǯ���α����εȶ�����ۤ�����ǯ���ޤǺǤ⶯�����Ѥ��ޤ���(��ǯ�Ԥ�Ƚ�ǤϤ����餬ͭ��)</U></FONT></P>
                  
                  <BLOCKQUOTE>$kakusu{'chikaku'}�衧$res{'chikaku'}</BLOCKQUOTE>
                  
                  <P></P>
               </TD>
               <TD VALIGN=top>
                  <P><FONT SIZE="+2"><B>��ǯ��
                  </B></FONT><FONT SIZE="-1"><U>��50�����夫�鶯������Ƥ��ޤ������������籿�ȴ��ñ��˺�������ޤ��Τ���դ��Ʋ�������</U></FONT></P>
                  
                  <BLOCKQUOTE>$kakusu{'soukaku'}�衧$res{'soukaku'}</BLOCKQUOTE>
                  
                  <P></P>
               </TD>
            </TR>
         </TABLE>
         </P>
         
         <CENTER><B>�����̤����ˤʤ����ϡ�������Υ����ʡ�����������Τ��Τ餻����ʻ���Ƥ�����������</B></CENTER>
         
         <P>
         
         <HR>
         
         </P>
      </TD>
   </TR>
   <TR>
      <TD>
         <P><TABLE BORDER=1 WIDTH="100%">
            <TR>
               <TD>
                  <CENTER><A HREF="$root/i-geti.html" TARGET="_self"><B>�ȥåץڡ���</B></A></CENTER>
               </TD>
               <TD>
                  <CENTER><A HREF="$root/g-input.html" TARGET="_self"><B>�⤦���ٴ��ꤹ��</B></A></CENTER>
               </TD>
               <TD>
                  <CENTER><A HREF="$root/g-book.html" TARGET="_self"><B>����Υ����ʡ�</B></A></CENTER>
               </TD>
               <TD>
                  <CENTER><A HREF="$root/g-baby.html" TARGET="_self"><B>̿̾�Υ����ʡ�</B></A></CENTER>
               </TD>
               <TD>
                  <CENTER><A HREF="$root/g-info.html" TARGET="_self"><B>������Τ��Τ餻</B></A></CENTER>
               </TD>
            </TR>
         </TABLE>
         
         <HR>
         
         </P>
      </TD>
   </TR>
   <TR>
      <TD>
         <CENTER>���Υ���ƥ�Ĥϥ��㡼��(��)�¤Υ����륹�������ƥ�<FONT SIZE="-2">(TM)</FONT>�����������Խ����줿��ΤǤ���<BR>
         �ե�С�������<A HREF="http://www2.mahoroba.ne.jp/~kazy-y/index.html">������</A>������������
         
         <P>
         
         <HR>
         
         </P></CENTER>
      </TD>
   </TR>
   <TR>
      <TD>
         <CENTER><FONT SIZE="-2">���η�̤򸫤ƤΤ��ո��䤴���ۤ�ʹ��������������</FONT><A HREF="mailto:okina\@e-mail.ne.jp"><FONT SIZE="-2">okina\@e-mail.ne.jp</FONT></A><FONT SIZE="-2"><I><BR>
         </I>��󥯤ϴ��ޤ��ޤ�����ɬ��</FONT><A HREF="$root/i-geti.html" TARGET="_self"><FONT SIZE="-2">TOP�ڡ���</FONT></A><FONT SIZE="-2">�ؤ��ꤤ���ޤ���<BR>
         ���Υ���ƥ�Ĥξ������Ѥʤ�Ӥ�̵��ž�ܤϤ��Ǥꤤ�����ޤ������δ����̵���Ǥ���<BR>
         <I>CopyRight. K.Yamamoto. 1999.5.8</I></FONT></CENTER>
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
