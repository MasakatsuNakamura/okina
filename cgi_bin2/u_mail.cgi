#!/usr/local/bin/perl
$|=1;
########################
$sendmail = "/usr/lib/sendmail";
$youraddress = 'okina@e-mail.ne.jp';
########################
require "cgi-lib.pl";
require "jcode.pl";
require "zenhan.pl";
&ReadParse;
######�ǡ����μ�����#######
$member = $in{'member'};
$KMEI = $in{'name'};
$KMAIL = $in{'email'};
$order1 = $in{'order1'};
$order2 = $in{'order2'};
$order3 = $in{'order3'};
$SPOST = $in{'zipcord'};
$SADR = $in{'address'};
$STEL = $in{'tel'};
$SMEI = $in{'fullname'};
$familyname = $in{'familyname'};
$brthday = $in{'brthday'};
$user = $in{'user'};
$brother = $in{'brother'};
$request = $in{'request'};

######���Ϥ��줿�ǡ����Υ����å�######
if ($member =~ /^\s*$/) {
	&CgiError("NET-U����ֹ椬���Ϥ���Ƥ��ޤ���",
	"�֥饦���Ύ�Back���ܥ������äƺ����Ϥ��Ƥ���������");
	exit;
}
if ($KMEI =~ /^\s*$/) {
	&CgiError("�����ͤΤ�̾���ε���������ޤ���",
	"�֥饦���Ύ�Back���ܥ������äƺ����Ϥ��Ƥ���������");
	exit;
}
if (($order1 eq "" ) and ($order2 eq "" ) and ($order3 eq ""))  {
	&CgiError("���ϥ��顼",
		"����ʸ������ؼ�����Ƥ��ޤ���",
		"�֥饦���Ύ�Back���ܥ������äƺ����Ϥ��Ƥ���������");
	exit;
}	
if ($order2 ne "") {
	if ($SPOST eq "") {
		&CgiError("͹���ֹ椬���Ϥ���Ƥ��ޤ���",
		"�֥饦���Ύ�Back���ܥ������äƺ����Ϥ��Ƥ���������");
		exit;
	}
	elsif ($SADR eq "") {
		&CgiError("���꤬���Ϥ���Ƥ��ޤ���",
		"�֥饦���Ύ�Back���ܥ������äƺ����Ϥ��Ƥ���������");
		exit;
	}	
	elsif ($SMEI eq "") {
		&CgiError("����ͤ����Ϥ���Ƥ��ޤ���",
		"�֥饦���Ύ�Back���ܥ������äƺ����Ϥ��Ƥ���������");
		exit;
	}
}
if ($order3 ne "") {
	if ($familyname eq "") {
		&CgiError("�Ļ�(��)�����Ϥ���Ƥ��ޤ���",
		"�֥饦���Ύ�Back���ܥ������äƺ����Ϥ��Ƥ���������");
		exit;
	}
	elsif ($brthday eq "") {
		&CgiError("ͽ����(������)�����Ϥ���Ƥ��ޤ���",
		"�֥饦���Ύ�Back���ܥ������äƺ����Ϥ��Ƥ���������");
		exit;
	}
}

######�᡼�륢�ɥ쥹�Υ����å�######
if ($KMAIL =~ /^\s*$/){
	&CgiError("�᡼�륢�ɥ쥹�ε���������ޤ���",
	"�֥饦���Ύ�Back���ܥ������äƺ����Ϥ��Ƥ���������");
	exit;
}
elsif (($KMAIL) and (not $KMAIL =~ /.+\@.+\..+/)) {
	&CgiError("���ϥ��顼",
		"�᡼�륢�ɥ쥹�ν������ְ�äƤ��ޤ���",$KMAIL,
		"�֥饦���Ύ�Back���ܥ������äƺ����Ϥ��Ƥ���������");
	exit;
}
elsif (($hostname = $KMAIL) =~ s/.+\@(\S+)/$1/) {
	($hname,$aliases,$addresstype, $length,@address) =
		gethostbyname $hostname;
	if (not $hname) {
		&CgiError("�᡼��ۥ��ȥ��顼",
		"�᡼�륢�ɥ쥹����ǧ�Ǥ��ޤ���Ǥ�����");
		exit;
	}
}

######���ϥǡ�������������######
$member =~ s/\s*//g;
if ($SPOST ne "") {
	$SPOST =~ s/\s*//g;
	#���ѱѿ����򤹤٤�Ⱦ�ѱѿ����ˤ��롣
	$SPOST = &zen2han($SPOST); 
	#͹���ֹ椬7��ʲ������Ϥ��줿��硢00���������ղä��롣
	$SPOST = $SPOST . "00000000";
	$SPOST = substr($SPOST, 0, 8);
}
if ($STEL ne "") {
	$STEL =~ s/\s*//g;
	#���ѱѿ����򤹤٤�Ⱦ�ѱѿ����ˤ��롣
	$STEL = &zen2han($STEL); 
}
if ($familyname ne "") {
	$familyname =~ s/\s*//g;
}
if ($brthday ne "") {
	$brthday =~ s/\s*//g;
}

