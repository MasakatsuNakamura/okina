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
&ReadParse;

###############$B2<5-$N9`L\$O!"L5@)8B$KDI2C=PMh$^$9!#(B#################
$kanji = $in{'kanji'};
$name2 = $in{'name2'};
$email2 = $in{'email2'};


####$B2<5-$N=;=j!";aL>!"(BTEL$B!"(BFAX$B$O!">e$N9`L\$K$"$o$;$FDI2C$9$k!#(B######
####$BNc$($P!"2q<RL>$rDI2C$N>l9g$O!"2q<RL>!"(B$kaisya $B$H5-F~!#(B
####$kaisya$B$O!"I,$:%m!]%^;z%3!]%I$GBG$A9~$`!#(B
$kanjicode = $kanji;
$kanjicode =~ s/ //g;
$kanjicode =~ s/(.)/sprintf("%02X",unpack("c",$1) >= 0 ? unpack("c",$1)
: 256 + unpack("c",$1))/eg;
$kanjicode =~ s/(....)/$1 /g;

$com = <<MESSAGE;
From: $email2
Subject: $BH=Dj=PMh$J$$4A;z(B($B4k6HHG(B)

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
#&jcode'convert(*com,"sjis","euc");
#$com =~ s/\$kanji/$kanji/;
#$com =~ s/\$name2/$name2/;
#$com =~ s/\$email2/$email2/;
#&jcode'convert(*com,"jis","sjis");
&jcode'convert(*com,"jis");
open(MAIL, "|$sendmail $youraddress");
print MAIL $com;
close(MAIL);
print "Content-type: text/html\n\n";
print "<html>\n";
print "<head>\n";
#$B2<5-$N(BURL$B$O!"$"$J$?$N%5!]%P!]$K$"$o$;$F2<$5$$!#(B
print "<META HTTP-EQUIV=\"Refresh\" CONTENT=\"5;URL=/~kazu-y/input3.html\">\n";
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
