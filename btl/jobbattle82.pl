#　竜戦士の戦闘データ
$tokuginame = "双龍波";
$tokugiserifu ="<font color=#$chamoji><b>$chaname</b></font> は武器を振りかざし、２匹の巨大な龍を呼び寄せた！";
$jobhpuprand = "22";
$jobhpup = "17";
$jobrand[2] = "3";
$jobrand[3] = "1";
$jobrand[4] = "3";
$jobrand[5] = "4";
$jobrand[6] = "4";
$jobrand[7] = "4";
$jobrand[8] = "5";
$crit = 170 + $agi;
$tokugihatu = 190 + $int;
##############
$tokugikouka = 0;

sub jobatk {
if ( $master[$chaclass] == 1 && $mast == 0) { $tokugihatu += 50;$mast = 1;}
	if ( $tokugikouka <= 0 ) {
#srand;
$tokugiritu = rand (1000);
		if ( $tokugiritu < $tokugihatu ) {

$dmg1 = int( $str / 3 ) + $pow - $monsac;
#srand;
$dmg1 += int(rand($chalvl));
$dmg1 * 4;

		if ( $dmg1 < 1 ) { $dmg1 = 0; }
$dmg2 = int( $str / 3 ) + $pow - $monsac;
#srand;
$dmg2 += int(rand($chalvl));
$dmg2 * 4;
		if ( $dmg2 < 1 ) { $dmg2 = 0; }

print "$tokugiserifu<br><font size=+2 color=#$mojiiro3><b>$tokuginame ！！</b></font><br>";
print "<b>２匹の巨大な龍が$monsname に襲い掛かる！</b><br><br>";
print "<b>紫炎龍</b>は鋭い爪で$monsname を引っ掻いた！<br>";
print "$monsname に<font size=4 color=#$mojiiro2><b>$dmg1</b></font>のダメージを与えた！<br><br>";
print "<b>青海龍</b>は鋭い牙で$monsname に喰らいついた！<br>";
print "$monsname に<font size=4 color=#$mojiiro2><b>$dmg2</b></font>のダメージを与えた！<br><br>";
print "<b>$chaname</b> はジャンプ斬りを放った！<br>";
$monshpnow -= $dmg1 + $dmg2;
		}
	}
$dmg = int( $str / 2 ) + $pow - $monsac;
#srand;
$dmg += int(rand($chalvl)) * 2;
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




1;