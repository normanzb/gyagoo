#　勇者の戦闘データ
$tokuginame = "ギガスマッシュ";
$tokugiserifu ="<font color=#$chamoji><b>$chaname</b></font> は敵の頭上を目掛けて力任せに腕を振り下ろした！";
$tokugiturn = "3";
$jobhpuprand = "5";
$jobhpup = "13";
$jobrand[2] = "2";
$jobrand[3] = "3";
$jobrand[4] = "5";
$jobrand[5] = "5";
$jobrand[6] = "6";
$jobrand[7] = "4";
$jobrand[8] = "4";
$crit = 170 + $agi;
$tokugihatu = 50 + $int;
##############
$tokugikouka = 100;

sub jobatk {
if ( $master[$chaclass] == 1 && $mast == 0) { $tokugihatu += 50;$mast = 1;}
	if ( $tokugikouka <= 100 ) {
#srand;
$tokugiritu = rand (1000);
		if ( $tokugiritu < $tokugihatu ) {
$dmg = int( $str / 3 ) + $pow * 10;
print "$tokugiserifu<br><font size=5 color=#$mojiiro3><b>$tokuginame ！！</b></font><br>";
print "$monsname に <font size=4 color=#$mojiiro2><b>$dmg</b></font> のダメージを与えた！<br>";
$monshpnow -= $dmg;
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
$agi -= $chastats[3] * 10000;
print "<font color=#$mojiiro2>特技の効果が切れた</font><br>";
	}
$tokugikouka --;
}



1;