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
	print "Location: $baseurl$root/input.html\n\n";
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
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=x-sjis">
</HEAD>

<BODY BGCOLOR="#FFFFFF">
<CENTER><FONT SIZE="+3"><B>$BF~NO$5$l$?4A;z!V(B\$error$B!W(B
$B$,H=JL$G$-$^$;$s!#(B</B></FONT>

<P>$B@?$K62$lF~$j$^$9$,!"(B<A HREF="#form" TARGET="_self"><B>$B2<5-$N%U%)!<%`(B</B></A>$B$N$K$45-F~$N>e!"Aw?.%\%?%s$r2!$7$F$/$@$5$$!#(B<BR>
$B4A;z%G!<%?%Y!<%9$N=$@5$,40N;$7$^$7$?$i!"$4;XDj$N%a!<%k%"%I%l%9$^$G$4O"Mm:9$7>e$2$^$9!#(B</P>

<P>

<HR>

<FONT SIZE="+3"><B>$B2'$+$i$N$*OM$S(B</B></FONT></P></CENTER>

<P><U>$BJ8;z$N2h?t%G!<%?%Y!<%9$K$D$$$F(B</U></P>

<P>$B8=:_!"L>A0$KMQ$$$i$l$k4A;z$O!"EvMQ4A;z$H?ML>4A;z$G$9!#EPO?4A;z(B
$B$O$3$NLs(B2000$BJ8;z$rLVMe$7$F$*$j$^$9$,!"2a5n$+$i$"$k@+L>$K$O$3$l$K3:Ev$7$J$$$b$N$,4v$D$+$"$j$^$9!#;3K\2'$N7P83$+$i2a5n!"2'$,@\$7$?$3$H$N$"$k@+L>$K$D$$$F$O=PMh$k$+$.$j%G!<%?%Y!<%9$K$OEPO?$7$F$*$j$^$9!#$7$+$7$J$,$i!"A4$F$,EPO?$5$l$F$$$k$H$O8@$$Fq$/!"$^$?EPO?O3$l$,$J$$$H$b8B$j$^$;$s!#(B</P>

<P>$B:#2s$O$=$&8@$C$?5)$J%1!<%9$G$"$k$H;W$o$l$^$9!#@?$K$*<j?t$G$9$,!"2<5-$N%U%)!<%`$K$45-F~D:$-$^$7$?$i!"8eF|$3$A$i$h$j7k2L$r$4O"Mm$5$;$F$$$?$@$-$^$9!#:#8e$N%G!<%?%Y!<%9$KH?1G$5$;$FD:$-$?$$$H9M$($^$9$N$G!"$46(NO59$7$/$*4j$$?=$7>e$2$^$9!#(B</P>

<CENTER><FORM ACTION="$cgipath/gn_mail2.cgi" METHOD=POST>
   <BLOCKQUOTE><BLOCKQUOTE><CENTER><A NAME=form></A><TABLE BORDER=0 CELLSPACING=10 CELLPADDING=0>
            <TR>
               <TD>
                  <P ALIGN=right>$B%(%i!<$K$J$C$?4A;z(B</P>
               </TD>
               <TD>
                  <P><INPUT TYPE=hidden NAME=kanji VALUE="\$error" size=10 maxlength=10>\$error</P>
               </TD>
            </TR>
            <TR>
               <TD>
                  <P ALIGN=right>$B$*L>A0(B</P>
               </TD>
               <TD>
                  <P><INPUT TYPE=text NAME=name2 VALUE="\$seimei" SIZE=20 MAXLENGTH=10></P>
               </TD>
            </TR>
            <TR>
               <TD>
                  <P ALIGN=right>$B%a!<%k%"%I%l%9(B</P>
               </TD>
               <TD>
                  <P><INPUT TYPE=text NAME=email2 VALUE="" SIZE=40></P>
               </TD>
            </TR>
            <TR>
               <TD>
                  <P></P>
               </TD>
               <TD>
                  <P><INPUT TYPE=submit NAME="$BAw?.(B" VALUE="$BAw?.(B"><INPUT TYPE=reset VALUE="$B<h$j>C$7(B"></P>
               </TD>
            </TR>
         </TABLE>
         </CENTER></BLOCKQUOTE></BLOCKQUOTE>
</FORM>

<P>

<HR>

<TABLE BORDER=1 WIDTH=600>
   <TR>
      <TD>
         <CENTER><A HREF="$root/g-index.html" TARGET="_self"><B>$B%H%C%W%Z!<%8(B</B></A></CENTER>
      </TD>
      <TD>
         <CENTER><A HREF="$root/g-input.html" TARGET="_self"><B>$B$b$&0lEY4UDj$9$k(B</B></A></CENTER>
      </TD>
      <TD>
         <CENTER><A HREF="$root/g-book.html" TARGET="_self"><B>$BCx=q$N%3!<%J!<(B</B></A></CENTER>
      </TD>
      <TD>
         <CENTER><A HREF="$root/g-baby.html" TARGET="_self"><B>$BL?L>$N%3!<%J!<(B</B></A></CENTER>
      </TD>
      <TD>
         <CENTER><A HREF="$root/g-info.html"><B>$B2'$+$i$N$*CN$i$;(B</B></A></CENTER>
      </TD>
   </TR>
</TABLE>
 $B!!!!(B <FONT SIZE="-2">

<HR>

$B%j%s%/$O4?7^$7$^$9$,!"I,$:(B</FONT><A HREF="$root/g-index.html" TARGET="_self"><FONT SIZE="-2"><I>TOP$B%Z!<%8(B</I></FONT></A><FONT SIZE="-2">$B$X$*4j$$$7$^$9!#(B<BR>
$B$3$N%3%s%F%s%D$N>&MQMxMQ$J$i$S$KL5CGE>:\$O$*CG$jCW$7$^$9!#(B<BR>
<I>CopyRight. K.Yamamoto.1999.5.8</I></FONT></P></CENTER>
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
   <TITLE>$B;3K\2'$N4UDj7k2L(B</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=x-sjis">
</HEAD>

<BODY BGCOLOR="#FFFFFF">
<CENTER><TABLE BORDER=0 CELLSPACING=0 WIDTH=600>
   <TR>
      <TD>
         <P><TABLE BORDER=0 CELLSPACING=0 CELLPADDING=0 WIDTH="100%">
            <TR>
               <TD VALIGN=top WIDTH=300 HEIGHT=170 BGCOLOR="#CCCCCC">
                  <CENTER><FONT SIZE="+2" COLOR="#0033FF"><B><TABLE BORDER=0 CELLSPACING=0 CELLPADDING=0 WIDTH=300>
                     <TR>
                        <TD VALIGN=bottom>
                           <CENTER><IMG SRC="$root/image/g-result.jpg" WIDTH=300 HEIGHT=240 ALIGN=top></CENTER>
                        </TD>
                     </TR>
                     <TR>
                        <TD>
                           <CENTER><FONT SIZE="+2"><B>\$seimei$B$5$s$X$N=u8@(B</B></FONT></CENTER>
                        </TD>
                     </TR>
                  </TABLE>
                   </B></FONT></CENTER>
               </TD>
               <TD VALIGN=top WIDTH=300 HEIGHT=170 BGCOLOR="#CCCCCC">
                  <CENTER><B><U>$B;3K\2'$h$j(B</U></B></CENTER>
                  
                  <P>$B!!<g1?!&BP?M1?!&4pAC1?!&HUG/1?$H0l8+L7=b$9$k$h$&$J7k2L$r<($9$3$H$b$"$j$^$9!#$3$l$O?M4V$H$$$&$b$N$O!"308+$HK\?4$,0c$&$N$b>o$G$9$7!"?M@8$bGH$"$jIw$"$j$H$$$&$3$H$G!"4UDj7k2L$K$b$=$l$O8=$l$F$-$F$$$k$H$4M}2r2<$5$$!#=>$C$F!"$^$:4UDj7k2LA4BN$rD/$a$FD:$-!"<!$K8D!9$NItJ,$K$D$$$F<+J,$J$j$KJ,@O$5$l$F$_$k;v$r$*A&$a$7$^$9!#$J$*!"K\Ev$N4UDj$H$$$&$N$O!"A0=R$N$h$&$J?M$=$l$>$l$N6-6x$d2s$j$N4D6-$rAm9gE*$K2CL#$7$FH=CG$9$k$N$G$9$,!"%$%s%?!<%M%C%H$G$O$=$3$^$G$N;v$,=PMh$^$;$s$N$G!"0-$7$+$i$:$4N;>52<$5$$!#(B</P>
               </TD>
            </TR>
         </TABLE>
         </P>
         
         <P>
         
         <HR>
         
         </P>
      </TD>
   </TR>
   <TR>
      <TD>
         <P><TABLE BORDER=3 CELLSPACING=10 WIDTH="100%">
            <TR>
               <TD VALIGN=top>
                  <P><FONT SIZE="+2"><B>$B<g1?(B</B>
                  </FONT><FONT SIZE="-1"><U>$B!(Ev?M$N0l@8$NCf?4$r;J$j$^$9!#7k:'$K$h$j@+$,JQ$o$k$H<g1?$bJQ$o$j$^$9$,!"CfG/0J9_$K6/$/8=$l$^$9!#(B</U></FONT></P>
                  
                  <BLOCKQUOTE>$kakusu{'jinkaku'}$B2h!'(B$res{'jinkaku'}</BLOCKQUOTE>
                  
                  <P></P>
               </TD>
               <TD VALIGN=top>
                  <P><FONT SIZE="+2"><B>$BBP?M1?!&<R8r1?(B</B></FONT><FONT SIZE="-1"><B>
                  </B><U>$B!(BP?M4X78$d2HB2!&IWIX4X78!"M'C#4X78$K8=$l$F$-$^$9!#(B</U></FONT></P>
                  
                  <BLOCKQUOTE>$kakusu{'gaikaku'}$B2h!'(B$res{'gaikaku'}</BLOCKQUOTE>
                  
                  <P></P>
               </TD>
            </TR>
            <TR>
               <TD VALIGN=top>
                  <P><FONT SIZE="+2"><B>$B7r9/1?(B($BBND4!&@:?@(B)
                  </B></FONT><FONT SIZE="-1"><U>$B!(Nc$(5H?tB7$$$N@+L>$G$"$C$F$b!"7r9/$K7C$^$l$J$1$l$P3h$+$5$;$^$;$s!#(B</U></FONT></P>
                  
                  <BLOCKQUOTE>$res{'kenkou'}</BLOCKQUOTE>
                  
                  <P></P>
               </TD>
               <TD VALIGN=top>
                  <P><FONT SIZE="+2"><B>$B@-3J(B
                  </B></FONT><FONT SIZE="-1"><U>$B!(Ev?M$N30LLE*$J@-3J$r8=$7$^$9!#<+J,$,B>?M$+$i$I$&8+$($F$$$k$N$+;29M$K$J$j$^$9!#(B</U></FONT></P>
                  
                  <BLOCKQUOTE>$res{'seikaku'}</BLOCKQUOTE>
                  
                  <P></P>
               </TD>
            </TR>
            <TR>
               <TD VALIGN=top>
                  <P><FONT SIZE="+2"><B>$B4pAC1?(B
                  </B></FONT><FONT SIZE="-1"><U>$B!(MD>/G/4|$N1?@*$N5H6'$r;YG[$7!"@DG/4|$^$G:G$b6/$/:nMQ$7$^$9!#(B($B<cG/<T$NH=CG$O$3$A$i$,M-8z(B)</U></FONT></P>
                  
                  <BLOCKQUOTE>$kakusu{'chikaku'}$B2h!'(B$res{'chikaku'}</BLOCKQUOTE>
                  
                  <P></P>
               </TD>
               <TD VALIGN=top>
                  <P><FONT SIZE="+2"><B>$BHUG/1?(B
                  </B></FONT><FONT SIZE="-1"><U>$B!((B50$B:PA08e$+$i6/$/8=$l$F$-$^$9!#$?$@$7!"<g1?$H4pAC1?$K:81&$5$l$^$9$N$GCm0U$7$F2<$5$$!#(B</U></FONT></P>
                  
                  <BLOCKQUOTE>$kakusu{'soukaku'}$B2h!'(B$res{'soukaku'}</BLOCKQUOTE>
                  
                  <P></P>
               </TD>
            </TR>
         </TABLE>
         </P>
         
         <CENTER><B>$B4UDj7k2L$,5$$K$J$kJ}$O!"!VCx=q$N%3!<%J!<!W!V2'$+$i$N$*CN$i$;!W$bJ;$;$F$4Mw2<$5$$!#(B</B></CENTER>
         
         <P>
         
         <HR>
         
         </P>
      </TD>
   </TR>
   <TR>
      <TD>
         <P><TABLE BORDER=1 WIDTH="100%">
            <TR>
               <TD>
                  <CENTER><A HREF="$root/i-geti.html" TARGET="_self"><B>$B%H%C%W%Z!<%8(B</B></A></CENTER>
               </TD>
               <TD>
                  <CENTER><A HREF="$root/g-input.html" TARGET="_self"><B>$B$b$&0lEY4UDj$9$k(B</B></A></CENTER>
               </TD>
               <TD>
                  <CENTER><A HREF="$root/g-book.html" TARGET="_self"><B>$BCx=q$N%3!<%J!<(B</B></A></CENTER>
               </TD>
               <TD>
                  <CENTER><A HREF="$root/g-baby.html" TARGET="_self"><B>$BL?L>$N%3!<%J!<(B</B></A></CENTER>
               </TD>
               <TD>
                  <CENTER><A HREF="$root/g-info.html" TARGET="_self"><B>$B2'$+$i$N$*CN$i$;(B</B></A></CENTER>
               </TD>
            </TR>
         </TABLE>
         
         <HR>
         
         </P>
      </TD>
   </TR>
   <TR>
      <TD>
         <CENTER>$B$3$N%3%s%F%s%D$O%7%c!<%W(B($B3t(B)$BEB$N%6%&%k%9%"%$%2%F%#(B<FONT SIZE="-2">(TM)</FONT>$B8~$1$KFCJLJT=8$5$l$?$b$N$G$9!#(B<BR>
         $B%U%k%P!<%8%g%s$O(B<A HREF="http://www2.mahoroba.ne.jp/~kazy-y/index.html">$B$3$A$i(B</A>$B$r$4Mw2<$5$$!#(B
         
         <P>
         
         <HR>
         
         </P></CENTER>
      </TD>
   </TR>
   <TR>
      <TD>
         <CENTER><FONT SIZE="-2">$B$3$N7k2L$r8+$F$N$40U8+$d$446A[$r$*J9$+$;2<$5$$!#!!(B</FONT><A HREF="mailto:okina\@e-mail.ne.jp"><FONT SIZE="-2">okina\@e-mail.ne.jp</FONT></A><FONT SIZE="-2"><I><BR>
         </I>$B%j%s%/$O4?7^$7$^$9$,!"I,$:(B</FONT><A HREF="$root/i-geti.html" TARGET="_self"><FONT SIZE="-2">TOP$B%Z!<%8(B</FONT></A><FONT SIZE="-2">$B$X$*4j$$$7$^$9!#(B<BR>
         $B$3$N%3%s%F%s%D$N>&MQMxMQ$J$i$S$KL5CGE>:\$O$*CG$j$$$?$7$^$9!#$3$N4UDj$OL5NA$G$9!#(B<BR>
         <I>CopyRight. K.Yamamoto. 1999.5.8</I></FONT></CENTER>
      </TD>
   </TR>
</TABLE>
</CENTER>

<P>$B!!(B</P>

<P><FONT SIZE="-1">$B!!(B</FONT></P>

<CENTER>$B!!!!!!(B $B!!!!!!(B</CENTER>
</BODY>
</HTML>


EOM
	&jcode'convert(*msg, "sjis", "euc");
	$msg =~ s/\$seimei/$sei $mei/g;
	print $msg;
}
