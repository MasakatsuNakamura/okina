#!/usr/local/bin/perl
$|=1;
##########################
$sendmail = "/usr/lib/sendmail";
$youraddress = 'okina@e-mail.ne.jp ';
##########################
require "cgi-lib.pl";
require "jcode.pl";
require "zenhan.pl";
&ReadParse;

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
	#$BM9JXHV9f$,(B7$B7e0J2<$GF~NO$5$l$?>l9g!"(B00$B$rKvHx$KIU2C$9$k!#(B
	$zipcord = $zipcord . "00000000";
	$zipcord = substr($zipcord, 0, 8);
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
	$method ="$B%a!<%k$7$F2<$5$$!#(B";
}
#####$BCmJ8%a!<%k$NAw?.(B#####
$com = <<"MESSAGE";
From: $email
Subject: $B2'$X$4CmJ8(B(i$B%b!<%I(Bv.3)

=====================================
$B?=9~?MMM$N;aL>!'(B
$name
$B?=9~?MMM$N(BE$B%a!<%k%"%I%l%9!'(B
$email
$B$4CmJ8FbMF!'(B
$order2
$order3

$B=q@R$NAwIU@h(B
$BM9JXHV9f!'(B
$zipcord
$B$4=;=j!'(B
$address
$B$*EEOCHV9f!'(B
$tel
$B<u<h?MMM!'(B
$fullname

$BL?L>$N$40MMjFbMF(B
$B@+(B($B$_$g$&$8(B)$B!'(B
$familyname
$B=P;:M=DjF|!'(B
$brthday
$B7k2L$NAw?.<jCJ!'(B
$method
$B%U%!%C%/%9$NHV9f!'(B
$fax
$B7k2L(BE$B%a!<%k$NHV9f!'(B
$email2
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

print "Content-type: text/html\n\n";
print "<HTML>\n";
print "<HEAD>\n";
print "<TITLE>$B$40MMj<uIU40N;(B</TITLE>\n";
print "<META HTTP-EQUIV=\"Content-Type\" CONTENT=\"text/html;CHARSET=SHIFT_JIS\">\n";
print "</HEAD>\n";
print "<BODY BGCOLOR=\"#FFFFFF\" TEXT=\"#000000\" LINK=\"#0000FF\">\n";
print "<P>\n";
print "<BR>\n";
print "<BR>\n";
print "<FONT COLOR=\"#FF0000\"><B>$B$"$j$,$H$&$4$6$$$^$7$?!#(B</B></FONT><BR>\n";
print "<A HREF=\"/~kazu-y/i-info.html\" accesskey=1>1$B"*$*CN$i$;$KLa$k!#(B</A><BR>\n";
print "</BODY>\n";
print "</HTML>\n";
