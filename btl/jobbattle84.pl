#�@�ł̎��l�̐퓬�f�[�^
$tokuginame = "�Í��̎�";
$tokugiserifu ="<font color=#$chamoji><b>$chaname</b></font> �͍����I�[����Y�킹�A�s�v�c�Ȏ����r���������I";
$tokugiturn = "0";
$jobhpuprand = "10";
$jobhpup = "17";
$jobrand[2] = "3";
$jobrand[3] = "1";
$jobrand[4] = "3";
$jobrand[5] = "4";
$jobrand[6] = "4";
$jobrand[7] = "4";
$jobrand[8] = "5";
$crit = 170 + $agi;
$tokugihatu = 350 + $int;
##############
$tokugikouka = 0;

sub jobatk {
if ( $master[$chaclass] == 1 && $mast == 0) { $tokugihatu += 50;$mast = 1;}
	if ( $tokugikouka <= 0 ) {
#srand;
$tokugiritu = rand (1000);
		if ( $tokugiritu < $tokugihatu ) {
$tokugi += 2;
print "$tokugiserifu<br><font size=+2 color=#$mojiiro3><b>$tokuginame �I�I</b></font><br>";
$tokugikouka = $tokugiturn;
$kyuusyuu = int(rand($chalvl));

print "�����I�[���� $monsname ���ݍ��񂾁I<br>";
		}
	}
$dmg = int( $str / 3 ) + $pow - $monsac;
#srand;
$dmg += int(rand($chalvl / 1.5));
		if ( $dmg < 1 ) { $dmg = 0; }

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
print "$monsname �� <font size=4 color=#$mojiiro2><b>$dmg</b></font> �̃_���[�W��^�����I<br><br>";
		}

	if ( $tokugi > 1 ) {

$kyuusyuu = int(rand($chalvl + 10));

$chahpnow += $kyuusyuu;
				if ( $chahpnow > $chastats[9] ) {
$chahpnow = $chastats[9];
				}
$monshpnow -= $kyuusyuu;
print "�Í��̎��𒮂��Ă��� $monsname ����HP��<font color=#$mojiiro3><b>$kyuusyuu</b></font>�z�������I<br>";
	}
$tokugikouka --;
}



1;