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
Subject: $BH=Dj=PMh$J$$4A;z(B(i$B%b!<%I(B2)

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
print "<HTML>\n";
print "<HEAD>\n";
print "<TITLE>$B%(%i!<Aw?.40N;(B</TITLE>\n";
print "<META HTTP-EQUIV=\"Content-Type\" CONTENT=\"text/html;CHARSET=SHIFT_JIS\">\n";
print "</HEAD>\n";
print "<BODY BGCOLOR=\"#FFFFFF\" TEXT=\"#000000\" LINK=\"#0000FF\">\n";
print "<P>\n";
print "<BR>\n";
print "<BR>\n";
print "<FONT COLOR=\"#FF0000\"><B>$B$46(NO$"$j$,$H$&$4$6$$$^$7$?!#(B</B></FONT><BR>\n";
print "<A HREF=\"/~kazu-y/i-mode.html\" accesskey=1>1$B"*$b$&0lEY4UDj$9$k!#(B</A><BR>\n";
print "</BODY>\n";
print "</HTML>\n";
