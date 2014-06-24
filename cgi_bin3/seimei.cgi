#!/usr/local/bin/perl
require "jcode.pl";
require "cgi-lib.pl";
require "kakusu.pl";
require "reii.pl";
require "seikaku.pl";
require "kenkou.pl";

# 会社環境テスト用
#$root = "/~nakamura/test/seimei2/public_html";
#$cgipath = "/~nakamura/test/seimei2/cgi_bin";
#$baseurl = "http://ppd.sf.nara.sharp.co.jp";

# まほろばWWW2用
$root = "/~kazu-y";
$cgipath = "/~kazu-y/cgi_bin3";
#$baseurl = "http://www2.mahoroba.ne.jp";



# CGI変数取りこみ
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

# 々の処理
$sei1 =~ s/(..)\x81\x58/$1$1/;
$mei1 =~ s/(..)\x81\x58/$1$1/;

# 天画・人画・地画・外画・総画の算出(結構ややこしい)
$kakusu{'tenkaku'} = 0;
$kakusu{'chikaku'} = 0;
$kakusu{'gaikaku'} = 0;
$kakusu{'soukaku'} = 0;
@error = ();

# 天画の算出
for ($i = 0; $i<length($sei1); $i+=2) {
	$kanji = substr($sei1, $i, 2);
	$kakusu = &kakusu($kanji);
	if ($kakusu == 0) {
		push (@error, $kanji);
	}
	$kakusu{'tenkaku'} += $kakusu;
}

# 一文字姓の処理
if (length($sei1) == 2) {
	$kakusu{'tenkaku'}++; # 一画借りる
	$kakusu{'gaikaku'}++;
	$kakusu{'soukaku'}--; # 一画返す
}

# 人画の算出
$kakusu{'jinkaku'} = &kakusu(substr($sei1, length($sei1)-2, 2)) + &kakusu(substr($mei1, 0, 2));

# 地画の算出
for ($i = 0; $i<length($mei1); $i+=2) {
	$kanji = substr($mei1, $i, 2);
	$kakusu = &kakusu($kanji);
	if ($kakusu == 0) {
		push (@error, $kanji);
	}
	$kakusu{'chikaku'} += $kakusu;
}

# 一文字名の処理
if (length($mei1) == 2) {
	$kakusu{'chikaku'}++; # 一画借りる
	$kakusu{'gaikaku'}++;
	$kakusu{'soukaku'}--; # 一画返す
}

# 総画・外画の算出
$kakusu{'soukaku'} += $kakusu{'tenkaku'} + $kakusu{'chikaku'};
$kakusu{'gaikaku'} += $kakusu{'soukaku'} - $kakusu{'jinkaku'};

#姓字1・姓字2・名字1・名字2の算出
$seijib = &kakusu(substr($sei1, length($sei1)-2, 2));
$meijia = &kakusu(substr($mei1, 0, 2));
if (length($mei1) == 2) {
	$seijia = $kakusu{'soukaku'} - $kakusu{'jinkaku'};
}else {
	$seijia = $kakusu{'soukaku'} - $kakusu{'chikaku'} - $seijib;
}
$meijib = $kakusu{'soukaku'} - $kakusu{'jinkaku'} - $seijia;


# オーバーフロー処理 - ちなみに > 81は間違いではない。
foreach (keys %kakusu) {
	$kakusu{$_} %= 80 if ($kakusu{$_} > 81);
}

# 天画・人画・地画の下一桁の算出(10で割った余りを取るだけ)
$tenshimo = $kakusu{'tenkaku'} % 10;
$jinshimo = $kakusu{'jinkaku'} % 10;
$chishimo = $kakusu{'chikaku'} % 10;

# 性格診断の準備
$kakusu{'seikaku'} = $jinshimo;

# 陰陽五行のシリアル番号の算出(詳しくはkenkou.plを参照)
$kakusu{'kenkou'} = &f($tenshimo)*25 + &f($jinshimo) *5 + &f($chishimo);

# 曲名決定
#$kyoku = $jinshimo;
#$kyoku = 10 if ($kyoku == 0);
#$kyoku -= 1;
#$kyoku -= $kyoku % 2;
#$kyoku /= 2;
#$kyoku++;

# 占い結果の整形処理
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
	# エラー漢字が一文字でもあればエラー表示
	$msg = <<"EOK";
Content-type: text/html

<HTML>
<HEAD>
   <TITLE>エラーメッセージ</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=x-sjis">
</HEAD>

<BODY BGCOLOR="#FFFFFF" BACKGROUND="$root/image/wall.jpg">
<P><HTML><HEAD><TITLE>エラーメッセージ</TITLE></HEAD></P>

