#!/usr/local/bin/perl
$|=1;
#############################
$sendmail = "/usr/lib/sendmail";
$youraddress = 'kazu-y@mahoroba.ne.jp ';
#############################
require "cgi-lib.pl";
require "jcode.pl";
require "zenhan.pl";
&ReadParse;
#############################
$kanji = $in{'kanji'};
$name2 = $in{'name2'};
$email2 = $in{'email2'};

#####$B%G!<%?$N@07A=hM}(B#####
if ($email2 ne "") {
	$email2 =~ s/\s*//g;
	#$BA43Q1Q?t;z$r$9$Y$FH>3Q1Q?t;z$K$9$k!#(B
	$email2 = &zen2han($email2);
} 

#####$B4A;z%3!<%I$N@8@.(B#####
$kanjicode = $kanji;
$kanjicode =~ s/ //g;
$kanjicode =~ s/(.)/sprintf("%02X",unpack("c",$1) >= 0 ? unpack("c",$1)
: 256 + unpack("c",$1))/eg;
$kanjicode =~ s/(....)/$1 /g;

#####$BCmJ8%a!<%k$NAw?.(B#####
$com = <<"MESSAGE";
From: $email2
Subject: $BH=Dj=PMh$J$$4A;z(B(i-geti2)

=====================================
$B4UDj$G$-$J$$4A;z%3!<%I(B(SJIS)$B!'(B
$kanjicode
$BO"Mm?M$N(BE$B%a!<%k%"%I%l%9!'(B
$email2
$BO"Mm?M$N;aL>(B($B;29M(B)$B!'(B
$name2
$B%(%i!<4A;z(B($B;29M(B)$B!'(B
$kanji
$B;29M!'%(%i!<$,H/@8$9$k2DG=@-$,9b$$!#(B
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
print "<META HTTP-EQUIV=\"Refresh\" CONTENT=\"5;URL=/~kazu-y/g-input.html\">\n";
#print "<META HTTP-EQUIV=\"Refresh\" CONTENT=\"5;URL=http://ppd.sf.nara.sharp.co.jp/~nakamura/test/seimei2/public_html/input.html\">\n";
print "<title>$BAw?.40N;(B</title></head>\n";
print "<body bgcolor=\"ffffff\" TEXT=\"000000\" link=\"fb02ee\" vlink=\"fb02ee\">\n";
print "<p>\n";
print "<br>\n";
print "<br>\n";
print "<center>\n";
print "<font size=\"6\" color=\"000000\"><b>$B$46(NO$"$j$,$H$&$4$6$$$^$7$?!#(B</b></font><br>\n";
print "</center>\n";
print "</body>\n";
print "</html>\n";
