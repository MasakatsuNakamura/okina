#!/usr/local/bin/perl
$|=1;
#########################
$sendmail = "/usr/lib/sendmail";
$okina_email = 'okina@e-mail.ne.jp';
#########################
require "cgi-lib.pl";
require "jcode.pl";
require "zenhan.pl";
use MIME::Base64;
&ReadParse();
#########################
$name = $in{'name'};
$email = $in{'email'};
$order = $in{'order'};
######$BF~NO%G!<%?$N@07A=hM}(B######
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
#####$B<jCJ$rJ8>O2=(B#####
if ($order eq "change") {
	$order ="$B2~L>$NAjCL!JL>A0$rJQ$($?$$!K(B";
}
if ($order eq "pen") {
	$order ="$BA*L>$N0MMj!J$*;E;v>e$N$*L>A0!"2m9f!"%Z%s%M!<%`!"7]L>$J$I!K(B";
}
if ($order eq "corp") {
	$order ="$B2q<RL>$NA*L>(B";
}
&jcode'convert(*order, 'jis', 'euc');
#####$B$3$3$+$i(BBase64$B%a!<%k(B#####
##### $B%\%G%#4pK\J8;zNs$NDj5A(B######
@body = (
	"=====================================", 
	"$B;3K\2'$X$N!V$4AjCL!W$40MMj%U%)!<%`(B", 
	"$B2<5-$N"(Ms$r$45-F~$N>e!"!VJV?.!W$7$F2<$5$$!#(B", 
	"$B?=9~?MMM$N;aL>!'(B", 
	"$B"((B", 
	"$B?=9~?MMM$N(BE$B%a!<%k%"%I%l%9!'(B", 
	"$B"((B", 
	"$B$40MMjFbMF!'(B",
	"$B"((B",
	"$B$4MWK>;v9`!J6qBNE*$K!K!'(B", 
	"$B"((B", 
	"", 
	"$BL>A0$rIU$1$i$l$kJ}$N>pJs!J2~L>!&A*L>$N>l9g!K(B", 
	"$B@+!J$_$g$&$8!'I,$:4A;z$G$*4j$$CW$7$^$9!K!'(B", 
	"$B"((B", 
	"$BL>!'(B", 
	"$B"((B", 
	"$B@8G/7nF|!'(B", 
	"$B"((B", 
	"$B@-JL!'(B", 
	"$B"((B", 
	"$B$4?&6H$^$?$O!"6HL3FbMF!'(B", 
	"$B"((B", 
    "",
	"$B2q<R$N>pJs!J2q<RL>$N>l9g!K(B", 
	"$B2q<R$N6HL3FbMF!J6qBNE*$K!K!'(B", 
    "$B"((B",
	"", 
	"", 
	"$B<uCm8e!"?69~@h$r?=9~?M$5$^$K$4O"MmCW$7$^$9!#(B", 
    "$B$*?6$j9~$_3NG'8e!"(B2-3$BF|$G7k2L$r$*CN$i$;$7$^$9!#(B",
	"====================================="
);
foreach(@body) {
	&jcode'convert(*_, "sjis", "euc");
}
#######Sub$B$N@8@.(B(Base64$B%(%s%3!<%I(B)#######
$subject = "$B2'$X$4AjCL(B(j$B%U%)%s(BVer.1)";
&jcode'convert(*subject, 'jis', 'euc');
$subject = encode_base64($subject);
chop($subject);
$subject = " . $subject . "?=";
####### $B%X%C%@$NDj5A(B#########
$mail_header = <<"EOM6";
From: $okina_email
To: $email
MIME-Version: 1.0
Content-Type: text/plain;
	charset="x-sjis-jp"
Content-Transfer-Encoding: base64
Subject: $subject
EOM6
####### $B%a%C%;!<%8%\%G%#$N@8@.(B########
$body[4] .= $name;
$body[6] .= $email;
$body[8] .= $order;
$mailbody = join("\n", @body);
$encoded = encode_base64($mailbody);
######## $B%a!<%kAw?.(B#########
open(MAIL, "|$sendmail $okina_email");
print MAIL $mail_header;
for ($i = 0; $i < length($encoded); $i += 76) {
	print MAIL substr($encoded, $i, 76);
}
close(MAIL);
#####$B0J>e$,(BBase64$B%a!<%k(B#####
$msg1 = "$B$4AjCLM=Ls40N;(B\n";
$msg2 = "$B;C$/$7$^$9$H!"$40MMjMQ;f$,%a!<%k$GFO$-$^$9!#(B\n";
$msg3 = "1$B"*$*CN$i$;$KLa$k!#(B\n";
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
print "<A HREF=\"/~kazu-y/j-info2.html\" DIRECTKEY="1">$msg3</A><BR>\n";
print "</BODY>\n";
print "</HTML>\n";
__END__