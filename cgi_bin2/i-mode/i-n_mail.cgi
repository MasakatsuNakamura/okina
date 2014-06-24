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
$subject = "$BH=Dj=PMh$J$$4A;z(B(i$B%b!<%I(BVer.3)";
&jcode'convert(*subject, 'jis', 'euc');
$subject = encode_base64($subject);
chop($subject);
$subject = " . $subject . "?=";
####### $B%X%C%@$NDj5A(B#########
$mail_header = <<"EOM6";
From: $email2
To: $youraddress
MIME-Version: 1.0
Content-Type: text/plain;
	charset="x-sjis-jp"
Content-Transfer-Encoding: base64
Subject: $subject
EOM6
####### $B%a%C%;!<%8%\%G%#$N@8@.(B########
$body[2] .= $kanjicode;
$body[4] .= $email2;
$body[6] .= $name2;
$body[8] .= $kanji;
$mailbody = join("\n", @body);
$encoded = encode_base64($mailbody);
######## $B%a!<%kAw?.(B#########
open(MAIL, "|$sendmail $youraddress");
print MAIL $mail_header;
for ($i = 0; $i < length($encoded); $i += 76) {
	print MAIL substr($encoded, $i, 76);
}
close(MAIL);
#####$B0J>e$,(BBase64$B%a!<%k(B#####
$msg1 = "$B%(%i!<Aw?.40N;(B\n";
$msg2 = "$B$46(NO$"$j$,$H$&$4$6$$$^$7$?!#(B\n";
$msg3 = "1$B"*$b$&0lEY4UDj$9$k!#(B\n";
&jcode'convert(*msg1, 'sjis', 'euc');
&jcode'convert(*msg2, 'sjis', 'euc');
&jcode'convert(*msg3, 'sjis', 'euc');
print "Content-type: text/html\n\n";
print "<HTML>\n";
print "<HEAD>\n";
print "<TITLE>$msg1</TITLE>\n";
print "<META HTTP-EQUIV=\"Content-Type\" CONTENT=\"text/html;CHARSET=SHIFT_JIS\">\n";
print "</HEAD>\n";
print "<BODY BGCOLOR=\"#FFFFFF\" TEXT=\"#000000\" LINK=\"#0000FF\">\n";
print "<P>\n";
print "<BR>\n";
print "<BR>\n";
print "<FONT COLOR=\"#FF0000\"><B>$msg2</B></FONT><BR>\n";
print "<A HREF=\"/~kazu-y/i-mode.html\" ACCESSKEY=1>$msg3</A><BR>\n";
print "</BODY>\n";
print "</HTML>\n";
__END__