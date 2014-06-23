#!/usr/local/bin/perl
open(KANJI, "./kanji.dat") || die;
$i = 0;
while (<KANJI>) {
	$kakusu[$i++] = $_;
}
close(KANJI);

sub kakusu {
        local($kanji) = @_;
        local($i);
#        if ($kanji =~ /[0-9][0-9]/) {
#                return($kanji);
#        };
        LOOPEND:
        for ($i = 0; $i < 30; $i++) {
                for ($j = 0; $j < length($kakusu[$i]); $j += 2) {
                        if (substr($kakusu[$i], $j, 2) eq $kanji) {
                                last LOOPEND;
                        }
                }
        }
        $i++;
        $i = 0 if($i == 31);
        $i;
}

1;
