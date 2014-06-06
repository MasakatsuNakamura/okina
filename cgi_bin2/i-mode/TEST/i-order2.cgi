#!/usr/local/bin/perl
$|=1;
#########################
$sendmail = "/usr/lib/sendmail";
$youraddress = 'okina@e-mail.ne.jp';
#########################
require "cgi-lib.pl";
require "jcode.pl";
require "zenhan.pl";
&ReadParse;
#########################
$name = $in{'name'};
$email = $in{'email'};
$order4 = $in{'order4'};
$order6 = $in{'order6'};
$order7 = $in{'order7'};
$familyname1 = $in{'familyname1'};
$firstname1 = $in{'firstname1'};
$birthday1= $in{'birthday1'};
$sex1 = $in{'sex1'};
$trade1 = $in{'trade1'};
$familyname2 = $in{'familyname2'};
$firstname2 = $in{'firstname2'};
$birthday2= $in{'birthday2'};
$sex2 = $in{'sex2'};
$trade2 = $in{'trade2'};
$request = $in{'request'};

######入力データの整形処理######
if ($familyname1 ne "") {
	$familyname1 =~ s/\s*//g;
}
if ($familyname2 ne "") {
	$familyname2 =~ s/\s*//g;
}
if ($firstname1 ne "") {
	$familyname1 =~ s/\s*//g;
}
if ($firstname2 ne "") {
	$familyname3 =~ s/\s*//g;
}
if ($birthday1 ne "") {
	$birthday1 =~ s/\s*//g;
}
if ($birthday2 ne "") {
	$birthday3 =~ s/\s*//g;
}
if ($email ne "") {
	$email =~ s/\s*//g;
	#全角英数字をすべて半角英数字にする。
	$email = &zen2han($email);
} 

#####入力エラーのチェック#####
if ($name =~ /^\s*$/){
	&CgiError("名前の記入がありません。",
	"ブラウザの｢Back｣ボタンで戻って再入力してください。");
	exit;
}
if ($email =~ /^\s*$/){
	&CgiError("メールアドレスの記入がありません。",
	"ブラウザの｢Back｣ボタンで戻って再入力してください。");
	exit;
}
elsif (($email) and (not $email =~ /.+\@.+\..+/)) {
	&CgiError("入力エラー",
		"メールアドレスの書き方が間違っています。",$email,
		"ブラウザの｢Back｣ボタンで戻って再入力してください。");
	exit;
}
if ($order4 ne "") {
	if ($familyname1 eq "") {
		&CgiError("姓が入力されていません。",
		"ブラウザの｢Back｣ボタンで戻って再入力してください。");
		exit;
	}
	elsif ($firstname1 eq "") {
		&CgiError("名が入力されていません。",
		"ブラウザの｢Back｣ボタンで戻って再入力してください。");
		exit;
	}	
	elsif ($birthday1 eq "") {
		&CgiError("生年月日が入力されていません。",
		"ブラウザの｢Back｣ボタンで戻って再入力してください。");
		exit;
	}
	elsif ($trade1 eq "") {
		&CgiError("お仕事内容または、名前の用途が入力されていません。",
		"ブラウザの｢Back｣ボタンで戻って再入力してください。");
		exit;
	}
}
if ($order6 ne "") {
	if ($familyname1 eq "") {
		&CgiError("依頼者側の姓が入力されていません。",
		"ブラウザの｢Back｣ボタンで戻って再入力してください。");
		exit;
	}
   elsif ($firstname1 eq "") {
		&CgiError("依頼者側の名が入力されていません。",
		"ブラウザの｢Back｣ボタンで戻って再入力してください。");
		exit;
	}
   elsif ($birthday1 eq "") {
		&CgiError("依頼者側の生年月日が入力されていません。",
		"ブラウザの｢Back｣ボタンで戻って再入力してください。");
		exit;
	}
   elsif ($trade1 eq "") {
		&CgiError("依頼者側のご職業が入力されていません。",
		"ブラウザの｢Back｣ボタンで戻って再入力してください。");
		exit;
	}
   elsif ($familyname2 eq "") {
		&CgiError("相手側の姓が入力されていません。",
		"ブラウザの｢Back｣ボタンで戻って再入力してください。");
		exit;
	}
   elsif ($firstname2 eq "") {
		&CgiError("相手側の名が入力されていません。",
		"ブラウザの｢Back｣ボタンで戻って再入力してください。");
		exit;
	}
   elsif ($birthday2 eq "") {
		&CgiError("相手側の生年月日が入力されていません。",
		"ブラウザの｢Back｣ボタンで戻って再入力してください。");
		exit;
	}
   elsif ($trade2 eq "") {
		&CgiError("相手側のご職業が入力されていません。",
		"ブラウザの｢Back｣ボタンで戻って再入力してください。");
		exit;
	}
   elsif ($request eq "") {
		&CgiError("ご相談内容をお書き下さい。",
		"ブラウザの｢Back｣ボタンで戻って再入力してください。");
		exit;
	}
}
if ($order7 ne "") {
	if ($familyname1 eq "") {
		&CgiError("姓が入力されていません。",
		"ブラウザの｢Back｣ボタンで戻って再入力してください。");
		exit;
	}
   elsif ($firstname1 eq "") {
		&CgiError("名が入力されていません。",
		"ブラウザの｢Back｣ボタンで戻って再入力してください。");
		exit;
	}
   elsif ($birthday1 eq "") {
		&CgiError("生年月日が入力されていません。",
		"ブラウザの｢Back｣ボタンで戻って再入力してください。");
		exit;
	}
   elsif ($trade1 eq "") {
		&CgiError("ご職業が入力されていません。",
		"ブラウザの｢Back｣ボタンで戻って再入力してください。");
		exit;
	}
   elsif ($request eq "") {
		&CgiError("ご相談内容をお書き下さい。",
		"ブラウザの｢Back｣ボタンで戻って再入力してください。");
		exit;
	}
}

#####注文メールの送信#####
$com = <<"MESSAGE3";
From: $email
Subject: 翁へご相談(iモードv.1)

=====================================
山本翁さまへ、以下のご相談を致したく。

申込人様の氏名：
$name
申込人様のEメールアドレス：
$email
ご依頼内容：
$order4 
$order6 
$order7 
ご要望事項：
$request

ご依頼者の情報
姓：
$familyname1
名：
$firstname1
生年月日：
$birthday1
姓別：
$sex1
ご職業・業務内容：
$trade1
結婚後の姓：
$sei

相手方の情報
姓：
$familyname2 
名：
$firstname2
生年月日：
$birthday2
性別：
$sex2 
ご職業：
$trade2

=====================================
MESSAGE3

&jcode'convert(*com,"jis");
open(MAIL, "|$sendmail $youraddress");
print MAIL $com;
close(MAIL);

print "Content-type: text/html\n\n";
print "<HTML>\n";
print "<HEAD>\n";
print "<TITLE>ご相談受付完了</TITLE>\n";
print "<META HTTP-EQUIV=\"Content-Type\" CONTENT=\"text/html;CHARSET=SHIFT_JIS\">\n";
print "</HEAD>\n";
print "<BODY BGCOLOR=\"#FFFFFF\" TEXT=\"#000000\" LINK=\"#0000FF\">\n";
print "<P>\n";
print "<BR>\n";
print "<BR>\n";
print "<FONT COLOR=\"#FF0000\"><B>ありがとうございました。</B></FONT><BR>\n";
print "<A HREF=\"/~kazu-y/i-info2.html\" accesskey=1>1→お知らせに戻る。</A><BR>\n";
print "</BODY>\n";
print "</HTML>\n";
