<?php
require 'reii.php';
require 'kenkou.php';
require 'seikaku.php';

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
	
	private $kanji;
	
	private $tenshimo;
	private $jinshimo;
	private $chishimo;
	
	function Seimei() {
		$this->kanji = Array();
		$in = fopen("./kanji.dat", "r");
		
		$i = 0;
		while (!feof($in)) {
			if ($i++ > 31) {
				$i = 1;
			}
			$line = fgets($in);
			for ($j = 0; $j < mb_strlen($line, "utf-8"); $j++) {
				$c = mb_substr($line, $j, 1, "utf-8");
				$this->kanji[$c] = $i;
			}
		}
		fclose($in);
	}
	
	function kakusu ($sei, $mei, $sex, $marry, $over40) {
		mb_regex_encoding("UTF-8");
		$this->sei = $sei;
		$this->mei = $mei;
		$this->sex = $sex;
		$this->marry = $marry;
		$this->over40 = $over40;
		
		// 々ゝ仝の処理
		$sei = preg_replace("/(.)(々ゝ仝)/u", "$1$1", $sei);
		$mei = preg_replace("/(.)(々ゝ仝)/u", "$1$1", $mei);

		// 天画・人画・地画・外画・総画の算出(結構ややこしい)
		$this->tenkaku = 0;
		$this->jinkaku = 0;
		$this->chikaku = 0;
		$this->error = Array();
		
		// 天画の算出
		for ($i = 0; $i < mb_strlen($sei, "utf-8"); $i++) {
			$c = mb_substr($sei, $i, 1, "utf-8");
			$k = $this->kanji[$c];
			if ($k == 0) {
				push($this->error, $c);
			} else {
				$this->tenkaku += $k;
			}
		}
		
		// 一文字姓の処理
		if (mb_strlen($sei) == 1) {
			$this->tenkaku++; // 一画借りる
			$this->gaikaku++;
			$this->soukaku--; // 一画返す
		}
		
		// 人画の算出
		$this->jinkaku = $this->kanji[mb_substr($sei, mb_strlen($sei, "utf-8")-1, 1, "utf-8")]
						 + $this->kanji[mb_substr($mei, 0, 1, "utf-8")];
		
		// 地画の算出
		for ($i = 0; $i < mb_strlen($mei, "utf-8"); $i++) {
			$c = mb_substr($mei, $i, 1, "utf-8");
			$k = $this->kanji[$c];
			if ($k == 0) {
				push($this->error, $c);
			} else {
				$this->chikaku += $k;
			}
		}
		
		// 一文字名の処理
		if (mb_strlen($mei) == 1) {
			$this->chikaku++; // 一画借りる
			$this->gaikaku++;
			$this->soukaku--; // 一画返す
		}
		
		// 総画・外画の算出
		$this->soukaku = $this->tenkaku + $this->chikaku;
		$this->gaikaku = $this->soukaku - $this->jinkaku;
		
		// オーバーフロー処理 - ちなみに > 81は間違いではない。
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
		
		// 天画・人画・地画の下一桁の算出(10で割った余りを取るだけ)
		$this->tenshimo = $this->tenkaku % 10;
		$this->jinshimo = $this->jinkaku % 10;
		$this->chishimo = $this->chikaku % 10;
		
		// 性格診断の準備
		$this->seikaku = $this->jinshimo; //人画の下一桁で決まる

		// 陰陽五行のシリアル番号の算出(詳しくはkenkou.phpを参照)
		$this->kenkou = $this->f($this->tenshimo) * 25 + $this->f($this->jinshimo) * 5 + $this->f($this->chishimo);
	}
	
	public function mongon ($category) {
		mb_regex_encoding("UTF-8");
		// 占い結果(文言)の出力
		$reii = New Reii();
		$kenkou = New Kenkou();
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
