#�@����m�̐퓬�f�[�^
$tokuginame = "�o���g";
$tokugiserifu ="<font color=#$chamoji><b>$chaname</b></font> �͕����U�肩�����A�Q�C�̋���ȗ����Ăъ񂹂��I";
$jobhpuprand = "22";
$jobhpup = "17";
$jobrand[2] = "3";
$jobrand[3] = "1";
$jobrand[4] = "3";
$jobrand[5] = "4";
$jobrand[6] = "4";
$jobrand[7] = "4";
$jobrand[8] = "5";
$crit = 170 + $agi;
$tokugihatu = 190 + $int;
##############
$tokugikouka = 0;

sub jobatk {
if ( $master[$chaclass] == 1 && $mast == 0) { $tokugihatu += 50;$mast = 1;}
	if ( $tokugikouka <= 0 ) {
#srand;
$tokugiritu = rand (1000);
		if ( $tokugiritu < $tokugihatu ) {

$dmg1 = int( $str / 3 ) + $pow - $monsac;
#srand;
$dmg1 += int(rand($chalvl));
$dmg1 * 4;

		if ( $dmg1 < 1 ) { $dmg1 = 0; }
$dmg2 = int( $str / 3 ) + $pow - $monsac;
#srand;
$dmg2 += int(rand($chalvl));
$dmg2 * 4;
		if ( $dmg2 < 1 ) { $dmg2 = 0; }

print "$tokugiserifu<br><font size=+2 color=#$mojiiro3><b>$tokuginame �I�I</b></font><br>";
print "<b>�Q�C�̋���ȗ���$monsname �ɏP���|����I</b><br><br>";
print "<b>������</b>�͉s���܂�$monsname �������~�����I<br>";
print "$monsname ��<font size=4 color=#$mojiiro2><b>$dmg1</b></font>�̃_���[�W��^�����I<br><br>";
print "<b>�C��</b>�͉s�����$monsname �ɋ�炢�����I<br>";
print "$monsname ��<font size=4 color=#$mojiiro2><b>$dmg2</b></font>�̃_���[�W��^�����I<br><br>";
print "<b>$chaname</b> �̓W�����v�a���������I<br>";
$monshpnow -= $dmg1 + $dmg2;
		}
	}
$dmg = int( $str / 2 ) + $pow - $monsac;
#srand;
$dmg += int(rand($chalvl)) * 2;
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
}




1;