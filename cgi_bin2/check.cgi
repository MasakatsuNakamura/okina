#!/usr/local/bin/perl
$|=1;
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
#####$B9g7WBe6b$N7W;;%m%8%C%/(B#####
if (($order1 ne "") and ($order2 ne "") and ($order3 ne ""))  {
   if ($exp ne "") {
       $kgak ="16,810";
   }
   elsif ($exp eq "") {
       $kgak ="11,810";
   }
}
elsif (($order1 ne "") and ($order2 ne ""))  {
   $kgak ="1,810";
}
elsif (($order1 ne "") and ($order3 ne ""))  {
   if ($exp ne "") {
       $kgak ="15,500";
   }
   elsif ($exp eq "") {
       $kgak ="10,500";
   }
}
elsif (($order2 ne "") and ($order3 ne ""))  {
   if ($exp ne "") {
       $kgak ="16,810";
   }
   elsif ($exp eq "") {
       $kgak ="11,810";
   }
}
elsif ($order1 ne "")  {
   $kgak ="500";
}
elsif ($order2 ne "")  {
   $kgak ="1,810";
}
elsif ($order3 ne "")  {
   if ($exp ne "") {
       $kgak ="15,000";
   }
   elsif ($exp eq "") {
       $kgak ="10,000";
  }
}
######$B$3$3$+$i0z$-7Q$.>pJs$N@8@.$HI=<(2hLL(B######
######$BEE;RK\!"=q@R!"L?L>$N(B3$B$D$rCmJ8(B#######
if (($order1 ne "") and ($order2 ne "") and ($order3 ne ""))  {
	$msg = <<"ORDER123";
Content-type: text/html

<HTML>
<HEAD>
   <TITLE>$BEE;RK\$H=q@R$N$4CmJ8!&L?L>$N$40MMj(B</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=x-sjis">
</HEAD>
<BODY BGCOLOR="#FFFFFF" BACKGROUND="/~kazu-y/image/wall.jpg">
<P><TABLE BORDER=0 CELLSPACING=0 CELLPADDING=0 WIDTH=640>
   <TR>
      <TD>
         <CENTER><FONT SIZE="+3"><B><U>$B$4CmJ8FbMF$N$43NG'(B</U></B></FONT></CENTER>
         
         <BLOCKQUOTE>$B$3$N2hLL$O!"$4CmJ8FbMF$r$43NG'D:$/$?$a$N$b$N$G$9!#FbMF$K8m$j$,$"$k>l9g$O!"%V%i%&%6$N!VLa$k!W%\%?%s$r2!$7$F!VF~NO%U%)!<%`!W$+$i=$@5$7$F2<$5$$!#$3$l$G59$7$1$l$P!VCmJ8!W%\%?%s$r2!$7$F2<$5$$!#$J$*EE;RK\$H=q@R$NN>J}$4CmJ8$N>l9g!"(B500$B1_$r3d0zCW$7$^$9!#(B</BLOCKQUOTE>
         
         <CENTER><B>$B$4CmJ8FbMF(B</B><BR>
<TABLE BORDER=1 WIDTH="90%">
   <TR>
      <TD WIDTH=148>
         <P>$B$40MMj<T(B($B5.J}(B)$B$N$*L>A0(B</P>
      </TD>
      <TD>
         <P>\$name</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>$B$40MMj<T$N%a!<%k%"%I%l%9(B</P>
      </TD>
      <TD>
         <P>\$email</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>$B$40MMj$NFbMF(B</P>
      </TD>
      <TD>
         <P>$B;3K\2'$NCx=q(B($BEE;RK\$H<BK\(B)$B$NCmJ8!"?7@8;y$NL?L>0MMj(B</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>$B=q@R$N$4AwIU@h(B</P>
      </TD>
      <TD>
         <P><TABLE BORDER=1>
            <TR>
               <TD WIDTH=55>
                  <P>$BM9JXHV9f(B</P>
               </TD>
               <TD>
                  <P>\$zipcord</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=55>
                  <P>$B=;=j(B</P>
               </TD>
               <TD>
                  <P>\$address</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=55>
                  <P>$B$*<u<h?M(B</P>
               </TD>
               <TD>
                  <P>\$fullname</P>
               </TD>
            </TR>
         </TABLE>
         </P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>$B$4O"Mm@h$*EEOCHV9f(B</P>
      </TD>
      <TD>
         <P>\$tel</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>$B?7@8;y$NL?L>0MMj(B</P>
      </TD>
      <TD>
         <P><TABLE BORDER=1>
            <TR>
               <TD WIDTH=92>
                  <P>$B@+(B($BID;z(B)</P>
               </TD>
               <TD>
                  <P>\$familyname</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=92>
                  <P>$B=P@8F|(B($BM=DjF|(B)</P>
               </TD>
               <TD>
                  <P>\$brthday</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=92>
                  <P>$B2a5n$N$40MMj(B</P>
               </TD>
               <TD>
                  <P>\$user</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=92>
                  <P>$B$47;Do$N$*L>A0(B</P>
               </TD>
               <TD>
                  <P>\$brother</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=92>
                  <P>$B$4MWK>;v9`(B</P>
               </TD>
               <TD>
                  <P>\$request</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=92>
                  <P>$BFC5-;v9`(B</P>
               </TD>
               <TD>
                  <P>\$exp</P>
               </TD>
            </TR>
         </TABLE>
         </P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>$B9g7W$*;YJ'$$6b3[(B</P>
      </TD>
      <TD>
         <P>\$kgak $B1_(B</P>
      </TD>
   </TR>
</TABLE>
</CENTER>
         
         <BLOCKQUOTE>
            <B>$B$43NG'$,:Q$_$^$7$?$i(B</B><FONT COLOR="#FF0000"><B>$B2<5-!VCmJ8!W%\%?%s$r(B1$B2s$@$12!$7$F$4H/Cm(B</B></FONT><B>$B$/$@$5$$!#(B<BR>
            $B$J$*!">&IJ$N@-3J>e!"$3$l0J9_$N$4CmJ8$N<h$j>C$7$dJVIJ$O0l@Z=PMh$^$;$s$N$GM=$a$4N;>52<$5$$!#(B($BK,LdHNGdK!$N%/!<%j%s%0%*%U$OE,MQ$5$l$^$;$s!#!K(B</B></BLOCKQUOTE>
         
         <CENTER>$B$4CmJ8$ND{@5$O!"%V%i%&%6$N!VLa$k!W$G!VF~NO%U%)!<%`!W$+$i$d$jD>$7$F2<$5$$!#(B</CENTER>
         
         <P><FORM ACTION="/~kazu-y/cgi_bin2/nn_mail.cgi" METHOD=POST>
            <P><INPUT TYPE="hidden" NAME="name" VALUE="\$name">
            <INPUT TYPE="hidden" NAME="email" VALUE="\$email">
            <INPUT TYPE="hidden" NAME="order1" VALUE="\$order1">
            <INPUT TYPE="hidden" NAME="order2" VALUE="\$order2">
            <INPUT TYPE="hidden" NAME="order3" VALUE="\$order3">
            <INPUT TYPE="hidden" NAME="zipcord" VALUE="\$zipcord">
            <INPUT TYPE="hidden" NAME="address" VALUE="\$address">
            <INPUT TYPE="hidden" NAME="tel" VALUE="\$tel">
            <INPUT TYPE="hidden" NAME="fullname" VALUE="\$fullname">
            <INPUT TYPE="hidden" NAME="familyname" VALUE="\$familyname">
            <INPUT TYPE="hidden" NAME="brthday" VALUE="\$brthday">
            <INPUT TYPE="hidden" NAME="user" VALUE="\$user">
            <INPUT TYPE="hidden" NAME="brother" VALUE="\$brother">
            <INPUT TYPE="hidden" NAME="request" VALUE="\$request">
            <INPUT TYPE="hidden" NAME="exp" VALUE="\$exp">
            <INPUT TYPE="hidden" NAME="kgak" VALUE="\$kgak">
            <CENTER><INPUT TYPE=submit NAME="$BAw?.(B" VALUE="$BCmJ8(B"></CENTER>
         </FORM></P></CENTER>
      </TD>
   </TR>
</TABLE>
</P>
</BODY>
</HTML>

ORDER123
&jcode'convert(*msg, "sjis", "euc");
	$msg =~ s/\$name/$name/g;
	$msg =~ s/\$email/$email/g;
	$msg =~ s/\$order1/$order1/g;
	$msg =~ s/\$order2/$order2/g;	
	$msg =~ s/\$order3/$order3/g;	
	$msg =~ s/\$zipcord/$zipcord/g;
	$msg =~ s/\$address/$address/g;
	$msg =~ s/\$tel/$tel/g;
	$msg =~ s/\$fullname/$fullname/g;
	$msg =~ s/\$familyname/$familyname/g;
	$msg =~ s/\$brthday/$brthday/g;
	$msg =~ s/\$user/$user/g;
	$msg =~ s/\$brother/$brother/g;
	$msg =~ s/\$request/$request/g;
	$msg =~ s/\$exp/$exp/g;
    $msg =~ s/\$kgak/$kgak/g;
	print $msg;
}
#######$BEE;RK\$H=q@R$rCmJ8(B##########
elsif (($order1 ne "") and ($order2 ne ""))  {
	$msg = <<"ORDER120";
Content-type: text/html

<HTML>
<HEAD>
   <TITLE>$BEE;RK\$H=q@R$N$4CmJ8(B</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=x-sjis">
</HEAD>
<BODY BGCOLOR="#FFFFFF" BACKGROUND="/~kazu-y/image/wall.jpg">
<P><TABLE BORDER=0 CELLSPACING=0 CELLPADDING=0 WIDTH=640>
   <TR>
      <TD>
<CENTER><FONT SIZE="+3"><B><U>$B$4CmJ8FbMF$N$43NG'(B</U></B></FONT></CENTER>
         
         <BLOCKQUOTE>$B$3$N2hLL$O!"$4CmJ8FbMF$r$43NG'D:$/$?$a$N$b$N$G$9!#FbMF$K8m$j$,$"$k>l9g$O!"%V%i%&%6$N!VLa$k!W%\%?%s$r2!$7$F!VF~NO%U%)!<%`!W$+$i=$@5$7$F2<$5$$!#$3$l$G59$7$1$l$P!VCmJ8!W%\%?%s$r2!$7$F2<$5$$!#$J$*EE;RK\$H=q@R$NN>J}$4CmJ8$N>l9g!"(B500$B1_$r3d0zCW$7$^$9!#(B</BLOCKQUOTE>
         
         <CENTER><B>$B$4CmJ8FbMF(B</B><BR>
         <TABLE BORDER=1 WIDTH="90%">
 <TR>
      <TD WIDTH=148>
         <P>$B$40MMj<T(B($B5.J}(B)$B$N$*L>A0(B</P>
      </TD>
      <TD>
         <P>\$name</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>$B$40MMj<T$N%a!<%k%"%I%l%9(B</P>
      </TD>
      <TD>
         <P>\$email</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>$B$40MMj$NFbMF(B</P>
      </TD>
      <TD>
         <P>$B;3K\2'$NCx=q(B($BEE;RK\$H<BK\(B)$B$NCmJ8(B</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>$B=q@R$N$4AwIU@h(B</P>
      </TD>
      <TD>
         <P><TABLE BORDER=1>
            <TR>
               <TD WIDTH=55>
                  <P>$BM9JXHV9f(B</P>
               </TD>
               <TD>
                  <P>\$zipcord</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=55>
                  <P>$B=;=j(B</P>
               </TD>
               <TD>
                  <P>\$address</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=55>
                  <P>$B$*<u<h?M(B</P>
               </TD>
               <TD>
                  <P>\$fullname</P>
               </TD>
            </TR>
         </TABLE>
         </P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>$B$4O"Mm@h$*EEOCHV9f(B</P>
      </TD>
      <TD>
         <P>\$tel</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>$B9g7W$*;YJ'$$6b3[(B</P>
      </TD>
      <TD>
         <P>\$kgak $B1_(B</P>
      </TD>
   </TR>
</TABLE>
</CENTER>
         
         <BLOCKQUOTE>
            <B>$B$43NG'$,:Q$_$^$7$?$i(B</B><FONT COLOR="#FF0000"><B>$B2<5-!VCmJ8!W%\%?%s$r(B1$B2s$@$12!$7$F$4H/Cm(B</B></FONT><B>$B$/$@$5$$!#(B<BR>
            $B$J$*!">&IJ$N@-3J>e!"$3$l0J9_$N$4CmJ8$N<h$j>C$7$dJVIJ$O0l@Z=PMh$^$;$s$N$GM=$a$4N;>52<$5$$!#(B($BK,LdHNGdK!$N%/!<%j%s%0%*%U$OE,MQ$5$l$^$;$s!#!K(B</B></BLOCKQUOTE>
         
         <CENTER>$B$4CmJ8$ND{@5$O!"%V%i%&%6$N!VLa$k!W$G!VF~NO%U%)!<%`!W$+$i$d$jD>$7$F2<$5$$!#(B</CENTER>
         
         <P><FORM ACTION="/~kazu-y/cgi_bin2/nn_mail.cgi" METHOD=POST>
            <P><INPUT TYPE="hidden" NAME="name" VALUE="\$name">
            <INPUT TYPE="hidden" NAME="email" VALUE="\$email">
            <INPUT TYPE="hidden" NAME="order1" VALUE="\$order1">
            <INPUT TYPE="hidden" NAME="order2" VALUE="\$order2">
            <INPUT TYPE="hidden" NAME="order3" VALUE="">
            <INPUT TYPE="hidden" NAME="zipcord" VALUE="\$zipcord">
            <INPUT TYPE="hidden" NAME="address" VALUE="\$address">
            <INPUT TYPE="hidden" NAME="tel" VALUE="\$tel">
            <INPUT TYPE="hidden" NAME="fullname" VALUE="\$fullname">
            <INPUT TYPE="hidden" NAME="familyname" VALUE="">
            <INPUT TYPE="hidden" NAME="brthday" VALUE="">
            <INPUT TYPE="hidden" NAME="user" VALUE="">
            <INPUT TYPE="hidden" NAME="brother" VALUE="">
            <INPUT TYPE="hidden" NAME="request" VALUE="">
            <INPUT TYPE="hidden" NAME="exp" VALUE="">
            <INPUT TYPE="hidden" NAME="kgak" VALUE="\$kgak">
            <CENTER><INPUT TYPE=submit NAME="$BAw?.(B" VALUE="$BCmJ8(B"></CENTER>
         </FORM></P></CENTER>
      </TD>
   </TR>
</TABLE>
</P>
</BODY>
</HTML>

ORDER120
&jcode'convert(*msg, "sjis", "euc");
	$msg =~ s/\$name/$name/g;
	$msg =~ s/\$email/$email/g;
	$msg =~ s/\$order1/$order1/g;
	$msg =~ s/\$order2/$order2/g;	
	$msg =~ s/\$zipcord/$zipcord/g;
	$msg =~ s/\$address/$address/g;
	$msg =~ s/\$tel/$tel/g;
	$msg =~ s/\$fullname/$fullname/g;
    $msg =~ s/\$kgak/$kgak/g;
	print $msg;
}
########$BEE;RK\$NCmJ8$HL?L>$N0MMj(B###########
elsif (($order1 ne "") and ($order3 ne ""))  {
	$msg = <<"ORDER103";
Content-type: text/html

<HTML>
<HEAD>
   <TITLE>$BEE;RK\$N$4CmJ8!&L?L>$N$40MMj(B</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=x-sjis">
</HEAD>
<BODY BGCOLOR="#FFFFFF" BACKGROUND="/~kazu-y/image/wall.jpg">
<P><TABLE BORDER=0 CELLSPACING=0 CELLPADDING=0 WIDTH=640>
   <TR>
      <TD>
         <CENTER><FONT SIZE="+3"><B><U>$B$4CmJ8FbMF$N$43NG'(B</U></B></FONT></CENTER>
         
         <BLOCKQUOTE>$B$3$N2hLL$O!"$4CmJ8FbMF$r$43NG'D:$/$?$a$N$b$N$G$9!#FbMF$K8m$j$,$"$k>l9g$O!"%V%i%&%6$N!VLa$k!W%\%?%s$r2!$7$F!VF~NO%U%)!<%`!W$+$i=$@5$7$F2<$5$$!#$3$l$G59$7$1$l$P!VCmJ8!W%\%?%s$r2!$7$F2<$5$$!#(B</BLOCKQUOTE>
         
         <CENTER><B>$B$4CmJ8FbMF(B</B><BR>
         <TABLE BORDER=1 WIDTH="90%">
   <TR>
      <TD WIDTH=148>
         <P>$B$40MMj<T(B($B5.J}(B)$B$N$*L>A0(B</P>
      </TD>
      <TD>
         <P>\$name</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>$B$40MMj<T$N%a!<%k%"%I%l%9(B</P>
      </TD>
      <TD>
         <P>\$email</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>$B$40MMj$NFbMF(B</P>
      </TD>
      <TD>
         <P>$B;3K\2'$NCx=q(B($BEE;RK\(B)$B$NCmJ8!"?7@8;y$NL?L>0MMj(B</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>$B$40MMj<g$5$^$N>pJs(B<BR>
         ($B$*5^$.$NJ}$N$_(B)</P>
      </TD>
      <TD>
         <P><TABLE BORDER=1>
            <TR>
               <TD WIDTH=64>
                  <P>$BM9JXHV9f(B</P>
               </TD>
               <TD>
                  <P>\$zipcord</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=64>
                  <P>$B=;=j(B</P>
               </TD>
               <TD>
                  <P>\$address</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=64>
                  <P>$B$*EEOCHV9f(B</P>
               </TD>
               <TD>
                  <P>\$tel</P>
               </TD>
            </TR>
         </TABLE>
         </P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>$B?7@8;y$NL?L>0MMj(B</P>
      </TD>
      <TD>
         <P><TABLE BORDER=1>
            <TR>
               <TD WIDTH=90>
                  <P>$B@+(B($BID;z(B)</P>
               </TD>
               <TD>
                  <P>\$familyname</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=90>
                  <P>$B=P@8F|(B($BM=DjF|(B)</P>
               </TD>
               <TD>
                  <P>\$brthday</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=90>
                  <P>$B2a5n$N$40MMj(B</P>
               </TD>
               <TD>
                  <P>\$user</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=90>
                  <P>$B$47;Do$N$*L>A0(B</P>
               </TD>
               <TD>
                  <P>\$brother</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=90>
                  <P>$B$4MWK>;v9`(B</P>
               </TD>
               <TD>
                  <P>\$request</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=90>
                  <P>$BFC5-;v9`(B</P>
               </TD>
               <TD>
                  <P>\$exp</P>
               </TD>
            </TR>
         </TABLE>
         </P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>$B9g7W$*;YJ'$$6b3[(B</P>
      </TD>
      <TD>
         <P>\$kgak $B1_(B</P>
      </TD>
   </TR>
         </TABLE>
</CENTER>
         
         <BLOCKQUOTE>
            <B>$B$43NG'$,:Q$_$^$7$?$i(B</B><FONT COLOR="#FF0000"><B>$B2<5-!VCmJ8!W%\%?%s$r(B1$B2s$@$12!$7$F$4H/Cm(B</B></FONT><B>$B$/$@$5$$!#:G6a!"%a!<%k%"%I%l%9$N4V0c$$$,B?$$$h$&$G$9!#%a!<%k%"%I%l%9$r$b$&0lEY!"$43NG'2<$5$$!#(B<BR>
            $B$J$*!">&IJ$N@-3J>e!"$3$l0J9_$N$4CmJ8$N<h$j>C$7$dJVIJ$O0l@Z=PMh$^$;$s$N$GM=$a$4N;>52<$5$$!#(B($BK,LdHNGdK!$N%/!<%j%s%0%*%U$OE,MQ$5$l$^$;$s!#!K(B</B></BLOCKQUOTE>
         
         <CENTER>$B$4CmJ8$ND{@5$O!"%V%i%&%6$N!VLa$k!W$G!VF~NO%U%)!<%`!W$+$i$d$jD>$7$F2<$5$$!#(B</CENTER>
         
         <P><FORM ACTION="/~kazu-y/cgi_bin2/nn_mail.cgi" METHOD=POST>
            <P><INPUT TYPE="hidden" NAME="name" VALUE="\$name">
            <INPUT TYPE="hidden" NAME="email" VALUE="\$email">
            <INPUT TYPE="hidden" NAME="order1" VALUE="\$order1">
            <INPUT TYPE="hidden" NAME="order2" VALUE="">
            <INPUT TYPE="hidden" NAME="order3" VALUE="\$order3">
            <INPUT TYPE="hidden" NAME="zipcord" VALUE="\$zipcord">
            <INPUT TYPE="hidden" NAME="address" VALUE="\$address">
            <INPUT TYPE="hidden" NAME="tel" VALUE="\$tel">
            <INPUT TYPE="hidden" NAME="fullname" VALUE="">
            <INPUT TYPE="hidden" NAME="familyname" VALUE="\$familyname">
            <INPUT TYPE="hidden" NAME="brthday" VALUE="\$brthday">
            <INPUT TYPE="hidden" NAME="user" VALUE="\$user">
            <INPUT TYPE="hidden" NAME="brother" VALUE="\$brother">
            <INPUT TYPE="hidden" NAME="request" VALUE="\$request">
            <INPUT TYPE="hidden" NAME="exp" VALUE="\$exp">
            <INPUT TYPE="hidden" NAME="kgak" VALUE="\$kgak">
            <CENTER><INPUT TYPE=submit NAME="$BAw?.(B" VALUE="$BCmJ8(B"></CENTER>
         </FORM></P></CENTER>
      </TD>
   </TR>
</TABLE>
</P>
</BODY>
</HTML>

ORDER103
&jcode'convert(*msg, "sjis", "euc");
	$msg =~ s/\$name/$name/g;
	$msg =~ s/\$email/$email/g;
	$msg =~ s/\$order1/$order1/g;	
	$msg =~ s/\$order3/$order3/g;	
	$msg =~ s/\$zipcord/$zipcord/g;
	$msg =~ s/\$address/$address/g;
	$msg =~ s/\$tel/$tel/g;
	$msg =~ s/\$familyname/$familyname/g;
	$msg =~ s/\$brthday/$brthday/g;
	$msg =~ s/\$user/$user/g;
	$msg =~ s/\$brother/$brother/g;
	$msg =~ s/\$request/$request/g;
	$msg =~ s/\$exp/$exp/g;
	$msg =~ s/\$kgak/$kgak/g;
	print $msg;
}
########$B=q@R$NCmJ8$HL?L>$N0MMj(B###########
elsif (($order2 ne "") and ($order3 ne ""))  {
	$msg = <<"ORDER023";
Content-type: text/html

<HTML>
<HEAD>
   <TITLE>$B=q@R$N$4CmJ8!&L?L>$N$40MMj(B</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=x-sjis">
</HEAD>
<BODY BGCOLOR="#FFFFFF" BACKGROUND="/~kazu-y/image/wall.jpg">
<P><TABLE BORDER=0 CELLSPACING=0 CELLPADDING=0 WIDTH=640>
   <TR>
      <TD>
         <CENTER><FONT SIZE="+3"><B><U>$B$4CmJ8FbMF$N$43NG'(B</U></B></FONT></CENTER>
         
         <BLOCKQUOTE>$B$3$N2hLL$O!"$4CmJ8FbMF$r$43NG'D:$/$?$a$N$b$N$G$9!#FbMF$K8m$j$,$"$k>l9g$O!"%V%i%&%6$N!VLa$k!W%\%?%s$r2!$7$F!VF~NO%U%)!<%`!W$+$i=$@5$7$F2<$5$$!#$3$l$G59$7$1$l$P!VCmJ8!W%\%?%s$r2!$7$F2<$5$$!#(B</BLOCKQUOTE>
         
         <CENTER><B>$B$4CmJ8FbMF(B</B><BR>
         <TABLE BORDER=1 WIDTH="80%">
  <TR>
      <TD WIDTH=148>
         <P>$B$40MMj<T(B($B5.J}(B)$B$N$*L>A0(B</P>
      </TD>
      <TD>
         <P>\$name</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>$B$40MMj<T$N%a!<%k%"%I%l%9(B</P>
      </TD>
      <TD>
         <P>\$email</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>$B$40MMj$NFbMF(B</P>
      </TD>
      <TD>
         <P>$B;3K\2'$NCx=q(B($B<BK\(B)$B$NCmJ8!"?7@8;y$NL?L>0MMj(B</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>$B=q@R$N$4AwIU@h(B</P>
      </TD>
      <TD>
         <P><TABLE BORDER=1>
            <TR>
               <TD WIDTH=55>
                  <P>$BM9JXHV9f(B</P>
               </TD>
               <TD>
                  <P>\$zipcord</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=55>
                  <P>$B=;=j(B</P>
               </TD>
               <TD>
                  <P>\$address</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=55>
                  <P>$B$*<u<h?M(B</P>
               </TD>
               <TD>
                  <P>\$fullname</P>
               </TD>
            </TR>
         </TABLE>
         </P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>$B$4O"Mm@h$*EEOCHV9f(B</P>
      </TD>
      <TD>
         <P>\$tel</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>$B?7@8;y$NL?L>0MMj(B</P>
      </TD>
      <TD>
         <P><TABLE BORDER=1>
            <TR>
               <TD WIDTH=92>
                  <P>$B@+(B($BID;z(B)</P>
               </TD>
               <TD>
                  <P>\$familyname</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=92>
                  <P>$B=P@8F|(B($BM=DjF|(B)</P>
               </TD>
               <TD>
                  <P>\$brthday</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=92>
                  <P>$B2a5n$N$40MMj(B</P>
               </TD>
               <TD>
                  <P>\$user</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=92>
                  <P>$B$47;Do$N$*L>A0(B</P>
               </TD>
               <TD>
                  <P>\$brother</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=92>
                  <P>$B$4MWK>;v9`(B</P>
               </TD>
               <TD>
                  <P>\$request</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=92>
                  <P>$BFC5-;v9`(B</P>
               </TD>
               <TD>
                  <P>\$exp</P>
               </TD>
            </TR>
         </TABLE>
         </P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>$B9g7W$*;YJ'$$6b3[(B</P>
      </TD>
      <TD>
         <P>\$kgak $B1_(B</P>
      </TD>
   </TR>
         </TABLE>
        </CENTER>
         
         <BLOCKQUOTE>
            <B>$B$43NG'$,:Q$_$^$7$?$i(B</B><FONT COLOR="#FF0000"><B>$B2<5-!VCmJ8!W%\%?%s$r(B1$B2s$@$12!$7$F$4H/Cm(B</B></FONT><B>$B$/$@$5$$!#(B<BR>
            $B$J$*!">&IJ$N@-3J>e!"$3$l0J9_$N$4CmJ8$N<h$j>C$7$dJVIJ$O0l@Z=PMh$^$;$s$N$GM=$a$4N;>52<$5$$!#(B($BK,LdHNGdK!$N%/!<%j%s%0%*%U$OE,MQ$5$l$^$;$s!#!K(B</B></BLOCKQUOTE>
         
         <CENTER>$B$4CmJ8$ND{@5$O!"%V%i%&%6$N!VLa$k!W$G!VF~NO%U%)!<%`!W$+$i$d$jD>$7$F2<$5$$!#(B</CENTER>
         
         <P><FORM ACTION="/~kazu-y/cgi_bin2/nn_mail.cgi" METHOD=POST>
            <P><INPUT TYPE="hidden" NAME="name" VALUE="\$name">
            <INPUT TYPE="hidden" NAME="email" VALUE="\$email">
            <INPUT TYPE="hidden" NAME="order1" VALUE="">
            <INPUT TYPE="hidden" NAME="order2" VALUE="\$order2">
            <INPUT TYPE="hidden" NAME="order3" VALUE="\$order3">
            <INPUT TYPE="hidden" NAME="zipcord" VALUE="\$zipcord">
            <INPUT TYPE="hidden" NAME="address" VALUE="\$address">
            <INPUT TYPE="hidden" NAME="tel" VALUE="\$tel">
            <INPUT TYPE="hidden" NAME="fullname" VALUE="\$fullname">
            <INPUT TYPE="hidden" NAME="familyname" VALUE="\$familyname">
            <INPUT TYPE="hidden" NAME="brthday" VALUE="\$brthday">
            <INPUT TYPE="hidden" NAME="user" VALUE="\$user">
            <INPUT TYPE="hidden" NAME="brother" VALUE="\$brother">
            <INPUT TYPE="hidden" NAME="request" VALUE="\$request">
            <INPUT TYPE="hidden" NAME="exp" VALUE="\$exp">
            <INPUT TYPE="hidden" NAME="kgak" VALUE="\$kgak">
            <CENTER><INPUT TYPE=submit NAME="$BAw?.(B" VALUE="$BCmJ8(B"></CENTER>
         </FORM></P></CENTER>
      </TD>
   </TR>
</TABLE>
</P>
</BODY>
</HTML>

ORDER023
&jcode'convert(*msg, "sjis", "euc");
	$msg =~ s/\$name/$name/g;
	$msg =~ s/\$email/$email/g;
	$msg =~ s/\$order2/$order2/g;	
	$msg =~ s/\$order3/$order3/g;	
	$msg =~ s/\$zipcord/$zipcord/g;
	$msg =~ s/\$address/$address/g;
	$msg =~ s/\$tel/$tel/g;
	$msg =~ s/\$fullname/$fullname/g;
	$msg =~ s/\$familyname/$familyname/g;
	$msg =~ s/\$brthday/$brthday/g;
	$msg =~ s/\$user/$user/g;
	$msg =~ s/\$brother/$brother/g;
	$msg =~ s/\$request/$request/g;
	$msg =~ s/\$exp/$exp/g;
	$msg =~ s/\$kgak/$kgak/g;
	print $msg;
}
############$BEE;RK\$N$_CmJ8(B###########
elsif ($order1 ne "")  {
	$msg = <<"ORDER100";
Content-type: text/html

<HTML>
<HEAD>
   <TITLE>$BEE;RK\$N$4CmJ8(B</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=x-sjis">
</HEAD>
<BODY BGCOLOR="#FFFFFF" BACKGROUND="/~kazu-y/image/wall.jpg">
<P><TABLE BORDER=0 CELLSPACING=0 CELLPADDING=0 WIDTH=640>
   <TR>
      <TD>
<CENTER><FONT SIZE="+3"><B><U>$B$4CmJ8FbMF$N$43NG'(B</U></B></FONT></CENTER>
         
         <BLOCKQUOTE>$B$3$N2hLL$O!"$4CmJ8FbMF$r$43NG'D:$/$?$a$N$b$N$G$9!#FbMF$K8m$j$,$"$k>l9g$O!"%V%i%&%6$N!VLa$k!W%\%?%s$r2!$7$F!VF~NO%U%)!<%`!W$+$i=$@5$7$F2<$5$$!#$3$l$G59$7$1$l$P!VCmJ8!W%\%?%s$r2!$7$F2<$5$$!#(B</BLOCKQUOTE>
         
         <CENTER><B>$B$4CmJ8FbMF(B</B><BR>
         <TABLE BORDER=1 WIDTH="90%">
   <TR>
      <TD WIDTH=148>
         <P>$B$40MMj<T(B($B5.J}(B)$B$N$*L>A0(B</P>
      </TD>
      <TD>
         <P>\$name</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>$B$40MMj<T$N%a!<%k%"%I%l%9(B</P>
      </TD>
      <TD>
         <P>\$email</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>$B$40MMj$NFbMF(B</P>
      </TD>
      <TD>
         <P>$B;3K\2'$NCx=q(B($BEE;RK\(B)$B$NCmJ8(B</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>$B9g7W$*;YJ'$$6b3[(B</P>
      </TD>
      <TD>
         <P>\$kgak $B1_(B</P>
      </TD>
   </TR>
         </TABLE>
</CENTER>
         
         <BLOCKQUOTE>
            <B>$B$43NG'$,:Q$_$^$7$?$i(B</B><FONT COLOR="#FF0000"><B>$B2<5-!VCmJ8!W%\%?%s$r(B1$B2s$@$12!$7$F$4H/Cm(B</B></FONT><B>$B$/$@$5$$!#:G6a!"%a!<%k%"%I%l%9$N4V0c$$$,B?$$$h$&$G$9!#%a!<%k%"%I%l%9$r$b$&0lEY!"$43NG'2<$5$$!#(B<BR>
            $B$J$*!">&IJ$N@-3J>e!"$3$l0J9_$N$4CmJ8$N<h$j>C$7$dJVIJ$O0l@Z=PMh$^$;$s$N$GM=$a$4N;>52<$5$$!#(B($BK,LdHNGdK!$N%/!<%j%s%0%*%U$OE,MQ$5$l$^$;$s!#!K(B</B></BLOCKQUOTE>
         
         <CENTER>$B$4CmJ8$ND{@5$O!"%V%i%&%6$N!VLa$k!W$G!VF~NO%U%)!<%`!W$+$i$d$jD>$7$F2<$5$$!#(B</CENTER>
         
         <P><FORM ACTION="/~kazu-y/cgi_bin2/nn_mail.cgi" METHOD=POST>
            <P><INPUT TYPE="hidden" NAME="name" VALUE="\$name">
            <INPUT TYPE="hidden" NAME="email" VALUE="\$email">
            <INPUT TYPE="hidden" NAME="order1" VALUE="\$order1">
            <INPUT TYPE="hidden" NAME="order2" VALUE="">
            <INPUT TYPE="hidden" NAME="order3" VALUE="">
            <INPUT TYPE="hidden" NAME="zipcord" VALUE="">
            <INPUT TYPE="hidden" NAME="address" VALUE="">
            <INPUT TYPE="hidden" NAME="tel" VALUE="">
            <INPUT TYPE="hidden" NAME="fullname" VALUE="">
            <INPUT TYPE="hidden" NAME="familyname" VALUE="">
            <INPUT TYPE="hidden" NAME="brthday" VALUE="">
            <INPUT TYPE="hidden" NAME="user" VALUE="">
            <INPUT TYPE="hidden" NAME="brother" VALUE="">
            <INPUT TYPE="hidden" NAME="request" VALUE="">
            <INPUT TYPE="hidden" NAME="exp" VALUE="">
            <INPUT TYPE="hidden" NAME="kgak" VALUE="\$kgak">
            <CENTER><INPUT TYPE=submit NAME="$BAw?.(B" VALUE="$BCmJ8(B"></CENTER>
         </FORM></P></CENTER>
      </TD>
   </TR>
</TABLE>
</P>
</BODY>
</HTML>

ORDER100
&jcode'convert(*msg, "sjis", "euc");
	$msg =~ s/\$name/$name/g;
	$msg =~ s/\$email/$email/g;
	$msg =~ s/\$order1/$order1/g;
	$msg =~ s/\$kgak/$kgak/g;
	print $msg;
}
#########$B=q@R$N$_CmJ8(B##########
elsif ($order2 ne "")  {
	$msg = <<"ORDER020";
Content-type: text/html

<HTML>
<HEAD>
   <TITLE>$B=q@R$N$4CmJ8(B</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=x-sjis">
</HEAD>
<BODY BGCOLOR="#FFFFFF" BACKGROUND="/~kazu-y/image/wall.jpg">
<P><TABLE BORDER=0 CELLSPACING=0 CELLPADDING=0 WIDTH=640>
   <TR>
      <TD>
 <CENTER><FONT SIZE="+3"><B><U>$B$4CmJ8FbMF$N$43NG'(B</U></B></FONT></CENTER>
         
         <BLOCKQUOTE>$B$3$N2hLL$O!"$4CmJ8FbMF$r$43NG'D:$/$?$a$N$b$N$G$9!#FbMF$K8m$j$,$"$k>l9g$O!"%V%i%&%6$N!VLa$k!W%\%?%s$r2!$7$F!VF~NO%U%)!<%`!W$+$i=$@5$7$F2<$5$$!#$3$l$G59$7$1$l$P!VCmJ8!W%\%?%s$r2!$7$F2<$5$$!#(B</BLOCKQUOTE>
         
         <CENTER><B>$B$4CmJ8FbMF(B</B><BR>
         <TABLE BORDER=1 WIDTH="90%">
   <TR>
      <TD WIDTH=148>
         <P>$B$40MMj<T(B($B5.J}(B)$B$N$*L>A0(B</P>
      </TD>
      <TD>
         <P>\$name</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>$B$40MMj<T$N%a!<%k%"%I%l%9(B</P>
      </TD>
      <TD>
         <P>\$email</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>$B$40MMj$NFbMF(B</P>
      </TD>
      <TD>
         <P>$B;3K\2'$NCx=q(B($B<BK\(B)$B$NCmJ8(B</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>$B=q@R$N$4AwIU@h(B</P>
      </TD>
      <TD>
         <P><TABLE BORDER=1>
            <TR>
               <TD WIDTH=55>
                  <P>$BM9JXHV9f(B</P>
               </TD>
               <TD>
                  <P>\$zipcord</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=55>
                  <P>$B=;=j(B</P>
               </TD>
               <TD>
                  <P>\$address</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=55>
                  <P>$B$*<u<h?M(B</P>
               </TD>
               <TD>
                  <P>\$fullname</P>
               </TD>
            </TR>
         </TABLE>
         </P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>$B$4O"Mm@h$*EEOCHV9f(B</P>
      </TD>
      <TD>
         <P>\$tel</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>$B9g7W$*;YJ'$$6b3[(B</P>
      </TD>
      <TD>
         <P>\$kgak $B1_(B</P>
      </TD>
   </TR>
         </TABLE>
</CENTER>
         
         <BLOCKQUOTE>
            <B>$B$43NG'$,:Q$_$^$7$?$i(B</B><FONT COLOR="#FF0000"><B>$B2<5-!VCmJ8!W%\%?%s$r(B1$B2s$@$12!$7$F$4H/Cm(B</B></FONT><B>$B$/$@$5$$!#(B<BR>
            $B$J$*!">&IJ$N@-3J>e!"$3$l0J9_$N$4CmJ8$N<h$j>C$7$dJVIJ$O0l@Z=PMh$^$;$s$N$GM=$a$4N;>52<$5$$!#(B($BK,LdHNGdK!$N%/!<%j%s%0%*%U$OE,MQ$5$l$^$;$s!#!K(B</B></BLOCKQUOTE>
         
         <CENTER>$B$4CmJ8$ND{@5$O!"%V%i%&%6$N!VLa$k!W$G!VF~NO%U%)!<%`!W$+$i$d$jD>$7$F2<$5$$!#(B</CENTER>
         
         <P><FORM ACTION="/~kazu-y/cgi_bin2/nn_mail.cgi" METHOD=POST>
            <P><INPUT TYPE="hidden" NAME="name" VALUE="\$name">
            <INPUT TYPE="hidden" NAME="email" VALUE="\$email">
            <INPUT TYPE="hidden" NAME="order1" VALUE="">
            <INPUT TYPE="hidden" NAME="order2" VALUE="\$order2">
            <INPUT TYPE="hidden" NAME="order3" VALUE="">
            <INPUT TYPE="hidden" NAME="zipcord" VALUE="\$zipcord">
            <INPUT TYPE="hidden" NAME="address" VALUE="\$address">
            <INPUT TYPE="hidden" NAME="tel" VALUE="\$tel">
            <INPUT TYPE="hidden" NAME="fullname" VALUE="\$fullname">
            <INPUT TYPE="hidden" NAME="familyname" VALUE="">
            <INPUT TYPE="hidden" NAME="brthday" VALUE="">
            <INPUT TYPE="hidden" NAME="user" VALUE="">
            <INPUT TYPE="hidden" NAME="brother" VALUE="">
            <INPUT TYPE="hidden" NAME="request" VALUE="">
            <INPUT TYPE="hidden" NAME="exp" VALUE="">
            <INPUT TYPE="hidden" NAME="kgak" VALUE="\$kgak">
            <CENTER><INPUT TYPE=submit NAME="$BAw?.(B" VALUE="$BCmJ8(B"></CENTER>
         </FORM></P></CENTER>
      </TD>
   </TR>
</TABLE>
</P>
</BODY>
</HTML>

ORDER020
&jcode'convert(*msg, "sjis", "euc");
	$msg =~ s/\$name/$name/g;
	$msg =~ s/\$email/$email/g;
	$msg =~ s/\$order2/$order2/g;		
	$msg =~ s/\$zipcord/$zipcord/g;
	$msg =~ s/\$address/$address/g;
	$msg =~ s/\$tel/$tel/g;
	$msg =~ s/\$fullname/$fullname/g;
    $msg =~ s/\$kgak/$kgak/g;
	print $msg;
}
###########$BL?L>$N$_0MMj(B############
elsif ($order3 ne "")  {
	$msg = <<"ORDER003";
Content-type: text/html

<HTML>
<HEAD>
   <TITLE>$BL?L>$N$40MMj(B</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=x-sjis">
</HEAD>
<BODY BGCOLOR="#FFFFFF" BACKGROUND="/~kazu-y/image/wall.jpg">
<P><TABLE BORDER=0 CELLSPACING=0 CELLPADDING=0 WIDTH=640>
   <TR>
      <TD>
        <CENTER><FONT SIZE="+3"><B><U>$B$4CmJ8FbMF$N$43NG'(B</U></B></FONT></CENTER>
         
         <BLOCKQUOTE>$B$3$N2hLL$O!"$4CmJ8FbMF$r$43NG'D:$/$?$a$N$b$N$G$9!#FbMF$K8m$j$,$"$k>l9g$O!"%V%i%&%6$N!VLa$k!W%\%?%s$r2!$7$F!VF~NO%U%)!<%`!W$+$i=$@5$7$F2<$5$$!#$3$l$G59$7$1$l$P!VCmJ8!W%\%?%s$r2!$7$F2<$5$$!#(B</BLOCKQUOTE>
         
         <CENTER><B>$B$4CmJ8FbMF(B</B><BR>
         <TABLE BORDER=1 WIDTH="90%">
   <TR>
      <TD WIDTH=148>
         <P>$B$40MMj<T(B($B5.J}(B)$B$N$*L>A0(B</P>
      </TD>
      <TD>
         <P>\$name</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>$B$40MMj<T$N%a!<%k%"%I%l%9(B</P>
      </TD>
      <TD>
         <P>\$email</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>$B$40MMj$NFbMF(B</P>
      </TD>
      <TD>
         <P>$B?7@8;y$NL?L>0MMj(B</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>$B$40MMj<g$5$^$N>pJs(B<BR>
         ($B$*5^$.$NJ}$N$_(B)</P>
      </TD>
      <TD>
         <P><TABLE BORDER=1>
            <TR>
               <TD WIDTH=64>
                  <P>$BM9JXHV9f(B</P>
               </TD>
               <TD>
                  <P>\$zipcord</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=64>
                  <P>$B=;=j(B</P>
               </TD>
               <TD>
                  <P>\$address</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=64>
                  <P>$B$*EEOCHV9f(B</P>
               </TD>
               <TD>
                  <P>\$tel</P>
               </TD>
            </TR>
         </TABLE>
         </P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>$B?7@8;y$NL?L>0MMj(B</P>
      </TD>
      <TD>
         <P><TABLE BORDER=1>
            <TR>
               <TD WIDTH=90>
                  <P>$B@+(B($BID;z(B)</P>
               </TD>
               <TD>
                  <P>\$familyname</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=90>
                  <P>$B=P@8F|(B($BM=DjF|(B)</P>
               </TD>
               <TD>
                  <P>\$brthday</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=90>
                  <P>$B2a5n$N$40MMj(B</P>
               </TD>
               <TD>
                  <P>\$user</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=90>
                  <P>$B$47;Do$N$*L>A0(B</P>
               </TD>
               <TD>
                  <P>\$brother</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=90>
                  <P>$B$4MWK>;v9`(B</P>
               </TD>
               <TD>
                  <P>\$request</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=90>
                  <P>$BFC5-;v9`(B</P>
               </TD>
               <TD>
                  <P>\$exp</P>
               </TD>
            </TR>
         </TABLE>
         </P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>$B9g7W$*;YJ'$$6b3[(B</P>
      </TD>
      <TD>
         <P>\$kgak $B1_(B</P>
      </TD>
   </TR>
         </TABLE>
</CENTER>
         
         <BLOCKQUOTE>
            <B>$B$43NG'$,:Q$_$^$7$?$i(B</B><FONT COLOR="#FF0000"><B>$B2<5-!VCmJ8!W%\%?%s$r(B1$B2s$@$12!$7$F$4H/Cm(B</B></FONT><B>$B$/$@$5$$!#:G6a!"%a!<%k%"%I%l%9$N4V0c$$$,B?$$$h$&$G$9!#%a!<%k%"%I%l%9$r$b$&0lEY!"$43NG'2<$5$$!#(B<BR>
            $B$J$*!">&IJ$N@-3J>e!"$3$l0J9_$N$4CmJ8$N<h$j>C$7$dJVIJ$O0l@Z=PMh$^$;$s$N$GM=$a$4N;>52<$5$$!#(B($BK,LdHNGdK!$N%/!<%j%s%0%*%U$OE,MQ$5$l$^$;$s!#!K(B</B></BLOCKQUOTE>
         
         <CENTER>$B$4CmJ8$ND{@5$O!"%V%i%&%6$N!VLa$k!W$G!VF~NO%U%)!<%`!W$+$i$d$jD>$7$F2<$5$$!#(B</CENTER>
         
         <P><FORM ACTION="/~kazu-y/cgi_bin2/nn_mail.cgi" METHOD=POST>
            <P><INPUT TYPE="hidden" NAME="name" VALUE="\$name">
            <INPUT TYPE="hidden" NAME="email" VALUE="\$email">
            <INPUT TYPE="hidden" NAME="order1" VALUE="">
            <INPUT TYPE="hidden" NAME="order2" VALUE="">
            <INPUT TYPE="hidden" NAME="order3" VALUE="\$order3">
            <INPUT TYPE="hidden" NAME="zipcord" VALUE="\$zipcord">
            <INPUT TYPE="hidden" NAME="address" VALUE="\$address">
            <INPUT TYPE="hidden" NAME="tel" VALUE="\$tel">
            <INPUT TYPE="hidden" NAME="fullname" VALUE="">
            <INPUT TYPE="hidden" NAME="familyname" VALUE="\$familyname">
            <INPUT TYPE="hidden" NAME="brthday" VALUE="\$brthday">
            <INPUT TYPE="hidden" NAME="user" VALUE="\$user">
            <INPUT TYPE="hidden" NAME="brother" VALUE="\$brother">
            <INPUT TYPE="hidden" NAME="request" VALUE="\$request">
            <INPUT TYPE="hidden" NAME="exp" VALUE="\$exp">
            <INPUT TYPE="hidden" NAME="kgak" VALUE="\$kgak">
            <CENTER><INPUT TYPE=submit NAME="$BAw?.(B" VALUE="$BCmJ8(B"></CENTER>
         </FORM></P></CENTER>
      </TD>
   </TR>
</TABLE>
</P>
</BODY>
</HTML>

ORDER003
&jcode'convert(*msg, "sjis", "euc");
	$msg =~ s/\$name/$name/g;
	$msg =~ s/\$email/$email/g;	
	$msg =~ s/\$order3/$order3/g;	
	$msg =~ s/\$zipcord/$zipcord/g;
	$msg =~ s/\$address/$address/g;
	$msg =~ s/\$tel/$tel/g;
	$msg =~ s/\$familyname/$familyname/g;
	$msg =~ s/\$brthday/$brthday/g;
	$msg =~ s/\$user/$user/g;
	$msg =~ s/\$brother/$brother/g;
	$msg =~ s/\$request/$request/g;
	$msg =~ s/\$exp/$exp/g;
	$msg =~ s/\$kgak/$kgak/g;
	print $msg;
}
__end__