<P><TABLE BORDER=0 CELLSPACING=0 CELLPADDING=0 WIDTH=640>
   <TR>
      <TD>
         <CENTER><FONT SIZE="+3" COLOR="#FF0000"><B>入力された漢字「
         \$error 」が判別できません。</B></FONT>
         
         <P>誠に恐れ入りますが、下記の送信フォームをご確認後、「送信」ボタンを押して下さい。<BR>
         山本翁が正確に漢字の画数判定を行い、下記メールアドレスまでご連絡差し上げます。</P>
         
         <P>お急ぎの場合には、該当する漢字の画数を2桁の<B>半角</B>算用数字で入力して下さい。<BR>
         例、山田太郎→山田太14（「郎」にエラーメッセージが出た場合。）</P>
         
         <P>ご契約に基づきデータベースの更新作業時には、今回のエラー漢字を反映させて頂きます。</P></CENTER>
         
         <P>
         
         <HR>
         
         </P>
      </TD>
   </TR>
   <TR>
      <TD>
         <CENTER><FONT SIZE="+3"><B>翁からのお詫び</B></FONT></CENTER>
         
         <P><U>文字の画数データベースについて</U></P>
         
         <P>現在、名前に用いられる漢字は、当用漢字と人名漢字です。登録漢字
         はこの4000文字以上を網羅しておりますが、過去からある姓名にはこれに該当しないものが幾つもあります。山本翁の経験から過去、翁が接したことのある姓名については出来るかぎりデータベースには登録しております。しかしながら、全てが登録されているとは言い難く、また登録漏れがないとも限りません。</P>
         
         <P>今回はそう言った稀なケースであると思われます。誠にお手数ですが、下記の内容をご確認頂き(メールアドレスは管理者の指示に従ってください)、送信して頂ければ、後日、翁から漢字の画数をお知らせ致します。今後のデータベースに反映させて頂きます。</P>
         
         <CENTER><FORM ACTION="$cgipath/n_mail2.cgi" METHOD=POST>
            <BLOCKQUOTE><BLOCKQUOTE><CENTER><TABLE BORDER=0 CELLSPACING=10 CELLPADDING=0>
                     <TR>
                        <TD>
                           <P ALIGN=right>エラーになった漢字</P>
                        </TD>
                        <TD>
                           <P><INPUT TYPE=hidden NAME=kanji VALUE="\$error" SIZE=10 MAXLENGTH=10>\$error</P>
                        </TD>
                     </TR>
                     <TR>
                        <TD>
                           <P ALIGN=right>お名前</P>
                        </TD>
                        <TD>
                           <P><INPUT TYPE=text NAME=name2 VALUE="\$seimei" SIZE=20 MAXLENGTH=10></P>
                        </TD>
                     </TR>
                     <TR>
                        <TD>
                           <P ALIGN=right>メールアドレス</P>
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
                           <P><INPUT TYPE=submit NAME="送信" VALUE="送信"><INPUT TYPE=reset VALUE="取り消し"></P>
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
         <CENTER><A HREF="$root/input3.html" TARGET="_self"><B>もう一度鑑定する</B></A>
         
         <P><B>
         
         <HR>
         
         </B></P></CENTER>
      </TD>
   </TR>
   <TR>
      <TD>
         <CENTER><FONT SIZE="-2">このプログラムは企業向けイントラネット版です。WWWでの商用利用はできません。<BR>
         このプログラムのライセンスを受けた企業以外の第三者へ転売、再配付を禁止します。<BR>
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
	# 判定結果表示
	$msg = <<"EOM";
Content-type: text/html

<HTML>
<HEAD>
   <TITLE>山本翁の鑑定結果</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=x-sjis">
</HEAD>
<BODY BGCOLOR="#FFFFFF" BACKGROUND="$root/image/wall.jpg">
<P><HTML><HEAD><TITLE>山本翁の姓名判断</TITLE></HEAD></P>

<CENTER><TABLE BORDER=0 CELLSPACING=0 WIDTH=640>
   <TR>
      <TD>
         <CENTER><FONT SIZE="+3" COLOR="#00CC00"><B>\$seimeiさんの鑑定結果</B></FONT></CENTER>
         
         <P>
         
         <HR>
         
         </P>
         
         <P>基礎データ：姓A=$seijia,　姓B=$seijib,　天画=$kakusu{'tenkaku'},　名A=$meijia,　名B=$meijib
