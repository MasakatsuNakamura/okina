<?php
/*
 * にこにこカー GTR
 */
 
// クラス
include("pChart/pData.class");
include("pChart/pChart.class");
 
define("DRAW_FONT", "Fonts/ipagp.ttf");

// データ
$DataSet = new pData;
$DataSet->AddPoint(array("健康運","若年期運","基礎運","晩年運","対人運"),"Label");
$DataSet->AddPoint(array($_GET['kenkou'],$_GET['tenkaku'], $_GET['jinkaku'], $_GET['soukaku'], $_GET['gaikaku']),"Serie");
$DataSet->AddSerie("Serie");
$DataSet->SetAbsciseLabelSerie("Label");

// 初期設定
$Test = new pChart(320,320);
$Test->drawBackground(255,255,255);
$Test->setFontProperties(DRAW_FONT, 8);
// 外枠
$Test->drawFilledRoundedRectangle(7,7,313,313,5,240,240,240);
$Test->drawRoundedRectangle(5,5,315,315,5,230,230,230);
// レーダー描画エリア
$Test->setGraphArea(30,50,280,280);
// 内枠
$Test->drawFilledRoundedRectangle(15,30,295,292,5,254,254,254);
$Test->drawRoundedRectangle(15,30,295,295,5,220,220,220);

// レーダー設定
$Test->drawRadarAxis($DataSet->GetData(),$DataSet->GetDataDescription(),TRUE,
    20,100,100,100,130,230,230);  // サイズ, 文字RGB, 線RGB
// グラフ設定
$Test->drawFilledRadar($DataSet->GetData(),$DataSet->GetDataDescription(),
    40,20);                       // opacity, サイズ

// タイトル
$Test->setFontProperties(DRAW_FONT,10);
$Test->drawTitle(0,22,"各運勢のバランス(5段階評価)",50,50,50,300);

// 描画
$Test->Stroke();
?>
