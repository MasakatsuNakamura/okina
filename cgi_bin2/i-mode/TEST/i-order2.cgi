#!/usr/local/bin/perl
$|=1;
#########################
$sendmail = "/usr/lib/sendmail";
$youraddress = 'okina@e-mail.ne.jp';
#########################
require "cgi-lib.pl";
require "jcode.pl";
require "zenhan.pl";
&ReadParse;
#########################
$name = $in{'name'};
$email = $in{'email'};
$order4 = $in{'order4'};
$order6 = $in{'order6'};
$order7 = $in{'order7'};
$familyname1 = $in{'familyname1'};
$firstname1 = $in{'firstname1'};
$birthday1= $in{'birthday1'};
$sex1 = $in{'sex1'};
$trade1 = $in{'trade1'};
$familyname2 = $in{'familyname2'};
$firstname2 = $in{'firstname2'};
$birthday2= $in{'birthday2'};
$sex2 = $in{'sex2'};
$trade2 = $in{'trade2'};
$request = $in{'request'};

######$BF~NO%G!<%?$N@07A=hM}(B######
if ($familyname1 ne "") {
	$familyname1 =~ s/\s*//g;
}
if ($familyname2 ne "") {
	$familyname2 =~ s/\s*//g;
}
if ($firstname1 ne "") {
	$familyname1 =~ s/\s*//g;
}
if ($firstname2 ne "") {
	$familyname3 =~ s/\s*//g;
}
if ($birthday1 ne "") {
	$birthday1 =~ s/\s*//g;
}
if ($birthday2 ne "") {
	$birthday3 =~ s/\s*//g;
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
	elsif ($trade1 eq "") {
		&CgiError("$B$*;E;vFbMF$^$?$O!"L>A0$NMQES$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
}
if ($order6 ne "") {
	if ($familyname1 eq "") {
		&CgiError("$B0MMj<TB&$N@+$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
   elsif ($firstname1 eq "") {
		&CgiError("$B0MMj<TB&$NL>$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
   elsif ($birthday1 eq "") {
		&CgiError("$B0MMj<TB&$N@8G/7nF|$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
   elsif ($trade1 eq "") {
		&CgiError("$B0MMj<TB&$N$4?&6H$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
   elsif ($familyname2 eq "") {
		&CgiError("$BAj<jB&$N@+$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
   elsif ($firstname2 eq "") {
		&CgiError("$BAj<jB&$NL>$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
   elsif ($birthday2 eq "") {
		&CgiError("$BAj<jB&$N@8G/7nF|$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
   elsif ($trade2 eq "") {
		&CgiError("$BAj<jB&$N$4?&6H$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
   elsif ($request eq "") {
		&CgiError("$B$4AjCLFbMF$r$*=q$-2<$5$$!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
}
if ($order7 ne "") {
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
   elsif ($trade1 eq "") {
		&CgiError("$B$4?&6H$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
   elsif ($request eq "") {
		&CgiError("$B$4AjCLFbMF$r$*=q$-2<$5$$!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
}

#####$BCmJ8%a!<%k$NAw?.(B#####
$com = <<"MESSAGE3";
From: $email
Subject: $B2'$X$4AjCL(B(i$B%b!<%I(Bv.1)

=====================================
$B;3K\2'$5$^$X!"0J2<$N$4AjCL$rCW$7$?$/!#(B

$B?=9~?MMM$N;aL>!'(B
$name
$B?=9~?MMM$N(BE$B%a!<%k%"%I%l%9!'(B
$email
$B$40MMjFbMF!'(B
$order4 
$order6 
$order7 
$B$4MWK>;v9`!'(B
$request

$B$40MMj<T$N>pJs(B
$B@+!'(B
$familyname1
$BL>!'(B
$firstname1
$B@8G/7nF|!'(B
$birthday1
$B@+JL!'(B
$sex1
$B$4?&6H!&6HL3FbMF!'(B
$trade1
$B7k:'8e$N@+!'(B
$sei

$BAj<jJ}$N>pJs(B
$B@+!'(B
$familyname2 
$BL>!'(B
$firstname2
$B@8G/7nF|!'(B
$birthday2
$B@-JL!'(B
$sex2 
$B$4?&6H!'(B
$trade2

=====================================
MESSAGE3

&jcode'convert(*com,"jis");
open(MAIL, "|$sendmail $youraddress");
print MAIL $com;
close(MAIL);

print "Content-type: text/html\n\n";
print "<HTML>\n";
print "<HEAD>\n";
print "<TITLE>$B$4AjCL<uIU40N;(B</TITLE>\n";
print "<META HTTP-EQUIV=\"Content-Type\" CONTENT=\"text/html;CHARSET=SHIFT_JIS\">\n";
print "</HEAD>\n";
print "<BODY BGCOLOR=\"#FFFFFF\" TEXT=\"#000000\" LINK=\"#0000FF\">\n";
print "<P>\n";
print "<BR>\n";
print "<BR>\n";
print "<FONT COLOR=\"#FF0000\"><B>$B$"$j$,$H$&$4$6$$$^$7$?!#(B</B></FONT><BR>\n";
print "<A HREF=\"/~kazu-y/i-info2.html\" accesskey=1>1$B"*$*CN$i$;$KLa$k!#(B</A><BR>\n";
print "</BODY>\n";
print "</HTML>\n";
