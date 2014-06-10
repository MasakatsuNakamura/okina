<?php
Class Meimei
{
	private $meimei;
	
	public function getNewName($sei1, $sei2, $sex) {
		$key = $sei1 . "-" . $sei2 . "-" . $sex;
		if (array_key_exists($key, $baby)) {
			return ($meimei[$key]);
		} else {
			return ('');
		}
	}
	
	public function NewName() {
		$meimei = Array(
			"1-5-M" => "一功=かずのり,乙由=たかゆき,一巨=かずお,一平=いっぺい,一弘=かずひろ,一矢=かずや,一史=かずふみ",
			"1-6-M" => "一臣=かずおみ,一好=かずよし,一光=かずみつ,一匡=かずまさ,一亘=かずのぶ",
			"1-7-M" => "一宏=かずひろ,一亨=かずあき,一志=かずし,一成=かずなり,一佑=いちすけ,一良=かずよし",
			"1-12-M" => "一雄=かずお,一清=いっせい,一博=かずひろ,一淳=かずあき,一勝=かずまさ,一理=かずのり",
			"1-12-F" => "一恵=かずえ,一深=かずみ,一央里=かおり,一保子=かほこ,一由希=ちゆき",
			"1-14-M" => "一嘉=かずひろ,一瑛=かずあき,一綺=かずき,一誠=いっせい,一郎=いちろう",
			"1-14-F" => "一実=かずみ,一華=かずか,一寿=ちず,一奈衣=かなえ,一由紀=ちゆき",
			"1-15-M" => "一葵=かずき,一賢=かずのり,一慶=かずよし,一摩=かずま,一諒=かずあき,一広=かずひろ",
			"1-15-F" => "一慧=かずえ,一葉=かずよ,一輪=いちわ,一嫁=かずか,一里亜=いちりあ",
			"1-16-M" => "一憲=かずのり,一樹=かずき,一磨=かずま,一潤=かずひろ,一道=かずみち",
			"1-16-F" => "一樺=かずか,一蓉=いちよう,一澄=かすみ,一央梨=かおり,一江美=ちえみ",
			"1-17-M" => "一聡=かずあき,一弥=かずや,一陽=かずあき,一優=かずひろ,一斎=いちさい,一繁=かずしげ,一聡=かずあき",
			"1-17-F" => "一弥=かずみ,一霞=かずか,一声=かずな,一穂=いちほ,一央理=かおり",
			"11-2-M" => "健二=けんじ,悠力=ひさお,祥人=あきひと,英了=ひでのり,第人,悌人=だいと,第力,悌力=だいりき,了第,了悌=りょうだい",
			"11-2-F" => "茅乃=かやの,茄了=かすみ,毬乃=まりの,彩乃=あやの,雪乃=ゆきの,梅乃=うめの,梨乃=りの",
			"11-4-M" => "浩文=ひろふみ,英夫=ひでお,啓介=けいすけ,健仁=けんじ,祥太=しょうた,健介=けんすけ,敏元=としはる,爽太=そうた,英夫=ひでお,祥仁=あきひと,悠太=ゆうた,健夫=たけお,悠介=ゆうすけ,康仁=やすひと",
			"11-4-F" => "茅之=かやの,茉方=まみ,祥心・康心=やすみ,毬水=まりな,鹿月・茄月=かつき,敏方=としみ,海日=みはる,望仁=みさと,若之=よしの,彗方・苗水=えみ,笙心=ふえみ,那仁・那心=なみ,毬文=まりや,茅元・茅日=ちはる,海月=みつき,梅心=うめみ,麻友=まゆ",
			"11-5-M" => "章弘=あきひろ,英司=えいじ,崚平=りょうへい,浩由=ひろゆき,健史・健司=けんじ,偉巨=いお,彗布=えふ,浩史=ひろし・ひろふみ,爽平=そうへい,英生=ひでお,祥平=しょうへい,康弘=やすひろ,爽矢=そうや,敏弘=としひろ,健司=けんじ,彬弘=あきひろ,祥司・笙司=しょうじ,敏矢=としや,悠史=ゆうじ紳矢=しんや",
			"11-5-F" => "祥代=さちよ,御由=みゆき,茅令=ちはる,彗巨=えみ,規加=のりか,毬加=まりか,茄代=かよ,彗巨=えみ,梨加=りか,悠代=ひさよ,麻由・茉由=まゆ,麻央=まお,梨左=りさ",
			"11-6-M" => "紳伍・晨伍=しんご,英光=ひでみつ,悠吉=ゆうきち,敏臣=としおみ,英匡=ひでまさ,祥伍=しょうご,康光=やすひろ,紹吉=しょうきち,祥多=しょうた,章次=しょうじ,英亘=ひでのぶ,健吉=けんきち,浩光=ひろみつ,章光=あきひろ,英臣=ひでみつ,悠丞=ゆうすけ",
			"11-6-F" => "彩圭=さいか・あやか,麻冴=まさえ,茅衣=ちえ,那好=なみ,梨名=りな,麻吏=まり,苗名=えな,若衣=よしえ,梨圭=りか,麻伎=まき,毬名=まりな,麻伎=まき,梨圭=りか,祥衣=やすえ,悠伎=ゆうき,茉衣=まい,彗吏=えり,悠圭=ゆうか,悠好=ゆみ,悠吏=ゆり,悠巳子=ゆみこ",
			"11-7-M" => "祥宏=よしひろ,紳吾=しんご,国男=くにお,研志・健志=けんじ,笙吾・祥吾・爽吾・祥吾=しょうご,彗佑・彗助=けいすけ,健作=けんさく,悟志=さとし,彬宏・章宏=あきひろ,英良=ひでよし,健成=やすなり,悟志・敏伺=さとし,悟希・敏岐=さとき,浩志=ひろし・こうじ,英希=ひでき,健秀=やすひで,悌宏=やすひろ,英男=ひでお,健作=けんさく,悠助=ゆうすけ,敏良=としろう,悠吾=ゆうご,英作=えいさく,康志=やすし,祥男=よしお,敏宏=としひろ,紳吾=しんご,英作=えいさく,悠志=ゆうじ,彬宏=あきひろ,健佑=けんすけ",
			"11-7-F" => "麻李・茉李=まり,那甫・茄歩=なほ,彩江=あやえ,彗見=えみ,海邑=みさと,毬江=まりえ,梨佐=りさ,祥江=やすえ・あきえ,麻希・茉希=まき,茄甫・鹿歩=かほ,茅里=ちさと,苗李・彗里・彗李=えり,那歩=なほ,御希=みき,麻見=まみ,悠希=ゆうき,英里=えり,悠里=ゆり,梨甫・梨歩=りほ,茄甫=かほ,悠江=ひさえ",
			"11-10-M" => "彬洋=あきひろ,英哲=ひでのり,敏晋=としゆき,健剛=やすよし,浩晃=ひろあき,康晋=やすゆき,悠記=ゆうき",
			"11-12-M" => "康智=やすのり,英雄=ひでお,浩喜=ひろき,敏尊=としたか,章博=あきひろ,啓智=たかのり,啓晶=のぶあき,啓雄=たかお,啓博・崇博=たかひろ,祥雄=さちお・やすお,敏博=としひろ,章雄・彬雄=あきお,康晴=やすはる,英博=ひでひろ,悠喜=ゆうき,健翔=けんしょう,敏智=としのり,健雄=たけお,英晴=ひではる,祥博・章博=あきひろ,英晶=ひであき,崇晶=たかあき,国壱=くにかず,章智=あきのり,健晶=としあき,祥喬=よしたか,英智=ひでのり,祥智=あきのり,崇淳=たかあき,敏晴=としはる,康博=やすひろ,英喜=ひでき,健晴=たけはる,英喜=ひでゆき,敏博=としひろ,祥智=あきのり,英晶=ひであき,健勝=としかつ,康清=やすきよ,祥博=やすひろ,祥勝=よしかつ,敏理=としまさ,健一朗=けんいちろう,悠一朗=ゆういちろう",
			"12-13-M" => "浩暉=ひろき,敏琢=としたか,爽耶・爽椰=そうや,英脩=ひではる,康裕=やすひろ,英暉=ひでき,康琢=やすたか,敏椰=としや,彬裕・祥裕=あきひろ,祥聖=あきまさ,敏琢=としたか,康嵩・健琢・康琢=やすたか,研路=けんじ,英靖=ひでやす,崇義=たかよし,健嗣=けんじ,祥琢=よしたか,章義=あきのり,紳耶=しんや,敏裕=としひろ,英義=ひでよし,祥聖=よしまさ,健裕=たけひろ,紳耶=しんや,英聖=ひでまさ,敏耶=としや,英聖=ひでまさ,研裕=あきひろ,浩郁=ひろふみ,英琢=ひでたか,悠暉=ゆうき,健裕=たけひろ,章裕=あきひろ,悠耶・悠椰=ゆうや,悠渡=ゆうと,浩渡=ひろと,浩耶・浩椰=ひろや",
			"12-3-F" => "啓椰=けいや,啓愛=けいあい,啓郁=はるか,梨嵯・梨裟・梨嵯=りさ,毬椰・毬耶=まりや,茅聖=ちさと,鹿路=かろ,茉莉・麻莉=まり,麻耶=まや,那郁=ともか,雪会=ゆきえ,毬阿=まりあ,彩郁=あやか,苗莉=えり,麻裕=まゆ,茅愛=ちあき,鹿鈴=かりん,海裕=みゆ,茉裕=まゆ,麻暉=まき,彬郁=あやか,彗莉=えり,祥会=さちえ,梨郁=りか,麻幹=まみ,茉幹=まき,御鈴=みすず,梨紗子=りさこ,麻記子=まきこ,茄帆里=かほり,彗益子=みえこ",
			"11-14-M" => "彬嘉=あきひろ,彗輔=けいすけ,英鳳=ひでたか,敏郎=としろう,章嘉=あきひろ,健爾=けんじ,康滉=やすあき,敏鳳=としたか,彬嘉=あきひろ,爽輔=そうすけ,英暢=ひでのぶ,祥鳳=やすたか,敏郎=としろう,浩鳳=ひろたか,英嘉=ひでよし,健豪=かつとし,康誠=やすあき,英嘉=ひでひろ,笙瑚=しょうご,健造=けんぞう,健大朗=けんたろう,悠士朗=ゆうじろう",
			"11-14-F" => "彩華=あやか,麻綺=まき,那実=なみ,麻実=あさみ,彩華=さいか,彗梨子=えりこ,茉梨子=まりこ,那央美=なおみ",
			"11-18-M" => "悠太郎=ゆうたろう,康燿=やすてる,章礼=あきひろ,英爵=ひでたか,彗翼=けいすけ,常燿=のぶてる,研鎮=あきしげ,康礼=やすのり,章豊=あきひろ,英爵=ひでたか,悠翼=ゆうすけ",
			"11-20-M" => "教厳=ゆきひろ,英覚=ひであき,啓蔵=けいぞう,康宝=やすたけ,康厳=やすひろ,啓蔵=けいぞう,悠治朗=ゆうじろう,英重朗=えいじゅうろう,商治朗=しょうしろう,御紀朗=みきろう",
			"11-20-F" => "苑馨=そのか,麻宝=まほ,悠羅=ゆうら,紫穂子=しほこ,茉沙恵=まさえ,英理奈=えりな,茄於理=かおり",
			"11-21-M" => "健鉄=たけかね,英誉=ひでやす,祥誉=よしたか,康芸=やすのり,崇芸=たかのり",
			"11-24-M" => "英鷹=ひでたか,健鷹=やすたか,祥鷹=よしたか,敏鷹=としたか,悠鷹=ひさたか",
			"2-0-M" => "乃=おさむ,力=いさお・つとむ,丁=つよし,了=あきら・さとる",
			"2-3-F" => "了子=りょうこ,アキ,アミ,クミ,ナミ,マキ,マミ,ユキ,ルミ,ユミ,リサ,いよ,てつこ,としこ,とも,りえ,りか",
			"2-4-M" => "力夫=いさお,了介=りょうすけ,了太=りょうた,人仁=きよひと,了仁=のりひと",
			"2-4-F" => "人心=ひとみ,カホ,アイコ,アリス,アンナ,カンナ,カリン,スミレ,セリカ,ハルナ,マリア,ユカリ",
			"2-9-F" => "人美=ひとみ,了香=りょうか,乃吏子=のりこ",
			"2-11-M" => "力堂=りきどう,乃茂=のも,了国=りょうごく,人教=じんきょう,力朗=りきろう",
			"2-11-F" => "人参=ひとみ,乃梨=のり,了彗=すみえ",
			"2-13-M" => "力耶=りきや,人聖=きよまさ,了寛=あきひろ,力裕=りきひろ,了敬=あきのり",
			"2-14-M" => "二郎=じろう,了彰=のりあき,力寿=りきひさ,了輔=りょうすけ,了大朗=りょうたろう",
			"2-15-M" => "力広=りきひろ,丁徳=あつのり,了徳=あきのり,力太朗=りきたろう,了太朗=りょうたろう,了一郎=りょういちろう,丁輝=あつき",
			"2-15-F" => "了慧=あきえ,二葉=ふたば,乃理子=のりこ",
			"2-16-M" => "力暁=ちかあき,人達・人導=きよみち,了憲=あきのり,人勲=きよひろ,了篤=あきしげ,力憲=ちかのり,了都=あきひろ,力道=ちかみち・りきどう,人篤=きよしげ,人頼=ひとより,了磨=りょうま,人憲=きよのり,二陳=かずのり",
			"12-0-M" => "淳=あつし,智=まさる,雄=たけし,清=きよし,博=ひろし",
			"12-0-F" => "茜=あかね,恵=めぐみ,喜=ゆき,雅=みやび",
			"12-1-M" => "智一=ともかず,淳一=じゅんいち,翔一=しょういち,雄一=ゆういち",
			"12-3-M" => "雅也=まさや,雄大=ゆうだい,善久=よしひさ,博士=ひろし,雄也=ゆうや,雅大=まさひろ,勝久=かつひさ,恵士=さとし",
			"12-3-F" => "尊子=たかこ,翔子=しょうこ,喜子=よしこ・ゆきこ,雅子=まさこ,恵子=けいこ,博巳=ひろみ,晴巳=はるみ,尋巳=ひろみ,智巳=ともみ,恵巳=えみ,善女=よしめ,智子=ともこ,淳子=じゅんこ,智子=ともこ,翔子=しょうこ,雅巳=まさみ,淑子=よしこ",
			"12-4-M" => "博文=ひろふみ,智夫=ともお,雄介=ゆうすけ,勝仁=かつのり,翔太=しょうた,雅夫=まさお,善仁=よしまさ,雄夫=たかお,竣介=しゅんすけ,博斗=ひろと,雄文=たかふみ,喜夫=のぶお,理仁=まさひと,創太=そうた,善夫=よしお,恵介=けいすけ,雅仁=まさひと,雄太=ゆうた,雄介=ゆうすけ,喬太=きょうた,淳太・惇太=じゅんた,竣太=しゅんた,雅仁=まさのり",
			"12-4-F" => "雅之=まさの,智文=ちゆき,淑心=きよみ,尋水=ひろみ,雅文・雅心=まさみ,智方=ともみ,恵心=えみ,深日=みはる,恵文=えみ,智公=ちさと,雅文=まさや,智公=ちさと,寒月=かんげつ",
			"12-5-M" => "喬司=たかし,智生=ともお,雄弘=たけひろ,欽矢=きんや,衆央=ひろお,智弘=ともひろ,翔司=しょうじ,淳平=じゅんぺい,勝史=かつし",
			"12-5-F" => "恵生=やすよ・よしみ,智民・智未=ともみ,理加=りか,淑代=すみよ,雅代=まさよ,恵史=めぐみ,晴生=はるよ,博未・尋未=ひろみ,恵巨=えみ,雅未=まさみ,晴代=はるよ",
			"12-6-M" => "欽匡・喬匡=ただまさ,翔伍=しょうご,雄吉=ゆうきち,博光=ひろみつ,勝光・理光=まさひろ,博臣=ひろみつ,雄好=かつみ,博行=ひろゆき,雄冴=ゆうご,善吉=ぜんきち,理次=まさつぐ,博好=ひろよし,智匡=としまさ,雅光=まさひろ,雄伎=ゆうき,善好=よしみ,博臣=ひろお,椋冴=りょうご,椋光=りょうこう,椋臣=りょうじん",
			"12-6-F" => "理圭=りか,雅好=まさみ,恵名=えな,晴圭=はるか,理名・理字=りな,恵臣・恵好=えみ,晴名=はるな,恵吏=えり,智好=さとみ,善衣=よしえ,恵吏・理衣=りえ,智圭=ともか,斐冴=ひさえ,深冴=みさえ,雅衣=まさえ",
			"12-11-M" => "智浩=ともひろ,翔英=しょうえい,恵章・恵祥=しげあき,善崇=よしたか,雄浩=たけひろ,勝章=まさあき,善英=よしひで,善朗・恵朗・理朗・勝朗=よしろう,雄浩・理浩=たかひろ,理英=ただひで,理規=としき,理章=まさあき,晶英=あきひで,喬章=たかあき,智英=としひで,雄規=ゆうき,勝敏=まさとし,勝章=かつのり,博敏=ひろとし,勝浩・雅浩=まさひろ,尊章・喬彬=たかあき,博英=ひろひで,善浩=よしひろ,博章=ひろあき,理英=まさひで,晶浩=あきひろ,雄英=かずひで,勝敏=かつとし,翔悟=しょうご,欽浩=よしひろ,椋第,椋悌=りょうだい,翔第,翔悌=しょうだい,雄第,雄悌=ゆうだい,雄規=ゆうき,博朗=ひろお,善悠=よしひさ,博康=ひろやす",
			"12-12-M" => "雅喬=まさたか,恵晴=しげはる,理雄=まさお,智博=さとひろ,翔喜=しょうき,善雄=よしお,尋晶=ひろあき,雅博・理博=まさひろ,善智=よしのり,晴雄=はるお,勝博=かつひろ,尋喜=ひろゆき,恵智=しげのり,恵晶=よしあき,晴雄=はるお,恵喜=しげゆき,凱理=よしのり,勝智・雄智=かつのり,勝淳=かつあき,強善=かつよし,淳一朗=じゅんいちろう,翔一朗=しょういちろう",
			"12-12-F" => "智尋=ちひろ,理恵=りえ,博恵=ひろえ,視晴=みはる,深喜・深稀・証稀=みき,欽恵=よしえ,惟雅=ゆいが,茜媛=せんひめ,淑恵=よしえ,雅恵=まさえ,智晶=ちあき,須雅=すが,晴恵=はるえ,雅深=まさみ,喜恵=ゆきえ,智晴=ちはる,捺稀=なつき,恵理=えり,喜晴=きはる,雅恵=まさえ,淑恵=としえ,深喜=みき,晶恵=あきえ,喜美子=きみこ,斐加里=ひかり,恵里加=えりか,深由希=みゆき",
			"12-13-M" => "善琢=よしたか,雅耶・理揶=まさや,博聖=ひろまさ,翔耶=しょうや,雄義=たかよし,恵裕=としひろ,博義=ひろよし,理裕=ただひろ,博暉=ひろき,恵靖=しげやす,雄椰=ゆうや,椋耶=りょうや,智裕=ともひろ,善琢=よしたか,雄暉=ゆうき,晶暉=まさき,智郁=ともふみ,雅琢=まさたか,喜裕=よしひろ",
			"3-2-M" => "大人=ひろと,工人=ただひこ,久人=ひさひこ,丈人=たけひこ,大了=ひろあき,工了=ひろあき,久了=ひさのり,丈了=たけのり",
			"3-2-F" => "千乃=ゆきの,久乃=ひさの,エマ,サラ,ミカ,ミナ,ケイ,チカ,あい,あこ,えり,かこ,ちこ,みこ,ゆい,ゆう,ゆり,れい,よしの",
			"3-3-M" => "久也=ひさや,工也=たくや,久士=ひさし,丈士=たけし,丈大=たけひろ,大也=ひろや",
			"3-3-F" => "久子=ひさこ,夕子=ゆうこ,弓子=ゆみこ,エミ,サチ,チエ,ミキ,ミサ",
			"3-4-M" => "大介=だいすけ,工介=こうすけ,丈仁=たけひと,久夫=ひさお,大友=ひろとも",
			"3-4-F" => "千文=ちふみ,久方・久心・久水=くみ,エリカ,サヤカ,サユリ,チハル,モニカ",
			"3-5-M" => "久永=ひさのり,士司=ひとし,也正=ただまさ,大史=ひろふみ,丈史=たけし",
			"3-5-F" => "久代・久世=ひさよ,久未=ひさみ,千加=ちか,(カタカナで)エミリ,モニエ,ミチル,ミユキ,サトミ,タマエ,サオリ,サナエ,タカエ,エミコ,サチコ,サエコ,タミコ,ウタコ",
			"3-8-M" => "工汰=こうた,丈昌=たけまさ,久和=ひさかず,久尚・久直=ひさなお,千昌=ゆきまさ",
			"3-10-M" => "大祐=だいすけ,久哲・久記=ひさのり,丈師=たけし,大晃=ひろあき,三隼=みつとし,大育=ひろやす,工哲=ただのり,千恒=ゆきひさ,丈洋=たけひろ,久師=ひさし,凡晃=ひろあき,大朔=だいさく,工洋=ただひろ,千真=かずま,丈恒=たけひさ,大晋=ひろあき,工真=ただまさ,大起=だいき,大朔=だいさく,工晃=ただあき,久師=ひさみつ・ひさし",
			"3-10-F" => "大花=はるか・だいか,千洋=ちひろ,巳紗=みさ,三記=みき,千花=ちはる・ちか,小洋=こなみ,久益=くみ,千晃=ちあき,千紗=ちさ,千高=ちたか,三倭=みわ,小花=こはる,小記=さき,三洋=みなみ,巳記=みき,巳花=みか,千江子=ちえこ,三希子=みきこ,三佐子=みさこ,久良子=くみこ,巳佐子=みさこ,三矢加=さやか,久未代=くみよ",
			"3-12-M" => "大喜・大貴=だいき,工博=ただひろ,丈雅=とものり,久雄=ひさお,千博=ゆきひろ",
			"3-12-F" => "千晴=ちはる,千恵=ちえ,千尋=ちひろ,久恵=ひさえ,巳稀・巳喜=みき,千晶=ちあき,千智=ちさと,久深=くみ,小晴=こはる,久深=くみ,三也香=さやか,巳由希=みゆき,久美子=くみこ",
			"3-13-M" => "大暉=だいき,久耶=ひさや,士義=ただのり,丈寛=たけひろ,大聖・大勢=だいせい,大裕=だいすけ,丈耶=たけや,丈嗣=たけつぐ,久琢=ひさたか,久義=ひさよし",
			"3-13-F" => "千嵩=ちたか,千愛=ちあき,千聖=ちさと,千裕=ちひろ,巳暉=みき,久会=ひさえ,小鈴=こすず,巳嵯=みさ,千郁=ちふみ,久幹=くみ,千会=ちえ,三鈴=みすず,小暉=さき,小暉=さき,千敬・千裕=ちひろ,丈幹=ともみ,巳聖=みさと,千花子=ちかこ,三紗子=みさこ",
			"3-14-M" => "大輔=だいすけ,久鳳=ひさたか,士郎=しろう,大造=だいぞう,千寿=ゆきひろ",
			"3-14-F" => "小華=こはな,大華=だいか,千華=ちか,丸華=まろか,千彗子=ちえこ,久美加=くみか,三矢香=みやか,巳由紀=みゆき",
			"3-15-M" => "大輝・大毅・大葵=だいき,工諒=ただあき,久慶・久賢・久徳=ひさのり,凡徳=ひろのり,丈賢・丈徳=たけのり,久慶=ひさよし,千摩=かずま,千諒=ちあき",
			"3-15-F" => "千慧=ちえ,千奈見=ちなみ,久深子=くみこ,小於里=さおり,小侑里=さゆり,巳葉=みほ,千賢=ちさと,久慧=ひさえ,三有紀=みゆき,千名美=ちなみ",
			"3-18-M" => "大翼=だいすけ,久礼=ひさのり,丈鎮=ともしげ,凡豊=ひろと,工鎮=ただしげ,大鯉=だいり,千豊=ゆきひろ,凡爵=ひろたか",
			"3-21-M" => "大鉄=ひろとし,大誉=ひろたか,大覇=ひろはる,大芸=ひろのり,工誉=ただよし,工覇=ただはる,工芸=ただまさ,久芸=ひさのり",
			"3-21-F" => "小藤=こふじ,千鶴=ちづ,久美恵=くみえ,也須美=やすみ,小芸=さき",
			"13-2-M" => "暉人=てるひと,暉了=てるあき,郁人=ふみひと,靖了=やすあき,琢人=たくひこ,義人=よしひと,聖人=まさひと",
			"13-2-F" => "郁乃=あやの,聖乃=まさの,愛乃=ひでの,裕乃=ひろの,琢乃=たかの,鈴乃=すずの",
			"13-3-M" => "琢也=たくや,義久=よしひさ,嵩士=たかし,裕也=ゆうや,琢大=たかひろ,聖士=まさし,聖大=まさひろ,祐士=ゆうじ",
			"13-3-F" => "幹千=みゆき,嵯千・裟千=さち,会巳=えみ,阿巳=あみ,靖子=やすこ,愛子=あきこ・あいこ,聖子=せいこ,脩子=はるこ,裕子=ゆうこ,郁子=あやこ,琢子=たかこ,阿巳=あみ,裕巳=ゆみ",
			"13-4-M" => "琢文=たかふみ,敬太=けいた,督夫=よしお,裕介=ゆうすけ,聖元=まさはる,靖仁=やすひと,新月=しんげつ,郁夫=ふみお,琢仁=たかひと,頌太=しょうた,聖文=まさふみ,靖夫=やすお,脩介=しゅうすけ,裕太=ゆうた",
			"13-4-F" => "聖方・聖心=まさみ,愛心=ひでみ・なるみ,稚公・稚仁=ちさと,郁之=あやの,聖水=せいな,裕方=ゆみ,幹公=みく,裕公=ゆうこう,裕心・湧方=ゆうみ,敬之=ゆきの,聖水=せいな,幹公=みく",
			"13-5-M" => "靖生=やすお,琢巨=たくみ,聖司=せいじ,聖史=さとし,裕矢=ゆうや,義正=よしまさ,敬司=ひろし,琢生=たくお,靖弘=やすひろ,郁生=いくお,裕司=ゆうじ,琢外=たくと,脩平=しゅうへい,聖矢=せいや,嵩史=たかし",
			"13-5-F" => "愛巨・愛未・愛生=ひでみ,郁加=あやか,莉左=りさ,靖代=やすよ,稚央=ちひろ,聖加=せいか,照代=てるよ,裕未・裕巨=ゆみ,聖生=さとみ,裕加=ゆか・ゆうか,幹令=みはる,円加=まどか,会未=えみ,絹代=まさよ,照未=てるみ,鈴加=すずか,新玉=あらたま,愛加=あいか,幹加=みか,郁加=ふみか・あやか,路代=みちよ,聖代=まさよ,稚令=ちはる,阿未=あみ,睦史=むつみ,郁代=いくよ,聖加=せいか,愛代=ひでよ,阿由=あゆ,裕未=ゆみ,稚令=ちはる",
			"13-8-M" => "敬汰=けいた,義忠=よしただ,聖幸=まさゆき,琢於=たくお,郁明=ふみあき,靖忠=やすただ,裕幸=ひろゆき",
			"13-10-M" => "郁晃=ふみあき,靖晋=やすゆき,聖隼=まさとし,裕祐=ゆうすけ,聖晃=まさあき,琢紘=たかひろ,靖高=やすたか,裕哲・敬哲=ひろのり,嵩晃=たかあき,暉晋=てるゆき,靖祐=せいすけ,義晋=よしゆき,暉晃=てるあき,聖哲=まさのり,靖洋・靖紘=やすひろ,裕晋=ひろゆき,義洋=よしひろ,嵩祐=しゅうすけ,郁紘・郁洋=ふみひろ,義真=よしまさ,脩晃=のぶあき,寛記=ひろき,義晃=よしあき,敬真=ひろまさ,聖洋=まさよし・まさひろ,嵩芳=たかよし,嵩晃=たかあき,琢晋=たかゆき,義哲=よしのり,靖晃=やすあき,聖晋=まさゆき,裕恭=ひろやす,琢真=たくま,義恒=よしつね,靖洋=やすひろ",
			"13-11-M" => "琢浩=たかひろ,義彬=よしあき,聖英=まさひで,新悟=しんご,聖敏=まさとし,裕康・寛祥=ひろやす,義英=よしひで,靖浩=やすひろ,聖浩=まさひろ,裕章=ひろあき,靖敏=やすとし,義朗=よしろう,新朗=よしろう,琢朗=たくろう,稜悟=りょうご,稔英=としひで,歳浩=としひろ,郁浩=ふみひろ,暉章=てるあき,靖英=やすひで,新悟=しんご,脩悠=はるひさ",
			"13-11-F" => "郁鹿=あやか,聖那=せいな,裕梨=ゆり,嵯苗=さなえ,会麻=えま,裕鹿・裕茄=ゆうか,耶那=かな,聖茄・聖鹿=せいか,寛彗=ひろえ,愛茄=あいか,新那=にいな,聖慧=まさえ,絹苗=きぬえ,聖彗=さとえ,愛鹿=あきか,会梨=えり,暉彩=きさい,円茄=まどか,裟苗=さなえ,鈴茄・鈴鹿=すずか,裟茅=さち,郁彗=いくえ,稚彗=ちえ",
			"13-12-M" => "裕喬=ひろたか,郁雄=ふみお,琢博・嵩博=たかひろ,暉雅=てるまさ,琢間=たくま,裕智=ひろのり,靖淳=やすあき,郁雄=ふみお",
			"13-12-F" => "嵯智=さち,郁恵=いくえ,裕喜=ゆき・ゆうき,愛深=ひでみ,裟雅=さが,睦恵=ともえ,幹喜=みき,稚尋=ちひろ,裕理=ゆり,裕稀=ゆうき,郁恵=ふみえ,愛喜=あいき,会未里=えみり,嵯也香=さやか,詩央里=しおり,阿加里=あかり,裕加里=ゆかり,阿紀子=あきこ,暉美子=きみこ,会里加=えりか",
			"13-16-M" => "靖篤=やすしげ,琢勲=たかひろ,郁学=ふみひさ,裕樹=ゆうき,聖憲=まさかず",
			"4-0-M" => "元=はじめ,仁=ひさし・ひとし・ひろし,丹=あきら,大=ふとし,升=のぼる,允=まこと",
			"4-2-M" => "文力=ふみお,仁人・公人=きみひと,友了=ともあき,仁力=まさお,允人=よしひと",
			"4-2-F" => "文乃=あやの,巴乃=ともの,公乃=きみの,仁乃=まさの,丹乃=あかの",
			"4-3-M" => "友久=ともひさ,公久=きみひさ,文也=ひさや,元也=もとや,仁士=ひとし",
			"4-3-F" => "文子=あやこ,公子=きみこ,仁子=のりこ,友子=ゆうこ,巴子=ともこ",
			"4-4-M" => "公夫=きみお,元太=げんた,文太=ぶんた,友介=ゆうすけ,友太=ゆうた",
			"4-4-F" => "文水・文心=あやみ,允心=まさみ,巴心・巴水・友水・友心=ともみ,元心・元水=はるみ",
			"4-7-M" => "文宏=ふみひろ,心吾=しんご,友佑=ゆうすけ,仁志=ひとし,友秀=ともひで",
			"4-9-M" => "文彦=ふみひこ,仁亮=まさあき,太泰=ひろやす,太亮=ひろあき,仁哉=まさや,公治=きみはる,公紀=きみのり(こうき),巴彦=ともひこ,文哉=ふみや,友治=ゆうじ,元保=はるお,太保=ひろやす,仁治=まさはる,文秋=ふみあき",
			"4-9-F" => "公美=くみ,文香=あやか・ふみか,友紀=ゆき・ゆうき,心保=みほ,心紀=みき,方美=まさみ,仁美=ひとみ・ひろみ,友美・友皆・巴美・巴皆=ともみ,文音=あやね・あやか,友香=ともか,心春・方春・水春=みはる,水紀・心紀=みき,方保・心保=みほ,丹音=あかね,公香=きみか,丹音=あかね,公好子=くみこ,友吉子=ゆきこ",
			"4-11-M" => "允章=まさあき,文浩=ふみひろ,仁悠=ひろひさ,友英=ともひで,心悟=しんご,友悠=ともひさ,友章=ともあき,公悠=きみひさ,仁英=まさひで,仁英=まさひで",
			"4-11-F" => "文鹿=あやか・ふみか,仁那=にいな,巴彗=ともえ,巴茄=ともか,之彗=ゆきえ,水苗=みなえ,心雪=みゆき,公御=くみ,仁彗=きみえ,水那=みな,友梨=ゆり,心由妃=みゆき,友化里=ゆかり",
			"4-12-M" => "文雄=ふみお,公晴=きみはる,仁博=まさひろ,太勝=ひろのり,公博=きみひろ,仁理・仁智=まさのり,友晶=ともあき,文博=ふみひろ,友喜=ともき,元雄=はるお,公詞=こうじ,仁勝=まさかつ,友博=ともひろ",
			"4-12-F" => "巴恵=ともえ,心晴=みはる,心喜・心稀・方稀=みき,文恵=ふみえ,方淑=みすえ,公視=くみ,友喜=ゆうき,友雅=ゆうが,心賀=みか,月深=つきみ,水無=みな,友理=ゆり,公美子=くみこ,水由希=みゆき",
			"4-13-M" => "文郁=あやか・ふみか,文会=ふみえ,水鈴=みすず,心聖=みさと,友愛=ゆうあい,友郁=ともか,公会=きみえ,友会=ともえ,心鈴=みすず,水嵯=みさ,公未枝=くみえ,心友紀=みゆき,友里衣=ゆりえ",
			"4-14-M" => "文嘉=ふみひろ,友輔=ゆうすけ,仁郎=まさお,公造=こうぞう,友寿=ともかず",
			"4-14-F" => "文華・文嘉=あやか・ふみか,公実=くみ,心輔=みほ,友嘉=ともか・ゆうか,心温=みはる,仁華=のりか,友伽里=ゆかり",
			"4-19-M" => "文穏=ふみやす,方観=まさあき,友勧=ともゆき,友鏡=ともあき,元拡=もとひろ",
			"4-20-M" => "文蔵=ぶんぞう,友宝=ともたか,公継=まさつぐ,友治朗=ゆうじろう,文厳=ふみひろ,仁厳=まさひろ,太薫=ひろゆき,公蔵=こうぞう,文宝=ふみたか",
			"4-20-F" => "文馨=あやか・ふみか,心薫=みゆき,日佳理=ひかり,心沙恵=みさえ,公弥子=くみこ,友香梨・友佳理=ゆかり,心穂子=みほこ,友理枝=ゆりえ,水沙貴=みさき",
			"4-21-M" => "仁鉄=まさとし,文藤=ゆきひさ,友誉=とものり",
			"4-21-F" => "友香理・友佳莉=ゆかり,友里菜・友莉奈=ゆりな,友理香=ゆりか,心芸・水芸=みき,友芸=ゆうき",
			"14-0-M" => "暢=とおる,彰=あきら,寿=ひさし,豪=たけし,誠=まこと",
			"14-0-F" => "菖=あやめ,碧=みどり,綾=あや,嘉=よしみ,槙=こずえ,華=はな",
			"14-1-M" => "誠一=せいいち,慎一=しんいち,碩一=ひろかず,暢一=まさかず,瑛一=えいいち",
			"14-2-M" => "維力=しげお,維人=まさと,維了=まさのり,鳳力=たかお,暢人=まさひろ,誠了=まさあき",
			"14-2-F" => "綾乃=あやの,歌乃=うたの,寿乃=ひさの,華乃・温乃=はるの,瑛乃=あきの",
			"14-3-M" => "誠也=せいや,寿久=かずひさ,鳳士=たかし,慎也=しんや,誠大=まさひろ,嘉久=よしひさ",
			"14-3-F" => "華巳=はるみ,実千・誠千=みち,綾女=あやめ,綾子=あやこ,嘉子=よしこ,温子=あつこ",
			"14-4-M" => "鳳夫=たかお,暢仁=のぶひと,誠介=せいすけ,嘉元=よしゆき,颯太=りゅうた,嘉仁=よしひろ,",
			"14-7-M" => "慎吾=しんご,誠宏=まさひろ,鳳志=たかし,暢良=まさよし,綾佑=りょうすけ,豪男=たけお,誠志=さとし,嘉宏=よしひろ,誠佑=せいすけ,碩志=ひろし",
			"14-9-M" => "嘉紀=よしのり,碩重=ひろしげ,慎哉=しんや,綱彦=つねひこ,嘉彦=よしひこ,鳳亮=たかあき,維哉・暢哉=まさや,誠治=まさはる,実重=みつしげ,瑛彦=あきひこ,滉亮=ひろあき,嘉保=よしお,誠俊=まさとし,寿哉=かずや,滋治=しげはる,誠泰=まさひろ,誠哉=せいや,源治=もとはる,豪俊=かつとし,実重=みつしげ",
			"14-10-M" => "鳳晃=たかあき,嘉洋=よしひろ,豪哲=たけのり,嘉晋=よしゆき,誠高=まさたか,鳳洋・豪洸=たかひろ,嘉晃=よしあき,寿真=かずま,誠師=まさし,碩晃・嘉晃=ひろあき,暢晋=のぶゆき,実隼=みつとし,慎祐=しんすけ,誠哲=まさのり,慎真=よしまさ,実芳=みつよし,彰洋=あきひろ,鳳隼=たかとし,瑛紘=あきひろ,誠晋=まさゆき,寿真=かずま,誠祐=せいすけ,滋晃=しげあき,寿哲=ひさのり,碩起=ひろき,鳳哲=たかのり,誠洋=まさひろ,綾祐=りょうすけ",
			"14-10-F" => "実芳・実花=みか,誠花=せいか,華留・嘉留=かる,瑳記=さき,実紗=みさ,実記=みき,綾花・綺花=あやか,華花=はるか,嘉益=よしみ,福益=ふくみ,誠花=せいか,綾峰=あやね,華洋=かなみ,華留=かる,華玲,嘉玲,箇玲=かれい,実甫子=みほこ,緋呂子=ひろこ,瑛里子・瑛李子=えりこ,華歩子・華甫子=かほこ,瑳江子=さえこ,実希子=みきこ,実佐子=みさこ,寿良子=すみこ,寿未代=すみよ,綺久江=きくえ",
			"14-11-M" => "嘉浩=よしひろ,鳳章=たかあき,誠英=まさひで,実敏=みつとし,誠章=まさあき,鳳英=たかひで,嘉英=よしひで,鳳浩=たかひろ,嘉章=ひろあき,豪朗=たけお,鳳敏=たかとし,誠祥=まさあき,慎悟=しんご,嘉規=ひろき,嘉悠=よしひさ",
			"14-11-F" => "華那=かな・はるな,嘉彗=よしえ,実雪=みゆき,暢苗=のぶえ,誠彩=みさい,綾茄=あやか,実由妃=みゆき",
			"14-17-M" => "綾霞=あやか,華央理=かおり,寿美枝=すみえ,実紗江=みさえ,瑛里花=えりか",
			"14-18-M" => "誠翼=せいすけ,碩鎮=ひろしげ,滋礼=しげゆき,維鴻=まさひろ,維鎮=まさしげ,維礼=まさのり,維爵=しげたか,誠燿=まさてる,鳳礼=たかまさ,実豊=みつひろ,慎翼=しんすけ",
			"24-1-M" => "鷹一=よういち",
			"5-0-M" => "弘=ひろし,永=ひさし,玄=ひかる,正=ただし,巧=たくみ",
			"5-0-F" => "玄=はるか・ひかる,史=ふみ",
			"5-1-M" => "弘一,功一=こういち,永一=えいいち,玄一=げんいち,正一=まさかず,史一=ふみかず",
			"5-2-M" => "弘人=ひろひと,功人=のりひと,巨人・正人=まさと,玄人=はるひと,史人=ふみひと",
			"5-3-M" => "正也=まさや,由大=よしひろ・ゆうだい,央久=てるひさ,功士=あつし,叶久=やすひさ,由也=ゆうや,央大=ひろお,正士=まさし,永大=ひさお,玄大=はるお,正大=まさひろ,史大=ふみひろ",
			"5-3-F" => "弘巳=ひろみ,未久=みく,叶子=きょうこ,未己=みき,由子=よしこ・ゆうこ・ゆきこ",
			"5-6-M" => "正臣=まさおみ,由光=よしみつ,正好=まさよし,弘匡=ひろただ,央伎=ひろき",
			"5-6-F" => "加名=かな,史帆=しほ,玉衣=たまえ,未羽=みう,未帆=みほ,由妃=ゆき",
			"5-8-M" => "弘昌=ひろまさ,由汰=ゆうた,正幸=まさゆき,玄汰=げんた,由幸=よしゆき,正和=まさかず,生於=いくお,由知=よしのり,正汰=しょうた,永幸=ひさゆき,弘明・弘昂=ひろあき,弘昂=ひろあき,由汰=ゆうた,玄幸=のりゆき,玄武=のりたけ,永児=えいじ,正忠=まさただ,巨和=まさかず",
			"5-8-F" => "加奈=かな,由果=ゆか,未玖=みく,由枝=よしえ,未沙・生沙=みさ,正佳=せいか,由枝=ゆきえ,左季=さき",
			"5-10-M" => "弘晃=ひろあき,功晋=のりゆき,只祐=ただすけ,永哲=ひさのり,正洋=まさひろ,史晃=ふみあき,由晋=よしゆき,巨哲=まさのり",
			"5-10-F" => "史洋=みなみ,加留=かる,由記・由起=ゆき,巨花=みか,未紗・史紗=みさ,令花=はるか,巨記=みき,由真=ゆま,永花=のりか・えいか,白花=のりか,丙真=えま,加甫子=かほこ,左矢加=さやか",
			"5-11-M" => "正浩=まさひろ,弘章=ひろあき,永英=のりひで,充茂=みつしげ,由悠=よしひさ,由英=よしひで,永章=ひさあき,巨敏=まさとし",
			"5-11-F" => "由鹿・由茄=ゆか,加苗=かなえ,未那=みな,玉彗=たまえ,永茉=えま,巨那=みな,未茅=みち,正彗=まさえ,白雪=しらゆき,巨鹿=みか,加那=かな,由梨=ゆり,史彗=みえ,令苗=はるえ,令那=はるな,丙梨=えり",
			"5-12-M" => "功雄=いさお,由博=よしひろ,正晴=まさはる,正勝=まさかつ,弘喜=ひろき",
			"5-12-F" => "生恵=ゆきえ・いくえ,充喜・生喜・未喜・史喜・未稀=みき,史晴・巨晴・民晴=みはる,由理=ゆり,央恵=ひろえ,由惟=ゆい,左智=さち,末惟=まい,加淑=かすみ,正恵=まさえ,令恵=はるえ,史智・未智=みち,玉恵=たまえ,由喜・由稀=ゆき,充智=みさと,央恵=ひろえ,生淑=みすえ,永理=えり,加央里=かおり,永美子=えみこ,由美子=ゆみこ,史保子=みほこ,生由希=みゆき,永里加=えりか,加央里=かおり,由加里=ゆかり,左也香=さやか,史央里=しおり",
			"5-13-M" => "正暉=まさき,正義=まさよし,央敬=ひろたか,由照=よしてる,史靖=ふみやす",
			"5-13-F" => "由暉=ゆき,央会=ひろえ,未幹=みき,巨鈴=みすず,生聖・未聖=みさと,史郁=ふみか,由莉=ゆり,玉会=たまえ,加帆里=かほり,由記子=ゆきこ,未由季=みゆき,布沙代=ふさよ",
			"5-16-M" => "史勲=ふみひろ,玄学=ひろのり,由樹=ゆうき,正道=まさみち,弘憲=ひろのり",
			"5-18-M" => "巨翼=なおすけ,正鴻・巨鴻=まさひろ,永礼=のりあき,永翼=えいすけ,正礼=まさのり,由鎮=ゆきしげ,功鴻=のりひろ,正鎮=まさしげ,主礼=かずゆき,巧燿=よしてる,史礼=ふみのり,正豊=まさと,由翼=ゆうすけ,玄鎮=ひろしげ,巨燿=まさてる,玄礼=ひろゆき,生織=いおり ,功太郎=こうたろう,正太郎=しょうたろう,由太郎=ゆうたろう",
			"5-19-M" => "弘鏡=ひろあき,正拡=まさひろ,正汰朗=しょうたろう",
			"5-19-F" => "永観=えみ,加麗・甲麗=かれい,由佳梨=ゆかり,未希恵=みきえ,加於梨=かおり,由里恵=ゆりえ",
			"15-0-M" => "慧=さとる,毅=たけし,賢=まさる,進=すすむ,徹=とおる",
			"15-0-F" => "葵=あおい,慶=けい",
			"15-1-M" => "嬉一=よしかず,諄一=じゅんいち,賢一=けんいち,慶一=けいいち,瑠一=りゅういち",
			"15-2-M" => "慧人=けいと,毅人=たけひと,輝人=てるひと,賢人=まさと,慶人=やすひこ,広人=ひろひと,満人=みつひと,毅力=たけお,輝了=てるあき,賢力=まさお,徳力=とくお,楽了=よしあき,満力=みつお",
			"15-3-M" => "諒大=あきひろ,賢久=たかひさ,進也=しんや,毅士=たけし,範久=のりひさ,満大=みつひろ",
			"15-6-M" => "慶丞=けいすけ,毅光=たけひろ,賢匠=まさなる,諒匡=あきまさ,進伍=しんご",
			"15-8-M" => "毅於=たけお,賢昌・賢明=まさあき,諒汰=りょうた,広和=ひろかず,慶汰=けいた,諒児=りょうじ,徳知=やすのり,諒於=あきお,満幸=ありゆき",
			"15-9-M" => "賢彦=まさひこ,広亮=ひろあき,瑠哉=りゅうや,慶治・慧治=けいじ,徳重=なるしげ,慶彦=やすひこ,瑠哉=りゅうや,賢重=まさしげ,誼保=よしお,広泰=ひろやす",
			"15-9-F" => "慶美=よしみ,瑠香=るか,賢美=さとみ,摩紀=まき,慧美=えみ,慶香=けいか,稼保=かほ,瑠皆・瑠美=るみ",
			"15-10-M" => "慧師=さとし,興記=ともき,満芳=みつよし,賢洋=まさひろ,慶展=やすのり,賢晋=まさゆき,諄祐=しゅんすけ,楽哲=よしのり,徳洋=とくひろ,慶晋=やすゆき,逸哲=としのり,輝真=てるまさ",
			"15-10-F" => "葉留=はる,賢花=のりか,摩城・摩記=まき,慧真=えま,満紗=みさ,瑠花=るか,慶花=けいか,慧留=える,徳紗=ありさ,嬉花=よしか,摩記=まき,嬉花・楽芳=よしか,賜起=たまき,瑠花=るか,摩記=まき,瑠花=るか,葉洋=ほなみ,嬉未代=きみよ,駒見子=くみこ,稼甫子・稼歩子=かほこ,瑠見子=るみこ,慧李子=えりこ",
			"15-17-M" => "徳謙=やすのり,広繁=ひろしげ,賢陽=まさあき,慶隆=よしたか,輝優=てるまさ",
			"6-0-M" => "旭=あきら,匡=ただし,亘=わたる,丞=すすむ,光=ひかる,匠=たくみ,旬=ひとし",
			"6-0-F" => "汀=なぎさ,冴=さえ,光=ひかり,早=さき,朱=あけみ,",
			"6-1-M" => "圭一=けいいち,庄一=しょういち,亘一=のぶかず,光一=こういち,臣一=とみかず",
			"6-2-M" => "圭乃=よしの,光乃=ひろの,朱乃=あやの,吏乃=りの,宇乃=うの",
			"6-5-M" => "有矢=ゆうや,亘平=こうへい,光司=こうじ,好玄=よしひろ,匠五=しょうご",
			"6-5-F" => "好史=よしみ,光民=ひろみ,多未=たみ,臣央=みお,有加=ゆか,冴加=さえか,吏加=りか,早代=さよ,圭代=かよ,安由=あゆ,安矢=あや,臣卯=みう",
			"6-7-M" => "光志=ひろし,匠吾=しょうご,匡宏・庄宏=まさひろ,臣秀=みつひで,光宏=みつひろ,臣吾=しんご,匡志=まさし,有助=ゆうすけ,臣志=たかし,光秀=みつひで,圭宏=よしひろ,光男=てるお,臣利・光利=みつとし,匡宏=ただひろ,圭助=けいすけ",
			"6-7-F" => "衣李・衣里=えり,好甫・好歩・臣歩=みほ,有希=ゆき・ゆうき,圭江・好江=よしえ,衣江=きぬえ,吏佐=りさ,朱見=あけみ,多江=たえ,好里・臣里・好邑=みさと,光良=てるみ,名甫=なほ,有歩=ゆうほ,早江=さえ,吏歩=りほ,圭歩=かほ,有希=ゆうき,有李・有里=ゆり,圭甫=かほ,好希=みき,好希=みき,早希=さき",
			"6-9-M" => "光彦=あきひこ,有哉=ゆうや,好治=よしはる,臣保=たかお,匠彦=なるひこ,匡哉=まさや,好亮・圭亮=よしあき,光治=みつはる,匡彦=まさひこ,匠哉=たくや,庄治=しょうじ,臣保=みつお,光泰=ひろやす,好信=よしのぶ,圭紀=よしき,亘保=のぶお,匡俊=まさとし",
			"6-9-F" => "好美=よしみ,冴香=さえか,有紀=ゆうき,圭保=かほ,早紀=さき,吏保=りほ,有香=ゆうか,朱音=あかね,光美=ひろみ,好春=みはる,好香=みか,朱美=あけみ,安紀=あき,衣美=えみ,臣紀=みき,好美=よしみ,冴香=さえか,吏香=りか",
			"6-10-M" => "好晋・圭晋=よしゆき,有記=ゆうき,匡哲=まさのり,光洋=みつひろ・あきひろ,匡晋=まさゆき,光隼=みつとし,臣哲=しげのり・みつのり,好洋・圭洋=よしひろ,匡晃=まさあき,圭剛・好剛=よしたけ,光真=てるまさ,臣洋=みつひろ,吏納=さとのり,好高=よしたか,光哲=みつのり,臣晃=みつあき,光祐=こうすけ,好哲=よしのり,光晋=てるゆき,臣紘=みつひろ,吉晃・好晃=よしあき,匡隼=まさとし,光晋=ひろゆき,匡洋=まさひろ,圭哲=よしのり,圭晃=よしあき,光紘=てるひろ,匠真=なるまさ,考晃=やすあき,圭恭=やしたか,吉哲=よしのり,圭晋・好晋=よしゆき,有祐=ゆうすけ,好真=よしまさ,光隼=みつとし,匠真=たくま",
			"6-10-F" => "吏紗=りさ,早記=さき,冴花=さえか,衣真=えま,有紗=ありさ,安記=あき,光記=みつき,臣紗=みさ,有記=ゆうき,合花=はるか,好花=みか,衣留=える,光紗=ありさ,圭花=よしか,好記=みき,好矩=みく,有起=ゆうき,圭良子=かよこ,有希子=ゆきこ,衣里子=えりこ,吏甫子=りほこ,早矢加=さやか",
			"6-11-M" => "匡敏=ただとし,光彬=みつあき,好章=よしあき,吉崇=よしたか,臣教=みつのり",
			"6-11-F" => "合鹿・合茄=はるか,安那=あんな,早苗=さなえ,衣梨=えり,匡彗=まさえ,好彩=みさえ,吏那=りな,光彗=ひろえ,多麻=たま,有梨=ゆり,有鹿,有茄=ゆか,光彗=みつえ,安那=あんな,有史圭=ゆみか,名史衣=なみえ",
			"6-12-M" => "光博=みつひろ,匡雄=ただお,有喜=ゆうき,好晴=よしはる,圭雅=よしまさ",
			"6-12-F" => "光恵=ひろえ,衣理=えり,好喜=みき,守惟=まい,百恵=ももえ,早稀=さき,有惟=ゆい,多恵=たえ,光視=てるみ,早智=さち,有稀=ゆうき,吉視=よしみ,好晴=みはる,圭恵=よしえ,吏里加=りりか,圭央里=かおり,有里加=ゆりか",
			"6-15-M" => "光諒=てるあき,臣慧=みさと,匡賢=まさのり,吉慶・好慶=よしのり・よしやす,匡毅=まさとし,光葵・光嬉=ひろき,臣賢=みつまさ,匠広=なるひろ,好賢=よしまさ,匡広=まさひろ,圭太朗=けいたろう,庄太朗=しょうたろう,光太朗=こうたろう",
			"6-17-M" => "有弥=ゆうや,匡聡=まさあき,光陽=ひろみつ・ひろあき・みつはる,好隆=よしたか,匡弥=まさや,臣優=たかまさ・みつまさ,匡陽=まさあき,光優=みつひろ,臣駿=みつとし,好隆・吉隆=よしたか,全弥=まさや,好陽=よしあき・よしはる,旭陽=てるあき,匡駿=まさとし,吉優=よしまさ,臣隆=みつたか,匠優=なるひろ,考大郎=こうたろう,光次朗=こうじろう,光吉朗=こうきちろう",
			"6-18-M" => "匡鴻=まさひろ,庄鎮・匡鎮=まさしげ,好礼=よしあき・よしのり,有豊=ゆうと,光翼=ひろすけ・こうすけ,色鯉=いろり,冴麿=さえまろ,好燿=よしてる,衣織=いおり,臣鎮=みつしげ",
			"6-18-F" => "衣鯉=えり,圭蕗=かろ,早織=さおり,好礼=みゆき,朱鯉=あかり,圭織・圭央莉=かおり,好臨=よしみ,安槻子=あきこ,有嬉子=ゆきこ,多慧子=たえこ,圭葉子=かよこ,衣摩子=えまこ,好葉子=みほこ,光慧子=みえこ,早嬉子=さきこ,吏稼子=りかこ,圭那江=かなえ,衣里那=えりな,有茄里=ゆかり,好紗枝=みさえ,吏葉子=りほこ",
			"6-19-M" => "臣穏=みつとし,圭鏡=よしあき,亘勧=のぶゆき,匡勧=まさゆき,光拡=みつひろ",
			"6-19-F" => "吏樺子=りかこ,有樹子=ゆきこ,圭都子=かつこ,圭於梨=かおり,有貴江=ゆきえ,安祐美=あゆみ,衣梨佳=えりか",
			"16-5-M" => "蒼平=そうへい,憲功=かずのり,篤司=あつし,叡央=まさし,達生=たつお,暁弘=あきひろ,篤生=しげお,勲司=ひろし,潤平=じゅんぺい,憲矢=かずや,学史=ひさし,勲生=いさお,潤史=ひろし,鮎平=あゆへい,樹矢=みきや",
			"16-7-M" => "暁宏=あきひろ,達男=たつお,学志=さとし,憲秀=かずひで,篤宏=しげひろ,憲吾=けんご,道克=まさかつ,潔志=きよし,頼孝=よしたか",
			"16-8-M" => "暁於=あきお,篤昌=しげあき,燎汰=りょうた,達典=たつのり,蒼汰=そうた,道明=みちあき,勲和=ひろかず,篤幸=しげゆき,篤於=しげお,勲昂=ひろあき,憲汰=けんた,頼宗=よしのり,勲於=いさお・しげお,叡昌=まさあき,遊汰=ゆうた,篤知=しげのり,頼政=よりまさ,憲汰=けんた",
			"16-8-F" => "樺奈=かな,璃沙=りさ,静枝=しずえ,磨奈=まな,璃沙=りさ,都依=ひろえ,親幸=みゆき",
			"16-9-M" => "達彦=たつひこ,憲哉=かずや,道治=みちはる,篤俊=しげとし,勲亮=ひろあき,鮎彦=あゆひこ,蒼哉=そうや,篤治=しげはる,勲保=いさお,憲彦=かずひこ,潤哉=じゅんや,樹保=しげお,学亮=たかあき,篤彦=しげひこ,達哉=たつや,憲治=けんじ,勲保=いさお,都泰=ひろやす,暁彦=あきひこ,衛亮=ひろあき,篤泰=しげやす,達哉=たつや,潤亮=ひろあき",
			"16-9-F" => "鮎美=あゆみ,樺保=かほ,璃香=りか,磨紀=まき,樹美=なみ,璃保=りほ,璃早子=りさこ,都好子=とみこ,磨衣子=まいこ,磨好子=まみこ,磨有子=まゆこ",
			"16-13-M" => "篤暉=しげき,勲=ひろき,叡郁=としふみ,道靖=みちはる,暁琢=あきたか,蒼椰=そうや,潤耶=じゅんや,学詩=さとし,勲路=いさじ,憲裕=かずひろ",
			"16-15-M" => "篤葵=しげき,勲輝=ひろき,道慶=みちやす,暁賢=あきまさ,憲徳=かずのり,憲磨=かずま",
			"16-15-F" => "磨緯=まい,璃恵子=りえこ,磨稀子=まきこ,都稀子=ときこ,磨惟子=まいこ,璃恵子=りえこ,蓉理子=ゆりこ",
			"16-16-M" => "篤樹=しげき,頼道=よりみち,達磨=たつま,都勲=くにひろ,勲樹=ひろき,篤学=しげひさ,頼道=よりみち",
			"16-19-M" => "都拡=くにひろ,学勧=ひさゆき,道遵=みちより,憲薦=かずのぶ,篤穏=しげとし",
			"7-0-M" => "杏=あんず,李=すもも・もも,伶=れい,歩=あゆみ,佑=ゆう,妙=たえ",
			"7-4-M" => "邑太=ゆうた,宏文=ひろふみ,秀元=ひでゆき,君仁=きみひと,良太=りょうた",
			"7-6-M" => "伸冴・伸伍=しんご,佑次=ゆうじ,甫全=まさみつ,克守=かつま,秀臣=ひでお,良光=よしひろ,孝臣=たかおみ,佑吉=ゆうきち,秀匡=ひでまさ",
			"7-6-F" => "佑圭=ゆうか,良冴=みさえ,初衣=はつえ,秀好=ひでみ,李名=りな,里圭=りか,杏名=あんな,杏圭=きょうか,里冴=りさえ,李衣=りえ,佑名=ゆうな,江吏=えり,佐伎=さき,見冴=みさえ,良衣=よしえ,成好=なるみ",
			"7-8-M" => "亨於=あきお,良昂=よしあき,佑汰・邑汰=ゆうた,宏明=ひろあき,伸幸=のぶゆき,秀和=ひでかず,言汰=げんた,良弦=よしお,秀於=ひでお",
			"7-8-F" => "里奈=りな,李沙・里沙=りさ,君枝=きみえ,秀佳・良佳=はるか,見幸・良幸=みゆき,七奈=なな,里沙・李沙=りさ,良枝=よしえ,杏奈=あんな,里佳=りか,伶佳=れいか,佐知・作知=さち,佑佳=ゆうか,伶佳=れいか・りょうか,見季=みき,里奈=りな,杏佳=きょうか,初枝・初姉=はつえ,佑奈=ゆうな,李枝・里枝=りえ,良枝=よしえ,見幸=みゆき,佐季=さき",
			"7-9-M" => "佑哉=ゆうや,秀彦=ひでひこ,宏信=ひろのぶ,克彦=かつひこ,甫治=まさはる",
			"7-9-F" => "秀美=ひでみ,李香・里香=りか,佑紀=ゆうき,良春・見春=みはる,志保=しほ,良重=よしえ,里保・李保=りほ,佑美=ゆみ,佐紀=さき,初音=はつね,李砂=りさ,里美・里皆=さとみ,見紀=みき,七美=なみ,秀美=ひでみ,良香=はるか,見保=みほ,伶香=れいか,成皆=なるみ,宏美=ひろみ,佑香=ゆうか,佑美=ゆみ,杏香=きょうか",
			"7-10-M" => "宏晃=ひろあき,良晋=よしゆき,亨紘=あきひろ,克哲=かつのり,利晋=としゆき,邑祐=ゆうすけ,秀洋=ひでひろ,利晋=としゆき,伸祐=しんすけ,秀哲=ひでのり,宏記=ひろき,伸洋=のぶひろ",
			"7-10-F" => "李紗=りさ,作記=さき,良花=みはる,江留=える,里紗=りさ,佑花=ゆうか,江真=えま,甫洋=ほなみ,佐記=さき,里花=りか",
			"7-11-M" => "宏章=ひろあき,良健=よしたけ,秀敏=ひではる,甫浩=まさひろ,秀章=ひであき,志英=ゆきひで,良朗・利朗=よしろう,延英=のぶひで",
			"7-11-F" => "佑鹿=ゆうか,里那=りな,江梨=えり,甫彗=まさえ,七苗=ななえ,杏梨=あんり,君彗=きみえ,良雪=みゆき,杏茄=きょうか,佑那=ゆうな,李彗=りえ,佐苗=さなえ",
			"7-14-M" => "良郎=よしお,佑輔=ゆうすけ,秀鳳=ひでたか,宏誠=ひろあき,伶造=りょうぞう,甫嘉=まさひろ,利源=まさよし,孝源=たかよし,伸源=しんげん(のぶよし),言大朗=げんたろう,良嘉=よしひろ,佑輔=ゆうすけ,志寿=ゆきひさ,秀誠=ひでまさ,初大朗=はつたろう",
			"7-16-M" => "宏暁=ひろあき,志学=ゆきのり,佑樹=ゆうき,秀頼=ひでより,秀暁=ひであき,甫勲=まさひろ,良潔=よしゆき,利憲=としのり,良勲=かずひろ,秀学=ひでひさ,克憲=かつのり,宏燎・宏暁=ひろあき,亨勲=あきひろ,秀樹=ひでき,甫憲=まさのり,秀憧=しゅうどう,利潤=としひろ,志篤=ゆきしげ,志篤=ゆきしげ,佑樹=ゆうき,甫憲=まさのり,良勲=よしひろ,秀憲=ひでのり,利磨=かずま,宏篤=ひろしげ,秀潤=ひでひろ,良憲=よしのり,成篤=まさしげ,秀勲=ひでひろ",
			"7-17-M" => "佑弥=ゆうや,志繁=ゆきしげ,秀陽=ひであき,良隆=よしたか,伸弥=しんや,良聡=よしあき,克駿=かつとし,孝声=こうせい,志優=ゆきひろ",
			"7-17-F" => "宏弥=ひろみ,佑霞=ゆうか,李声=りな,佑霞=ゆうか,良陽=みはる,志穂=しほ,希美枝=きみえ,志央理=しおり,見紗江=みさえ",
			"7-18-M" => "佑翼・邑翼=ゆうすけ,秀礼=ひであき,甫鎮=まさしげ,宏鎮=ひろしげ,良礼=よしのり,亨豊=あきひろ,良翼=りょうすけ",
			"7-18-F" => "作織=さおり,佑鯉=ゆり,志織=しおり,佑茄里=ゆかり,李葉子=りほこ,希美香=きみか,良紗枝=みさえ,佐央莉=さおり,見稼子=みかこ,七那江=ななえ",
			"17-0-M" => "聡・駿=さとし,弥=わたる,陽・燦・郷=あきら,繁=しげる,斎=ひとし,隆=たかし,優=まさる",
			"17-0-F" => "瞳=ひとみ,霞=かすみ,鞠=まり,澪=みお,操=みさお,優=ゆう",
			"17-4-M" => "弥允=ひさみつ,陽介=ようすけ,謙仁=けんじ,優太=ゆうた,隆夫=たかお,優文=まさふみ,謙太=けんた,隆之=たかゆき,弥文=ひろふみ,陽夫・聡夫=あきお,優仁=まさひろ,弥夫=ひさお,聡介=そうすけ,駿太=しゅんた,隆太=りゅうた,駿夫=としお,聡仁=さとのり",
			"17-6-M" => "隆伍=りゅうご,営吉=えいきち,陽光=はるひこ,優臣=ひろお,優伍=ゆうご,陽光=あきひろ,隆臣=たかお,優伎=ゆうき,優多=ゆうた,謙多=けんた,駿臣=としおみ,駿伍=しゅんご,弥臣=ひろみつ",
			"17-7-M" => "聡志=さとし,駿伸=としのぶ,陽宏=あきひろ,優吾=ゆうご,弥良=ひろお",
			"17-7-F" => "霞歩=かほ,陽江=はるえ,優希=ゆうき,弥里=みさと,弥甫=みほ",
			"17-8-M" => "駿於=としお,弥昌=ひろあき,聡汰=そうた,隆明=たかあき,優直=まさなお,謙幸=のりゆき,陽政=はるまさ,陽於=はるお・あきお,駿明=としあき,優幸=まさゆき,弥和=ひろかず,聡汰=そうた,繁忠=しげただ,優汰=ゆうた,繁忠=しげただ,謙幸=よしゆき,繁明=しげあき",
			"17-8-F" => "弥沙=みさ,霞奈=かな,聡枝=としえ,陽佳=はるか,優佳=ゆうか,優奈=ゆうな,操枝=みさえ,弥玖=みく,陽奈=はるな,陽枝=はるえ・あきえ,弥代子=みよこ",
			"17-14-M" => "陽嘉・陽碩=あきひろ,優輔=ゆうすけ,隆郎=たかお,謙造=けんぞう,優鳳=まさたか,嶺造=りょうぞう,謙大朗=けんたろう",
			"17-14-F" => "弥華=みか,陽実=はるみ,霞奈衣=かなえ,弥由紀=みゆき,声央美=なおみ,陽伽里=ひかり",
			"17-15-M" => "陽広=あきひろ,弥嬉=ひろき,優輝=ゆうき,聡賢=あきのり,繁慶=しげやす,駿進=としゆき,営太朗=えいたろう,謙一郎=けんいちろう",
			"17-18-M" => "総礼=のぶあき,陽曜=あきてる,優翼=ゆうすけ,弥蕗=みろ,営豊=えいと,弥燿=よしてる,応鎮=まさしげ,聡礼=あきひろ,陽翼=ようすけ",
			"8-3-M" => "侑也=ゆうや,忠己=ただのり,昂大=あきひろ,和大=かずひろ,佳久=よしひさ,武士=たけし",
			"8-3-F" => "朋巳=ともみ,奈巳=なみ,侑巳=ゆみ,知千=ちゆき,沙千=さち,昂子=あきこ,亜弓=あゆみ,季己=きこ",
			"8-5-M" => "昌弘=まさひろ,昂央=あきひろ,孟司=たけし,侑矢=ゆうや,昂巨=あきお,武玄=たけのり,忠司=ただし",
			"8-5-F" => "知加=ちか,佳代=かよ,和生=かずよ,沙代・沙生=さよ,奈未・奈巨=なみ,直巨・奈央・奈生=なお,玖巨=くみ,采加=あやか,亜矢=あや,朋生=ともみ,采加=さいか,侑卯=ゆう,朋加=ともか,沙矢=さや,幸代=さちよ・ゆきよ・さちよ,直未=なおみ,直生=なおみ,知令=ちはる,亜由=あゆ,侑加=ゆうか,和加=わか",
			"8-7-M" => "昌吾・昇吾=しょうご,侑佑=ゆうすけ,彼呂=ひろ,孟志=たけし,幸良=ゆきお,昂宏=あきひろ",
			"8-7-F" => "奈甫・奈歩=なほ,昌江=あきえ,沙希=さき,枝里・枝李・依李=えり,幸江=さちえ,亜希=あき,知里=ちさと,侑里・侑李=ゆり,知江=ともえ・ちえ,玖見=くみ,佳歩・佳甫=かほ,朋見=ともみ,沙江=さえ,侑岐=ゆき,佳江=よしえ,亜佑=あゆ,沙岐=さき",
			"8-8-M" => "明於=あきお,昌汰=しょうた,侑児=ゆうじ,知和=ともかず,忠幸=ただゆき",
			"8-8-F" => "朋味=ともみ,佳奈=かな,侑依=ゆい,沙知=さち,幸枝=さちえ,朋枝=ともえ,玖味=くみ,亜侑=あゆ,朋果=ともか,沙姉・沙枝=さえ,采佳=さいか,奈味=なみ,知明=ちあき,奈々=なな,玖味=くみ,侑季=ゆき,采佳=あやか,和枝=かずえ,沙代子=さよこ,亜矢子=あやこ",
			"8-9-M" => "孟彦=たけひこ,昌哉=まさや,知治=ともはる,幸重=ゆきしげ,昂保=たかお,昂彦=あきひこ,忠亮=ただあき,忠彦＝ただひこ,武俊=たけとし,直哉=なおや,昂昭=たかあき,幸彦=ゆきひこ,朋彦=ともひこ,昌亮=まさあき,忠哉=ちゅうや,武治=たけはる,直重=ただしげ,朋哉=ともや,忠柾=ただまさ,佳治=よしはる,和保=かずお,侑哉=ゆうや,佳秋=よしあき,忠治=ただはる,幸重=ゆきしげ",
			"8-9-F" => "玖美=くみ,采香=さいか,沙紀=さき,明音=あかね,奈保=なほ,朋美・知美=ともみ,奈美=なみ,采音=あやね,佳保=かほ,奈保=なほ,朋香=ともか,亜美=あみ,侑香=ゆか,知春=ちはる,佳保=かほ,奈美=なみ,知秋=ちあき",
			"8-10-M" => "昌晃=まさあき,佳晋=よしゆき,侑祐=ゆうすけ,昂紘=あきひろ,武哲=たけのり,佳晃=よしあき,和洋=かずひろ,知真=ともまさ,武剛=たけよし,和晋=かずゆき,宗真・和真=かずま,朋晃=ともあき,武真=たけまさ,昌哲=まさのり,和芳=かずよし,忠晃=ただあき,政高=まさたか,昌晋=まさゆき,昂洋=あきひろ,侑記=ゆうき,忠真=ただまさ,佳哲=よしのり,知晃=ともあき,昂晋=たかゆき,和芳=かずよし,忠洋=ただひろ,和隼=かずとし,旺洋=あきひろ,忠哲=ただのり,政晃=まさあき,直晋=なおゆき,忠祐=ただすけ,昂哲=あきのり,政洋=まさひろ,宗晋=むねゆき,尚記=なおき,幸洋=ゆきひろ,朋晋=ともゆき,和真=かずま,直起=なおき,武晋=たけゆき,空隼=たかとし",
			"8-10-F" => "采花=あやか・さいか,侑花=ゆか,沙記=さき,亜記=あき,奈留=なる,枝留=える,朋花=ともか,知洋=ちひろ,侑記=ゆき,知衿=ちえり,侑真=ゆま,奈甫子=なほこ,亜希子=あきこ",
			"8-13-M" => "直郁=なおふみ,佳琢=よしたか,侑耶=ゆうや,昌裕=まさひろ,直暉=なおき,知椰・知耶=ともや,昂裕=あきひろ,昂暉=こうき,忠靖=ただやす,武嗣=たけし,幸裕=ゆきひろ,和聖=かずまさ,直路=なおみち,典嗣=のりつぐ,武義=たけよし,知暉=ともき,昌耶=まさや,佳嵩=よしたか,昂裕=たかひろ",
			"8-15-M" => "侑葵・侑嬉=ゆうき,佳賢・佳徳=よしのり,和慶=かずよし,明徳=あきのり,和賢=かずまさ,侑葵=ゆうき,佳徳=よしのり,朋広=ともひろ,和摩=かずま,幸一郎=こういちろう",
			"8-16-M" => "政勲=まさひろ,武学=たけひさ,和樹=かずき,直達=なおみち,忠暁=ただあき,和篤=かずしげ,幸潤=ゆきひろ,知樹=ともき,政道=まさみち,忠篤=ただしげ,昂勲=あきひろ,直樹=なおき,佳憲=よしのり,幸篤=ゆきしげ,知勲=ともひろ,佳勲=よしひろ,侑樹=ゆうき,武憲=たけのり,和磨=かずま",
			"8-16-F" => "侑樺=ゆか,枝璃=えり,沙樹=さき,依磨=えま,奈々枝=ななえ,亜佑美=あゆみ,佳保里=かほり,季美江=きみえ,知亜季=ちあき,侑幹子=ゆみこ,奈美江=なみえ,沙奈枝=さなえ,亜暉子=あきこ",
			"8-17-M" => "和聡=かずあき,直弥=なおや,空陽=たかはる,政隆=まさお,昌聡=まさあき,朋弥=ともや,佳陽=よしはる,知優=ともひろ,和弥=かずや,知謙=とものり,忠陽=ただあき,佳隆=よしたか",
			"8-17-F" => "亜弥=あみ,奈弥=なみ,采霞=さいか,佳声=かな,枝弥=えみ,朋弥=ともみ,昌弥=まさみ,侑霞=ゆか,知陽=ちはる,奈穂=なほ,奈声=なな,直弥=なおみ,朋霞=ともか,佳穂・果穂=かほ,侑霞=ゆうか,奈穂=なほ,朋霞=ともか,沙綺子=さきこ,侑華子=ゆかこ,知華子=ちかこ,侑綺子=ゆきこ,玖実子=くみこ,枝実子=えみこ,侑里花=ゆりか,亜里紗=ありさ,佳央理=かおり",
			"18-3-M" => "爵大=たかひろ,燿久=てるひさ,礼士=まさし,蕉也=しょうや,爵己=たかのり,鎮大=しげひろ,礼久=あきひさ,豊士=ひろし",
			"18-5-M" => "鴻由=ひろゆき,礼弘=あきひろ,蕉矢=しょうや,鎮弘=しげひろ,蕉平=しょうへい,爵司=たかし,豊永=よしのり,燿生=てるお,豊正=ひろまさ,礼史=ひろし,鎮生=しげお,礼司=まさし,燿正=てるまさ",
			"18-6-M" => "蕉伍・蕉冴=しょうご,鎌多=れんた,爵光=たかひろ,豊臣=ひろおみ,豊伎=とよき,燿匡=てるまさ,鎮光=しげみつ,礼臣=まさおみ",
			"18-7-M" => "燿宏=てるひろ,鎮男・鎮良=しげお,蕉志=しょうじ,礼秀=まさひで,礼志・豊志=ひろし,豊孝=よしたか,鎮宏=しげひろ,蕉吾=しょうご,曜佑・燿助=ようすけ,礼男=あきお,礼宏=まさひろ,蕉吾=しょうご,燿甫=てるまさ,鎮利=しげとし,豊良=ひろよし",
			"18-7-F" => "鯉甫・鯉歩=りほ,蕗見=ろみ,蕗里・蕗李=ろり,蕗江=ふきえ,環希・環岐=たまき,礼江=ひろえ,鎮江=しずえ",
			"18-11-M" => "耀悠=てるひさ,曜彬=てるあき,豊英=ひろひで,鎮規=しげき,礼崇=ひろたか",
			"18-14-M" => "礼輔=ひろすけ,耀彰=てるあき,豊鳳=ひろたか,鎮実=しげみつ,豊郎=よしろう",
			"18-17-M" => "礼聡=ひろあき,豊隆=よしたか,燿優=てるまさ,鎮陽=しげあき,蕉大郎=しょうたろう",
			"9-4-M" => "泰文=やすふみ,哉夫=としお,亮介=りょうすけ,紀仁=かずひろ,勇太=ゆうた,勇介=ゆうすけ,紀元=のりゆき,泰仁=やすのり・やすひと,亮太=りょうた,亮夫=あきお,俊介=しゅんすけ,重仁=しげのり・しげひと,勇太=ゆうた,泰文=やすふみ・ひろふみ,柾夫=まさお,亮仁=あきひと,春夫=はるお,重文=しげふみ,紀夫=のりお,保仁=やすのり,亮太=りょうた",
			"9-4-F" => "春方=はるみ,美仁=みさと,香心=こうみ,香之=かの,美公=みく,春心=はるみ,保心=やすみ,泉水=いずみ,美日=みはる,香月=かつき,紀文=きふみ,香方=こうみ,泉水=いづみ,美月=みつき,紀文=きふみ",
			"9-6-M" => "勇伍=ゆうご,亮光=あきひろ,治好=はるよし,紀臣=のりみつ,保匡=やすまさ",
			"9-6-F" => "皆伎=みき,怜圭=れいか,美冴=みさえ,香好=よしみ,宥伎=ゆうき,美圭=みか,香衣=よしえ,虹好=こうみ,紀圭=のりか,秋衣=あきえ,虹圭=にじか,春名=はるな,虹伎=こうき,美圭=みか,秋衣=あきえ,宥好=ゆか,虹衣=にじえ,皆好=みなみ,泉伎=みずき,宥圭=ゆうか,香名=かな",
			"9-7-M" => "泰宏・保宏=やすひろ,信吾=しんご,亮佑=りょうすけ,勇志=ゆうじ,柾成=まさなり,保宏=やすひろ,勇吾=ゆうご,柾克=まさかつ,泰志=ひろし",
			"9-7-F" => "香甫・香歩=かほ,春江=はるえ,宥希=ゆうき,美里=みさと,美佐・皆佐=みさ,春見=はるみ,保甫=ほなみ,紀見=よしみ,美希=みき,皆歩=みほ,紀江=かずえ,美歩・美甫=みほ,虹良=こうみ,香杏=こうあん,春江=はるえ,砂希=さき,泉里=せんり,秋江=あきえ,虹江=にじえ,宥希=ゆうき,宥里=ゆり,皆佐=みさ,泉江=みずえ",
			"9-8-M" => "香奈=かな,美沙=みさ,皆佳=みか,紀奈・秋奈=あきな,美奈=みな,美幸=みゆき,美佳=みか,亮枝・秋依=あきえ",
			"9-9-M" => "泰亮=やすあき,重彦=しげひこ,柾哉=まさや,勇治・宥治=ゆうじ,信彦=のぶひこ,亮哉=りょうや,泰俊=やすとし,泰亮=ひろあき,貞治=さだはる,柾重=まさしげ,泰保=やすお",
			"9-9-F" => "香保=かほ,砂紀=さき,美春=みはる,虹美=こうみ,美保=みほ,美紀=みき,美香=みか,香吉子=かよこ,九好子=くみこ,美名子=みなこ",
			"9-12-M" => "泰雄=やすお,治善=はるよし,柾博=まさひろ,信普=のぶゆき,亮雄=あきお,柾智=まさのり,治善=はるよし,保博=やすひろ,保博=やすひろ,治雄=はるお,亮喜=あきゆき,法理=かずのり,要雅=としまさ,秋雄=あきお,重博=しげひろ,勇雄=いさお,重喜=しげき,亮博=あきひろ,勇一朗=ゆういちろう,秋一朗=しゅういちろう",
			"9-14-M" => "泰嘉=やすひろ,亮輔=りょうすけ,哉滉=としあき,治郎=はるお・じろう,保嘉=やすひろ,亮輔=りょうすけ,勇鳳=としたか,柾彰=まさあき,泰造=たいぞう",
			"9-15-M" => "柾輝=まさき,法賢=かずのり・のりまさ,重慶=しげよし,勇輝・宥毅=ゆうき,柾徳=まさのり,保毅=やすのり,紀賢=かずまさ,泰慶=ひろやす,重徳=しげと,勇葵=ゆうき,俊賢=よしのり,泰広=やすひろ,哉毅=としのり,信慶=のぶやす,勉徳=かつのり,柾輝=まさき,重慶=しげよし,俊進=としゆき,紀徳=よしのり,重賢=しげのり,亮広=あきひろ,虹一郎=こういちろう",
			"9-15-F" => "美嬉・美葵=みき,香瑠=かる,秋慧=あきえ,虹慧=にじえ,美慧=みえ,泉嬉=みずき,皆葉=みなよ,美喜子=みきこ,美智子=みちこ,美恵子=みえこ,香須子=かずこ,紀久恵=きくえ,美沙希=みさき,美有紀=みゆき,香於里=かおり,保名美=ほなみ",
			"9-16-M" => "信篤=のぶしげ,保勲=やすひろ,亮潤=あきひろ,勇運=たけゆき,宥樹=ゆうき,重憲=しげかず",
			"9-16-F" => "紀樺=のりか,香璃=かおり,美樹=みき,春樺=はるか,宥璃=ゆり,美暉子=みきこ,美嵯子=みさこ,美郁子=みかこ,美耶子=みやこ,香保里=かほり,美佑紀=みゆき,保南見=ほなみ,紀美江=きみえ,皆奈枝=みなえ",
			"19-12-M" => "遼雅=りょうが,遼喜=りょうき,穏雄=としお,穏詞=やすし,拡智=ひろのり,勧博=ゆきひろ,鏡勝=あきのり",
			"19-13-M" => "遼耶・遼椰=りょうや,穏敬=やすのり,穏詞=やすし,拡暉=ひろき,勧琢=ゆきたか",
			"19-16-M" => "拡篤=ひろしげ,賛陳=よしのり,穏道=としみち,遼磨=りょうま,遵衛=のぶひろ",
			"10-0-M" => "晃=あきら,晋=すすむ,隼=はやと,洵=まこと,洸=ひろし,倭=やまと,剛=たかし,真=まこと,哲=さとし",
			"10-3-M" => "真也・晋也=しんや,芳己=よしのり,祐大=ゆうだい,晃久=あきひさ,剛士=たけし,玲也=りょうや,晃己=あきのり,恭丈=よしたけ,祐也=ゆうや,秦也・晋也=しんや,洋大=ひろお,芳久=よしひさ,真大=まさひろ,剛久=たけひさ,哲士=さとし,真大=まさひろ,恒久=つねひさ,洋士・洸士=ひろし",
			"10-3-F" => "留巳=るみ,紗己=さき,玲巳=たまみ,花女=はるか,真千=まち,真巳=まみ,紗千=さち,洋子=ようこ,晃子=あきこ,真子=まこ,恭子=きょうこ,玲子=れいこ,祐子=ゆうこ,祐巳=ゆみ",
			"10-5-M" => "晋弘=ゆきひろ,真生=まさお,恭司=ただし,紘平=こうへい,真弘=まさひろ,秦平・晋平=しんぺい,祐矢=ゆうや,洋史・紘史・紘司・洋司=ひろし,晃弘=あきひろ,祐司=ゆうじ,啄矢=たくや,哲司=さとし,真矢=まさや,啄生=たくお,倭功=まさのり,哲正=よしただ,晋矢・秦矢=しんや,晃央=あきひろ,真功・真永=まさのり,哲平=てっぺい,祐矢=ゆうや,芳弘=よしひろ,祐司=ゆうじ,真平・晋平=しんぺい,恭巨=やすお,芳史=よしふみ,真史=まさし,祐矢=ゆうや,隼平=じゅんぺい,真生=まさお,晋弘=ゆきひろ,洋充=ひろみつ,洋正=ひろまさ,洋由=ひろゆき,洋平=ようへい,倫弘=ともひろ,倫生=としお,倫功=みちのり,倫司=ひとし,倫正=としまさ,倫史=としふみ",
			"10-5-F" => "祐生=ゆみ・ゆうき,衿加=えりか,育代=いくよ,真由=まゆ,花未=はるみ,矩巨=くみ,祐加=ゆうか,紗代=さよ,紘未・洋未・洋生=ひろみ,花代=かよ・はなよ,留未・留史=るみ,玲未=たまみ,紗矢=さや,花由=かより,留加=るか,祐代=まさよ,芹加=せりか,祐未・祐充=ゆみ,花加=はるか",
			"10-6-M" => "晋伍・晋冴・真伍=しんご,宰匡=ただまさ,哲光=よしみつ,真臣=まさお,真光=まさみつ,啄臣=たくみ,祐吉=ゆうきち,洋好=ひろみ,哲臣=よしたか,隼丞=しゅんすけ,倖吉=こうきち,拳次=けんじ,祐丞=ゆうすけ,祐伎=ゆうき,洋光=ひろみつ",
			"10-6-F" => "紗伎=さき,真衣=まい,留好=るみ,花圭=はるか,祐伎=ゆうき,芹圭=せりか,真有=まゆ,紗衣=さえ,玲好=たまみ,真名=まな,真伎=まき,祐圭=ゆうか,益冴=みさえ,花名=はるな,留吏=るり,真冴=まさえ,洋衣=ひろえ,晏名=あんな",
			"10-7-M" => "晃宏=あきひろ,晋吾=しんご,祐佑=ゆうすけ,哲男=てつお,恭志=やすし,真良=まさお",
			"10-7-F" => "真李・真里=まり,花甫=かほ,記江・芳江=よしえ,紗希=さき,洋見=ひろみ,紗江=さえ,祐希=ゆうき,留見=るみ,祐李=ゆり,花甫・花歩=かほ,洋江=ひろえ,真希=まき,留里=るり,真江=まさえ",
			"10-8-M" => "晃於=あきお,晋昌=ゆきあき,祐汰=ゆうた,紘明=ひろあき,玲児=れいじ,恭幸=やすゆき,真忠=まさただ",
			"10-8-F" => "花奈=かな・はるな,紗枝=さき・さえ,祐佳=ゆうか,真知=まち,晃奈=あきな,真依=まい,紘枝・洋枝・洋依・洋姉=ひろえ,紗知=さち,芹佳・芹果=せりか,留奈=るな,紗枝=さえ,晃奈=あきな,真侑=まゆ,花枝=はるえ,真季=まき,衿佳=えりか,益沙=みさ,真知=まち,祐史子=ゆみこ,花代子=かよこ",
			"10-11-M" => "芳浩=よしひろ,洋康=ひろやす,真敏=まさとし,晃浩=あきひろ,真敏=まさとし,洋規=ひろき,哲朗・芳朗=よしろう,剛健=よしたけ,紘章=ひろゆき,記英=のりひで,祐浩=まさひろ,洋章=ひろあき,剛英=たかひで",
			"10-13-M" => "祐暉・紘暉・洋暉=ひろき,真義=まさよし,芳琢・剛琢=よしたか,祐耶=ゆうや,晃郁=あきふみ,秦椰・晋耶=しんや,哲聖=のりまさ,真嗣=まさつぐ,洋裕=ひろゆき,恭琢=やすたか,真暉=まさき,洋靖=ひろやす,晃裕=あきひろ,晃靖=こうせい,祐聖=ゆうせい,凌勢=りょうせい,隼椰=じゅんや,晃暉=こうき,真嗣=しんじ,晋裕=ゆきひろ,恭脩=たかなお,高較=たかなお,剛嗣=たかし,拳裕=たかひろ,晃督=てるまさ,真寛=まさひろ,洋裕=ようすけ,哲耶=てつや,恭琢=やすたか,真義=まさよし,哲裕=のりひろ,晃義=あきよし,高義=たかよし,洋義=ひろよし,洋郁=ひろふみ,真琢=まさたか,哲耶=てつや,哲琢=よしたか・あきたか,真耶=まさや,真郁=まさふみ,洋聖=ひろまさ",
			"10-14-M" => "晋嘉=ゆきひろ,祐輔=ゆうすけ,洸誠=ひろあき,哲鳳=よしたか,真造=しんぞう,啄郎=たくろう,晋輔=しんすけ,迅鳳=としたか,真彰=まさあき,祐爾=ゆうじ,芳郎=よしろう,洋造=ようぞう,倫嘉=ともひろ,真鳳=まさたか,洋郎=ひろお,晃大朗=こうたろう,芳嘉=よしひろ,祐鳳=まさたか,洋輔=ようすけ,真三朗=しんざぶろう",
			"10-14-F" => "玲嘉=れいか,祐華=ゆうか,留実=るみ,紗綺=さき,夏実=なつみ,真維=まい,真瑚=まこ,留維=るい,洋実=ひろみ,芳嘉=よしか,洋瑚=ようこ,花嘉=はるか,祐実=ゆみ,芹華=せりか,祐実=ゆみ,栗寿=くりす,留実=るみ,紋華=あやか,玲嘉=れいか,衿華=えりか,花実=はるみ,洋瑚=ようこ,真梨子=まりこ,夏那子=かなこ,真由美=まゆみ",
			"10-15-M" => "真賢=さだまさ,洋慶=ひろやす,恭進=たかゆき,晋広=ゆきひろ,祐徳=まさのり,祐葵=ゆうき,哲賢=よしまさ,恭慶=たかやす,紘徳=ひろのり,洋輝=ひろき,哲賢=よしのり,隼進=としゆき,芳輝=よしてる,真輝=まさき,祐輝=ゆうき,剛瑠=たける,晋徳=あきのり,洸太朗=こうたろう",
			"10-15-F" => "花瑠=かる,祐葵=ゆうき,紗慧=さえ,真葉=まほ,玲嬉=たまき,晃慧=あきえ,花葉=かほ,真葵=まき,花葉=はなよ,芳慧=よしえ,洋慧=ひろえ,真葉=まよ,紗葉=さよ,花於里=かおり,真里亜=まりあ,留里枝=るりえ,紗於里=さおり,花奈江=かなえ,祐里佳=ゆりか,紗智子=さちこ,真理子=まりこ",
			"10-19-M" => "真穏=まさとし,晋拡=あきひろ,隼勧=としゆき,洋勧=ひろゆき,恭鏡=たかあき",
			"10-21-M" => "真芸=まき,祐芸=ゆき,紗保理=さおり,祐香理=ゆかり,真須美=ますみ,素美恵=すみえ",
			"20-1-M" => "耀一=よういち,馨一=けいいち,厳一=ひろかず,蔵一=まさかず,宝一=たかかず",
			"20-3-M" => "厳也=よしや,宝大=たけひろ,蔵士=まさし,継久=つねひさ,覚己=あきのり",
			"20-11-M" => "耀浩=あきひろ,耀英=あきひで,耀悠=てるひさ,厳規=ひろき,覚悠=よしひさ,蔵敏=まさとし",
			"20-12-M" => "宝詞=たかし,覚雄=あきお,蔵智=まさのり,厳暉=ひろき,覚琢=よしたか,蔵敬=まさのり"
		);
	}
}
?>