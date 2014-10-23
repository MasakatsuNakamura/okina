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
$Test = new pChart(420,420);
$Test->drawBackground(255,255,255);
$Test->setFontProperties(DRAW_FONT, 10);
// 外枠
$Test->drawFilledRoundedRectangle(7,7,400,400,5,240,240,240);
$Test->drawRoundedRectangle(5,5,400,400,5,230,230,230);
// レーダー描画エリア
$Test->setGraphArea(55,55,340,340);
// 内枠
$Test->drawFilledRoundedRectangle(30,30,370,370,5,254,254,254);
$Test->drawRoundedRectangle(30,30,370,370,5,220,220,220);

// レーダー設定
$Test->drawRadarAxis($DataSet->GetData(),$DataSet->GetDataDescription(),TRUE,
    20,100,100,100,130,230,230);  // サイズ, 文字RGB, 線RGB
// グラフ設定
$Test->drawFilledRadar($DataSet->GetData(),$DataSet->GetDataDescription(),
    40,20);                       // opacity, サイズ

// タイトル
$Test->setFontProperties(DRAW_FONT,10);
$Test->drawTitle(0,22,"各運勢のバランス(5段階評価)",50,50,50,400);

// 描画
$Test->Stroke();
?>
