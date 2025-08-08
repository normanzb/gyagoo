#　呪術師の戦闘データ
$tokuginame = "ドレインホール";
$tokugiserifu ="<font color=#$chamoji><b>$chaname</b></font> の目の前に紫の渦が出現した！";
$jobhpuprand = "12";
$jobhpup = "13";
$jobrand[2] = "4";
$jobrand[3] = "4";
$jobrand[4] = "1";
$jobrand[5] = "4";
$jobrand[6] = "4";
$jobrand[7] = "4";
$jobrand[8] = "2";
$crit = 180 + $agi;
$tokugihatu = 140 + $int;

##############

sub jobatk {
if ( $master[$chaclass] == 1 && $mast == 0) { $tokugihatu += 50;$mast = 1;}
#srand;
$hissatu = int ( rand(1000) );

	if ( $hissatu < $tokugihatu ) {
print <<"HTM";
$tokugiserifu<br>
<font size=+1 color=#$mojiiro4><b>$tokuginame ！！</b></font><br>
HTM
#srand;
$dmg = int((( $str / 4 ) + ($int / 4 ) + $pow - $monsac) * 2 + rand($chalvl));
			if ( $dmg < 1 ) { 
print "<font color=#$mojiiro4>$monsname はヒラリと身をかわした！<br></font>"; 
			} else {
$monshpnow -= $dmg;
$kyuusyuu = int ( $dmg / 2 );
$chahpnow += $kyuusyuu;
		if ( $chahpnow > $chastats[9] ) { $chahpnow = $chastats[9]; }
print "$monsname に <font size=4 color=#$mojiiro2><b>$dmg</b></font> のダメージを与えた！<br>";
print "<font size=4 color=#$mojiiro2><b>$kyuusyuu</b></font> のHPを吸い取った！<br>";
			}
	} else {
#srand;
$mazokusei = rand (3);
	if ( $mazokusei < 1 ) {
print "<b>魔属性攻撃！</b><br>";
$dmg = int( ($str + $int) / 6 ) + $pow - int ($monsac / 2 ) - $monssvm;
	} else {
$dmg = int( $str / 3 ) + $pow - $monsac;
	}
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

	}
}


1;