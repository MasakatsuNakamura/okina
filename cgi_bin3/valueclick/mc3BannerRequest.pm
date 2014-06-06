package mc3BannerRequest;
use strict;
use vars qw(@ISA @EXPORT);
use Exporter;
@ISA = qw(Exporter);
@EXPORT = qw(BannerRequest);

use Socket;

sub TryBannerRequest{
    my $page_id = $_[0];
    my $host = "deliv.mobileclick.ne.jp";
    socket(DLV,PF_INET,SOCK_STREAM,getprotobyname('tcp')) || return "";
    my $dlv_addr = sockaddr_in(80,inet_aton($host));
    connect(DLV,$dlv_addr) || return "";
    select(DLV); $| = 1; select(STDOUT);
    SendString(<<END);
GET /$page_id HTTP/1.0
Accept: */*
User-Agent: $ENV{'HTTP_USER_AGENT'}
Server-Name: $ENV{'SERVER_NAME'}
Request-Uri: $ENV{'REQUEST_URI'}
Remote-Addr: $ENV{'REMOTE_ADDR'}
Server-Software: $ENV{'SERVER_SOFTWARE'}
Version: 3.00

END
    my $output= "";
    my $BlankCnt = 0;
    while(<DLV>){
        if ($BlankCnt == 1){
            $output .=$_;
        }
        my $CrLf = pack "cc" ,13,10;
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
    print DLV;
}

sub BannerRequest{
    my $btext = "";
    my $TIMEOUT = 2;
    if($_[1]){            
        $TIMEOUT=$_[1];
    }
    $SIG{ALRM} = sub{die "conntimeout"};
    eval{ 
        alarm($TIMEOUT);
        $btext = TryBannerRequest($_[0]);
        alarm(0);
    };
    if($@){
        if($@ =~ /conntimeout/){
            return "";
        }else{
            alarm(0);
            die;
        }
    }
    return $btext;
}
1;
