#�@���[�h�̐퓬�f�[�^
$tokuginame = "���C�g�j���O�C���p�N�g";
$tokugiserifu ="<font color=#$chamoji><b>$chaname</b></font> �͓���ɗ��_���Ăъ񂹂��I";
$jobhpuprand = "9";
$jobhpup = "17";
$jobrand[2] = "2";
$jobrand[3] = "2";
$jobrand[4] = "4";
$jobrand[5] = "5";
$jobrand[6] = "4";
$jobrand[7] = "4";
$jobrand[8] = "4";
$crit = 250 + $agi;
$tokugihatu = 210 + $int;

##############
$tokugikouka = 0;

sub jobatk {
if ( $master[$chaclass] == 1 && $mast == 0) { $tokugihatu += 50;$mast = 1;}
	if ( $tokugikouka <= 0 ) {
#srand;
$tokugiritu = rand (1000);
		if ( $tokugiritu < $tokugihatu ) {
print "$tokugiserifu<br><font size=5 color=#$mojiiro3><b>$tokuginame �I�I</b></font><br>";
#srand;
$tokugikouka = int( rand($chalvl / 10) + 1);
		}
	}

	if ( $tokugikouka > 0 ) {

print "<font size=4 color=#$mojiiro4><b>�������U���I</b></font><br>";
#srand;
$dmg = int(( $int / 3 ) + $pow - ( $monsac / 2 ));
	} else {
$dmg = int( $str / 3 ) + $pow - $monsac;
	} 
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
print "<font color=#$mojiiro2>���Z�̌��ʂ��؂ꂽ</font><br>";
	}
$tokugikouka --;
}



1;