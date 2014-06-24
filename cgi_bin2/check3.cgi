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
$order4 = $in{'order4'};
$familyname1 = $in{'familyname1'};
$firstname1 = $in{'firstname1'};
$birthday1= $in{'birthday1'};
$sex1 = $in{'sex1'};
$trade1 = $in{'trade1'};
$request1 = $in{'request1'};
$order6 = $in{'order6'};
$familyname3 = $in{'familyname3'};
$firstname3 = $in{'firstname3'};
$birthday3= $in{'birthday3'};
$sex3 = $in{'sex3'};
$trade3 = $in{'trade3'};
$familyname4 = $in{'familyname4'};
$firstname4 = $in{'firstname4'};
$birthday4= $in{'birthday4'};
$sex4 = $in{'sex4'};
$trade4 = $in{'trade4'};
$sei = $in{'sei'};
$request3 = $in{'request3'};
######入力データの整形処理######
if ($familyname1 ne "") {
	$familyname1 =~ s/\s*//g;
}
if ($familyname3 ne "") {
	$familyname3 =~ s/\s*//g;
}
if ($familyname4 ne "") {
	$familyname4 =~ s/\s*//g;
}
if ($firstname1 ne "") {
	$familyname1 =~ s/\s*//g;
}
if ($firstname3 ne "") {
	$familyname3 =~ s/\s*//g;
}
if ($firstname4 ne "") {
	$familyname4 =~ s/\s*//g;
}
if ($birthday1 ne "") {
	$birthday1 =~ s/\s*//g;
}
if ($birthday3 ne "") {
	$birthday3 =~ s/\s*//g;
}
if ($birthday4 ne "") {
	$birthday4 =~ s/\s*//g;
}
if ($email ne "") {
	$email =~ s/\s*//g;
	#全角英数字をすべて半角英数字にする。
	$email = &zen2han($email);
}
#####入力エラーのチェック#####
if ($name =~ /^\s*$/){
	&CgiError("名前の記入がありません。",
	"ブラウザの「Back」ボタンで戻って再入力してください。");
	exit;
}
if ($email =~ /^\s*$/){
	&CgiError("メールアドレスの記入がありません。",
	"ブラウザの「Back」ボタンで戻って再入力してください。");
	exit;
}
elsif (($email) and (not $email =~ /.+\@.+\..+/)) {
	&CgiError("入力エラー",
		"メールアドレスの書き方が間違っています。",$email,
		"ブラウザの「Back」ボタンで戻って再入力してください。");
	exit;
}
if (($order4 eq "" ) and ($order6 eq "") )  {
	&CgiError("入力エラー",
		"ご依頼事項が何も指示されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
	exit;
}
if ($order4 ne "") {
	if ($familyname1 eq "") {
		&CgiError("姓が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
	elsif ($firstname1 eq "") {
		&CgiError("名が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
	elsif ($birthday1 eq "") {
		&CgiError("生年月日が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
    elsif ($sex1 eq "") {
		&CgiError("性別が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
    elsif ($trade1 eq "") {
		&CgiError("業種・ご職業が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
   elsif ($request1 eq "") {
		&CgiError("ご依頼内容の詳細が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
}
if ($order6 ne "") {
	if ($familyname3 eq "") {
		&CgiError("依頼者側の姓が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
   elsif ($firstname3 eq "") {
		&CgiError("依頼者側の名が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
   elsif ($birthday3 eq "") {
		&CgiError("依頼者側の生年月日が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
   elsif ($sex3 eq "") {
		&CgiError("依頼者側の性別が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
   elsif ($trade3 eq "") {
		&CgiError("依頼者側のご職業が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
   elsif ($familyname4 eq "") {
		&CgiError("相手側の姓が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
   elsif ($firstname4 eq "") {
		&CgiError("相手側の名が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
   elsif ($birthday4 eq "") {
		&CgiError("相手側の生年月日が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
   elsif ($sex4 eq "") {
		&CgiError("相手側の性別が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
   elsif ($trade4 eq "") {
		&CgiError("相手側のご職業が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
   elsif ($sei eq "") {
		&CgiError("ご結婚後の姓が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
}
######ここから引き継ぎ情報の生成と表示画面######
$msg = <<"ORDER";
Content-type: text/html

<HTML>
<HEAD>
   <TITLE>翁へのご相談内容の確認</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=x-sjis">
</HEAD>
<BODY BGCOLOR="#FFFFFF" BACKGROUND="/~kazu-y/image/wall.jpg">
<P><TABLE BORDER=0 CELLSPACING=0 CELLPADDING=0 WIDTH=640>
   <TR>
      <TD>
         <CENTER><FONT SIZE="+3"><B><U>ご依頼内容のご確認</U></B></FONT></CENTER>
         <BLOCKQUOTE>この画面は、ご依頼内容をご確認頂くためのものです。内容に誤りがある場合は、ブラウザの「戻る」ボタンを押して「入力フォーム」から修正して下さい。これで宜しければ「依頼」ボタンを押して下さい。</BLOCKQUOTE>
         <CENTER><B>ご依頼内容</B><BR>
<TABLE BORDER=1 WIDTH="90%">
   <TR>
      <TD WIDTH=148>
         <P>ご依頼者(貴方)のお名前</P>
      </TD>
      <TD>
         <P>\$name</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>ご依頼者のメールアドレス</P>
      </TD>
      <TD>
         <P>\$email</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148 HEIGHT=6>
         <CENTER>ご依頼の内容</CENTER>
      </TD>
      <TD HEIGHT=6>
         <CENTER>ご依頼内容に関する詳細項目</CENTER>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>\$order4</P>
      </TD>
      <TD>
         <P>改名や選名を受けられる方の情報<BR>
         <TABLE BORDER=1>
            <TR>
               <TD WIDTH=105>
                  <P>姓(苗字)</P>
               </TD>
               <TD>
                  <P>\$familyname1</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=105>
                  <P>現在の名</P>
               </TD>
               <TD>
                  <P>\$firstname1</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=105>
                  <P>生年月日</P>
               </TD>
               <TD>
                  <P>\$birthday1</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=105>
                  <P>性別</P>
               </TD>
               <TD>
                  <P>\$sex1</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=105>
                  <P>ご職業(業種)</P>
               </TD>
               <TD>
                  <P>\$trade1</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=105>
                  <P>ご要望事項<BR>
                  (選名条件)</P>
               </TD>
               <TD>
                  <P>\$request1</P>
               </TD>
            </TR>
         </TABLE>
         </P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>\$order6</P>
      </TD>
      <TD>
         <P>結婚されるお二人の情報<BR>
         <TABLE BORDER=1>
            <TR>
               <TD WIDTH=105>
                  <P>依頼者の姓(苗字)</P>
               </TD>
               <TD>
                  <P>\$familyname3</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=105>
                  <P>依頼者の名</P>
               </TD>
               <TD>
                  <P>\$firstname3</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=105>
                  <P>依頼者の生年月日</P>
               </TD>
               <TD>
                  <P>\$birthday3</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=105>
                  <P>依頼者の性別</P>
               </TD>
               <TD>
                  <P>\$sex3</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=105>
                  <P>依頼者のご職業</P>
               </TD>
               <TD>
                  <P>\$trade3</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=105>
                  <P>相手方の姓(苗字)</P>
               </TD>
               <TD>
                  <P>\$familyname4</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=105>
                  <P>相手方の名</P>
               </TD>
               <TD>
                  <P>\$firstname4</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=105>
                  <P>相手方の生年月日</P>
               </TD>
               <TD>
                  <P>\$birthday4</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=105>
                  <P>相手方の性別</P>
               </TD>
               <TD>
                  <P>\$sex4</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=105>
                  <P>相手方のご職業</P>
               </TD>
               <TD>
                  <P>\$trade4</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=105>
                  <P>結婚後の姓(苗字)</P>
               </TD>
               <TD>
                  <P>\$sei</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=105>
                  <P>ご要望事項</P>
               </TD>
               <TD>
                  <P>\$request3</P>
               </TD>
            </TR>
         </TABLE>
         </P>
      </TD>
   </TR>
</TABLE>
</CENTER>
         <BLOCKQUOTE>
            <B>ご確認が済みましたら</B><FONT COLOR="#FF0000"><B>下記「注文」ボタンを1回だけ押してご発注</B></FONT><B>ください。<BR>
            なお、商品の性格上、これ以降のご注文の取り消しや返品は一切出来ませんので予めご了承下さい。(訪問販売法のクーリングオフは適用されません。)</B></BLOCKQUOTE>
         <CENTER>ご注文の訂正は、ブラウザの「戻る」で「入力フォーム」からやり直して下さい。</CENTER>
         <P><FORM ACTION="/~kazu-y/cgi_bin2/nn_mail3.cgi" METHOD=POST>
            <P><INPUT TYPE="hidden" NAME="name" VALUE="\$name">
            <INPUT TYPE="hidden" NAME="email" VALUE="\$email">
            <INPUT TYPE="hidden" NAME="order4" VALUE="\$order4">
            <INPUT TYPE="hidden" NAME="familyname1" VALUE="\$familyname1">
            <INPUT TYPE="hidden" NAME="firstname1" VALUE="\$firstname1">
            <INPUT TYPE="hidden" NAME="birthday1" VALUE="\$birthday1">
            <INPUT TYPE="hidden" NAME="sex1" VALUE="\$sex1">
            <INPUT TYPE="hidden" NAME="trade1" VALUE="\$trade1">
            <INPUT TYPE="hidden" NAME="request1" VALUE="\$request1">
            <INPUT TYPE="hidden" NAME="order5" VALUE="">
            <INPUT TYPE="hidden" NAME="familyname2" VALUE="">
            <INPUT TYPE="hidden" NAME="firstname2" VALUE="">
            <INPUT TYPE="hidden" NAME="family" VALUE="">
            <INPUT TYPE="hidden" NAME="request2" VALUE="">
            <INPUT TYPE="hidden" NAME="order6" VALUE="\$order6">
            <INPUT TYPE="hidden" NAME="familyname3" VALUE="\$familyname3">
            <INPUT TYPE="hidden" NAME="firstname3" VALUE="\$firstname3">
            <INPUT TYPE="hidden" NAME="birthday3" VALUE="\$birthday3">
            <INPUT TYPE="hidden" NAME="sex3" VALUE="\$sex3">
            <INPUT TYPE="hidden" NAME="trade3" VALUE="\$trade3">
            <INPUT TYPE="hidden" NAME="familyname4" VALUE="\$familyname4">
            <INPUT TYPE="hidden" NAME="firstname4" VALUE="\$firstname4">
            <INPUT TYPE="hidden" NAME="birthday4" VALUE="\$birthday4">
            <INPUT TYPE="hidden" NAME="sex4" VALUE="\$sex4">
            <INPUT TYPE="hidden" NAME="trade4" VALUE="\$trade4">
            <INPUT TYPE="hidden" NAME="sei" VALUE="\$sei">
            <INPUT TYPE="hidden" NAME="request3" VALUE="\$request3">
            <INPUT TYPE="hidden" NAME="order7" VALUE="">
            <INPUT TYPE="hidden" NAME="familyname5" VALUE="">
            <INPUT TYPE="hidden" NAME="firstname5" VALUE="">
            <INPUT TYPE="hidden" NAME="birthday5" VALUE="">
            <INPUT TYPE="hidden" NAME="sex5" VALUE="">
            <INPUT TYPE="hidden" NAME="trade5" VALUE="">
            <INPUT TYPE="hidden" NAME="request5" VALUE="">
            <CENTER><INPUT TYPE=submit NAME="送信" VALUE="依頼"></CENTER>
         </FORM></P></CENTER>
      </TD>
   </TR>
</TABLE>
</P>
</BODY>
</HTML>
ORDER
&jcode'convert(*msg, "sjis", "euc");
	$msg =~ s/\$name/$name/g;
	$msg =~ s/\$email/$email/g;
	$msg =~ s/\$order4/$order4/g;
	$msg =~ s/\$familyname1/$familyname1/g;
	$msg =~ s/\$firstname1/$firstname1/g;
	$msg =~ s/\$birthday1/$birthday1/g;
	$msg =~ s/\$sex1/$sex1/g;
	$msg =~ s/\$trade1/$trade1/g;
	$msg =~ s/\$request1/$request1/g;
	$msg =~ s/\$order6/$order6/g;
	$msg =~ s/\$familyname3/$familyname3/g;
	$msg =~ s/\$firstname3/$firstname3/g;
	$msg =~ s/\$birthday3/$birthday3/g;
	$msg =~ s/\$sex3/$sex3/g;
	$msg =~ s/\$trade3/$trade3/g;
	$msg =~ s/\$familyname4/$familyname4/g;
	$msg =~ s/\$firstname4/$firstname4/g;
	$msg =~ s/\$birthday4/$birthday4/g;
	$msg =~ s/\$sex4/$sex4/g;
	$msg =~ s/\$trade4/$trade4/g;
	$msg =~ s/\$sei/$sei/g;
	$msg =~ s/\$request3/$request3/g;
	print $msg;
__end__
