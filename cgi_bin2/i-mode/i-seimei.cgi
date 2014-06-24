#!/usr/local/bin/perl
require "jcode.pl";
require "cgi-lib.pl";
require "kakusu.pl";
require "reii.pl";
require "seikaku.pl";
require "kenkou.pl";

# $B2q<R4D6-%F%9%HMQ(B
#$root = "/~nakamura/test/seimei2/public_html";
#$cgipath = "/~nakamura/test/seimei2/cgi_bin";
#$baseurl = "http://ppd.sf.nara.sharp.co.jp";

# $B;30l4D6-MQ(B
$root = "/~kazu-y";
$cgipath = "/~kazu-y/cgi_bin2";
$baseurl = "http://www2.mahoroba.ne.jp";



# CGI$BJQ?t<h$j$3$_(B
&ReadParse();
$sei = $in{'sei'};
$mei = $in{'mei'};
$sex = $in{'sex'};
$marry = $in{'marry'};

$seimei = $sei.$mei;
$incode = &jcode'getcode(*seimei);
if ($incode ne "sjis") {
&jcode'convert(*sei, "sjis", $incode);
&jcode'convert(*mei, "sjis", $incode);
}

$sei =~ s/\s//g;
$mei =~ s/\s//g;

$sei =~ s/\x81\x40//g;
$mei =~ s/\x81\x40//g;

if ($sei eq "" || $mei eq "") {
	print "Location: $baseurl$root/i-mode.html\n\n";
	exit;
}

$sei1 = $sei;
$mei1 = $mei;

# $B!9$N=hM}(B
$sei1 =~ s/(..)\x81\x58/$1$1/;
$mei1 =~ s/(..)\x81\x58/$1$1/;

# $BE72h!&?M2h!&CO2h!&302h!&Am2h$N;;=P(B($B7k9=$d$d$3$7$$(B)
$kakusu{'tenkaku'} = 0;
$kakusu{'chikaku'} = 0;
$kakusu{'gaikaku'} = 0;
$kakusu{'soukaku'} = 0;
@error = ();

# $BE72h$N;;=P(B
for ($i = 0; $i<length($sei1); $i+=2) {
	$kanji = substr($sei1, $i, 2);
	$kakusu = &kakusu($kanji);
	if ($kakusu == 0) {
		push (@error, $kanji);
	}
	$kakusu{'tenkaku'} += $kakusu;
}

# $B0lJ8;z@+$N=hM}(B
if (length($sei1) == 2) {
	$kakusu{'tenkaku'}++; # $B0l2h<Z$j$k(B
	$kakusu{'gaikaku'}++;
	$kakusu{'soukaku'}--; # $B0l2hJV$9(B
}

# $B?M2h$N;;=P(B
$kakusu{'jinkaku'} = &kakusu(substr($sei1, length($sei1)-2, 2)) + &kakusu(substr($mei1, 0, 2));

# $BCO2h$N;;=P(B
for ($i = 0; $i<length($mei1); $i+=2) {
	$kanji = substr($mei1, $i, 2);
	$kakusu = &kakusu($kanji);
	if ($kakusu == 0) {
		push (@error, $kanji);
	}
	$kakusu{'chikaku'} += $kakusu;
}

# $B0lJ8;zL>$N=hM}(B
if (length($mei1) == 2) {
	$kakusu{'chikaku'}++; # $B0l2h<Z$j$k(B
	$kakusu{'gaikaku'}++;
	$kakusu{'soukaku'}--; # $B0l2hJV$9(B
}

# $BAm2h!&302h$N;;=P(B
$kakusu{'soukaku'} += $kakusu{'tenkaku'} + $kakusu{'chikaku'};
$kakusu{'gaikaku'} += $kakusu{'soukaku'} - $kakusu{'jinkaku'};

# $B%*!<%P!<%U%m!<=hM}(B - $B$A$J$_$K(B > 81$B$O4V0c$$$G$O$J$$!#(B
foreach (keys %kakusu) {
	$kakusu{$_} %= 80 if ($kakusu{$_} > 81);
}

