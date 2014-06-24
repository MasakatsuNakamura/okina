#!/usr/bin/perl
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

# $B!5$N=hM}(B
$sei1 =~ s/(..)\x81\x54/$1$1/;
$mei1 =~ s/(..)\x81\x54/$1$1/;

# $B!8$N=hM}(B
$sei1 =~ s/(..)\x81\x57/$1$1/;
$mei1 =~ s/(..)\x81\x57/$1$1/;

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

<BODY BGCOLOR="#FFFFFF" BACKGROUND="$root/image/wall.jpg">
<P><HTML><HEAD><TITLE>$B%(%i!<%a%C%;!<%8(B</TITLE></HEAD></P>

<P><TABLE BORDER=0 WIDTH=640>
   <TR>
      <TD>
         <CENTER><FONT SIZE="+3"><B>$BF~NO$5$l$?4A;z(B $B!V(B\$error$B!W(B
         $B$,H=JL$G$-$^$;$s!#(B</B></FONT>
         
         <P>$B@?$K62$lF~$j$^$9$,!"(B<A HREF="#form" TARGET="_self"><B>$B2<5-$N%U%)!<%`(B</B></A>$B$N$K$45-F~$N>e!"Aw?.%\%?%s$r2!$7$F$/$@$5$$!#(B<BR>
         $B4A;z%G!<%?%Y!<%9$N=$@5$,40N;$7$^$7$?$i!"$4;XDj$N%a!<%k%"%I%l%9$^$G$4O"Mm:9$7>e$2$^$9!#$^$?!"4A;z!&$R$i$+$J!&%+%?%+%J0J30$N1QJ8;z!&?t;z!&3(J8;z!&5-9f$J$I$O;3K\<0@+L>H=CG$G$O07$C$F$*$j$^$;$s$N$G!"O"Mm$OITMW$G$9!#2<5-$N!V$b$&0lEY4UDj$9$k!W$r2!$7$F2<$5$$!#(B</P></CENTER>
         
         <P>
         
         <HR>
         
         </P>
      </TD>
   </TR>
   <TR>
      <TD>
         <CENTER><FONT SIZE="+3"><B>$B2'$+$i$N$*OM$S(B</B></FONT></CENTER>
         
         <P><U>$BJ8;z$N2h?t%G!<%?%Y!<%9$K$D$$$F(B</U></P>
         
         <P>$B8=:_!"L>A0$KMQ$$$i$l$k4A;z$O!"EvMQ4A;z$H?ML>4A;z$G$9!#$3$l0J30$K$b<B:]$K;H$o$l$F$$$k@+L>$K$O$3$l$K3:Ev$7$J$$$b$N$,4v$D$b$"$j$^$9!#8=:_!"$3$l$i$NCf$+$i(B4580$BJ8;z(B(2003.9$B8=:_(B)$B$r%G!<%?%Y!<%9$KEPO?$7$F$*$j$^$9!#$3$l$i$O!";3K\2'$N4UDjNr(B50$BG/$N7P83$K4p$E$/$b$N$G$9!#$7$+$7$J$,$i!"$^$@A4$F$,EPO?$5$l$F$$$k$H$O8@$$Fq$/!"$^$?EPO?O3$l$,$J$$$H$b8B$j$^$;$s!#(B</P>
         
         <P>$B:#2s$O$=$&8@$C$?5)$J%1!<%9$G$"$k$H;W$o$l$^$9!#@?$K$*<j?t$G$9$,!"2<5-$N%U%)!<%`$K$45-F~D:$-$^$7$?$i!"8eF|$3$A$i$h$j7k2L$r$4O"Mm$5$;$F$$$?$@$-$^$9!#:#8e$N%G!<%?%Y!<%9$KH?1G$5$;$FD:$-$?$$$H9M$($^$9$N$G!"$46(NO59$7$/$*4j$$?=$7>e$2$^$9!#(B<BR>
         $B$*4j$$!'7k2L$N$*CN$i$;$,I,MW$G$J$$J}$O!"%a!<%k%"%I%l%9$r6uGr$N$^$^Aw?.2<$5$$!#4V0c$C$?%"%I%l%9$r5-F~$5$l$^$9$HB>$NJ}$K8fLBOG$,$+$+$j$^$9!#(B</P>
         
         <CENTER><FORM ACTION="$cgipath/n_mail2.cgi" METHOD=POST>
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
         
         <P><FONT SIZE="+2">
         
         <HR>
         
         </FONT><A HREF="$root/input.html" TARGET="_self"><FONT SIZE="+1">$B$b$&0lEY4UDj$9$k(B</FONT></A></P></CENTER>
         
         <P>
         
         <HR>
         
         </P>
      </TD>
   </TR>
   <TR>
      <TD>
         <P><TABLE BORDER=0 WIDTH=640>
            <TR>
               <TD>
                  <CENTER><A HREF="$root/index.html" TARGET="_self">$B%H%C%W%Z!<%8(B</A></CENTER>
               </TD>
               <TD>
                  <CENTER><A HREF="$root/book.html" TARGET="_self">$BCx=q$N%3!<%J!<(B</A></CENTER>
               </TD>
               <TD>
                  <CENTER><A HREF="$root/baby.html" TARGET="_self">$BL?L>$N%3!<%J!<(B</A></CENTER>
               </TD>
            </TR>
            <TR>
               <TD>
                  <CENTER><A HREF="$root/consul.html">$B$4AjCL$N%3!<%J!<(B</A></CENTER>
               </TD>
               <TD>
                  <CENTER><A HREF="$root/info.html">$B2'$+$i$N$*CN$i$;(B</A></CENTER>
               </TD>
               <TD>
                  <CENTER><A HREF="$root/link.html">$B!V@j$$D>9TJX!W(B</A></CENTER>
               </TD>
            </TR>
         </TABLE>
         
         <HR>
         
         </P>
      </TD>
   </TR>
   <TR>
      <TD>
         <CENTER>$B!!!!(B
         <FONT SIZE="-2">$B%j%s%/$O4?7^$7$^$9$,!"I,$:(B</FONT><A HREF="$root/index.html" TARGET="_self"><FONT SIZE="-2"><I>TOP$B%Z!<%8(B</I></FONT></A><FONT SIZE="-2">$B$X$*4j$$$7$^$9!#(B<BR>
         $B$3$N%3%s%F%s%D$N>&MQMxMQ$J$i$S$KL5CGE>:\$O$*CG$jCW$7$^$9!#(B<BR>
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

<BODY BGCOLOR="#FFFFFF" BACKGROUND="$root/image/wall.jpg" onload="scll()">
<P><SCRIPT LANGUAGE=JavaScript>var cnt = -2;//$BJ8;z0LCV(B
var speed = 500;//$BF0$+$9%9%T!<%I(B(1/1000$BICC10L(B)
var msg = "              Web$B$G=i$a$F!*(B $B4UDj7k2L$K$h$C$F2;3Z$,(B5$BDL$j$KJQ2=$7$^$9!#4UDj$N:,5r$d?M@8$r$h$jNI$/@8$-$kJ}K!$K$D$$$F$O!";d$NCx=q$r$4Mw$/$@$5$$!#7k2L$r$h$j>\$7$/CN$j$?$$J}!"2~L>$r4uK>$5$l$kJ}!"$47k:'$NM=Dj$N$"$kJ}$O!"M-NA$N$4AjCL%3!<%J!<$b3+@_$7$F$*$j$^$9$N$G!"$4MxMQ2<$5$$!#$^$?!"%Q!<%H%J!<$r$*C5$7$NJ}$O!"$3$N%Z!<%8$N9-9p$r$4;2>H2<$5$$!#(B"; //$B%a%C%;!<%8FbMF(B
timeID=setTimeout('',1); //IE$BBP:v$J$K$b$7$J$$(B;$B%?%$%^!<%;%C%H(B

//$B!!J8;z$r0\F0$5$;$k(B
function scll()
{
 status = msg.substring(cnt=cnt+2,msg.length+2);//$BF|K\8l$O(B2$BJ8;z$E$DF0$+$9(B
 if (cnt>msg.length){cnt=-2};
 clearTimeout(timeID);//$B%?%$%^!<$r%/%j%"(B
 timeID = setTimeout('scll()',speed);
  }</SCRIPT></P>

<P><HTML><HEAD><TITLE>$B;3K\2'$N4UDj7k2L(B</TITLE></HEAD></P>

<CENTER><TABLE BORDER=0 CELLSPACING=0 WIDTH=640>
   <TR>
      <TD>
         <P><TABLE BORDER=0 CELLSPACING=0 CELLPADDING=0 WIDTH="100%">
            <TR>
               <TD VALIGN=top WIDTH=320 HEIGHT=240 BGCOLOR="#CCCC99">
                  <CENTER><FONT SIZE="+2" COLOR="#0033FF"><B><TABLE BORDER=0 CELLSPACING=0 CELLPADDING=0 WIDTH=320 HEIGHT=240>
                     <TR>
                        <TD VALIGN=bottom BACKGROUND="$root/image/result.jpg">
                           <CENTER><FONT SIZE="+2" COLOR="#9933FF"><B>\$seimei$B$5$s$X$N=u8@(B</B></FONT></CENTER>
                        </TD>
                     </TR>
                  </TABLE>
                   </B></FONT></CENTER>
               </TD>
               <TD VALIGN=top WIDTH=320 HEIGHT=240 BGCOLOR="#CCCC99">
                  <CENTER><B><U>$B;3K\2'$h$j(B</U></B></CENTER>
                  
                  <P>$B!!<g1?!&BP?M1?!&4pAC1?!&HUG/1?$H0l8+L7=b$9$k$h$&$J7k2L$r<($9$3$H$b$"$j$^$9!#$3$l$O?M4V$H$$$&$b$N$O!"308+$HK\?4$,0c$&$N$b>o$G$9$7!"?M@8$bGH$"$jIw$"$j$H$$$&$3$H$G!"4UDj7k2L$K$b$=$l$O8=$l$F$-$F$$$k$H$4M}2r2<$5$$!#=>$C$F!"$^$:4UDj7k2LA4BN$rD/$a$FD:$-!"<!$K8D!9$NItJ,$K$D$$$F<+J,$J$j$KJ,@O$5$l$F$_$k;v$r$*A&$a$7$^$9!#$J$*!"K\Ev$N4UDj$H$$$&$N$O!"A0=R$N$h$&$J?M$=$l$>$l$N6-6x$d2s$j$N4D6-$rAm9gE*$K2CL#$7$FH=CG$9$k$N$G$9$,!"%$%s%?!<%M%C%H$G$O$=$3$^$G$N;v$,=PMh$^$;$s$N$G!"0-$7$+$i$:$4N;>52<$5$$!#(B</P>
               </TD>
            </TR>
         </TABLE>
         </P>
         
         <P><IMG SRC="$root/image/line_j.gif" WIDTH=640 HEIGHT=17 ALIGN=bottom></P>
         
         <P></P>
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
                  <FONT SIZE="-1" COLOR="#007F1F">$B!(Nc$(5H?tB7$$$N@+L>$G$"$C$F$b!"7r9/$K7C$^$l$J$1$l$P3h$+$5$;$^$;$s!#!J"$$OC1FH$G$NH=CG$,Fq$7$$!K(B</FONT></P>
                  
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
         <BR>
         <IMG SRC="../../image/line_a1.gif" WIDTH=640 HEIGHT=3 ALIGN=bottom></P>
         
         <P>$B!!7k2L$OG!2?$G$7$g$&$+!)!!;3K\2'$G$OMM!9$J(B<FONT COLOR="#FF0000">$BM-NA%5!<%S%9(B</FONT>$B$b<B;\$7$F$*$j$^$9$N$G!"$h$m$7$1$l$P$=$A$i$b$4MxMQ2<$5$$!#$^$?!"0lHLE*$KNI$/J9$+$l$k$4<ALd$K$D$$$F(B<A HREF="$root/info.html">$B!V$*CN$i$;%3!<%J!<!W(B</A>$B$KE;$a$F$$$^$9$N$G!"J;$;$F$4Mw2<$5$$!#(B</P>
         
         <CENTER><IMG SRC="$root/image/line_a2.gif" WIDTH=640 HEIGHT=3 ALIGN=bottom>
         
         <P><TABLE BORDER=0 WIDTH="61%">
            <TR>
               <TD COLSPAN=5>
                  <CENTER><B>$BB>$N%Z!<%8$b$<$R8+$K9T$C$F$/$@$5$$!#(B</B></CENTER>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=68>
                  <CENTER><A HREF="$root/input.html" TARGET="_self"><FONT SIZE="+1" FACE="$BCf%4%7%C%/BN(B"><IMG SRC="$root/image/seimei.gif" WIDTH=57 HEIGHT=71 BORDER=3 ALIGN=bottom></FONT></A></CENTER>
               </TD>
               <TD WIDTH=70>
                  <CENTER><A HREF="$root/book.html" TARGET="_self"><FONT SIZE="+1" FACE="$BCf%4%7%C%/BN(B"><IMG SRC="$root/image/chosyo.gif" WIDTH=57 HEIGHT=71 BORDER=3 ALIGN=bottom></FONT></A></CENTER>
               </TD>
               <TD WIDTH=73>
                  <CENTER><A HREF="$root/baby.html" TARGET="_self"><FONT SIZE="+1" FACE="$BCf%4%7%C%/BN(B"><IMG SRC="$root/image/baby-name.gif" WIDTH=57 HEIGHT=71 BORDER=3 ALIGN=bottom></FONT></A></CENTER>
               </TD>
               <TD WIDTH=72>
                  <CENTER><A HREF="$root/consul.html"><IMG SRC="$root/image/consul.gif" WIDTH=57 HEIGHT=71 BORDER=3 ALIGN=bottom></A></CENTER>
               </TD>
               <TD>
                  <CENTER><A HREF="$root/link.html"><IMG SRC="$root/image/d-rink.gif" WIDTH=57 HEIGHT=71 BORDER=3 ALIGN=bottom></A></CENTER>
               </TD>
            </TR>
         </TABLE>
         </P>
         
         <P><IMG SRC=".$root/image/line_a2.gif" WIDTH=640 HEIGHT=3 ALIGN=bottom></P>
         
         <P><B><U>$B$3$3$+$i$O!"9-9p$G$9!#(B</U></B></P>
         
         <P>$B$"$J$?$N?M@8$N%Q!<%H%J!<$O$b$&8+$D$+$j$^$7$?$+!)AG@2$i$7$$=P2q$$$r8+$D$1$F2<$5$$!#(B<BR>
         <A HREF="http://love.nozze-deai.com/guest/SZX00101/" TARGET="_blank"><IMG SRC="$root/image/nozze3.gif" WIDTH=468 HEIGHT=60 BORDER=0 ALIGN=bottom></A></P>

         <P><CENTER>
<TABLE BORDER=0 WIDTH=468 HEIGHT=80 CELLPADDING=0 CELLSPACING=0 BGCOLOR="#FFFFFF">
<TR><TD ALIGIN="center">
<A HREF="http://lovely.dd-c.net/w5/txlink.cgi/DDC000411_00/105/" TARGET="_top">
</A></TD></TR>
<TR><TD ALIGN=CENTER VALIGN=TOP>
<A HREF="http://lovely.dd-c.net/cgi-bin/dd/hb/banner/w5slink.cgi?uid=DDC000411_00 &bid=ONW5.210" TARGET="_top">
<IMG SRC="$root/image/o_net210.gif" WIDTH=468 HEIGHT=60 BORDER=0> </A></TD></TR>
</TABLE>
</CENTER></P>

         <P>$B0e2J3&$G%*%Z5;=Q$NM%$l$F$$$k$HI>H=$N3F%/%j%K%C%/MM$G$9!#(B<A HREF="http://cgi.din.or.jp/~toa-ad/tsw021a/jump.cgi?053102" TARGET="_blank"><IMG SRC="$root/image/sasamoto.gif" WIDTH=380 HEIGHT=30 BORDER=0 ALIGN=bottom></A>
         <A HREF="http://cgi.din.or.jp/~toa-ad/tsir99c/jump.cgi?053102">
         </A><A HREF="http://cgi.din.or.jp/~toa-ad/tsir99c/jump.cgi?053102" TARGET="_blank"><IMG SRC="$root/image/airu.gif" WIDTH=380 HEIGHT=30 BORDER=0 ALIGN=bottom></A>
         <A HREF="http://cgi.din.or.jp/~toa-ad/taka/seisin/lucky/jump.cgi?053102">
         </A><A HREF="http://cgi.din.or.jp/~toa-ad/taka/seisin/lucky/jump.cgi?053102" TARGET="_blank"><IMG SRC="$root/image/seisin.gif" WIDTH=380 HEIGHT=30 BORDER=0 ALIGN=bottom></A>
         <A HREF="http://cgi.din.or.jp/~toa-ad/tsak00k/sakai/jump.cgi?053102">
         </A><A HREF="http://cgi.din.or.jp/~toa-ad/tsak00k/sakai/jump.cgi?053102" TARGET="_blank"><IMG SRC="$root/image/sakai.gif" WIDTH=380 HEIGHT=30 BORDER=0 ALIGN=bottom></A>
         <A HREF="http://cgi.din.or.jp/~toa-ad/ane20a/jump.cgi?053102">
         </A><A HREF="http://cgi.din.or.jp/~toa-ad/ane20a/jump.cgi?053102" TARGET="_blank"><IMG SRC="$root/image/anesis.gif" WIDTH=380 HEIGHT=30 BORDER=0 ALIGN=bottom></A></P>
         
         <P>
<IFRAME frameBorder="0" height="60" width="468" marginHeight="0" scrolling="no" src="http://ad.jp.ap.valuecommerce.com/servlet/htmlbanner?sid=5358&pid=870014383" MarginWidth="0">
         <SCRIPT LANGUAGE=javascript src="http://ad.jp.ap.valuecommerce.com/servlet/jsbanner?sid=5358&pid=870014383"></SCRIPT>
<noscript> <A HREF="http://ck.jp.ap.valuecommerce.com/servlet/referral?sid=5358&pid=870014383" TARGET="_blank"><IMG SRC="http://ad.jp.ap.valuecommerce.com/servlet/gifbanner?sid=5358&pid=870014383" WIDTH=468 HEIGHT=60 BORDER=0 ALIGN=bottom></A>
</noscript> </IFRAME></P>
         
         <P>
<IFRAME frameBorder="0" height="60" width="468" marginHeight="0" scrolling="no" src="http://ad.jp.ap.valuecommerce.com/servlet/htmlbanner?sid=5358&pid=870014434" MarginWidth="0">
         <SCRIPT LANGUAGE=javascript src="http://ad.jp.ap.valuecommerce.com/servlet/jsbanner?sid=5358&pid=870014434"></SCRIPT>
<noscript> <A HREF="http://ck.jp.ap.valuecommerce.com/servlet/referral?sid=5358&pid=870014434" TARGET="_blank"><IMG SRC="http://ad.jp.ap.valuecommerce.com/servlet/gifbanner?sid=5358&pid=870014434" WIDTH=468 HEIGHT=60 BORDER=0 ALIGN=bottom></A>
</noscript> </IFRAME></P>
         
         <P><IMG SRC="$root/image/line_a2.gif" WIDTH=640 HEIGHT=3 ALIGN=bottom></P></CENTER>
      </TD>
   </TR>
   <TR>
      <TD>
         <CENTER>$B!!(B
         
         <P><TABLE BORDER=1 WIDTH="100%">
            <TR>
               <TD>
                  <CENTER><A HREF="$root/index.html" TARGET="_self">$B%H%C%W%Z!<%8(B</A></CENTER>
               </TD>
               <TD>
                  <CENTER><A HREF="$root/book.html" TARGET="_self">$BCx=q$N%3!<%J!<(B</A></CENTER>
               </TD>
               <TD>
                  <CENTER><A HREF="$root/baby.html" TARGET="_self">$BL?L>$N%3!<%J!<(B</A></CENTER>
               </TD>
            </TR>
            <TR>
               <TD>
                  <CENTER><A HREF="$root/consul.html">$B!V$4AjCL%3!<%J!<!W(B</A></CENTER>
               </TD>
               <TD>
                  <CENTER><A HREF="$root/info.html" TARGET="_self">$B2'$+$i$N$*CN$i$;(B</A></CENTER>
               </TD>
               <TD>
                  <CENTER><A HREF="$root/link.html">$B!V@j$$D>9TJX!W(B</A></CENTER>
               </TD>
            </TR>
         </TABLE>
         </P>
         
         <P><IMG SRC="$root/image/line_a1.gif" WIDTH=640 HEIGHT=3 ALIGN=bottom></P></CENTER>
      </TD>
   </TR>
   <TR>
      <TD>
         <CENTER>$B!!(B
         
         <P>$B$*J9$-$N6J$K$D$$$F$O!"(B<A HREF="$root/info.html#midi">$B$3$A$i(B</A>$B$r$4Mw2<$5$$!#(B</P>
         
         <P><IMG SRC="$root/image/line_a1.gif" WIDTH=640 HEIGHT=3 ALIGN=bottom></P></CENTER>
      </TD>
   </TR>
   <TR>
      <TD>
         <CENTER>$B!!(B
         
         <P><FONT SIZE="-2">$B$3$N7k2L$r8+$F$N$40U8+$d$446A[$r$*J9$+$;2<$5$$!#!!(B<IMG SRC="$root/image/mail_a2.gif" WIDTH=20 HEIGHT=18 ALIGN=bottom></FONT><A HREF="mailto:okina\@e-mail.ne.jp"><FONT SIZE="-2">okina\@e-mail.ne.jp</FONT></A><FONT SIZE="-2"><I><BR>
         </I>$B%j%s%/$O4?7^$7$^$9$,!"I,$:(B</FONT><A HREF="$root/index.html" TARGET="_self"><FONT SIZE="-2">TOP$B%Z!<%8(B</FONT></A><FONT SIZE="-2">$B$X$*4j$$$7$^$9!#(B<BR>
         $B$3$N%3%s%F%s%D$N>&MQMxMQ$J$i$S$KL5CGE>:\$O$*CG$j$$$?$7$^$9!#$3$N4UDj$OL5NA$G$9!#(B<BR>
         <I>CopyRight. K.Yamamoto. 1998.9.1</I></FONT></P></CENTER>
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
