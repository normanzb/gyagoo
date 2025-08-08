#!/usr/bin/perl

#@ªƒT[ƒo[‚Ìİ’è‚É‡‚í‚¹‚Ä•ÏX‚µ‚Ä‚­‚¾‚³‚¢B

require "./settei.cgi";
require "./cgi-lib.pl";
&ReadParse;



if ( $in{new} ne "" ){
	$charafremu = "<iframe name=\"charaga\" src=\"./$charapic?atama=$in{head}&eye=$in{me}&hana=$in{nose}&kuti=$in{mouth}&kami=$in{hair}&leg=$in{asi}&arm=$in{ude}&hlm=$in{kabuto}&che=$in{chest}&wp=$in{buki}&sld=$in{tate}&hada=$in{skin}\" frameborder=0 scrolling=no width=100 height=125></iframe><br><br>";
	$hitokoto ="<br><nobr> <font color=#$mojiiro2>”§‚ÌF‚ğÄ“x‘I‘ğ‚µ‚È‚¨‚µ‚Ä‚­‚¾‚³‚¢</font></nobr>";
	$hitokoto2 ="<nobr> <font color=#$mojiiro2>•¶šF‚ğÄ“x‘I‘ğ‚µ‚È‚¨‚µ‚Ä‚­‚¾‚³‚¢</font></nobr><br>";
}

if ( $in{head} eq ""){ $chkall = "checked";} else {
	$chkatama[$in{head}] = $chkeye[$in{me}] = $chkhana[$in{nose}] = $chkkuti[$in{mouth}] = $chkkami[$in{hair}] = $chkhada[$in{skin}] = $chksex[$in{sex}] = "checked";
}
&ipblock;
&gaibublock;
&cookieget;

