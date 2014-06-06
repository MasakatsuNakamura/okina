#!/usr/local/bin/perl
#↑（注）perlのパスを確認してください。

use Socket;

require "./dclick_perl.pl";
#use dclick_perl;

#dclick SSI 対応
#初期設定

#注意！必ずご自身の広告IDに変更してください。
$id = "B00369";

#表示させたい広告数を入力してください(1〜3)
$number = 1;

#表示させたいhtmlの中に以下のコマンドを挿入してください。
#<!--#exec cgi="./dclick_ssi.cgi"-->
#もしくは <!--#include file="./dclick_ssi.cgi"-->

#左から（ID,広告数）
@banner=&dclick_perl'dclick($id,$number);

print "Content-type: text/html\n\n";
for($i = 0;$i < $number;$i++){
	print "$banner[$i]<br>";
}