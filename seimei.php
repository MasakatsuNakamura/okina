<?php
Class Seimei {
	
	public $sei;
	public $mei;
	public $sex;
	public $marry;
	public $over40;
	
	public $tenkaku;
	public $jinkaku;
	public $chikaku;
	public $gaikaku;
	public $soukaku;
	
	public $seikaku;
	public $kenkou;
	
	public $error;
	
	private $sei1;
	private $sei2;
	private $tenshimo;
	private $jinshimo;
	private $chishimo;
	
	function meimei ($sex) {
		$meimei = New Meimei();
		return($meimei->getNewName($this->sei1, $this->sei2, $sex));
	}
	
	// $B2h?t7W;;(B
	function shindan ($sei, $mei, $sex, $marry, $over40) {
		mb_regex_encoding("UTF-8");
		$this->sei = $sei;
		$this->mei = $mei;
		$this->sex = $sex;
		$this->marry = $marry;
		$this->over40 = $over40;

		$kanji = New Kanji();
		
		$this->sei1 = $kanji->kakusu(mb_substr($this->sei, 0, 1, "utf-8"));
		$this->sei2 = $kanji->kakusu(mb_substr($this->sei, mb_strlen($this->sei, "utf-8") - 1, 1, "utf-8"));
		
		// $B!9!5!8$N=hM}(B
		$sei = preg_replace("/(.)($B!9!5!8(B)/u", "$1$1", $sei);
		$mei = preg_replace("/(.)($B!9!5!8(B)/u", "$1$1", $mei);
		
		// $BE72h!&?M2h!&CO2h!&302h!&Am2h$N;;=P(B($B7k9=$d$d$3$7$$(B)
		$this->tenkaku = 0;
		$this->jinkaku = 0;
		$this->chikaku = 0;
		$this->error = Array();
		
		// $BE72h$N;;=P(B
		for ($i = 0; $i < mb_strlen($sei, "utf-8"); $i++) {
			$c = mb_substr($sei, $i, 1, "utf-8");
			$k = $kanji->kakusu($c);
			if ($k == 0) {
				push($this->error, $c);
			} else {
				$this->tenkaku += $k;
			}
		}
		
		// $B0lJ8;z@+$N=hM}(B
		if (mb_strlen($sei) == 1) {
			$this->tenkaku++; // $B0l2h<Z$j$k(B
			$this->gaikaku++;
			$this->soukaku--; // $B0l2hJV$9(B
		}
		
		// $B?M2h$N;;=P(B
		$this->jinkaku = $kanji->kakusu(mb_substr($sei, mb_strlen($sei, "utf-8")-1, 1, "utf-8"))
					   + $kanji->kakusu(mb_substr($mei, 0, 1, "utf-8"));
		
		// $BCO2h$N;;=P(B
		for ($i = 0; $i < mb_strlen($mei, "utf-8"); $i++) {
			$c = mb_substr($mei, $i, 1, "utf-8");
			$k = $kanji->kakusu($c);
			if ($k == 0) {
				push($this->error, $c);
			} else {
				$this->chikaku += $k;
			}
		}
		
		// $B0lJ8;zL>$N=hM}(B
		if (mb_strlen($mei) == 1) {
			$this->chikaku++; // $B0l2h<Z$j$k(B
			$this->gaikaku++;
			$this->soukaku--; // $B0l2hJV$9(B
		}
		
		// $BAm2h!&302h$N;;=P(B
		$this->soukaku = $this->tenkaku + $this->chikaku;
		$this->gaikaku = $this->soukaku - $this->jinkaku;
		
		// $B%*!<%P!<%U%m!<=hM}(B - $B$A$J$_$K(B > 81$B$O4V0c$$$G$O$J$$!#(B
		if ($this->tenkaku > 81) {
			$this->tenkaku %= 80;
		}
		if ($this->jinkaku > 81) {
			$this->jinkaku %= 80;
		}
		if ($this->chikaku > 81) {
			$this->chikaku %= 80;
		}
		if ($this->gaikaku > 81) {
			$this->gaikaku %= 80;
		}
		if ($this->soukaku > 81) {
			$this->soukaku %= 80;
		}
		
		// $BE72h!&?M2h!&CO2h$N2<0l7e$N;;=P(B(10$B$G3d$C$?M>$j$r<h$k$@$1(B)
		$this->tenshimo = $this->tenkaku % 10;
		$this->jinshimo = $this->jinkaku % 10;
		$this->chishimo = $this->chikaku % 10;
		
		// $B@-3J?GCG$N=`Hw(B
		$this->seikaku = $this->jinshimo; //$B?M2h$N2<0l7e$G7h$^$k(B

		// $B1"M[8^9T$N%7%j%"%kHV9f$N;;=P(B($B>\$7$/$O(Bkenkou.php$B$r;2>H(B)
		$this->kenkou = $this->f($this->tenshimo) * 25 + $this->f($this->jinshimo) * 5 + $this->f($this->chishimo);
	}
	
	// $B@j$$7k2L(B($BJ88@(B)$B$N=PNO(B
	public function mongon ($category) {
		mb_regex_encoding("UTF-8");
		// $B?t$NNn0LJ88@$N=i4|2=(B
		$reii = New Reii();
		// $B7r9/J88@$N=i4|2=(B
		$kenkou = New Kenkou();
		// $B@-3JJ88@$N=i4|2=(B
		$seikaku = New Seikaku();
		
		switch ($category) {

			case 'tenkaku':
				$mongon = $reii->mongon[$this->tenkaku];
				break;
			
			case 'chikaku':
				$mongon = $reii->mongon[$this->chikaku];
				break;
			
			case 'gaikaku':
				$mongon = $reii->mongon[$this->gaikaku];
				break;
			
			case 'soukaku':
				$mongon = $reii->mongon[$this->soukaku];
				break;
			
			case 'jinkaku':
				$mongon = $reii->mongon[$this->jinkaku];
				break;
			
			case 'seikaku':
				$mongon = $seikaku->mongon[$this->seikaku];
				break;
			
			case 'kenkou':
				$mongon = $kenkou->mongon[$this->kenkou];
				break;

			default:
		}
		if ($this->sex != "female") {
			$mongon = preg_replace("/\+w.*-w/u", "", $mongon);
		}
		if ($this->sex != "male") {
			$mongon = preg_replace("/\+m.*-m/u", "", $mongon);
		}
		if ($this->marry != "yes") {
			$mongon = preg_replace("/\+k.*-k/u", "", $mongon);
		}
		if ($this->marry != "no") {
			$mongon = preg_replace("/\+u.*-u/u", "", $mongon);
		}
		if ($category != "jinkaku") {
			$mongon = preg_replace("/\+j.*-j/u", "", $mongon);
		}
		if ($category != "soukaku") {
			$mongon = preg_replace("/\+s.*-s/u", "", $mongon);
		}
		if ($category != "gaikaku") {
			$mongon = preg_replace("/\+o.*-o/u", "", $mongon);
		}
		if ($this->chikaku != 11) {
			$mongon = preg_replace("/\+e.*-e/u", "", $mongon);
		}
		if ($this->jinkaku != 26) {
			$mongon = preg_replace("/\+t.*-t/u", "", $mongon);
		}
		if ($this->jinkaku != 10 && $this->jinkaku != 20) {
			$mongon = preg_replace("/\+g.*-g/u", "", $mongon);
		}
		$mongon = preg_replace("/[\-\+][a-z]/u", "", $mongon);
		
		return($mongon);
	}
	
	private function f($i) {
		$i += $i % 2;
		$i = (int)($i / 2);
		if ($i == 0) {
			$i = 5;
		}
		$i -= 1;
		return($i);
	}
}
?>
