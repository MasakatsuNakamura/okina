#!/usr/bin/perl
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

# ゝの処理
$sei1 =~ s/(..)\x81\x54/$1$1/;
$mei1 =~ s/(..)\x81\x54/$1$1/;

# 仝の処理
$sei1 =~ s/(..)\x81\x57/$1$1/;
$mei1 =~ s/(..)\x81\x57/$1$1/;

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

<BODY BGCOLOR="#FFFFFF" BACKGROUND="$root/image/wall.jpg">
<P><HTML><HEAD><TITLE>エラーメッセージ</TITLE></HEAD></P>

<P><TABLE BORDER=0 WIDTH=640>
   <TR>
      <TD>
         <CENTER><FONT SIZE="+3"><B>入力された漢字 「\$error」
         が判別できません。</B></FONT>
         
         <P>誠に恐れ入りますが、<A HREF="#form" TARGET="_self"><B>下記のフォーム</B></A>のにご記入の上、送信ボタンを押してください。<BR>
         漢字データベースの修正が完了しましたら、ご指定のメールアドレスまでご連絡差し上げます。また、漢字・ひらかな・カタカナ以外の英文字・数字・絵文字・記号などは山本式姓名判断では扱っておりませんので、連絡は不要です。下記の「もう一度鑑定する」を押して下さい。</P></CENTER>
         
         <P>
         
         <HR>
         
         </P>
      </TD>
   </TR>
   <TR>
      <TD>
         <CENTER><FONT SIZE="+3"><B>翁からのお詫び</B></FONT></CENTER>
         
         <P><U>文字の画数データベースについて</U></P>
         
         <P>現在、名前に用いられる漢字は、当用漢字と人名漢字です。これ以外にも実際に使われている姓名にはこれに該当しないものが幾つもあります。現在、これらの中から4580文字(2003.9現在)をデータベースに登録しております。これらは、山本翁の鑑定歴50年の経験に基づくものです。しかしながら、まだ全てが登録されているとは言い難く、また登録漏れがないとも限りません。</P>
         
         <P>今回はそう言った稀なケースであると思われます。誠にお手数ですが、下記のフォームにご記入頂きましたら、後日こちらより結果をご連絡させていただきます。今後のデータベースに反映させて頂きたいと考えますので、ご協力宜しくお願い申し上げます。<BR>
         お願い：結果のお知らせが必要でない方は、メールアドレスを空白のまま送信下さい。間違ったアドレスを記入されますと他の方に御迷惑がかかります。</P>
         
         <CENTER><FORM ACTION="$cgipath/n_mail2.cgi" METHOD=POST>
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
         
         <P><FONT SIZE="+2">
         
         <HR>
         
         </FONT><A HREF="$root/input.html" TARGET="_self"><FONT SIZE="+1">もう一度鑑定する</FONT></A></P></CENTER>
         
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
                  <CENTER><A HREF="$root/index.html" TARGET="_self">トップページ</A></CENTER>
               </TD>
               <TD>
                  <CENTER><A HREF="$root/book.html" TARGET="_self">著書のコーナー</A></CENTER>
               </TD>
               <TD>
                  <CENTER><A HREF="$root/baby.html" TARGET="_self">命名のコーナー</A></CENTER>
               </TD>
            </TR>
            <TR>
               <TD>
                  <CENTER><A HREF="$root/consul.html">ご相談のコーナー</A></CENTER>
               </TD>
               <TD>
                  <CENTER><A HREF="$root/info.html">翁からのお知らせ</A></CENTER>
               </TD>
               <TD>
                  <CENTER><A HREF="$root/link.html">「占い直行便」</A></CENTER>
               </TD>
            </TR>
         </TABLE>
         
         <HR>
         
         </P>
      </TD>
   </TR>
   <TR>
      <TD>
         <CENTER>　　
         <FONT SIZE="-2">リンクは歓迎しますが、必ず</FONT><A HREF="$root/index.html" TARGET="_self"><FONT SIZE="-2"><I>TOPページ</I></FONT></A><FONT SIZE="-2">へお願いします。<BR>
         このコンテンツの商用利用ならびに無断転載はお断り致します。<BR>
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

