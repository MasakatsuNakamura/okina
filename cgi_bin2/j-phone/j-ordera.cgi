#!/usr/local/bin/perl
$|=1;
##########################
$sendmail = "/usr/lib/sendmail";
$okina_email = 'okina@e-mail.ne.jp ';
##########################
require "cgi-lib.pl";
require "jcode.pl";
require "zenhan.pl";
use MIME::Base64;
&ReadParse();
#####$B%G!<%?$N<h$j9~$_(B#####
$name = $in{'name'};
$email = $in{'email'};
$email2 = $in{'email2'};
$fax = $in{'fax'};
$method = $in{'method'};
######$BF~NO%G!<%?$N@07A=hM}(B######
if ($fax ne "") {
	$fax =~ s/\s*//g;
	#$BA43Q1Q?t;z$r$9$Y$FH>3Q1Q?t;z$K$9$k!#(B
	$fax = &zen2han($fax); 
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
if ($method eq "fax") {
	if ($fax eq "") {
		&CgiError("$BAw$j@h$N%U%!%C%/%9HV9f$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
}
if ($method eq "mail") {
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
	$method ="$B%U%!%C%/%9$G$N<u?.$r4uK>(B";
}
if ($method eq "mail") {
	$method ="$B%Q%=%3%s$+$i%a!<%k<u?.$r4uK>(B";
}
&jcode'convert(*method, 'jis', 'euc');
#####$B$3$3$+$i(BBase64$B%a!<%k(B#####
##### $B%\%G%#4pK\J8;zNs$NDj5A(B######
@body = (
	"=====================================", 
	"$B;3K\2'$X$N!V?7@8;yL?L>!W$40MMj%U%)!<%`(B", 
	"$B2<5-$N"(Ms$rA4$F$45-F~$N>e!"!VJV?.!W$7$F2<$5$$!#(B", 
	"$B?=9~?MMM$N;aL>!'(B", 
	"$B"((B", 
	"$B?=9~?MMM$N(BE$B%a!<%k%"%I%l%9!'(B", 
	"$B"((B",  
	"$BL?L>$N$40MMjFbMF$K$D$$$F(B", 
	"$B@+(B($B$_$g$&$8!'I,$:4A;z$G$45-F~2<$5$$!#(B)$B!'(B", 
	"$B"((B", 
	"$B=P;:M=DjF|!JL$Dj$NJ}$O$*$*$h$=$G7k9=$G$9!K!'(B", 
	"$B"((B", 
    "$B7k2L$NAw?.<jCJ!'(B",
    "$B"((B",
    "$B%U%!%C%/%9$NHV9f!J$44uK><T$N$_!K!'(B",
    "$B"((B",
    "$B%Q%=%3%s$N(BE$B%a!<%k%"%I%l%9!J$44uK><T$N$_!K!'(B",
    "$B"((B",
	"$B:#$^$G!V2'$NL?L>!W$r$4MxMQ$J$5$$$^$7$?$+!)!'(B", 
	"", 
	"$B7;;P$N$*L>A0!J:9$7;Y$($J$1$l$P!K!'(B", 
	"", 
	"$B$4MWK>;v9`!'(B", 
	"", 
	"", 
	"", 
	"$B$*5^$.$NJ}$O!"$=$N;]$45-F~2<$5$$!#(B", 
	"", 
	"$B<uCm8e!"?69~@h$r?=9~?M$5$^$K$4O"MmCW$7$^$9!#(B", 
	"$B$*?6$j9~$_3NG'8e!"(B2-3$BF|$G7k2L$r$*CN$i$;$7$^$9!#(B", 
	"====================================="
);
foreach(@body) {
	&jcode'convert(*_, "sjis", "euc");
}
#######Sub$B$N@8@.(B(Base64$B%(%s%3!<%I(B)#######
$subject = "$B2'$X$4CmJ8(B(j$B%U%)%s(BVer.1)";
&jcode'convert(*subject, 'jis', 'euc');
$subject = encode_base64($subject);
chop($subject);
$subject = " . $subject . "?=";
####### $B%X%C%@$NDj5A(B#########
$mail_header = <<"EOM5";
From: $okina_email
To: $email
MIME-Version: 1.0
Content-Type: text/plain;
	charset="x-sjis-jp"
Content-Transfer-Encoding: base64
Subject: $subject
EOM5
####### $B%a%C%;!<%8%\%G%#$N@8@.(B########
$body[4] .= $name;
$body[6] .= $email;
$body[13] .= $method;
$body[15] .= $fax;
$body[17] .= $email2;
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
$msg1 = "$B$40MMjM=Ls40N;(B\n";
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
print "<A HREF=\"/~kazu-y/j-info.html\" DIRECTKEY="1">$msg3</A><BR>\n";
print "</BODY>\n";
print "</HTML>\n";
__END__