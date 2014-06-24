#! /usr/local/bin/perl

;#####################################################
;#
;#  Graphical Access Counter PRO (G-counter PRO) v3.0
;#  (c)rescue.ne.jp
;#
;#####################################################

# $B@_CV9=@.(B
#
# $B%[!<%`%Z!<%8%G%#%l%/%H%j(B
#            |
#            |-- index.html ($B$3$N%U%!%$%k$K%+%&%s%?$rI=<($9$k(B) (*)
#            |
#            |          $B$3$N%U%!%$%k$N%+%&%s%?$rI=<($5$;$?$$>l=j$K<!$N(BSSI$B%3%^%s%I$r=q$/(B.
#            |          <!--#exec cmd="./count/pcount.cgi"-->
#            |
#            |-- cgi_bin3
#                   |--count/ <777>
#                         |
#                         |-- pcount.cgi ($B$3$N%9%/%j%W%H(B) <755>
#                         |-- count.txt ($BN_7W%+%&%s%H3+;O?t$,F~$C$?%U%!%$%k(B) <666>
#                         |-- day.txt ($BF|7W%+%&%s%H3+;O?t$,F~$C$?%U%!%$%k(B) <666>
#                         |-- date.txt ($BK\F|$NF|(B..25$BF|$J$i(B25..$B$,F~$C$?%U%!%$%k(B) <666>
#                         |-- old.txt ($B:rF|$N%+%&%s%H?t$,F~$C$?%U%!%$%k(B) <666>


#$B"#(B(*)$B0u$N%U%!%$%k$+$i8+$?(Bcount/$B%G%#%l%/%H%j$N0LCV$r@_Dj(B($B%Q%9(B) <$B@dBP%Q%9$G=q$$$F$b$h$$(B>
$basedir = './cgi_bin3/count2/';

#$B"##C#G#IFs=E5/F0KI;_%m%C%/=hM}(B
#$B!!DL>o$O(B 1 $B$K@_Dj$7$^$9$,!"(Bsymlink$B$N;H$($J$$6K0lIt$N%5!<%P$G$O!V>o$K(BBUSY$B!W$K$J$j$^$9$N$G!"(B
#$B!!$=$N>l9g$O(B 2 $B$K@_Dj$7$F$/$@$5$$(B.$B!!(B1 $B$h$j$b(B 2 $B$NJ}$,=hM}$,4E$/$J$j$^$9(B.
#
#  $B!!(B0:$B%m%C%/=hM}$7$J$$(B 1:$B%m%C%/=hM}(B(symlink) 2:$B%m%C%/=hM}(B(open)

$lock_key = 1;


#$B!~(B--- $B$3$3$+$i@h$O==J,$JCN<1$,$J$$>l9g$O2~JQ$7$J$$$3$H(B ---$B!~(B

$file = $basedir . 'count.txt';
$file_day = $basedir . 'day.txt';
$file_date = $basedir . 'date.txt';
$file_old = $basedir . 'old.txt';
$lockfile = $basedir . 'count.lock';

if ($lock_key == 1) { &lock; }
elsif ($lock_key == 2) { &lock2; }

($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime(time);

if (!open(NEW,">$file.tmp")) { &error('ERROR1'); }
select(NEW); $| = 1; select(STDOUT);

if (!open(IN,$file)) { &error('ERROR2'); }
$count = <IN>; chop($count) if $count =~ /\n/;

#--#

if (!open(NEW2,">$file_day.tmp")) { &error('ERROR3'); }
select(NEW2); $| = 1; select(STDOUT);

if (!open(IN2,"$file_day")) { &error('ERROR4'); }
$count2 = <IN2>; chop($count2) if $count2 =~ /\n/;

#--#

if (!open(DAY,"$file_date")) { &error('ERROR5'); }
$fd = <DAY>; chop($fd) if $fd =~ /\n/;
close(DAY);

if ($fd eq '' || $fd ne $mday) {

   if (!open(DAY,">$file_date")) { &error('ERROR6'); }
   print DAY $mday;
   close(DAY);

   if (!open(OLD,">$file_old")) { &error('ERROR7'); }
   print OLD $count2;
   close(OLD);

   $count2 = 1;
}

else {

   $count2++;
}

$count++; print NEW $count;
print NEW2 $count2;

close NEW;
close IN;
close NEW2;
close IN2;

if (!rename("$file.tmp",$file)) { &error('ERROR8'); }
if (!rename("$file_day.tmp",$file_day)) { &error('ERROR9'); }

#--------------#
print $count;
#--------------#

if (-e $lockfile) { unlink($lockfile); }
exit;

sub lock {

        local($retry) = 3;
        while (!symlink(".", $lockfile)) {

                if (--$retry <= 0) { &error('BUSY'); }
                sleep(2);
        }
}

sub lock2 {

        $c = 0;
        while(-f "$lockfile") {

                $c++;
                if ($c >= 3) { &error('BUSY'); }
                sleep(2);
        }
        open(LOCK,">$lockfile");
        close(LOCK);
}

sub error {

        if (-e $lockfile) { unlink($lockfile); }
        print $_[0];
        exit;
}
