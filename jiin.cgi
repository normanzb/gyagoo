&topsisetu;
	if ( $in{riyou} eq "2" ) {
#　中級ジョブ転職処理
		if ( $chalvl > 0 ) {
$chaclass = $in{jobgime};
&charadatawrt;
print <<"HTM";
ではいくぞ！<br><br>
<font size=6 color=#$mojiiro3><b>キェェェぇぇっっ～！！</b></font><br><br>
<font size=5 color=#$mojiiro2><b><font color=#$chamoji>
$chaname</font> は <font color=#$chamoji>
$job[$chaclass]</font> に転職をした！</b></font><br><br>
ふむ。無事完了したようだ。<br>
新たな人生を歩むがよい。
HTM



		} else {&fuseisyori;}
	} elsif ( $in{riyou} eq "1" ) {
	if ( $chalvl > 0 ) {
if ( $master[0] == 1 ){ $kiwame0 = "<font color=#cd5c5c><b>M<font color=#dc143c>a<font color=#ff0000>s<font color=#ff4500>t<font color=#ff6347>e<font color=#ff7f50>r!</b></font>";}
if ( $master[1] == 1 ){ $kiwame1 = "<font color=#cd5c5c><b>M<font color=#dc143c>a<font color=#ff0000>s<font color=#ff4500>t<font color=#ff6347>e<font color=#ff7f50>r!</b></font>";}
if ( $master[2] == 1 ){ $kiwame2 = "<font color=#cd5c5c><b>M<font color=#dc143c>a<font color=#ff0000>s<font color=#ff4500>t<font color=#ff6347>e<font color=#ff7f50>r!</b></font>";}
if ( $master[3] == 1 ){ $kiwame3 = "<font color=#cd5c5c><b>M<font color=#dc143c>a<font color=#ff0000>s<font color=#ff4500>t<font color=#ff6347>e<font color=#ff7f50>r!</b></font>";}
if ( $master[4] == 1 ){ $kiwame4 = "<font color=#cd5c5c><b>M<font color=#dc143c>a<font color=#ff0000>s<font color=#ff4500>t<font color=#ff6347>e<font color=#ff7f50>r!</b></font>";}
if ( $master[5] == 1 ){ $kiwame5 = "<font color=#cd5c5c><b>M<font color=#dc143c>a<font color=#ff0000>s<font color=#ff4500>t<font color=#ff6347>e<font color=#ff7f50>r!</b></font>";}
if ( $master[6] == 1 ){ $kiwame6 = "<font color=#cd5c5c><b>M<font color=#dc143c>a<font color=#ff0000>s<font color=#ff4500>t<font color=#ff6347>e<font color=#ff7f50>r!</b></font>";}
if ( $master[7] == 1 ){ $kiwame7 = "<font color=#cd5c5c><b>M<font color=#dc143c>a<font color=#ff0000>s<font color=#ff4500>t<font color=#ff6347>e<font color=#ff7f50>r!</b></font>";}
if ( $master[11] == 1 ){ $kiwame11 = "<font color=#cd5c5c><b>M<font color=#dc143c>a<font color=#ff0000>s<font color=#ff4500>t<font color=#ff6347>e<font color=#ff7f50>r!</b></font>";}
if ( $master[12] == 1 ){ $kiwame12 = "<font color=#cd5c5c><b>M<font color=#dc143c>a<font color=#ff0000>s<font color=#ff4500>t<font color=#ff6347>e<font color=#ff7f50>r!</b></font>";}
if ( $master[21] == 1 ){ $kiwame21 = "<font color=#cd5c5c><b>M<font color=#dc143c>a<font color=#ff0000>s<font color=#ff4500>t<font color=#ff6347>e<font color=#ff7f50>r!</b></font>";}
if ( $master[22] == 1 ){ $kiwame22 = "<font color=#cd5c5c><b>M<font color=#dc143c>a<font color=#ff0000>s<font color=#ff4500>t<font color=#ff6347>e<font color=#ff7f50>r!</b></font>";}
if ( $master[31] == 1 ){ $kiwame31 = "<font color=#cd5c5c><b>M<font color=#dc143c>a<font color=#ff0000>s<font color=#ff4500>t<font color=#ff6347>e<font color=#ff7f50>r!</b></font>";}
if ( $master[32] == 1 ){ $kiwame32 = "<font color=#cd5c5c><b>M<font color=#dc143c>a<font color=#ff0000>s<font color=#ff4500>t<font color=#ff6347>e<font color=#ff7f50>r!</b></font>";}
if ( $master[41] == 1 ){ $kiwame41 = "<font color=#cd5c5c><b>M<font color=#dc143c>a<font color=#ff0000>s<font color=#ff4500>t<font color=#ff6347>e<font color=#ff7f50>r!</b></font>";}
if ( $master[42] == 1 ){ $kiwame42 = "<font color=#cd5c5c><b>M<font color=#dc143c>a<font color=#ff0000>s<font color=#ff4500>t<font color=#ff6347>e<font color=#ff7f50>r!</b></font>";}
if ( $master[51] == 1 ){ $kiwame51 = "<font color=#cd5c5c><b>M<font color=#dc143c>a<font color=#ff0000>s<font color=#ff4500>t<font color=#ff6347>e<font color=#ff7f50>r!</b></font>";}
if ( $master[52] == 1 ){ $kiwame52 = "<font color=#cd5c5c><b>M<font color=#dc143c>a<font color=#ff0000>s<font color=#ff4500>t<font color=#ff6347>e<font color=#ff7f50>r!</b></font>";}
if ( $master[61] == 1 ){ $kiwame61 = "<font color=#cd5c5c><b>M<font color=#dc143c>a<font color=#ff0000>s<font color=#ff4500>t<font color=#ff6347>e<font color=#ff7f50>r!</b></font>";}
if ( $master[62] == 1 ){ $kiwame62 = "<font color=#cd5c5c><b>M<font color=#dc143c>a<font color=#ff0000>s<font color=#ff4500>t<font color=#ff6347>e<font color=#ff7f50>r!</b></font>";}
if ( $master[71] == 1 ){ $kiwame71 = "<font color=#cd5c5c><b>M<font color=#dc143c>a<font color=#ff0000>s<font color=#ff4500>t<font color=#ff6347>e<font color=#ff7f50>r!</b></font>";}
if ( $master[72] == 1 ){ $kiwame72 = "<font color=#cd5c5c><b>M<font color=#dc143c>a<font color=#ff0000>s<font color=#ff4500>t<font color=#ff6347>e<font color=#ff7f50>r!</b></font>";}
if ( $master[8] == 1 ){ $kiwame8 = "<font color=#cd5c5c><b>M<font color=#dc143c>a<font color=#ff0000>s<font color=#ff4500>t<font color=#ff6347>e<font color=#ff7f50>r!</b></font>";}
if ( $master[9] == 1 ){ $kiwame9 = "<font color=#cd5c5c><b>M<font color=#dc143c>a<font color=#ff0000>s<font color=#ff4500>t<font color=#ff6347>e<font color=#ff7f50>r!</b></font>";}
if ( $master[10] == 1 ){ $kiwame10 = "<font color=#cd5c5c><b>M<font color=#dc143c>a<font color=#ff0000>s<font color=#ff4500>t<font color=#ff6347>e<font color=#ff7f50>r!</b></font>";}
if ( $master[79] == 1 ){ $kiwame79 = "<font color=#cd5c5c><b>M<font color=#dc143c>a<font color=#ff0000>s<font color=#ff4500>t<font color=#ff6347>e<font color=#ff7f50>r!</b></font>";}
if ( $master[80] == 1 ){ $kiwame80 = "<font color=#cd5c5c><b>M<font color=#dc143c>a<font color=#ff0000>s<font color=#ff4500>t<font color=#ff6347>e<font color=#ff7f50>r!</b></font>";}
if ( $master[81] == 1 ){ $kiwame81 = "<font color=#cd5c5c><b>M<font color=#dc143c>a<font color=#ff0000>s<font color=#ff4500>t<font color=#ff6347>e<font color=#ff7f50>r!</b></font>";}
if ( $master[82] == 1 ){ $kiwame82 = "<font color=#cd5c5c><b>M<font color=#dc143c>a<font color=#ff0000>s<font color=#ff4500>t<font color=#ff6347>e<font color=#ff7f50>r!</b></font>";}
if ( $master[83] == 1 ){ $kiwame83 = "<font color=#cd5c5c><b>M<font color=#dc143c>a<font color=#ff0000>s<font color=#ff4500>t<font color=#ff6347>e<font color=#ff7f50>r!</b></font>";}
if ( $master[84] == 1 ){ $kiwame84 = "<font color=#cd5c5c><b>M<font color=#dc143c>a<font color=#ff0000>s<font color=#ff4500>t<font color=#ff6347>e<font color=#ff7f50>r!</b></font>";}
if ( $master[85] == 1 ){ $kiwame85 = "<font color=#cd5c5c><b>M<font color=#dc143c>a<font color=#ff0000>s<font color=#ff4500>t<font color=#ff6347>e<font color=#ff7f50>r!</b></font>";}
if ( $master[86] == 1 ){ $kiwame86 = "<font color=#cd5c5c><b>M<font color=#dc143c>a<font color=#ff0000>s<font color=#ff4500>t<font color=#ff6347>e<font color=#ff7f50>r!</b></font>";}
if ( $master[87] == 1 ){ $kiwame87 = "<font color=#cd5c5c><b>M<font color=#dc143c>a<font color=#ff0000>s<font color=#ff4500>t<font color=#ff6347>e<font color=#ff7f50>r!</b></font>";}
if ( $master[88] == 1 ){ $kiwame88 = "<font color=#cd5c5c><b>M<font color=#dc143c>a<font color=#ff0000>s<font color=#ff4500>t<font color=#ff6347>e<font color=#ff7f50>r!</b></font>";}
if ( $master[89] == 1 ){ $kiwame89 = "<font color=#cd5c5c><b>M<font color=#dc143c>a<font color=#ff0000>s<font color=#ff4500>t<font color=#ff6347>e<font color=#ff7f50>r!</b></font>";}



$jobbarcha0 = int( ( $jobexpnow[0] / $jobexp[0] ) * 230 );
$jobritu0 = int($jobbarcha0 / 2.3); 
if ( $jobbarcha0 != 230 ) {
$jobbarcha00 = 230 - $jobbarcha0;
$jobbardmg00 = "<img src=\"$maindir/$imgfile/hpbar2.gif\" width=$jobbarcha11 height=\"8\">";
}

$jobbarcha1 = int( ( $jobexpnow[1] / $jobexp[1] ) * 230 );
$jobritu1 = int($jobbarcha1 / 2.3); 
if ( $jobbarcha1 != 230 ) {
$jobbarcha11 = 230 - $jobbarcha1;
$jobbardmg11 = "<img src=\"$maindir/$imgfile/hpbar2.gif\" width=$jobbarcha11 height=\"8\">";
}

$jobbarcha2 = int( ( $jobexpnow[2] / $jobexp[2] ) * 230 );
$jobritu2 = int($jobbarcha2 / 2.3); 
if ( $jobbarcha2 != 230 ) {
$jobbarcha22 = 230 - $jobbarcha2;
$jobbardmg22 = "<img src=\"$maindir/$imgfile/hpbar2.gif\" width=$jobbarcha22 height=\"8\">";
}

$jobbarcha3 = int( ( $jobexpnow[3] / $jobexp[3] ) * 230 );
$jobritu3 = int($jobbarcha3 / 2.3); 
if ( $jobbarcha3 != 230 ) {
$jobbarcha33 = 230 - $jobbarcha3;
$jobbardmg33 = "<img src=\"$maindir/$imgfile/hpbar2.gif\" width=$jobbarcha33 height=\"8\">";
}
 
$jobbarcha4 = int( ( $jobexpnow[4] / $jobexp[4] ) * 230 );
$jobritu4 = int($jobbarcha4 / 2.3);
if ( $jobbarcha4 != 230 ) {
$jobbarcha44 = 230 - $jobbarcha4;
$jobbardmg44 = "<img src=\"$maindir/$imgfile/hpbar2.gif\" width=$jobbarcha44 height=\"8\">";
}

$jobbarcha5 = int( ( $jobexpnow[5] / $jobexp[5] ) * 230 );
$jobritu5 = int($jobbarcha5 / 2.3); 
if ( $jobbarcha5 != 230 ) {
$jobbarcha55 = 230 - $jobbarcha5;
$jobbardmg55 = "<img src=\"$maindir/$imgfile/hpbar2.gif\" width=$jobbarcha55 height=\"8\">";
}

$jobbarcha6 = int( ( $jobexpnow[6] / $jobexp[6] ) * 230 );
$jobritu6 = int($jobbarcha6 / 2.3); 
if ( $jobbarcha6 != 230 ) {
$jobbarcha66 = 230 - $jobbarcha6;
$jobbardmg66 = "<img src=\"$maindir/$imgfile/hpbar2.gif\" width=$jobbarcha66 height=\"8\">";
}

$jobbarcha7 = int( ( $jobexpnow[7] / $jobexp[7] ) * 230 );
$jobritu7 = int($jobbarcha7 / 2.3); 
if ( $jobbarcha7 != 230 ) {
$jobbarcha77 = 230 - $jobbarcha7;
$jobbardmg77 = "<img src=\"$maindir/$imgfile/hpbar2.gif\" width=$jobbarcha77 height=\"8\">";
}

$jobbarchaa1 = int( ( $jobexpnow[11] / $jobexp[11] ) * 230 );
$jobritu11 = int($jobbarchaa1 / 2.3);
if ( $jobbarchaa1 != 230 ) {
$jobbarchaa11 = 230 - $jobbarchaa1;
$jobbardmga11 = "<img src=\"$maindir/$imgfile/hpbar2.gif\" width=$jobbarchaa11 height=\"8\">";
}

$jobbarchaa2 = int( ( $jobexpnow[12] / $jobexp[12] ) * 230 );
$jobritu12 = int($jobbarchaa2 / 2.3); 
if ( $jobbarchaa2 != 230 ) {
$jobbarchaa22 = 230 - $jobbarchaa2;
$jobbardmga22 = "<img src=\"$maindir/$imgfile/hpbar2.gif\" width=$jobbarchaa22 height=\"8\">";
}

$jobbarchab1 = int( ( $jobexpnow[21] / $jobexp[21] ) * 230 );
$jobritu21 = int($jobbarchab1 / 2.3); 
if ( $jobbarchab1 != 230 ) {
$jobbarchab11 = 230 - $jobbarchab1;
$jobbardmgb11 = "<img src=\"$maindir/$imgfile/hpbar2.gif\" width=$jobbarchab11 height=\"8\">";
}

$jobbarchab2 = int( ( $jobexpnow[22] / $jobexp[22] ) * 230 );
$jobritu22 = int($jobbarchab2 / 2.3); 
if ( $jobbarchab2 != 230 ) {
$jobbarchab22 = 230 - $jobbarchab2;
$jobbardmgb22 = "<img src=\"$maindir/$imgfile/hpbar2.gif\" width=$jobbarchab22 height=\"8\">";
}

$jobbarchac1 = int( ( $jobexpnow[31] / $jobexp[31] ) * 230 );
$jobritu31 = int($jobbarchac1 / 2.3); 
if ( $jobbarchac1 != 230 ) {
$jobbarchac11 = 230 - $jobbarchac1;
$jobbardmgc11 = "<img src=\"$maindir/$imgfile/hpbar2.gif\" width=$jobbarchac11 height=\"8\">";
}

$jobbarchac2 = int( ( $jobexpnow[32] / $jobexp[32] ) * 230 );
$jobritu32 = int($jobbarchac2 / 2.3);
if ( $jobbarchac2 != 230 ) {
$jobbarchac22 = 230 - $jobbarchac2;
$jobbardmgc22 = "<img src=\"$maindir/$imgfile/hpbar2.gif\" width=$jobbarchac22 height=\"8\">";
}

$jobbarchad1 = int( ( $jobexpnow[41] / $jobexp[41] ) * 230 );
$jobritu41 = int($jobbarchad1 / 2.3); 
if ( $jobbarchad1 != 230 ) {
$jobbarchad11 = 230 - $jobbarchad1;
$jobbardmgd11 = "<img src=\"$maindir/$imgfile/hpbar2.gif\" width=$jobbarchad11 height=\"8\">";
}

$jobbarchad2 = int( ( $jobexpnow[42] / $jobexp[42] ) * 230 );
$jobritu42 = int($jobbarchad2 / 2.3); 
if ( $jobbarchad2 != 230 ) {
$jobbarchad22 = 230 - $jobbarchad2;
$jobbardmgd22 = "<img src=\"$maindir/$imgfile/hpbar2.gif\" width=$jobbarchad22 height=\"8\">";
}

$jobbarchae1 = int( ( $jobexpnow[51] / $jobexp[51] ) * 230 );
$jobritu51 = int($jobbarchae1 / 2.3); 
if ( $jobbarchae1 != 230 ) {
$jobbarchae11 = 230 - $jobbarchae1;
$jobbardmge11 = "<img src=\"$maindir/$imgfile/hpbar2.gif\" width=$jobbarchae11 height=\"8\">";
}

$jobbarchae2 = int( ( $jobexpnow[52] / $jobexp[52] ) * 230 );
$jobritu52 = int($jobbarchae2 / 2.3); 
if ( $jobbarchae2 != 230 ) {
$jobbarchae22 = 230 - $jobbarchae2;
$jobbardmge22 = "<img src=\"$maindir/$imgfile/hpbar2.gif\" width=$jobbarchae22 height=\"8\">";
}

$jobbarchaf1 = int( ( $jobexpnow[61] / $jobexp[61] ) * 230 );
$jobritu61 = int($jobbarchaf1 / 2.3); 
if ( $jobbarchaf1 != 230 ) {
$jobbarchaf11 = 230 - $jobbarchaf1;
$jobbardmgf11 = "<img src=\"$maindir/$imgfile/hpbar2.gif\" width=$jobbarchaf11 height=\"8\">";
}

$jobbarchaf2 = int( ( $jobexpnow[62] / $jobexp[62] ) * 230 );
$jobritu62 = int($jobbarchaf2 / 2.3); 
if ( $jobbarchaf2 != 230 ) {
$jobbarchaf22 = 230 - $jobbarchaf2;
$jobbardmgf22 = "<img src=\"$maindir/$imgfile/hpbar2.gif\" width=$jobbarchaf22 height=\"8\">";
}

$jobbarchag1 = int( ( $jobexpnow[71] / $jobexp[71] ) * 230 );
$jobritu71 = int($jobbarchag1 / 2.3); 
if ( $jobbarchag1 != 230 ) {
$jobbarchag11 = 230 - $jobbarchag1;
$jobbardmgg11 = "<img src=\"$maindir/$imgfile/hpbar2.gif\" width=$jobbarchag11 height=\"8\">";
}

$jobbarchag2 = int( ( $jobexpnow[72] / $jobexp[72] ) * 230 );
$jobritu72 = int($jobbarchag2 / 2.3); 
if ( $jobbarchag2 != 230 ) {
$jobbarchag22 = 230 - $jobbarchag2;
$jobbardmgg22 = "<img src=\"$maindir/$imgfile/hpbar2.gif\" width=$jobbarchag22 height=\"8\">";
}

$jobbarcha8 = int( ( $jobexpnow[8] / $jobexp[8] ) * 230 );
$jobritu8 = int($jobbarcha8 / 2.3); 
if ( $jobbarcha8 != 230 ) {
$jobbarcha88 = 230 - $jobbarcha8;
$jobbardmg88 = "<img src=\"$maindir/$imgfile/hpbar2.gif\" width=$jobbarcha88 height=\"8\">";
}

$jobbarcha9 = int( ( $jobexpnow[9] / $jobexp[9] ) * 230 );
$jobritu9 = int($jobbarcha9 / 2.3); 
if ( $jobbarcha9 != 230 ) {
$jobbarcha99 = 230 - $jobbarcha9;
$jobbardmg99 = "<img src=\"$maindir/$imgfile/hpbar2.gif\" width=$jobbarcha99 height=\"8\">";
}

$jobbarcha10 = int( ( $jobexpnow[10] / $jobexp[10] ) * 230 );
$jobritu10 = int($jobbarcha10 / 2.3); 
if ( $jobbarcha10 != 230 ) {
$jobbarcha1010 = 230 - $jobbarcha10;
$jobbardmg1010 = "<img src=\"$maindir/$imgfile/hpbar2.gif\" width=$jobbarcha1010 height=\"8\">";
}

$jobbarcha79 = int( ( $jobexpnow[79] / $jobexp[79] ) * 230 );
$jobritu79 = int($jobbarcha79 / 2.3); 
if ( $jobbarcha79 != 230 ) {
$jobbarcha7979 = 230 - $jobbarcha79;
$jobbardmg7979 = "<img src=\"$maindir/$imgfile/hpbar2.gif\" width=$jobbarcha7979 height=\"8\">";
}

$jobbarcha80 = int( ( $jobexpnow[80] / $jobexp[80] ) * 230 );
$jobritu80 = int($jobbarcha80 / 2.3); 
if ( $jobbarcha80 != 230 ) {
$jobbarcha8080 = 230 - $jobbarcha80;
$jobbardmg8080 = "<img src=\"$maindir/$imgfile/hpbar2.gif\" width=$jobbarcha8080 height=\"8\">";
}

$jobbarcha81 = int( ( $jobexpnow[81] / $jobexp[81] ) * 230 );
$jobritu81 = int($jobbarcha81 / 2.3); 
if ( $jobbarcha81 != 230 ) {
$jobbarcha8181 = 230 - $jobbarcha81;
$jobbardmg8181 = "<img src=\"$maindir/$imgfile/hpbar2.gif\" width=$jobbarcha8181 height=\"8\">";
}

$jobbarcha82 = int( ( $jobexpnow[82] / $jobexp[82] ) * 230 );
$jobritu82 = int($jobbarcha82 / 2.3); 
if ( $jobbarcha82 != 230 ) {
$jobbarcha8282 = 230 - $jobbarcha82;
$jobbardmg8282 = "<img src=\"$maindir/$imgfile/hpbar2.gif\" width=$jobbarcha8282 height=\"8\">";
}

$jobbarcha83 = int( ( $jobexpnow[83] / $jobexp[83] ) * 230 );
$jobritu83 = int($jobbarcha83 / 2.3); 
if ( $jobbarcha83 != 230 ) {
$jobbarcha8383 = 230 - $jobbarcha83;
$jobbardmg8383 = "<img src=\"$maindir/$imgfile/hpbar2.gif\" width=$jobbarcha8383 height=\"8\">";
}

$jobbarcha84 = int( ( $jobexpnow[84] / $jobexp[84] ) * 230 );
$jobritu84 = int($jobbarcha84 / 2.3); 
if ( $jobbarcha84 != 230 ) {
$jobbarcha8484 = 230 - $jobbarcha84;
$jobbardmg8484 = "<img src=\"$maindir/$imgfile/hpbar2.gif\" width=$jobbarcha8484 height=\"8\">";
}

$jobbarcha85 = int( ( $jobexpnow[85] / $jobexp[85] ) * 230 );
$jobritu85 = int($jobbarcha85 / 2.3); 
if ( $jobbarcha85 != 230 ) {
$jobbarcha8585 = 230 - $jobbarcha85;
$jobbardmg8585 = "<img src=\"$maindir/$imgfile/hpbar2.gif\" width=$jobbarcha8585 height=\"8\">";
}

$jobbarcha86 = int( ( $jobexpnow[86] / $jobexp[86] ) * 230 );
$jobritu86 = int($jobbarcha86 / 2.3); 
if ( $jobbarcha86 != 230 ) {
$jobbarcha8686 = 230 - $jobbarcha86;
$jobbardmg8686 = "<img src=\"$maindir/$imgfile/hpbar2.gif\" width=$jobbarcha8686 height=\"8\">";
}

$jobbarcha87 = int( ( $jobexpnow[87] / $jobexp[87] ) * 230 );
$jobritu87 = int($jobbarcha87 / 2.3); 
if ( $jobbarcha87 != 230 ) {
$jobbarcha8787 = 230 - $jobbarcha87;
$jobbardmg8787 = "<img src=\"$maindir/$imgfile/hpbar2.gif\" width=$jobbarcha8787 height=\"8\">";
}

$jobbarcha88 = int( ( $jobexpnow[88] / $jobexp[88] ) * 230 );
$jobritu88 = int($jobbarcha88 / 2.3); 
if ( $jobbarcha88 != 230 ) {
$jobbarcha8888 = 230 - $jobbarcha88;
$jobbardmg8888 = "<img src=\"$maindir/$imgfile/hpbar2.gif\" width=$jobbarcha8888 height=\"8\">";
}


print <<"HTM";
</td><td>
では、以下の中からジョブを選択しなさい。<br><br>
<table border=1>
<form method="post" action="./$zonecgi">
<tr><td><input type=radio name="jobgime" value="0" checked></td><td><nobr><b>$job[0]</nobr></td><td><img src="$maindir/$imgfile/exp.gif" height="10"><img src="$maindir/$imgfile/jobbar1.gif" width=$jobbarcha0 height="8">$jobbardmg00<img src="$maindir/$imgfile/exp.gif" height="8"></td><td align=right><font color=#$chamoji><b><font face="Westminster">$jobritu0 </font></font><font size=-1>％</b></font></td><td><font face="Copperplate Gothic Bold">$kiwame0</td></tr>
<tr><td><input type=radio name="jobgime" value="1"></td><td><nobr><b>$job[1]</nobr></td><td><img src="$maindir/$imgfile/exp.gif" height="10"><img src="$maindir/$imgfile/jobbar1.gif" width=$jobbarcha1 height="8">$jobbardmg11<img src="$maindir/$imgfile/exp.gif" height="8"></td><td align=right><font color=#$chamoji><b><font face="Westminster">$jobritu1 </font></font><font size=-1>％</b></font></td><td><font face="Copperplate Gothic Bold">$kiwame1</td></tr>
<tr><td><input type=radio name="jobgime" value="2"></td><td><nobr><b>$job[2]</nobr></td><td><img src="$maindir/$imgfile/exp.gif" height="10"><img src="$maindir/$imgfile/jobbar1.gif" width=$jobbarcha2 height="8">$jobbardmg22<img src="$maindir/$imgfile/exp.gif" height="8"></td><td align=right><font color=#$chamoji><b><font face="Westminster">$jobritu2 </font></font><font size=-1>％</td><td><font face="Copperplate Gothic Bold">$kiwame2</td></tr>
<tr><td><input type=radio name="jobgime" value="3"></td><td><nobr><b>$job[3]</nobr></td><td><img src="$maindir/$imgfile/exp.gif" height="10"><img src="$maindir/$imgfile/jobbar1.gif" width=$jobbarcha3 height="8">$jobbardmg33<img src="$maindir/$imgfile/exp.gif" height="8"></td><td align=right><font color=#$chamoji><b><font face="Westminster">$jobritu3 </font></font><font size=-1>％</td><td><font face="Copperplate Gothic Bold">$kiwame3</td></tr>
<tr><td><input type=radio name="jobgime" value="4"></td><td><nobr><b>$job[4]</nobr></td><td><img src="$maindir/$imgfile/exp.gif" height="10"><img src="$maindir/$imgfile/jobbar1.gif" width=$jobbarcha4 height="8">$jobbardmg44<img src="$maindir/$imgfile/exp.gif" height="8"></td><td align=right><font color=#$chamoji><b><font face="Westminster">$jobritu4 </font></font><font size=-1>％</td><td><font face="Copperplate Gothic Bold">$kiwame4</td></tr>
<tr><td><input type=radio name="jobgime" value="5"></td><td><nobr><b>$job[5]</nobr></td><td><img src="$maindir/$imgfile/exp.gif" height="10"><img src="$maindir/$imgfile/jobbar1.gif" width=$jobbarcha5 height="8">$jobbardmg55<img src="$maindir/$imgfile/exp.gif" height="8"></td><td align=right><font color=#$chamoji><b><font face="Westminster">$jobritu5 </font></font><font size=-1>％</td><td><font face="Copperplate Gothic Bold">$kiwame5</td></tr>
<tr><td><input type=radio name="jobgime" value="6"></td><td><nobr><b>$job[6]</nobr></td><td><img src="$maindir/$imgfile/exp.gif" height="10"><img src="$maindir/$imgfile/jobbar1.gif" width=$jobbarcha6 height="8">$jobbardmg66<img src="$maindir/$imgfile/exp.gif" height="8"></td><td align=right><font color=#$chamoji><b><font face="Westminster">$jobritu6 </font></font><font size=-1>％</td><td><font face="Copperplate Gothic Bold">$kiwame6</td></tr>
<tr><td><input type=radio name="jobgime" value="7"></td><td><nobr><b>$job[7]</nobr></td><td><img src="$maindir/$imgfile/exp.gif" height="10"><img src="$maindir/$imgfile/jobbar1.gif" width=$jobbarcha7 height="8">$jobbardmg77<img src="$maindir/$imgfile/exp.gif" height="8"></td><td align=right><font color=#$chamoji><b><font face="Westminster">$jobritu7 </font></font><font size=-1>％</td><td><font face="Copperplate Gothic Bold">$kiwame7</td></tr>
HTM
	if ( $master[1] == 1 ){
print <<"HTM";
<tr><td><input type=radio name="jobgime" value="11"></td><td><nobr><font color=darkbrown><b>$job[11]</font></nobr></td><td><img src="$maindir/$imgfile/exp.gif" height="10"><img src="$maindir/$imgfile/jobbar1.gif" width=$jobbarchaa1 height="8">$jobbardmga11<img src="$maindir/$imgfile/exp.gif" height="8"></td><td align=right><font color=#$chamoji><b><font face="Westminster">$jobritu11 </font></font><font size=-1>％</td><td><font face="Copperplate Gothic Bold">$kiwame11</td></tr>
<tr><td><input type=radio name="jobgime" value="12"></td><td><nobr><font color=darkbrown><b>$job[12]</font></nobr></td><td><img src="$maindir/$imgfile/exp.gif" height="10"><img src="$maindir/$imgfile/jobbar1.gif" width=$jobbarchaa2 height="8">$jobbardmga22<img src="$maindir/$imgfile/exp.gif" height="8"></td><td align=right><font color=#$chamoji><b><font face="Westminster">$jobritu12 </font></font><font size=-1>％</td><td><font face="Copperplate Gothic Bold">$kiwame12</td></tr>
HTM
	}
	if ( $master[2] == 1 ){
print <<"HTM";
<tr><td><input type=radio name="jobgime" value="21"></td><td><nobr><font color=darkbrown><b>$job[21]</font></nobr></td><td><img src="$maindir/$imgfile/exp.gif" height="10"><img src="$maindir/$imgfile/jobbar1.gif" width=$jobbarchab1 height="8">$jobbardmgb11<img src="$maindir/$imgfile/exp.gif" height="8"></td><td align=right><font color=#$chamoji><b><font face="Westminster">$jobritu21 </font></font><font size=-1>％</td><td><font face="Copperplate Gothic Bold">$kiwame21</td></tr>
<tr><td><input type=radio name="jobgime" value="22"></td><td><nobr><font color=darkbrown><b>$job[22]</font></nobr></td><td><img src="$maindir/$imgfile/exp.gif" height="10"><img src="$maindir/$imgfile/jobbar1.gif" width=$jobbarchab2 height="8">$jobbardmgb22<img src="$maindir/$imgfile/exp.gif" height="8"></td><td align=right><font color=#$chamoji><b><font face="Westminster">$jobritu22 </font></font><font size=-1>％</td><td><font face="Copperplate Gothic Bold">$kiwame22</td></tr>
HTM
	}
	if ( $master[3] == 1 ){
print <<"HTM";
<tr><td><input type=radio name="jobgime" value="31"></td><td><nobr><font color=darkbrown><b>$job[31]</font></nobr></td><td><img src="$maindir/$imgfile/exp.gif" height="10"><img src="$maindir/$imgfile/jobbar1.gif" width=$jobbarchac1 height="8">$jobbardmgc11<img src="$maindir/$imgfile/exp.gif" height="8"></td><td align=right><font color=#$chamoji><b><font face="Westminster">$jobritu31 </font></font><font size=-1>％</td><td><font face="Copperplate Gothic Bold">$kiwame31</td></tr>
<tr><td><input type=radio name="jobgime" value="32"></td><td><nobr><font color=darkbrown><b>$job[32]</font></nobr></td><td><img src="$maindir/$imgfile/exp.gif" height="10"><img src="$maindir/$imgfile/jobbar1.gif" width=$jobbarchac2 height="8">$jobbardmgc22<img src="$maindir/$imgfile/exp.gif" height="8"></td><td align=right><font color=#$chamoji><b><font face="Westminster">$jobritu32 </font></font><font size=-1>％</td><td><font face="Copperplate Gothic Bold">$kiwame32</td></tr>
HTM
	}
	if ( $master[4] == 1 ){
print <<"HTM";
<tr><td><input type=radio name="jobgime" value="41"></td><td><nobr><font color=darkbrown><b>$job[41]</font></nobr></td><td><img src="$maindir/$imgfile/exp.gif" height="10"><img src="$maindir/$imgfile/jobbar1.gif" width=$jobbarchad1 height="8">$jobbardmgd11<img src="$maindir/$imgfile/exp.gif" height="8"></td><td align=right><font color=#$chamoji><b><font face="Westminster">$jobritu41 </font></font><font size=-1>％</td><td><font face="Copperplate Gothic Bold">$kiwame41</td></tr>
<tr><td><input type=radio name="jobgime" value="42"></td><td><nobr><font color=darkbrown><b>$job[42]</font></nobr></td><td><img src="$maindir/$imgfile/exp.gif" height="10"><img src="$maindir/$imgfile/jobbar1.gif" width=$jobbarchad2 height="8">$jobbardmgd22<img src="$maindir/$imgfile/exp.gif" height="8"></td><td align=right><font color=#$chamoji><b><font face="Westminster">$jobritu42 </font></font><font size=-1>％</td><td><font face="Copperplate Gothic Bold">$kiwame42</td></tr>
HTM
	}
	if ( $master[5] == 1 ){
print <<"HTM";
<tr><td><input type=radio name="jobgime" value="51"></td><td><nobr><font color=darkbrown><b>$job[51]</font></nobr></td><td><img src="$maindir/$imgfile/exp.gif" height="10"><img src="$maindir/$imgfile/jobbar1.gif" width=$jobbarchae1 height="8">$jobbardmge11<img src="$maindir/$imgfile/exp.gif" height="8"></td><td align=right><font color=#$chamoji><b><font face="Westminster">$jobritu51 </font></font><font size=-1>％</td><td><font face="Copperplate Gothic Bold">$kiwame51</td></tr>
<tr><td><input type=radio name="jobgime" value="52"></td><td><nobr><font color=darkbrown><b>$job[52]</font></nobr></td><td><img src="$maindir/$imgfile/exp.gif" height="10"><img src="$maindir/$imgfile/jobbar1.gif" width=$jobbarchae2 height="8">$jobbardmge22<img src="$maindir/$imgfile/exp.gif" height="8"></td><td align=right><font color=#$chamoji><b><font face="Westminster">$jobritu52 </font></font><font size=-1>％</td><td><font face="Copperplate Gothic Bold">$kiwame52</td></tr>
HTM
	}
	if ( $master[6] == 1 ){
print <<"HTM";
<tr><td><input type=radio name="jobgime" value="61"></td><td><nobr><font color=darkbrown><b>$job[61]</font></nobr></td><td><img src="$maindir/$imgfile/exp.gif" height="10"><img src="$maindir/$imgfile/jobbar1.gif" width=$jobbarchaf1 height="8">$jobbardmgf11<img src="$maindir/$imgfile/exp.gif" height="8"></td><td align=right><font color=#$chamoji><b><font face="Westminster">$jobritu61 </font></font><font size=-1>％</td><td><font face="Copperplate Gothic Bold">$kiwame61</td></tr>
<tr><td><input type=radio name="jobgime" value="62"></td><td><nobr><font color=darkbrown><b>$job[62]</font></nobr></td><td><img src="$maindir/$imgfile/exp.gif" height="10"><img src="$maindir/$imgfile/jobbar1.gif" width=$jobbarchaf2 height="8">$jobbardmgf22<img src="$maindir/$imgfile/exp.gif" height="8"></td><td align=right><font color=#$chamoji><b><font face="Westminster">$jobritu62 </font></font><font size=-1>％</td><td><font face="Copperplate Gothic Bold">$kiwame62</td></tr>
HTM
	}
	if ( $master[7] == 1 ){
print <<"HTM";
<tr><td><input type=radio name="jobgime" value="71"></td><td><nobr><font color=darkbrown><b>$job[71]</font></nobr></td><td><img src="$maindir/$imgfile/exp.gif" height="10"><img src="$maindir/$imgfile/jobbar1.gif" width=$jobbarchag1 height="8">$jobbardmgg11<img src="$maindir/$imgfile/exp.gif" height="8"></td><td align=right><font color=#$chamoji><b><font face="Westminster">$jobritu71 </font></font><font size=-1>％</td><td><font face="Copperplate Gothic Bold">$kiwame71</td></tr>
<tr><td><input type=radio name="jobgime" value="72"></td><td><nobr><font color=darkbrown><b>$job[72]</font></nobr></td><td><img src="$maindir/$imgfile/exp.gif" height="10"><img src="$maindir/$imgfile/jobbar1.gif" width=$jobbarchag2 height="8">$jobbardmgg22<img src="$maindir/$imgfile/exp.gif" height="8"></td><td align=right><font color=#$chamoji><b><font face="Westminster">$jobritu72 </font></font><font size=-1>％</td><td><font face="Copperplate Gothic Bold">$kiwame72</td></tr>
HTM
	}
	if ( $master[2] == 1 && $master[1] == 1){
print <<"HTM";
<tr><td><input type=radio name="jobgime" value="8"></td><td><nobr><font color=purple><b>$job[8]</font></nobr></td><td><img src="$maindir/$imgfile/exp.gif" height="10"><img src="$maindir/$imgfile/jobbar1.gif" width=$jobbarcha8 height="8">$jobbardmg88<img src="$maindir/$imgfile/exp.gif" height="8"></td><td align=right><font color=#$chamoji><b><font face="Westminster">$jobritu8 </font></font><font size=-1>％</td><td><font face="Copperplate Gothic Bold">$kiwame8</td></tr>
HTM
	}
	if ( $master[61] == 1 && $master[7] == 1){
print <<"HTM";
<tr><td><input type=radio name="jobgime" value="9"></td><td><nobr><font color=purple><b>$job[9]</font></nobr></td><td><img src="$maindir/$imgfile/exp.gif" height="10"><img src="$maindir/$imgfile/jobbar1.gif" width=$jobbarcha9 height="8">$jobbardmg99<img src="$maindir/$imgfile/exp.gif" height="8"></td><td align=right><font color=#$chamoji><b><font face="Westminster">$jobritu9 </font></font><font size=-1>％</td><td><font face="Copperplate Gothic Bold">$kiwame9</td></tr>
HTM
	}
	if ( $master[42] == 1 && $master[5] == 1){
print <<"HTM";
<tr><td><input type=radio name="jobgime" value="10"></td><td><nobr><font color=purple><b>$job[10]</font></nobr></td><td><img src="$maindir/$imgfile/exp.gif" height="10"><img src="$maindir/$imgfile/jobbar1.gif" width=$jobbarcha10 height="8">$jobbardmg1010<img src="$maindir/$imgfile/exp.gif" height="8"></td><td align=right><font color=#$chamoji><b><font face="Westminster">$jobritu10 </font></font><font size=-1>％</td><td><font face="Copperplate Gothic Bold">$kiwame10</td></tr>
HTM
}
	if ( $master[11] == 1 && $master[12] == 1){
print <<"HTM";
<tr><td><input type=radio name="jobgime" value="79"></td><td><nobr><font color=purple><b>$job[79]</font></nobr></td><td><img src="$maindir/$imgfile/exp.gif" height="10"><img src="$maindir/$imgfile/jobbar1.gif" width=$jobbarcha79 height="8">$jobbardmg7979<img src="$maindir/$imgfile/exp.gif" height="8"></td><td align=right><font color=#$chamoji><b><font face="Westminster">$jobritu79 </font></font><font size=-1>％</td><td><font face="Copperplate Gothic Bold">$kiwame79</td></tr>
HTM
	}
	if ( $master[72] == 1 && $master[0] == 1){
print <<"HTM";
<tr><td><input type=radio name="jobgime" value="80"></td><td><nobr><font color=purple><b>$job[80]</font></nobr></td><td><img src="$maindir/$imgfile/exp.gif" height="10"><img src="$maindir/$imgfile/jobbar1.gif" width=$jobbarcha80 height="8">$jobbardmg8080<img src="$maindir/$imgfile/exp.gif" height="8"></td><td align=right><font color=#$chamoji><b><font face="Westminster">$jobritu80 </font></font><font size=-1>％</td><td><font face="Copperplate Gothic Bold">$kiwame80</td></tr>
HTM
	}
	if ( $master[71] == 1 && $master[52] == 1){
print <<"HTM";
<tr><td><input type=radio name="jobgime" value="81"></td><td><nobr><font color=purple><b>$job[81]</font></nobr></td><td><img src="$maindir/$imgfile/exp.gif" height="10"><img src="$maindir/$imgfile/jobbar1.gif" width=$jobbarcha81 height="8">$jobbardmg8181<img src="$maindir/$imgfile/exp.gif" height="8"></td><td align=right><font color=#$chamoji><b><font face="Westminster">$jobritu81 </font></font><font size=-1>％</td><td><font face="Copperplate Gothic Bold">$kiwame81</td></tr>
HTM
	}
	if ( $master[41] == 1 && $master[12] == 1){
print <<"HTM";
<tr><td><input type=radio name="jobgime" value="82"></td><td><nobr><font color=purple><b>$job[82]</font></nobr></td><td><img src="$maindir/$imgfile/exp.gif" height="10"><img src="$maindir/$imgfile/jobbar1.gif" width=$jobbarcha82 height="8">$jobbardmg8282<img src="$maindir/$imgfile/exp.gif" height="8"></td><td align=right><font color=#$chamoji><b><font face="Westminster">$jobritu82 </font></font><font size=-1>％</td><td><font face="Copperplate Gothic Bold">$kiwame82</td></tr>
HTM
	}
	if ( $master[31] == 1 && $master[6] == 1){
print <<"HTM";
<tr><td><input type=radio name="jobgime" value="83"></td><td><nobr><font color=purple><b>$job[83]</font></nobr></td><td><img src="$maindir/$imgfile/exp.gif" height="10"><img src="$maindir/$imgfile/jobbar1.gif" width=$jobbarcha83 height="8">$jobbardmg8383<img src="$maindir/$imgfile/exp.gif" height="8"></td><td align=right><font color=#$chamoji><b><font face="Westminster">$jobritu83 </font></font><font size=-1>％</td><td><font face="Copperplate Gothic Bold">$kiwame83</td></tr>
HTM
	}
	if ( $master[32] == 1 && $master[7] == 1){
print <<"HTM";
<tr><td><input type=radio name="jobgime" value="84"></td><td><nobr><font color=purple><b>$job[84]</font></nobr></td><td><img src="$maindir/$imgfile/exp.gif" height="10"><img src="$maindir/$imgfile/jobbar1.gif" width=$jobbarcha84 height="8">$jobbardmg8484<img src="$maindir/$imgfile/exp.gif" height="8"></td><td align=right><font color=#$chamoji><b><font face="Westminster">$jobritu84 </font></font><font size=-1>％</td><td><font face="Copperplate Gothic Bold">$kiwame84</td></tr>
HTM
	}
	if ( $master[12] == 1 && $master[5] == 1){
print <<"HTM";
<tr><td><input type=radio name="jobgime" value="85"></td><td><nobr><font color=purple><b>$job[85]</font></nobr></td><td><img src="$maindir/$imgfile/exp.gif" height="10"><img src="$maindir/$imgfile/jobbar1.gif" width=$jobbarcha85 height="8">$jobbardmg8585<img src="$maindir/$imgfile/exp.gif" height="8"></td><td align=right><font color=#$chamoji><b><font face="Westminster">$jobritu85 </font></font><font size=-1>％</td><td><font face="Copperplate Gothic Bold">$kiwame85</td></tr>
HTM
	}
	if ( $master[4] == 1 && $master[22] == 1){
print <<"HTM";
<tr><td><input type=radio name="jobgime" value="86"></td><td><nobr><font color=purple><b>$job[86]</font></nobr></td><td><img src="$maindir/$imgfile/exp.gif" height="10"><img src="$maindir/$imgfile/jobbar1.gif" width=$jobbarcha86 height="8">$jobbardmg8686<img src="$maindir/$imgfile/exp.gif" height="8"></td><td align=right><font color=#$chamoji><b><font face="Westminster">$jobritu86 </font></font><font size=-1>％</td><td><font face="Copperplate Gothic Bold">$kiwame86</td></tr>
HTM
	}

	if ( $master[8] == 1 && $master[9] == 1 && $master[10] == 1 && $master[79] == 1 && $master[80] == 1 && $master[81] == 1 && $master[82] == 1 && $master[83] == 1 && $master[84] == 1 && $master[85] == 1 && $master[86] == 1){
print <<"HTM";
<tr><td><input type=radio name="jobgime" value="87"></td><td><nobr><font color=Teal><b>$job[87]</font></nobr></td><td><img src="$maindir/$imgfile/exp.gif" height="10"><img src="$maindir/$imgfile/jobbar1.gif" width=$jobbarcha87 height="8">$jobbardmg8787<img src="$maindir/$imgfile/exp.gif" height="8"></td><td align=right><font color=#$chamoji><b><font face="Westminster">$jobritu87 </font></font><font size=-1>％</td><td><font face="Copperplate Gothic Bold">$kiwame87</td></tr>
HTM
	}

	if ( $master[8] == 1 && $master[9] == 1 && $master[10] == 1 && $master[79] == 1 && $master[80] == 1 && $master[81] == 1 && $master[82] == 1 && $master[83] == 1 && $master[84] == 1 && $master[85] == 1 && $master[86] == 1){
print <<"HTM";
<tr><td><input type=radio name="jobgime" value="88"></td><td><nobr><font color=Teal><b>$job[88]</font></nobr></td><td><img src="$maindir/$imgfile/exp.gif" height="10"><img src="$maindir/$imgfile/jobbar1.gif" width=$jobbarcha88 height="8">$jobbardmg8888<img src="$maindir/$imgfile/exp.gif" height="8"></td><td align=right><font color=#$chamoji><b><font face="Westminster">$jobritu88 </font></font><font size=-1>％</td><td><font face="Copperplate Gothic Bold">$kiwame88</td></tr>
HTM
	}


print <<"HTM";
</table>
<br>
<form method="post" action="./$zonecgi">
<input type=hidden value="6" name="sisetu">
<input type=hidden value="2" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="     転職する     ">
</form>
HTM
		} else { 
&fuseisyori;
		}
	} else {
print <<"HTM";
ここは寺院。<br>
旅の者が新たな人生を求めにくる場所である。<br><br>
HTM
		if ( $master[0] == 1 ){
print <<"HTM";
<b><font color=#$chamoji>$chaname</font></b> よ・・・・<br>
お主は新しい人生を求めるのか？<br><br>
<br>
<form method="post" action="./$zonecgi">
<input type=hidden value="6" name="sisetu">
<input type=hidden value="1" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="     転職する     ">
</form><br>
HTM


		} else {
print <<"HTM";
お主はまだ十\分な経験を積んでいないようだな。<br>
まだ早すぎるようだ。<br>
お主が強くなった時、またお会いしよう。<br><br>
HTM
		}
	}
&townmodori;

1;