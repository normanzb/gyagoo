#�@����t�̐퓬�f�[�^
$tokuginame = "�X���E";
$tokugiserifu ="<font color=#$chamoji><b>$chaname</b></font> �͎��̖��@��G�Ɍ����ĕ������I";
$tokugiturn = "3";
$jobhpuprand = "15";
$jobhpup = "13";
$jobrand[2] = "2";
$jobrand[3] = "3";
$jobrand[4] = "5";
$jobrand[5] = "5";
$jobrand[6] = "6";
$jobrand[7] = "4";
$jobrand[8] = "4";
$crit = 170 + $agi;
$tokugihatu = 100 + $int;
##############
$tokugikouka = 100;

sub jobatk {
if ( $master[$chaclass] == 1 && $mast == 0) { $tokugihatu += 50;$mast = 1;}
	if ( $tokugikouka <= 100 ) {
#srand;
$tokugiritu = rand (1000);
		if ( $tokugiritu < $tokugihatu ) {
print "$tokugiserifu<br><font size=5 color=#$mojiiro3><b>$tokuginame �I�I</b></font><br>";
print "$monsname�̓������T�̂悤�ɒx���Ȃ����I<br>";
$tokugikouka = $tokugiturn;
$agi += $chastats[3] * 10000;
		}
	}
$dmg = int( $str / 3 ) + $pow - $monsac;
#srand;
$dmg += int(rand($chalvl));
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
print "$monsname �� <font size=4 color=#$mojiiro2><b>$dmg</b></font> �̃_���[�W��^�����I<br>";
		}

	if ( $tokugikouka == 1 ) {
$agi -= $chastats[3] * 10000;
print "<font color=#$mojiiro2>���Z�̌��ʂ��؂ꂽ</font><br>";
	}
$tokugikouka --;
}



1;