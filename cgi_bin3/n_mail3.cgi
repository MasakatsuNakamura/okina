#!/usr/local/bin/perl
#$B>e$N%Q%9$O!"$"$J$?$N%5!]%P!]$K$"$o$;$F2<$5$$!#(B
####################################################################
#N_Mail CGI
#Copyright 1992/1997                 K.Yamano 
#Scripts Archive at$B!'(B          
#CGI$B$NHNGd!"E>:\!"G[I[!"L5CGMxMQ876X!#(B
####################################################################
#$B$"$J$?$N%5!]%P!]$N(Bsendmail$B$N%Q%9$K$"$o$;$k!#(B
$sendmail = "/usr/lib/sendmail";
#$B$"$J$?$N(BMail$B%"%I%l%9$r5-F~!#(B
$youraddress = 'kazu-y@mahoroba.ne.jp ';
#$youraddress = 'nakamura@ppd.sf.nara.sharp.co.jp ';
#####################################################################
require "cgi-lib.pl";
require "jcode.pl";
require "zenhan.pl";
&ReadParse;

###############$B2<5-$N9`L\$O!"L5@)8B$KDI2C=PMh$^$9!#(B
#################
$email = $in{'email'};
$name = $in{'name'};
$tel = $in{'tel'};
$adress = $in{'adress'};
$price = $in{'price'};
$order = $in{'order'};
######$BF~NO%G!<%?$N@07A=hM}(B######
if ($tel ne "") {
	$tel =~ s/\s*//g;
	#$BA43Q1Q?t;z$r$9$Y$FH>3Q1Q?t;z$K$9$k!#(B
	$tel = &zen2han($tel); 
}
if ($email ne "") {
	$email =~ s/\s*//g;
	#$BA43Q1Q?t;z$r$9$Y$FH>3Q1Q?t;z$K$9$k!#(B
	$email = &zen2han($email);
} 
#####$BF~NO%(%i!<$N%A%'%C%/(B#####
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
if ($name eq ""){
	&CgiError("$BL>A0$N5-F~$,$"$j$^$;$s!#(B",
	"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
	exit;
}
if ($adress eq "") {
    &CgiError("$B=;=j$,F~NO$5$l$F$$$^$;$s!#(B",
    "$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
    exit;
}	
if ($tel eq "") {
	&CgiError("$BEEOCHV9f$,F~NO$5$l$F$$$^$;$s!#(B",
	"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
	exit;
}
#####$BCmJ8%a!<%k$NAw?.(B#####
$com = <<MESSAGE;
From: $email
Subject: $BJ*7o$N$*Ld$$9g$o$;(B

=====================================
$B$*L>A0!'(B
$name
$B%a!<%k%"%I%l%9!'(B
$email
$BEEOCHV9f!'(B
$tel
$B=;=j!'(B
$adress
$B4uK>2A3J!'(B
$price
$BO"Mm;v9`!'(B
$order
=====================================
MESSAGE
#&jcode'convert(*com,"sjis","euc");
#$com =~ s/\$name/$name/;
#$com =~ s/\$email/$email/;
#$com =~ s/\$tel/$tel/;
#$com =~ s/\$adress/$adress/;
#$com =~ s/\$price/$price/;
#$com =~ s/\$order/$order/;
#&jcode'convert(*com,"jis","sjis");
&jcode'convert(*com,"jis");
open(MAIL, "|$sendmail $youraddress");
print MAIL $com;
close(MAIL);
print "Content-type: text/html\n\n";
print "<html>\n";
print "<head>\n";
#$B2<5-$N(BURL$B$O!"$"$J$?$N%5!]%P!]$K$"$o$;$F2<$5$$!#(B
print "<META HTTP-EQUIV=\"Refresh\" CONTENT=\"5;URL=http://www.sikasenbey.or.jp/haibara/haibara.htm\">\n";
#print "<META HTTP-EQUIV=\"Refresh\" CONTENT=\"5;URL=http://ppd.sf.nara.sharp.co.jp/~nakamura/test/seimei2/public_html/input.html\">\n";
print "<title>$BAw?.40N;(B</title></head>\n";
print "<body bgcolor=\"ffffff\" TEXT=\"000000\" link=\"fb02ee\" vlink=\"fb02ee\">\n";
print "<p>\n";
print "<br>\n";
print "<br>\n";
print "<center>\n";
print "<font size=\"6\" color=\"000000\"><b>$B8eF|!"$3$A$i$+$i$4O"Mm:9$7>e$2$^$9!#(B</b></font><br>\n";
print "</center>\n";
print "</body>\n";
print "</html>\n";
