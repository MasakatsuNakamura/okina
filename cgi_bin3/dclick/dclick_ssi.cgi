#!/usr/local/bin/perl
#$B",!JCm!K(Bperl$B$N%Q%9$r3NG'$7$F$/$@$5$$!#(B

use Socket;

require "./dclick_perl.pl";
#use dclick_perl;

#dclick SSI $BBP1~(B
#$B=i4|@_Dj(B

#$BCm0U!*I,$:$4<+?H$N9-9p(BID$B$KJQ99$7$F$/$@$5$$!#(B
$id = "B00369";

#$BI=<($5$;$?$$9-9p?t$rF~NO$7$F$/$@$5$$(B(1$B!A(B3)
$number = 1;

#$BI=<($5$;$?$$(Bhtml$B$NCf$K0J2<$N%3%^%s%I$rA^F~$7$F$/$@$5$$!#(B
#<!--#exec cgi="./dclick_ssi.cgi"-->
#$B$b$7$/$O(B <!--#include file="./dclick_ssi.cgi"-->

#$B:8$+$i!J(BID,$B9-9p?t!K(B
@banner=&dclick_perl'dclick($id,$number);

print "Content-type: text/html\n\n";
for($i = 0;$i < $number;$i++){
	print "$banner[$i]<br>";
}