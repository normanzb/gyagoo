#　忍者の戦闘データ
$tokuginame = "分身の術";
$tokugiserifu ="<font color=#$chamoji><b>$chaname</b></font> の体の周りに複数の葉が舞い始める！";
$jobhpuprand = "12";
$jobhpup = "16";
$jobrand[2] = "2";
$jobrand[3] = "2";
$jobrand[4] = "4";
$jobrand[5] = "4";
$jobrand[6] = "5";
$jobrand[7] = "5";
$jobrand[8] = "5";
$crit = 150 + $agi;
$tokugihatu = 150 + $int;

##############

sub jobatk {
if ( $master[$chaclass] == 1 && $mast == 0) { $tokugihatu += 50;$mast = 1;}
#srand;
$hissatu = int ( rand(1000) );

	if ( $hissatu < $tokugihatu ) {
print <<"HTM";
$tokugiserifu<br>
<font size=+2 color=#$mojiiro2><b>$tokuginame ！！</b></font><br>
HTM
$hissatu = int ( $chalvl / 20 );
$hissatu2 = 0;
		while ( $hissatu2 < $hissatu ) {
$dmg = int( $str / 3 ) + $pow - $monsac;
#srand;
$dmg += int(rand($chalvl));
#srand;
$critritu = rand(1000);
			if ( $critritu < $crit ) {
 $dmg *= 2;
print "<font size=4 color=#$mojiiro4>クリティカルヒット！<br></font>"; 
			}
			if ( $dmg < 1 ) { $dmg = 0; }
			if ( $dmg == 0 ) {
print "<font color=#$mojiiro4>$monsname はヒラリと身をかわした！<br></font>"; 
			} else {
$monshpnow -= $dmg;
print "$monsname に <font size=4 color=#$mojiiro2><b>$dmg</b></font> のダメージを与えた！<br>";
			}
			if ( $monshp < 0 ) { last; }
$hissatu2 ++;
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