<FORM ACTION="seimei.cgi" METHOD=POST>
            <CENTER><TABLE BORDER=0 CELLSPACING=5 WIDTH=160>
               <TR>
                  <TD>
                     <CENTER>姓<BR>
                     <INPUT TYPE=text NAME=sei VALUE="\$sei" SIZE=10 MAXLENGTH=10></CENTER>
                  </TD>
                  <TD>
                     <CENTER>名<BR>
                     <INPUT TYPE=text NAME=mei VALUE="" SIZE=10 MAXLENGTH=10></CENTER>
                  </TD>
               </TR><INPUT TYPE=hidden NAME=sex VALUE="\$sex" size=10 maxlength=10>
       <INPUT TYPE=hidden NAME=marry VALUE="\$marry" size=10 maxlength=10>
               <TR>
                  <TD>
                     <CENTER><INPUT TYPE=submit NAME="送信" VALUE="鑑定"></CENTER>
                  </TD>
                  <TD>
                     <CENTER><A HREF="$root/input3.html">戻る</A></CENTER>
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
                  <P><FONT SIZE="+2" COLOR="#B30000"><B><U>主運</U></B></FONT>
                  <FONT SIZE="-1" COLOR="#B30000">；当人の一生の中心を司ります。結婚により姓が変わると主運も変わりますが、中年以降に強く現れます。</FONT></P>
                  
                  <BLOCKQUOTE>$kakusu{'jinkaku'}画：$res{'jinkaku'}</BLOCKQUOTE>
                  
                  <P></P>
               </TD>
               <TD VALIGN=top>
                  <P><FONT SIZE="+2" COLOR="#1D00B3"><B><U>対人運・社交運</U></B></FONT>
                  <FONT SIZE="-1" COLOR="#1D00B3">；対人関係や家族・夫婦関係、友達関係に現れてきます。</FONT></P>
                  
                  <BLOCKQUOTE>$kakusu{'gaikaku'}画：$res{'gaikaku'}</BLOCKQUOTE>
                  
                  <P></P>
               </TD>
            </TR>
            <TR>
               <TD VALIGN=top>
                  <P><FONT SIZE="+2" COLOR="#007F1F"><B><U>健康運(体調・精神)</U></B></FONT>
                  <FONT SIZE="-1" COLOR="#007F1F">；例え吉数揃いの姓名であっても、健康に恵まれなければ活かさせません。</FONT></P>
                  
                  <BLOCKQUOTE>$res{'kenkou'}</BLOCKQUOTE>
                  
                  <P></P>
               </TD>
               <TD VALIGN=top>
                  <P><FONT SIZE="+2" COLOR="#B35900"><B><U>性格</U></B></FONT>
                  <FONT SIZE="-1" COLOR="#B35900">；当人の外面的な性格を現します。自分が他人からどう見えているのか参考になります。</FONT></P>
                  
                  <BLOCKQUOTE>$res{'seikaku'}</BLOCKQUOTE>
                  
                  <P></P>
               </TD>
            </TR>
            <TR>
               <TD VALIGN=top>
                  <P><FONT SIZE="+2" COLOR="#7F0260"><B><U>基礎運</U></B></FONT>
                  <FONT SIZE="-1" COLOR="#7F0260">；幼少年期の運勢の吉凶を支配し、青年期まで最も強く作用します。(若年者の判断はこちらが有効)</FONT></P>
                  
                  <BLOCKQUOTE>$kakusu{'chikaku'}画：$res{'chikaku'}</BLOCKQUOTE>
                  
                  <P></P>
               </TD>
               <TD VALIGN=top>
                  <P><FONT SIZE="+2" COLOR="#B30068"><B><U>晩年運</U></B></FONT>
                  <FONT SIZE="-1" COLOR="#B30068">；50歳前後から強く現れてきます。ただし、主運と基礎運に左右されますので注意して下さい。</FONT></P>
                  
                  <BLOCKQUOTE>$kakusu{'soukaku'}画：$res{'soukaku'}</BLOCKQUOTE>
                  
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
         <CENTER><A HREF="$root/input3.html" TARGET="_self"><B>もう一度鑑定をする</B></A>
         
         <P><B>
         
         <HR>
         
         </B></P></CENTER>
      </TD>
   </TR>
   <TR>
      <TD>
         <CENTER><FONT SIZE="-2">このプログラムは企業向けイントラネット版です。WWWでの商用利用はできません。<BR>
         このプログラムのライセンスを受けた企業以外の第三者へ転売、再配付を禁止します。<BR>
         <I>CopyRight. K.Yamamoto.1999.3.21</I></FONT></CENTER>
      </TD>
   </TR>
</TABLE>
 <FONT SIZE="-1">　</FONT>　　　 　　　</CENTER>
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
