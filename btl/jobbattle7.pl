#　吟遊詩人の戦闘データ
$tokuginame = "誘惑の\ソ\ング";
$tokugiserifu ="<font color=#$chamoji><b>$chaname</b></font> はいきなり竪琴を取り出し奏で始めた！";
$tokugiturn = "4";
$jobhpuprand = "4";
$jobhpup = "7";
$jobrand[2] = "10";
$jobrand[3] = "8";
$jobrand[4] = "7";
$jobrand[5] = "3";
$jobrand[6] = "5";
$jobrand[7] = "5";
$jobrand[8] = "9";
$crit = 240 + $agi;
$tokugihatu = 200 + int ( $cha / 2 ) + int ( $int / 2 );
###########

$tokugikouka = 0;

sub jobatk {
if ( $master[$chaclass] == 1 && $mast == 0) { $tokugihatu += 50;$mast = 1;}
	if ( $tokugikouka <= 0 ) {
#srand;
$tokugiritu = rand (1000);
		if ( $tokugiritu < $tokugihatu ) {
print "$tokugiserifu<br><font size=5 color=#$mojiiro2><b>$tokuginame ！！</b></font><br>";
$tokugikouka = $tokugiturn;
$cha += ($chastats[5] * 10);
		}
	}
$dmg = int( $str / 3 ) + $pow - $monsac;
		if ( $dmg < 1 ) { $dmg = 0; }
#srand;
$dmg += int(rand($chalvl));

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
$cha -= ($chastats[5] * 10);
print "<font color=#$mojiiro4>特技の効果が切れた</font><br>";
	}
$tokugikouka --;
}



1;