######P�쥸�����ֹ������######
$countfile = "count.txt";
open COUNTER,"$countfile"
	or &CgiError("$countfile �����ץ���1\n");
$SJNO = <COUNTER>;
close COUNTER;

++$SJNO;

open COUNTER,">$countfile"
	or &CgiError("$countfile �����ץ���2\n");
print COUNTER $SJNO;
close COUNTER;

######���ؤΤ���ʸ�᡼�������######
$com = <<MESSAGE;
From: $KMAIL
Subject: ���ܲ��ؤΤ���ʸ(NET-U���)

=====================================
�Х쥸�����ֹ桧
$SJNO
�������ͤλ�̾��
$KMEI
�������ͤ�E�᡼�륢�ɥ쥹��
$KMAIL
����ʸ���ơ�
$order1
$order2
$order3

���Ҥ�������ޤ���Ϣ����
͹���ֹ桧
$SPOST
�����ꡧ
$SADR
�������ֹ桧
$STEL
������͡�
$SMEI

̿̾�Τ���������
��(�ߤ礦��)��
$familyname
�л�ͽ������
$brthday
���ޤǤ����ѡ�
$user
���ФΤ�̾����
$brother
����˾���ࡧ
$request

=====================================
MESSAGE

&jcode'convert(*com,"jis");
open(MAIL, "|$sendmail $youraddress");
print MAIL $com;
close(MAIL);

