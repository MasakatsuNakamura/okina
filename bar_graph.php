<?php
// Standard inclusions
include("pChart/pData.class");
include("pChart/pChart.class");

define("DRAW_FONT", "Fonts/ipagp.ttf");

// Dataset definition
$DataSet = new pData;
$DataSet->AddPoint(array("～20際", "20～40歳", "40～60歳", "60歳～", "総合"), "Serie1");
$DataSet->AddPoint(array($_GET['a'], $_GET['b'], $_GET['c'], $_GET['d'], $_GET['e']), "Serie2");
$DataSet->AddSerie("Serie2");
$DataSet->SetAbsciseLabelSerie("Serie1");
$DataSet->SetYAxisUnit("%");
$DataSet->SetYAxisName("運勢のパワー");

// Initialise the graph
// 初期設定
$Test = new pChart(320,320);
$Test->drawBackground(255,255,255);
$Test->setFontProperties(DRAW_FONT, 8);
$Test->setGraphArea(60,50,300,270);
$Test->drawFilledRoundedRectangle(7,7,313,313,5,240,240,240);
$Test->drawRoundedRectangle(5,5,315,315,5,230,230,230);
$Test->drawGraphArea(254,254,254,TRUE);
$Test->drawScale($DataSet->GetData(),$DataSet->GetDataDescription(),SCALE_ADDALLSTART0,150,150,150,TRUE,0,2,TRUE,1);
$Test->drawGrid(4,TRUE,230,230,230,50);

// Draw the 0 line
$Test->setFontProperties(DRAW_FONT, 6);
$Test->drawTreshold(0,143,55,72,FALSE,FALSE, 1);

// Draw the bar graph
$Test->drawBarGraph($DataSet->GetData(),$DataSet->GetDataDescription(),TRUE);

// Finish the graph
$Test->setFontProperties(DRAW_FONT,10);
$Test->drawTitle(0,22,"あなたの年齢別運勢",50,50,50,320);
$Test->Stroke();
?>
