#�@���b�t�̐퓬�f�[�^
$tokuginame = "���_�E�V���x�X";
$tokugiserifu ="<font color=#$chamoji><b>$chaname</b></font> �͋��ɂ̌��b���������n�߂��I";
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
$genju[0] = "�Η�E�V����";
$genju[1] = "����E�V�������X";
$genju[2] = "����E�u���b�s";
$genju[3] = "�Η�E�C�t���[�g";
$genju[4] = "����E�����@�C�A�T��";
$genju[5] = "����E�f�[����";
##############

sub jobatk {
if ( $master[$chaclass] == 1 && $mast == 0) { $tokugihatu += 50;$mast = 1;}
#srand;
$tokugiritu = rand (1000);
		if ( $tokugiritu < $tokugihatu ) {
print "$tokugiserifu<br><font size=5 color=#$mojiiro3><b>$tokuginame �I�I</b></font><br>";
$dmg = int((( $int / 3 ) + $pow - ( $monsac / 2 )) * ( $chalvl / 10 ));
		} else {

#srand;
$svritu = int(rand(9));
			if ( $svritu < 6 ) {
@svkei = ($svf,$svc,$svm,$svf,$svc,$svm);
				if ( $svritu > 2 ) { $baikouka = 2; } else { $baikouka = 1; }
print "<font size=4 color=#$mojiiro2><b>$genju[$svritu] �����������I</b></font><br>";
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
print "<font size=4 color=#$mojiiro4>�N���e�B�J���q�b�g�I<br></font>"; 
		}

		if ( $dmg < 1 ) {
print "<font color=#$mojiiro4>$monsname �̓q�����Ɛg�����킵���I<br></font>"; 
		} else {
$monshpnow -= $dmg;
print "$monsname �� <font size=4 color=#$mojiiro2><b>$dmg</b></font> �̃_���[�W��^�����I<br>";
		}

}


1;