######������������Ѥ������������ɽ������######
######�Ż��ܡ����ҡ�̿̾��3�Ĥ���ʸ#######
if (($order1 ne "") and ($order2 ne "") and ($order3 ne ""))  {
	$msg = <<"ORDER123";
Content-type: text/html

<HTML>
<HEAD>
   <TITLE>�Ż��ܤȽ��ҤΤ���ʸ��̿̾�Τ�����</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=x-sjis">
</HEAD>
<BODY BGCOLOR="#FFFFFF" BACKGROUND="/~kazu-y/image/wall.jpg">
<P><TABLE BORDER=0 CELLSPACING=0 CELLPADDING=0 WIDTH=640>
   <TR>
      <TD>
         <CENTER><FONT SIZE="+3"><B><U>����ʸͭ�񤦤������ޤ���</U></B></FONT>
         
         <P><FONT COLOR="#FF0000"><B>����³��NET-U�����ɤη�Ѥ�ԤäƤ��������ޤ���</B></FONT></P>
         
         <P>����ʸ���ƤΤ���ǧ<BR>
         <TABLE BORDER=1 WIDTH="80%">
            <TR>
               <TD>
                  <CENTER>����ʸ����</CENTER>
               </TD>
               <TD>
                  <CENTER>���(�����ǹ���)</CENTER>
               </TD>
               <TD>
                  <CENTER>����</CENTER>
               </TD>
            </TR>
            <TR>
               <TD>
                  <P>1.�����ܲ����Ż��܎������</P>
               </TD>
               <TD>
                  <P ALIGN=right>500��</P>
               </TD>
               <TD>
                  <P ALIGN=right>�ѥ�������</P>
               </TD>
            </TR>
            <TR>
               <TD>
                  <P>2.�����ܲ������񎣤����</P>
               </TD>
               <TD>
                  <P ALIGN=right>1,810��</P>
               </TD>
               <TD>
                  <P ALIGN=right>����310�߹���</P>
               </TD>
            </TR>
            <TR>
               <TD>
                  <P>3.����������̿̾�������</P>
               </TD>
               <TD>
                  <P ALIGN=right>10,000��</P>
               </TD>
               <TD>
                  <P></P>
               </TD>
            </TR>
            <TR>
               <TD>
                  <P ALIGN=right>��׹������</P>
               </TD>
               <TD>
                  <P ALIGN=right>12,310��</P>
               </TD>
               <TD>
                  <P></P>
               </TD>
            </TR>
         </TABLE>
         
         <B>����ǧ���Ѥߤޤ�����</B><FONT COLOR="#FF0000"><B>�������������ܥ����1�����������</B></FONT><B>����������<BR>
         ���Ф餯���Ԥ�ĺ����С�NET-U�����ɤη�Ѳ��̤��Ѥ��ޤ���</B></P>
         
         <P>����ʸ�������ϡ��֥饦���Ύ���뎣�ǎ����ϥե�������������ľ���Ʋ�������</P>
         
         <P><FORM ACTION="http://p-reg.u-card.co.jp/cgi-bin/junbi.cgi" METHOD=POST>
            <P><INPUT TYPE=hidden NAME="SID" VALUE=P0000161>
            <INPUT TYPE="hidden" NAME="SJNO" VALUE="\$SJNO">
            <INPUT TYPE="hidden" NAME="KGAK" VALUE="12310">
            <INPUT TYPE="hidden" NAME="SSUU" VALUE="3">
            <INPUT TYPE="hidden" NAME="ZEIGAK" VALUE="0">
            <INPUT TYPE="hidden" NAME="ICD1" VALUE="EBOK">
            <INPUT TYPE="hidden" NAME="ISUU1" VALUE="1">
            <INPUT TYPE="hidden" NAME="ICD2" VALUE="RBOK">
            <INPUT TYPE="hidden" NAME="ISUU2" VALUE="1">
            <INPUT TYPE="hidden" NAME="ICD3" VALUE="BABY">
            <INPUT TYPE="hidden" NAME="ISUU3" VALUE="1">
            <INPUT TYPE="hidden" NAME="KMEI" VALUE="\$KMEI">
            <INPUT TYPE="hidden" NAME="KMAIL" VALUE="\$KMAIL">
            <INPUT TYPE="hidden" NAME="SMEI" VALUE="\$SMEI">
            <INPUT TYPE="hidden" NAME="SPOST" VALUE="\$SPOST">
            <INPUT TYPE="hidden" NAME="SADR" VALUE="\$SADR">
            <INPUT TYPE="hidden" NAME="STEL" VALUE="\$STEL"></P>
            <CENTER><INPUT TYPE=submit NAME="����" VALUE="����"></CENTER>
         </FORM></P></CENTER>
      </TD>
   </TR>
</TABLE>
</P>
</BODY>
</HTML>

ORDER123
&jcode'convert(*msg, "sjis", "euc");
	$msg =~ s/\$KMEI/$KMEI/g;
	$msg =~ s/\$KMAIL/$KMAIL/g;
	$msg =~ s/\$order1/$order1/g;	
	$msg =~ s/\$order2/$order2/g;	
	$msg =~ s/\$order3/$order3/g;
	$msg =~ s/\$SPOST/$SPOST/g;
	$msg =~ s/\$SADR/$SADR/g;
	$msg =~ s/\$STEL/$STEL/g;
	$msg =~ s/\$SMEI/$SMEI/g;
	$msg =~ s/\$SJNO/$SJNO/g;
	print $msg;
}
#######�Ż��ܤȽ��Ҥ���ʸ##########
elsif (($order1 ne "") and ($order2 ne ""))  {
	$msg = <<"ORDER120";
Content-type: text/html

<HTML>
<HEAD>
   <TITLE>�Ż��ܤȽ��ҤΤ���ʸ</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=x-sjis">
</HEAD>
<BODY BGCOLOR="#FFFFFF" BACKGROUND="/~kazu-y/image/wall.jpg">
<P><TABLE BORDER=0 CELLSPACING=0 CELLPADDING=0 WIDTH=640>
   <TR>
      <TD>
         <CENTER><FONT SIZE="+3"><B><U>����ʸͭ�񤦤������ޤ���</U></B></FONT>
         
         <P><FONT COLOR="#FF0000"><B>����³��NET-U�����ɤη�Ѥ�ԤäƤ��������ޤ���</B></FONT></P>
         
         <P>����ʸ���ƤΤ���ǧ<BR>
         <TABLE BORDER=1 WIDTH="80%">
            <TR>
               <TD>
                  <CENTER>����ʸ����</CENTER>
               </TD>
               <TD>
                  <CENTER>���(�����ǹ���)</CENTER>
               </TD>
               <TD>
                  <CENTER>����</CENTER>
               </TD>
            </TR>
            <TR>
               <TD>
                  <P>1.�����ܲ����Ż��܎������</P>
               </TD>
               <TD>
                  <P ALIGN=right>500��</P>
               </TD>
               <TD>
                  <P ALIGN=right>�ѥ�������</P>
               </TD>
            </TR>
            <TR>
               <TD>
                  <P>2.�����ܲ������񎣤����</P>
               </TD>
               <TD>
                  <P ALIGN=right>1,810��</P>
               </TD>
               <TD>
                  <P ALIGN=right>����310�߹���</P>
               </TD>
            </TR>
            <TR>
               <TD>
                  <P ALIGN=right>��׹������</P>
               </TD>
               <TD>
                  <P ALIGN=right>2,310��</P>
               </TD>
               <TD>
                  <P></P>
               </TD>
            </TR>
         </TABLE>
         
         <B>����ǧ���Ѥߤޤ�����</B><FONT COLOR="#FF0000"><B>�������������ܥ����1�����������</B></FONT><B>����������<BR>
         ���Ф餯���Ԥ�ĺ����С�NET-U�����ɤη�Ѳ��̤��Ѥ��ޤ���</B></P>
         
         <P>����ʸ�������ϡ��֥饦���Ύ���뎣�ǎ����ϥե�������������ľ���Ʋ�������</P>
         
         <P><FORM ACTION="http://p-reg.u-card.co.jp/cgi-bin/junbi.cgi" METHOD=POST>
            <P><INPUT TYPE="hidden" NAME="SID" VALUE="P0000161">
            <INPUT TYPE="hidden" NAME="SJNO" VALUE="\$SJNO">
            <INPUT TYPE="hidden" NAME="KGAK" VALUE="2310">
            <INPUT TYPE="hidden" NAME="SSUU" VALUE="2">
            <INPUT TYPE="hidden" NAME="ZEIGAK" VALUE="0">
            <INPUT TYPE="hidden" NAME="ICD1" VALUE="EBOK">
            <INPUT TYPE="hidden" NAME="ISUU1" VALUE="1">
            <INPUT TYPE="hidden" NAME="ICD2" VALUE="RBOK">
            <INPUT TYPE="hidden" NAME="ISUU2" VALUE="1">
            <INPUT TYPE="hidden" NAME="KMEI" VALUE="\$KMEI">
            <INPUT TYPE="hidden" NAME="KMAIL" VALUE="\$KMAIL">
            <INPUT TYPE="hidden" NAME="SMEI" VALUE="\$SMEI">
            <INPUT TYPE="hidden" NAME="SPOST" VALUE="\$SPOST">
            <INPUT TYPE="hidden" NAME="SADR" VALUE="\$SADR">
            <INPUT TYPE="hidden" NAME="STEL" VALUE="\$STEL"></P>
            
            <CENTER><INPUT TYPE=submit NAME="����" VALUE="����"></CENTER>
         </FORM></P></CENTER>
      </TD>
   </TR>
</TABLE>
</P>
</BODY>
</HTML>

ORDER120
&jcode'convert(*msg, "sjis", "euc");
	$msg =~ s/\$KMEI/$KMEI/g;
	$msg =~ s/\$KMAIL/$KMAIL/g;
	$msg =~ s/\$order1/$order1/g;	
	$msg =~ s/\$order2/$order2/g;	
	$msg =~ s/\$SPOST/$SPOST/g;
	$msg =~ s/\$SADR/$SADR/g;
	$msg =~ s/\$STEL/$STEL/g;
	$msg =~ s/\$SMEI/$SMEI/g;
	$msg =~ s/\$SJNO/$SJNO/g;
	print $msg;
}
########�Ż��ܤ���ʸ��̿̾�ΰ���###########
elsif (($order1 ne "") and ($order3 ne ""))  {
	$msg = <<"ORDER103";
Content-type: text/html

<HTML>
<HEAD>
   <TITLE>�Ż��ܤΤ���ʸ��̿̾�Τ�����</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=x-sjis">
</HEAD>
<BODY BGCOLOR="#FFFFFF" BACKGROUND="/~kazu-y/image/wall.jpg">
<P><TABLE BORDER=0 CELLSPACING=0 CELLPADDING=0 WIDTH=640>
   <TR>
      <TD>
         <CENTER><FONT SIZE="+3"><B><U>����ʸͭ�񤦤������ޤ���</U></B></FONT>
         
         <P><FONT COLOR="#FF0000"><B>����³��NET-U�����ɤη�Ѥ�ԤäƤ��������ޤ���</B></FONT></P>
         
         <P>����ʸ���ƤΤ���ǧ<BR>
         <TABLE BORDER=1 WIDTH="80%">
            <TR>
               <TD>
                  <CENTER>����ʸ����</CENTER>
               </TD>
               <TD>
                  <CENTER>���(�����ǹ���)</CENTER>
               </TD>
               <TD>
                  <CENTER>����</CENTER>
               </TD>
            </TR>
            <TR>
               <TD>
                  <P>1.�����ܲ����Ż��܎������</P>
               </TD>
               <TD>
                  <P ALIGN=right>500��</P>
               </TD>
               <TD>
                  <P ALIGN=right>�ѥ�������</P>
               </TD>
            </TR>
            <TR>
               <TD>
                  <P>2.����������̿̾�������</P>
               </TD>
               <TD>
                  <P ALIGN=right>10,000��</P>
               </TD>
               <TD>
                  <P></P>
               </TD>
            </TR>
            <TR>
               <TD>
                  <P ALIGN=right>��׹������</P>
               </TD>
               <TD>
                  <P ALIGN=right>10,500��</P>
               </TD>
               <TD>
                  <P></P>
               </TD>
            </TR>
         </TABLE>
         
         <B>����ǧ���Ѥߤޤ�����</B><FONT COLOR="#FF0000"><B>�������������ܥ����1�����������</B></FONT><B>����������<BR>
         ���Ф餯���Ԥ�ĺ����С�NET-U�����ɤη�Ѳ��̤��Ѥ��ޤ���</B></P>
         
         <P>����ʸ�������ϡ��֥饦���Ύ���뎣�ǎ����ϥե�������������ľ���Ʋ�������</P>
         
         <P><FORM ACTION="http://p-reg.u-card.co.jp/cgi-bin/junbi.cgi" METHOD=POST>
            <P><INPUT TYPE="hidden" NAME="SID" VALUE="P0000161">
            <INPUT TYPE="hidden" NAME="SJNO" VALUE="\$SJNO">
            <INPUT TYPE="hidden" NAME="KGAK" VALUE="10500">
            <INPUT TYPE="hidden" NAME="SSUU" VALUE="2">
            <INPUT TYPE="hidden" NAME="ZEIGAK" VALUE="0">
            <INPUT TYPE="hidden" NAME="ICD1" VALUE="EBOK">
            <INPUT TYPE="hidden" NAME="ISUU1" VALUE="1">
            <INPUT TYPE="hidden" NAME="ICD2" VALUE="BABY">
            <INPUT TYPE="hidden" NAME="ISUU2" VALUE="1">
            <INPUT TYPE="hidden" NAME="KMEI" VALUE="\$KMEI">
            <INPUT TYPE="hidden" NAME="KMAIL" VALUE="\$KMAIL"></P>
            <CENTER><INPUT TYPE=submit NAME="����" VALUE="����"></CENTER>
         </FORM></P></CENTER>
      </TD>
   </TR>
</TABLE>
</P>
</BODY>
</HTML>

ORDER103
&jcode'convert(*msg, "sjis", "euc");
	$msg =~ s/\$KMEI/$KMEI/g;
	$msg =~ s/\$KMAIL/$KMAIL/g;
	$msg =~ s/\$order1/$order1/g;		
	$msg =~ s/\$order3/$order3/g;
	$msg =~ s/\$SPOST/$SPOST/g;
	$msg =~ s/\$SADR/$SADR/g;
	$msg =~ s/\$STEL/$STEL/g;
	$msg =~ s/\$SMEI/$SMEI/g;
	$msg =~ s/\$SJNO/$SJNO/g;
	print $msg;
}
########���Ҥ���ʸ��̿̾�ΰ���###########
elsif (($order2 ne "") and ($order3 ne ""))  {
	$msg = <<"ORDER023";
Content-type: text/html

<HTML>
<HEAD>
   <TITLE>���ҤΤ���ʸ��̿̾�Τ�����</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=x-sjis">
</HEAD>
<BODY BGCOLOR="#FFFFFF" BACKGROUND="/~kazu-y/image/wall.jpg">
<P><TABLE BORDER=0 CELLSPACING=0 CELLPADDING=0 WIDTH=640>
   <TR>
      <TD>
         <CENTER><FONT SIZE="+3"><B><U>����ʸͭ�񤦤������ޤ���</U></B></FONT>
         
         <P><FONT COLOR="#FF0000"><B>����³��NET-U�����ɤη�Ѥ�ԤäƤ��������ޤ���</B></FONT></P>
         
         <P>����ʸ���ƤΤ���ǧ<BR>
         <TABLE BORDER=1 WIDTH="80%">
            <TR>
               <TD>
                  <CENTER>����ʸ����</CENTER>
               </TD>
               <TD>
                  <CENTER>���(�����ǹ���)</CENTER>
               </TD>
               <TD>
                  <CENTER>����</CENTER>
               </TD>
            </TR>
            <TR>
               <TD>
                  <P>1.�����ܲ������񎣤����</P>
               </TD>
               <TD>
                  <P ALIGN=right>1,810��</P>
               </TD>
               <TD>
                  <P ALIGN=right>����310�߹���</P>
               </TD>
            </TR>
            <TR>
               <TD>
                  <P>2.����������̿̾�������</P>
               </TD>
               <TD>
                  <P ALIGN=right>10,000��</P>
               </TD>
               <TD>
                  <P></P>
               </TD>
            </TR>
            <TR>
               <TD>
                  <P ALIGN=right>��׹������</P>
               </TD>
               <TD>
                  <P ALIGN=right>11,810��</P>
               </TD>
               <TD>
                  <P></P>
               </TD>
            </TR>
         </TABLE>
         
         <B>����ǧ���Ѥߤޤ�����</B><FONT COLOR="#FF0000"><B>�������������ܥ����1�����������</B></FONT><B>����������<BR>
         ���Ф餯���Ԥ�ĺ����С�NET-U�����ɤη�Ѳ��̤��Ѥ��ޤ���</B></P>
         
         <P>����ʸ�������ϡ��֥饦���Ύ���뎣�ǎ����ϥե�������������ľ���Ʋ�������</P>
         
         <P><FORM ACTION="http://p-reg.u-card.co.jp/cgi-bin/junbi.cgi" METHOD=POST>
            <P><INPUT TYPE="hidden" NAME="SID" VALUE="P0000161">
            <INPUT TYPE="hidden" NAME="SJNO" VALUE="\$SJNO">
            <INPUT TYPE="hidden" NAME="KGAK" VALUE="11810">
            <INPUT TYPE="hidden" NAME="ZEIGAK" VALUE="0">
            <INPUT TYPE="hidden" NAME="SSUU" VALUE="2">
            <INPUT TYPE="hidden" NAME="ICD1" VALUE="RBOK">
            <INPUT TYPE="hidden" NAME="ISUU1" VALUE="1">
            <INPUT TYPE="hidden" NAME="ICD2" VALUE="BABY">
            <INPUT TYPE="hidden" NAME="ISUU2" VALUE="1">
            <INPUT TYPE="hidden" NAME="KMEI" VALUE="\$KMEI">
            <INPUT TYPE="hidden" NAME="KMAIL" VALUE="\$KMAIL">
            <INPUT TYPE="hidden" NAME="SMEI" VALUE="\$SMEI">
            <INPUT TYPE="hidden" NAME="SPOST" VALUE="\$SPOST">
            <INPUT TYPE="hidden" NAME="SADR" VALUE="\$SADR">
            <INPUT TYPE="hidden" NAME="STEL" VALUE="\$STEL"></P>
            <CENTER><INPUT TYPE=submit NAME="����" VALUE="����"></CENTER>
         </FORM></P></CENTER>
      </TD>
   </TR>
</TABLE>
</P>
</BODY>
</HTML>

ORDER023
&jcode'convert(*msg, "sjis", "euc");
	$msg =~ s/\$KMEI/$KMEI/g;
	$msg =~ s/\$KMAIL/$KMAIL/g;	
	$msg =~ s/\$order2/$order2/g;	
	$msg =~ s/\$order3/$order3/g;
	$msg =~ s/\$SPOST/$SPOST/g;
	$msg =~ s/\$SADR/$SADR/g;
	$msg =~ s/\$STEL/$STEL/g;
	$msg =~ s/\$SMEI/$SMEI/g;
	$msg =~ s/\$SJNO/$SJNO/g;
	print $msg;
}
############�Ż��ܤΤ���ʸ###########
elsif ($order1 ne "")  {
	$msg = <<"ORDER100";
Content-type: text/html

<HTML>
<HEAD>
   <TITLE>�Ż��ܤΤ���ʸ</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=x-sjis">
</HEAD>
<BODY BGCOLOR="#FFFFFF" BACKGROUND="/~kazu-y/image/wall.jpg">
<P><TABLE BORDER=0 CELLSPACING=0 CELLPADDING=0 WIDTH=640>
   <TR>
      <TD>
         <CENTER><FONT SIZE="+3"><B><U>����ʸͭ�񤦤������ޤ���</U></B></FONT>
         
         <P><FONT COLOR="#FF0000"><B>����³��NET-U�����ɤη�Ѥ�ԤäƤ��������ޤ���</B></FONT></P>
         
         <P>����ʸ���ƤΤ���ǧ<BR>
         <TABLE BORDER=1 WIDTH="80%">
            <TR>
               <TD>
                  <CENTER>����ʸ����</CENTER>
               </TD>
               <TD>
                  <CENTER>���(�����ǹ���)</CENTER>
               </TD>
               <TD>
                  <CENTER>����</CENTER>
               </TD>
            </TR>
            <TR>
               <TD>
                  <P>1.�����ܲ����Ż��܎������</P>
               </TD>
               <TD>
                  <P ALIGN=right>500��</P>
               </TD>
               <TD>
                  <P ALIGN=right>�ѥ�������</P>
               </TD>
            </TR>
            <TR>
               <TD>
                  <P ALIGN=right>��׹������</P>
               </TD>
               <TD>
                  <P ALIGN=right>500��</P>
               </TD>
               <TD>
                  <P></P>
               </TD>
            </TR>
         </TABLE>
         
         <B>����ǧ���Ѥߤޤ�����</B><FONT COLOR="#FF0000"><B>�������������ܥ����1�����������</B></FONT><B>����������<BR>
         ���Ф餯���Ԥ�ĺ����С�NET-U�����ɤη�Ѳ��̤��Ѥ��ޤ���</B></P>
         
         <P>����ʸ�������ϡ��֥饦���Ύ���뎣�ǎ����ϥե�������������ľ���Ʋ�������</P>
         
         <P><FORM ACTION="http://p-reg.u-card.co.jp/cgi-bin/junbi.cgi" METHOD=POST>
            <P><INPUT TYPE="hidden" NAME="SID" VALUE="P0000161">
            <INPUT TYPE="hidden" NAME="SJNO" VALUE="\$SJNO">
            <INPUT TYPE="hidden" NAME="KGAK" VALUE="500">
            <INPUT TYPE="hidden" NAME="ZEIGAK" VALUE="0">
            <INPUT TYPE="hidden" NAME="SSUU" VALUE="1">
            <INPUT TYPE="hidden" NAME="ICD1" VALUE="EBOK">
            <INPUT TYPE="hidden" NAME="ISUU1" VALUE="1">
            <INPUT TYPE="hidden" NAME="KMEI" VALUE="\$KMEI">
            <INPUT TYPE="hidden" NAME="KMAIL" VALUE="\$KMAIL"></P>
            <CENTER><INPUT TYPE=submit NAME="����" VALUE="����"></CENTER>
         </FORM></P></CENTER>
      </TD>
   </TR>
</TABLE>
</P>
</BODY>
</HTML>

ORDER100
&jcode'convert(*msg, "sjis", "euc");
	$msg =~ s/\$KMEI/$KMEI/g;
	$msg =~ s/\$KMAIL/$KMAIL/g;
	$msg =~ s/\$order1/$order1/g;	
	$msg =~ s/\$SPOST/$SPOST/g;
	$msg =~ s/\$SADR/$SADR/g;
	$msg =~ s/\$STEL/$STEL/g;
	$msg =~ s/\$SMEI/$SMEI/g;
	$msg =~ s/\$SJNO/$SJNO/g;
	print $msg;
}
#########���ҤΤ���ʸ##########
elsif ($order2 ne "")  {
	$msg = <<"ORDER020";
Content-type: text/html

<HTML>
<HEAD>
   <TITLE>���ҤΤ���ʸ</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=x-sjis">
</HEAD>
<BODY BGCOLOR="#FFFFFF" BACKGROUND="/~kazu-y/image/wall.jpg">
<P><TABLE BORDER=0 CELLSPACING=0 CELLPADDING=0 WIDTH=640>
   <TR>
      <TD>
         <CENTER><FONT SIZE="+3"><B><U>����ʸͭ�񤦤������ޤ���</U></B></FONT>
         
         <P><FONT COLOR="#FF0000"><B>����³��NET-U�����ɤη�Ѥ�ԤäƤ��������ޤ���</B></FONT></P>
         
         <P>����ʸ���ƤΤ���ǧ<BR>
         <TABLE BORDER=1 WIDTH="80%">
            <TR>
               <TD>
                  <CENTER>����ʸ����</CENTER>
               </TD>
               <TD>
                  <CENTER>���(�����ǹ���)</CENTER>
               </TD>
               <TD>
                  <CENTER>����</CENTER>
               </TD>
            </TR>
            <TR>
               <TD>
                  <P>1.�����ܲ������񎣤����</P>
               </TD>
               <TD>
                  <P ALIGN=right>1,810��</P>
               </TD>
               <TD>
                  <P ALIGN=right>����310�߹���</P>
               </TD>
            </TR>
            <TR>
               <TD>
                  <P ALIGN=right>��׹������</P>
               </TD>
               <TD>
                  <P ALIGN=right>1,810��</P>
               </TD>
               <TD>
                  <P></P>
               </TD>
            </TR>
         </TABLE>
         
         <B>����ǧ���Ѥߤޤ�����</B><FONT COLOR="#FF0000"><B>�������������ܥ����1�����������</B></FONT><B>����������<BR>
         ���Ф餯���Ԥ�ĺ����С�NET-U�����ɤη�Ѳ��̤��Ѥ��ޤ���</B></P>
         
         <P>����ʸ�������ϡ��֥饦���Ύ���뎣�ǎ����ϥե�������������ľ���Ʋ�������</P>
         
         <P><FORM ACTION="http://p-reg.u-card.co.jp/cgi-bin/junbi.cgi" METHOD=POST>
            <P><INPUT TYPE="hidden" NAME="SID" VALUE="P0000161">
            <INPUT TYPE="hidden" NAME="SJNO" VALUE="\$SJNO">
            <INPUT TYPE="hidden" NAME="KGAK" VALUE="1810">
            <INPUT TYPE="hidden" NAME="ZEIGAK" VALUE="0">
            <INPUT TYPE="hidden" NAME="SSUU" VALUE="1">
            <INPUT TYPE="hidden" NAME="ICD1" VALUE="RBOK">
            <INPUT TYPE="hidden" NAME="ISUU1" VALUE="1">
            <INPUT TYPE="hidden" NAME="KMEI" VALUE="\$KMEI">
            <INPUT TYPE="hidden" NAME="KMAIL" VALUE="\$KMAIL">
            <INPUT TYPE="hidden" NAME="SMEI" VALUE="\$SMEI">
            <INPUT TYPE="hidden" NAME="SPOST" VALUE="\$SPOST">
            <INPUT TYPE="hidden" NAME="SADR" VALUE="\$SADR">
            <INPUT TYPE="hidden" NAME="STEL" VALUE="\$STEL"></P>
            <CENTER><INPUT TYPE=submit NAME="����" VALUE="����"></CENTER>
         </FORM></P></CENTER>
      </TD>
   </TR>
</TABLE>
</P>
</BODY>
</HTML>

ORDER020
&jcode'convert(*msg, "sjis", "euc");
	$msg =~ s/\$KMEI/$KMEI/g;
	$msg =~ s/\$KMAIL/$KMAIL/g;
	$msg =~ s/\$order2/$order2/g;	
	$msg =~ s/\$SPOST/$SPOST/g;
	$msg =~ s/\$SADR/$SADR/g;
	$msg =~ s/\$STEL/$STEL/g;
	$msg =~ s/\$SMEI/$SMEI/g;
	$msg =~ s/\$SJNO/$SJNO/g;
	print $msg;
}
elsif ($order3 ne "")  {
#̿̾�Τ߰���
	$msg = <<"ORDER003";
Content-type: text/html

<HTML>
<HEAD>
   <TITLE>̿̾�Τ�����</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=x-sjis">
</HEAD>
<BODY BGCOLOR="#FFFFFF" BACKGROUND="/~kazu-y/image/wall.jpg">
<P><TABLE BORDER=0 CELLSPACING=0 CELLPADDING=0 WIDTH=640>
   <TR>
      <TD>
         <CENTER><FONT SIZE="+3"><B><U>����ʸͭ�񤦤������ޤ���</U></B></FONT>
         
         <P><FONT COLOR="#FF0000"><B>����³��NET-U�����ɤη�Ѥ�ԤäƤ��������ޤ���</B></FONT></P>
         
         <P>����ʸ���ƤΤ���ǧ<BR>
         <TABLE BORDER=1 WIDTH="80%">
            <TR>
               <TD>
                  <CENTER>����ʸ����</CENTER>
               </TD>
               <TD>
                  <CENTER>���(�����ǹ���)</CENTER>
               </TD>
               <TD>
                  <CENTER>����</CENTER>
               </TD>
            </TR>
            <TR>
               <TD>
                  <P>1.����������̿̾�������</P>
               </TD>
               <TD>
                  <P ALIGN=right>10,000��</P>
               </TD>
               <TD>
                  <P></P>
               </TD>
            </TR>
            <TR>
               <TD>
                  <P ALIGN=right>��׹������</P>
               </TD>
               <TD>
                  <P ALIGN=right>10,000��</P>
               </TD>
               <TD>
                  <P></P>
               </TD>
            </TR>
         </TABLE>
         
         <B>����ǧ���Ѥߤޤ�����</B><FONT COLOR="#FF0000"><B>�������������ܥ����1�����������</B></FONT><B>����������<BR>
         ���Ф餯���Ԥ�ĺ����С�NET-U�����ɤη�Ѳ��̤��Ѥ��ޤ���</B></P>
         
         <P>����ʸ�������ϡ��֥饦���Ύ���뎣�ǎ����ϥե�������������ľ���Ʋ�������</P>
         
         <P><FORM ACTION="http://p-reg.u-card.co.jp/cgi-bin/junbi.cgi" METHOD=POST>
            <P><INPUT TYPE="hidden" NAME="SID" VALUE="P0000161">
            <INPUT TYPE="hidden" NAME="SJNO" VALUE="\$SJNO">
            <INPUT TYPE="hidden" NAME="KGAK" VALUE="10000">
            <INPUT TYPE="hidden" NAME="ZEIGAK" VALUE="0">
            <INPUT TYPE="hidden" NAME="SSUU" VALUE="1">
            <INPUT TYPE="hidden" NAME="ICD1" VALUE="BABY">
            <INPUT TYPE="hidden" NAME="ISUU1" VALUE="1">
            <INPUT TYPE="hidden" NAME="KMEI" VALUE="\$KMEI">
            <INPUT TYPE="hidden" NAME="KMAIL" VALUE="\$KMAIL"></P>
            <CENTER><INPUT TYPE=submit NAME="����" VALUE="����"></CENTER>
         </FORM></P></CENTER>
      </TD>
   </TR>
</TABLE>
</P>
</BODY>
</HTML>

ORDER003
&jcode'convert(*msg, "sjis", "euc");
	$msg =~ s/\$KMEI/$KMEI/g;
	$msg =~ s/\$KMAIL/$KMAIL/g;	
	$msg =~ s/\$order3/$order3/g;
	$msg =~ s/\$SPOST/$SPOST/g;
	$msg =~ s/\$SADR/$SADR/g;
	$msg =~ s/\$STEL/$STEL/g;
	$msg =~ s/\$SMEI/$SMEI/g;
	$msg =~ s/\$SJNO/$SJNO/g;
	print $msg;
}
__end__
