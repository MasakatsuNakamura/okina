#!/usr/local/bin/perl
$|=1;
#########################
require 'cgi-lib.pl';
require 'jcode.pl';
require "zenhan.pl";
use MIME::Base64;
&ReadParse();
#####$B%G!<%?$N<h$j9~$_(B#####
$name = $in{'name'};
$email = $in{'email'};
$email2 = $in{'email2'};
$order2 = $in{'order2'};
$order3 = $in{'order3'};
$zipcord = $in{'zipcord'};
$address = $in{'address'};
$tel = $in{'tel'};
$fax = $in{'fax'};
$fullname = $in{'fullname'};
$familyname = $in{'familyname'};
$brthday = $in{'brthday'};
$method = $in{'method'};
$user = $in{'user'};
$brother = $in{'brother'};
$request = $in{'request'};
######$BF~NO%G!<%?$N@07A=hM}(B######
if ($zipcord ne "") {
	$zipcord =~ s/\s*//g;
	#$BA43Q1Q?t;z$r$9$Y$FH>3Q1Q?t;z$K$9$k!#(B
	$zipcord = &zen2han($zipcord); 
}
if ($tel ne "") {
	$tel =~ s/\s*//g;
	#$BA43Q1Q?t;z$r$9$Y$FH>3Q1Q?t;z$K$9$k!#(B
	$tel = &zen2han($tel); 
}
if ($fax ne "") {
	$fax =~ s/\s*//g;
	#$BA43Q1Q?t;z$r$9$Y$FH>3Q1Q?t;z$K$9$k!#(B
	$fax = &zen2han($fax); 
}
if ($familyname ne "") {
	$familyname =~ s/\s*//g;
}
if ($brthday ne "") {
	$brthday =~ s/\s*//g;
}
if ($email ne "") {
	$email =~ s/\s*//g;
	#$BA43Q1Q?t;z$r$9$Y$FH>3Q1Q?t;z$K$9$k!#(B
	$email = &zen2han($email);
} 
if ($email2 ne "") {
	$email2 =~ s/\s*//g;
	#$BA43Q1Q?t;z$r$9$Y$FH>3Q1Q?t;z$K$9$k!#(B
	$email2 = &zen2han($email);
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
if ($order2 ne "") {
	if ($zipcord eq "") {
		&CgiError("$BM9JXHV9f$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
	elsif ($address eq "") {
		&CgiError("$B=;=j$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}	
	elsif ($fullname eq "") {
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
if (($order3 ne "") and ($method eq "fax")) {
	if ($fax eq "") {
		&CgiError("$BAw$j@h$N%U%!%C%/%9HV9f$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
}
if (($order3 ne "") and ($method eq "mail")) {
	if ($email2 =~ /^\s*$/){
	&CgiError("$B7k2LO"Mm@h$N%a!<%k%"%I%l%9$N5-F~$,$"$j$^$;$s!#(B",
	"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
	exit;
    }
    elsif (($email2) and (not $email2 =~ /.+\@.+\..+/)) {
	&CgiError("$BF~NO%(%i!<(B",
		"$B7k2LO"Mm@h$N%a!<%k%"%I%l%9$N=q$-J}$,4V0c$C$F$$$^$9!#(B",$email2,
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
	exit;
    }
}
#####$B<jCJ$rJ8>O2=(B#####
if ($method eq "fax") {
	$method ="$B%U%!%C%/%9$GAw$C$F$/$@$5$$!#(B";
}
if ($method eq "mail") {
	$method ="$BEE;R%a!<%k$GAw$C$F$/$@$5$$!#(B";
}
&jcode'convert(*method, 'jis', 'euc');
######$B$3$3$+$i0z$-7Q$.>pJs$N@8@.$HI=<(2hLL(B######
#########$B=q@R$N$_CmJ8(B##########
if ($order2 ne "")  {
	$msg = <<"ORDER020";
Content-type: text/html

<HTML>
<HEAD>
<TITLE>$B=q@R$N$4CmJ8(B</TITLE>
<META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=x-sjis">
</HEAD>
<BODY BGCOLOR="#FFFFFF">
<P>
<CENTER><B><U>$B$4CmJ8FbMF$N$43NG'(B</U></B></CENTER>        
<BLOCKQUOTE>$B$3$N2hLL$O!"$4CmJ8FbMF$r$43NG'D:$/$?$a$N$b$N$G$9!#FbMF$K8m$j$,$"$k>l9g$O!"%V%i%&%6$N!VLa$k!W%\%?%s$r2!$7$F!VF~NO%U%)!<%`!W$+$i=$@5$7$F2<$5$$!#$3$l$G59$7$1$l$P!VCmJ8!W%\%?%s$r2!$7$F2<$5$$!#(B</BLOCKQUOTE>         
<CENTER><B>$B$4CmJ8FbMF(B</B></CENTER><BR>
<HR>
$B$"$J$?$N$*L>A0!J$*?=9~?M!K(B<BR>
\$name<BR>
$B%a!<%k%"%I%l%9(B<BR>
\$email<BR>
$B=q@R$NAw$j@h$K$D$$$F(B<BR>
$BM9JXHV9f(B<BR>
\$zipcord<BR>
$B$4=;=j(B<BR>
\$address<BR>
$B$4<+Bp$N$*EEOCHV9f(B<BR>
\$tel<BR>
$B<u<h?M$4;aL>(B<BR>
\$fullname<BR>
<HR>         
<BLOCKQUOTE><B>$B$43NG'$,:Q$_$^$7$?$i(B</B><FONT COLOR="#FF0000"><B>$B2<5-!VCmJ8!W%\%?%s$r(B1$B2s$@$12!$7$F$4H/Cm(B</B></FONT><B>$B$/$@$5$$!#(B<BR>
$B$J$*!">&IJ$N@-3J>e!"$3$l0J9_$N$4CmJ8$N<h$j>C$7$dJVIJ$O0l@Z=PMh$^$;$s$N$GM=$a$4N;>52<$5$$!#(B($BK,LdHNGdK!$N%/!<%j%s%0%*%U$OE,MQ$5$l$^$;$s!#!K(B</B></BLOCKQUOTE>        
$B$4CmJ8$ND{@5$O!"%V%i%&%6$N!VLa$k!W$G!VF~NO%U%)!<%`!W$+$i$d$jD>$7$F2<$5$$!#(B<BR>          <P><FORM ACTION="/~kazu-y/cgi_bin2/in-order.cgi" METHOD=POST>
            <P><INPUT TYPE="hidden" NAME="name" VALUE="\$name">
            <INPUT TYPE="hidden" NAME="email" VALUE="\$email">
            <INPUT TYPE="hidden" NAME="email2" VALUE="">
            <INPUT TYPE="hidden" NAME="order2" VALUE="\$order2">
            <INPUT TYPE="hidden" NAME="order3" VALUE="">
            <INPUT TYPE="hidden" NAME="zipcord" VALUE="\$zipcord">
            <INPUT TYPE="hidden" NAME="address" VALUE="\$address">
            <INPUT TYPE="hidden" NAME="tel" VALUE="\$tel">
            <INPUT TYPE="hidden" NAME="fax" VALUE="">
            <INPUT TYPE="hidden" NAME="fullname" VALUE="\$fullname">
            <INPUT TYPE="hidden" NAME="familyname" VALUE="">
            <INPUT TYPE="hidden" NAME="brthday" VALUE="">
            <INPUT TYPE="hidden" NAME="method" VALUE="">
            <INPUT TYPE="hidden" NAME="user" VALUE="">
            <INPUT TYPE="hidden" NAME="brother" VALUE="">
            <INPUT TYPE="hidden" NAME="request" VALUE="">
            <INPUT TYPE="hidden" NAME="kgak" VALUE="1,810">
            <CENTER><INPUT TYPE=submit NAME="$BAw?.(B" VALUE="$BCmJ8(B">
         </FORM></P>
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
	print $msg;
}
###########$BL?L>$N$_0MMj(B############
elsif ($order3 ne "")  {
	$msg = <<"ORDER003";
Content-type: text/html

<HTML>
<HEAD>
<TITLE>$BL?L>$N$40MMj(B</TITLE>
<META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=x-sjis">
</HEAD>
<BODY BGCOLOR="#FFFFFF">
<P>
<CENTER><B><U>$B$4CmJ8FbMF$N$43NG'(B</U></B></CENTER>         
<BLOCKQUOTE>$B$3$N2hLL$O!"$4CmJ8FbMF$r$43NG'D:$/$?$a$N$b$N$G$9!#FbMF$K8m$j$,$"$k>l9g$O!"%V%i%&%6$N!VLa$k!W%\%?%s$r2!$7$F!VF~NO%U%)!<%`!W$+$i=$@5$7$F2<$5$$!#$3$l$G59$7$1$l$P!VCmJ8!W%\%?%s$r2!$7$F2<$5$$!#(B</BLOCKQUOTE>
<CENTER><B>$B$4CmJ8FbMF(B</B><BR></CENTER>
<HR>
$B$"$J$?$N$*L>A0!J$*?=9~?M!K(B<BR>
\$name<BR>
$B%a!<%k%"%I%l%9(B<BR>
\$email<BR>
$B?7@8;y$NID;z(B($B@+(B)<BR>
\$familyname<BR>
$B$4=P;:M=DjF|(B<BR>
\$brthday<BR>
$B$4MxMQ2s?t(B<BR>
\$user<BR>
$B$47;;P$N$*L>A0(B<BR>
\$brother<BR>
$B$4MWK>;v9`(B<BR>
\$request<BR>
$B7k2L$N$4O"MmJ}K!(B<BR>
\$method<BR>
$B%U%!%C%/%9HV9f(B<BR>
\$fax<BR>
$B%Q%=%3%s$N(BE$B%a!<%k%"%I%l%9(B<BR>
\$email2<BR>
<HR>
<BLOCKQUOTE><B>$B$43NG'$,:Q$_$^$7$?$i(B</B><FONT COLOR="#FF0000"><B>$B2<5-!VCmJ8!W%\%?%s$r(B1$B2s$@$12!$7$F$4H/Cm(B</B></FONT><B>$B$/$@$5$$!#(B<BR>
$B$J$*!">&IJ$N@-3J>e!"$3$l0J9_$N$4CmJ8$N<h$j>C$7$dJVIJ$O0l@Z=PMh$^$;$s$N$GM=$a$4N;>52<$5$$!#(B($BK,LdHNGdK!$N%/!<%j%s%0%*%U$OE,MQ$5$l$^$;$s!#!K(B</B></BLOCKQUOTE>         
$B$4CmJ8$ND{@5$O!"%V%i%&%6$N!VLa$k!W$G!VF~NO%U%)!<%`!W$+$i$d$jD>$7$F2<$5$$!#(B        
         <P><FORM ACTION="/~kazu-y/cgi_bin2/in-order.cgi" METHOD=POST>
            <P><INPUT TYPE="hidden" NAME="name" VALUE="\$name">
            <INPUT TYPE="hidden" NAME="email" VALUE="\$email">
            <INPUT TYPE="hidden" NAME="order2" VALUE="">
            <INPUT TYPE="hidden" NAME="order3" VALUE="\$order3">
            <INPUT TYPE="hidden" NAME="zipcord" VALUE="">
            <INPUT TYPE="hidden" NAME="address" VALUE="">
            <INPUT TYPE="hidden" NAME="tel" VALUE="\$tel">
            <INPUT TYPE="hidden" NAME="method" VALUE="\$method">
            <INPUT TYPE="hidden" NAME="email2" VALUE="\$email2">
            <INPUT TYPE="hidden" NAME="fax" VALUE="\$fax">
            <INPUT TYPE="hidden" NAME="fullname" VALUE="">
            <INPUT TYPE="hidden" NAME="familyname" VALUE="\$familyname">
            <INPUT TYPE="hidden" NAME="brthday" VALUE="\$brthday">
            <INPUT TYPE="hidden" NAME="user" VALUE="\$user">
            <INPUT TYPE="hidden" NAME="brother" VALUE="\$brother">
            <INPUT TYPE="hidden" NAME="request" VALUE="\$request">
            <INPUT TYPE="hidden" NAME="kgak" VALUE="10,000">
            <CENTER><INPUT TYPE=submit NAME="$BAw?.(B" VALUE="$BCmJ8(B">
         </FORM></P>
</P>
</BODY>
</HTML>
ORDER003
&jcode'convert(*msg, "sjis", "euc");
	$msg =~ s/\$name/$name/g;
	$msg =~ s/\$email/$email/g;	
	$msg =~ s/\$order3/$order3/g;
	$msg =~ s/\$tel/$tel/g;
	$msg =~ s/\$method/$method/g;
	$msg =~ s/\$email2/$email2/g;
	$msg =~ s/\$fax/$fax/g;	
	$msg =~ s/\$familyname/$familyname/g;
	$msg =~ s/\$brthday/$brthday/g;
	$msg =~ s/\$user/$user/g;
	$msg =~ s/\$brother/$brother/g;
	$msg =~ s/\$request/$request/g;
	print $msg;
}
__end__
