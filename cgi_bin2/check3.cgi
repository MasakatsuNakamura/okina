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
$order4 = $in{'order4'};
$familyname1 = $in{'familyname1'};
$firstname1 = $in{'firstname1'};
$birthday1= $in{'birthday1'};
$sex1 = $in{'sex1'};
$trade1 = $in{'trade1'};
$request1 = $in{'request1'};
$order6 = $in{'order6'};
$familyname3 = $in{'familyname3'};
$firstname3 = $in{'firstname3'};
$birthday3= $in{'birthday3'};
$sex3 = $in{'sex3'};
$trade3 = $in{'trade3'};
$familyname4 = $in{'familyname4'};
$firstname4 = $in{'firstname4'};
$birthday4= $in{'birthday4'};
$sex4 = $in{'sex4'};
$trade4 = $in{'trade4'};
$sei = $in{'sei'};
$request3 = $in{'request3'};
######$BF~NO%G!<%?$N@07A=hM}(B######
if ($familyname1 ne "") {
	$familyname1 =~ s/\s*//g;
}
if ($familyname3 ne "") {
	$familyname3 =~ s/\s*//g;
}
if ($familyname4 ne "") {
	$familyname4 =~ s/\s*//g;
}
if ($firstname1 ne "") {
	$familyname1 =~ s/\s*//g;
}
if ($firstname3 ne "") {
	$familyname3 =~ s/\s*//g;
}
if ($firstname4 ne "") {
	$familyname4 =~ s/\s*//g;
}
if ($birthday1 ne "") {
	$birthday1 =~ s/\s*//g;
}
if ($birthday3 ne "") {
	$birthday3 =~ s/\s*//g;
}
if ($birthday4 ne "") {
	$birthday4 =~ s/\s*//g;
}
if ($email ne "") {
	$email =~ s/\s*//g;
	#$BA43Q1Q?t;z$r$9$Y$FH>3Q1Q?t;z$K$9$k!#(B
	$email = &zen2han($email);
}
#####$BF~NO%(%i!<$N%A%'%C%/(B#####
if ($name =~ /^\s*$/){
	&CgiError("$BL>A0$N5-F~$,$"$j$^$;$s!#(B",
	"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
	exit;
}
if ($email =~ /^\s*$/){
	&CgiError("$B%a!<%k%"%I%l%9$N5-F~$,$"$j$^$;$s!#(B",
	"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
	exit;
}
elsif (($email) and (not $email =~ /.+\@.+\..+/)) {
	&CgiError("$BF~NO%(%i!<(B",
		"$B%a!<%k%"%I%l%9$N=q$-J}$,4V0c$C$F$$$^$9!#(B",$email,
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
	exit;
}
if (($order4 eq "" ) and ($order6 eq "") )  {
	&CgiError("$BF~NO%(%i!<(B",
		"$B$40MMj;v9`$,2?$b;X<($5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
	exit;
}
if ($order4 ne "") {
	if ($familyname1 eq "") {
		&CgiError("$B@+$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
	elsif ($firstname1 eq "") {
		&CgiError("$BL>$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
	elsif ($birthday1 eq "") {
		&CgiError("$B@8G/7nF|$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
    elsif ($sex1 eq "") {
		&CgiError("$B@-JL$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
    elsif ($trade1 eq "") {
		&CgiError("$B6H<o!&$4?&6H$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
   elsif ($request1 eq "") {
		&CgiError("$B$40MMjFbMF$N>\:Y$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
}
if ($order6 ne "") {
	if ($familyname3 eq "") {
		&CgiError("$B0MMj<TB&$N@+$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
   elsif ($firstname3 eq "") {
		&CgiError("$B0MMj<TB&$NL>$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
   elsif ($birthday3 eq "") {
		&CgiError("$B0MMj<TB&$N@8G/7nF|$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
   elsif ($sex3 eq "") {
		&CgiError("$B0MMj<TB&$N@-JL$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
   elsif ($trade3 eq "") {
		&CgiError("$B0MMj<TB&$N$4?&6H$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
   elsif ($familyname4 eq "") {
		&CgiError("$BAj<jB&$N@+$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
   elsif ($firstname4 eq "") {
		&CgiError("$BAj<jB&$NL>$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
   elsif ($birthday4 eq "") {
		&CgiError("$BAj<jB&$N@8G/7nF|$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
   elsif ($sex4 eq "") {
		&CgiError("$BAj<jB&$N@-JL$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
   elsif ($trade4 eq "") {
		&CgiError("$BAj<jB&$N$4?&6H$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
   elsif ($sei eq "") {
		&CgiError("$B$47k:'8e$N@+$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
}
######$B$3$3$+$i0z$-7Q$.>pJs$N@8@.$HI=<(2hLL(B######
$msg = <<"ORDER";
Content-type: text/html

<HTML>
<HEAD>
   <TITLE>$B2'$X$N$4AjCLFbMF$N3NG'(B</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=x-sjis">
</HEAD>
<BODY BGCOLOR="#FFFFFF" BACKGROUND="/~kazu-y/image/wall.jpg">
<P><TABLE BORDER=0 CELLSPACING=0 CELLPADDING=0 WIDTH=640>
   <TR>
      <TD>
         <CENTER><FONT SIZE="+3"><B><U>$B$40MMjFbMF$N$43NG'(B</U></B></FONT></CENTER>
         <BLOCKQUOTE>$B$3$N2hLL$O!"$40MMjFbMF$r$43NG'D:$/$?$a$N$b$N$G$9!#FbMF$K8m$j$,$"$k>l9g$O!"%V%i%&%6$N!VLa$k!W%\%?%s$r2!$7$F!VF~NO%U%)!<%`!W$+$i=$@5$7$F2<$5$$!#$3$l$G59$7$1$l$P!V0MMj!W%\%?%s$r2!$7$F2<$5$$!#(B</BLOCKQUOTE>
         <CENTER><B>$B$40MMjFbMF(B</B><BR>
<TABLE BORDER=1 WIDTH="90%">
   <TR>
      <TD WIDTH=148>
         <P>$B$40MMj<T(B($B5.J}(B)$B$N$*L>A0(B</P>
      </TD>
      <TD>
         <P>\$name</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>$B$40MMj<T$N%a!<%k%"%I%l%9(B</P>
      </TD>
      <TD>
         <P>\$email</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148 HEIGHT=6>
         <CENTER>$B$40MMj$NFbMF(B</CENTER>
      </TD>
      <TD HEIGHT=6>
         <CENTER>$B$40MMjFbMF$K4X$9$k>\:Y9`L\(B</CENTER>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>\$order4</P>
      </TD>
      <TD>
         <P>$B2~L>$dA*L>$r<u$1$i$l$kJ}$N>pJs(B<BR>
         <TABLE BORDER=1>
            <TR>
               <TD WIDTH=105>
                  <P>$B@+(B($BID;z(B)</P>
               </TD>
               <TD>
                  <P>\$familyname1</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=105>
                  <P>$B8=:_$NL>(B</P>
               </TD>
               <TD>
                  <P>\$firstname1</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=105>
                  <P>$B@8G/7nF|(B</P>
               </TD>
               <TD>
                  <P>\$birthday1</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=105>
                  <P>$B@-JL(B</P>
               </TD>
               <TD>
                  <P>\$sex1</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=105>
                  <P>$B$4?&6H(B($B6H<o(B)</P>
               </TD>
               <TD>
                  <P>\$trade1</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=105>
                  <P>$B$4MWK>;v9`(B<BR>
                  ($BA*L>>r7o(B)</P>
               </TD>
               <TD>
                  <P>\$request1</P>
               </TD>
            </TR>
         </TABLE>
         </P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>\$order6</P>
      </TD>
      <TD>
         <P>$B7k:'$5$l$k$*Fs?M$N>pJs(B<BR>
         <TABLE BORDER=1>
            <TR>
               <TD WIDTH=105>
                  <P>$B0MMj<T$N@+(B($BID;z(B)</P>
               </TD>
               <TD>
                  <P>\$familyname3</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=105>
                  <P>$B0MMj<T$NL>(B</P>
               </TD>
               <TD>
                  <P>\$firstname3</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=105>
                  <P>$B0MMj<T$N@8G/7nF|(B</P>
               </TD>
               <TD>
                  <P>\$birthday3</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=105>
                  <P>$B0MMj<T$N@-JL(B</P>
               </TD>
               <TD>
                  <P>\$sex3</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=105>
                  <P>$B0MMj<T$N$4?&6H(B</P>
               </TD>
               <TD>
                  <P>\$trade3</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=105>
                  <P>$BAj<jJ}$N@+(B($BID;z(B)</P>
               </TD>
               <TD>
                  <P>\$familyname4</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=105>
                  <P>$BAj<jJ}$NL>(B</P>
               </TD>
               <TD>
                  <P>\$firstname4</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=105>
                  <P>$BAj<jJ}$N@8G/7nF|(B</P>
               </TD>
               <TD>
                  <P>\$birthday4</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=105>
                  <P>$BAj<jJ}$N@-JL(B</P>
               </TD>
               <TD>
                  <P>\$sex4</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=105>
                  <P>$BAj<jJ}$N$4?&6H(B</P>
               </TD>
               <TD>
                  <P>\$trade4</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=105>
                  <P>$B7k:'8e$N@+(B($BID;z(B)</P>
               </TD>
               <TD>
                  <P>\$sei</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=105>
                  <P>$B$4MWK>;v9`(B</P>
               </TD>
               <TD>
                  <P>\$request3</P>
               </TD>
            </TR>
         </TABLE>
         </P>
      </TD>
   </TR>
</TABLE>
</CENTER>
         <BLOCKQUOTE>
            <B>$B$43NG'$,:Q$_$^$7$?$i(B</B><FONT COLOR="#FF0000"><B>$B2<5-!VCmJ8!W%\%?%s$r(B1$B2s$@$12!$7$F$4H/Cm(B</B></FONT><B>$B$/$@$5$$!#(B<BR>
            $B$J$*!">&IJ$N@-3J>e!"$3$l0J9_$N$4CmJ8$N<h$j>C$7$dJVIJ$O0l@Z=PMh$^$;$s$N$GM=$a$4N;>52<$5$$!#(B($BK,LdHNGdK!$N%/!<%j%s%0%*%U$OE,MQ$5$l$^$;$s!#(B)</B></BLOCKQUOTE>
         <CENTER>$B$4CmJ8$ND{@5$O!"%V%i%&%6$N!VLa$k!W$G!VF~NO%U%)!<%`!W$+$i$d$jD>$7$F2<$5$$!#(B</CENTER>
         <P><FORM ACTION="/~kazu-y/cgi_bin2/nn_mail3.cgi" METHOD=POST>
            <P><INPUT TYPE="hidden" NAME="name" VALUE="\$name">
            <INPUT TYPE="hidden" NAME="email" VALUE="\$email">
            <INPUT TYPE="hidden" NAME="order4" VALUE="\$order4">
            <INPUT TYPE="hidden" NAME="familyname1" VALUE="\$familyname1">
            <INPUT TYPE="hidden" NAME="firstname1" VALUE="\$firstname1">
            <INPUT TYPE="hidden" NAME="birthday1" VALUE="\$birthday1">
            <INPUT TYPE="hidden" NAME="sex1" VALUE="\$sex1">
            <INPUT TYPE="hidden" NAME="trade1" VALUE="\$trade1">
            <INPUT TYPE="hidden" NAME="request1" VALUE="\$request1">
            <INPUT TYPE="hidden" NAME="order5" VALUE="">
            <INPUT TYPE="hidden" NAME="familyname2" VALUE="">
            <INPUT TYPE="hidden" NAME="firstname2" VALUE="">
            <INPUT TYPE="hidden" NAME="family" VALUE="">
            <INPUT TYPE="hidden" NAME="request2" VALUE="">
            <INPUT TYPE="hidden" NAME="order6" VALUE="\$order6">
            <INPUT TYPE="hidden" NAME="familyname3" VALUE="\$familyname3">
            <INPUT TYPE="hidden" NAME="firstname3" VALUE="\$firstname3">
            <INPUT TYPE="hidden" NAME="birthday3" VALUE="\$birthday3">
            <INPUT TYPE="hidden" NAME="sex3" VALUE="\$sex3">
            <INPUT TYPE="hidden" NAME="trade3" VALUE="\$trade3">
            <INPUT TYPE="hidden" NAME="familyname4" VALUE="\$familyname4">
            <INPUT TYPE="hidden" NAME="firstname4" VALUE="\$firstname4">
            <INPUT TYPE="hidden" NAME="birthday4" VALUE="\$birthday4">
            <INPUT TYPE="hidden" NAME="sex4" VALUE="\$sex4">
            <INPUT TYPE="hidden" NAME="trade4" VALUE="\$trade4">
            <INPUT TYPE="hidden" NAME="sei" VALUE="\$sei">
            <INPUT TYPE="hidden" NAME="request3" VALUE="\$request3">
            <INPUT TYPE="hidden" NAME="order7" VALUE="">
            <INPUT TYPE="hidden" NAME="familyname5" VALUE="">
            <INPUT TYPE="hidden" NAME="firstname5" VALUE="">
            <INPUT TYPE="hidden" NAME="birthday5" VALUE="">
            <INPUT TYPE="hidden" NAME="sex5" VALUE="">
            <INPUT TYPE="hidden" NAME="trade5" VALUE="">
            <INPUT TYPE="hidden" NAME="request5" VALUE="">
            <CENTER><INPUT TYPE=submit NAME="$BAw?.(B" VALUE="$B0MMj(B"></CENTER>
         </FORM></P></CENTER>
      </TD>
   </TR>
</TABLE>
</P>
</BODY>
</HTML>
ORDER
&jcode'convert(*msg, "sjis", "euc");
	$msg =~ s/\$name/$name/g;
	$msg =~ s/\$email/$email/g;
	$msg =~ s/\$order4/$order4/g;
	$msg =~ s/\$familyname1/$familyname1/g;
	$msg =~ s/\$firstname1/$firstname1/g;
	$msg =~ s/\$birthday1/$birthday1/g;
	$msg =~ s/\$sex1/$sex1/g;
	$msg =~ s/\$trade1/$trade1/g;
	$msg =~ s/\$request1/$request1/g;
	$msg =~ s/\$order6/$order6/g;
	$msg =~ s/\$familyname3/$familyname3/g;
	$msg =~ s/\$firstname3/$firstname3/g;
	$msg =~ s/\$birthday3/$birthday3/g;
	$msg =~ s/\$sex3/$sex3/g;
	$msg =~ s/\$trade3/$trade3/g;
	$msg =~ s/\$familyname4/$familyname4/g;
	$msg =~ s/\$firstname4/$firstname4/g;
	$msg =~ s/\$birthday4/$birthday4/g;
	$msg =~ s/\$sex4/$sex4/g;
	$msg =~ s/\$trade4/$trade4/g;
	$msg =~ s/\$sei/$sei/g;
	$msg =~ s/\$request3/$request3/g;
	print $msg;
__end__
