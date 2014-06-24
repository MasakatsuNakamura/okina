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
$order1 = $in{'order1'};
$order2 = $in{'order2'};
$order3 = $in{'order3'};
$zipcord = $in{'zipcord'};
$address = $in{'address'};
$tel = $in{'tel'};
$fullname = $in{'fullname'};
$familyname = $in{'familyname'};
$brthday = $in{'brthday'};
$user = $in{'user'};
$brother = $in{'brother'};
$request = $in{'request'};
$exp = $in{'exp'};
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
if (($order1 eq "" ) and ($order2 eq "" ) and ($order3 eq ""))  {
	&CgiError("入力エラー",
		"ご注文が何も指示されていません。",
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
	elsif ($tel eq "") {
		&CgiError("電話番号が入力されていません。固定電話が無い時に限り携帯番号でも結構です。",
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
if ($exp ne "") {
	if ($tel eq "") {
		&CgiError("電話番号が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
	elsif ($zipcord eq "") {
		&CgiError("郵便番号が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}
    elsif ($address eq "") {
		&CgiError("住所が入力されていません。",
		"ブラウザの「Back」ボタンで戻って再入力してください。");
		exit;
	}	
}
#####合計代金の計算ロジック#####
if (($order1 ne "") and ($order2 ne "") and ($order3 ne ""))  {
   if ($exp ne "") {
       $kgak ="16,810";
   }
   elsif ($exp eq "") {
       $kgak ="11,810";
   }
}
elsif (($order1 ne "") and ($order2 ne ""))  {
   $kgak ="1,810";
}
elsif (($order1 ne "") and ($order3 ne ""))  {
   if ($exp ne "") {
       $kgak ="15,500";
   }
   elsif ($exp eq "") {
       $kgak ="10,500";
   }
}
elsif (($order2 ne "") and ($order3 ne ""))  {
   if ($exp ne "") {
       $kgak ="16,810";
   }
   elsif ($exp eq "") {
       $kgak ="11,810";
   }
}
elsif ($order1 ne "")  {
   $kgak ="500";
}
elsif ($order2 ne "")  {
   $kgak ="1,810";
}
elsif ($order3 ne "")  {
   if ($exp ne "") {
       $kgak ="15,000";
   }
   elsif ($exp eq "") {
       $kgak ="10,000";
  }
}
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
         <CENTER><FONT SIZE="+3"><B><U>ご注文内容のご確認</U></B></FONT></CENTER>
         
         <BLOCKQUOTE>この画面は、ご注文内容をご確認頂くためのものです。内容に誤りがある場合は、ブラウザの「戻る」ボタンを押して「入力フォーム」から修正して下さい。これで宜しければ「注文」ボタンを押して下さい。なお電子本と書籍の両方ご注文の場合、500円を割引致します。</BLOCKQUOTE>
         
         <CENTER><B>ご注文内容</B><BR>
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
      <TD WIDTH=148>
         <P>ご依頼の内容</P>
      </TD>
      <TD>
         <P>山本翁の著書(電子本と実本)の注文、新生児の命名依頼</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>書籍のご送付先</P>
      </TD>
      <TD>
         <P><TABLE BORDER=1>
            <TR>
               <TD WIDTH=55>
                  <P>郵便番号</P>
               </TD>
               <TD>
                  <P>\$zipcord</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=55>
                  <P>住所</P>
               </TD>
               <TD>
                  <P>\$address</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=55>
                  <P>お受取人</P>
               </TD>
               <TD>
                  <P>\$fullname</P>
               </TD>
            </TR>
         </TABLE>
         </P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>ご連絡先お電話番号</P>
      </TD>
      <TD>
         <P>\$tel</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>新生児の命名依頼</P>
      </TD>
      <TD>
         <P><TABLE BORDER=1>
            <TR>
               <TD WIDTH=92>
                  <P>姓(苗字)</P>
               </TD>
               <TD>
                  <P>\$familyname</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=92>
                  <P>出生日(予定日)</P>
               </TD>
               <TD>
                  <P>\$brthday</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=92>
                  <P>過去のご依頼</P>
               </TD>
               <TD>
                  <P>\$user</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=92>
                  <P>ご兄弟のお名前</P>
               </TD>
               <TD>
                  <P>\$brother</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=92>
                  <P>ご要望事項</P>
               </TD>
               <TD>
                  <P>\$request</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=92>
                  <P>特記事項</P>
               </TD>
               <TD>
                  <P>\$exp</P>
               </TD>
            </TR>
         </TABLE>
         </P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>合計お支払い金額</P>
      </TD>
      <TD>
         <P>\$kgak 円</P>
      </TD>
   </TR>
</TABLE>
</CENTER>
         
         <BLOCKQUOTE>
            <B>ご確認が済みましたら</B><FONT COLOR="#FF0000"><B>下記「注文」ボタンを1回だけ押してご発注</B></FONT><B>ください。<BR>
            なお、商品の性格上、これ以降のご注文の取り消しや返品は一切出来ませんので予めご了承下さい。(訪問販売法のクーリングオフは適用されません。）</B></BLOCKQUOTE>
         
         <CENTER>ご注文の訂正は、ブラウザの「戻る」で「入力フォーム」からやり直して下さい。</CENTER>
         
         <P><FORM ACTION="/~kazu-y/cgi_bin2/nn_mail.cgi" METHOD=POST>
            <P><INPUT TYPE="hidden" NAME="name" VALUE="\$name">
            <INPUT TYPE="hidden" NAME="email" VALUE="\$email">
            <INPUT TYPE="hidden" NAME="order1" VALUE="\$order1">
            <INPUT TYPE="hidden" NAME="order2" VALUE="\$order2">
            <INPUT TYPE="hidden" NAME="order3" VALUE="\$order3">
            <INPUT TYPE="hidden" NAME="zipcord" VALUE="\$zipcord">
            <INPUT TYPE="hidden" NAME="address" VALUE="\$address">
            <INPUT TYPE="hidden" NAME="tel" VALUE="\$tel">
            <INPUT TYPE="hidden" NAME="fullname" VALUE="\$fullname">
            <INPUT TYPE="hidden" NAME="familyname" VALUE="\$familyname">
            <INPUT TYPE="hidden" NAME="brthday" VALUE="\$brthday">
            <INPUT TYPE="hidden" NAME="user" VALUE="\$user">
            <INPUT TYPE="hidden" NAME="brother" VALUE="\$brother">
            <INPUT TYPE="hidden" NAME="request" VALUE="\$request">
            <INPUT TYPE="hidden" NAME="exp" VALUE="\$exp">
            <INPUT TYPE="hidden" NAME="kgak" VALUE="\$kgak">
            <CENTER><INPUT TYPE=submit NAME="送信" VALUE="注文"></CENTER>
         </FORM></P></CENTER>
      </TD>
   </TR>
</TABLE>
</P>
</BODY>
</HTML>

ORDER123
&jcode'convert(*msg, "sjis", "euc");
	$msg =~ s/\$name/$name/g;
	$msg =~ s/\$email/$email/g;
	$msg =~ s/\$order1/$order1/g;
	$msg =~ s/\$order2/$order2/g;	
	$msg =~ s/\$order3/$order3/g;	
	$msg =~ s/\$zipcord/$zipcord/g;
	$msg =~ s/\$address/$address/g;
	$msg =~ s/\$tel/$tel/g;
	$msg =~ s/\$fullname/$fullname/g;
	$msg =~ s/\$familyname/$familyname/g;
	$msg =~ s/\$brthday/$brthday/g;
	$msg =~ s/\$user/$user/g;
	$msg =~ s/\$brother/$brother/g;
	$msg =~ s/\$request/$request/g;
	$msg =~ s/\$exp/$exp/g;
    $msg =~ s/\$kgak/$kgak/g;
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
<CENTER><FONT SIZE="+3"><B><U>ご注文内容のご確認</U></B></FONT></CENTER>
         
         <BLOCKQUOTE>この画面は、ご注文内容をご確認頂くためのものです。内容に誤りがある場合は、ブラウザの「戻る」ボタンを押して「入力フォーム」から修正して下さい。これで宜しければ「注文」ボタンを押して下さい。なお電子本と書籍の両方ご注文の場合、500円を割引致します。</BLOCKQUOTE>
         
         <CENTER><B>ご注文内容</B><BR>
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
      <TD WIDTH=148>
         <P>ご依頼の内容</P>
      </TD>
      <TD>
         <P>山本翁の著書(電子本と実本)の注文</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>書籍のご送付先</P>
      </TD>
      <TD>
         <P><TABLE BORDER=1>
            <TR>
               <TD WIDTH=55>
                  <P>郵便番号</P>
               </TD>
               <TD>
                  <P>\$zipcord</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=55>
                  <P>住所</P>
               </TD>
               <TD>
                  <P>\$address</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=55>
                  <P>お受取人</P>
               </TD>
               <TD>
                  <P>\$fullname</P>
               </TD>
            </TR>
         </TABLE>
         </P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>ご連絡先お電話番号</P>
      </TD>
      <TD>
         <P>\$tel</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>合計お支払い金額</P>
      </TD>
      <TD>
         <P>\$kgak 円</P>
      </TD>
   </TR>
</TABLE>
</CENTER>
         
         <BLOCKQUOTE>
            <B>ご確認が済みましたら</B><FONT COLOR="#FF0000"><B>下記「注文」ボタンを1回だけ押してご発注</B></FONT><B>ください。<BR>
            なお、商品の性格上、これ以降のご注文の取り消しや返品は一切出来ませんので予めご了承下さい。(訪問販売法のクーリングオフは適用されません。）</B></BLOCKQUOTE>
         
         <CENTER>ご注文の訂正は、ブラウザの「戻る」で「入力フォーム」からやり直して下さい。</CENTER>
         
         <P><FORM ACTION="/~kazu-y/cgi_bin2/nn_mail.cgi" METHOD=POST>
            <P><INPUT TYPE="hidden" NAME="name" VALUE="\$name">
            <INPUT TYPE="hidden" NAME="email" VALUE="\$email">
            <INPUT TYPE="hidden" NAME="order1" VALUE="\$order1">
            <INPUT TYPE="hidden" NAME="order2" VALUE="\$order2">
            <INPUT TYPE="hidden" NAME="order3" VALUE="">
            <INPUT TYPE="hidden" NAME="zipcord" VALUE="\$zipcord">
            <INPUT TYPE="hidden" NAME="address" VALUE="\$address">
            <INPUT TYPE="hidden" NAME="tel" VALUE="\$tel">
            <INPUT TYPE="hidden" NAME="fullname" VALUE="\$fullname">
            <INPUT TYPE="hidden" NAME="familyname" VALUE="">
            <INPUT TYPE="hidden" NAME="brthday" VALUE="">
            <INPUT TYPE="hidden" NAME="user" VALUE="">
            <INPUT TYPE="hidden" NAME="brother" VALUE="">
            <INPUT TYPE="hidden" NAME="request" VALUE="">
            <INPUT TYPE="hidden" NAME="exp" VALUE="">
            <INPUT TYPE="hidden" NAME="kgak" VALUE="\$kgak">
            <CENTER><INPUT TYPE=submit NAME="送信" VALUE="注文"></CENTER>
         </FORM></P></CENTER>
      </TD>
   </TR>
</TABLE>
</P>
</BODY>
</HTML>

ORDER120
&jcode'convert(*msg, "sjis", "euc");
	$msg =~ s/\$name/$name/g;
	$msg =~ s/\$email/$email/g;
	$msg =~ s/\$order1/$order1/g;
	$msg =~ s/\$order2/$order2/g;	
	$msg =~ s/\$zipcord/$zipcord/g;
	$msg =~ s/\$address/$address/g;
	$msg =~ s/\$tel/$tel/g;
	$msg =~ s/\$fullname/$fullname/g;
    $msg =~ s/\$kgak/$kgak/g;
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
         <CENTER><FONT SIZE="+3"><B><U>ご注文内容のご確認</U></B></FONT></CENTER>
         
         <BLOCKQUOTE>この画面は、ご注文内容をご確認頂くためのものです。内容に誤りがある場合は、ブラウザの「戻る」ボタンを押して「入力フォーム」から修正して下さい。これで宜しければ「注文」ボタンを押して下さい。</BLOCKQUOTE>
         
         <CENTER><B>ご注文内容</B><BR>
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
      <TD WIDTH=148>
         <P>ご依頼の内容</P>
      </TD>
      <TD>
         <P>山本翁の著書(電子本)の注文、新生児の命名依頼</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>ご依頼主さまの情報<BR>
         (お急ぎの方のみ)</P>
      </TD>
      <TD>
         <P><TABLE BORDER=1>
            <TR>
               <TD WIDTH=64>
                  <P>郵便番号</P>
               </TD>
               <TD>
                  <P>\$zipcord</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=64>
                  <P>住所</P>
               </TD>
               <TD>
                  <P>\$address</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=64>
                  <P>お電話番号</P>
               </TD>
               <TD>
                  <P>\$tel</P>
               </TD>
            </TR>
         </TABLE>
         </P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>新生児の命名依頼</P>
      </TD>
      <TD>
         <P><TABLE BORDER=1>
            <TR>
               <TD WIDTH=90>
                  <P>姓(苗字)</P>
               </TD>
               <TD>
                  <P>\$familyname</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=90>
                  <P>出生日(予定日)</P>
               </TD>
               <TD>
                  <P>\$brthday</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=90>
                  <P>過去のご依頼</P>
               </TD>
               <TD>
                  <P>\$user</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=90>
                  <P>ご兄弟のお名前</P>
               </TD>
               <TD>
                  <P>\$brother</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=90>
                  <P>ご要望事項</P>
               </TD>
               <TD>
                  <P>\$request</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=90>
                  <P>特記事項</P>
               </TD>
               <TD>
                  <P>\$exp</P>
               </TD>
            </TR>
         </TABLE>
         </P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>合計お支払い金額</P>
      </TD>
      <TD>
         <P>\$kgak 円</P>
      </TD>
   </TR>
         </TABLE>
</CENTER>
         
         <BLOCKQUOTE>
            <B>ご確認が済みましたら</B><FONT COLOR="#FF0000"><B>下記「注文」ボタンを1回だけ押してご発注</B></FONT><B>ください。最近、メールアドレスの間違いが多いようです。メールアドレスをもう一度、ご確認下さい。<BR>
            なお、商品の性格上、これ以降のご注文の取り消しや返品は一切出来ませんので予めご了承下さい。(訪問販売法のクーリングオフは適用されません。）</B></BLOCKQUOTE>
         
         <CENTER>ご注文の訂正は、ブラウザの「戻る」で「入力フォーム」からやり直して下さい。</CENTER>
         
         <P><FORM ACTION="/~kazu-y/cgi_bin2/nn_mail.cgi" METHOD=POST>
            <P><INPUT TYPE="hidden" NAME="name" VALUE="\$name">
            <INPUT TYPE="hidden" NAME="email" VALUE="\$email">
            <INPUT TYPE="hidden" NAME="order1" VALUE="\$order1">
            <INPUT TYPE="hidden" NAME="order2" VALUE="">
            <INPUT TYPE="hidden" NAME="order3" VALUE="\$order3">
            <INPUT TYPE="hidden" NAME="zipcord" VALUE="\$zipcord">
            <INPUT TYPE="hidden" NAME="address" VALUE="\$address">
            <INPUT TYPE="hidden" NAME="tel" VALUE="\$tel">
            <INPUT TYPE="hidden" NAME="fullname" VALUE="">
            <INPUT TYPE="hidden" NAME="familyname" VALUE="\$familyname">
            <INPUT TYPE="hidden" NAME="brthday" VALUE="\$brthday">
            <INPUT TYPE="hidden" NAME="user" VALUE="\$user">
            <INPUT TYPE="hidden" NAME="brother" VALUE="\$brother">
            <INPUT TYPE="hidden" NAME="request" VALUE="\$request">
            <INPUT TYPE="hidden" NAME="exp" VALUE="\$exp">
            <INPUT TYPE="hidden" NAME="kgak" VALUE="\$kgak">
            <CENTER><INPUT TYPE=submit NAME="送信" VALUE="注文"></CENTER>
         </FORM></P></CENTER>
      </TD>
   </TR>
</TABLE>
</P>
</BODY>
</HTML>

ORDER103
&jcode'convert(*msg, "sjis", "euc");
	$msg =~ s/\$name/$name/g;
	$msg =~ s/\$email/$email/g;
	$msg =~ s/\$order1/$order1/g;	
	$msg =~ s/\$order3/$order3/g;	
	$msg =~ s/\$zipcord/$zipcord/g;
	$msg =~ s/\$address/$address/g;
	$msg =~ s/\$tel/$tel/g;
	$msg =~ s/\$familyname/$familyname/g;
	$msg =~ s/\$brthday/$brthday/g;
	$msg =~ s/\$user/$user/g;
	$msg =~ s/\$brother/$brother/g;
	$msg =~ s/\$request/$request/g;
	$msg =~ s/\$exp/$exp/g;
	$msg =~ s/\$kgak/$kgak/g;
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
         <CENTER><FONT SIZE="+3"><B><U>ご注文内容のご確認</U></B></FONT></CENTER>
         
         <BLOCKQUOTE>この画面は、ご注文内容をご確認頂くためのものです。内容に誤りがある場合は、ブラウザの「戻る」ボタンを押して「入力フォーム」から修正して下さい。これで宜しければ「注文」ボタンを押して下さい。</BLOCKQUOTE>
         
         <CENTER><B>ご注文内容</B><BR>
         <TABLE BORDER=1 WIDTH="80%">
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
      <TD WIDTH=148>
         <P>ご依頼の内容</P>
      </TD>
      <TD>
         <P>山本翁の著書(実本)の注文、新生児の命名依頼</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>書籍のご送付先</P>
      </TD>
      <TD>
         <P><TABLE BORDER=1>
            <TR>
               <TD WIDTH=55>
                  <P>郵便番号</P>
               </TD>
               <TD>
                  <P>\$zipcord</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=55>
                  <P>住所</P>
               </TD>
               <TD>
                  <P>\$address</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=55>
                  <P>お受取人</P>
               </TD>
               <TD>
                  <P>\$fullname</P>
               </TD>
            </TR>
         </TABLE>
         </P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>ご連絡先お電話番号</P>
      </TD>
      <TD>
         <P>\$tel</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>新生児の命名依頼</P>
      </TD>
      <TD>
         <P><TABLE BORDER=1>
            <TR>
               <TD WIDTH=92>
                  <P>姓(苗字)</P>
               </TD>
               <TD>
                  <P>\$familyname</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=92>
                  <P>出生日(予定日)</P>
               </TD>
               <TD>
                  <P>\$brthday</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=92>
                  <P>過去のご依頼</P>
               </TD>
               <TD>
                  <P>\$user</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=92>
                  <P>ご兄弟のお名前</P>
               </TD>
               <TD>
                  <P>\$brother</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=92>
                  <P>ご要望事項</P>
               </TD>
               <TD>
                  <P>\$request</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=92>
                  <P>特記事項</P>
               </TD>
               <TD>
                  <P>\$exp</P>
               </TD>
            </TR>
         </TABLE>
         </P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>合計お支払い金額</P>
      </TD>
      <TD>
         <P>\$kgak 円</P>
      </TD>
   </TR>
         </TABLE>
        </CENTER>
         
         <BLOCKQUOTE>
            <B>ご確認が済みましたら</B><FONT COLOR="#FF0000"><B>下記「注文」ボタンを1回だけ押してご発注</B></FONT><B>ください。<BR>
            なお、商品の性格上、これ以降のご注文の取り消しや返品は一切出来ませんので予めご了承下さい。(訪問販売法のクーリングオフは適用されません。）</B></BLOCKQUOTE>
         
         <CENTER>ご注文の訂正は、ブラウザの「戻る」で「入力フォーム」からやり直して下さい。</CENTER>
         
         <P><FORM ACTION="/~kazu-y/cgi_bin2/nn_mail.cgi" METHOD=POST>
            <P><INPUT TYPE="hidden" NAME="name" VALUE="\$name">
            <INPUT TYPE="hidden" NAME="email" VALUE="\$email">
            <INPUT TYPE="hidden" NAME="order1" VALUE="">
            <INPUT TYPE="hidden" NAME="order2" VALUE="\$order2">
            <INPUT TYPE="hidden" NAME="order3" VALUE="\$order3">
            <INPUT TYPE="hidden" NAME="zipcord" VALUE="\$zipcord">
            <INPUT TYPE="hidden" NAME="address" VALUE="\$address">
            <INPUT TYPE="hidden" NAME="tel" VALUE="\$tel">
            <INPUT TYPE="hidden" NAME="fullname" VALUE="\$fullname">
            <INPUT TYPE="hidden" NAME="familyname" VALUE="\$familyname">
            <INPUT TYPE="hidden" NAME="brthday" VALUE="\$brthday">
            <INPUT TYPE="hidden" NAME="user" VALUE="\$user">
            <INPUT TYPE="hidden" NAME="brother" VALUE="\$brother">
            <INPUT TYPE="hidden" NAME="request" VALUE="\$request">
            <INPUT TYPE="hidden" NAME="exp" VALUE="\$exp">
            <INPUT TYPE="hidden" NAME="kgak" VALUE="\$kgak">
            <CENTER><INPUT TYPE=submit NAME="送信" VALUE="注文"></CENTER>
         </FORM></P></CENTER>
      </TD>
   </TR>
</TABLE>
</P>
</BODY>
</HTML>

ORDER023
&jcode'convert(*msg, "sjis", "euc");
	$msg =~ s/\$name/$name/g;
	$msg =~ s/\$email/$email/g;
	$msg =~ s/\$order2/$order2/g;	
	$msg =~ s/\$order3/$order3/g;	
	$msg =~ s/\$zipcord/$zipcord/g;
	$msg =~ s/\$address/$address/g;
	$msg =~ s/\$tel/$tel/g;
	$msg =~ s/\$fullname/$fullname/g;
	$msg =~ s/\$familyname/$familyname/g;
	$msg =~ s/\$brthday/$brthday/g;
	$msg =~ s/\$user/$user/g;
	$msg =~ s/\$brother/$brother/g;
	$msg =~ s/\$request/$request/g;
	$msg =~ s/\$exp/$exp/g;
	$msg =~ s/\$kgak/$kgak/g;
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
<CENTER><FONT SIZE="+3"><B><U>ご注文内容のご確認</U></B></FONT></CENTER>
         
         <BLOCKQUOTE>この画面は、ご注文内容をご確認頂くためのものです。内容に誤りがある場合は、ブラウザの「戻る」ボタンを押して「入力フォーム」から修正して下さい。これで宜しければ「注文」ボタンを押して下さい。</BLOCKQUOTE>
         
         <CENTER><B>ご注文内容</B><BR>
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
      <TD WIDTH=148>
         <P>ご依頼の内容</P>
      </TD>
      <TD>
         <P>山本翁の著書(電子本)の注文</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>合計お支払い金額</P>
      </TD>
      <TD>
         <P>\$kgak 円</P>
      </TD>
   </TR>
         </TABLE>
</CENTER>
         
         <BLOCKQUOTE>
            <B>ご確認が済みましたら</B><FONT COLOR="#FF0000"><B>下記「注文」ボタンを1回だけ押してご発注</B></FONT><B>ください。最近、メールアドレスの間違いが多いようです。メールアドレスをもう一度、ご確認下さい。<BR>
            なお、商品の性格上、これ以降のご注文の取り消しや返品は一切出来ませんので予めご了承下さい。(訪問販売法のクーリングオフは適用されません。）</B></BLOCKQUOTE>
         
         <CENTER>ご注文の訂正は、ブラウザの「戻る」で「入力フォーム」からやり直して下さい。</CENTER>
         
         <P><FORM ACTION="/~kazu-y/cgi_bin2/nn_mail.cgi" METHOD=POST>
            <P><INPUT TYPE="hidden" NAME="name" VALUE="\$name">
            <INPUT TYPE="hidden" NAME="email" VALUE="\$email">
            <INPUT TYPE="hidden" NAME="order1" VALUE="\$order1">
            <INPUT TYPE="hidden" NAME="order2" VALUE="">
            <INPUT TYPE="hidden" NAME="order3" VALUE="">
            <INPUT TYPE="hidden" NAME="zipcord" VALUE="">
            <INPUT TYPE="hidden" NAME="address" VALUE="">
            <INPUT TYPE="hidden" NAME="tel" VALUE="">
            <INPUT TYPE="hidden" NAME="fullname" VALUE="">
            <INPUT TYPE="hidden" NAME="familyname" VALUE="">
            <INPUT TYPE="hidden" NAME="brthday" VALUE="">
            <INPUT TYPE="hidden" NAME="user" VALUE="">
            <INPUT TYPE="hidden" NAME="brother" VALUE="">
            <INPUT TYPE="hidden" NAME="request" VALUE="">
            <INPUT TYPE="hidden" NAME="exp" VALUE="">
            <INPUT TYPE="hidden" NAME="kgak" VALUE="\$kgak">
            <CENTER><INPUT TYPE=submit NAME="送信" VALUE="注文"></CENTER>
         </FORM></P></CENTER>
      </TD>
   </TR>
</TABLE>
</P>
</BODY>
</HTML>

ORDER100
&jcode'convert(*msg, "sjis", "euc");
	$msg =~ s/\$name/$name/g;
	$msg =~ s/\$email/$email/g;
	$msg =~ s/\$order1/$order1/g;
	$msg =~ s/\$kgak/$kgak/g;
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
 <CENTER><FONT SIZE="+3"><B><U>ご注文内容のご確認</U></B></FONT></CENTER>
         
         <BLOCKQUOTE>この画面は、ご注文内容をご確認頂くためのものです。内容に誤りがある場合は、ブラウザの「戻る」ボタンを押して「入力フォーム」から修正して下さい。これで宜しければ「注文」ボタンを押して下さい。</BLOCKQUOTE>
         
         <CENTER><B>ご注文内容</B><BR>
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
      <TD WIDTH=148>
         <P>ご依頼の内容</P>
      </TD>
      <TD>
         <P>山本翁の著書(実本)の注文</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>書籍のご送付先</P>
      </TD>
      <TD>
         <P><TABLE BORDER=1>
            <TR>
               <TD WIDTH=55>
                  <P>郵便番号</P>
               </TD>
               <TD>
                  <P>\$zipcord</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=55>
                  <P>住所</P>
               </TD>
               <TD>
                  <P>\$address</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=55>
                  <P>お受取人</P>
               </TD>
               <TD>
                  <P>\$fullname</P>
               </TD>
            </TR>
         </TABLE>
         </P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>ご連絡先お電話番号</P>
      </TD>
      <TD>
         <P>\$tel</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>合計お支払い金額</P>
      </TD>
      <TD>
         <P>\$kgak 円</P>
      </TD>
   </TR>
         </TABLE>
</CENTER>
         
         <BLOCKQUOTE>
            <B>ご確認が済みましたら</B><FONT COLOR="#FF0000"><B>下記「注文」ボタンを1回だけ押してご発注</B></FONT><B>ください。<BR>
            なお、商品の性格上、これ以降のご注文の取り消しや返品は一切出来ませんので予めご了承下さい。(訪問販売法のクーリングオフは適用されません。）</B></BLOCKQUOTE>
         
         <CENTER>ご注文の訂正は、ブラウザの「戻る」で「入力フォーム」からやり直して下さい。</CENTER>
         
         <P><FORM ACTION="/~kazu-y/cgi_bin2/nn_mail.cgi" METHOD=POST>
            <P><INPUT TYPE="hidden" NAME="name" VALUE="\$name">
            <INPUT TYPE="hidden" NAME="email" VALUE="\$email">
            <INPUT TYPE="hidden" NAME="order1" VALUE="">
            <INPUT TYPE="hidden" NAME="order2" VALUE="\$order2">
            <INPUT TYPE="hidden" NAME="order3" VALUE="">
            <INPUT TYPE="hidden" NAME="zipcord" VALUE="\$zipcord">
            <INPUT TYPE="hidden" NAME="address" VALUE="\$address">
            <INPUT TYPE="hidden" NAME="tel" VALUE="\$tel">
            <INPUT TYPE="hidden" NAME="fullname" VALUE="\$fullname">
            <INPUT TYPE="hidden" NAME="familyname" VALUE="">
            <INPUT TYPE="hidden" NAME="brthday" VALUE="">
            <INPUT TYPE="hidden" NAME="user" VALUE="">
            <INPUT TYPE="hidden" NAME="brother" VALUE="">
            <INPUT TYPE="hidden" NAME="request" VALUE="">
            <INPUT TYPE="hidden" NAME="exp" VALUE="">
            <INPUT TYPE="hidden" NAME="kgak" VALUE="\$kgak">
            <CENTER><INPUT TYPE=submit NAME="送信" VALUE="注文"></CENTER>
         </FORM></P></CENTER>
      </TD>
   </TR>
</TABLE>
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
    $msg =~ s/\$kgak/$kgak/g;
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
<BODY BGCOLOR="#FFFFFF" BACKGROUND="/~kazu-y/image/wall.jpg">
<P><TABLE BORDER=0 CELLSPACING=0 CELLPADDING=0 WIDTH=640>
   <TR>
      <TD>
        <CENTER><FONT SIZE="+3"><B><U>ご注文内容のご確認</U></B></FONT></CENTER>
         
         <BLOCKQUOTE>この画面は、ご注文内容をご確認頂くためのものです。内容に誤りがある場合は、ブラウザの「戻る」ボタンを押して「入力フォーム」から修正して下さい。これで宜しければ「注文」ボタンを押して下さい。</BLOCKQUOTE>
         
         <CENTER><B>ご注文内容</B><BR>
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
      <TD WIDTH=148>
         <P>ご依頼の内容</P>
      </TD>
      <TD>
         <P>新生児の命名依頼</P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>ご依頼主さまの情報<BR>
         (お急ぎの方のみ)</P>
      </TD>
      <TD>
         <P><TABLE BORDER=1>
            <TR>
               <TD WIDTH=64>
                  <P>郵便番号</P>
               </TD>
               <TD>
                  <P>\$zipcord</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=64>
                  <P>住所</P>
               </TD>
               <TD>
                  <P>\$address</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=64>
                  <P>お電話番号</P>
               </TD>
               <TD>
                  <P>\$tel</P>
               </TD>
            </TR>
         </TABLE>
         </P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>新生児の命名依頼</P>
      </TD>
      <TD>
         <P><TABLE BORDER=1>
            <TR>
               <TD WIDTH=90>
                  <P>姓(苗字)</P>
               </TD>
               <TD>
                  <P>\$familyname</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=90>
                  <P>出生日(予定日)</P>
               </TD>
               <TD>
                  <P>\$brthday</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=90>
                  <P>過去のご依頼</P>
               </TD>
               <TD>
                  <P>\$user</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=90>
                  <P>ご兄弟のお名前</P>
               </TD>
               <TD>
                  <P>\$brother</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=90>
                  <P>ご要望事項</P>
               </TD>
               <TD>
                  <P>\$request</P>
               </TD>
            </TR>
            <TR>
               <TD WIDTH=90>
                  <P>特記事項</P>
               </TD>
               <TD>
                  <P>\$exp</P>
               </TD>
            </TR>
         </TABLE>
         </P>
      </TD>
   </TR>
   <TR>
      <TD WIDTH=148>
         <P>合計お支払い金額</P>
      </TD>
      <TD>
         <P>\$kgak 円</P>
      </TD>
   </TR>
         </TABLE>
</CENTER>
         
         <BLOCKQUOTE>
            <B>ご確認が済みましたら</B><FONT COLOR="#FF0000"><B>下記「注文」ボタンを1回だけ押してご発注</B></FONT><B>ください。最近、メールアドレスの間違いが多いようです。メールアドレスをもう一度、ご確認下さい。<BR>
            なお、商品の性格上、これ以降のご注文の取り消しや返品は一切出来ませんので予めご了承下さい。(訪問販売法のクーリングオフは適用されません。）</B></BLOCKQUOTE>
         
         <CENTER>ご注文の訂正は、ブラウザの「戻る」で「入力フォーム」からやり直して下さい。</CENTER>
         
         <P><FORM ACTION="/~kazu-y/cgi_bin2/nn_mail.cgi" METHOD=POST>
            <P><INPUT TYPE="hidden" NAME="name" VALUE="\$name">
            <INPUT TYPE="hidden" NAME="email" VALUE="\$email">
            <INPUT TYPE="hidden" NAME="order1" VALUE="">
            <INPUT TYPE="hidden" NAME="order2" VALUE="">
            <INPUT TYPE="hidden" NAME="order3" VALUE="\$order3">
            <INPUT TYPE="hidden" NAME="zipcord" VALUE="\$zipcord">
            <INPUT TYPE="hidden" NAME="address" VALUE="\$address">
            <INPUT TYPE="hidden" NAME="tel" VALUE="\$tel">
            <INPUT TYPE="hidden" NAME="fullname" VALUE="">
            <INPUT TYPE="hidden" NAME="familyname" VALUE="\$familyname">
            <INPUT TYPE="hidden" NAME="brthday" VALUE="\$brthday">
            <INPUT TYPE="hidden" NAME="user" VALUE="\$user">
            <INPUT TYPE="hidden" NAME="brother" VALUE="\$brother">
            <INPUT TYPE="hidden" NAME="request" VALUE="\$request">
            <INPUT TYPE="hidden" NAME="exp" VALUE="\$exp">
            <INPUT TYPE="hidden" NAME="kgak" VALUE="\$kgak">
            <CENTER><INPUT TYPE=submit NAME="送信" VALUE="注文"></CENTER>
         </FORM></P></CENTER>
      </TD>
   </TR>
</TABLE>
</P>
</BODY>
</HTML>

ORDER003
&jcode'convert(*msg, "sjis", "euc");
	$msg =~ s/\$name/$name/g;
	$msg =~ s/\$email/$email/g;	
	$msg =~ s/\$order3/$order3/g;	
	$msg =~ s/\$zipcord/$zipcord/g;
	$msg =~ s/\$address/$address/g;
	$msg =~ s/\$tel/$tel/g;
	$msg =~ s/\$familyname/$familyname/g;
	$msg =~ s/\$brthday/$brthday/g;
	$msg =~ s/\$user/$user/g;
	$msg =~ s/\$brother/$brother/g;
	$msg =~ s/\$request/$request/g;
	$msg =~ s/\$exp/$exp/g;
	$msg =~ s/\$kgak/$kgak/g;
	print $msg;
}
__end__
