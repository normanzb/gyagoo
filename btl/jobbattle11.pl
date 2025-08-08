#　特技を無効にするモンスター名
$none = "モンスターの名前";
$none = "モンスターの名前";
$none = "モンスターの名前";
$none = "モンスターの名前";
$none = "モンスターの名前";
$none = "モンスターの名前";

#　侍の戦闘データ
$tokuginame = "飛燕斬鉄剣";
$tokugiserifu ="「我が秘剣を受けよ・・」 <font color=#$chamoji><b>$chaname</b></font> は低い姿勢でダッシュした！";
$jobhpuprand = "10";
$jobhpup = "19";
$jobrand[2] = "1";
$jobrand[3] = "2";
$jobrand[4] = "5";
$jobrand[5] = "4";
$jobrand[6] = "5";
$jobrand[7] = "5";
$jobrand[8] = "5";
$crit = 250 + $agi;
$tokugihatu = 120 + $int;

##############

sub jobatk {
if ( $master[$chaclass] == 1 && $mast == 0) { $tokugihatu += 50;$mast = 1;}
#srand;
$hissatu = int ( rand(1000) );

	if ( $hissatu < $tokugihatu && $monspop > 40 ) {
print <<"HTM";
$tokugiserifu<br>
<font size=+2 color=#$mojiiro3><b>$tokuginame ！！</b></font><br>
HTM

	if ($none eq $monsname){
print <<"HTM";
<font color=red>しかし、$monsname にかわされてしまった！</font><br>
HTM
}else{
print <<"HTM";
一撃のもとに敵を斬り崩したっ！！<br>
HTM
$monshpnow = 0;
}
	} else {

$dmg = int( $str / 3 ) + $pow - $monsac;
#srand;
$dmg += int(rand($chalvl));
		if ( $dmg < 1 ) { $dmg = 0; }
	if ( $usepotion == 1 ) { $dmg = int( $dmg / 3 ); }
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