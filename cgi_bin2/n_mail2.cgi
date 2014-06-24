#!/usr/local/bin/perl
$|=1;
#############################
$sendmail = "/usr/lib/sendmail";
$youraddress = 'kazu-y@mahoroba.ne.jp ';
#############################
require "cgi-lib.pl";
require "jcode.pl";
require "zenhan.pl";
use MIME::Base64;
&ReadParse();
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
#####$B$3$3$+$i(BBase64$B%a!<%k(B#####
##### $B%\%G%#4pK\J8;zNs$NDj5A(B######
@body = (
	"=====================================", 
	"$B4UDj$G$-$J$$4A;z%3!<%I(B(SJIS)$B!'(B", 
	"", 
	"$BO"Mm?M$N(BE$B%a!<%k%"%I%l%9!'(B", 
	"", 
	"$BO"Mm?M$N;aL>(B($B;29M(B)$B!'(B", 
	"", 
	"$B%(%i!<4A;z(B($B;29M(B)$B!'(B",
	"",
	"$B;29M!'%(%i!<$,H/@8$9$k2DG=@-$,9b$$!#(B", 
	"====================================="
);
foreach(@body) {
	&jcode'convert(*_, "sjis", "euc");
}
#######Sub$B$N@8@.(B(Base64$B%(%s%3!<%I(B)#######
$subject = "$BH=Dj=PMh$J$$4A;z(B(Ver.4)";
&jcode'convert(*subject, 'jis', 'euc');
$subject = encode_base64($subject);
chop($subject);
$subject = " . $subject . "?=";
####### $B%X%C%@$NDj5A(B#########
$mail_header = <<"EOM2";
From: $email2
To: $youraddress
MIME-Version: 1.0
Content-Type: text/plain;
	charset="x-sjis-jp"
Content-Transfer-Encoding: base64
Subject: $subject
EOM2
####### $B%a%C%;!<%8%\%G%#$N@8@.(B########
$body[2] .= $kanjicode;
$body[4] .= $email2;
$body[6] .= $name2;
$body[8] .= $kanji;
$mailbody = join("\r\n", @body);
$encoded = encode_base64($mailbody);
######## $B%a!<%kAw?.(B#########
open(MAIL, "|$sendmail $youraddress");
print MAIL $mail_header;
for ($i = 0; $i < length($encoded); $i += 76) {
	print MAIL substr($encoded, $i, 76);
}
close(MAIL);
#####$B0J>e$,(BBase64$B%a!<%k(B#####
print "Content-type: text/html\n\n";
print "<html>\n";
print "<head>\n";
#$B2<5-$N(BURL$B$O!"$"$J$?$N%5!]%P!]$K$"$o$;$F2<$5$$!#(B
print "<META HTTP-EQUIV=\"Refresh\" CONTENT=\"5;URL=/~kazu-y/input.html\">\n";
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