if ( $in{new} eq "" || $in{new} eq "2" ){
&hpsaisyo;
print <<HTM;
<SCRIPT LANGUAGE="JavaScript">
<!--
function loading() {
    document.getElementById('load_page').style.visibility = 'hidden';
}
//-->
</script>
</HEAD>
<BODY OnLoad="loading()">
<div id="load_page" style="position: absolute; background-color: c8c8c8; height: 100%; width: 100%; text-align:center;">
<table width=100%><tr><td><font face=Westminster><font color=black><center><br><br><br><br><br><br><br><br><br>NOW LOADING...</center></font></font></td></tr></table>
</div>
<center><nobr><font size=7 color=#$mojiiro2>V‹Kì¬</font></nobr><br><br>
ŠeŠçƒp[ƒc‚ğ‘I‘ğ‚µA‚ ‚È‚½‚¾‚¯‚ÌƒLƒƒƒ‰‚ğì¬‚µ‚Ä‚­‚¾‚³‚¢B<br>
”[“¾‚ª‚¢‚­‚Ü‚Å‰½“x‚Å‚à\‚µ‚Ä‚İ‚Ü‚µ‚å‚¤B<br>
ˆê“x“o˜^‚µ‚Ä‚µ‚Ü‚¤‚Æ•ÏX‚Í‚Å‚«‚È‚¢‚Ì‚Å’ˆÓ‚µ‚Ä‚­‚¾‚³‚¢B<br><br>

$charafremu

<form method="post" action="./$sinki" method="POST">
<table border=1>
<tr><td>
”§</td><td>
<INPUT NAME="skin" TYPE=radio VALUE="ffdba9" checked><font size=5 color=#ffdba9>¡@</font>b@<wbr>
<INPUT NAME="skin" TYPE=radio VALUE="f0c488"><font size=5 color=#f0c488>¡@</font>b@<wbr>
<INPUT NAME="skin" TYPE=radio VALUE="e0ad66"><font size=5 color=#e0ad66>¡@</font>b@<wbr>
<INPUT NAME="skin" TYPE=radio VALUE="d19644"><font size=5 color=#d19644>¡@</font>b@<wbr>
<INPUT NAME="skin" TYPE=radio VALUE="c17f22"><font size=5 color=#c17f22>¡@</font>b@<wbr>
<INPUT NAME="skin" TYPE=radio VALUE="b16800"><font size=5 color=#b16800>¡@</font>b@<wbr>
<INPUT NAME="skin" TYPE=radio VALUE="ffffd1"><font size=5 color=#ffffd1>¡@</font>b@<wbr>
<INPUT NAME="skin" TYPE=radio VALUE="ffd1d1"><font size=5 color=#ffd1d1>¡@</font>b@<wbr>
<INPUT NAME="skin" TYPE=radio VALUE="938bcf"><font size=5 color=#938bcf>¡@</font>b@<wbr>
<INPUT NAME="skin" TYPE=radio VALUE="687eb7"><font size=5 color=#687eb7>¡@</font>b@<wbr>
<INPUT NAME="skin" TYPE=radio VALUE="d0ffd0"><font size=5 color=#d0ffd0>¡@</font>b@<wbr>
<INPUT NAME="skin" TYPE=radio VALUE="7ac57a"><font size=5 color=#7ac57a>¡@</font>b@<wbr>
</nobr>$hitokoto
</td></tr>

<tr><td>
”¯</td><td>

<nobr><INPUT NAME="head" TYPE=radio VALUE="1" $chkall$chkatama[1]>‚È‚µb<wbr>

<INPUT NAME="head" TYPE=radio VALUE="2" $chkatama[2]><img src="$maindir/$imgfile/atama2.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="3" $chkatama[3]><img src ="$maindir/$imgfile/atama3.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="4" $chkatama[4]><img src ="$maindir/$imgfile/atama4.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="5" $chkatama[5]><img src ="$maindir/$imgfile/atama5.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="6" $chkatama[6]><img src ="$maindir/$imgfile/atama6.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="7" $chkatama[7]><img src ="$maindir/$imgfile/atama7.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="8" $chkatama[8]><img src ="$maindir/$imgfile/atama8.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="9" $chkatama[9]><img src ="$maindir/$imgfile/atama9.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="10" $chkatama[10]><img src ="$maindir/$imgfile/atama10.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="11" $chkatama[11]><img src ="$maindir/$imgfile/atama11.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="12" $chkatama[12]><img src ="$maindir/$imgfile/atama12.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="13" $chkatama[13]><img src ="$maindir/$imgfile/atama13.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="14" $chkatama[14]><img src ="$maindir/$imgfile/atama14.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="15" $chkatama[15]><img src ="$maindir/$imgfile/atama15.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="16" $chkatama[16]><img src ="$maindir/$imgfile/atama16.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="17" $chkatama[17]><img src ="$maindir/$imgfile/atama17.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="18" $chkatama[18]><img src ="$maindir/$imgfile/atama18.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="19" $chkatama[19]><img src ="$maindir/$imgfile/atama19.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="20" $chkatama[20]><img src ="$maindir/$imgfile/atama20.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="21" $chkatama[21]><img src ="$maindir/$imgfile/atama21.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="22" $chkatama[22]><img src ="$maindir/$imgfile/atama22.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="23" $chkatama[23]><img src ="$maindir/$imgfile/atama23.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="24" $chkatama[24]><img src ="$maindir/$imgfile/atama24.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="25" $chkatama[25]><img src ="$maindir/$imgfile/atama25.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="26" $chkatama[26]><img src ="$maindir/$imgfile/atama26.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="27" $chkatama[27]><img src ="$maindir/$imgfile/atama27.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="28" $chkatama[28]><img src ="$maindir/$imgfile/atama28.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="29" $chkatama[29]><img src ="$maindir/$imgfile/atama29.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="30" $chkatama[30]><img src ="$maindir/$imgfile/atama30.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="31" $chkatama[31]><img src ="$maindir/$imgfile/atama31.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="32" $chkatama[32]><img src ="$maindir/$imgfile/atama32.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="33" $chkatama[33]><img src ="$maindir/$imgfile/atama33.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="34" $chkatama[34]><img src ="$maindir/$imgfile/atama34.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="35" $chkatama[35]><img src ="$maindir/$imgfile/atama35.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="36" $chkatama[36]><img src ="$maindir/$imgfile/atama36.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="37" $chkatama[37]><img src ="$maindir/$imgfile/atama37.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="38" $chkatama[38]><img src ="$maindir/$imgfile/atama38.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="39" $chkatama[39]><img src ="$maindir/$imgfile/atama39.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="40" $chkatama[40]><img src ="$maindir/$imgfile/atama40.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="41" $chkatama[41]><img src ="$maindir/$imgfile/atama41.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="42" $chkatama[42]><img src ="$maindir/$imgfile/atama42.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="43" $chkatama[43]><img src ="$maindir/$imgfile/atama43.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="44" $chkatama[44]><img src ="$maindir/$imgfile/atama44.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="45" $chkatama[45]><img src ="$maindir/$imgfile/atama45.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="46" $chkatama[46]><img src ="$maindir/$imgfile/atama46.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="47" $chkatama[47]><img src ="$maindir/$imgfile/atama47.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="48" $chkatama[48]><img src ="$maindir/$imgfile/atama48.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="49" $chkatama[49]><img src ="$maindir/$imgfile/atama49.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="50" $chkatama[50]><img src ="$maindir/$imgfile/atama50.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="51" $chkatama[51]><img src ="$maindir/$imgfile/atama51.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="52" $chkatama[52]><img src ="$maindir/$imgfile/atama52.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="53" $chkatama[53]><img src ="$maindir/$imgfile/atama53.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="54" $chkatama[54]><img src ="$maindir/$imgfile/atama54.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="55" $chkatama[55]><img src ="$maindir/$imgfile/atama55.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="56" $chkatama[56]><img src ="$maindir/$imgfile/atama56.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="57" $chkatama[57]><img src ="$maindir/$imgfile/atama57.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="58" $chkatama[58]><img src ="$maindir/$imgfile/atama58.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="59" $chkatama[59]><img src ="$maindir/$imgfile/atama59.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="60" $chkatama[60]><img src ="$maindir/$imgfile/atama60.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="61" $chkatama[61]><img src ="$maindir/$imgfile/atama61.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="62" $chkatama[62]><img src ="$maindir/$imgfile/atama62.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="63" $chkatama[63]><img src ="$maindir/$imgfile/atama63.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="64" $chkatama[64]><img src ="$maindir/$imgfile/atama64.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="65" $chkatama[65]><img src ="$maindir/$imgfile/atama65.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="66" $chkatama[66]><img src ="$maindir/$imgfile/atama66.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="67" $chkatama[67]><img src ="$maindir/$imgfile/atama67.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="68" $chkatama[68]><img src ="$maindir/$imgfile/atama68.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="69" $chkatama[69]><img src ="$maindir/$imgfile/atama69.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="70" $chkatama[70]><img src ="$maindir/$imgfile/atama70.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="71" $chkatama[71]><img src ="$maindir/$imgfile/atama71.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="72" $chkatama[72]><img src ="$maindir/$imgfile/atama72.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="73" $chkatama[73]><img src ="$maindir/$imgfile/atama73.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="74" $chkatama[74]><img src ="$maindir/$imgfile/atama74.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="75" $chkatama[75]><img src ="$maindir/$imgfile/atama75.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="76" $chkatama[76]><img src ="$maindir/$imgfile/atama76.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="77" $chkatama[77]><img src ="$maindir/$imgfile/atama77.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="78" $chkatama[78]><img src ="$maindir/$imgfile/atama78.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="79" $chkatama[79]><img src ="$maindir/$imgfile/atama79.gif">b<wbr>
<INPUT NAME="head" TYPE=radio VALUE="80" $chkatama[80]><img src ="$maindir/$imgfile/atama80.gif">b<wbr>
</nobr>
</td></tr>


<tr><td>
–Ú</td><td>
<b>‚Ü‚Î‚½‚«‚È‚µ</b><br>
<nobr>
<INPUT NAME="me" TYPE=radio VALUE="1" $chkall$chkeye[1]><img src="$maindir/$imgfile/eye1.gif">b<wbr>
<INPUT NAME="me" TYPE=radio VALUE="2" $chkeye[2]><img src="$maindir/$imgfile/eye2.gif">b<wbr>
<INPUT NAME="me" TYPE=radio VALUE="3" $chkeye[3]><img src="$maindir/$imgfile/eye3.gif">b<wbr>
<INPUT NAME="me" TYPE=radio VALUE="4" $chkeye[4]><img src="$maindir/$imgfile/eye4.gif">b<wbr>
<INPUT NAME="me" TYPE=radio VALUE="5" $chkeye[5]><img src="$maindir/$imgfile/eye5.gif">b<wbr>
<INPUT NAME="me" TYPE=radio VALUE="6" $chkeye[6]><img src="$maindir/$imgfile/eye6.gif">b<wbr>
<INPUT NAME="me" TYPE=radio VALUE="7" $chkeye[7]><img src="$maindir/$imgfile/eye7.gif">b<wbr>
<INPUT NAME="me" TYPE=radio VALUE="8" $chkeye[8]><img src="$maindir/$imgfile/eye8.gif">b<wbr>
<INPUT NAME="me" TYPE=radio VALUE="9" $chkeye[9]><img src="$maindir/$imgfile/eye9.gif">b<wbr>
<INPUT NAME="me" TYPE=radio VALUE="10" $chkeye[10]><img src="$maindir/$imgfile/eye10.gif">b<wbr>
<INPUT NAME="me" TYPE=radio VALUE="11" $chkeye[11]><img src="$maindir/$imgfile/eye11.gif">b<wbr>
<INPUT NAME="me" TYPE=radio VALUE="12" $chkeye[12]><img src="$maindir/$imgfile/eye12.gif">b<wbr>
<INPUT NAME="me" TYPE=radio VALUE="13" $chkeye[13]><img src="$maindir/$imgfile/eye13.gif">b<wbr>
<INPUT NAME="me" TYPE=radio VALUE="14" $chkeye[14]><img src="$maindir/$imgfile/eye14.gif">b<wbr>
<INPUT NAME="me" TYPE=radio VALUE="15" $chkeye[15]><img src="$maindir/$imgfile/eye15.gif">b<wbr>
<INPUT NAME="me" TYPE=radio VALUE="16" $chkeye[16]><img src="$maindir/$imgfile/eye16.gif">b<wbr>
<INPUT NAME="me" TYPE=radio VALUE="17" $chkeye[17]><img src="$maindir/$imgfile/eye17.gif">b<wbr>
<INPUT NAME="me" TYPE=radio VALUE="18" $chkeye[18]><img src="$maindir/$imgfile/eye18.gif">b<wbr>
<INPUT NAME="me" TYPE=radio VALUE="19" $chkeye[19]><img src="$maindir/$imgfile/eye19.gif">b<wbr>
<INPUT NAME="me" TYPE=radio VALUE="20" $chkeye[20]><img src="$maindir/$imgfile/eye20.gif">b<wbr>
<INPUT NAME="me" TYPE=radio VALUE="21" $chkeye[21]><img src="$maindir/$imgfile/eye21.gif">b<wbr>
<INPUT NAME="me" TYPE=radio VALUE="22" $chkeye[22]><img src="$maindir/$imgfile/eye22.gif">b<wbr>
<INPUT NAME="me" TYPE=radio VALUE="23" $chkeye[23]><img src="$maindir/$imgfile/eye23.gif">b<wbr>
<INPUT NAME="me" TYPE=radio VALUE="24" $chkeye[24]><img src="$maindir/$imgfile/eye24.gif">b<wbr>
<br>
<b>‚Ü‚Î‚½‚«‚ ‚è</b><br>
<INPUT NAME="me" TYPE=radio VALUE="25" $chkeye[25]><img src="$maindir/$imgfile/eye25.gif">b<wbr>
<INPUT NAME="me" TYPE=radio VALUE="26" $chkeye[26]><img src="$maindir/$imgfile/eye26.gif">b<wbr>
<INPUT NAME="me" TYPE=radio VALUE="27" $chkeye[27]><img src="$maindir/$imgfile/eye27.gif">b<wbr>
<INPUT NAME="me" TYPE=radio VALUE="28" $chkeye[28]><img src="$maindir/$imgfile/eye28.gif">b<wbr>
<INPUT NAME="me" TYPE=radio VALUE="29" $chkeye[29]><img src="$maindir/$imgfile/eye29.gif">b<wbr>
<INPUT NAME="me" TYPE=radio VALUE="30" $chkeye[30]><img src="$maindir/$imgfile/eye30.gif">b<wbr>
<INPUT NAME="me" TYPE=radio VALUE="31" $chkeye[31]><img src="$maindir/$imgfile/eye31.gif">b<wbr>
<INPUT NAME="me" TYPE=radio VALUE="32" $chkeye[32]><img src="$maindir/$imgfile/eye32.gif">b<wbr>
<INPUT NAME="me" TYPE=radio VALUE="33" $chkeye[33]><img src="$maindir/$imgfile/eye33.gif">b<wbr>
<INPUT NAME="me" TYPE=radio VALUE="34" $chkeye[34]><img src="$maindir/$imgfile/eye34.gif">b<wbr>
<INPUT NAME="me" TYPE=radio VALUE="35" $chkeye[35]><img src="$maindir/$imgfile/eye35.gif">b<wbr>
<INPUT NAME="me" TYPE=radio VALUE="36" $chkeye[36]><img src="$maindir/$imgfile/eye36.gif">b<wbr>
<INPUT NAME="me" TYPE=radio VALUE="37" $chkeye[37]><img src="$maindir/$imgfile/eye37.gif">b<wbr>
<INPUT NAME="me" TYPE=radio VALUE="38" $chkeye[38]><img src="$maindir/$imgfile/eye38.gif">b<wbr>
<INPUT NAME="me" TYPE=radio VALUE="39" $chkeye[39]><img src="$maindir/$imgfile/eye39.gif">b<wbr>
<INPUT NAME="me" TYPE=radio VALUE="40" $chkeye[40]><img src="$maindir/$imgfile/eye40.gif">b<wbr>
<INPUT NAME="me" TYPE=radio VALUE="41" $chkeye[41]><img src="$maindir/$imgfile/eye41.gif">b<wbr>
<INPUT NAME="me" TYPE=radio VALUE="42" $chkeye[42]><img src="$maindir/$imgfile/eye42.gif">b<wbr>
<INPUT NAME="me" TYPE=radio VALUE="43" $chkeye[43]><img src="$maindir/$imgfile/eye43.gif">b<wbr>
<INPUT NAME="me" TYPE=radio VALUE="44" $chkeye[44]><img src="$maindir/$imgfile/eye44.gif">b<wbr>
<INPUT NAME="me" TYPE=radio VALUE="45" $chkeye[45]><img src="$maindir/$imgfile/eye45.gif">b<wbr>
</nobr>
</td></tr>


<tr><td>
•@</td><td>
<nobr>
<INPUT NAME="nose" TYPE=radio VALUE="1" $chkall$chkhana[1]><img src="$maindir/$imgfile/hana1.gif">b<wbr>
<INPUT NAME="nose" TYPE=radio VALUE="2" $chkhana[2]><img src="$maindir/$imgfile/hana2.gif">b<wbr>
<INPUT NAME="nose" TYPE=radio VALUE="3" $chkhana[3]><img src="$maindir/$imgfile/hana3.gif">b<wbr>
<INPUT NAME="nose" TYPE=radio VALUE="4" $chkhana[4]><img src="$maindir/$imgfile/hana4.gif">b<wbr>
<INPUT NAME="nose" TYPE=radio VALUE="5" $chkhana[5]><img src="$maindir/$imgfile/hana5.gif">b<wbr>
<INPUT NAME="nose" TYPE=radio VALUE="6" $chkhana[6]><img src="$maindir/$imgfile/hana6.gif">b<wbr>
<INPUT NAME="nose" TYPE=radio VALUE="7" $chkhana[7]><img src="$maindir/$imgfile/hana7.gif">b<wbr>
<INPUT NAME="nose" TYPE=radio VALUE="8" $chkhana[8]><img src="$maindir/$imgfile/hana8.gif">b<wbr>
<INPUT NAME="nose" TYPE=radio VALUE="9" $chkhana[9]><img src="$maindir/$imgfile/hana9.gif">b<wbr>
<INPUT NAME="nose" TYPE=radio VALUE="10" $chkhana[10]><img src="$maindir/$imgfile/hana10.gif">b<wbr>
<INPUT NAME="nose" TYPE=radio VALUE="11" $chkhana[11]><img src="$maindir/$imgfile/hana11.gif">b<wbr>
<INPUT NAME="nose" TYPE=radio VALUE="12" $chkhana[12]><img src="$maindir/$imgfile/hana12.gif">b<wbr>
<INPUT NAME="nose" TYPE=radio VALUE="13" $chkhana[13]><img src="$maindir/$imgfile/hana13.gif">b<wbr>
<INPUT NAME="nose" TYPE=radio VALUE="14" $chkhana[14]><img src="$maindir/$imgfile/hana14.gif">b<wbr>
<INPUT NAME="nose" TYPE=radio VALUE="15" $chkhana[15]><img src="$maindir/$imgfile/hana15.gif">b<wbr>
<INPUT NAME="nose" TYPE=radio VALUE="16" $chkhana[16]><img src="$maindir/$imgfile/hana16.gif">b<wbr>
<INPUT NAME="nose" TYPE=radio VALUE="17" $chkhana[17]><img src="$maindir/$imgfile/hana17.gif">b<wbr>
<INPUT NAME="nose" TYPE=radio VALUE="18" $chkhana[18]><img src="$maindir/$imgfile/hana18.gif">b<wbr>
<INPUT NAME="nose" TYPE=radio VALUE="19" $chkhana[19]><img src="$maindir/$imgfile/hana19.gif">b<wbr>
</nobr>
</td></tr>


<tr><td>
Œû</td><td>
<nobr>
<INPUT NAME="mouth" TYPE=radio VALUE="1" $chkall$chkkuti[1]><img src="$maindir/$imgfile/kuti1.gif">b<wbr>
<INPUT NAME="mouth" TYPE=radio VALUE="2" $chkkuti[2]><img src="$maindir/$imgfile/kuti2.gif">b<wbr>
<INPUT NAME="mouth" TYPE=radio VALUE="3" $chkkuti[3]><img src="$maindir/$imgfile/kuti3.gif">b<wbr>
<INPUT NAME="mouth" TYPE=radio VALUE="4" $chkkuti[4]><img src="$maindir/$imgfile/kuti4.gif">b<wbr>
<INPUT NAME="mouth" TYPE=radio VALUE="5" $chkkuti[5]><img src="$maindir/$imgfile/kuti5.gif">b<wbr>
<INPUT NAME="mouth" TYPE=radio VALUE="6" $chkkuti[6]><img src="$maindir/$imgfile/kuti6.gif">b<wbr>
<INPUT NAME="mouth" TYPE=radio VALUE="7" $chkkuti[7]><img src="$maindir/$imgfile/kuti7.gif">b<wbr>
<INPUT NAME="mouth" TYPE=radio VALUE="8" $chkkuti[8]><img src="$maindir/$imgfile/kuti8.gif">b<wbr>
<INPUT NAME="mouth" TYPE=radio VALUE="9" $chkkuti[9]><img src="$maindir/$imgfile/kuti9.gif">b<wbr>
<INPUT NAME="mouth" TYPE=radio VALUE="10" $chkkuti[10]><img src="$maindir/$imgfile/kuti10.gif">b<wbr>
<INPUT NAME="mouth" TYPE=radio VALUE="11" $chkkuti[11]><img src="$maindir/$imgfile/kuti11.gif">b<wbr>
<INPUT NAME="mouth" TYPE=radio VALUE="12" $chkkuti[12]><img src="$maindir/$imgfile/kuti12.gif">b<wbr>
<INPUT NAME="mouth" TYPE=radio VALUE="13" $chkkuti[13]><img src="$maindir/$imgfile/kuti13.gif">b<wbr>
<INPUT NAME="mouth" TYPE=radio VALUE="14" $chkkuti[14]><img src="$maindir/$imgfile/kuti14.gif">b<wbr>
<INPUT NAME="mouth" TYPE=radio VALUE="15" $chkkuti[15]><img src="$maindir/$imgfile/kuti15.gif">b<wbr>
<INPUT NAME="mouth" TYPE=radio VALUE="16" $chkkuti[16]><img src="$maindir/$imgfile/kuti16.gif">b<wbr>
<INPUT NAME="mouth" TYPE=radio VALUE="17" $chkkuti[17]><img src="$maindir/$imgfile/kuti17.gif">b<wbr>
<INPUT NAME="mouth" TYPE=radio VALUE="18" $chkkuti[18]><img src="$maindir/$imgfile/kuti18.gif">b<wbr>
<INPUT NAME="mouth" TYPE=radio VALUE="19" $chkkuti[19]><img src="$maindir/$imgfile/kuti19.gif">b<wbr>
<INPUT NAME="mouth" TYPE=radio VALUE="20" $chkkuti[20]><img src="$maindir/$imgfile/kuti20.gif">b<wbr>
<INPUT NAME="mouth" TYPE=radio VALUE="0" $chkkuti[0]><img src="$maindir/$imgfile/kuti0.gif">b<wbr>
<INPUT NAME="mouth" TYPE=radio VALUE="21" $chkkuti[21]><img src="$maindir/$imgfile/kuti21.gif">b<wbr>
<INPUT NAME="mouth" TYPE=radio VALUE="22" $chkkuti[22]><img src="$maindir/$imgfile/kuti22.gif">b<wbr>
<INPUT NAME="mouth" TYPE=radio VALUE="23" $chkkuti[23]><img src="$maindir/$imgfile/kuti23.gif">b<wbr>
<INPUT NAME="mouth" TYPE=radio VALUE="24" $chkkuti[24]><img src="$maindir/$imgfile/kuti24.gif">b<wbr>
<INPUT NAME="mouth" TYPE=radio VALUE="25" $chkkuti[25]><img src="$maindir/$imgfile/kuti25.gif">b<wbr>
</nobr>
</td></tr>


<tr><td>
<nobr>Œã‚ë”¯</td><td>
<nobr>
<INPUT NAME="hair" TYPE=radio VALUE="1" $chkall$chkkami[1]>‚È‚µb<wbr>
<INPUT NAME="hair" TYPE=radio VALUE="2" $chkkami[2]><img src="$maindir/$imgfile/kami2.gif">b<wbr>
<INPUT NAME="hair" TYPE=radio VALUE="3" $chkkami[3]><img src="$maindir/$imgfile/kami3.gif">b<wbr>
<INPUT NAME="hair" TYPE=radio VALUE="4" $chkkami[4]><img src="$maindir/$imgfile/kami4.gif">b<wbr>
<INPUT NAME="hair" TYPE=radio VALUE="5" $chkkami[5]><img src="$maindir/$imgfile/kami5.gif">b<wbr>
<INPUT NAME="hair" TYPE=radio VALUE="6" $chkkami[6]><img src="$maindir/$imgfile/kami6.gif">b<wbr>
<INPUT NAME="hair" TYPE=radio VALUE="7" $chkkami[7]><img src="$maindir/$imgfile/kami7.gif">b<wbr>
<INPUT NAME="hair" TYPE=radio VALUE="8" $chkkami[8]><img src="$maindir/$imgfile/kami8.gif">b<wbr>
<INPUT NAME="hair" TYPE=radio VALUE="9" $chkkami[9]><img src="$maindir/$imgfile/kami9.gif">b<wbr>
<INPUT NAME="hair" TYPE=radio VALUE="10" $chkkami[10]><img src="$maindir/$imgfile/kami10.gif">b<wbr>
<INPUT NAME="hair" TYPE=radio VALUE="11" $chkkami[11]><img src="$maindir/$imgfile/kami11.gif">b<wbr>
<INPUT NAME="hair" TYPE=radio VALUE="12" $chkkami[12]><img src="$maindir/$imgfile/kami12.gif">b<wbr>
<INPUT NAME="hair" TYPE=radio VALUE="13" $chkkami[13]><img src="$maindir/$imgfile/kami13.gif">b<wbr>

<INPUT NAME="hair" TYPE=radio VALUE="23" $chkkami[23]><img src="$maindir/$imgfile/kami23.gif">b<wbr>
<INPUT NAME="hair" TYPE=radio VALUE="24" $chkkami[24]><img src="$maindir/$imgfile/kami24.gif">b<wbr>
<INPUT NAME="hair" TYPE=radio VALUE="25" $chkkami[25]><img src="$maindir/$imgfile/kami25.gif">b<wbr>
<INPUT NAME="hair" TYPE=radio VALUE="26" $chkkami[26]><img src="$maindir/$imgfile/kami26.gif">b<wbr>
<INPUT NAME="hair" TYPE=radio VALUE="27" $chkkami[27]><img src="$maindir/$imgfile/kami27.gif">b<wbr>
<INPUT NAME="hair" TYPE=radio VALUE="28" $chkkami[28]><img src="$maindir/$imgfile/kami28.gif">b<wbr>
<INPUT NAME="hair" TYPE=radio VALUE="29" $chkkami[29]><img src="$maindir/$imgfile/kami29.gif">b<wbr>
<INPUT NAME="hair" TYPE=radio VALUE="30" $chkkami[30]><img src="$maindir/$imgfile/kami30.gif">b<wbr>
<INPUT NAME="hair" TYPE=radio VALUE="31" $chkkami[31]><img src="$maindir/$imgfile/kami31.gif">b<wbr>
<INPUT NAME="hair" TYPE=radio VALUE="32" $chkkami[32]><img src="$maindir/$imgfile/kami32.gif">b<wbr>
<INPUT NAME="hair" TYPE=radio VALUE="33" $chkkami[33]><img src="$maindir/$imgfile/kami33.gif">b<wbr>
<INPUT NAME="hair" TYPE=radio VALUE="34" $chkkami[34]><img src="$maindir/$imgfile/kami34.gif">b<wbr>
<INPUT NAME="hair" TYPE=radio VALUE="35" $chkkami[35]><img src="$maindir/$imgfile/kami35.gif">b<wbr>
<INPUT NAME="hair" TYPE=radio VALUE="36" $chkkami[36]><img src="$maindir/$imgfile/kami36.gif">b<wbr>
<INPUT NAME="hair" TYPE=radio VALUE="37" $chkkami[37]><img src="$maindir/$imgfile/kami37.gif">b<wbr>
<INPUT NAME="hair" TYPE=radio VALUE="38" $chkkami[38]><img src="$maindir/$imgfile/kami38.gif">b<wbr>
<INPUT NAME="hair" TYPE=radio VALUE="39" $chkkami[39]><img src="$maindir/$imgfile/kami39.gif">b<wbr>
<INPUT NAME="hair" TYPE=radio VALUE="40" $chkkami[40]><img src="$maindir/$imgfile/kami40.gif">b<wbr>
<INPUT NAME="hair" TYPE=radio VALUE="41" $chkkami[41]><img src="$maindir/$imgfile/kami41.gif">b<wbr>
<INPUT NAME="hair" TYPE=radio VALUE="42" $chkkami[42]><img src="$maindir/$imgfile/kami42.gif">b<wbr>
<INPUT NAME="hair" TYPE=radio VALUE="43" $chkkami[43]><img src="$maindir/$imgfile/kami43.gif">b<wbr>
<INPUT NAME="hair" TYPE=radio VALUE="44" $chkkami[44]><img src="$maindir/$imgfile/kami44.gif">b<wbr>
<INPUT NAME="hair" TYPE=radio VALUE="45" $chkkami[45]><img src="$maindir/$imgfile/kami45.gif">b<wbr>
<INPUT NAME="hair" TYPE=radio VALUE="46" $chkkami[46]><img src="$maindir/$imgfile/kami46.gif">b<wbr>
<INPUT NAME="hair" TYPE=radio VALUE="47" $chkkami[47]><img src="$maindir/$imgfile/kami47.gif">b<wbr>
<INPUT NAME="hair" TYPE=radio VALUE="48" $chkkami[48]><img src="$maindir/$imgfile/kami48.gif">b<wbr>
<INPUT NAME="hair" TYPE=radio VALUE="49" $chkkami[49]><img src="$maindir/$imgfile/kami49.gif">b<wbr>
<INPUT NAME="hair" TYPE=radio VALUE="50" $chkkami[50]><img src="$maindir/$imgfile/kami50.gif">b<wbr>
<INPUT NAME="hair" TYPE=radio VALUE="51" $chkkami[51]><img src="$maindir/$imgfile/kami51.gif">b<wbr>
<INPUT NAME="hair" TYPE=radio VALUE="52" $chkkami[52]><img src="$maindir/$imgfile/kami52.gif">b<wbr>
<INPUT NAME="hair" TYPE=radio VALUE="53" $chkkami[53]><img src="$maindir/$imgfile/kami53.gif">b<wbr>
<INPUT NAME="hair" TYPE=radio VALUE="54" $chkkami[54]><img src="$maindir/$imgfile/kami54.gif">b<wbr>
<INPUT NAME="hair" TYPE=radio VALUE="55" $chkkami[55]><img src="$maindir/$imgfile/kami55.gif">b<wbr>
<INPUT NAME="hair" TYPE=radio VALUE="56" $chkkami[56]><img src="$maindir/$imgfile/kami56.gif">b<wbr>
<INPUT NAME="hair" TYPE=radio VALUE="57" $chkkami[57]><img src="$maindir/$imgfile/kami57.gif">b<wbr>
<INPUT NAME="hair" TYPE=radio VALUE="58" $chkkami[58]><img src="$maindir/$imgfile/kami58.gif">b<wbr>
<INPUT NAME="hair" TYPE=radio VALUE="59" $chkkami[59]><img src="$maindir/$imgfile/kami59.gif">b<wbr>
<INPUT NAME="hair" TYPE=radio VALUE="60" $chkkami[60]><img src="$maindir/$imgfile/kami60.gif">b<wbr>
<INPUT NAME="hair" TYPE=radio VALUE="61" $chkkami[61]><img src="$maindir/$imgfile/kami61.gif">b<wbr>
<INPUT NAME="hair" TYPE=radio VALUE="62" $chkkami[62]><img src="$maindir/$imgfile/kami62.gif">b<wbr>
<INPUT NAME="hair" TYPE=radio VALUE="63" $chkkami[63]><img src="$maindir/$imgfile/kami63.gif">b<wbr>

</nobr>
</td></tr>

<tr><td>

<nobr>•¶šF</nobr></td><td>$hitokoto2
<select name="mojisyoku">
<option value="000000" selected>•
<option value="dd0000">Ô
<option value="0000dd">Â
<option value="009900">—Î
<option value="ffbb00">‰©
<option value="00aaaa">…
<option value="00bb00">‰©—Î
<option value="ff55ff">“
<option value="a96800">’ƒ
<option value="af00af">‡
<option value="666666">‹â
<option value="888800">‹à
<option value="ff8500">ò
<option value="7800d3">Â‡
</select><br><ul>
<table border=0>
<tr><td width=30><b><center><font color=#000000>•</font></b></center></td>
<td width=30><b><center><font color=#dd0000>Ô</font></b></center></td>
<td width=30><b><center><font color=#0000dd>Â</font></b></center></td>
<td width=30><b><center><font color=#009900>—Î</font></b></center></td>
<td width=30><b><center><font color=#ffbb00>‰©</font></b></center></td>
<td width=30><b><center><font color=#00aaaa>…</font></b></center></td>
<td width=30><b><center><font color=#00cc00>‰©—Î</font></b></center></td></tr>
<tr>
<td width=30><b><center><font color=#ff55ff>“</font></b></center></td>
<td width=30><b><center><font color=#a96800>’ƒ</font></b></center></td>
<td width=30><b><center><font color=#af00af>‡</font></b></center></td>
<td width=30><b><center><font color=#666666>‹â</font></b></center></td>
<td width=30><b><center><font color=#888800>‹à</font></b></center></td>
<td width=30><b><center><font color=#ff8500>ò</font></b></center></td>
<td width=30><b><center><font color=#7800d3>Â‡</font></b></center></td>
</tr>
</table></ul>
</td></tr>
<tr><td>«•Ê</td>
<td><input name="sex" type="radio" value="1" $chkall$chksex[1]>‰@b@<input name="sex" type="radio" value="2" $chksex[2]>Š</td></tr>
</table><br><br>

<table border=0>
<tr><td>ƒLƒƒƒ‰–¼F</td><td>
<INPUT NAME="sinkinamae" TYPE="text" size=20 value="$in{sinkinamae}">i‘SŠp‚P‚OšˆÈ“àj
</td></tr><tr><td>‚h‚cF</td>
<td><INPUT NAME="usrid" TYPE="text" size=8 value="$in{usrid}"><nobr>i”¼Šp‰p”š‚S`‚WšjƒQ[ƒ€’†‚É\ƒ\\[ƒX‚Å\•\\‹L‚³‚ê‚é‚à‚Ì‚È‚Ì‚Å’ˆÓ</nobr>
</td></tr><tr><td>ƒpƒXƒ[ƒhF</td>
<td><INPUT NAME="sinkipass" TYPE="password" size=8><nobr>i”¼Šp‰p”š‚S`‚Wšj<b><font color=red>ID‚©‚ç˜A‘z‚³‚ê‚éƒpƒX‚â˜A”Ô“™‚ÌƒpƒX‚Íİ’è‚µ‚È‚¢‚Å‚­‚¾‚³‚¢B</b></font></nobr>
</td></tr>
<tr><td></td><td><INPUT NAME="sinkipass2" TYPE="password" size=8>i”O‚Ì‚½‚ß‚à‚¤‚P“xƒpƒXƒ[ƒh“ü—Íj
</td></tr>
<tr><td>ƒz[ƒ€ƒy[ƒWF</td>
<td><INPUT NAME="sinkihome" TYPE="text" size=80 value="$in{sinkihome}">
</td></tr></table>
<INPUT NAME="new" TYPE=hidden VALUE="1">

<INPUT TYPE=submit VALUE="___‚Æ‚è‚ ‚¦‚¸‰¼“o˜^___">
HTM


} elsif ( $in{new} eq "1" ) {

	if(length($in{sinkinamae}) < 1 || length($in{sinkinamae}) > 20){ &hpsaisyo;print "<br><center><font size=6 color=\#$mojiiro2>ƒLƒƒƒ‰–¼‚Ì—“‚ª‹ó”’‚©•¶š”‚ª’·‚·‚¬‚Ü‚·I</font><br></center><br>";&sinkierr;exit;}
	if(length($in{usrid}) < 4 || length($in{usrid}) > 8 ){ &hpsaisyo;print "<br><center><font size=6 color=\#$mojiiro2>ID‚Ì•¶š”ŠÔˆá‚¢‚Å‚·I</font><br></center><br>";&sinkierr;exit;}
	if(length($in{sinkipass}) < 4 || length($in{sinkipass}) > 8 ){ &hpsaisyo;print "<br><center><font size=6 color=\#$mojiiro2>ƒpƒXƒ[ƒh‚Ì•¶š”ŠÔˆá‚¢‚Å‚·I</font><br></center><br>";&sinkierr;exit;}
	if( $in{sinkipass} ne $in{sinkipass2} ){ &hpsaisyo;print "<br><center><font size=6 color=\#$mojiiro2>“ü—Í‚³‚ê‚½‚Q‚Â‚ÌƒpƒXƒ[ƒh‚ª‡’v‚µ‚Ü‚¹‚ñI</font><br></center><br>";&sinkierr;exit;}
	if(length($in{sinkihome})  > 80 ){ &hpsaisyo;print "<br><center><font size=6 color=\#$mojiiro2>ƒz[ƒ€ƒy[ƒWƒAƒhƒŒƒX‚Ì•¶š”‚ª’·‚·‚¬‚Ü‚·I</font><br></center><br>";&sinkierr;exit;}
	if( $in{sinkinamae} =~ /ŠÇ—/){ &hpsaisyo;print "<br><center><font size=5 color=\#$mojiiro2>‘¼‚ÌƒvƒŒƒCƒ„[‚ÉŒë‰ğ‚ğµ‚­‹°‚ê‚ª‚ ‚éˆ×A<br>ƒLƒƒƒ‰–¼‚ÉA‚»‚Ì–¼‘O‚ğ•t‚¯‚é‚±‚Æ‚Í‚Å‚«‚Ü‚¹‚ñB<br>‚²—¹³‚­‚¾‚³‚¢B</font><br></center><br>";&sinkierr;exit;}
	if( $in{sex} eq "1" ){$chasex = "’j";} else {$chasex = "—";}

$in{sinkinamae} =~ s/</&lt;/g;
$in{sinkinamae} =~ s/>/&gt;/g;
$in{sinkinamae} =~ s/,/./g;
$in{sinkinamae} =~ s/\//_/g;
$in{usrid} =~ s/</&lt;/g;
$in{usrid} =~ s/>/&gt;/g;
$in{usrid} =~ s/,/./g;
$in{usrid} =~ s/\//_/g;
$in{sinkipass} =~ s/</&lt;/g;
$in{sinkipass} =~ s/>/&gt;/g;
$in{sinkipass} =~ s/,/./g;
$in{sinkipass} =~ s/\//_/g;
$in{sinkihome} =~ s/</&lt;/g;
$in{sinkihome} =~ s/>/&gt;/g;
$in{sinkihome} =~ s/,/./g;
&hpsaisyo;

print <<HTML2;

<center>
ƒLƒƒƒ‰‰æ‘œ‚ª•\\¦‚³‚ê‚È‚¢•û‚Í‚±‚Ìƒ{ƒ^ƒ“‚ğ‰Ÿ‚µ‚ÄŠm”F‚µ‚Ä‚­‚¾‚³‚¢B
<FORM>
<INPUT TYPE="button" NAME="win" VALUE="ƒlƒXƒPg—pÒ—pƒLƒƒƒ‰‰æ‘œ•\\¦" onClick="guide()">
</FORM>
<script language="JavaScript">
function guide()
{
window.open("./$charapic?atama=$in{head}&hada=$in{skin}&eye=$in{me}&hana=$in{nose}&kuti=$in{mouth}&kami=$in{hair}","","width=100,height=125")
}
</script>
$charafremu
<br><br>
<table border=1>
<tr><td>ƒLƒƒƒ‰–¼</td><td><font color=#$in{mojisyoku}>$in{sinkinamae}</font></td></tr>
<tr><td>‚h‚c</td><td><font color=#$in{mojisyoku}>$in{usrid}</font></td></tr>
<tr><td>ƒpƒXƒ[ƒh</td><td><font color=#$in{mojisyoku}>$in{sinkipass}</font></td></tr>
<tr><td><nobr>ƒz[ƒ€ƒy[ƒW</nobr></td><td><nobr><font color=#$in{mojisyoku}><a href="$in{sinkihome}" target="_blank">$in{sinkihome}</a></font></td></tr>
<tr><td>«•Ê</td><td><font color=#$in{mojisyoku}>$chasex</font></td></tr>

</table>
<br><br>
‚±‚ÌƒLƒƒƒ‰İ’è‚Å“o˜^‚µ‚Ü‚·‚©H<br><br>
<form method="post" action="./$sinki">
<INPUT NAME="new" TYPE=hidden VALUE="3">
<INPUT NAME="head" TYPE=hidden VALUE="$in{head}">
<INPUT NAME="me" TYPE=hidden VALUE="$in{me}">
<INPUT NAME="nose" TYPE=hidden VALUE="$in{nose}">
<INPUT NAME="mouth" TYPE=hidden VALUE="$in{mouth}">
<INPUT NAME="hair" TYPE=hidden VALUE="$in{hair}">
<INPUT NAME="skin" TYPE=hidden VALUE="$in{skin}">
<INPUT NAME="sinkinamae" TYPE=hidden VALUE="$in{sinkinamae}">
<INPUT NAME="mojisyoku" TYPE=hidden VALUE="$in{mojisyoku}">
<INPUT NAME="sinkihome" TYPE=hidden VALUE="$in{sinkihome}">
<INPUT NAME="sex" TYPE=hidden VALUE="$in{sex}">
<INPUT NAME="usrid" TYPE=hidden VALUE="$in{usrid}">
<INPUT NAME="sinkipass" TYPE=hidden VALUE="$in{sinkipass}">
<INPUT TYPE=submit VALUE="___ “o˜^‚·‚é ___">
</form>
<br>

HTML2
&sinkierr


} else {


open(IN,"$maindir/$foldacha/user_id$bousi2cha$bousikts2");
	while ($line = <IN>) {
		($fukuid,$fukuname) = split(/\//,$line);
		if ($fukuid eq $in{usrid}) {$fukuid2 = "1";}
		if ($fukuname eq $in{sinkinamae}) {$fukuname2 = "1";}
	}
close(IN);

if ($fukuid2 eq "1") {&hpsaisyo;print "<font size=6 color=#$mojiiro3>‚»‚ÌID‚Í‚·‚Å‚É“o˜^Ï‚Å‚·I<br>ID‚ğ•ÏX‚µAÄ“o˜^‚µ‚Ä‚­‚¾‚³‚¢B</font><br><br>";&sinkierr;exit;}
if ($fukuname2 eq "1") {&hpsaisyo;print "<font size=6 color=#$mojiiro3>‚»‚ÌƒLƒƒƒ‰–¼‚Í‚·‚Å‚É“o˜^Ï‚Å‚·I<br>ƒLƒƒƒ‰–¼‚ğ•ÏX‚µAÄ“o˜^‚µ‚Ä‚­‚¾‚³‚¢B</font><br><br>";&sinkierr;exit;}
if ($in{usrid} eq $in{sinkipass} ) {&hpsaisyo;print "<font size=6 color=#$mojiiro3>ID‚ÆƒpƒXƒ[ƒh‚ª“¯‚¶‚Å‚·I<br>ID‚ÆƒpƒXƒ[ƒh‚Í•K‚¸•Ê‚È‚à‚Ì‚É‚µ‚Ä‚­‚¾‚³‚¢B</font><br><br>";&sinkierr;exit;}
if( $in{sex} eq "1" ){$chasex = "’j";} else {$chasex = "—";}

$chaid = $in{usrid};$chapass = $in{sinkipass};$chaname = $in{sinkinamae};$chaurl = $in{sinkihome};
$chamoji = "$in{mojisyoku}";$chaclass = $chaexp = $chaplace = "0";
$chagold = "100";$chalvl = $chastats[0] = "1";$chastats[9] = $chahp = "30";
$chastats[1] = "2";
$chastats[2] = $chastats[3] = $chastats[4] = $chastats[5] = $chastats[6] = $chastats[7] = $chastats[8] = "10";
$nowstrexp = $nowacexp = $nowagiexp = $nowintexp = "0";
$strexp = "10";
$acexp = "10";
$agiexp = "2";
$intexp = "3";
$chaage = "15";
$chastats[10] = $chastats[12] = "0";
$chastats[13] = "10";
$chastats[14] = "0";
$chastats[15] = "0";
$chastats[11] = "0";
$chastats[16] = $champ = "20";
$morai = "10";
$hukubiki = "0";
$chaitem[1] = "ƒ|[ƒVƒ‡ƒ“";$chaeff[1] = "3";$chasetumei[1] = "HP‚ğ100‰ñ•œ";
$chasoubi[5] ="—·l‚ÌƒYƒ{ƒ“";
$chasoubi[4] = "—·l‚Ì•";
$chasoubi[1] = "ƒ_ƒK[";
$chaskin = $in{skin};$chahead = $in{head};$chaeye = $in{me};$chanose = $in{nose};
$chamouth = $in{mouth};$chahair = $in{hair};
$chabougue[4] = "tabi";$chabougue[5] = "tabi";$chabougue[1] = "dagger";
$chabun[1] = "DMG 1";$chabun[4] = "AC 1";$chabun[5] = "AC 1";
$karistats[0] = "1";
$karistats[1] = "2";
$karistats[2] = "0";
$karistats[3] = "0";
$karistats[4] = "0";
$karistats[5] = "0";
$karistats[6] = "0";
$karistats[7] = "0";
$karistats[8] = "0";
$karistats[9] = "0";
$autop = "0";
$potion = "ƒ|[ƒVƒ‡ƒ“";
$bpo = "0";
$newtegami = "0";
$master[0] = "0";$master[1] = "0";$master[2] = "0";$master[3] = "0";$master[4] = "0";$master[5] = "0";$master[6] = "0";$master[7] = "0";$master[8] = "0";$master[9] = "0";$master[10] = "0";$master[11] = "0";$master[12] = "0";$master[21] = "0";$master[22] = "0";$master[31] = "0";$master[32] = "0";$master[41] = "0";$master[42] = "0";$master[51] = "0";$master[52] = "0";$master[61] = "0";$master[62] = "0";$master[71] = "0";$master[62] = "0";$master[72] = "0";$master[79] = "0";$master[80] = "0";$master[81] = "0";$master[82] = "0";$master[83] = "0";$master[84] = "0";$master[85] = "0";$master[86] = "0";$master[87] = "0";$master[88] = "0";$master[89] = "0";$master[90] = "0";$master[91] = "0";$master[92] = "0";$master[93] = "0";$master[94] = "0";$master[95] = "0";
$jobexp[0] = "100";$jobexp[1] = "1000";$jobexp[2] = "1000";$jobexp[3] = "1000";$jobexp[4] = "1000";$jobexp[5] = "1000";$jobexp[6] = "1000";$jobexp[7] = "1000";
$jobexp[11] = "3000";$jobexp[12] = "3000";$jobexp[21] = "3000";$jobexp[22] = "3000";$jobexp[31] = "3000";$jobexp[32] = "3000";$jobexp[41] = "3000";$jobexp[42] = "3000";$jobexp[51] = "3000";$jobexp[52] = "3000";$jobexp[61] = "3000";$jobexp[62] = "3000";$jobexp[71] = "3000";$jobexp[72] = "3000";
$jobexp[8] = "5000";$jobexp[9] = "5000";$jobexp[10] = "5000";$jobexp[79] = "5000";$jobexp[80] = "5000";$jobexp[81] = "5000";$jobexp[82] = "5000";$jobexp[83] = "5000";$jobexp[84] = "5000";$jobexp[85] = "6000";$jobexp[86] = "7000";$jobexp[87] = "8000";$jobexp[88] = "9000";$jobexp[90] = "10000";$jobexp[91] = "10000";$jobexp[92] = "7000";$jobexp[93] = "7000";$jobexp[94] = "7000";$jobexp[95] = "7000";
$jobexpnow[0] = "0";$jobexpnow[1] = "0";$jobexpnow[2] = "0";$jobexpnow[3] = "0";$jobexpnow[4] = "0";$jobexpnow[5] = "0";$jobexpnow[6] = "0";$jobexpnow[7] = "0";$jobexpnow[8] = "0";$jobexpnow[9] = "0";$jobexpnow[10] = "0";$jobexpnow[79] = "0";$jobexpnow[80] = "0";$jobexpnow[81] = "0";$jobexpnow[82] = "0";$jobexpnow[83] = "0";$jobexpnow[84] = "0";
$jobexpnow[11] = "0";$jobexpnow[12] = "0";$jobexpnow[21] = "0";$jobexpnow[22] = "0";$jobexpnow[31] = "0";$jobexpnow[32] = "0";$jobexpnow[41] = "0";$jobexpnow[42] = "0";$jobexpnow[51] = "0";$jobexpnow[52] = "0";$jobexpnow[61] = "0";$jobexpnow[62] = "0";$jobexpnow[71] = "0";$jobexpnow[72] = "0";
$jobexpnow[85] = "0";$jobexpnow[86] = "0";$jobexpnow[87] = "0";$jobexpnow[88] = "0";$jobexpnow[89] = "0";$jobexpnow[90] = "0";$jobexpnow[91] = "0";$jobexpnow[92] = "0";$jobexpnow[93] = "0";$jobexpnow[94] = "0";$jobexpnow[95] = "0";$masterjob = "0";
$pass2a = rand(89999);
$pass2b = int($pass2a + 10000);
$passkey = "$pass2b";
$angou1 = rand(9000);
$angou = int($angou1 + 999);
$karistats[10] = "$angou";
$kougeki = "0";
$mamori = "0";
$balance = "0";
$lvlpoint = "0";
$chanextlvl = "5";
$petexp[0] = "10";
$petnowexp[0] = "0";
$petexp[1] = "10";
$petnowexp[1] = "0";
$petexp[2] = "10";
$petnowexp[2] = "0";
$kougekit = "-1";
$mamorit = "-1";
$houou = "-1";
$ribaibu = "-1";
$tp = "2";
$tensei = "0";
open(DATA,">>$maindir/$foldacha/user_id$bousi2cha$bousikts2");
flock(DATA,2);
print DATA "$chaid/$chaname/\n";
flock(DATA,8);
close(DATA);


&charadatawrt;
&cookieset;
&hpsaisyo;
print <<HTML4;
<center>
<font size=6 color=#$mojiiro3>“o˜^Š®—¹</font><br><br>
ˆÈ‰º‚Ì“à—e‚ÅƒLƒƒƒ‰‚Ì“o˜^‚ªŠ®—¹‚µ‚Ü‚µ‚½B<br>
‚h‚cAƒpƒXƒ[ƒh‚Í–Y‚ê‚È‚¢‚æ‚¤‚Éƒƒ‚‚µ‚Ä‚¨‚¢‚Ä‚­‚¾‚³‚¢B<br><br>

<table border=1>
<tr><td>‚h‚c</td><td width=59><font color=#$chamoji>$chaid</font></td></tr>
<tr><td>ƒpƒXƒ[ƒh</td><td><font color=#$chamoji>$chapass</font></td></tr>
<tr><td>ƒpƒXƒL[</td><td><font color=#$chamoji><font color=red>$passkey</font></font></td></tr>
</table>
<br>
<font color=red>ƒpƒXƒL[</font>‚ÍAƒpƒXƒ[ƒh‚ğ•ÏX‚·‚éÛ‚É•K—v‚É‚È‚è‚Ü‚·B<br>
‚±‚¿‚ç‚àA–Y‚ê‚È‚¢‚æ‚¤‚Éƒƒ‚‚µ‚Ä‚¨‚­‚±‚Æ‚ğƒIƒXƒXƒ‚µ‚Ü‚·B
<br><br><br>
HTML4

&pettukitable;
&itemtable;

print <<HTML3;
<br><br>
ƒ}ƒi[‚ğç‚Á‚ÄƒvƒŒƒC‚µ‚Ü‚µ‚å‚¤B<br>
‚Å‚ÍA—Ç‚¢—·‚ğII<br><br>
<font size=4>[<a href="zone.cgi?usrid=$chaid&usrpass=$chapass">‚±‚Ì‚Ü‚ÜƒƒOƒCƒ“‚·‚é</a>]</font><br>
<font size=4>[<a href="index.html">’Êí”ÅƒƒOƒCƒ“‰æ–Ê‚É–ß‚é</a>]</font><br>
<br>
<hr><br><br>
HTML3
}

&hpowari;

sub sinkierr {

print <<HTML0;
<br><form method="post" action="./$sinki">
<INPUT NAME="new" TYPE=hidden VALUE="2">
<INPUT NAME="head" TYPE=hidden VALUE="$in{head}">
<INPUT NAME="me" TYPE=hidden VALUE="$in{me}">
<INPUT NAME="nose" TYPE=hidden VALUE="$in{nose}">
<INPUT NAME="mouth" TYPE=hidden VALUE="$in{mouth}">
<INPUT NAME="hair" TYPE=hidden VALUE="$in{hair}">
<INPUT NAME="skin" TYPE=hidden VALUE="$in{skin}">
<INPUT NAME="sinkinamae" TYPE=hidden VALUE="$in{sinkinamae}">
<INPUT NAME="mojisyoku" TYPE=hidden VALUE="$in{mojisyoku}">
<INPUT NAME="sinkihome" TYPE=hidden VALUE="$in{sinkihome}">
<INPUT NAME="sex" TYPE=hidden VALUE="$in{sex}">
<INPUT NAME="usrid" TYPE=hidden VALUE="$in{usrid}">
<INPUT TYPE=submit VALUE="___ Äİ’è ___">
<INPUT NAME="sinkipass" TYPE=hidden VALUE="$in{sinkipass}">
</form>
<br><br>
HTML0
}

