#�@��V���l�̐퓬�f�[�^
$tokuginame = "�U�f��\�\\���O";
$tokugiserifu ="<font color=#$chamoji><b>$chaname</b></font> �͂����Ȃ�G�Ղ����o���t�Ŏn�߂��I";
$tokugiturn = "4";
$jobhpuprand = "4";
$jobhpup = "7";
$jobrand[2] = "10";
$jobrand[3] = "8";
$jobrand[4] = "7";
$jobrand[5] = "3";
$jobrand[6] = "5";
$jobrand[7] = "5";
$jobrand[8] = "9";
$crit = 240 + $agi;
$tokugihatu = 200 + int ( $cha / 2 ) + int ( $int / 2 );
###########

$tokugikouka = 0;

sub jobatk {
if ( $master[$chaclass] == 1 && $mast == 0) { $tokugihatu += 50;$mast = 1;}
	if ( $tokugikouka <= 0 ) {
#srand;
$tokugiritu = rand (1000);
		if ( $tokugiritu < $tokugihatu ) {
print "$tokugiserifu<br><font size=5 color=#$mojiiro2><b>$tokuginame �I�I</b></font><br>";
$tokugikouka = $tokugiturn;
$cha += ($chastats[5] * 10);
		}
	}
$dmg = int( $str / 3 ) + $pow - $monsac;
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

	if ( $tokugikouka == 1 ) {
$cha -= ($chastats[5] * 10);
print "<font color=#$mojiiro4>���Z�̌��ʂ��؂ꂽ</font><br>";
	}
$tokugikouka --;
}



1;