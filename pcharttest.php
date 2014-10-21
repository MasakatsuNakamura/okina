<?php
/*
 * ニコニコ村
 */
 
// クラス
include("pChart/pData.class");
include("pChart/pChart.class");
 
define("DRAW_FONT",    "Fonts/ipagp.ttf");
 
// データ
$data = new pData;
$data->AddPoint(array(43,10,32,15),"Serie1");
$data->AddPoint(array("好き","嫌い","わからない","無回答"),"Serie2");
$data->AddAllSeries();
$data->SetAbsciseLabelSerie("Serie2");
 
// グラフ初期化
$pie = new pChart(430,330);
$pie->drawFilledRoundedRectangle(6,6,400,300,5,240,240,240);  // x,y,w,h,,r,g,b
$pie->drawRoundedRectangle(5,5,400,300,5,230,230,230);        // x,y,w,h,,r,g,b
   
// 円グラフ
$pie->setFontProperties(DRAW_FONT,10);
$pie->setShadowProperties(2,2,200,200,200);   // x,y,r,g,b
$pie->drawFlatPieGraphWithShadow($data->GetData(),$data->GetDataDescription(),
    160,160,90,PIE_PERCENTAGE,10);            // x,y,radius
// 凡例
$pie->drawPieLegend(290,20,$data->GetData(),$data->GetDataDescription(),250,250,250);  

// タイトル
$pie->setFontProperties(DRAW_FONT,14);
$pie->drawTitle(15,25,"ニコニコ村について",0,0,0);

// 描画
$pie->Stroke();
?>