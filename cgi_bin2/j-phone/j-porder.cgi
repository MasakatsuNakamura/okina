#!/usr/local/bin/perl
$|=1;
require "cgi-lib.pl";
require "jcode.pl";
require "zenhan.pl";

$root = "/~kazu-y";
$cgipath = "/~kazu-y/cgi_bin2";
$baseurl = "http://www2.mahoroba.ne.jp";

&ReadParse;
#####$B%G!<%?$N<h$j9~$_(B#####
$name = $in{'name'};
$email = $in{'email'};
$order3 = $in{'order3'};
$familyname = $in{'familyname'};
$brthday = $in{'brthday'};
$user = $in{'user'};
$brother = $in{'brother'};

######$BF~NO%G!<%?$N@07A=hM}(B######
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
if ($order3 eq "")  {
	&CgiError("$BF~NO%(%i!<(B",
		"$B$4CmJ8$,2?$b;X<($5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
	exit;
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

#####$BCmJ8I<#2$NI=<((B#####
$msg = <<"ORDER2";
Content-type: text/html

<HTML>
<HEAD>
   <TITLE>$BL?L>$N$40MMj(B(1/2)</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=SHIFT_JIS">
</HEAD>
<BODY BGCOLOR="#FFFFFF" TEXT="#000000" LINK="#0000FF">
<P><FORM ACTION="$cgipath/j-order.cgi" METHOD=GET>
   <P><INPUT TYPE=hidden NAME=name VALUE="\$name">
   <INPUT TYPE=hidden NAME=email VALUE="\$email">
   <INPUT TYPE=hidden NAME=order3 VALUE="\$order3">
   <INPUT TYPE=hidden NAME=familyname VALUE="\$familyname">
   <INPUT TYPE=hidden NAME=brthday VALUE="\$brthday">
   <INPUT TYPE=hidden NAME=user VALUE="\$user">
   <INPUT TYPE=hidden NAME=brother VALUE="\$brother"></P>
   
   <P><B><U>$B$4MWK>;v9`(B</U></B><U>$B!!(B($B$44|BT$KE:$($J$$>l9g$b$"$j$^$9!#$4N;>52<$5$$!#(B)</U><BR>
   <TEXTAREA NAME=request ROWS=6 COLS=10 WRAP=virtual></TEXTAREA></P>
   
   <P><B><U>$B7k2L$N$4O"MmJ}K!(B</U></B><BR>
   <INPUT TYPE=radio NAME=method VALUE=fax CHECKED>$B%U%!%C%/%9$G<u?."*2<5-(B1.$B$K$*EEOCHV9f$r$45-F~2<$5$$!#(B<BR>
   <INPUT TYPE=radio NAME=method VALUE=mail>E$B%a!<%k$G<u?.(B<FONT COLOR="#FF0000">$B!J%Q%=%3%sEy$+$i$4Mw2<$5$$!#7HBSEEOC$O<u?.IT2D(B)</FONT>$B"*2<5-(B2.$B$K%"%I%l%9$r$45-F~2<$5$$!#(B</P>
   
   <P><B><U>1.$B%U%!%C%/%9HV9f(B</U></B><BR>
   <INPUT TYPE=text NAME=fax VALUE="" SIZE=16 MODE=numeric></P>
   
   <P><B><U>2.E$B%a!<%k%"%I%l%9(B<BR>
   </U></B><INPUT TYPE=text NAME=email2 VALUE="" SIZE=16 MAXLENGTH=80 MODE=alphabet></P>
   
   <P><FONT COLOR="#FF0000"><B>$BF~NO$O0J>e$G$9!#FbMF$r$43NG'$N>e!"$4CmJ8%\%?%s$r(B1$B2s$@$1%/%j%C%/$7$F2<$5$$!#(B<BR>
   $B$4CmJ8<uIU8e!"!V$"$j$,$H$&$4$6$$$^$7$?!W$N2hLL$,I=<($5$l!"(BTOP$B%Z!<%8$KLa$j$^$9!#(B</B></FONT></P>
   
   <P><FONT COLOR="#FF0000"><B>$B$J$*!"$4CmJ8$N%-%c%s%;%k$O=PMh$^$;$s$N$G!"$h$/$*3N$+$a2<$5$$!#(B</B></FONT></P>
   
   <P><B><INPUT TYPE=submit NAME="$BAw?.(B" VALUE="$B$4CmJ8(B"></B><INPUT TYPE=reset VALUE="$B%j%;%C%H(B">
</FORM></P>

<P><B>$B"(>e<j$/CmJ8$G$-$J$$>l9g$K$O!">e5-FbMF$r(B</B><A HREF="mailto:okina\@e-mail.ne.jp" DIRECTKEY="0"><B>$B%a!<%k(B(0$B%\%?%s$r2!$7$F2<$5$$!#(B)</B></A>(okina\@e-mail.ne.jp)<B>$B$K$FAwIU2<$5$$!#(B</B></P>
</BODY>
</HTML>
ORDER2
	&jcode'convert(*msg, "sjis", "euc");
	$msg =~ s/\$name/$name/g;
	$msg =~ s/\$email/$email/g;
	$msg =~ s/\$order3/$order3/g;
	$msg =~ s/\$familyname/$familyname/g;
	$msg =~ s/\$brthday/$brthday/g;
	$msg =~ s/\$user/$user/g;
	$msg =~ s/\$brother/$brother/g;
	print $msg;
__END__


