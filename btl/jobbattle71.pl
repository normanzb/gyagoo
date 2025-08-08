#　魔獣士の戦闘データ
$tokuginame = "がんばれペットちゃん";
$tokugiserifu ="<font color=#$chamoji><b>$chaname</b></font> はペットを応援し始めた！";
$tokugiturn = "3";
$jobhpuprand = "12";
$jobhpup = "13";
$jobrand[2] = "5";
$jobrand[3] = "3";
$jobrand[4] = "3";
$jobrand[5] = "1";
$jobrand[6] = "4";
$jobrand[7] = "4";
$jobrand[8] = "4";
$crit = 280 + $agi;
$tokugihatu = 150 + int ( ($cha / 2) + ($int / 2) );
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
$cha += 1000;
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
$cha -= 1000;
print "<font color=#$mojiiro4>特技の効果が切れた</font><br>";
	}
$tokugikouka --;
}



1;