# $BE72h!&?M2h!&CO2h$N2<0l7e$N;;=P(B(10$B$G3d$C$?M>$j$r<h$k$@$1(B)
$tenshimo = $kakusu{'tenkaku'} % 10;
$jinshimo = $kakusu{'jinkaku'} % 10;
$chishimo = $kakusu{'chikaku'} % 10;

# $B@-3J?GCG$N=`Hw(B
$kakusu{'seikaku'} = $jinshimo;

# $B1"M[8^9T$N%7%j%"%kHV9f$N;;=P(B($B>\$7$/$O(Bkenkou.pl$B$r;2>H(B)
$kakusu{'kenkou'} = &f($tenshimo)*25 + &f($jinshimo) *5 + &f($chishimo);

# $B6JL>7hDj(B
$kyoku = $jinshimo;
$kyoku = 10 if ($kyoku == 0);
$kyoku -= 1;
$kyoku -= $kyoku % 2;
$kyoku /= 2;
$kyoku++;

# $B@j$$7k2L$N@07A=hM}(B
foreach (keys %kakusu) {
	if ($_ eq "kenkou") {
		$res{$_} = $kenkou[$kakusu{$_}];
	} elsif ($_ eq "seikaku") {
		$res{$_} = $seikaku[$kakusu{$_}];
	} else {
		$res{$_} = $reii[$kakusu{$_}];
	}
	$res{$_} =~ s/\+n/<BR>/g;
	$res{$_} =~ s/\+w.*-w//g if ($sex ne "female");
	$res{$_} =~ s/\+m.*-m//g if ($sex ne "male");
	$res{$_} =~ s/\+k.*-k//g if ($marry ne "yes");
	$res{$_} =~ s/\+u.*-u//g if ($marry ne "no");
	$res{$_} =~ s/\+j.*-j//g if ($_ ne "jinkaku");
	$res{$_} =~ s/\+s.*-s//g if ($_ ne "soukaku");
	$res{$_} =~ s/\+o.*-o//g if ($_ ne "gaikaku");
	$res{$_} =~ s/\+e.*-e//g if ($kakusu{'chikaku'} != 11);
	$res{$_} =~ s/\+t.*-t//g if ($kakusu{'jinkaku'} != 26);
	$res{$_} =~ s/\+g.*-g//g if ($kakusu{'jinkaku'} != 10 && $kakusu{'jinkaku'} != 20);
	$res{$_} =~ s/[\-\+][a-z]//g;
	$res{$_} =~ s/<BR>$//g;
}

