#�@�f�X�i�C�g�̐퓬�f�[�^
$tokuginame = "�W���X�e�B�X���C�g";
$tokugiserifu ="�u�_��I�@�׈��Ȃ鍰�ɐ��Ȃ�����������܂��I�v<br>";
$jobhpuprand = "20";
$jobhpup = "8";
$jobrand[2] = "9";
$jobrand[3] = "7";
$jobrand[4] = "4";
$jobrand[5] = "7";
$jobrand[6] = "9";
$jobrand[7] = "9";
$jobrand[8] = "5";
$crit = 280 + $agi;
$tokugihatu = 600 + $int;

##############

sub jobatk {
if ( $master[$chaclass] == 1 && $mast == 0) { $tokugihatu += 50;$mast = 1;}
#srand;

$tokugiritu = rand (1000);
		if ( $tokugiritu < $tokugihatu ) {
$dmg = int( $str / 3 ) + $pow - $monsac;
		if ( $dmg < 1 ) { $dmg = 0; }
$monshpnow -= $dmg;
print "$monsname �� <font size=4 color=#$mojiiro2><b>$dmg</b></font> �̃_���[�W��^�����I<br>";
$kaihuku = int($dmg / 5);
print "$chaname �� <font size=4 color=#$mojiiro3><b>$kaihuku</b></font> �񕜂����I<br>";
$chahpnow += $kaihuku;
	if($chahpnow > $chastats[9]) {$chahpnow = $chastats[9];}

		} else {

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
		}
}



1;