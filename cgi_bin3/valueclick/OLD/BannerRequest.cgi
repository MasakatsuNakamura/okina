#!/usr/local/bin/perl

require "./nmcBannerRequest.pl";
#use nmcBannerRequest;
$banner=&nmcBannerRequest'BannerRequest("hsm002750");

print "Content-type: text/html\n\n";
print $banner;
