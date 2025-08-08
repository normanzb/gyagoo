#　魔術師の戦闘データ
$tokuginame = "フレアボム";
$tokugiserifu ="<font color=#$chamoji><b>$chaname</b></font> は静かに呪文を唱えだした！";
$jobhpuprand = "5";
$jobhpup = "7";
$jobrand[2] = "10";
$jobrand[3] = "9";
$jobrand[4] = "3";
$jobrand[5] = "6";
$jobrand[6] = "5";
$jobrand[7] = "5";
$jobrand[8] = "10";
$crit = 200 + $agi;
$tokugihatu = 150 + $int;

##############

sub jobatk {
if ( $master[$chaclass] == 1 && $mast == 0) { $tokugihatu += 50;$mast = 1;}
#srand;
$tokugiritu = rand (1000);
		if ( $tokugiritu < $tokugihatu ) {
print "$tokugiserifu<br><font size=5 color=#$mojiiro3><b>$tokuginame ！！</b></font><br>";
$dmg = int( $int / 3 ) + $pow - int( $monsac / 2 );
		} else {

#srand;
$svritu = rand(6);
			if ( $svritu < 1 ) {
$svkei = $monssvf;
print "<font size=4 color=#$mojiiro2><b>火の呪文を唱えた！</b></font><br>";
$dmg = int( $int / 3 ) + $pow - int( $monsac / 2 ) - $svkei;
			} elsif ( $svritu < 2 ) {
$svkei = $monssvc;
print "<font size=4 color=#$mojiiro4><b>水の呪文を唱えた！</b></font><br>";
$dmg = int( $int / 3 ) + $pow - int( $monsac / 2 ) - $svkei;
			} elsif ( $svritu < 3 ) {
$svkei = $monssvm;
print "<font size=4><b>魔の呪文を唱えた！</b></font><br>";
$dmg = int( $int / 3 ) + $pow - int( $monsac / 2 ) - $svkei;
			} else {
$dmg = int( $str / 3 ) + $pow - $monsac;
			}

		}

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


1;