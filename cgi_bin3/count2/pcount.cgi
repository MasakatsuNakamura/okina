#! /usr/local/bin/perl

;#####################################################
;#
;#  Graphical Access Counter PRO (G-counter PRO) v3.0
;#  (c)rescue.ne.jp
;#
;#####################################################

# 設置構成
#
# ホームページディレクトリ
#            |
#            |-- index.html (このファイルにカウンタを表示する) (*)
#            |
#            |          このファイルのカウンタを表示させたい場所に次のSSIコマンドを書く.
#            |          <!--#exec cmd="./count/pcount.cgi"-->
#            |
#            |-- cgi_bin3
#                   |--count/ <777>
#                         |
#                         |-- pcount.cgi (このスクリプト) <755>
#                         |-- count.txt (累計カウント開始数が入ったファイル) <666>
#                         |-- day.txt (日計カウント開始数が入ったファイル) <666>
#                         |-- date.txt (本日の日..25日なら25..が入ったファイル) <666>
#                         |-- old.txt (昨日のカウント数が入ったファイル) <666>


#■(*)印のファイルから見たcount/ディレクトリの位置を設定(パス) <絶対パスで書いてもよい>
$basedir = './cgi_bin3/count2/';

#■ＣＧＩ二重起動防止ロック処理
#　通常は 1 に設定しますが、symlinkの使えない極一部のサーバでは「常にBUSY」になりますので、
#　その場合は 2 に設定してください.　1 よりも 2 の方が処理が甘くなります.
#
#  　0:ロック処理しない 1:ロック処理(symlink) 2:ロック処理(open)

$lock_key = 1;


#◇--- ここから先は十分な知識がない場合は改変しないこと ---◇

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
