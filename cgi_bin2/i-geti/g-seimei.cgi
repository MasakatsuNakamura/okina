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

# 山一環境用
$root = "/~kazu-y";
$cgipath = "/~kazu-y/cgi_bin2";
$baseurl = "http://www2.mahoroba.ne.jp";



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
$kyoku = $jinshimo;
$kyoku = 10 if ($kyoku == 0);
$kyoku -= 1;
$kyoku -= $kyoku % 2;
$kyoku /= 2;
$kyoku++;

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

<BODY BGCOLOR="#FFFFFF">
<CENTER><FONT SIZE="+3"><B>入力された漢字「\$error」
が判別できません。</B></FONT>

<P>誠に恐れ入りますが、<A HREF="#form" TARGET="_self"><B>下記のフォーム</B></A>のにご記入の上、送信ボタンを押してください。<BR>
漢字データベースの修正が完了しましたら、ご指定のメールアドレスまでご連絡差し上げます。</P>

<P>

<HR>

<FONT SIZE="+3"><B>翁からのお詫び</B></FONT></P></CENTER>

<P><U>文字の画数データベースについて</U></P>

<P>現在、名前に用いられる漢字は、当用漢字と人名漢字です。登録漢字
はこの約2000文字を網羅しておりますが、過去からある姓名にはこれに該当しないものが幾つかあります。山本翁の経験から過去、翁が接したことのある姓名については出来るかぎりデータベースには登録しております。しかしながら、全てが登録されているとは言い難く、また登録漏れがないとも限りません。</P>

<P>今回はそう言った稀なケースであると思われます。誠にお手数ですが、下記のフォームにご記入頂きましたら、後日こちらより結果をご連絡させていただきます。今後のデータベースに反映させて頂きたいと考えますので、ご協力宜しくお願い申し上げます。</P>

<CENTER><FORM ACTION="$cgipath/gn_mail2.cgi" METHOD=POST>
   <BLOCKQUOTE><BLOCKQUOTE><CENTER><A NAME=form></A><TABLE BORDER=0 CELLSPACING=10 CELLPADDING=0>
            <TR>
               <TD>
                  <P ALIGN=right>エラーになった漢字</P>
               </TD>
               <TD>
                  <P><INPUT TYPE=hidden NAME=kanji VALUE="\$error" size=10 maxlength=10>\$error</P>
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
</FORM>

<P>

<HR>

<TABLE BORDER=1 WIDTH=600>
   <TR>
      <TD>
         <CENTER><A HREF="$root/g-index.html" TARGET="_self"><B>トップページ</B></A></CENTER>
      </TD>
      <TD>
         <CENTER><A HREF="$root/g-input.html" TARGET="_self"><B>もう一度鑑定する</B></A></CENTER>
      </TD>
      <TD>
         <CENTER><A HREF="$root/g-book.html" TARGET="_self"><B>著書のコーナー</B></A></CENTER>
      </TD>
      <TD>
         <CENTER><A HREF="$root/g-baby.html" TARGET="_self"><B>命名のコーナー</B></A></CENTER>
      </TD>
      <TD>
         <CENTER><A HREF="$root/g-info.html"><B>翁からのお知らせ</B></A></CENTER>
      </TD>
   </TR>
</TABLE>
 　　 <FONT SIZE="-2">

<HR>

