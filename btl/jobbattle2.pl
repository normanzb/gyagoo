#　モンクの戦闘データ
$tokuginame = "青光波動拳";
$tokugiserifu ="「ハァ～～～ッ」青き光が <font color=#$chamoji><b>$chaname</b></font> の拳をまといだす！";
$jobhpuprand = "6";
$jobhpup = "12";
$jobrand[2] = "2";
$jobrand[3] = "3";
$jobrand[4] = "10";
$jobrand[5] = "10";
$jobrand[6] = "10";
$jobrand[7] = "10";
$jobrand[8] = "10";
$crit = 300 + $agi + $int;

##############

sub jobatk {
if ( $master[$chaclass] == 1 && $mast == 0) { $tokugihatu += 50;$mast = 1;}

$dmg = int( $str / 3 ) + $pow - $monsac;
		if ( $dmg < 1 ) { $dmg = 0; }
#srand;
$dmg += int(rand($chalvl));

#srand;
$critritu = rand(1000);
		if ( $critritu < $crit ) {
#srand;
$tokugiritu = rand (2);
			if ( $tokugiritu < 1 ) {
$dmg = int ( $dmg * 3 );
print "$tokugiserifu<br><font size=5 color=#$mojiiro2><b>$tokuginame ！！</b></font><br>";
			} else {
 $dmg *= 2;
print "<font size=4 color=#$mojiiro4>クリティカルヒット！<br></font>"; 
			}
		}

		if ( $dmg == 0 ) {
print "<font color=#$mojiiro4>$monsname はヒラリと身をかわした！<br></font>"; 
		} else {
$monshpnow -= $dmg;
print "$monsname に <font size=4 color=#$mojiiro2><b>$dmg</b></font> のダメージを与えた！<br>";
		}

}



1;