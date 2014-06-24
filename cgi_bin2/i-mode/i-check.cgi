#!/usr/local/bin/perl
$|=1;
#########################
require 'cgi-lib.pl';
require 'jcode.pl';
require "zenhan.pl";
use MIME::Base64;
&ReadParse();
#####データの取り込み#####
$name = $in{'name'};
$email = $in{'email'};
$email2 = $in{'email2'};
$order2 = $in{'order2'};
$order3 = $in{'order3'};
$zipcord = $in{'zipcord'};
$address = $in{'address'};
$tel = $in{'tel'};
$fax = $in{'fax'};
$fullname = $in{'fullname'};
$familyname = $in{'familyname'};
$brthday = $in{'brthday'};
$method = $in{'method'};
$user = $in{'user'};
$brother = $in{'brother'};
$request = $in{'request'};
######入力データの整形処理######
if ($zipcord ne "") {
	$zipcord =~ s/\s*//g;
	#全角英数字をすべて半角英数字にする。
	$zipcord = &zen2han($zipcord); 
}
if ($tel ne "") {
	$tel =~ s/\s*//g;
	#全角英数字をすべて半角英数字にする。
	$tel = &zen2han($tel); 
}
if ($fax ne "") {
	$fax =~ s/\s*//g;
	#全角英数字をすべて半角英数字にする。
	$fax = &zen2han($fax); 
}
if ($familyname ne "") {
	$familyname =~ s/\s*//g;
}
if ($brthday ne "") {
	$brthday =~ s/\s*//g;
}
if ($email ne "") {
	$email =~ s/\s*//g;
	#全角英数字をすべて半角英数字にする。
	$email = &zen2han($email);
} 
if ($email2 ne "") {
	$email2 =~ s/\s*//g;
	#全角英数字をすべて半角英数字にする。
	$email2 = &zen2han($email);
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
if ($order2 ne "") {
	if ($zipcord eq "") {
		&CgiError("郵便番号が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
	elsif ($address eq "") {
		&CgiError("住所が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}	
	elsif ($fullname eq "") {
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
if (($order3 ne "") and ($method eq "fax")) {
	if ($fax eq "") {
		&CgiError("送り先のファックス番号が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
}
if (($order3 ne "") and ($method eq "mail")) {
	if ($email2 =~ /^\s*$/){
	&CgiError("結果連絡先のメールアドレスの記入がありません。",
	"ブラウザの「Back」ボタンで戻って再入力してください。");
	exit;
    }
    elsif (($email2) and (not $email2 =~ /.+\@.+\..+/)) {
	&CgiError("入力エラー",
		"結果連絡先のメールアドレスの書き方が間違っています。",$email2,
		"ブラウザの「Back」ボタンで戻って再入力してください。");
	exit;
    }
}
#####手段を文章化#####
if ($method eq "fax") {
	$method ="ファックスで送ってください。";
}
if ($method eq "mail") {
	$method ="電子メールで送ってください。";
}
&jcode'convert(*method, 'jis', 'euc');
######ここから引き継ぎ情報の生成と表示画面######
#########書籍のみ注文##########
if ($order2 ne "")  {
	$msg = <<"ORDER020";
Content-type: text/html

<HTML>
<HEAD>
<TITLE>書籍のご注文</TITLE>
<META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=x-sjis">
</HEAD>
<BODY BGCOLOR="#FFFFFF">
<P>
<CENTER><B><U>ご注文内容のご確認</U></B></CENTER>        
<BLOCKQUOTE>この画面は、ご注文内容をご確認頂くためのものです。内容に誤りがある場合は、ブラウザの「戻る」ボタンを押して「入力フォーム」から修正して下さい。これで宜しければ「注文」ボタンを押して下さい。</BLOCKQUOTE>         
<CENTER><B>ご注文内容</B></CENTER><BR>
<HR>
あなたのお名前（お申込人）<BR>
\$name<BR>
メールアドレス<BR>
\$email<BR>
書籍の送り先について<BR>
郵便番号<BR>
\$zipcord<BR>
ご住所<BR>
\$address<BR>
ご自宅のお電話番号<BR>
\$tel<BR>
受取人ご氏名<BR>
\$fullname<BR>
<HR>         
<BLOCKQUOTE><B>ご確認が済みましたら</B><FONT COLOR="#FF0000"><B>下記「注文」ボタンを1回だけ押してご発注</B></FONT><B>ください。<BR>
なお、商品の性格上、これ以降のご注文の取り消しや返品は一切出来ませんので予めご了承下さい。(訪問販売法のクーリングオフは適用されません。）</B></BLOCKQUOTE>        
ご注文の訂正は、ブラウザの「戻る」で「入力フォーム」からやり直して下さい。<BR>          <P><FORM ACTION="/~kazu-y/cgi_bin2/in-order.cgi" METHOD=POST>
            <P><INPUT TYPE="hidden" NAME="name" VALUE="\$name">
            <INPUT TYPE="hidden" NAME="email" VALUE="\$email">
            <INPUT TYPE="hidden" NAME="email2" VALUE="">
            <INPUT TYPE="hidden" NAME="order2" VALUE="\$order2">
            <INPUT TYPE="hidden" NAME="order3" VALUE="">
            <INPUT TYPE="hidden" NAME="zipcord" VALUE="\$zipcord">
            <INPUT TYPE="hidden" NAME="address" VALUE="\$address">
            <INPUT TYPE="hidden" NAME="tel" VALUE="\$tel">
            <INPUT TYPE="hidden" NAME="fax" VALUE="">
            <INPUT TYPE="hidden" NAME="fullname" VALUE="\$fullname">
            <INPUT TYPE="hidden" NAME="familyname" VALUE="">
            <INPUT TYPE="hidden" NAME="brthday" VALUE="">
            <INPUT TYPE="hidden" NAME="method" VALUE="">
            <INPUT TYPE="hidden" NAME="user" VALUE="">
            <INPUT TYPE="hidden" NAME="brother" VALUE="">
            <INPUT TYPE="hidden" NAME="request" VALUE="">
            <INPUT TYPE="hidden" NAME="kgak" VALUE="1,810">
            <CENTER><INPUT TYPE=submit NAME="送信" VALUE="注文">
         </FORM></P>
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
	print $msg;
}
###########命名のみ依頼############
elsif ($order3 ne "")  {
	$msg = <<"ORDER003";
Content-type: text/html

<HTML>
<HEAD>
<TITLE>命名のご依頼</TITLE>
<META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=x-sjis">
</HEAD>
<BODY BGCOLOR="#FFFFFF">
<P>
<CENTER><B><U>ご注文内容のご確認</U></B></CENTER>         
<BLOCKQUOTE>この画面は、ご注文内容をご確認頂くためのものです。内容に誤りがある場合は、ブラウザの「戻る」ボタンを押して「入力フォーム」から修正して下さい。これで宜しければ「注文」ボタンを押して下さい。</BLOCKQUOTE>
<CENTER><B>ご注文内容</B><BR></CENTER>
<HR>
あなたのお名前（お申込人）<BR>
\$name<BR>
メールアドレス<BR>
\$email<BR>
新生児の苗字(姓)<BR>
\$familyname<BR>
ご出産予定日<BR>
\$brthday<BR>
ご利用回数<BR>
\$user<BR>
ご兄姉のお名前<BR>
\$brother<BR>
ご要望事項<BR>
\$request<BR>
結果のご連絡方法<BR>
\$method<BR>
ファックス番号<BR>
\$fax<BR>
パソコンのEメールアドレス<BR>
\$email2<BR>
<HR>
<BLOCKQUOTE><B>ご確認が済みましたら</B><FONT COLOR="#FF0000"><B>下記「注文」ボタンを1回だけ押してご発注</B></FONT><B>ください。<BR>
なお、商品の性格上、これ以降のご注文の取り消しや返品は一切出来ませんので予めご了承下さい。(訪問販売法のクーリングオフは適用されません。）</B></BLOCKQUOTE>         
ご注文の訂正は、ブラウザの「戻る」で「入力フォーム」からやり直して下さい。        
         <P><FORM ACTION="/~kazu-y/cgi_bin2/in-order.cgi" METHOD=POST>
            <P><INPUT TYPE="hidden" NAME="name" VALUE="\$name">
            <INPUT TYPE="hidden" NAME="email" VALUE="\$email">
            <INPUT TYPE="hidden" NAME="order2" VALUE="">
            <INPUT TYPE="hidden" NAME="order3" VALUE="\$order3">
            <INPUT TYPE="hidden" NAME="zipcord" VALUE="">
            <INPUT TYPE="hidden" NAME="address" VALUE="">
            <INPUT TYPE="hidden" NAME="tel" VALUE="\$tel">
            <INPUT TYPE="hidden" NAME="method" VALUE="\$method">
            <INPUT TYPE="hidden" NAME="email2" VALUE="\$email2">
            <INPUT TYPE="hidden" NAME="fax" VALUE="\$fax">
            <INPUT TYPE="hidden" NAME="fullname" VALUE="">
            <INPUT TYPE="hidden" NAME="familyname" VALUE="\$familyname">
            <INPUT TYPE="hidden" NAME="brthday" VALUE="\$brthday">
            <INPUT TYPE="hidden" NAME="user" VALUE="\$user">
            <INPUT TYPE="hidden" NAME="brother" VALUE="\$brother">
            <INPUT TYPE="hidden" NAME="request" VALUE="\$request">
            <INPUT TYPE="hidden" NAME="kgak" VALUE="10,000">
            <CENTER><INPUT TYPE=submit NAME="送信" VALUE="注文">
         </FORM></P>
</P>
</BODY>
</HTML>
ORDER003
&jcode'convert(*msg, "sjis", "euc");
	$msg =~ s/\$name/$name/g;
	$msg =~ s/\$email/$email/g;	
	$msg =~ s/\$order3/$order3/g;
	$msg =~ s/\$tel/$tel/g;
	$msg =~ s/\$method/$method/g;
	$msg =~ s/\$email2/$email2/g;
	$msg =~ s/\$fax/$fax/g;	
	$msg =~ s/\$familyname/$familyname/g;
	$msg =~ s/\$brthday/$brthday/g;
	$msg =~ s/\$user/$user/g;
	$msg =~ s/\$brother/$brother/g;
	$msg =~ s/\$request/$request/g;
	print $msg;
}
__end__
