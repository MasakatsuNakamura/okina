#!/usr/local/bin/perl
$|=1;
#########################
$sendmail = "/usr/lib/sendmail";
$okina_email = 'okina@e-mail.ne.jp';
#########################
require 'cgi-lib.pl';
require 'jcode.pl';
require "zenhan.pl";
use MIME::Base64;
&ReadParse();
#########################
$name = $in{'name'};
$email = $in{'email'};
$order1 = $in{'order1'};
$order2 = $in{'order2'};
$order3 = $in{'order3'};
$zipcord = $in{'zipcord'};
$address = $in{'address'};
$tel = $in{'tel'};
$fullname = $in{'fullname'};
$familyname = $in{'familyname'};
$brthday = $in{'brthday'};
$user = $in{'user'};
$brother = $in{'brother'};
$request = $in{'request'};
$exp = $in{'exp'};
######$BF~NO%G!<%?$N@07A=hM}(B######
if ($zipcord ne "") {
	$zipcord =~ s/\s*//g;
	#$BA43Q1Q?t;z$r$9$Y$FH>3Q1Q?t;z$K$9$k!#(B
	$zipcord = &zen2han($zipcord); 
}
if ($tel ne "") {
	$tel =~ s/\s*//g;
	#$BA43Q1Q?t;z$r$9$Y$FH>3Q1Q?t;z$K$9$k!#(B
	$tel = &zen2han($tel); 
}
if ($familyname ne "") {
	$familyname =~ s/\s*//g;
}
if ($brthday ne "") {
	$brthday =~ s/\s*//g;
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
if (($order1 eq "" ) and ($order2 eq "" ) and ($order3 eq ""))  {
	&CgiError("$BF~NO%(%i!<(B",
		"$B$4CmJ8$,2?$b;X<($5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
	exit;
}	
if ($order2 ne "") {
	if ($zipcord eq "") {
		&CgiError("$BM9JXHV9f$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
	elsif ($address eq "") {
		&CgiError("$B=;=j$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}	
	elsif ($fullname eq "") {
		&CgiError("$B<u<h?M$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
	elsif ($tel eq "") {
		&CgiError("$BEEOCHV9f$,F~NO$5$l$F$$$^$;$s!#8GDjEEOC$,L5$$;~$K8B$j7HBSHV9f$G$b7k9=$G$9!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
}
if ($order3 ne "") {
	if ($familyname eq "") {
		&CgiError("$BID;z(B($B@+(B)$B$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
	elsif ($brthday eq "") {
		&CgiError("$BM=DjF|(B($BCB@8F|(B)$B$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
}
if ($exp ne "") {
	if ($tel eq "") {
		&CgiError("$BEEOCHV9f$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
	elsif ($zipcord eq "") {
		&CgiError("$BM9JXHV9f$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}
    elsif ($address eq "") {
		&CgiError("$B=;=j$,F~NO$5$l$F$$$^$;$s!#(B",
		"$B%V%i%&%6$N!V(BBack$B!W%\%?%s$GLa$C$F:FF~NO$7$F$/$@$5$$!#(B");
		exit;
	}	
}
#####$B$3$3$+$i(BBase64$B%a!<%k(B#####
##### $B%\%G%#4pK\J8;zNs$NDj5A(B######
@body = (
	"=====================================", 
	"$B;3K\2'$5$^$X!"0J2<$NCmJ8$rCW$7$?$/!#(B", 
	"", 
	"$B?=9~?MMM$N;aL>!'(B", 
	"", 
	"$B?=9~?MMM$N(BE$B%a!<%k%"%I%l%9!'(B", 
	"", 
	"$B$4CmJ8FbMF!'(B",
	"",
	"", 
	"",  
	"$B=q@R$NAwIU@h$^$?$OO"Mm@h(B", 
	"$BM9JXHV9f!'(B", 
	"", 
	"$B$4=;=j!'(B", 
	"", 
	"$B$*EEOCHV9f!'(B", 
	"", 
	"$B<u<h?MMM!'(B", 
	"", 
	"$BL?L>$N$40MMjFbMF!'(B", 
	"", 
	"$B@+(B($B$_$g$&$8(B)$B!'(B", 
	"", 
	"$B=P;:M=DjF|!'(B", 
	"", 
	"$B:#$^$G$NMxMQ!'(B", 
	"", 
	"$B7;;P$N$*L>A0!'(B", 
	"", 
	"$B$4MWK>;v9`!'(B", 
	"", 
	"====================================="
);
foreach(@body) {
	&jcode'convert(*_, "sjis", "euc");
}
#######Sub$B$N@8@.(B(Base64$B%(%s%3!<%I(B)#######
$subject = "$B2'$X$4CmJ8(B(Ver.7)";
&jcode'convert(*subject, 'jis', 'euc');
$subject = encode_base64($subject);
chop($subject);
$subject = " . $subject . "?=";
####### $B%X%C%@$NDj5A(B#########
$mail_header = <<"EOM";
From: $email
To: $okina_email
MIME-Version: 1.0
Content-Type: text/plain;
	charset="x-sjis-jp"
Content-Transfer-Encoding: base64
Subject: $subject
EOM
####### $B%a%C%;!<%8%\%G%#$N@8@.(B########
$body[4] .= $name;
$body[6] .= $email;
$body[8] .= $order1;
$body[9] .= $order2;
$body[10] .= $order3;
$body[13] .= $zipcord;
$body[15] .= $address;
$body[17] .= $tel;
$body[19] .= $fullname;
$body[21] .= $exp;
$body[23] .= $familyname;
$body[25] .= $brthday;
$body[27] .= $user;
$body[29] .= $brother;
$body[31] .= $request;
$mailbody = join("\r\n", @body);
$encoded = encode_base64($mailbody);
######## $B%a!<%kAw?.(B#########
open(MAIL, "|$sendmail $okina_email");
print MAIL $mail_header;
for ($i = 0; $i < length($encoded); $i += 76) {
	print MAIL substr($encoded, $i, 76);
}
close(MAIL);
#####$B0J>e$,(BBase64$B%a!<%k(B#####
print "Content-type: text/html\n\n";
print "<html>\n";
print "<head>\n";
print "<META HTTP-EQUIV=\"Refresh\" CONTENT=\"5;URL=/~kazu-y/index.html\">\n";
print "<title>$B$4CmJ8<uIU40N;(B</title></head>\n";
print "<body bgcolor=\"ffffff\" TEXT=\"000000\" link=\"fb02ee\" vlink=\"fb02ee\">\n";
print "<p>\n";
print "<br>\n";
print "<br>\n";
print "<center>\n";
print "<font size=\"6\" color=\"000000\"><b>$B$"$j$,$H$&$4$6$$$^$7$?!#(B</b></font><br>\n";
print "</center>\n";
print "</body>\n";
print "</html>\n";