#　猛獣使いの戦闘データ
$jobhpuprand = "15";
$jobhpup = "8";
$jobrand[2] = "9";
$jobrand[3] = "7";
$jobrand[4] = "4";
$jobrand[5] = "7";
$jobrand[6] = "9";
$jobrand[7] = "9";
$jobrand[8] = "5";
$crit = 280 + $agi;
$tokugihatu = 200 + $int;

##############

sub jobatk {
if ( $master[$chaclass] == 1 && $mast == 0) { $tokugihatu += 50;$mast = 1;}
#srand;

$tokugiritu = rand (1000);
		if ( $tokugiritu < $tokugihatu ) {
print "<font color=#$chamoji><b>$chaname</b></font> は突然口笛を吹き、一瞬にして$monsnameの心を和ませた！<br>$monsnameは安心しきって、$chanameに近づいてきた。<br>";

$damasi = rand(3);
$damasi2 = int($damasi + 0);

$dmg = int( $str / 3 ) + $pow - $monsac;
		if ( $dmg < 1 ) { $dmg = 0; }
#srand;
$dmg += int(rand($chalvl));

if ( $damasi2 == 0 ) {
$dmg *= 3;
print "$chanameは、すかさず$monsnameに襲撃をかけた！<br>";
print "$monsname に <font size=4 color=#$mojiiro2><b>$dmg</b></font> のダメージを与えた！<br>";
#srand;
$monshpnow -= $dmg;
} elsif ( $damasi2 == 1 ) {
 $dmg = int($dmg / 1.5);
print "$chanameは、すかさず $monsname の懐から、<font color=blue><b>$dmg</font>G</b>盗んだ！<br>";
$chagold += $dmg;

} elsif ( $damasi2 == 2 ) {
print "$chanameは、すかさず$monsnameから、<font color=#$mojiiro3><b>$chalvl</font>EXP</b>盗んだ！<br>";
$chaexp += $chalvl;
}

		} else {

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
		}
}



1;