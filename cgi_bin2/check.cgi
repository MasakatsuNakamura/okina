#!/usr/local/bin/perl
$|=1;
#########################
require 'cgi-lib.pl';
require 'jcode.pl';
require "zenhan.pl";
use MIME::Base64;
&ReadParse();
#########################
$name = $in{'name'};
$email = $in{'email'};
$order1 = $in{'order1'};
$order2 = $in{'order2'};
$order3 = $in{'order3'};
$zipcord = $in{'zipcord'};
$address = $in{'address'};
$tel = $in{'tel'};
$fullname = $in{'fullname'};
$familyname = $in{'familyname'};
$brthday = $in{'brthday'};
$user = $in{'user'};
$brother = $in{'brother'};
$request = $in{'request'};
$exp = $in{'exp'};
######���ϥǡ�������������######
if ($zipcord ne "") {
	$zipcord =~ s/\s*//g;
	#���ѱѿ����򤹤٤�Ⱦ�ѱѿ����ˤ��롣
	$zipcord = &zen2han($zipcord); 
}
if ($tel ne "") {
	$tel =~ s/\s*//g;
	#���ѱѿ����򤹤٤�Ⱦ�ѱѿ����ˤ��롣
	$tel = &zen2han($tel); 
}
if ($familyname ne "") {
	$familyname =~ s/\s*//g;
}
if ($brthday ne "") {
	$brthday =~ s/\s*//g;
}
if ($email ne "") {
	$email =~ s/\s*//g;
	#���ѱѿ����򤹤٤�Ⱦ�ѱѿ����ˤ��롣
	$email = &zen2han($email);
} 
#####���ϥ��顼�Υ����å�#####
if ($name =~ /^\s*$/){
	&CgiError("̾���ε���������ޤ���",
	"�֥饦���Ύ�Back���ܥ������äƺ����Ϥ��Ƥ���������");
	exit;
}
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
if (($order1 eq "" ) and ($order2 eq "" ) and ($order3 eq ""))  {
	&CgiError("���ϥ��顼",
		"����ʸ������ؼ�����Ƥ��ޤ���",
		"�֥饦���Ύ�Back���ܥ������äƺ����Ϥ��Ƥ���������");
	exit;
}	
if ($order2 ne "") {
	if ($zipcord eq "") {
		&CgiError("͹���ֹ椬���Ϥ���Ƥ��ޤ���",
		"�֥饦���Ύ�Back���ܥ������äƺ����Ϥ��Ƥ���������");
		exit;
	}
	elsif ($address eq "") {
		&CgiError("���꤬���Ϥ���Ƥ��ޤ���",
		"�֥饦���Ύ�Back���ܥ������äƺ����Ϥ��Ƥ���������");
		exit;
	}	
	elsif ($fullname eq "") {
		&CgiError("����ͤ����Ϥ���Ƥ��ޤ���",
		"�֥饦���Ύ�Back���ܥ������äƺ����Ϥ��Ƥ���������");
		exit;
	}
	elsif ($tel eq "") {
		&CgiError("�����ֹ椬���Ϥ���Ƥ��ޤ��󡣸������ä�̵�����˸¤�����ֹ�Ǥ�빽�Ǥ���",
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
if ($exp ne "") {
	if ($tel eq "") {
		&CgiError("�����ֹ椬���Ϥ���Ƥ��ޤ���",
		"�֥饦���Ύ�Back���ܥ������äƺ����Ϥ��Ƥ���������");
		exit;
	}
	elsif ($zipcord eq "") {
		&CgiError("͹���ֹ椬���Ϥ���Ƥ��ޤ���",
		"�֥饦���Ύ�Back���ܥ������äƺ����Ϥ��Ƥ���������");
		exit;
	}
    elsif ($address eq "") {
		&CgiError("���꤬���Ϥ���Ƥ��ޤ���",
		"�֥饦���Ύ�Back���ܥ������äƺ����Ϥ��Ƥ���������");
		exit;
	}	
}
#####������η׻����å�#####
if (($order1 ne "") and ($order2 ne "") and ($order3 ne ""))  {
   if ($exp ne "") {
       $kgak ="16,810";
   }
   elsif ($exp eq "") {
       $kgak ="11,810";
   }
}
elsif (($order1 ne "") and ($order2 ne ""))  {
   $kgak ="1,810";
}
elsif (($order1 ne "") and ($order3 ne ""))  {
   if ($exp ne "") {
       $kgak ="15,500";
   }
   elsif ($exp eq "") {
       $kgak ="10,500";
   }
}
elsif (($order2 ne "") and ($order3 ne ""))  {
   if ($exp ne "") {
       $kgak ="16,810";
   }
   elsif ($exp eq "") {
       $kgak ="11,810";
   }
}
elsif ($order1 ne "")  {
   $kgak ="500";
}
elsif ($order2 ne "")  {
   $kgak ="1,810";
}
elsif ($order3 ne "")  {
   if ($exp ne "") {
       $kgak ="15,000";
   }
   elsif ($exp eq "") {
       $kgak ="10,000";
  }
}
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
         <CENTER><FONT SIZE="+3"><B><U>����ʸ���ƤΤ���ǧ</U></B></FONT></CENTER>
         
         <BLOCKQUOTE>���β��̤ϡ�����ʸ���Ƥ򤴳�ǧĺ������Τ�ΤǤ������Ƥ˸�꤬������ϡ��֥饦���Ρ����ץܥ���򲡤��Ǝ����ϥե����������齤�����Ʋ�����������ǵ�������С���ʸ�ץܥ���򲡤��Ʋ��������ʤ��Ż��ܤȽ��Ҥ�ξ������ʸ�ξ�硢500�ߤ����פ��ޤ���</BLOCKQUOTE>
         
         <CENTER><B>����ʸ����</B><BR>
<TABLE BORDER=1 WIDTH="90%">
   <TR>
      <TD WIDTH=148>
         <P>�������(����)�Τ�̾��</P>
      </TD>
      <TD>
         <P>\$name</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>������ԤΥ᡼�륢�ɥ쥹</P>
      </TD>
      <TD>
         <P>\$email</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>�����������</P>
      </TD>
      <TD>
         <P>���ܲ�������(�Ż��ܤȼ���)����ʸ����������̿̾����</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>���ҤΤ�������</P>
      </TD>
      <TD>
         <P><TABLE BORDER=1>
            <TR>
               <TD WIDTH=55>
                  <P>͹���ֹ�</P>
               </TD>
               <TD>
                  <P>\$zipcord</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=55>
                  <P>����</P>
               </TD>
               <TD>
                  <P>\$address</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=55>
                  <P>�������</P>
               </TD>
               <TD>
                  <P>\$fullname</P>
               </TD>
            </TR>
         </TABLE>
         </P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>��Ϣ���褪�����ֹ�</P>
      </TD>
      <TD>
         <P>\$tel</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>��������̿̾����</P>
      </TD>
      <TD>
         <P><TABLE BORDER=1>
            <TR>
               <TD WIDTH=92>
                  <P>��(�Ļ�)</P>
               </TD>
               <TD>
                  <P>\$familyname</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=92>
                  <P>������(ͽ����)</P>
               </TD>
               <TD>
                  <P>\$brthday</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=92>
                  <P>���Τ�����</P>
               </TD>
               <TD>
                  <P>\$user</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=92>
                  <P>������Τ�̾��</P>
               </TD>
               <TD>
                  <P>\$brother</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=92>
                  <P>����˾����</P>
               </TD>
               <TD>
                  <P>\$request</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=92>
                  <P>�õ�����</P>
               </TD>
               <TD>
                  <P>\$exp</P>
               </TD>
            </TR>
         </TABLE>
         </P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>��פ���ʧ�����</P>
      </TD>
      <TD>
         <P>\$kgak ��</P>
      </TD>
   </TR>
</TABLE>
</CENTER>
         
         <BLOCKQUOTE>
            <B>����ǧ���Ѥߤޤ�����</B><FONT COLOR="#FF0000"><B>��������ʸ���ܥ����1����������Ƥ�ȯ��</B></FONT><B>����������<BR>
            �ʤ������ʤ����ʾ塢����ʹߤΤ���ʸ�μ��ä������ʤϰ��ڽ���ޤ���Τ�ͽ�ᤴλ����������(ˬ������ˡ�Υ�����󥰥��դ�Ŭ�Ѥ���ޤ��󡣡�</B></BLOCKQUOTE>
         
         <CENTER>����ʸ�������ϡ��֥饦���Ύ���뎣�ǎ����ϥե�������������ľ���Ʋ�������</CENTER>
         
         <P><FORM ACTION="/~kazu-y/cgi_bin2/nn_mail.cgi" METHOD=POST>
            <P><INPUT TYPE="hidden" NAME="name" VALUE="\$name">
            <INPUT TYPE="hidden" NAME="email" VALUE="\$email">
            <INPUT TYPE="hidden" NAME="order1" VALUE="\$order1">
            <INPUT TYPE="hidden" NAME="order2" VALUE="\$order2">
            <INPUT TYPE="hidden" NAME="order3" VALUE="\$order3">
            <INPUT TYPE="hidden" NAME="zipcord" VALUE="\$zipcord">
            <INPUT TYPE="hidden" NAME="address" VALUE="\$address">
            <INPUT TYPE="hidden" NAME="tel" VALUE="\$tel">
            <INPUT TYPE="hidden" NAME="fullname" VALUE="\$fullname">
            <INPUT TYPE="hidden" NAME="familyname" VALUE="\$familyname">
            <INPUT TYPE="hidden" NAME="brthday" VALUE="\$brthday">
            <INPUT TYPE="hidden" NAME="user" VALUE="\$user">
            <INPUT TYPE="hidden" NAME="brother" VALUE="\$brother">
            <INPUT TYPE="hidden" NAME="request" VALUE="\$request">
            <INPUT TYPE="hidden" NAME="exp" VALUE="\$exp">
            <INPUT TYPE="hidden" NAME="kgak" VALUE="\$kgak">
            <CENTER><INPUT TYPE=submit NAME="����" VALUE="��ʸ"></CENTER>
         </FORM></P></CENTER>
      </TD>
   </TR>
</TABLE>
</P>
</BODY>
</HTML>

ORDER123
&jcode'convert(*msg, "sjis", "euc");
	$msg =~ s/\$name/$name/g;
	$msg =~ s/\$email/$email/g;
	$msg =~ s/\$order1/$order1/g;
	$msg =~ s/\$order2/$order2/g;	
	$msg =~ s/\$order3/$order3/g;	
	$msg =~ s/\$zipcord/$zipcord/g;
	$msg =~ s/\$address/$address/g;
	$msg =~ s/\$tel/$tel/g;
	$msg =~ s/\$fullname/$fullname/g;
	$msg =~ s/\$familyname/$familyname/g;
	$msg =~ s/\$brthday/$brthday/g;
	$msg =~ s/\$user/$user/g;
	$msg =~ s/\$brother/$brother/g;
	$msg =~ s/\$request/$request/g;
	$msg =~ s/\$exp/$exp/g;
    $msg =~ s/\$kgak/$kgak/g;
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
<CENTER><FONT SIZE="+3"><B><U>����ʸ���ƤΤ���ǧ</U></B></FONT></CENTER>
         
         <BLOCKQUOTE>���β��̤ϡ�����ʸ���Ƥ򤴳�ǧĺ������Τ�ΤǤ������Ƥ˸�꤬������ϡ��֥饦���Ρ����ץܥ���򲡤��Ǝ����ϥե����������齤�����Ʋ�����������ǵ�������С���ʸ�ץܥ���򲡤��Ʋ��������ʤ��Ż��ܤȽ��Ҥ�ξ������ʸ�ξ�硢500�ߤ����פ��ޤ���</BLOCKQUOTE>
         
         <CENTER><B>����ʸ����</B><BR>
         <TABLE BORDER=1 WIDTH="90%">
 <TR>
      <TD WIDTH=148>
         <P>�������(����)�Τ�̾��</P>
      </TD>
      <TD>
         <P>\$name</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>������ԤΥ᡼�륢�ɥ쥹</P>
      </TD>
      <TD>
         <P>\$email</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>�����������</P>
      </TD>
      <TD>
         <P>���ܲ�������(�Ż��ܤȼ���)����ʸ</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>���ҤΤ�������</P>
      </TD>
      <TD>
         <P><TABLE BORDER=1>
            <TR>
               <TD WIDTH=55>
                  <P>͹���ֹ�</P>
               </TD>
               <TD>
                  <P>\$zipcord</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=55>
                  <P>����</P>
               </TD>
               <TD>
                  <P>\$address</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=55>
                  <P>�������</P>
               </TD>
               <TD>
                  <P>\$fullname</P>
               </TD>
            </TR>
         </TABLE>
         </P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>��Ϣ���褪�����ֹ�</P>
      </TD>
      <TD>
         <P>\$tel</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>��פ���ʧ�����</P>
      </TD>
      <TD>
         <P>\$kgak ��</P>
      </TD>
   </TR>
</TABLE>
</CENTER>
         
         <BLOCKQUOTE>
            <B>����ǧ���Ѥߤޤ�����</B><FONT COLOR="#FF0000"><B>��������ʸ���ܥ����1����������Ƥ�ȯ��</B></FONT><B>����������<BR>
            �ʤ������ʤ����ʾ塢����ʹߤΤ���ʸ�μ��ä������ʤϰ��ڽ���ޤ���Τ�ͽ�ᤴλ����������(ˬ������ˡ�Υ�����󥰥��դ�Ŭ�Ѥ���ޤ��󡣡�</B></BLOCKQUOTE>
         
         <CENTER>����ʸ�������ϡ��֥饦���Ύ���뎣�ǎ����ϥե�������������ľ���Ʋ�������</CENTER>
         
         <P><FORM ACTION="/~kazu-y/cgi_bin2/nn_mail.cgi" METHOD=POST>
            <P><INPUT TYPE="hidden" NAME="name" VALUE="\$name">
            <INPUT TYPE="hidden" NAME="email" VALUE="\$email">
            <INPUT TYPE="hidden" NAME="order1" VALUE="\$order1">
            <INPUT TYPE="hidden" NAME="order2" VALUE="\$order2">
            <INPUT TYPE="hidden" NAME="order3" VALUE="">
            <INPUT TYPE="hidden" NAME="zipcord" VALUE="\$zipcord">
            <INPUT TYPE="hidden" NAME="address" VALUE="\$address">
            <INPUT TYPE="hidden" NAME="tel" VALUE="\$tel">
            <INPUT TYPE="hidden" NAME="fullname" VALUE="\$fullname">
            <INPUT TYPE="hidden" NAME="familyname" VALUE="">
            <INPUT TYPE="hidden" NAME="brthday" VALUE="">
            <INPUT TYPE="hidden" NAME="user" VALUE="">
            <INPUT TYPE="hidden" NAME="brother" VALUE="">
            <INPUT TYPE="hidden" NAME="request" VALUE="">
            <INPUT TYPE="hidden" NAME="exp" VALUE="">
            <INPUT TYPE="hidden" NAME="kgak" VALUE="\$kgak">
            <CENTER><INPUT TYPE=submit NAME="����" VALUE="��ʸ"></CENTER>
         </FORM></P></CENTER>
      </TD>
   </TR>
</TABLE>
</P>
</BODY>
</HTML>

ORDER120
&jcode'convert(*msg, "sjis", "euc");
	$msg =~ s/\$name/$name/g;
	$msg =~ s/\$email/$email/g;
	$msg =~ s/\$order1/$order1/g;
	$msg =~ s/\$order2/$order2/g;	
	$msg =~ s/\$zipcord/$zipcord/g;
	$msg =~ s/\$address/$address/g;
	$msg =~ s/\$tel/$tel/g;
	$msg =~ s/\$fullname/$fullname/g;
    $msg =~ s/\$kgak/$kgak/g;
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
         <CENTER><FONT SIZE="+3"><B><U>����ʸ���ƤΤ���ǧ</U></B></FONT></CENTER>
         
         <BLOCKQUOTE>���β��̤ϡ�����ʸ���Ƥ򤴳�ǧĺ������Τ�ΤǤ������Ƥ˸�꤬������ϡ��֥饦���Ρ����ץܥ���򲡤��Ǝ����ϥե����������齤�����Ʋ�����������ǵ�������С���ʸ�ץܥ���򲡤��Ʋ�������</BLOCKQUOTE>
         
         <CENTER><B>����ʸ����</B><BR>
         <TABLE BORDER=1 WIDTH="90%">
   <TR>
      <TD WIDTH=148>
         <P>�������(����)�Τ�̾��</P>
      </TD>
      <TD>
         <P>\$name</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>������ԤΥ᡼�륢�ɥ쥹</P>
      </TD>
      <TD>
         <P>\$email</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>�����������</P>
      </TD>
      <TD>
         <P>���ܲ�������(�Ż���)����ʸ����������̿̾����</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>������礵�ޤξ���<BR>
         (���ޤ������Τ�)</P>
      </TD>
      <TD>
         <P><TABLE BORDER=1>
            <TR>
               <TD WIDTH=64>
                  <P>͹���ֹ�</P>
               </TD>
               <TD>
                  <P>\$zipcord</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=64>
                  <P>����</P>
               </TD>
               <TD>
                  <P>\$address</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=64>
                  <P>�������ֹ�</P>
               </TD>
               <TD>
                  <P>\$tel</P>
               </TD>
            </TR>
         </TABLE>
         </P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>��������̿̾����</P>
      </TD>
      <TD>
         <P><TABLE BORDER=1>
            <TR>
               <TD WIDTH=90>
                  <P>��(�Ļ�)</P>
               </TD>
               <TD>
                  <P>\$familyname</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=90>
                  <P>������(ͽ����)</P>
               </TD>
               <TD>
                  <P>\$brthday</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=90>
                  <P>���Τ�����</P>
               </TD>
               <TD>
                  <P>\$user</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=90>
                  <P>������Τ�̾��</P>
               </TD>
               <TD>
                  <P>\$brother</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=90>
                  <P>����˾����</P>
               </TD>
               <TD>
                  <P>\$request</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=90>
                  <P>�õ�����</P>
               </TD>
               <TD>
                  <P>\$exp</P>
               </TD>
            </TR>
         </TABLE>
         </P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>��פ���ʧ�����</P>
      </TD>
      <TD>
         <P>\$kgak ��</P>
      </TD>
   </TR>
         </TABLE>
</CENTER>
         
         <BLOCKQUOTE>
            <B>����ǧ���Ѥߤޤ�����</B><FONT COLOR="#FF0000"><B>��������ʸ���ܥ����1����������Ƥ�ȯ��</B></FONT><B>�����������Ƕᡢ�᡼�륢�ɥ쥹�δְ㤤��¿���褦�Ǥ����᡼�륢�ɥ쥹��⤦���١�����ǧ��������<BR>
            �ʤ������ʤ����ʾ塢����ʹߤΤ���ʸ�μ��ä������ʤϰ��ڽ���ޤ���Τ�ͽ�ᤴλ����������(ˬ������ˡ�Υ�����󥰥��դ�Ŭ�Ѥ���ޤ��󡣡�</B></BLOCKQUOTE>
         
         <CENTER>����ʸ�������ϡ��֥饦���Ύ���뎣�ǎ����ϥե�������������ľ���Ʋ�������</CENTER>
         
         <P><FORM ACTION="/~kazu-y/cgi_bin2/nn_mail.cgi" METHOD=POST>
            <P><INPUT TYPE="hidden" NAME="name" VALUE="\$name">
            <INPUT TYPE="hidden" NAME="email" VALUE="\$email">
            <INPUT TYPE="hidden" NAME="order1" VALUE="\$order1">
            <INPUT TYPE="hidden" NAME="order2" VALUE="">
            <INPUT TYPE="hidden" NAME="order3" VALUE="\$order3">
            <INPUT TYPE="hidden" NAME="zipcord" VALUE="\$zipcord">
            <INPUT TYPE="hidden" NAME="address" VALUE="\$address">
            <INPUT TYPE="hidden" NAME="tel" VALUE="\$tel">
            <INPUT TYPE="hidden" NAME="fullname" VALUE="">
            <INPUT TYPE="hidden" NAME="familyname" VALUE="\$familyname">
            <INPUT TYPE="hidden" NAME="brthday" VALUE="\$brthday">
            <INPUT TYPE="hidden" NAME="user" VALUE="\$user">
            <INPUT TYPE="hidden" NAME="brother" VALUE="\$brother">
            <INPUT TYPE="hidden" NAME="request" VALUE="\$request">
            <INPUT TYPE="hidden" NAME="exp" VALUE="\$exp">
            <INPUT TYPE="hidden" NAME="kgak" VALUE="\$kgak">
            <CENTER><INPUT TYPE=submit NAME="����" VALUE="��ʸ"></CENTER>
         </FORM></P></CENTER>
      </TD>
   </TR>
</TABLE>
</P>
</BODY>
</HTML>

ORDER103
&jcode'convert(*msg, "sjis", "euc");
	$msg =~ s/\$name/$name/g;
	$msg =~ s/\$email/$email/g;
	$msg =~ s/\$order1/$order1/g;	
	$msg =~ s/\$order3/$order3/g;	
	$msg =~ s/\$zipcord/$zipcord/g;
	$msg =~ s/\$address/$address/g;
	$msg =~ s/\$tel/$tel/g;
	$msg =~ s/\$familyname/$familyname/g;
	$msg =~ s/\$brthday/$brthday/g;
	$msg =~ s/\$user/$user/g;
	$msg =~ s/\$brother/$brother/g;
	$msg =~ s/\$request/$request/g;
	$msg =~ s/\$exp/$exp/g;
	$msg =~ s/\$kgak/$kgak/g;
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
         <CENTER><FONT SIZE="+3"><B><U>����ʸ���ƤΤ���ǧ</U></B></FONT></CENTER>
         
         <BLOCKQUOTE>���β��̤ϡ�����ʸ���Ƥ򤴳�ǧĺ������Τ�ΤǤ������Ƥ˸�꤬������ϡ��֥饦���Ρ����ץܥ���򲡤��Ǝ����ϥե����������齤�����Ʋ�����������ǵ�������С���ʸ�ץܥ���򲡤��Ʋ�������</BLOCKQUOTE>
         
         <CENTER><B>����ʸ����</B><BR>
         <TABLE BORDER=1 WIDTH="80%">
  <TR>
      <TD WIDTH=148>
         <P>�������(����)�Τ�̾��</P>
      </TD>
      <TD>
         <P>\$name</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>������ԤΥ᡼�륢�ɥ쥹</P>
      </TD>
      <TD>
         <P>\$email</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>�����������</P>
      </TD>
      <TD>
         <P>���ܲ�������(����)����ʸ����������̿̾����</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>���ҤΤ�������</P>
      </TD>
      <TD>
         <P><TABLE BORDER=1>
            <TR>
               <TD WIDTH=55>
                  <P>͹���ֹ�</P>
               </TD>
               <TD>
                  <P>\$zipcord</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=55>
                  <P>����</P>
               </TD>
               <TD>
                  <P>\$address</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=55>
                  <P>�������</P>
               </TD>
               <TD>
                  <P>\$fullname</P>
               </TD>
            </TR>
         </TABLE>
         </P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>��Ϣ���褪�����ֹ�</P>
      </TD>
      <TD>
         <P>\$tel</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>��������̿̾����</P>
      </TD>
      <TD>
         <P><TABLE BORDER=1>
            <TR>
               <TD WIDTH=92>
                  <P>��(�Ļ�)</P>
               </TD>
               <TD>
                  <P>\$familyname</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=92>
                  <P>������(ͽ����)</P>
               </TD>
               <TD>
                  <P>\$brthday</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=92>
                  <P>���Τ�����</P>
               </TD>
               <TD>
                  <P>\$user</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=92>
                  <P>������Τ�̾��</P>
               </TD>
               <TD>
                  <P>\$brother</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=92>
                  <P>����˾����</P>
               </TD>
               <TD>
                  <P>\$request</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=92>
                  <P>�õ�����</P>
               </TD>
               <TD>
                  <P>\$exp</P>
               </TD>
            </TR>
         </TABLE>
         </P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>��פ���ʧ�����</P>
      </TD>
      <TD>
         <P>\$kgak ��</P>
      </TD>
   </TR>
         </TABLE>
        </CENTER>
         
         <BLOCKQUOTE>
            <B>����ǧ���Ѥߤޤ�����</B><FONT COLOR="#FF0000"><B>��������ʸ���ܥ����1����������Ƥ�ȯ��</B></FONT><B>����������<BR>
            �ʤ������ʤ����ʾ塢����ʹߤΤ���ʸ�μ��ä������ʤϰ��ڽ���ޤ���Τ�ͽ�ᤴλ����������(ˬ������ˡ�Υ�����󥰥��դ�Ŭ�Ѥ���ޤ��󡣡�</B></BLOCKQUOTE>
         
         <CENTER>����ʸ�������ϡ��֥饦���Ύ���뎣�ǎ����ϥե�������������ľ���Ʋ�������</CENTER>
         
         <P><FORM ACTION="/~kazu-y/cgi_bin2/nn_mail.cgi" METHOD=POST>
            <P><INPUT TYPE="hidden" NAME="name" VALUE="\$name">
            <INPUT TYPE="hidden" NAME="email" VALUE="\$email">
            <INPUT TYPE="hidden" NAME="order1" VALUE="">
            <INPUT TYPE="hidden" NAME="order2" VALUE="\$order2">
            <INPUT TYPE="hidden" NAME="order3" VALUE="\$order3">
            <INPUT TYPE="hidden" NAME="zipcord" VALUE="\$zipcord">
            <INPUT TYPE="hidden" NAME="address" VALUE="\$address">
            <INPUT TYPE="hidden" NAME="tel" VALUE="\$tel">
            <INPUT TYPE="hidden" NAME="fullname" VALUE="\$fullname">
            <INPUT TYPE="hidden" NAME="familyname" VALUE="\$familyname">
            <INPUT TYPE="hidden" NAME="brthday" VALUE="\$brthday">
            <INPUT TYPE="hidden" NAME="user" VALUE="\$user">
            <INPUT TYPE="hidden" NAME="brother" VALUE="\$brother">
            <INPUT TYPE="hidden" NAME="request" VALUE="\$request">
            <INPUT TYPE="hidden" NAME="exp" VALUE="\$exp">
            <INPUT TYPE="hidden" NAME="kgak" VALUE="\$kgak">
            <CENTER><INPUT TYPE=submit NAME="����" VALUE="��ʸ"></CENTER>
         </FORM></P></CENTER>
      </TD>
   </TR>
</TABLE>
</P>
</BODY>
</HTML>

ORDER023
&jcode'convert(*msg, "sjis", "euc");
	$msg =~ s/\$name/$name/g;
	$msg =~ s/\$email/$email/g;
	$msg =~ s/\$order2/$order2/g;	
	$msg =~ s/\$order3/$order3/g;	
	$msg =~ s/\$zipcord/$zipcord/g;
	$msg =~ s/\$address/$address/g;
	$msg =~ s/\$tel/$tel/g;
	$msg =~ s/\$fullname/$fullname/g;
	$msg =~ s/\$familyname/$familyname/g;
	$msg =~ s/\$brthday/$brthday/g;
	$msg =~ s/\$user/$user/g;
	$msg =~ s/\$brother/$brother/g;
	$msg =~ s/\$request/$request/g;
	$msg =~ s/\$exp/$exp/g;
	$msg =~ s/\$kgak/$kgak/g;
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
<CENTER><FONT SIZE="+3"><B><U>����ʸ���ƤΤ���ǧ</U></B></FONT></CENTER>
         
         <BLOCKQUOTE>���β��̤ϡ�����ʸ���Ƥ򤴳�ǧĺ������Τ�ΤǤ������Ƥ˸�꤬������ϡ��֥饦���Ρ����ץܥ���򲡤��Ǝ����ϥե����������齤�����Ʋ�����������ǵ�������С���ʸ�ץܥ���򲡤��Ʋ�������</BLOCKQUOTE>
         
         <CENTER><B>����ʸ����</B><BR>
         <TABLE BORDER=1 WIDTH="90%">
   <TR>
      <TD WIDTH=148>
         <P>�������(����)�Τ�̾��</P>
      </TD>
      <TD>
         <P>\$name</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>������ԤΥ᡼�륢�ɥ쥹</P>
      </TD>
      <TD>
         <P>\$email</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>�����������</P>
      </TD>
      <TD>
         <P>���ܲ�������(�Ż���)����ʸ</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>��פ���ʧ�����</P>
      </TD>
      <TD>
         <P>\$kgak ��</P>
      </TD>
   </TR>
         </TABLE>
</CENTER>
         
         <BLOCKQUOTE>
            <B>����ǧ���Ѥߤޤ�����</B><FONT COLOR="#FF0000"><B>��������ʸ���ܥ����1����������Ƥ�ȯ��</B></FONT><B>�����������Ƕᡢ�᡼�륢�ɥ쥹�δְ㤤��¿���褦�Ǥ����᡼�륢�ɥ쥹��⤦���١�����ǧ��������<BR>
            �ʤ������ʤ����ʾ塢����ʹߤΤ���ʸ�μ��ä������ʤϰ��ڽ���ޤ���Τ�ͽ�ᤴλ����������(ˬ������ˡ�Υ�����󥰥��դ�Ŭ�Ѥ���ޤ��󡣡�</B></BLOCKQUOTE>
         
         <CENTER>����ʸ�������ϡ��֥饦���Ύ���뎣�ǎ����ϥե�������������ľ���Ʋ�������</CENTER>
         
         <P><FORM ACTION="/~kazu-y/cgi_bin2/nn_mail.cgi" METHOD=POST>
            <P><INPUT TYPE="hidden" NAME="name" VALUE="\$name">
            <INPUT TYPE="hidden" NAME="email" VALUE="\$email">
            <INPUT TYPE="hidden" NAME="order1" VALUE="\$order1">
            <INPUT TYPE="hidden" NAME="order2" VALUE="">
            <INPUT TYPE="hidden" NAME="order3" VALUE="">
            <INPUT TYPE="hidden" NAME="zipcord" VALUE="">
            <INPUT TYPE="hidden" NAME="address" VALUE="">
            <INPUT TYPE="hidden" NAME="tel" VALUE="">
            <INPUT TYPE="hidden" NAME="fullname" VALUE="">
            <INPUT TYPE="hidden" NAME="familyname" VALUE="">
            <INPUT TYPE="hidden" NAME="brthday" VALUE="">
            <INPUT TYPE="hidden" NAME="user" VALUE="">
            <INPUT TYPE="hidden" NAME="brother" VALUE="">
            <INPUT TYPE="hidden" NAME="request" VALUE="">
            <INPUT TYPE="hidden" NAME="exp" VALUE="">
            <INPUT TYPE="hidden" NAME="kgak" VALUE="\$kgak">
            <CENTER><INPUT TYPE=submit NAME="����" VALUE="��ʸ"></CENTER>
         </FORM></P></CENTER>
      </TD>
   </TR>
</TABLE>
</P>
</BODY>
</HTML>

ORDER100
&jcode'convert(*msg, "sjis", "euc");
	$msg =~ s/\$name/$name/g;
	$msg =~ s/\$email/$email/g;
	$msg =~ s/\$order1/$order1/g;
	$msg =~ s/\$kgak/$kgak/g;
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
 <CENTER><FONT SIZE="+3"><B><U>����ʸ���ƤΤ���ǧ</U></B></FONT></CENTER>
         
         <BLOCKQUOTE>���β��̤ϡ�����ʸ���Ƥ򤴳�ǧĺ������Τ�ΤǤ������Ƥ˸�꤬������ϡ��֥饦���Ρ����ץܥ���򲡤��Ǝ����ϥե����������齤�����Ʋ�����������ǵ�������С���ʸ�ץܥ���򲡤��Ʋ�������</BLOCKQUOTE>
         
         <CENTER><B>����ʸ����</B><BR>
         <TABLE BORDER=1 WIDTH="90%">
   <TR>
      <TD WIDTH=148>
         <P>�������(����)�Τ�̾��</P>
      </TD>
      <TD>
         <P>\$name</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>������ԤΥ᡼�륢�ɥ쥹</P>
      </TD>
      <TD>
         <P>\$email</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>�����������</P>
      </TD>
      <TD>
         <P>���ܲ�������(����)����ʸ</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>���ҤΤ�������</P>
      </TD>
      <TD>
         <P><TABLE BORDER=1>
            <TR>
               <TD WIDTH=55>
                  <P>͹���ֹ�</P>
               </TD>
               <TD>
                  <P>\$zipcord</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=55>
                  <P>����</P>
               </TD>
               <TD>
                  <P>\$address</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=55>
                  <P>�������</P>
               </TD>
               <TD>
                  <P>\$fullname</P>
               </TD>
            </TR>
         </TABLE>
         </P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>��Ϣ���褪�����ֹ�</P>
      </TD>
      <TD>
         <P>\$tel</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>��פ���ʧ�����</P>
      </TD>
      <TD>
         <P>\$kgak ��</P>
      </TD>
   </TR>
         </TABLE>
</CENTER>
         
         <BLOCKQUOTE>
            <B>����ǧ���Ѥߤޤ�����</B><FONT COLOR="#FF0000"><B>��������ʸ���ܥ����1����������Ƥ�ȯ��</B></FONT><B>����������<BR>
            �ʤ������ʤ����ʾ塢����ʹߤΤ���ʸ�μ��ä������ʤϰ��ڽ���ޤ���Τ�ͽ�ᤴλ����������(ˬ������ˡ�Υ�����󥰥��դ�Ŭ�Ѥ���ޤ��󡣡�</B></BLOCKQUOTE>
         
         <CENTER>����ʸ�������ϡ��֥饦���Ύ���뎣�ǎ����ϥե�������������ľ���Ʋ�������</CENTER>
         
         <P><FORM ACTION="/~kazu-y/cgi_bin2/nn_mail.cgi" METHOD=POST>
            <P><INPUT TYPE="hidden" NAME="name" VALUE="\$name">
            <INPUT TYPE="hidden" NAME="email" VALUE="\$email">
            <INPUT TYPE="hidden" NAME="order1" VALUE="">
            <INPUT TYPE="hidden" NAME="order2" VALUE="\$order2">
            <INPUT TYPE="hidden" NAME="order3" VALUE="">
            <INPUT TYPE="hidden" NAME="zipcord" VALUE="\$zipcord">
            <INPUT TYPE="hidden" NAME="address" VALUE="\$address">
            <INPUT TYPE="hidden" NAME="tel" VALUE="\$tel">
            <INPUT TYPE="hidden" NAME="fullname" VALUE="\$fullname">
            <INPUT TYPE="hidden" NAME="familyname" VALUE="">
            <INPUT TYPE="hidden" NAME="brthday" VALUE="">
            <INPUT TYPE="hidden" NAME="user" VALUE="">
            <INPUT TYPE="hidden" NAME="brother" VALUE="">
            <INPUT TYPE="hidden" NAME="request" VALUE="">
            <INPUT TYPE="hidden" NAME="exp" VALUE="">
            <INPUT TYPE="hidden" NAME="kgak" VALUE="\$kgak">
            <CENTER><INPUT TYPE=submit NAME="����" VALUE="��ʸ"></CENTER>
         </FORM></P></CENTER>
      </TD>
   </TR>
</TABLE>
</P>
</BODY>
</HTML>

ORDER020
&jcode'convert(*msg, "sjis", "euc");
	$msg =~ s/\$name/$name/g;
	$msg =~ s/\$email/$email/g;
	$msg =~ s/\$order2/$order2/g;		
	$msg =~ s/\$zipcord/$zipcord/g;
	$msg =~ s/\$address/$address/g;
	$msg =~ s/\$tel/$tel/g;
	$msg =~ s/\$fullname/$fullname/g;
    $msg =~ s/\$kgak/$kgak/g;
	print $msg;
}
###########̿̾�Τ߰���############
elsif ($order3 ne "")  {
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
        <CENTER><FONT SIZE="+3"><B><U>����ʸ���ƤΤ���ǧ</U></B></FONT></CENTER>
         
         <BLOCKQUOTE>���β��̤ϡ�����ʸ���Ƥ򤴳�ǧĺ������Τ�ΤǤ������Ƥ˸�꤬������ϡ��֥饦���Ρ����ץܥ���򲡤��Ǝ����ϥե����������齤�����Ʋ�����������ǵ�������С���ʸ�ץܥ���򲡤��Ʋ�������</BLOCKQUOTE>
         
         <CENTER><B>����ʸ����</B><BR>
         <TABLE BORDER=1 WIDTH="90%">
   <TR>
      <TD WIDTH=148>
         <P>�������(����)�Τ�̾��</P>
      </TD>
      <TD>
         <P>\$name</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>������ԤΥ᡼�륢�ɥ쥹</P>
      </TD>
      <TD>
         <P>\$email</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>�����������</P>
      </TD>
      <TD>
         <P>��������̿̾����</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>������礵�ޤξ���<BR>
         (���ޤ������Τ�)</P>
      </TD>
      <TD>
         <P><TABLE BORDER=1>
            <TR>
               <TD WIDTH=64>
                  <P>͹���ֹ�</P>
               </TD>
               <TD>
                  <P>\$zipcord</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=64>
                  <P>����</P>
               </TD>
               <TD>
                  <P>\$address</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=64>
                  <P>�������ֹ�</P>
               </TD>
               <TD>
                  <P>\$tel</P>
               </TD>
            </TR>
         </TABLE>
         </P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>��������̿̾����</P>
      </TD>
      <TD>
         <P><TABLE BORDER=1>
            <TR>
               <TD WIDTH=90>
                  <P>��(�Ļ�)</P>
               </TD>
               <TD>
                  <P>\$familyname</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=90>
                  <P>������(ͽ����)</P>
               </TD>
               <TD>
                  <P>\$brthday</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=90>
                  <P>���Τ�����</P>
               </TD>
               <TD>
                  <P>\$user</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=90>
                  <P>������Τ�̾��</P>
               </TD>
               <TD>
                  <P>\$brother</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=90>
                  <P>����˾����</P>
               </TD>
               <TD>
                  <P>\$request</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=90>
                  <P>�õ�����</P>
               </TD>
               <TD>
                  <P>\$exp</P>
               </TD>
            </TR>
         </TABLE>
         </P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>��פ���ʧ�����</P>
      </TD>
      <TD>
         <P>\$kgak ��</P>
      </TD>
   </TR>
         </TABLE>
</CENTER>
         
         <BLOCKQUOTE>
            <B>����ǧ���Ѥߤޤ�����</B><FONT COLOR="#FF0000"><B>��������ʸ���ܥ����1����������Ƥ�ȯ��</B></FONT><B>�����������Ƕᡢ�᡼�륢�ɥ쥹�δְ㤤��¿���褦�Ǥ����᡼�륢�ɥ쥹��⤦���١�����ǧ��������<BR>
            �ʤ������ʤ����ʾ塢����ʹߤΤ���ʸ�μ��ä������ʤϰ��ڽ���ޤ���Τ�ͽ�ᤴλ����������(ˬ������ˡ�Υ�����󥰥��դ�Ŭ�Ѥ���ޤ��󡣡�</B></BLOCKQUOTE>
         
         <CENTER>����ʸ�������ϡ��֥饦���Ύ���뎣�ǎ����ϥե�������������ľ���Ʋ�������</CENTER>
         
         <P><FORM ACTION="/~kazu-y/cgi_bin2/nn_mail.cgi" METHOD=POST>
            <P><INPUT TYPE="hidden" NAME="name" VALUE="\$name">
            <INPUT TYPE="hidden" NAME="email" VALUE="\$email">
            <INPUT TYPE="hidden" NAME="order1" VALUE="">
            <INPUT TYPE="hidden" NAME="order2" VALUE="">
            <INPUT TYPE="hidden" NAME="order3" VALUE="\$order3">
            <INPUT TYPE="hidden" NAME="zipcord" VALUE="\$zipcord">
            <INPUT TYPE="hidden" NAME="address" VALUE="\$address">
            <INPUT TYPE="hidden" NAME="tel" VALUE="\$tel">
            <INPUT TYPE="hidden" NAME="fullname" VALUE="">
            <INPUT TYPE="hidden" NAME="familyname" VALUE="\$familyname">
            <INPUT TYPE="hidden" NAME="brthday" VALUE="\$brthday">
            <INPUT TYPE="hidden" NAME="user" VALUE="\$user">
            <INPUT TYPE="hidden" NAME="brother" VALUE="\$brother">
            <INPUT TYPE="hidden" NAME="request" VALUE="\$request">
            <INPUT TYPE="hidden" NAME="exp" VALUE="\$exp">
            <INPUT TYPE="hidden" NAME="kgak" VALUE="\$kgak">
            <CENTER><INPUT TYPE=submit NAME="����" VALUE="��ʸ"></CENTER>
         </FORM></P></CENTER>
      </TD>
   </TR>
</TABLE>
</P>
</BODY>
</HTML>

ORDER003
&jcode'convert(*msg, "sjis", "euc");
	$msg =~ s/\$name/$name/g;
	$msg =~ s/\$email/$email/g;	
	$msg =~ s/\$order3/$order3/g;	
	$msg =~ s/\$zipcord/$zipcord/g;
	$msg =~ s/\$address/$address/g;
	$msg =~ s/\$tel/$tel/g;
	$msg =~ s/\$familyname/$familyname/g;
	$msg =~ s/\$brthday/$brthday/g;
	$msg =~ s/\$user/$user/g;
	$msg =~ s/\$brother/$brother/g;
	$msg =~ s/\$request/$request/g;
	$msg =~ s/\$exp/$exp/g;
	$msg =~ s/\$kgak/$kgak/g;
	print $msg;
}
__end__
