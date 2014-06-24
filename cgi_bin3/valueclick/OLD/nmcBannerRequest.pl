package nmcBannerRequest;

        # 初期設定
#	print "Version ".$]."\n";
#	if ($] >= 5 ){
        	use Socket;
#	}else{
#        	require "./sockets.pl";
#	}

sub BannerRequest{
	local ($S,$SiteId,$port,$host,$url,$ent,$output,$BlankCnt);
	$SIG{'ALRM'} = 'getaralm';
        $SiteId = $_[0];
        $S = "SOCK";
        # 広告配信サーバーの設定
        $host = "jaguar.mobileclick.ne.jp";
        $port = 80;
	#配信CGIの指定
	$url = "/cgi-bin/DealBanners.cgi"."?".$SiteId;
        socket($S,PF_INET,SOCK_STREAM,getprotobyname('tcp')) || return "socket NG<BR>\n";
        $port = getservbyname($port,'tcp') unless $port =~ /^\d+/;
        $ent = sockaddr_in($port,inet_aton($host));
	alarm 3;
        connect($S,$ent) || return "Connect NG<BR>\n";
	alarm 0;
        select(SOCK); $| = 1; select(STDOUT);
        SendString(<<END);

GET $url HTTP/1.0
Accept: */*
User-Agent: $Env{HTTP_USER_AGENT}

END

        # 出力結果を格納する
        local $output= "";
 	local $BlankCnt = 0;
        local $read_bits='';
        vec($read_bits,fileno(SOCK),1)=1;
	#TimeOutの設定	1sec
        select ($read_bits,undef,undef,1);
        if (vec($read_bits,fileno(SOCK),1) == 0 ) {
                return "";
        }
        while(<$S>){
		if ($BlankCnt == 1){
               		$output .=$_;
		}
		local $CrLf = pack "cc" ,13,10;
		if ($_ eq $CrLf && $BlankCnt == 0){
			$BlankCnt = 1;
		}
        }
	return $output;

}

sub SendString
{
        local($_) = @_;
        s/([^\r])\n/$1\r\n/g;
        print SOCK;
}
sub getaralm
{
}
1;
