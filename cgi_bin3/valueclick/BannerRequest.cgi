#!/usr/local/bin/perl
use strict;use mc3BannerRequest;

# 設定ファイルへの相対パス
my $pf='mc3_pref.txt';

my ($pg,$fl,$to,$bn);
open(PF,$pf);
while(<PF>){
if(m/^\#/){next;}s/\#.*$//;
if(m/^\s*PageID\s+(MC\d{7})\s$/){$pg=$1;}
if(/(\d+)/){$to=$1;}}
if($pg&&$to){$bn=BannerRequest($pg,$to);}
elsif($pg&&!$to){$bn=BannerRequest($pg);}
print "Content-Type: text/plain\n\n";
print BannerRequest($pg);
close(IN);close(PF);
exit;
