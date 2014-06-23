#!/usr/local/bin/perl
$|=1;
##########################
$sendmail = "/usr/lib/sendmail";
$youraddress = 'okina@e-mail.ne.jp ';
##########################
require "cgi-lib.pl";
require "jcode.pl";
require "zenhan.pl";
&ReadParse;

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
	#郵便番号が7桁以下で入力された場合、00を末尾に付加する。
	$zipcord = $zipcord . "00000000";
	$zipcord = substr($zipcord, 0, 8);
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
if ($order2 ne "") {
	if ($zipcord eq "") {
		&CgiError("郵便番号が入力されていません。",
		"ブラウザの｢Back｣ボタンで戻って再入力してください。");
		exit;
	}
	elsif ($address eq "") {
		&CgiError("住所が入力されていません。",
		"ブラウザの｢Back｣ボタンで戻って再入力してください。");
		exit;
	}	
	elsif ($fullname eq "") {
		&CgiError("受取人が入力されていません。",
		"ブラウザの｢Back｣ボタンで戻って再入力してください。");
		exit;
	}
}
if ($order3 ne "") {
	if ($familyname eq "") {
		&CgiError("苗字(姓)が入力されていません。",
		"ブラウザの｢Back｣ボタンで戻って再入力してください。");
		exit;
	}
	elsif ($brthday eq "") {
		&CgiError("予定日(誕生日)が入力されていません。",
		"ブラウザの｢Back｣ボタンで戻って再入力してください。");
		exit;
	}
}
if (($order3 ne "") and ($method eq "fax")) {
	if ($fax eq "") {
		&CgiError("送り先のファックス番号が入力されていません。",
		"ブラウザの｢Back｣ボタンで戻って再入力してください。");
		exit;
	}
}
if (($order3 ne "") and ($method eq "mail")) {
	if ($email2 =~ /^\s*$/){
	&CgiError("結果連絡先のメールアドレスの記入がありません。",
	"ブラウザの｢Back｣ボタンで戻って再入力してください。");
	exit;
    }
    elsif (($email2) and (not $email2 =~ /.+\@.+\..+/)) {
	&CgiError("入力エラー",
		"結果連絡先のメールアドレスの書き方が間違っています。",$email2,
		"ブラウザの｢Back｣ボタンで戻って再入力してください。");
	exit;
    }
}
#####手段を文章化#####
if ($method eq "fax") {
	$method ="ファックスで送ってください。";
}
if ($method eq "mail") {
	$method ="メールして下さい。";
}
#####注文メールの送信#####
$com = <<"MESSAGE";
From: $email
Subject: 翁へご注文(iモードv.3)

=====================================
申込人様の氏名：
$name
申込人様のEメールアドレス：
$email
ご注文内容：
$order2
$order3

書籍の送付先
郵便番号：
$zipcord
ご住所：
$address
お電話番号：
$tel
受取人様：
$fullname

命名のご依頼内容
姓(みょうじ)：
$familyname
出産予定日：
$brthday
結果の送信手段：
$method
ファックスの番号：
$fax
結果Eメールの番号：
$email2
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

print "Content-type: text/html\n\n";
print "<HTML>\n";
print "<HEAD>\n";
print "<TITLE>ご依頼受付完了</TITLE>\n";
print "<META HTTP-EQUIV=\"Content-Type\" CONTENT=\"text/html;CHARSET=SHIFT_JIS\">\n";
print "</HEAD>\n";
print "<BODY BGCOLOR=\"#FFFFFF\" TEXT=\"#000000\" LINK=\"#0000FF\">\n";
print "<P>\n";
print "<BR>\n";
print "<BR>\n";
print "<FONT COLOR=\"#FF0000\"><B>ありがとうございました。</B></FONT><BR>\n";
print "<A HREF=\"/~kazu-y/i-info.html\" accesskey=1>1→お知らせに戻る。</A><BR>\n";
print "</BODY>\n";
print "</HTML>\n";
