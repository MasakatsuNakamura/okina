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
if (($order1 eq "" ) and ($order2 eq "" ) and ($order3 eq ""))  {
	&CgiError("$BF~NO%(%i!<(B",
		"$B$4CmJ8$,2?$b;X<($5$l$F$$$^$;$s!#(B",
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

#####$BCmJ8%a!<%k$NAw?.(B#####
$com = <<"MESSAGE";
From: $email
Subject: $B;3K\2'$X$N$4CmJ8(B(i-geti/Ver.4)

=====================================
$B?=9~?MMM$N;aL>!'(B
$name
$B?=9~?MMM$N(BE$B%a!<%k%"%I%l%9!'(B
$email
$B$4CmJ8FbMF!'(B
$order1
$order2
$order3

$B=q@R$NAwIU@h$^$?$O$4O"Mm@h(B
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
print "<html>\n";
print "<head>\n";
#$B2<5-$N(BURL$B$O!"$"$J$?$N%5!]%P!]$K$"$o$;$F2<$5$$!#(B
print "<META HTTP-EQUIV=\"Refresh\" CONTENT=\"5;URL=/~kazu-y/i-geti.html\">\n";
print "<title>$B$4CmJ8<uIU40N;(B</title></head>\n";
print "<body bgcolor=\"ffffff\" TEXT=\"000000\" link=\"fb02ee\" vlink=\"fb02ee\">\n";
print "<p>\n";
print "<br>\n";
print "<br>\n";
print "<center>\n";
print "<font size=\"6\" color=\"000000\"><b>$B$"$j$,$H$&$4$6$$$^$7$?!#(B</b></font><br>\n";
print "</center>\n";
print "</body>\n";
print "</html>\n";
