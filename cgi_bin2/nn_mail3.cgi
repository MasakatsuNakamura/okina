#!/usr/local/bin/perl
$|=1;
#########################
$sendmail = "/usr/lib/sendmail";
$okina_email = 'kazu-y@mahoroba.ne.jp';
$okina_email2 = 'okina@e-mail.ne.jp';
#########################
require "cgi-lib.pl";
require "jcode.pl";
require "zenhan.pl";
use MIME::Base64;
&ReadParse();
#########################
$name = $in{'name'};
$email = $in{'email'};
$order4 = $in{'order4'};
$familyname1 = $in{'familyname1'};
$firstname1 = $in{'firstname1'};
$birthday1= $in{'birthday1'};
$sex1 = $in{'sex1'};
$trade1 = $in{'trade1'};
$request1 = $in{'request1'};
$order5 = $in{'order5'};
$familyname2 = $in{'familyname2'};
$firstname2 = $in{'firstname2'};
$family = $in{'family'};
$request2 = $in{'request2'};
$order6 = $in{'order6'};
$familyname3 = $in{'familyname3'};
$firstname3 = $in{'firstname3'};
$birthday3= $in{'birthday3'};
$sex3 = $in{'sex3'};
$trade3 = $in{'trade3'};
$familyname4 = $in{'familyname4'};
$firstname4 = $in{'firstname4'};
$birthday4= $in{'birthday4'};
$sex4 = $in{'sex4'};
$trade4 = $in{'trade4'};
$sei = $in{'sei'};
$request3 = $in{'request3'};
$order7 = $in{'order7'};
$familyname5 = $in{'familyname5'};
$firstname5 = $in{'firstname5'};
$birthday5= $in{'birthday5'};
$sex5 = $in{'sex5'};
$trade5 = $in{'trade5'};
$request5 = $in{'request5'};
######$BF~NO%G!<%?$N@07A=hM}(B######
if ($familyname1 ne "") {
	$familyname1 =~ s/\s*//g;
}
if ($familyname2 ne "") {
	$familyname2 =~ s/\s*//g;
}
if ($familyname3 ne "") {
	$familyname3 =~ s/\s*//g;
}
if ($familyname4 ne "") {
	$familyname4 =~ s/\s*//g;
}
if ($familyname5 ne "") {
	$familyname5 =~ s/\s*//g;
}
if ($firstname1 ne "") {
	$familyname1 =~ s/\s*//g;
}
if ($firstname2 ne "") {
	$familyname2 =~ s/\s*//g;
}
if ($firstname3 ne "") {
	$familyname3 =~ s/\s*//g;
}
if ($firstname4 ne "") {
	$familyname4 =~ s/\s*//g;
}
if ($firstname5 ne "") {
	$familyname5 =~ s/\s*//g;
}
if ($birthday1 ne "") {
	$birthday1 =~ s/\s*//g;
}
if ($birthday3 ne "") {
	$birthday3 =~ s/\s*//g;
}
if ($birthday4 ne "") {
	$birthday4 =~ s/\s*//g;
}
if ($birthday5 ne "") {
	$birthday5 =~ s/\s*//g;
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
if (($order4 eq "" ) and ($order5 eq "" ) and ($order6 eq "") and ($order7 eq ""))  {
	&CgiError("$BF~NO%(%i!<(B",
		"$B$40MMj;v9`$,2?$b;X<($5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
	exit;
}
if ($order4 ne "") {
	if ($familyname1 eq "") {
		&CgiError("$B@+$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
	elsif ($firstname1 eq "") {
		&CgiError("$BL>$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
	elsif ($birthday1 eq "") {
		&CgiError("$B@8G/7nF|$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
    elsif ($sex1 eq "") {
		&CgiError("$B@-JL$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
    elsif ($trade1 eq "") {
		&CgiError("$B6H<o!&$4?&6H$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
   elsif ($request1 eq "") {
		&CgiError("$B$40MMjFbMF$N>\:Y$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
}
if ($order5 ne "") {
	if ($familyname2 eq "") {
		&CgiError("$B@+$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
	elsif ($firstname2 eq "") {
		&CgiError("$BL>$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
}
if ($order6 ne "") {
	if ($familyname3 eq "") {
		&CgiError("$B0MMj<TB&$N@+$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
   elsif ($firstname3 eq "") {
		&CgiError("$B0MMj<TB&$NL>$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
   elsif ($birthday3 eq "") {
		&CgiError("$B0MMj<TB&$N@8G/7nF|$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
   elsif ($sex3 eq "") {
		&CgiError("$B0MMj<TB&$N@-JL$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
   elsif ($trade3 eq "") {
		&CgiError("$B0MMj<TB&$N$4?&6H$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
   elsif ($familyname4 eq "") {
		&CgiError("$BAj<jB&$N@+$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
   elsif ($firstname4 eq "") {
		&CgiError("$BAj<jB&$NL>$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
   elsif ($birthday4 eq "") {
		&CgiError("$BAj<jB&$N@8G/7nF|$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
   elsif ($sex4 eq "") {
		&CgiError("$BAj<jB&$N@-JL$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
   elsif ($trade4 eq "") {
		&CgiError("$BAj<jB&$N$4?&6H$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
   elsif ($sei eq "") {
		&CgiError("$B$47k:'8e$N@+$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
}
if ($order7 ne "") {
	if ($familyname5 eq "") {
		&CgiError("$B@+$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
   elsif ($firstname5 eq "") {
		&CgiError("$BL>$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
   elsif ($birthday5 eq "") {
		&CgiError("$B@8G/7nF|$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
   elsif ($sex5 eq "") {
		&CgiError("$B@-JL$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
   elsif ($trade5 eq "") {
		&CgiError("$B$4?&6H$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
   elsif ($request5 eq "") {
		&CgiError("$B$4AjCLFbMF$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
}
#####$B$3$3$+$i(BBase64$B%a!<%k(B#####
#####$B<+J,08$NCmJ8%a!<%kAw?.(B#####
##### $B%\%G%#4pK\J8;zNs$NDj5A(B######
@body = (
	"=====================================",
    "$B;3K\2'$5$^$X!"0J2<$N$4AjCL$rCW$7$?$/!#(B",
    "",
    "$B?=9~?MMM$N;aL>(B:",
    "",
    "$B?=9~?MMM$N(BE$B%a!<%k%"%I%l%9(B:",
    "",
    "",
    "$B$40MMjFbMF(B:",
    "",
    "$B@+(B:",
    "",
    "$BL>(B:",
    "",
    "$B@8G/7nF|(B:",
    "",
    "$B@-JL(B:",
    "",
    "$B6H<o!&?&6H(B:",
    "",
    "$B$4MWK>;v9`(B:",
    "",
    "",
    "$B$40MMjFbMF(B:",
    "",
    "$B@+(B:",
    "",
    "$BL>(B:",
    "",
    "$B$42HB2$N$*L>A0$HB3$-JA(B:",
    "",
    "$B$4MWK>;v9`(B:",
    "",
    "",
    "$B$40MMjFbMF(B:",
    "",
    "$B0MMj<TB&$N@+(B:",
    "",
    "$B0MMj<TB&$NL>(B:",
    "",
    "$B0MMj<TB&$N@8G/7nF|(B:",
    "",
    "$B0MMj<TB&$N@+JL(B:",
    "",
    "$B0MMj<TB&$N$4?&6H(B:",
    "",
    "$BAj<jB&$N@+(B:",
    "",
    "$BAj<jB&$NL>(B:",
    "",
    "$BAj<jB&$N@8G/7nF|(B:",
    "",
    "$BAj<jB&$N@-JL(B:",
    "",
    "$BAj<jB&$N$4?&6H(B:",
    "",
    "$B7k:'8e$N@+(B:",
    "",
    "$B$4MWK>;v9`(B:",
    "",
    "",
    "$B$40MMj;v9`(B:",
    "",
    "$B@+(B:",
    "",
    "$BL>(B:",
    "",
    "$B@8G/7nF|(B:",
    "",
    "$B@-JL(B:",
    "",
    "$B$4?&6H(B:",
    "",
    "$B$40MMj;v9`(B:",
    "",
    "====================================="
);
foreach(@body) {
	&jcode'convert(*_, "sjis", "euc");
}
#######Sub$B$N@8@.(B(Base64$B%(%s%3!<%I(B)#######
$subject = "$B2'$X$N$4AjCL(B(Ver.5)";
&jcode'convert(*subject, 'jis', 'euc');
$subject = encode_base64($subject);
chop($subject);
$subject = " . $subject . "?=";
####### $B%X%C%@$NDj5A(B#########
$mail_header = <<"EOM3";
From: $email
To: $okina_email
MIME-Version: 1.0
Content-Type: text/plain;
	charset="x-sjis-jp"
Content-Transfer-Encoding: base64
Subject: $subject
EOM3
####### $B%a%C%;!<%8%\%G%#$N@8@.(B########
$body[4] .= $name;
$body[6] .= $email;
$body[9] .= $order4;
$body[11] .= $familyname1;
$body[13] .= $firstname1;
$body[15] .= $birthday1;
$body[17] .= $sex1;
$body[19] .= $trade1;
$body[21] .= $request1;
$body[24] .= $order5;
$body[26] .= $familyname2;
$body[28] .= $firstname2;
$body[30] .= $family;
$body[32] .= $request2;
$body[35] .= $order6;
$body[37] .= $familyname3;
$body[39] .= $firstname3;
$body[41] .= $birthday3;
$body[43] .= $sex3;
$body[45] .= $trade3;
$body[47] .= $familyname4;
$body[49] .= $firstname4;
$body[51] .= $birthday4;
$body[53] .= $sex4;
$body[55] .= $trade4;
$body[57] .= $sei;
$body[59] .= $request3;
$body[62] .= $order7;
$body[64] .= $familyname5;
$body[66] .= $firstname5;
$body[68] .= $birthday5;
$body[70] .= $sex5;
$body[72] .= $trade5;
$body[74] .= $request5;
$mailbody = join("\r\n", @body);
$encoded = encode_base64($mailbody);
######## $B%a!<%kAw?.(B#########
open(MAIL, "|$sendmail $okina_email");
print MAIL $mail_header;
for ($i = 0; $i < length($encoded); $i += 76) {
	print MAIL substr($encoded, $i, 76);
}
close(MAIL);
#####$B?69~@h$40FFb%a!<%k(B#####
##### $B%\%G%#4pK\J8;zNs$NDj5A(B######
@body2 = (
	"",
	"$B$5$^!";3K\2'$G$9!#(B",
	"$B$3$N$?$S$O!"0J2<$N$40MMj$rD:$-$"$j$,$H$&$4$6$$$^$9!#(B",
	"",
	"",
	"",
	"",
	"$BB~:#!"FbMF$r8+$5$;$FD:$$$F$*$j$^$9!#(B",
	"$B$*<u$1$G$-$k$h$&$G$7$?$i!"?69~@h$N$40FFb$r$5$;$FD:$-$^$9!#(B",
	"$B$7$P$i$/$*BT$AD:$-$^$9$h$&$K$*4j$$CW$7$^$9!#(B",
);
foreach(@body2) {
	&jcode'convert(*_, "sjis", "euc");
}
#######Sub$B$N@8@.(B(Base64$B%(%s%3!<%I(B)#######
$subject = "$B$40MMj$r>5$j$^$7$?!#(B";
&jcode'convert(*subject, 'jis', 'euc');
$subject = encode_base64($subject);
chop($subject);
$subject = " . $subject . "?=";
####### $B%X%C%@$NDj5A(B#########
$mail_header = <<"EOM2";
From: $okina_email2
To: $email
MIME-Version: 1.0
Content-Type: text/plain;
	charset="ISO-2022-JP"
Content-Transfer-Encoding: base64
Subject: $subject
EOM2
####### $B%a%C%;!<%8%\%G%#$N@8@.(B########
$body2[0] .= $name;
$body2[3] .= $order4;
$body2[4] .= $order5;
$body2[5] .= $order6;
$body2[6] .= $order7;
$mailbody = join("\r\n", @body2);
$encoded = encode_base64($mailbody);
######## $B%a!<%kAw?.(B#########
open(MAIL, "|$sendmail $email");
print MAIL $mail_header;
for ($i = 0; $i < length($encoded); $i += 76) {
	print MAIL substr($encoded, $i, 76);
}
close(MAIL);
#####$B0J>e$,(BBase64$B%a!<%k(B#####
print "Content-type: text/html\n\n";
print "<html>\n";
print "<html lang=\"ja\">\n";
print "<head>\n";
print "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=EUC-JP\">\n";
#$B2<5-$N(BURL$B$O!"$"$J$?$N%5(B-$B%P(B-$B$K$"$o$;$F2<$5$$!#(B
print "<META HTTP-EQUIV=\"Refresh\" CONTENT=\"5;URL=/~kazu-y/index.html\">\n";
print "<title>$B$4AjCL<uIU40N;(B</title></head>\n";
print "<body bgcolor=\"ffffff\" TEXT=\"000000\" link=\"fb02ee\" vlink=\"fb02ee\">\n";
print "<p>\n";
print "<br>\n";
print "<br>\n";
print "<center>\n";
print "<font size=\"6\" color=\"000000\"><b>$B$"$j$,$H$&$4$6$$$^$7$?!#(B</b></font><br>\n";
print "<font size=\"3\" color=\"000000\"><b>$B$40MMj3NG'$N%a!<%k$rAw$i$;$FD:$-$^$7$?!#(B</b></font><br>\n";
print "</center>\n";
print "</body>\n";
print "</html>\n";