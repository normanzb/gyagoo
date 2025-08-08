#　盗賊の戦闘データ
$tokuginame = "金盗";
$tokugiserifu ="<font color=#$chamoji><b>$chaname</b></font> は目にもとまらぬ速さで、敵の懐に潜り込んだ！";
$jobhpuprand = "13";
$jobhpup = "16";
$jobrand[2] = "1";
$jobrand[3] = "2";
$jobrand[4] = "5";
$jobrand[5] = "4";
$jobrand[6] = "5";
$jobrand[7] = "5";
$jobrand[8] = "5";
$crit = 150 + $agi;
$tokugihatu = $int;

##############
$nusumi = 0;
sub jobatk {
if ( $master[$chaclass] == 1 && $mast == 0) { $tokugihatu += 50;$mast = 1;}
#srand;
$hissatu = int ( rand(1000) );

	if ( $hissatu < $tokugihatu && $nusumi == 0) {
$getgold = int( $str / 3 ) + $pow - $monsac;
		if ( $getgold > 200 ) { $getgold = 200; }
$nusumi = 1;
print <<"HTM";
$tokugiserifu<br>
$monsname から <font color=blue><b>$getgold</font>G</b>盗んだ！</b><br>
HTM
$chagold += $getgold;
#srand;
$dmg += int(rand($chalvl));
			if ( $dmg < 1 ) { $dmg = 0; }
			if ( $dmg == 0 ) {
print "<font color=#$mojiiro4>$monsname はヒラリと身をかわした！<br></font>"; 

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