if ($#error >= 0) {
	# $B%(%i!<4A;z$,0lJ8;z$G$b$"$l$P%(%i!<I=<((B
	$msg = <<"EOK";
Content-type: text/html

<HTML>
<HEAD>
   <TITLE>$B%(%i!<%a%C%;!<%8(B</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=SHIFT_JIS">
</HEAD>
<BODY BGCOLOR="#FFFFFF" TEXT="#000000" LINK="#0000FF">
<P>

<HR>

<FONT COLOR="#FF0000">$BF~NO$5$l$?4A;z!V(B\$error$B!W$,H=JL$G$-$^$;$s!#(B</FONT><BR>

<HR>

$B@?$K62$lF~$j$^$9$,!"2<5-$NAw?.%U%)!<%`$r$43NG'8e!"!VAw?.!W%\%?%s$r2!$7$F2<$5$$!#(B<BR>
$B@53N$J2h?tH=Dj$r9T$$!"%G!<%?%Y!<%9$r=$@5$7!"$4;XDj$N%a!<%k%"%I%l%9$^$GO"Mm:9$7>e$2$^$9!#$J$*!"@+L>H=CG$G;H$($kJ8;z$O!"A43Q$N$R$i$+$J!&%+%?%+%J!&4A;z$N$_$G$9!#H>3QJ8;z$d5-9f!&?t;z!&1QJ8;z!"N,4A;z$O$4;HMQD:$1$^$;$s!#(B</P>

<P><FORM ACTION="$cgipath/i-n_mail.cgi" METHOD=POST>
   <P>$B%(%i!<$K$J$C$?4A;z!'(B<INPUT TYPE=hidden NAME=kanji VALUE="\$error" size=10 maxlength=10>\$error<BR>
   $B$"$J$?MM$N$*L>A0!'(B<INPUT TYPE=text NAME=name2 VALUE="\$seimei" ISTYLE="1" SIZE=10 MAXLENGTH=10><BR>
   $B%a!<%k%"%I%l%9!'(B<INPUT TYPE=text NAME=email2 VALUE="" ISTYLE="3" SIZE=16 MAXLENGTH=256><BR>
   <INPUT TYPE=submit NAME="$BAw?.(B" VALUE="$BAw?.(B"><BR>
   <INPUT TYPE=reset VALUE="$B<h$j>C$7(B">
</FORM></P>

<P>

<HR>

<A HREF="$root/i-mode.html" accesskey=1>1$B"*$b$&0lEY4UDj$9$k!#(B</A><BR>
<A HREF="$root/i-info.html" accesskey=3>3$B"*2'$+$i$N$*CN$i$;$rFI$`!#(B</A><BR>
</P>
</BODY>
</HTML>
EOK
	&jcode'convert(*msg, "sjis", "euc");
	$msg =~ s/\$seimei/$sei $mei/g;
	$msg =~ s/\$error/@error/g;
	print $msg;
} else {
	# $BH=Dj7k2LI=<((B
	$msg = <<"EOM";
Content-type: text/html

<HTML>
<HEAD>
   <TITLE>$B;3K\2'$N4UDj7k2L(B(1/6)</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=SHIFT_JIS">
</HEAD>
<BODY BGCOLOR="#FFFFFF" TEXT="#000000" LINK="#0000FF">
<P>

<HR>

\$seimei$B$5$s$X$N=u8@(B(1/6)<BR>

<HR>

<FONT COLOR="#FF0000"><U>$B<g1?(B</U>
$B!(Ev?M$N0l@8$NCf?4$r;J$j$^$9!#7k:'$K$h$j@+$,JQ$o$k$H<g1?$bJQ$o$j$^$9$,!"$=$N>l9g$OCfG/0J9_$K6/$/8=$l$^$9!#$^$@$*<c$$J}$O5l@+$GF~NO$7$F$_$F2<$5$$!#(B</FONT></P>

<P>$kakusu{'jinkaku'}$B2h!'(B$res{'jinkaku'}</P>

<P><FORM ACTION="$cgipath/i2seimei.cgi" METHOD=POST>
   <P><INPUT TYPE=hidden NAME=sei VALUE="\$sei" size=10 maxlength=10>
   <INPUT TYPE=hidden NAME=mei VALUE="\$mei" size=10 maxlength=10>
   <INPUT TYPE=hidden NAME=sex VALUE="\$sex" size=10 maxlength=10>
   <INPUT TYPE=hidden NAME=marry VALUE="\$marry" size=10 maxlength=10>
   <INPUT TYPE=submit NAME="$BAw?.(B" VALUE="$BBP?M!&<R8r1?$X(B"><BR>

</FORM>

<HR>

<A HREF="$root/i-mode2.shtml" accesskey=1>1$B"*4UDj$r$d$jD>$9!#(B</A><BR>
</P>
</BODY>
</HTML>
EOM
	&jcode'convert(*msg, "sjis", "euc");
	$msg =~ s/\$seimei/$sei $mei/g;
	$msg =~ s/\$sei/$sei/g;
	$msg =~ s/\$mei/$mei/g;
	$msg =~ s/\$sex/$sex/g;
	$msg =~ s/\$marry/$marry/g;
	print $msg;
}
