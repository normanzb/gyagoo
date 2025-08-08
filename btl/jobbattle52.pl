#　幻獣師の戦闘データ
$tokuginame = "竜神・シルベス";
$tokugiserifu ="<font color=#$chamoji><b>$chaname</b></font> は究極の幻獣を召喚し始めた！";
$jobhpuprand = "11";
$jobhpup = "13";
$jobrand[2] = "5";
$jobrand[3] = "4";
$jobrand[4] = "1";
$jobrand[5] = "3";
$jobrand[6] = "5";
$jobrand[7] = "5";
$jobrand[8] = "5";
$crit = 10 + $agi;
$tokugihatu = 50 + $int;
$genju[0] = "火霊・シュワ";
$genju[1] = "水霊・シャロンス";
$genju[2] = "魔霊・ブラッピ";
$genju[3] = "火霊・イフリート";
$genju[4] = "水霊・リヴァイアサン";
$genju[5] = "魔霊・デーモン";
##############

sub jobatk {
if ( $master[$chaclass] == 1 && $mast == 0) { $tokugihatu += 50;$mast = 1;}
#srand;
$tokugiritu = rand (1000);
		if ( $tokugiritu < $tokugihatu ) {
print "$tokugiserifu<br><font size=5 color=#$mojiiro3><b>$tokuginame ！！</b></font><br>";
$dmg = int((( $int / 3 ) + $pow - ( $monsac / 2 )) * ( $chalvl / 10 ));
		} else {

#srand;
$svritu = int(rand(9));
			if ( $svritu < 6 ) {
@svkei = ($svf,$svc,$svm,$svf,$svc,$svm);
				if ( $svritu > 2 ) { $baikouka = 2; } else { $baikouka = 1; }
print "<font size=4 color=#$mojiiro2><b>$genju[$svritu] を召喚した！</b></font><br>";
$dmg = int((( $int / 3 ) + $pow - ( $monsac / 2 ) - $svkei[$svritu]) * $baikouka );
			} else {
$dmg = int( $str / 3 ) + $pow - $monsac;
			}

		}


#srand;
$dmg += int(rand($chalvl));

#srand;
$critritu = rand(1000);
		if ( $critritu < $crit ) {
 $dmg *= 2;
print "<font size=4 color=#$mojiiro4>クリティカルヒット！<br></font>"; 
		}

		if ( $dmg < 1 ) {
print "<font color=#$mojiiro4>$monsname はヒラリと身をかわした！<br></font>"; 
		} else {
$monshpnow -= $dmg;
print "$monsname に <font size=4 color=#$mojiiro2><b>$dmg</b></font> のダメージを与えた！<br>";
		}

}


1;