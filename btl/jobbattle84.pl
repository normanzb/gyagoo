#　闇の詩人の戦闘データ
$tokuginame = "暗黒の詩";
$tokugiserifu ="<font color=#$chamoji><b>$chaname</b></font> は黒いオーラを漂わせ、不思議な詩を詠いだした！";
$tokugiturn = "0";
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
$tokugihatu = 350 + $int;
##############
$tokugikouka = 0;

sub jobatk {
if ( $master[$chaclass] == 1 && $mast == 0) { $tokugihatu += 50;$mast = 1;}
	if ( $tokugikouka <= 0 ) {
#srand;
$tokugiritu = rand (1000);
		if ( $tokugiritu < $tokugihatu ) {
$tokugi += 2;
print "$tokugiserifu<br><font size=+2 color=#$mojiiro3><b>$tokuginame ！！</b></font><br>";
$tokugikouka = $tokugiturn;
$kyuusyuu = int(rand($chalvl));

print "黒いオーラが $monsname を包み込んだ！<br>";
		}
	}
$dmg = int( $str / 3 ) + $pow - $monsac;
#srand;
$dmg += int(rand($chalvl / 1.5));
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
print "$monsname に <font size=4 color=#$mojiiro2><b>$dmg</b></font> のダメージを与えた！<br><br>";
		}

	if ( $tokugi > 1 ) {

$kyuusyuu = int(rand($chalvl + 10));

$chahpnow += $kyuusyuu;
				if ( $chahpnow > $chastats[9] ) {
$chahpnow = $chastats[9];
				}
$monshpnow -= $kyuusyuu;
print "暗黒の詩を聴いている $monsname からHPを<font color=#$mojiiro3><b>$kyuusyuu</b></font>吸収した！<br>";
	}
$tokugikouka --;
}



1;