package dclick_perl;

use Socket;

sub dclick{
	$SIG{ALRM}= sub{die "timeout"};
	eval{ 
		alarm(3);
		$rc2 = dclick_try($_[0],$_[1]);
		alarm(0);
	};
	if($@){
		if($@ =~ /timeout/){
			return "";
		} else {
			alarm(0);
			die;
		}
	}
	@rc3 = split("\n",$rc2);
	return @rc3;
}
sub dclick_try{
	$serverurl ="i-mode.dclick.jp";
	$id = $_[0];
	$number = $_[1];
	if(!$number){$number = 1;}
	
	$port = 80;
	$port = getservbyname($port,'tcp') unless $port =~ /^\d+/;
	$iaddr = inet_aton("$serverurl")
	        or die "$serverurlは存在しないホストです。\n";
	$sock_addr = pack_sockaddr_in($port,$iaddr);
	socket(SOCKET,PF_INET,SOCK_STREAM,0)
	        or die "ソケットを生成できません。\n";
	connect(SOCKET,$sock_addr)
	        or die "$serverurlのポート$portに接続できません。\n";
	select(SOCKET); $|=1; select(STDOUT);
	print SOCKET "GET http://$serverurl/pv.php?id=$id&number=$number HTTP/1.0\r\n\r\n";
	
	while (<SOCKET>){
	    m/^\r\n$/ and last;
	}
	
	while (<SOCKET>){
	    $rc2 .= $_;
	}

	return $rc2;
}
1;
