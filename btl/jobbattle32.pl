#�@�Í��R�m�̐퓬�f�[�^
$tokuginame = "�h���C���V���[�g";
$tokugiserifu ="<font color=#$chamoji><b>$chaname</b></font> �̕���ɔZ�F�̉����������W�܂�I";
$jobhpuprand = "11";
$jobhpup = "17";
$jobrand[2] = "2";
$jobrand[3] = "3";
$jobrand[4] = "3";
$jobrand[5] = "5";
$jobrand[6] = "5";
$jobrand[7] = "5";
$jobrand[8] = "2";
$crit = 150 + $agi;
$tokugihatu = 210 + $int;

##############

sub jobatk {
if ( $master[$chaclass] == 1 && $mast == 0) { $tokugihatu += 50;$mast = 1;}
#srand;
$hissatu = int ( rand(1000) );

	if ( $hissatu < $tokugihatu ) {
print <<"HTM";
$tokugiserifu<br>
<font size=+1 color=#$mojiiro4><b>$tokuginame �I�I</b></font><br>
HTM
#srand;
$dmg = int((( $str / 3 ) + $pow - $monsac) * 2 + rand($chalvl));
			if ( $dmg < 1 ) { 
print "<font color=#$mojiiro4>$monsname �̓q�����Ɛg�����킵��$dmg�I<br></font>"; 
			} else {
$monshpnow -= $dmg;
$kyuusyuu = int ( $dmg / 3 ) + 1;
$chahpnow += $kyuusyuu;
		if ( $chahpnow > $chastats[9] ) { $chahpnow = $chastats[9]; }
print "$monsname �� <font size=4 color=#$mojiiro2><b>$dmg</b></font> �̃_���[�W��^�����I<br>";
print "<font size=4 color=#$mojiiro2><b>$kyuusyuu</b></font> ��HP���z��������I<br>";
			}
	} else {
#srand;
$mazokusei = rand (4);
	if ( $mazokusei < 1 ) {
print "<b>�������U���I</b><br>";
$dmg = int( ($str + $int) / 6 ) + $pow - int ($monsac / 2 ) - $monssvm;
	} else {
$dmg = int( $str / 3 ) + $pow - $monsac;
	}
		if ( $dmg < 1 ) { $dmg = 0; }
#srand;
$dmg += int(rand($chalvl));

#srand;
$critritu = rand(1000);
		if ( $critritu < $crit ) {
 $dmg *= 2;
print "<font size=4 color=#$mojiiro4>�N���e�B�J���q�b�g�I<br></font>"; 
		}

		if ( $dmg == 0 ) {
print "<font color=#$mojiiro4>$monsname �̓q�����Ɛg�����킵���I<br></font>"; 
		} else {
$monshpnow -= $dmg;
print "$monsname �� <font size=4 color=#$mojiiro2><b>$dmg</b></font> �̃_���[�W��^�����I<br>";
		}

	}
}



1;