リンクは歓迎しますが、必ず</FONT><A HREF="$root/g-index.html" TARGET="_self"><FONT SIZE="-2"><I>TOPページ</I></FONT></A><FONT SIZE="-2">へお願いします。<BR>
このコンテンツの商用利用ならびに無断転載はお断り致します。<BR>
<I>CopyRight. K.Yamamoto.1999.5.8</I></FONT></P></CENTER>
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
                           <CENTER><FONT SIZE="+2"><B>\$seimeiさんへの助言</B></FONT></CENTER>
                        </TD>
                     </TR>
                  </TABLE>
                   </B></FONT></CENTER>
               </TD>
               <TD VALIGN=top WIDTH=300 HEIGHT=170 BGCOLOR="#CCCCCC">
                  <CENTER><B><U>山本翁より</U></B></CENTER>
                  
                  <P>　主運・対人運・基礎運・晩年運と一見矛盾するような結果を示すこともあります。これは人間というものは、外見と本心が違うのも常ですし、人生も波あり風ありということで、鑑定結果にもそれは現れてきているとご理解下さい。従って、まず鑑定結果全体を眺めて頂き、次に個々の部分について自分なりに分析されてみる事をお薦めします。なお、本当の鑑定というのは、前述のような人それぞれの境遇や回りの環境を総合的に加味して判断するのですが、インターネットではそこまでの事が出来ませんので、悪しからずご了承下さい。</P>
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
                  <P><FONT SIZE="+2"><B>主運</B>
                  </FONT><FONT SIZE="-1"><U>；当人の一生の中心を司ります。結婚により姓が変わると主運も変わりますが、中年以降に強く現れます。</U></FONT></P>
                  
                  <BLOCKQUOTE>$kakusu{'jinkaku'}画：$res{'jinkaku'}</BLOCKQUOTE>
                  
                  <P></P>
               </TD>
               <TD VALIGN=top>
                  <P><FONT SIZE="+2"><B>対人運・社交運</B></FONT><FONT SIZE="-1"><B>
                  </B><U>；対人関係や家族・夫婦関係、友達関係に現れてきます。</U></FONT></P>
                  
                  <BLOCKQUOTE>$kakusu{'gaikaku'}画：$res{'gaikaku'}</BLOCKQUOTE>
                  
                  <P></P>
               </TD>
            </TR>
            <TR>
               <TD VALIGN=top>
                  <P><FONT SIZE="+2"><B>健康運(体調・精神)
                  </B></FONT><FONT SIZE="-1"><U>；例え吉数揃いの姓名であっても、健康に恵まれなければ活かさせません。</U></FONT></P>
                  
                  <BLOCKQUOTE>$res{'kenkou'}</BLOCKQUOTE>
                  
                  <P></P>
               </TD>
               <TD VALIGN=top>
                  <P><FONT SIZE="+2"><B>性格
                  </B></FONT><FONT SIZE="-1"><U>；当人の外面的な性格を現します。自分が他人からどう見えているのか参考になります。</U></FONT></P>
                  
                  <BLOCKQUOTE>$res{'seikaku'}</BLOCKQUOTE>
                  
                  <P></P>
               </TD>
            </TR>
            <TR>
               <TD VALIGN=top>
                  <P><FONT SIZE="+2"><B>基礎運
                  </B></FONT><FONT SIZE="-1"><U>；幼少年期の運勢の吉凶を支配し、青年期まで最も強く作用します。(若年者の判断はこちらが有効)</U></FONT></P>
                  
                  <BLOCKQUOTE>$kakusu{'chikaku'}画：$res{'chikaku'}</BLOCKQUOTE>
                  
                  <P></P>
               </TD>
               <TD VALIGN=top>
                  <P><FONT SIZE="+2"><B>晩年運
                  </B></FONT><FONT SIZE="-1"><U>；50歳前後から強く現れてきます。ただし、主運と基礎運に左右されますので注意して下さい。</U></FONT></P>
                  
                  <BLOCKQUOTE>$kakusu{'soukaku'}画：$res{'soukaku'}</BLOCKQUOTE>
                  
                  <P></P>
               </TD>
            </TR>
         </TABLE>
         </P>
         
         <CENTER><B>鑑定結果が気になる方は、｢著書のコーナー｣｢翁からのお知らせ｣も併せてご覧下さい。</B></CENTER>
         
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
                  <CENTER><A HREF="$root/i-geti.html" TARGET="_self"><B>トップページ</B></A></CENTER>
               </TD>
               <TD>
                  <CENTER><A HREF="$root/g-input.html" TARGET="_self"><B>もう一度鑑定する</B></A></CENTER>
               </TD>
               <TD>
                  <CENTER><A HREF="$root/g-book.html" TARGET="_self"><B>著書のコーナー</B></A></CENTER>
               </TD>
               <TD>
                  <CENTER><A HREF="$root/g-baby.html" TARGET="_self"><B>命名のコーナー</B></A></CENTER>
               </TD>
               <TD>
                  <CENTER><A HREF="$root/g-info.html" TARGET="_self"><B>翁からのお知らせ</B></A></CENTER>
               </TD>
            </TR>
         </TABLE>
         
         <HR>
         
         </P>
      </TD>
   </TR>
   <TR>
      <TD>
         <CENTER>このコンテンツはシャープ(株)殿のザウルスアイゲティ<FONT SIZE="-2">(TM)</FONT>向けに特別編集されたものです。<BR>
         フルバージョンは<A HREF="http://www2.mahoroba.ne.jp/~kazy-y/index.html">こちら</A>をご覧下さい。
         
         <P>
         
         <HR>
         
         </P></CENTER>
      </TD>
   </TR>
   <TR>
      <TD>
         <CENTER><FONT SIZE="-2">この結果を見てのご意見やご感想をお聞かせ下さい。　</FONT><A HREF="mailto:okina\@e-mail.ne.jp"><FONT SIZE="-2">okina\@e-mail.ne.jp</FONT></A><FONT SIZE="-2"><I><BR>
         </I>リンクは歓迎しますが、必ず</FONT><A HREF="$root/i-geti.html" TARGET="_self"><FONT SIZE="-2">TOPページ</FONT></A><FONT SIZE="-2">へお願いします。<BR>
         このコンテンツの商用利用ならびに無断転載はお断りいたします。この鑑定は無料です。<BR>
         <I>CopyRight. K.Yamamoto. 1999.5.8</I></FONT></CENTER>
      </TD>
   </TR>
</TABLE>
</CENTER>

<P>　</P>

<P><FONT SIZE="-1">　</FONT></P>

<CENTER>　　　 　　　</CENTER>
</BODY>
</HTML>


EOM
	&jcode'convert(*msg, "sjis", "euc");
	$msg =~ s/\$seimei/$sei $mei/g;
	print $msg;
}
