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
######$B%G!<%?$N<h$j9~$_(B#######
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

######$BF~NO$5$l$?%G!<%?$N%A%'%C%/(B######
if ($member =~ /^\s*$/) {
	&CgiError("NET-U$B2q0wHV9f$,F~NO$5$l$F$$$^$;$s!#(B",
	"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
	exit;
}
if ($KMEI =~ /^\s*$/) {
	&CgiError("$B$*5RMM$N$*L>A0$N5-F~$,$"$j$^$;$s!#(B",
	"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
	exit;
}
if (($order1 eq "" ) and ($order2 eq "" ) and ($order3 eq ""))  {
	&CgiError("$BF~NO%(%i!<(B",
		"$B$4CmJ8$,2?$b;X<($5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
	exit;
}	
if ($order2 ne "") {
	if ($SPOST eq "") {
		&CgiError("$BM9JXHV9f$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
	elsif ($SADR eq "") {
		&CgiError("$B=;=j$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}	
	elsif ($SMEI eq "") {
		&CgiError("$B<u<h?M$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
}
if ($order3 ne "") {
	if ($familyname eq "") {
		&CgiError("$BID;z(B($B@+(B)$B$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
	elsif ($brthday eq "") {
		&CgiError("$BM=DjF|(B($BCB@8F|(B)$B$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
}

######$B%a!<%k%"%I%l%9$N%A%'%C%/(B######
if ($KMAIL =~ /^\s*$/){
	&CgiError("$B%a!<%k%"%I%l%9$N5-F~$,$"$j$^$;$s!#(B",
	"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
	exit;
}
elsif (($KMAIL) and (not $KMAIL =~ /.+\@.+\..+/)) {
	&CgiError("$BF~NO%(%i!<(B",
		"$B%a!<%k%"%I%l%9$N=q$-J}$,4V0c$C$F$$$^$9!#(B",$KMAIL,
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
	exit;
}
elsif (($hostname = $KMAIL) =~ s/.+\@(\S+)/$1/) {
	($hname,$aliases,$addresstype, $length,@address) =
		gethostbyname $hostname;
	if (not $hname) {
		&CgiError("$B%a!<%k%[%9%H%(%i!<(B",
		"$B%a!<%k%"%I%l%9$,3NG'$G$-$^$;$s$G$7$?!#(B");
		exit;
	}
}

######$BF~NO%G!<%?$N@07A=hM}(B######
$member =~ s/\s*//g;
if ($SPOST ne "") {
	$SPOST =~ s/\s*//g;
	#$BA43Q1Q?t;z$r$9$Y$FH>3Q1Q?t;z$K$9$k!#(B
	$SPOST = &zen2han($SPOST); 
	#$BM9JXHV9f$,(B7$B7e0J2<$GF~NO$5$l$?>l9g!"(B00$B$rKvHx$KIU2C$9$k!#(B
	$SPOST = $SPOST . "00000000";
	$SPOST = substr($SPOST, 0, 8);
}
if ($STEL ne "") {
	$STEL =~ s/\s*//g;
	#$BA43Q1Q?t;z$r$9$Y$FH>3Q1Q?t;z$K$9$k!#(B
	$STEL = &zen2han($STEL); 
}
if ($familyname ne "") {
	$familyname =~ s/\s*//g;
}
if ($brthday ne "") {
	$brthday =~ s/\s*//g;
}

######P$B%l%8<uIUHV9f$N@8@.(B######
$countfile = "count.txt";
open COUNTER,"$countfile"
	or &CgiError("$countfile $B%*!<%W%s<:GT(B1\n");
$SJNO = <COUNTER>;
close COUNTER;

++$SJNO;

open COUNTER,">$countfile"
	or &CgiError("$countfile $B%*!<%W%s<:GT(B2\n");
print COUNTER $SJNO;
close COUNTER;

######$B2'$X$N$4CmJ8%a!<%k$NAw?.(B######
$com = <<MESSAGE;
From: $KMAIL
Subject: $B;3K\2'$X$N$4CmJ8(B(NET-U$B2q0w(B)

=====================================
$B#P%l%8<uIUHV9f!'(B
$SJNO
$B?=9~?MMM$N;aL>!'(B
$KMEI
$B?=9~?MMM$N(BE$B%a!<%k%"%I%l%9!'(B
$KMAIL
$B$4CmJ8FbMF!'(B
$order1
$order2
$order3

$B=q@R$NAwIU@h$^$?$OO"Mm@h(B
$BM9JXHV9f!'(B
$SPOST
$B$4=;=j!'(B
$SADR
$B$*EEOCHV9f!'(B
$STEL
$B<u<h?MMM!'(B
$SMEI

$BL?L>$N$40MMjFbMF(B
$B@+(B($B$_$g$&$8(B)$B!'(B
$familyname
$B=P;:M=DjF|!'(B
$brthday
$B:#$^$G$NMxMQ!'(B
$user
$B7;;P$N$*L>A0!'(B
$brother
$B$4MWK>;v9`!'(B
$request

=====================================
MESSAGE

&jcode'convert(*com,"jis");
open(MAIL, "|$sendmail $youraddress");
print MAIL $com;
close(MAIL);

######$B$3$3$+$i0z$-7Q$.>pJs$N@8@.$HI=<(2hLL(B######
######$BEE;RK\!"=q@R!"L?L>$N(B3$B$D$rCmJ8(B#######
if (($order1 ne "") and ($order2 ne "") and ($order3 ne ""))  {
	$msg = <<"ORDER123";
Content-type: text/html

<HTML>
<HEAD>
   <TITLE>$BEE;RK\$H=q@R$N$4CmJ8!&L?L>$N$40MMj(B</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=x-sjis">
</HEAD>
<BODY BGCOLOR="#FFFFFF" BACKGROUND="/~kazu-y/image/wall.jpg">
<P><TABLE BORDER=0 CELLSPACING=0 CELLPADDING=0 WIDTH=640>
   <TR>
      <TD>
         <CENTER><FONT SIZE="+3"><B><U>$B$4CmJ8M-Fq$&$4$6$$$^$9!#(B</U></B></FONT>
         
         <P><FONT COLOR="#FF0000"><B>$B0z$-B3$-(BNET-U$B%+!<%I$N7h:Q$r9T$C$F$$$?$@$-$^$9!#(B</B></FONT></P>
         
         <P>$B$4CmJ8FbMF$N$43NG'(B<BR>
         <TABLE BORDER=1 WIDTH="80%">
            <TR>
               <TD>
                  <CENTER>$B$4CmJ8FbMF(B</CENTER>
               </TD>
               <TD>
                  <CENTER>$BBe6b(B($B>CHq@G9~$_(B)</CENTER>
               </TD>
               <TD>
                  <CENTER>$BHw9M(B</CENTER>
               </TD>
            </TR>
            <TR>
               <TD>
                  <P>1.$B!V;3K\2'$NEE;RK\!W$r9XF~(B</P>
               </TD>
               <TD>
                  <P ALIGN=right>500$B1_(B</P>
               </TD>
               <TD>
                  <P ALIGN=right>$B%Q%9%o!<%IBe6b(B</P>
               </TD>
            </TR>
            <TR>
               <TD>
                  <P>2.$B!V;3K\2'$NCx=q!W$r9XF~(B</P>
               </TD>
               <TD>
                  <P ALIGN=right>1,810$B1_(B</P>
               </TD>
               <TD>
                  <P ALIGN=right>$BAwNA(B310$B1_9~$_(B</P>
               </TD>
            </TR>
            <TR>
               <TD>
                  <P>3.$B!V?7@8;y$NL?L>!W$r0MMj(B</P>
               </TD>
               <TD>
                  <P ALIGN=right>10,000$B1_(B</P>
               </TD>
               <TD>
                  <P></P>
               </TD>
            </TR>
            <TR>
               <TD>
                  <P ALIGN=right>$B9g7W9XF~6b3[(B</P>
               </TD>
               <TD>
                  <P ALIGN=right>12,310$B1_(B</P>
               </TD>
               <TD>
                  <P></P>
               </TD>
            </TR>
         </TABLE>
         
         <B>$B$43NG'$,:Q$_$^$7$?$i(B</B><FONT COLOR="#FF0000"><B>$B2<5-!VAw?.!W%\%?%s$r(B1$B2s$@$12!$7$F(B</B></FONT><B>$B$/$@$5$$!#(B<BR>
         $B$7$P$i$/$*BT$AD:$1$l$P!"(BNET-U$B%+!<%I$N7h:Q2hLL$KJQ$o$j$^$9!#(B</B></P>
         
         <P>$B$4CmJ8$ND{@5$O!"%V%i%&%6$N!VLa$k!W$G!VF~NO%U%)!<%`!W$+$i$d$jD>$7$F2<$5$$!#(B</P>
         
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
            <CENTER><INPUT TYPE=submit NAME="$BAw?.(B" VALUE="$BAw?.(B"></CENTER>
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
#######$BEE;RK\$H=q@R$rCmJ8(B##########
elsif (($order1 ne "") and ($order2 ne ""))  {
	$msg = <<"ORDER120";
Content-type: text/html

<HTML>
<HEAD>
   <TITLE>$BEE;RK\$H=q@R$N$4CmJ8(B</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=x-sjis">
</HEAD>
<BODY BGCOLOR="#FFFFFF" BACKGROUND="/~kazu-y/image/wall.jpg">
<P><TABLE BORDER=0 CELLSPACING=0 CELLPADDING=0 WIDTH=640>
   <TR>
      <TD>
         <CENTER><FONT SIZE="+3"><B><U>$B$4CmJ8M-Fq$&$4$6$$$^$9!#(B</U></B></FONT>
         
         <P><FONT COLOR="#FF0000"><B>$B0z$-B3$-(BNET-U$B%+!<%I$N7h:Q$r9T$C$F$$$?$@$-$^$9!#(B</B></FONT></P>
         
         <P>$B$4CmJ8FbMF$N$43NG'(B<BR>
         <TABLE BORDER=1 WIDTH="80%">
            <TR>
               <TD>
                  <CENTER>$B$4CmJ8FbMF(B</CENTER>
               </TD>
               <TD>
                  <CENTER>$BBe6b(B($B>CHq@G9~$_(B)</CENTER>
               </TD>
               <TD>
                  <CENTER>$BHw9M(B</CENTER>
               </TD>
            </TR>
            <TR>
               <TD>
                  <P>1.$B!V;3K\2'$NEE;RK\!W$r9XF~(B</P>
               </TD>
               <TD>
                  <P ALIGN=right>500$B1_(B</P>
               </TD>
               <TD>
                  <P ALIGN=right>$B%Q%9%o!<%IBe6b(B</P>
               </TD>
            </TR>
            <TR>
               <TD>
                  <P>2.$B!V;3K\2'$NCx=q!W$r9XF~(B</P>
               </TD>
               <TD>
                  <P ALIGN=right>1,810$B1_(B</P>
               </TD>
               <TD>
                  <P ALIGN=right>$BAwNA(B310$B1_9~$_(B</P>
               </TD>
            </TR>
            <TR>
               <TD>
                  <P ALIGN=right>$B9g7W9XF~6b3[(B</P>
               </TD>
               <TD>
                  <P ALIGN=right>2,310$B1_(B</P>
               </TD>
               <TD>
                  <P></P>
               </TD>
            </TR>
         </TABLE>
         
         <B>$B$43NG'$,:Q$_$^$7$?$i(B</B><FONT COLOR="#FF0000"><B>$B2<5-!VAw?.!W%\%?%s$r(B1$B2s$@$12!$7$F(B</B></FONT><B>$B$/$@$5$$!#(B<BR>
         $B$7$P$i$/$*BT$AD:$1$l$P!"(BNET-U$B%+!<%I$N7h:Q2hLL$KJQ$o$j$^$9!#(B</B></P>
         
         <P>$B$4CmJ8$ND{@5$O!"%V%i%&%6$N!VLa$k!W$G!VF~NO%U%)!<%`!W$+$i$d$jD>$7$F2<$5$$!#(B</P>
         
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
            
            <CENTER><INPUT TYPE=submit NAME="$BAw?.(B" VALUE="$BAw?.(B"></CENTER>
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
########$BEE;RK\$NCmJ8$HL?L>$N0MMj(B###########
elsif (($order1 ne "") and ($order3 ne ""))  {
	$msg = <<"ORDER103";
Content-type: text/html

<HTML>
<HEAD>
   <TITLE>$BEE;RK\$N$4CmJ8!&L?L>$N$40MMj(B</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=x-sjis">
</HEAD>
<BODY BGCOLOR="#FFFFFF" BACKGROUND="/~kazu-y/image/wall.jpg">
<P><TABLE BORDER=0 CELLSPACING=0 CELLPADDING=0 WIDTH=640>
   <TR>
      <TD>
         <CENTER><FONT SIZE="+3"><B><U>$B$4CmJ8M-Fq$&$4$6$$$^$9!#(B</U></B></FONT>
         
         <P><FONT COLOR="#FF0000"><B>$B0z$-B3$-(BNET-U$B%+!<%I$N7h:Q$r9T$C$F$$$?$@$-$^$9!#(B</B></FONT></P>
         
         <P>$B$4CmJ8FbMF$N$43NG'(B<BR>
         <TABLE BORDER=1 WIDTH="80%">
            <TR>
               <TD>
                  <CENTER>$B$4CmJ8FbMF(B</CENTER>
               </TD>
               <TD>
                  <CENTER>$BBe6b(B($B>CHq@G9~$_(B)</CENTER>
               </TD>
               <TD>
                  <CENTER>$BHw9M(B</CENTER>
               </TD>
            </TR>
            <TR>
               <TD>
                  <P>1.$B!V;3K\2'$NEE;RK\!W$r9XF~(B</P>
               </TD>
               <TD>
                  <P ALIGN=right>500$B1_(B</P>
               </TD>
               <TD>
                  <P ALIGN=right>$B%Q%9%o!<%IBe6b(B</P>
               </TD>
            </TR>
            <TR>
               <TD>
                  <P>2.$B!V?7@8;y$NL?L>!W$r0MMj(B</P>
               </TD>
               <TD>
                  <P ALIGN=right>10,000$B1_(B</P>
               </TD>
               <TD>
                  <P></P>
               </TD>
            </TR>
            <TR>
               <TD>
                  <P ALIGN=right>$B9g7W9XF~6b3[(B</P>
               </TD>
               <TD>
                  <P ALIGN=right>10,500$B1_(B</P>
               </TD>
               <TD>
                  <P></P>
               </TD>
            </TR>
         </TABLE>
         
         <B>$B$43NG'$,:Q$_$^$7$?$i(B</B><FONT COLOR="#FF0000"><B>$B2<5-!VAw?.!W%\%?%s$r(B1$B2s$@$12!$7$F(B</B></FONT><B>$B$/$@$5$$!#(B<BR>
         $B$7$P$i$/$*BT$AD:$1$l$P!"(BNET-U$B%+!<%I$N7h:Q2hLL$KJQ$o$j$^$9!#(B</B></P>
         
         <P>$B$4CmJ8$ND{@5$O!"%V%i%&%6$N!VLa$k!W$G!VF~NO%U%)!<%`!W$+$i$d$jD>$7$F2<$5$$!#(B</P>
         
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
            <CENTER><INPUT TYPE=submit NAME="$BAw?.(B" VALUE="$BAw?.(B"></CENTER>
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
########$B=q@R$NCmJ8$HL?L>$N0MMj(B###########
elsif (($order2 ne "") and ($order3 ne ""))  {
	$msg = <<"ORDER023";
Content-type: text/html

<HTML>
<HEAD>
   <TITLE>$B=q@R$N$4CmJ8!&L?L>$N$40MMj(B</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=x-sjis">
</HEAD>
<BODY BGCOLOR="#FFFFFF" BACKGROUND="/~kazu-y/image/wall.jpg">
<P><TABLE BORDER=0 CELLSPACING=0 CELLPADDING=0 WIDTH=640>
   <TR>
      <TD>
         <CENTER><FONT SIZE="+3"><B><U>$B$4CmJ8M-Fq$&$4$6$$$^$9!#(B</U></B></FONT>
         
         <P><FONT COLOR="#FF0000"><B>$B0z$-B3$-(BNET-U$B%+!<%I$N7h:Q$r9T$C$F$$$?$@$-$^$9!#(B</B></FONT></P>
         
         <P>$B$4CmJ8FbMF$N$43NG'(B<BR>
         <TABLE BORDER=1 WIDTH="80%">
            <TR>
               <TD>
                  <CENTER>$B$4CmJ8FbMF(B</CENTER>
               </TD>
               <TD>
                  <CENTER>$BBe6b(B($B>CHq@G9~$_(B)</CENTER>
               </TD>
               <TD>
                  <CENTER>$BHw9M(B</CENTER>
               </TD>
            </TR>
            <TR>
               <TD>
                  <P>1.$B!V;3K\2'$NCx=q!W$r9XF~(B</P>
               </TD>
               <TD>
                  <P ALIGN=right>1,810$B1_(B</P>
               </TD>
               <TD>
                  <P ALIGN=right>$BAwNA(B310$B1_9~$_(B</P>
               </TD>
            </TR>
            <TR>
               <TD>
                  <P>2.$B!V?7@8;y$NL?L>!W$r0MMj(B</P>
               </TD>
               <TD>
                  <P ALIGN=right>10,000$B1_(B</P>
               </TD>
               <TD>
                  <P></P>
               </TD>
            </TR>
            <TR>
               <TD>
                  <P ALIGN=right>$B9g7W9XF~6b3[(B</P>
               </TD>
               <TD>
                  <P ALIGN=right>11,810$B1_(B</P>
               </TD>
               <TD>
                  <P></P>
               </TD>
            </TR>
         </TABLE>
         
         <B>$B$43NG'$,:Q$_$^$7$?$i(B</B><FONT COLOR="#FF0000"><B>$B2<5-!VAw?.!W%\%?%s$r(B1$B2s$@$12!$7$F(B</B></FONT><B>$B$/$@$5$$!#(B<BR>
         $B$7$P$i$/$*BT$AD:$1$l$P!"(BNET-U$B%+!<%I$N7h:Q2hLL$KJQ$o$j$^$9!#(B</B></P>
         
         <P>$B$4CmJ8$ND{@5$O!"%V%i%&%6$N!VLa$k!W$G!VF~NO%U%)!<%`!W$+$i$d$jD>$7$F2<$5$$!#(B</P>
         
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
            <CENTER><INPUT TYPE=submit NAME="$BAw?.(B" VALUE="$BAw?.(B"></CENTER>
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
############$BEE;RK\$N$_CmJ8(B###########
elsif ($order1 ne "")  {
	$msg = <<"ORDER100";
Content-type: text/html

<HTML>
<HEAD>
   <TITLE>$BEE;RK\$N$4CmJ8(B</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=x-sjis">
</HEAD>
<BODY BGCOLOR="#FFFFFF" BACKGROUND="/~kazu-y/image/wall.jpg">
<P><TABLE BORDER=0 CELLSPACING=0 CELLPADDING=0 WIDTH=640>
   <TR>
      <TD>
         <CENTER><FONT SIZE="+3"><B><U>$B$4CmJ8M-Fq$&$4$6$$$^$9!#(B</U></B></FONT>
         
         <P><FONT COLOR="#FF0000"><B>$B0z$-B3$-(BNET-U$B%+!<%I$N7h:Q$r9T$C$F$$$?$@$-$^$9!#(B</B></FONT></P>
         
         <P>$B$4CmJ8FbMF$N$43NG'(B<BR>
         <TABLE BORDER=1 WIDTH="80%">
            <TR>
               <TD>
                  <CENTER>$B$4CmJ8FbMF(B</CENTER>
               </TD>
               <TD>
                  <CENTER>$BBe6b(B($B>CHq@G9~$_(B)</CENTER>
               </TD>
               <TD>
                  <CENTER>$BHw9M(B</CENTER>
               </TD>
            </TR>
            <TR>
               <TD>
                  <P>1.$B!V;3K\2'$NEE;RK\!W$r9XF~(B</P>
               </TD>
               <TD>
                  <P ALIGN=right>500$B1_(B</P>
               </TD>
               <TD>
                  <P ALIGN=right>$B%Q%9%o!<%IBe6b(B</P>
               </TD>
            </TR>
            <TR>
               <TD>
                  <P ALIGN=right>$B9g7W9XF~6b3[(B</P>
               </TD>
               <TD>
                  <P ALIGN=right>500$B1_(B</P>
               </TD>
               <TD>
                  <P></P>
               </TD>
            </TR>
         </TABLE>
         
         <B>$B$43NG'$,:Q$_$^$7$?$i(B</B><FONT COLOR="#FF0000"><B>$B2<5-!VAw?.!W%\%?%s$r(B1$B2s$@$12!$7$F(B</B></FONT><B>$B$/$@$5$$!#(B<BR>
         $B$7$P$i$/$*BT$AD:$1$l$P!"(BNET-U$B%+!<%I$N7h:Q2hLL$KJQ$o$j$^$9!#(B</B></P>
         
         <P>$B$4CmJ8$ND{@5$O!"%V%i%&%6$N!VLa$k!W$G!VF~NO%U%)!<%`!W$+$i$d$jD>$7$F2<$5$$!#(B</P>
         
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
            <CENTER><INPUT TYPE=submit NAME="$BAw?.(B" VALUE="$BAw?.(B"></CENTER>
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
#########$B=q@R$N$_CmJ8(B##########
elsif ($order2 ne "")  {
	$msg = <<"ORDER020";
Content-type: text/html

<HTML>
<HEAD>
   <TITLE>$B=q@R$N$4CmJ8(B</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=x-sjis">
</HEAD>
<BODY BGCOLOR="#FFFFFF" BACKGROUND="/~kazu-y/image/wall.jpg">
<P><TABLE BORDER=0 CELLSPACING=0 CELLPADDING=0 WIDTH=640>
   <TR>
      <TD>
         <CENTER><FONT SIZE="+3"><B><U>$B$4CmJ8M-Fq$&$4$6$$$^$9!#(B</U></B></FONT>
         
         <P><FONT COLOR="#FF0000"><B>$B0z$-B3$-(BNET-U$B%+!<%I$N7h:Q$r9T$C$F$$$?$@$-$^$9!#(B</B></FONT></P>
         
         <P>$B$4CmJ8FbMF$N$43NG'(B<BR>
         <TABLE BORDER=1 WIDTH="80%">
            <TR>
               <TD>
                  <CENTER>$B$4CmJ8FbMF(B</CENTER>
               </TD>
               <TD>
                  <CENTER>$BBe6b(B($B>CHq@G9~$_(B)</CENTER>
               </TD>
               <TD>
                  <CENTER>$BHw9M(B</CENTER>
               </TD>
            </TR>
            <TR>
               <TD>
                  <P>1.$B!V;3K\2'$NCx=q!W$r9XF~(B</P>
               </TD>
               <TD>
                  <P ALIGN=right>1,810$B1_(B</P>
               </TD>
               <TD>
                  <P ALIGN=right>$BAwNA(B310$B1_9~$_(B</P>
               </TD>
            </TR>
            <TR>
               <TD>
                  <P ALIGN=right>$B9g7W9XF~6b3[(B</P>
               </TD>
               <TD>
                  <P ALIGN=right>1,810$B1_(B</P>
               </TD>
               <TD>
                  <P></P>
               </TD>
            </TR>
         </TABLE>
         
         <B>$B$43NG'$,:Q$_$^$7$?$i(B</B><FONT COLOR="#FF0000"><B>$B2<5-!VAw?.!W%\%?%s$r(B1$B2s$@$12!$7$F(B</B></FONT><B>$B$/$@$5$$!#(B<BR>
         $B$7$P$i$/$*BT$AD:$1$l$P!"(BNET-U$B%+!<%I$N7h:Q2hLL$KJQ$o$j$^$9!#(B</B></P>
         
         <P>$B$4CmJ8$ND{@5$O!"%V%i%&%6$N!VLa$k!W$G!VF~NO%U%)!<%`!W$+$i$d$jD>$7$F2<$5$$!#(B</P>
         
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
            <CENTER><INPUT TYPE=submit NAME="$BAw?.(B" VALUE="$BAw?.(B"></CENTER>
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
#$BL?L>$N$_0MMj(B
	$msg = <<"ORDER003";
Content-type: text/html

<HTML>
<HEAD>
   <TITLE>$BL?L>$N$40MMj(B</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=x-sjis">
</HEAD>
<BODY BGCOLOR="#FFFFFF" BACKGROUND="/~kazu-y/image/wall.jpg">
<P><TABLE BORDER=0 CELLSPACING=0 CELLPADDING=0 WIDTH=640>
   <TR>
      <TD>
         <CENTER><FONT SIZE="+3"><B><U>$B$4CmJ8M-Fq$&$4$6$$$^$9!#(B</U></B></FONT>
         
         <P><FONT COLOR="#FF0000"><B>$B0z$-B3$-(BNET-U$B%+!<%I$N7h:Q$r9T$C$F$$$?$@$-$^$9!#(B</B></FONT></P>
         
         <P>$B$4CmJ8FbMF$N$43NG'(B<BR>
         <TABLE BORDER=1 WIDTH="80%">
            <TR>
               <TD>
                  <CENTER>$B$4CmJ8FbMF(B</CENTER>
               </TD>
               <TD>
                  <CENTER>$BBe6b(B($B>CHq@G9~$_(B)</CENTER>
               </TD>
               <TD>
                  <CENTER>$BHw9M(B</CENTER>
               </TD>
            </TR>
            <TR>
               <TD>
                  <P>1.$B!V?7@8;y$NL?L>!W$r0MMj(B</P>
               </TD>
               <TD>
                  <P ALIGN=right>10,000$B1_(B</P>
               </TD>
               <TD>
                  <P></P>
               </TD>
            </TR>
            <TR>
               <TD>
                  <P ALIGN=right>$B9g7W9XF~6b3[(B</P>
               </TD>
               <TD>
                  <P ALIGN=right>10,000$B1_(B</P>
               </TD>
               <TD>
                  <P></P>
               </TD>
            </TR>
         </TABLE>
         
         <B>$B$43NG'$,:Q$_$^$7$?$i(B</B><FONT COLOR="#FF0000"><B>$B2<5-!VAw?.!W%\%?%s$r(B1$B2s$@$12!$7$F(B</B></FONT><B>$B$/$@$5$$!#(B<BR>
         $B$7$P$i$/$*BT$AD:$1$l$P!"(BNET-U$B%+!<%I$N7h:Q2hLL$KJQ$o$j$^$9!#(B</B></P>
         
         <P>$B$4CmJ8$ND{@5$O!"%V%i%&%6$N!VLa$k!W$G!VF~NO%U%)!<%`!W$+$i$d$jD>$7$F2<$5$$!#(B</P>
         
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
            <CENTER><INPUT TYPE=submit NAME="$BAw?.(B" VALUE="$BAw?.(B"></CENTER>
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
