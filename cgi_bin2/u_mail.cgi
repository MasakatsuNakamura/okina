#!/usr/local/bin/perl
$|=1;
########################
$sendmail = "/usr/lib/sendmail";
$youraddress = 'okina@e-mail.ne.jp';
########################
require "cgi-lib.pl";
require "jcode.pl";
require "zenhan.pl";
&ReadParse;
######データの取り込み#######
$member = $in{'member'};
$KMEI = $in{'name'};
$KMAIL = $in{'email'};
$order1 = $in{'order1'};
$order2 = $in{'order2'};
$order3 = $in{'order3'};
$SPOST = $in{'zipcord'};
$SADR = $in{'address'};
$STEL = $in{'tel'};
$SMEI = $in{'fullname'};
$familyname = $in{'familyname'};
$brthday = $in{'brthday'};
$user = $in{'user'};
$brother = $in{'brother'};
$request = $in{'request'};

######入力されたデータのチェック######
if ($member =~ /^\s*$/) {
	&CgiError("NET-U会員番号が入力されていません。",
	"ブラウザの「Back」ボタンで戻って再入力してください。");
	exit;
}
if ($KMEI =~ /^\s*$/) {
	&CgiError("お客様のお名前の記入がありません。",
	"ブラウザの「Back」ボタンで戻って再入力してください。");
	exit;
}
if (($order1 eq "" ) and ($order2 eq "" ) and ($order3 eq ""))  {
	&CgiError("入力エラー",
		"ご注文が何も指示されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
	exit;
}	
if ($order2 ne "") {
	if ($SPOST eq "") {
		&CgiError("郵便番号が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
	elsif ($SADR eq "") {
		&CgiError("住所が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}	
	elsif ($SMEI eq "") {
		&CgiError("受取人が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
}
if ($order3 ne "") {
	if ($familyname eq "") {
		&CgiError("苗字(姓)が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
	elsif ($brthday eq "") {
		&CgiError("予定日(誕生日)が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
}

######メールアドレスのチェック######
if ($KMAIL =~ /^\s*$/){
	&CgiError("メールアドレスの記入がありません。",
	"ブラウザの「Back」ボタンで戻って再入力してください。");
	exit;
}
elsif (($KMAIL) and (not $KMAIL =~ /.+\@.+\..+/)) {
	&CgiError("入力エラー",
		"メールアドレスの書き方が間違っています。",$KMAIL,
		"ブラウザの「Back」ボタンで戻って再入力してください。");
	exit;
}
elsif (($hostname = $KMAIL) =~ s/.+\@(\S+)/$1/) {
	($hname,$aliases,$addresstype, $length,@address) =
		gethostbyname $hostname;
	if (not $hname) {
		&CgiError("メールホストエラー",
		"メールアドレスが確認できませんでした。");
		exit;
	}
}

######入力データの整形処理######
$member =~ s/\s*//g;
if ($SPOST ne "") {
	$SPOST =~ s/\s*//g;
	#全角英数字をすべて半角英数字にする。
	$SPOST = &zen2han($SPOST); 
	#郵便番号が7桁以下で入力された場合、00を末尾に付加する。
	$SPOST = $SPOST . "00000000";
	$SPOST = substr($SPOST, 0, 8);
}
if ($STEL ne "") {
	$STEL =~ s/\s*//g;
	#全角英数字をすべて半角英数字にする。
	$STEL = &zen2han($STEL); 
}
if ($familyname ne "") {
	$familyname =~ s/\s*//g;
}
if ($brthday ne "") {
	$brthday =~ s/\s*//g;
}

######Pレジ受付番号の生成######
$countfile = "count.txt";
open COUNTER,"$countfile"
	or &CgiError("$countfile オープン失敗1\n");
$SJNO = <COUNTER>;
close COUNTER;

++$SJNO;

open COUNTER,">$countfile"
	or &CgiError("$countfile オープン失敗2\n");
print COUNTER $SJNO;
close COUNTER;

######翁へのご注文メールの送信######
$com = <<MESSAGE;
From: $KMAIL
Subject: 山本翁へのご注文(NET-U会員)

=====================================
Ｐレジ受付番号：
$SJNO
申込人様の氏名：
$KMEI
申込人様のEメールアドレス：
$KMAIL
ご注文内容：
$order1
$order2
$order3

書籍の送付先または連絡先
郵便番号：
$SPOST
ご住所：
$SADR
お電話番号：
$STEL
受取人様：
$SMEI

命名のご依頼内容
姓(みょうじ)：
$familyname
出産予定日：
$brthday
今までの利用：
$user
兄姉のお名前：
$brother
ご要望事項：
$request

=====================================
MESSAGE

&jcode'convert(*com,"jis");
open(MAIL, "|$sendmail $youraddress");
print MAIL $com;
close(MAIL);

######ここから引き継ぎ情報の生成と表示画面######
######電子本、書籍、命名の3つを注文#######
if (($order1 ne "") and ($order2 ne "") and ($order3 ne ""))  {
	$msg = <<"ORDER123";
Content-type: text/html

<HTML>
<HEAD>
   <TITLE>電子本と書籍のご注文・命名のご依頼</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=x-sjis">
</HEAD>
<BODY BGCOLOR="#FFFFFF" BACKGROUND="/~kazu-y/image/wall.jpg">
<P><TABLE BORDER=0 CELLSPACING=0 CELLPADDING=0 WIDTH=640>
   <TR>
      <TD>
         <CENTER><FONT SIZE="+3"><B><U>ご注文有難うございます。</U></B></FONT>
         
         <P><FONT COLOR="#FF0000"><B>引き続きNET-Uカードの決済を行っていただきます。</B></FONT></P>
         
         <P>ご注文内容のご確認<BR>
         <TABLE BORDER=1 WIDTH="80%">
            <TR>
               <TD>
                  <CENTER>ご注文内容</CENTER>
               </TD>
               <TD>
                  <CENTER>代金(消費税込み)</CENTER>
               </TD>
               <TD>
                  <CENTER>備考</CENTER>
               </TD>
            </TR>
            <TR>
               <TD>
                  <P>1.「山本翁の電子本」を購入</P>
               </TD>
               <TD>
                  <P ALIGN=right>500円</P>
               </TD>
               <TD>
                  <P ALIGN=right>パスワード代金</P>
               </TD>
            </TR>
            <TR>
               <TD>
                  <P>2.「山本翁の著書」を購入</P>
               </TD>
               <TD>
                  <P ALIGN=right>1,810円</P>
               </TD>
               <TD>
                  <P ALIGN=right>送料310円込み</P>
               </TD>
            </TR>
            <TR>
               <TD>
                  <P>3.「新生児の命名」を依頼</P>
               </TD>
               <TD>
                  <P ALIGN=right>10,000円</P>
               </TD>
               <TD>
                  <P></P>
               </TD>
            </TR>
            <TR>
               <TD>
                  <P ALIGN=right>合計購入金額</P>
               </TD>
               <TD>
                  <P ALIGN=right>12,310円</P>
               </TD>
               <TD>
                  <P></P>
               </TD>
            </TR>
         </TABLE>
         
         <B>ご確認が済みましたら</B><FONT COLOR="#FF0000"><B>下記「送信」ボタンを1回だけ押して</B></FONT><B>ください。<BR>
         しばらくお待ち頂ければ、NET-Uカードの決済画面に変わります。</B></P>
         
         <P>ご注文の訂正は、ブラウザの「戻る」で「入力フォーム」からやり直して下さい。</P>
         
         <P><FORM ACTION="http://p-reg.u-card.co.jp/cgi-bin/junbi.cgi" METHOD=POST>
            <P><INPUT TYPE=hidden NAME="SID" VALUE=P0000161>
            <INPUT TYPE="hidden" NAME="SJNO" VALUE="\$SJNO">
            <INPUT TYPE="hidden" NAME="KGAK" VALUE="12310">
            <INPUT TYPE="hidden" NAME="SSUU" VALUE="3">
            <INPUT TYPE="hidden" NAME="ZEIGAK" VALUE="0">
            <INPUT TYPE="hidden" NAME="ICD1" VALUE="EBOK">
            <INPUT TYPE="hidden" NAME="ISUU1" VALUE="1">
            <INPUT TYPE="hidden" NAME="ICD2" VALUE="RBOK">
            <INPUT TYPE="hidden" NAME="ISUU2" VALUE="1">
            <INPUT TYPE="hidden" NAME="ICD3" VALUE="BABY">
            <INPUT TYPE="hidden" NAME="ISUU3" VALUE="1">
            <INPUT TYPE="hidden" NAME="KMEI" VALUE="\$KMEI">
            <INPUT TYPE="hidden" NAME="KMAIL" VALUE="\$KMAIL">
            <INPUT TYPE="hidden" NAME="SMEI" VALUE="\$SMEI">
            <INPUT TYPE="hidden" NAME="SPOST" VALUE="\$SPOST">
            <INPUT TYPE="hidden" NAME="SADR" VALUE="\$SADR">
            <INPUT TYPE="hidden" NAME="STEL" VALUE="\$STEL"></P>
            <CENTER><INPUT TYPE=submit NAME="送信" VALUE="送信"></CENTER>
         </FORM></P></CENTER>
      </TD>
   </TR>
</TABLE>
</P>
</BODY>
</HTML>

ORDER123
&jcode'convert(*msg, "sjis", "euc");
	$msg =~ s/\$KMEI/$KMEI/g;
	$msg =~ s/\$KMAIL/$KMAIL/g;
	$msg =~ s/\$order1/$order1/g;	
	$msg =~ s/\$order2/$order2/g;	
	$msg =~ s/\$order3/$order3/g;
	$msg =~ s/\$SPOST/$SPOST/g;
	$msg =~ s/\$SADR/$SADR/g;
	$msg =~ s/\$STEL/$STEL/g;
	$msg =~ s/\$SMEI/$SMEI/g;
	$msg =~ s/\$SJNO/$SJNO/g;
	print $msg;
}
#######電子本と書籍を注文##########
elsif (($order1 ne "") and ($order2 ne ""))  {
	$msg = <<"ORDER120";
Content-type: text/html

<HTML>
<HEAD>
   <TITLE>電子本と書籍のご注文</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=x-sjis">
</HEAD>
<BODY BGCOLOR="#FFFFFF" BACKGROUND="/~kazu-y/image/wall.jpg">
<P><TABLE BORDER=0 CELLSPACING=0 CELLPADDING=0 WIDTH=640>
   <TR>
      <TD>
         <CENTER><FONT SIZE="+3"><B><U>ご注文有難うございます。</U></B></FONT>
         
         <P><FONT COLOR="#FF0000"><B>引き続きNET-Uカードの決済を行っていただきます。</B></FONT></P>
         
         <P>ご注文内容のご確認<BR>
         <TABLE BORDER=1 WIDTH="80%">
            <TR>
               <TD>
                  <CENTER>ご注文内容</CENTER>
               </TD>
               <TD>
                  <CENTER>代金(消費税込み)</CENTER>
               </TD>
               <TD>
                  <CENTER>備考</CENTER>
               </TD>
            </TR>
            <TR>
               <TD>
                  <P>1.「山本翁の電子本」を購入</P>
               </TD>
               <TD>
                  <P ALIGN=right>500円</P>
               </TD>
               <TD>
                  <P ALIGN=right>パスワード代金</P>
               </TD>
            </TR>
            <TR>
               <TD>
                  <P>2.「山本翁の著書」を購入</P>
               </TD>
               <TD>
                  <P ALIGN=right>1,810円</P>
               </TD>
               <TD>
                  <P ALIGN=right>送料310円込み</P>
               </TD>
            </TR>
            <TR>
               <TD>
                  <P ALIGN=right>合計購入金額</P>
               </TD>
               <TD>
                  <P ALIGN=right>2,310円</P>
               </TD>
               <TD>
                  <P></P>
               </TD>
            </TR>
         </TABLE>
         
         <B>ご確認が済みましたら</B><FONT COLOR="#FF0000"><B>下記「送信」ボタンを1回だけ押して</B></FONT><B>ください。<BR>
         しばらくお待ち頂ければ、NET-Uカードの決済画面に変わります。</B></P>
         
         <P>ご注文の訂正は、ブラウザの「戻る」で「入力フォーム」からやり直して下さい。</P>
         
         <P><FORM ACTION="http://p-reg.u-card.co.jp/cgi-bin/junbi.cgi" METHOD=POST>
            <P><INPUT TYPE="hidden" NAME="SID" VALUE="P0000161">
            <INPUT TYPE="hidden" NAME="SJNO" VALUE="\$SJNO">
            <INPUT TYPE="hidden" NAME="KGAK" VALUE="2310">
            <INPUT TYPE="hidden" NAME="SSUU" VALUE="2">
            <INPUT TYPE="hidden" NAME="ZEIGAK" VALUE="0">
            <INPUT TYPE="hidden" NAME="ICD1" VALUE="EBOK">
            <INPUT TYPE="hidden" NAME="ISUU1" VALUE="1">
            <INPUT TYPE="hidden" NAME="ICD2" VALUE="RBOK">
            <INPUT TYPE="hidden" NAME="ISUU2" VALUE="1">
            <INPUT TYPE="hidden" NAME="KMEI" VALUE="\$KMEI">
            <INPUT TYPE="hidden" NAME="KMAIL" VALUE="\$KMAIL">
            <INPUT TYPE="hidden" NAME="SMEI" VALUE="\$SMEI">
            <INPUT TYPE="hidden" NAME="SPOST" VALUE="\$SPOST">
            <INPUT TYPE="hidden" NAME="SADR" VALUE="\$SADR">
            <INPUT TYPE="hidden" NAME="STEL" VALUE="\$STEL"></P>
            
            <CENTER><INPUT TYPE=submit NAME="送信" VALUE="送信"></CENTER>
         </FORM></P></CENTER>
      </TD>
   </TR>
</TABLE>
</P>
</BODY>
</HTML>

ORDER120
&jcode'convert(*msg, "sjis", "euc");
	$msg =~ s/\$KMEI/$KMEI/g;
	$msg =~ s/\$KMAIL/$KMAIL/g;
	$msg =~ s/\$order1/$order1/g;	
	$msg =~ s/\$order2/$order2/g;	
	$msg =~ s/\$SPOST/$SPOST/g;
	$msg =~ s/\$SADR/$SADR/g;
	$msg =~ s/\$STEL/$STEL/g;
	$msg =~ s/\$SMEI/$SMEI/g;
	$msg =~ s/\$SJNO/$SJNO/g;
	print $msg;
}
########電子本の注文と命名の依頼###########
elsif (($order1 ne "") and ($order3 ne ""))  {
	$msg = <<"ORDER103";
Content-type: text/html

<HTML>
<HEAD>
   <TITLE>電子本のご注文・命名のご依頼</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=x-sjis">
</HEAD>
<BODY BGCOLOR="#FFFFFF" BACKGROUND="/~kazu-y/image/wall.jpg">
<P><TABLE BORDER=0 CELLSPACING=0 CELLPADDING=0 WIDTH=640>
   <TR>
      <TD>
         <CENTER><FONT SIZE="+3"><B><U>ご注文有難うございます。</U></B></FONT>
         
         <P><FONT COLOR="#FF0000"><B>引き続きNET-Uカードの決済を行っていただきます。</B></FONT></P>
         
         <P>ご注文内容のご確認<BR>
         <TABLE BORDER=1 WIDTH="80%">
            <TR>
               <TD>
                  <CENTER>ご注文内容</CENTER>
               </TD>
               <TD>
                  <CENTER>代金(消費税込み)</CENTER>
               </TD>
               <TD>
                  <CENTER>備考</CENTER>
               </TD>
            </TR>
            <TR>
               <TD>
                  <P>1.「山本翁の電子本」を購入</P>
               </TD>
               <TD>
                  <P ALIGN=right>500円</P>
               </TD>
               <TD>
                  <P ALIGN=right>パスワード代金</P>
               </TD>
            </TR>
            <TR>
               <TD>
                  <P>2.「新生児の命名」を依頼</P>
               </TD>
               <TD>
                  <P ALIGN=right>10,000円</P>
               </TD>
               <TD>
                  <P></P>
               </TD>
            </TR>
            <TR>
               <TD>
                  <P ALIGN=right>合計購入金額</P>
               </TD>
               <TD>
                  <P ALIGN=right>10,500円</P>
               </TD>
               <TD>
                  <P></P>
               </TD>
            </TR>
         </TABLE>
         
         <B>ご確認が済みましたら</B><FONT COLOR="#FF0000"><B>下記「送信」ボタンを1回だけ押して</B></FONT><B>ください。<BR>
         しばらくお待ち頂ければ、NET-Uカードの決済画面に変わります。</B></P>
         
         <P>ご注文の訂正は、ブラウザの「戻る」で「入力フォーム」からやり直して下さい。</P>
         
         <P><FORM ACTION="http://p-reg.u-card.co.jp/cgi-bin/junbi.cgi" METHOD=POST>
            <P><INPUT TYPE="hidden" NAME="SID" VALUE="P0000161">
            <INPUT TYPE="hidden" NAME="SJNO" VALUE="\$SJNO">
            <INPUT TYPE="hidden" NAME="KGAK" VALUE="10500">
            <INPUT TYPE="hidden" NAME="SSUU" VALUE="2">
            <INPUT TYPE="hidden" NAME="ZEIGAK" VALUE="0">
            <INPUT TYPE="hidden" NAME="ICD1" VALUE="EBOK">
            <INPUT TYPE="hidden" NAME="ISUU1" VALUE="1">
            <INPUT TYPE="hidden" NAME="ICD2" VALUE="BABY">
            <INPUT TYPE="hidden" NAME="ISUU2" VALUE="1">
            <INPUT TYPE="hidden" NAME="KMEI" VALUE="\$KMEI">
            <INPUT TYPE="hidden" NAME="KMAIL" VALUE="\$KMAIL"></P>
            <CENTER><INPUT TYPE=submit NAME="送信" VALUE="送信"></CENTER>
         </FORM></P></CENTER>
      </TD>
   </TR>
</TABLE>
</P>
</BODY>
</HTML>

ORDER103
&jcode'convert(*msg, "sjis", "euc");
	$msg =~ s/\$KMEI/$KMEI/g;
	$msg =~ s/\$KMAIL/$KMAIL/g;
	$msg =~ s/\$order1/$order1/g;		
	$msg =~ s/\$order3/$order3/g;
	$msg =~ s/\$SPOST/$SPOST/g;
	$msg =~ s/\$SADR/$SADR/g;
	$msg =~ s/\$STEL/$STEL/g;
	$msg =~ s/\$SMEI/$SMEI/g;
	$msg =~ s/\$SJNO/$SJNO/g;
	print $msg;
}
########書籍の注文と命名の依頼###########
elsif (($order2 ne "") and ($order3 ne ""))  {
	$msg = <<"ORDER023";
Content-type: text/html

<HTML>
<HEAD>
   <TITLE>書籍のご注文・命名のご依頼</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=x-sjis">
</HEAD>
<BODY BGCOLOR="#FFFFFF" BACKGROUND="/~kazu-y/image/wall.jpg">
<P><TABLE BORDER=0 CELLSPACING=0 CELLPADDING=0 WIDTH=640>
   <TR>
      <TD>
         <CENTER><FONT SIZE="+3"><B><U>ご注文有難うございます。</U></B></FONT>
         
         <P><FONT COLOR="#FF0000"><B>引き続きNET-Uカードの決済を行っていただきます。</B></FONT></P>
         
         <P>ご注文内容のご確認<BR>
         <TABLE BORDER=1 WIDTH="80%">
            <TR>
               <TD>
                  <CENTER>ご注文内容</CENTER>
               </TD>
               <TD>
                  <CENTER>代金(消費税込み)</CENTER>
               </TD>
               <TD>
                  <CENTER>備考</CENTER>
               </TD>
            </TR>
            <TR>
               <TD>
                  <P>1.「山本翁の著書」を購入</P>
               </TD>
               <TD>
                  <P ALIGN=right>1,810円</P>
               </TD>
               <TD>
                  <P ALIGN=right>送料310円込み</P>
               </TD>
            </TR>
            <TR>
               <TD>
                  <P>2.「新生児の命名」を依頼</P>
               </TD>
               <TD>
                  <P ALIGN=right>10,000円</P>
               </TD>
               <TD>
                  <P></P>
               </TD>
            </TR>
            <TR>
               <TD>
                  <P ALIGN=right>合計購入金額</P>
               </TD>
               <TD>
                  <P ALIGN=right>11,810円</P>
               </TD>
               <TD>
                  <P></P>
               </TD>
            </TR>
         </TABLE>
         
         <B>ご確認が済みましたら</B><FONT COLOR="#FF0000"><B>下記「送信」ボタンを1回だけ押して</B></FONT><B>ください。<BR>
         しばらくお待ち頂ければ、NET-Uカードの決済画面に変わります。</B></P>
         
         <P>ご注文の訂正は、ブラウザの「戻る」で「入力フォーム」からやり直して下さい。</P>
         
         <P><FORM ACTION="http://p-reg.u-card.co.jp/cgi-bin/junbi.cgi" METHOD=POST>
            <P><INPUT TYPE="hidden" NAME="SID" VALUE="P0000161">
            <INPUT TYPE="hidden" NAME="SJNO" VALUE="\$SJNO">
            <INPUT TYPE="hidden" NAME="KGAK" VALUE="11810">
            <INPUT TYPE="hidden" NAME="ZEIGAK" VALUE="0">
            <INPUT TYPE="hidden" NAME="SSUU" VALUE="2">
            <INPUT TYPE="hidden" NAME="ICD1" VALUE="RBOK">
            <INPUT TYPE="hidden" NAME="ISUU1" VALUE="1">
            <INPUT TYPE="hidden" NAME="ICD2" VALUE="BABY">
            <INPUT TYPE="hidden" NAME="ISUU2" VALUE="1">
            <INPUT TYPE="hidden" NAME="KMEI" VALUE="\$KMEI">
            <INPUT TYPE="hidden" NAME="KMAIL" VALUE="\$KMAIL">
            <INPUT TYPE="hidden" NAME="SMEI" VALUE="\$SMEI">
            <INPUT TYPE="hidden" NAME="SPOST" VALUE="\$SPOST">
            <INPUT TYPE="hidden" NAME="SADR" VALUE="\$SADR">
            <INPUT TYPE="hidden" NAME="STEL" VALUE="\$STEL"></P>
            <CENTER><INPUT TYPE=submit NAME="送信" VALUE="送信"></CENTER>
         </FORM></P></CENTER>
      </TD>
   </TR>
</TABLE>
</P>
</BODY>
</HTML>

ORDER023
&jcode'convert(*msg, "sjis", "euc");
	$msg =~ s/\$KMEI/$KMEI/g;
	$msg =~ s/\$KMAIL/$KMAIL/g;	
	$msg =~ s/\$order2/$order2/g;	
	$msg =~ s/\$order3/$order3/g;
	$msg =~ s/\$SPOST/$SPOST/g;
	$msg =~ s/\$SADR/$SADR/g;
	$msg =~ s/\$STEL/$STEL/g;
	$msg =~ s/\$SMEI/$SMEI/g;
	$msg =~ s/\$SJNO/$SJNO/g;
	print $msg;
}
############電子本のみ注文###########
elsif ($order1 ne "")  {
	$msg = <<"ORDER100";
Content-type: text/html

<HTML>
<HEAD>
   <TITLE>電子本のご注文</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=x-sjis">
</HEAD>
<BODY BGCOLOR="#FFFFFF" BACKGROUND="/~kazu-y/image/wall.jpg">
<P><TABLE BORDER=0 CELLSPACING=0 CELLPADDING=0 WIDTH=640>
   <TR>
      <TD>
         <CENTER><FONT SIZE="+3"><B><U>ご注文有難うございます。</U></B></FONT>
         
         <P><FONT COLOR="#FF0000"><B>引き続きNET-Uカードの決済を行っていただきます。</B></FONT></P>
         
         <P>ご注文内容のご確認<BR>
         <TABLE BORDER=1 WIDTH="80%">
            <TR>
               <TD>
                  <CENTER>ご注文内容</CENTER>
               </TD>
               <TD>
                  <CENTER>代金(消費税込み)</CENTER>
               </TD>
               <TD>
                  <CENTER>備考</CENTER>
               </TD>
            </TR>
            <TR>
               <TD>
                  <P>1.「山本翁の電子本」を購入</P>
               </TD>
               <TD>
                  <P ALIGN=right>500円</P>
               </TD>
               <TD>
                  <P ALIGN=right>パスワード代金</P>
               </TD>
            </TR>
            <TR>
               <TD>
                  <P ALIGN=right>合計購入金額</P>
               </TD>
               <TD>
                  <P ALIGN=right>500円</P>
               </TD>
               <TD>
                  <P></P>
               </TD>
            </TR>
         </TABLE>
         
         <B>ご確認が済みましたら</B><FONT COLOR="#FF0000"><B>下記「送信」ボタンを1回だけ押して</B></FONT><B>ください。<BR>
         しばらくお待ち頂ければ、NET-Uカードの決済画面に変わります。</B></P>
         
         <P>ご注文の訂正は、ブラウザの「戻る」で「入力フォーム」からやり直して下さい。</P>
         
         <P><FORM ACTION="http://p-reg.u-card.co.jp/cgi-bin/junbi.cgi" METHOD=POST>
            <P><INPUT TYPE="hidden" NAME="SID" VALUE="P0000161">
            <INPUT TYPE="hidden" NAME="SJNO" VALUE="\$SJNO">
            <INPUT TYPE="hidden" NAME="KGAK" VALUE="500">
            <INPUT TYPE="hidden" NAME="ZEIGAK" VALUE="0">
            <INPUT TYPE="hidden" NAME="SSUU" VALUE="1">
            <INPUT TYPE="hidden" NAME="ICD1" VALUE="EBOK">
            <INPUT TYPE="hidden" NAME="ISUU1" VALUE="1">
            <INPUT TYPE="hidden" NAME="KMEI" VALUE="\$KMEI">
            <INPUT TYPE="hidden" NAME="KMAIL" VALUE="\$KMAIL"></P>
            <CENTER><INPUT TYPE=submit NAME="送信" VALUE="送信"></CENTER>
         </FORM></P></CENTER>
      </TD>
   </TR>
</TABLE>
</P>
</BODY>
</HTML>

ORDER100
&jcode'convert(*msg, "sjis", "euc");
	$msg =~ s/\$KMEI/$KMEI/g;
	$msg =~ s/\$KMAIL/$KMAIL/g;
	$msg =~ s/\$order1/$order1/g;	
	$msg =~ s/\$SPOST/$SPOST/g;
	$msg =~ s/\$SADR/$SADR/g;
	$msg =~ s/\$STEL/$STEL/g;
	$msg =~ s/\$SMEI/$SMEI/g;
	$msg =~ s/\$SJNO/$SJNO/g;
	print $msg;
}
#########書籍のみ注文##########
elsif ($order2 ne "")  {
	$msg = <<"ORDER020";
Content-type: text/html

<HTML>
<HEAD>
   <TITLE>書籍のご注文</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=x-sjis">
</HEAD>
<BODY BGCOLOR="#FFFFFF" BACKGROUND="/~kazu-y/image/wall.jpg">
<P><TABLE BORDER=0 CELLSPACING=0 CELLPADDING=0 WIDTH=640>
   <TR>
      <TD>
         <CENTER><FONT SIZE="+3"><B><U>ご注文有難うございます。</U></B></FONT>
         
         <P><FONT COLOR="#FF0000"><B>引き続きNET-Uカードの決済を行っていただきます。</B></FONT></P>
         
         <P>ご注文内容のご確認<BR>
         <TABLE BORDER=1 WIDTH="80%">
            <TR>
               <TD>
                  <CENTER>ご注文内容</CENTER>
               </TD>
               <TD>
                  <CENTER>代金(消費税込み)</CENTER>
               </TD>
               <TD>
                  <CENTER>備考</CENTER>
               </TD>
            </TR>
            <TR>
               <TD>
                  <P>1.「山本翁の著書」を購入</P>
               </TD>
               <TD>
                  <P ALIGN=right>1,810円</P>
               </TD>
               <TD>
                  <P ALIGN=right>送料310円込み</P>
               </TD>
            </TR>
            <TR>
               <TD>
                  <P ALIGN=right>合計購入金額</P>
               </TD>
               <TD>
                  <P ALIGN=right>1,810円</P>
               </TD>
               <TD>
                  <P></P>
               </TD>
            </TR>
         </TABLE>
         
         <B>ご確認が済みましたら</B><FONT COLOR="#FF0000"><B>下記「送信」ボタンを1回だけ押して</B></FONT><B>ください。<BR>
         しばらくお待ち頂ければ、NET-Uカードの決済画面に変わります。</B></P>
         
         <P>ご注文の訂正は、ブラウザの「戻る」で「入力フォーム」からやり直して下さい。</P>
         
         <P><FORM ACTION="http://p-reg.u-card.co.jp/cgi-bin/junbi.cgi" METHOD=POST>
            <P><INPUT TYPE="hidden" NAME="SID" VALUE="P0000161">
            <INPUT TYPE="hidden" NAME="SJNO" VALUE="\$SJNO">
            <INPUT TYPE="hidden" NAME="KGAK" VALUE="1810">
            <INPUT TYPE="hidden" NAME="ZEIGAK" VALUE="0">
            <INPUT TYPE="hidden" NAME="SSUU" VALUE="1">
            <INPUT TYPE="hidden" NAME="ICD1" VALUE="RBOK">
            <INPUT TYPE="hidden" NAME="ISUU1" VALUE="1">
            <INPUT TYPE="hidden" NAME="KMEI" VALUE="\$KMEI">
            <INPUT TYPE="hidden" NAME="KMAIL" VALUE="\$KMAIL">
            <INPUT TYPE="hidden" NAME="SMEI" VALUE="\$SMEI">
            <INPUT TYPE="hidden" NAME="SPOST" VALUE="\$SPOST">
            <INPUT TYPE="hidden" NAME="SADR" VALUE="\$SADR">
            <INPUT TYPE="hidden" NAME="STEL" VALUE="\$STEL"></P>
            <CENTER><INPUT TYPE=submit NAME="送信" VALUE="送信"></CENTER>
         </FORM></P></CENTER>
      </TD>
   </TR>
</TABLE>
</P>
</BODY>
</HTML>

ORDER020
&jcode'convert(*msg, "sjis", "euc");
	$msg =~ s/\$KMEI/$KMEI/g;
	$msg =~ s/\$KMAIL/$KMAIL/g;
	$msg =~ s/\$order2/$order2/g;	
	$msg =~ s/\$SPOST/$SPOST/g;
	$msg =~ s/\$SADR/$SADR/g;
	$msg =~ s/\$STEL/$STEL/g;
	$msg =~ s/\$SMEI/$SMEI/g;
	$msg =~ s/\$SJNO/$SJNO/g;
	print $msg;
}
elsif ($order3 ne "")  {
#命名のみ依頼
	$msg = <<"ORDER003";
Content-type: text/html

<HTML>
<HEAD>
   <TITLE>命名のご依頼</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=x-sjis">
</HEAD>
<BODY BGCOLOR="#FFFFFF" BACKGROUND="/~kazu-y/image/wall.jpg">
<P><TABLE BORDER=0 CELLSPACING=0 CELLPADDING=0 WIDTH=640>
   <TR>
      <TD>
         <CENTER><FONT SIZE="+3"><B><U>ご注文有難うございます。</U></B></FONT>
         
         <P><FONT COLOR="#FF0000"><B>引き続きNET-Uカードの決済を行っていただきます。</B></FONT></P>
         
         <P>ご注文内容のご確認<BR>
         <TABLE BORDER=1 WIDTH="80%">
            <TR>
               <TD>
                  <CENTER>ご注文内容</CENTER>
               </TD>
               <TD>
                  <CENTER>代金(消費税込み)</CENTER>
               </TD>
               <TD>
                  <CENTER>備考</CENTER>
               </TD>
            </TR>
            <TR>
               <TD>
                  <P>1.「新生児の命名」を依頼</P>
               </TD>
               <TD>
                  <P ALIGN=right>10,000円</P>
               </TD>
               <TD>
                  <P></P>
               </TD>
            </TR>
            <TR>
               <TD>
                  <P ALIGN=right>合計購入金額</P>
               </TD>
               <TD>
                  <P ALIGN=right>10,000円</P>
               </TD>
               <TD>
                  <P></P>
               </TD>
            </TR>
         </TABLE>
         
         <B>ご確認が済みましたら</B><FONT COLOR="#FF0000"><B>下記「送信」ボタンを1回だけ押して</B></FONT><B>ください。<BR>
         しばらくお待ち頂ければ、NET-Uカードの決済画面に変わります。</B></P>
         
         <P>ご注文の訂正は、ブラウザの「戻る」で「入力フォーム」からやり直して下さい。</P>
         
         <P><FORM ACTION="http://p-reg.u-card.co.jp/cgi-bin/junbi.cgi" METHOD=POST>
            <P><INPUT TYPE="hidden" NAME="SID" VALUE="P0000161">
            <INPUT TYPE="hidden" NAME="SJNO" VALUE="\$SJNO">
            <INPUT TYPE="hidden" NAME="KGAK" VALUE="10000">
            <INPUT TYPE="hidden" NAME="ZEIGAK" VALUE="0">
            <INPUT TYPE="hidden" NAME="SSUU" VALUE="1">
            <INPUT TYPE="hidden" NAME="ICD1" VALUE="BABY">
            <INPUT TYPE="hidden" NAME="ISUU1" VALUE="1">
            <INPUT TYPE="hidden" NAME="KMEI" VALUE="\$KMEI">
            <INPUT TYPE="hidden" NAME="KMAIL" VALUE="\$KMAIL"></P>
            <CENTER><INPUT TYPE=submit NAME="送信" VALUE="送信"></CENTER>
         </FORM></P></CENTER>
      </TD>
   </TR>
</TABLE>
</P>
</BODY>
</HTML>

ORDER003
&jcode'convert(*msg, "sjis", "euc");
	$msg =~ s/\$KMEI/$KMEI/g;
	$msg =~ s/\$KMAIL/$KMAIL/g;	
	$msg =~ s/\$order3/$order3/g;
	$msg =~ s/\$SPOST/$SPOST/g;
	$msg =~ s/\$SADR/$SADR/g;
	$msg =~ s/\$STEL/$STEL/g;
	$msg =~ s/\$SMEI/$SMEI/g;
	$msg =~ s/\$SJNO/$SJNO/g;
	print $msg;
}
__end__
