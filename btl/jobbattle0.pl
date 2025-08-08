$crit = 40 + $agi;
$jobhpuprand = "5";
$jobhpup = "5";
$jobrand[2] = "10";
$jobrand[3] = "10";
$jobrand[4] = "10";
$jobrand[5] = "10";
$jobrand[6] = "10";
$jobrand[7] = "10";
$jobrand[8] = "10";


sub jobatk {
#srand;
$monsagi = rand(10);
	if ( $monsagi < 1 ) {
print "<font color=#$mojiiro4>$monsname はヒラリと身をかわした！<br></font>"; 
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