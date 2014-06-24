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

# $B$^$[$m$P(BWWW2$BMQ(B
$root = "/~kazu-y";
$cgipath = "/~kazu-y/cgi_bin3";
#$baseurl = "http://www2.mahoroba.ne.jp";



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

#$B@+;z(B1$B!&@+;z(B2$B!&L>;z(B1$B!&L>;z(B2$B$N;;=P(B
$seijib = &kakusu(substr($sei1, length($sei1)-2, 2));
$meijia = &kakusu(substr($mei1, 0, 2));
if (length($mei1) == 2) {
	$seijia = $kakusu{'soukaku'} - $kakusu{'jinkaku'};
}else {
	$seijia = $kakusu{'soukaku'} - $kakusu{'chikaku'} - $seijib;
}
$meijib = $kakusu{'soukaku'} - $kakusu{'jinkaku'} - $seijia;


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
#$kyoku = $jinshimo;
#$kyoku = 10 if ($kyoku == 0);
#$kyoku -= 1;
#$kyoku -= $kyoku % 2;
#$kyoku /= 2;
#$kyoku++;

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

<BODY BGCOLOR="#FFFFFF" BACKGROUND="$root/image/wall.jpg">
<P><HTML><HEAD><TITLE>$B%(%i!<%a%C%;!<%8(B</TITLE></HEAD></P>

<P><TABLE BORDER=0 CELLSPACING=0 CELLPADDING=0 WIDTH=640>
   <TR>
      <TD>
         <CENTER><FONT SIZE="+3" COLOR="#FF0000"><B>$BF~NO$5$l$?4A;z!V(B
         \$error $B!W$,H=JL$G$-$^$;$s!#(B</B></FONT>
         
         <P>$B@?$K62$lF~$j$^$9$,!"2<5-$NAw?.%U%)!<%`$r$43NG'8e!"!VAw?.!W%\%?%s$r2!$7$F2<$5$$!#(B<BR>
         $B;3K\2'$,@53N$K4A;z$N2h?tH=Dj$r9T$$!"2<5-%a!<%k%"%I%l%9$^$G$4O"Mm:9$7>e$2$^$9!#(B</P>
         
         <P>$B$*5^$.$N>l9g$K$O!"3:Ev$9$k4A;z$N2h?t$r(B2$B7e$N(B<B>$BH>3Q(B</B>$B;;MQ?t;z$GF~NO$7$F2<$5$$!#(B<BR>
         $BNc!";3EDB@O:"*;3EDB@(B14$B!J!VO:!W$K%(%i!<%a%C%;!<%8$,=P$?>l9g!#!K(B</P>
         
         <P>$B$47@Ls$K4p$E$-%G!<%?%Y!<%9$N99?7:n6H;~$K$O!":#2s$N%(%i!<4A;z$rH?1G$5$;$FD:$-$^$9!#(B</P></CENTER>
         
         <P>
         
         <HR>
         
         </P>
      </TD>
   </TR>
   <TR>
      <TD>
         <CENTER><FONT SIZE="+3"><B>$B2'$+$i$N$*OM$S(B</B></FONT></CENTER>
         
         <P><U>$BJ8;z$N2h?t%G!<%?%Y!<%9$K$D$$$F(B</U></P>
         
         <P>$B8=:_!"L>A0$KMQ$$$i$l$k4A;z$O!"EvMQ4A;z$H?ML>4A;z$G$9!#EPO?4A;z(B
         $B$O$3$N(B4000$BJ8;z0J>e$rLVMe$7$F$*$j$^$9$,!"2a5n$+$i$"$k@+L>$K$O$3$l$K3:Ev$7$J$$$b$N$,4v$D$b$"$j$^$9!#;3K\2'$N7P83$+$i2a5n!"2'$,@\$7$?$3$H$N$"$k@+L>$K$D$$$F$O=PMh$k$+$.$j%G!<%?%Y!<%9$K$OEPO?$7$F$*$j$^$9!#$7$+$7$J$,$i!"A4$F$,EPO?$5$l$F$$$k$H$O8@$$Fq$/!"$^$?EPO?O3$l$,$J$$$H$b8B$j$^$;$s!#(B</P>
         
         <P>$B:#2s$O$=$&8@$C$?5)$J%1!<%9$G$"$k$H;W$o$l$^$9!#@?$K$*<j?t$G$9$,!"2<5-$NFbMF$r$43NG'D:$-(B($B%a!<%k%"%I%l%9$O4IM}<T$N;X<($K=>$C$F$/$@$5$$(B)$B!"Aw?.$7$FD:$1$l$P!"8eF|!"2'$+$i4A;z$N2h?t$r$*CN$i$;CW$7$^$9!#:#8e$N%G!<%?%Y!<%9$KH?1G$5$;$FD:$-$^$9!#(B</P>
         
         <CENTER><FORM ACTION="$cgipath/n_mail2.cgi" METHOD=POST>
            <BLOCKQUOTE><BLOCKQUOTE><CENTER><TABLE BORDER=0 CELLSPACING=10 CELLPADDING=0>
                     <TR>
                        <TD>
                           <P ALIGN=right>$B%(%i!<$K$J$C$?4A;z(B</P>
                        </TD>
                        <TD>
                           <P><INPUT TYPE=hidden NAME=kanji VALUE="\$error" SIZE=10 MAXLENGTH=10>\$error</P>
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
         </FORM></CENTER>
         
         <P>
         
         <HR>
         
         </P>
      </TD>
   </TR>
   <TR>
      <TD>
         <CENTER><A HREF="$root/input3.html" TARGET="_self"><B>$B$b$&0lEY4UDj$9$k(B</B></A>
         
         <P><B>
         
         <HR>
         
         </B></P></CENTER>
      </TD>
   </TR>
   <TR>
      <TD>
         <CENTER><FONT SIZE="-2">$B$3$N%W%m%0%i%`$O4k6H8~$1%$%s%H%i%M%C%HHG$G$9!#(BWWW$B$G$N>&MQMxMQ$O$G$-$^$;$s!#(B<BR>
         $B$3$N%W%m%0%i%`$N%i%$%;%s%9$r<u$1$?4k6H0J30$NBh;0<T$XE>Gd!":FG[IU$r6X;_$7$^$9!#(B<BR>
         <I>CopyRight. K.Yamamoto.1998.9.1</I></FONT></CENTER>
      </TD>
   </TR>
</TABLE>
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
   <TITLE>$B;3K\2'$N4UDj7k2L(B</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=x-sjis">
</HEAD>
<BODY BGCOLOR="#FFFFFF" BACKGROUND="$root/image/wall.jpg">
<P><HTML><HEAD><TITLE>$B;3K\2'$N@+L>H=CG(B</TITLE></HEAD></P>

<CENTER><TABLE BORDER=0 CELLSPACING=0 WIDTH=640>
   <TR>
      <TD>
         <CENTER><FONT SIZE="+3" COLOR="#00CC00"><B>\$seimei$B$5$s$N4UDj7k2L(B</B></FONT></CENTER>
         
         <P>
         
         <HR>
         
         </P>
         
         <P>$B4pAC%G!<%?!'@+(BA=$seijia,$B!!@+(BB=$seijib,$B!!E72h(B=$kakusu{'tenkaku'},$B!!L>(BA=$meijia,$B!!L>(BB=$meijib
<FORM ACTION="seimei.cgi" METHOD=POST>
            <CENTER><TABLE BORDER=0 CELLSPACING=5 WIDTH=160>
               <TR>
                  <TD>
                     <CENTER>$B@+(B<BR>
                     <INPUT TYPE=text NAME=sei VALUE="\$sei" SIZE=10 MAXLENGTH=10></CENTER>
                  </TD>
                  <TD>
                     <CENTER>$BL>(B<BR>
                     <INPUT TYPE=text NAME=mei VALUE="" SIZE=10 MAXLENGTH=10></CENTER>
                  </TD>
               </TR><INPUT TYPE=hidden NAME=sex VALUE="\$sex" size=10 maxlength=10>
       <INPUT TYPE=hidden NAME=marry VALUE="\$marry" size=10 maxlength=10>
               <TR>
                  <TD>
                     <CENTER><INPUT TYPE=submit NAME="$BAw?.(B" VALUE="$B4UDj(B"></CENTER>
                  </TD>
                  <TD>
                     <CENTER><A HREF="$root/input3.html">$BLa$k(B</A></CENTER>
                  </TD>
               </TR>
            </TABLE>
            </CENTER>
         </FORM></P>
      </TD>
   </TR>
   <TR>
      <TD>
         <P><TABLE BORDER=3 CELLSPACING=10 WIDTH="100%">
            <TR>
               <TD VALIGN=top>
                  <P><FONT SIZE="+2" COLOR="#B30000"><B><U>$B<g1?(B</U></B></FONT>
                  <FONT SIZE="-1" COLOR="#B30000">$B!(Ev?M$N0l@8$NCf?4$r;J$j$^$9!#7k:'$K$h$j@+$,JQ$o$k$H<g1?$bJQ$o$j$^$9$,!"CfG/0J9_$K6/$/8=$l$^$9!#(B</FONT></P>
                  
                  <BLOCKQUOTE>$kakusu{'jinkaku'}$B2h!'(B$res{'jinkaku'}</BLOCKQUOTE>
                  
                  <P></P>
               </TD>
               <TD VALIGN=top>
                  <P><FONT SIZE="+2" COLOR="#1D00B3"><B><U>$BBP?M1?!&<R8r1?(B</U></B></FONT>
                  <FONT SIZE="-1" COLOR="#1D00B3">$B!(BP?M4X78$d2HB2!&IWIX4X78!"M'C#4X78$K8=$l$F$-$^$9!#(B</FONT></P>
                  
                  <BLOCKQUOTE>$kakusu{'gaikaku'}$B2h!'(B$res{'gaikaku'}</BLOCKQUOTE>
                  
                  <P></P>
               </TD>
            </TR>
            <TR>
               <TD VALIGN=top>
                  <P><FONT SIZE="+2" COLOR="#007F1F"><B><U>$B7r9/1?(B($BBND4!&@:?@(B)</U></B></FONT>
                  <FONT SIZE="-1" COLOR="#007F1F">$B!(Nc$(5H?tB7$$$N@+L>$G$"$C$F$b!"7r9/$K7C$^$l$J$1$l$P3h$+$5$;$^$;$s!#(B</FONT></P>
                  
                  <BLOCKQUOTE>$res{'kenkou'}</BLOCKQUOTE>
                  
                  <P></P>
               </TD>
               <TD VALIGN=top>
                  <P><FONT SIZE="+2" COLOR="#B35900"><B><U>$B@-3J(B</U></B></FONT>
                  <FONT SIZE="-1" COLOR="#B35900">$B!(Ev?M$N30LLE*$J@-3J$r8=$7$^$9!#<+J,$,B>?M$+$i$I$&8+$($F$$$k$N$+;29M$K$J$j$^$9!#(B</FONT></P>
                  
                  <BLOCKQUOTE>$res{'seikaku'}</BLOCKQUOTE>
                  
                  <P></P>
               </TD>
            </TR>
            <TR>
               <TD VALIGN=top>
                  <P><FONT SIZE="+2" COLOR="#7F0260"><B><U>$B4pAC1?(B</U></B></FONT>
                  <FONT SIZE="-1" COLOR="#7F0260">$B!(MD>/G/4|$N1?@*$N5H6'$r;YG[$7!"@DG/4|$^$G:G$b6/$/:nMQ$7$^$9!#(B($B<cG/<T$NH=CG$O$3$A$i$,M-8z(B)</FONT></P>
                  
                  <BLOCKQUOTE>$kakusu{'chikaku'}$B2h!'(B$res{'chikaku'}</BLOCKQUOTE>
                  
                  <P></P>
               </TD>
               <TD VALIGN=top>
                  <P><FONT SIZE="+2" COLOR="#B30068"><B><U>$BHUG/1?(B</U></B></FONT>
                  <FONT SIZE="-1" COLOR="#B30068">$B!((B50$B:PA08e$+$i6/$/8=$l$F$-$^$9!#$?$@$7!"<g1?$H4pAC1?$K:81&$5$l$^$9$N$GCm0U$7$F2<$5$$!#(B</FONT></P>
                  
                  <BLOCKQUOTE>$kakusu{'soukaku'}$B2h!'(B$res{'soukaku'}</BLOCKQUOTE>
                  
                  <P></P>
               </TD>
            </TR>
         </TABLE>
         
         <HR>
         
         </P>
      </TD>
   </TR>
   <TR>
      <TD>
         <CENTER><A HREF="$root/input3.html" TARGET="_self"><B>$B$b$&0lEY4UDj$r$9$k(B</B></A>
         
         <P><B>
         
         <HR>
         
         </B></P></CENTER>
      </TD>
   </TR>
   <TR>
      <TD>
         <CENTER><FONT SIZE="-2">$B$3$N%W%m%0%i%`$O4k6H8~$1%$%s%H%i%M%C%HHG$G$9!#(BWWW$B$G$N>&MQMxMQ$O$G$-$^$;$s!#(B<BR>
         $B$3$N%W%m%0%i%`$N%i%$%;%s%9$r<u$1$?4k6H0J30$NBh;0<T$XE>Gd!":FG[IU$r6X;_$7$^$9!#(B<BR>
         <I>CopyRight. K.Yamamoto.1999.3.21</I></FONT></CENTER>
      </TD>
   </TR>
</TABLE>
 <FONT SIZE="-1">$B!!(B</FONT>$B!!!!!!(B $B!!!!!!(B</CENTER>
</BODY>
</HTML>


EOM
	&jcode'convert(*msg, "sjis", "euc");
	$msg =~ s/\$seimei/$sei $mei/g;
	$msg =~ s/\$sei/$sei/g;
	$msg =~ s/\$sex/$sex/g;
	$msg =~ s/\$marry/$marry/g;
	print $msg;
}
