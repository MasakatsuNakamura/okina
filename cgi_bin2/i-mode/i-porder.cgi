#!/usr/local/bin/perl
$|=1;
require "cgi-lib.pl";
require "jcode.pl";
require "zenhan.pl";

$root = "/~kazu-y";
$cgipath = "/~kazu-y/cgi_bin2";
$baseurl = "http://www2.mahoroba.ne.jp";

&ReadParse;
#####データの取り込み#####
$name = $in{'name'};
$email = $in{'email'};
$order3 = $in{'order3'};
$familyname = $in{'familyname'};
$brthday = $in{'brthday'};
$user = $in{'user'};
$brother = $in{'brother'};

######入力データの整形処理######
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
if ($order3 eq "")  {
	&CgiError("入力エラー",
		"ご注文が何も指示されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
	exit;
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

#####注文票２の表示#####
$msg = <<"ORDER2";
Content-type: text/html

<HTML>
<HEAD>
   <TITLE>命名のご依頼(1/2)</TITLE>
   <META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=SHIFT_JIS">
</HEAD>
<BODY BGCOLOR="#FFFFFF" TEXT="#000000" LINK="#0000FF">
<P><FORM ACTION="$cgipath/i-check.cgi" METHOD=POST>
   <P><INPUT TYPE=hidden NAME=name VALUE="\$name">
   <INPUT TYPE=hidden NAME=email VALUE="\$email">
   <INPUT TYPE=hidden NAME=order3 VALUE="\$order3">
   <INPUT TYPE=hidden NAME=familyname VALUE="\$familyname">
   <INPUT TYPE=hidden NAME=brthday VALUE="\$brthday">
   <INPUT TYPE=hidden NAME=user VALUE="\$user">
   <INPUT TYPE=hidden NAME=brother VALUE="\$brother"></P>
   
   <P><B><U>ご要望事項</U></B><U>　(ご期待に添えない場合もあります。ご了承下さい。)</U><BR>
   <TEXTAREA NAME=request ROWS=6 COLS=10 WRAP=virtual></TEXTAREA></P>
   
   <P><B><U>結果のご連絡方法</U></B><BR>
   <INPUT TYPE=radio NAME=method VALUE=fax CHECKED>ファックスで受信します。→下記1.にお電話番号をご記入下さい。<BR>
   <INPUT TYPE=radio NAME=method VALUE=mail>パソコンから電子メールで受信します。<FONT COLOR="#FF0000">（携帯電話では受信できません)</FONT>→下記2.にアドレスをご記入下さい。</P>
   
   <P><B><U>1.ファックス番号</U></B><BR>
   <INPUT TYPE=text NAME=fax VALUE="" SIZE=16 ISTYLE=4></P>
   
   <P><B><U>2.パソコンの電子メールアドレス<BR>
   </U></B><INPUT TYPE=text NAME=email2 VALUE="" SIZE=16 MAXLENGTH=80 ISTYLE=3></P>
   
   <P><FONT COLOR="#FF0000"><B>入力は以上です。内容をご確認の上、ご注文ボタンを1回だけクリックして下さい。<BR>
   ご注文確認の画面が表示されますので、入力内容をご確認下さい。</B></FONT></P>
   <P><B><INPUT TYPE=submit NAME="送信" VALUE="ご注文"></B><INPUT TYPE=reset VALUE="リセット">
</FORM></P>

<P><B>※上手く注文できない場合には、上記内容を</B><A HREF="mailto:okina\@e-mail.ne.jp" ACCESSKEY=0><B>メール(0ボタンを押して下さい。)</B></A>(okina\@e-mail.ne.jp)<B>にて送付下さい。</B></P>
</BODY>
</HTML>
ORDER2
	&jcode'convert(*msg, "sjis", "euc");
	$msg =~ s/\$name/$name/g;
	$msg =~ s/\$email/$email/g;
	$msg =~ s/\$order3/$order3/g;
	$msg =~ s/\$familyname/$familyname/g;
	$msg =~ s/\$brthday/$brthday/g;
	$msg =~ s/\$user/$user/g;
	$msg =~ s/\$brother/$brother/g;
	print $msg;
__END__


