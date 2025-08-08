#!/usr/bin/perl

#　↑サーバーの設定に合わせて変更してください。

#　画像フォルダへのパス
$imgfile = "./pics"; 

#########　設定はここまで　##########

require "./cgi-lib.pl";
&ReadParse;


print <<HTML;
Content-type: text/html

<html>
<body bgcolor=#$in{hada}>
<div id=body style="position:absolute; left:0px; top:0px;">
<img src="$imgfile/body.gif"></div>
<div id=atama style="position:absolute; left:20px; top:15px;">
<img src="$imgfile/atama$in{'atama'}.gif"></div>
<div id=eye style="position:absolute; left:26px; top:35px;">
<img src="$imgfile/eye$in{'eye'}.gif"></div>
<div id=hana style="position:absolute; left:36px; top:50px;">
<img src="$imgfile/hana$in{'hana'}.gif"></div>
<div id=kuti style="position:absolute; left:36px; top:60px;">
<img src="$imgfile/kuti$in{'kuti'}.gif"></div>
<div id=hair style="position:absolute; left:25px; top:55px;"><img src="$imgfile/kami$in{'kami'}.gif"></div>

<div id=asi style="position:absolute; left:25px; top:104px;"><img src="$imgfile/leg-$in{'leg'}.gif"></div>
<div id=ude style="position:absolute; left:5px; top:80px;"><img src="$imgfile/arm-$in{'arm'}.gif"></div>
<div id=kabuto style="position:absolute; left:0px; top:0px;"><img src="$imgfile/hlm-$in{'hlm'}.gif"></div>
<div id=chest style="position:absolute; left:20px; top:70px;"><img src="$imgfile/che-$in{'che'}.gif"></div>

<div id=wep style="position:absolute; left:0px; top:0px;"><img src="$imgfile/wp-$in{'wp'}.gif"></div>
<div id=tate style="position:absolute; left:65px; top:25px;"><img src="$imgfile/sld-$in{'sld'}.gif"></div>


</body></html>


HTML
exit;