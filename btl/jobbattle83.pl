#　パラディンの戦闘データ
$tokuginame = "ジャスティスライト";
$tokugiserifu ="「神よ！　邪悪なる魂に聖なる光を授けたまえ！」<br>";
$jobhpuprand = "19";
$jobhpup = "8";
$jobrand[2] = "9";
$jobrand[3] = "7";
$jobrand[4] = "4";
$jobrand[5] = "7";
$jobrand[6] = "9";
$jobrand[7] = "9";
$jobrand[8] = "5";
$crit = 280 + $agi;
$tokugihatu = 130 + $int;

##############

sub jobatk {
if ( $master[$chaclass] == 1 && $mast == 0) { $tokugihatu += 50;$mast = 1;}
#srand;

$tokugiritu = rand (1000);
		if ( $tokugiritu < $tokugihatu ) {


$damasi = rand(2);
$damasi2 = int($damasi + 0);

$dmg = int( $str / 3 ) + $pow - $monsac;
		if ( $dmg < 1 ) { $dmg = 0; }
#srand;
$dmg += int(rand($chalvl));

if ( $damasi2 == 0 ) {

if ($chahpnow > $chahp){$chahpnow = $chahp;}
print "<b>$tokugiserifu</b><b><font size=5 color=#$mojiiro2>$tokuginame ！！</b></font><br>一瞬にして辺りが眩い光に包まれる！<br><font color=blue>$monsnameの心に光が宿った！</font><br>";
print "$monsnameは残った体力で$chanameを回復してくれた。<br>";
print "$chanameの<b>HP</b>が<font color=#$mojiiro3> <b>$monshpnow</b> </font>回復した！<br>";
$chahpnow += $monshpnow;
	if ( $chahpnow > $chastats[9] ) {$chahpnow = $chastats[9];}
$monshpnow = 0;
#srand;

} elsif ( $damasi2 == 1 ) {
$tp = int(rand(3));
$champ += $tp;
if ($champ > $chastats[16]){$champ = $chastats[16];}
print "<b>$tokugiserifu</b><b><font size=5 color=#$mojiiro2>$tokuginame ！！</b></font><br>一瞬にして辺りが眩い光に包まれる！<br><font color=blue>$monsnameの心に光が宿った！</font><br>";
print "$monsnameは$chanameの<b>ＴＰ</b>を回復してくれた。<br>";
print "$chanameの<b>TP</b>が<font color=#$mojiiro3> <b>$tp</b> </font>回復した！";
$monshpnow = 0;
#srand;
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