<BODY BGCOLOR="#FFFFFF" BACKGROUND="$root/image/wall.jpg" onload="scll()">
<P><SCRIPT LANGUAGE=JavaScript>var cnt = -2;//文字位置
var speed = 500;//動かすスピード(1/1000秒単位)
var msg = "              Webで初めて！ 鑑定結果によって音楽が5通りに変化します。鑑定の根拠や人生をより良く生きる方法については、私の著書をご覧ください。結果をより詳しく知りたい方、改名を希望される方、ご結婚の予定のある方は、有料のご相談コーナーも開設しておりますので、ご利用下さい。また、パートナーをお探しの方は、このページの広告をご参照下さい。"; //メッセージ内容
timeID=setTimeout('',1); //IE対策なにもしない;タイマーセット

//　文字を移動させる
function scll()
{
 status = msg.substring(cnt=cnt+2,msg.length+2);//日本語は2文字づつ動かす
 if (cnt>msg.length){cnt=-2};
 clearTimeout(timeID);//タイマーをクリア
 timeID = setTimeout('scll()',speed);
  }</SCRIPT></P>

<P><HTML><HEAD><TITLE>山本翁の鑑定結果</TITLE></HEAD></P>

<CENTER><TABLE BORDER=0 CELLSPACING=0 WIDTH=640>
   <TR>
      <TD>
         <P><TABLE BORDER=0 CELLSPACING=0 CELLPADDING=0 WIDTH="100%">
            <TR>
               <TD VALIGN=top WIDTH=320 HEIGHT=240 BGCOLOR="#CCCC99">
                  <CENTER><FONT SIZE="+2" COLOR="#0033FF"><B><TABLE BORDER=0 CELLSPACING=0 CELLPADDING=0 WIDTH=320 HEIGHT=240>
                     <TR>
                        <TD VALIGN=bottom BACKGROUND="$root/image/result.jpg">
                           <CENTER><FONT SIZE="+2" COLOR="#9933FF"><B>\$seimeiさんへの助言</B></FONT></CENTER>
                        </TD>
                     </TR>
                  </TABLE>
                   </B></FONT></CENTER>
               </TD>
               <TD VALIGN=top WIDTH=320 HEIGHT=240 BGCOLOR="#CCCC99">
                  <CENTER><B><U>山本翁より</U></B></CENTER>
                  
                  <P>　主運・対人運・基礎運・晩年運と一見矛盾するような結果を示すこともあります。これは人間というものは、外見と本心が違うのも常ですし、人生も波あり風ありということで、鑑定結果にもそれは現れてきているとご理解下さい。従って、まず鑑定結果全体を眺めて頂き、次に個々の部分について自分なりに分析されてみる事をお薦めします。なお、本当の鑑定というのは、前述のような人それぞれの境遇や回りの環境を総合的に加味して判断するのですが、インターネットではそこまでの事が出来ませんので、悪しからずご了承下さい。</P>
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
                  <FONT SIZE="-1" COLOR="#007F1F">；例え吉数揃いの姓名であっても、健康に恵まれなければ活かさせません。（△は単独での判断が難しい）</FONT></P>
                  
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
         <BR>
         <IMG SRC="../../image/line_a1.gif" WIDTH=640 HEIGHT=3 ALIGN=bottom></P>
         
         <P>　結果は如何でしょうか？　山本翁では様々な<FONT COLOR="#FF0000">有料サービス</FONT>も実施しておりますので、よろしければそちらもご利用下さい。また、一般的に良く聞かれるご質問について<A HREF="$root/info.html">「お知らせコーナー」</A>に纏めていますので、併せてご覧下さい。</P>
         
         <CENTER><IMG SRC="$root/image/line_a2.gif" WIDTH=640 HEIGHT=3 ALIGN=bottom>
         
         <P><TABLE BORDER=0 WIDTH="61%">
            <TR>
               <TD COLSPAN=5>
                  <CENTER><B>他のページもぜひ見に行ってください。</B></CENTER>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=68>
                  <CENTER><A HREF="$root/input.html" TARGET="_self"><FONT SIZE="+1" FACE="中ゴシック体"><IMG SRC="$root/image/seimei.gif" WIDTH=57 HEIGHT=71 BORDER=3 ALIGN=bottom></FONT></A></CENTER>
               </TD>
               <TD WIDTH=70>
                  <CENTER><A HREF="$root/book.html" TARGET="_self"><FONT SIZE="+1" FACE="中ゴシック体"><IMG SRC="$root/image/chosyo.gif" WIDTH=57 HEIGHT=71 BORDER=3 ALIGN=bottom></FONT></A></CENTER>
               </TD>
               <TD WIDTH=73>
                  <CENTER><A HREF="$root/baby.html" TARGET="_self"><FONT SIZE="+1" FACE="中ゴシック体"><IMG SRC="$root/image/baby-name.gif" WIDTH=57 HEIGHT=71 BORDER=3 ALIGN=bottom></FONT></A></CENTER>
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
         
         <P><B><U>ここからは、広告です。</U></B></P>
         
         <P>あなたの人生のパートナーはもう見つかりましたか？素晴らしい出会いを見つけて下さい。<BR>
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

         <P>医科界でオペ技術の優れていると評判の各クリニック様です。<A HREF="http://cgi.din.or.jp/~toa-ad/tsw021a/jump.cgi?053102" TARGET="_blank"><IMG SRC="$root/image/sasamoto.gif" WIDTH=380 HEIGHT=30 BORDER=0 ALIGN=bottom></A>
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
         <CENTER>　
         
         <P><TABLE BORDER=1 WIDTH="100%">
            <TR>
               <TD>
                  <CENTER><A HREF="$root/index.html" TARGET="_self">トップページ</A></CENTER>
               </TD>
               <TD>
                  <CENTER><A HREF="$root/book.html" TARGET="_self">著書のコーナー</A></CENTER>
               </TD>
               <TD>
                  <CENTER><A HREF="$root/baby.html" TARGET="_self">命名のコーナー</A></CENTER>
               </TD>
            </TR>
            <TR>
               <TD>
                  <CENTER><A HREF="$root/consul.html">「ご相談コーナー」</A></CENTER>
               </TD>
               <TD>
                  <CENTER><A HREF="$root/info.html" TARGET="_self">翁からのお知らせ</A></CENTER>
               </TD>
               <TD>
                  <CENTER><A HREF="$root/link.html">「占い直行便」</A></CENTER>
               </TD>
            </TR>
         </TABLE>
         </P>
         
         <P><IMG SRC="$root/image/line_a1.gif" WIDTH=640 HEIGHT=3 ALIGN=bottom></P></CENTER>
      </TD>
   </TR>
   <TR>
      <TD>
         <CENTER>　
         
         <P>お聞きの曲については、<A HREF="$root/info.html#midi">こちら</A>をご覧下さい。</P>
         
         <P><IMG SRC="$root/image/line_a1.gif" WIDTH=640 HEIGHT=3 ALIGN=bottom></P></CENTER>
      </TD>
   </TR>
   <TR>
      <TD>
         <CENTER>　
         
         <P><FONT SIZE="-2">この結果を見てのご意見やご感想をお聞かせ下さい。　<IMG SRC="$root/image/mail_a2.gif" WIDTH=20 HEIGHT=18 ALIGN=bottom></FONT><A HREF="mailto:okina\@e-mail.ne.jp"><FONT SIZE="-2">okina\@e-mail.ne.jp</FONT></A><FONT SIZE="-2"><I><BR>
         </I>リンクは歓迎しますが、必ず</FONT><A HREF="$root/index.html" TARGET="_self"><FONT SIZE="-2">TOPページ</FONT></A><FONT SIZE="-2">へお願いします。<BR>
         このコンテンツの商用利用ならびに無断転載はお断りいたします。この鑑定は無料です。<BR>
         <I>CopyRight. K.Yamamoto. 1998.9.1</I></FONT></P></CENTER>
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
