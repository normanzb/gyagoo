#　レンジャーの戦闘データ
$tokuginame = "トゥルーショット";
$tokugiserifu ="<font color=#$chamoji><b>$chaname</b></font> が神速で動き出す！";
$tokugiturn = "2";
$jobhpuprand = "10";
$jobhpup = "17";
$jobrand[2] = "3";
$jobrand[3] = "1";
$jobrand[4] = "3";
$jobrand[5] = "4";
$jobrand[6] = "4";
$jobrand[7] = "4";
$jobrand[8] = "5";
$crit = 170 + $agi;
$tokugihatu = 180 + $int;
##############
$tokugikouka = 0;

sub jobatk {
if ( $master[$chaclass] == 1 && $mast == 0) { $tokugihatu += 50;$mast = 1;}
	if ( $tokugikouka <= 0 ) {
#srand;
$tokugiritu = rand (1000);
		if ( $tokugiritu < $tokugihatu ) {
print "$tokugiserifu<br><font size=+2 color=#$mojiiro3><b>$tokuginame ！！</b></font><br>";
$tokugikouka = $tokugiturn;
$agi += 300;
$crit += 300;
		}
	}
$dmg = int( $str / 3 ) + $pow - $monsac;
#srand;
$dmg += int(rand($chalvl));
		if ( $dmg < 1 ) { $dmg = 0; }

#srand;
$critritu = rand(1000);
		if ( $critritu < $crit ) {
 $dmg *= 2;
print "<font size=4 color=#$mojiiro4>クリティカルヒット！<br></font>"; 
		}

		if ( $dmg == 0 ) {
print "<font color=#$mojiiro4>$monsname はヒラリと身をかわした！<br></font>"; 
		} else {
$monshpnow -= $dmg;
print "$monsname に <font size=4 color=#$mojiiro2><b>$dmg</b></font> のダメージを与えた！<br>";
		}

	if ( $tokugikouka == 1 ) {
$agi -= 300;
$crit -= 300;
print "<font color=#$mojiiro2>特技の効果が切れた</font><br>";
	}
$tokugikouka --;
}



1;