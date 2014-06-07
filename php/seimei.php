<?php
class Seimei {
	
	public $sei;
	public $mei;

	public $tenkaku;
	public $chikaku;
	public $gaikaku;
	public $soukaku;
	public $seikaku;
	public $kenkou;
	
	public $kanji;
	
	private $tenshimo;
	private $jinshimo;
	private $chishimo;
	
	function Seimei() {
		$this->kanji = Array();
		$in = fopen("./kanji.dat", "r");
		
		$i = 1;
		while (!feof($in)) {
			$line = fgets($in);
			for ($j = 0; $j < mb_strlen($line); $j++) {
				$c = mb_substr($line, $j, 1);
				$this->kanji[$c] = $i;
			}
			$i++;
			if ($i > 31) {
				$i = 1;
			}
		}
		fclose($kanji);
	}
	
	function kakusu ($sei, $mei) {
		mb_regex_encoding("UTF-8");
		$this->sei = $sei;
		$this->mei = $mei;

		// 々ゝ仝の処理
		$sei = preg_replace("/(.)(々ゝ仝)/u", "$1$1", $sei);
		$mei = preg_replace("/(.)(々ゝ仝)/u", "$1$1", $mei);

		// 天画・人画・地画・外画・総画の算出(結構ややこしい)
		$this->tenkaku = 0;
		$this->chikaku = 0;
		$this->gaikaku = 0;
		$this->soukaku = 0;
		$error = Array();
		
		// 天画の算出
		for ($i = 0; $i < mb_strlen($sei); $i++) {
			$c = mb_substr($sei, $i, 1);
			$k = $this->kanji[$c];
			if ($k == 0) {
				push($error, $c);
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
		
		# 人画の算出
		$this->jinkaku = $this->kanji[mb_substr($sei, mb_strlen($sei)-1, 1)] + $this->kanji[mb_substr(mei, 0, 1)];
		
		# 地画の算出
		for ($i = 0; $i < mb_strlen($mei); $i++) {
			$c = mb_substr($sei, $i, 1);
			$k = $this->kanji[$c];
			if ($k == 0) {
				push($error, $c);
			} else {
				$this->chikaku += $k;
			}
		}
		
		# 一文字名の処理
		if (mb_strlen($mei) == 1) {
			$this->chikaku++; // 一画借りる
			$this->gaikaku++;
			$this->soukaku--; // 一画返す
		}
		
		// 総画・外画の算出
		$this->soukaku += $this->tenkaku + $this->chikaku;
		$this->gaikaku += $this->soukaku - $this->jinkaku;
		
		// オーバーフロー処理 - ちなみに > 81は間違いではない。
		if ($this->tenkaku > 81) {
			$this->tenkaku %= 80;
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
	
	private function f($i) {
		$i += $i % 2;
		$i /= 2;
		if ($i == 0) {
			$i = 5;
		}
		$i -= 1;
		return($i);
	}
}
