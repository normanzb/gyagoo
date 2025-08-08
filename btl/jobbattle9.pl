#　賢者の戦闘データ
$tokuginame = "ハイパーヒーリング";
$tokugiserifu ="<font color=#$chamoji><b>$chaname</b></font> は突然祈りだした！「神よ！　我にご加護を！」";
$jobhpuprand = "14";
$jobhpup = "14";
$jobrand[2] = "4";
$jobrand[3] = "5";
$jobrand[4] = "1";
$jobrand[5] = "3";
$jobrand[6] = "3";
$jobrand[7] = "3";
$jobrand[8] = "3";
$crit = 300 + $agi;
$tokugihatu = 150 + $int;

##############

sub jobatk {
if ( $master[$chaclass] == 1 && $mast == 0) { $tokugihatu += 50;$mast = 1;}
#srand;
$tokugiritu = rand (1000);
		if ( $tokugiritu < $tokugihatu ) {
print "$tokugiserifu<br><font size=5 color=#$mojiiro2><b>$tokuginame ！！</b></font><br>";
$dmg = int( ($int * 3 ) + rand($chalvl) );
			if ( $dmg < 1 ) { $dmg = 0; }
#srand;
$dmg += int(rand($chalvl));
#srand;
$critritu = rand(1000);
			if ( $critritu < $crit ) {
$dmg *= 5;
print "<font size=4 color=#$mojiiro4>祈りが届いた！<br></font>"; 
			}
$chahpnow += $dmg;
				if ( $chahpnow > $chastats[9] ) {
$chahpnow = $chastats[9];
				}
print "HPが <font color=#$mojiiro4><b>$dmg</b></font> 回復した！<br>";

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