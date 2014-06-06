#! /usr/local/bin/perl

;#####################################################
;#
;#  Graphical Access Counter PRO (G-counter PRO) v3.0
;#  (c)rescue.ne.jp
;#
;#####################################################

# ���ֹ���
#
# �ۡ���ڡ����ǥ��쥯�ȥ�
#            |
#            |-- index.html (���Υե�����˥����󥿤�ɽ������) (*)
#            |
#            |          ���Υե�����Υ����󥿤�ɽ�������������˼���SSI���ޥ�ɤ��.
#            |          <!--#exec cmd="./count/pcount.cgi"-->
#            |
#            |-- cgi_bin3
#                   |--count/ <777>
#                         |
#                         |-- pcount.cgi (���Υ�����ץ�) <755>
#                         |-- count.txt (�߷ץ�����ȳ��Ͽ������ä��ե�����) <666>
#                         |-- day.txt (���ץ�����ȳ��Ͽ������ä��ե�����) <666>
#                         |-- date.txt (��������..25���ʤ�25..�����ä��ե�����) <666>
#                         |-- old.txt (�����Υ�����ȿ������ä��ե�����) <666>


#��(*)���Υե����뤫�鸫��count/�ǥ��쥯�ȥ�ΰ��֤�����(�ѥ�) <���Хѥ��ǽ񤤤Ƥ�褤>
$basedir = './cgi_bin3/count2/';

#���ãǣ���ŵ�ư�ɻߥ�å�����
#���̾�� 1 �����ꤷ�ޤ�����symlink�λȤ��ʤ��˰����Υ����ФǤϡ־��BUSY�פˤʤ�ޤ��Τǡ�
#�����ξ��� 2 �����ꤷ�Ƥ�������.��1 ���� 2 �������������Ť��ʤ�ޤ�.
#
#  ��0:��å��������ʤ� 1:��å�����(symlink) 2:��å�����(open)

$lock_key = 1;


#��--- ����������Ͻ�ʬ���μ����ʤ����ϲ��Ѥ��ʤ����� ---��

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
