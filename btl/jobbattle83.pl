#�@�p���f�B���̐퓬�f�[�^
$tokuginame = "�W���X�e�B�X���C�g";
$tokugiserifu ="�u�_��I�@�׈��Ȃ鍰�ɐ��Ȃ�����������܂��I�v<br>";
$jobhpuprand = "19";
$jobhpup = "8";
$jobrand[2] = "9";
$jobrand[3] = "7";
$jobrand[4] = "4";
$jobrand[5] = "7";
$jobrand[6] = "9";
$jobrand[7] = "9";
$jobrand[8] = "5";
$crit = 280 + $agi;
$tokugihatu = 130 + $int;

##############

sub jobatk {
if ( $master[$chaclass] == 1 && $mast == 0) { $tokugihatu += 50;$mast = 1;}
#srand;

$tokugiritu = rand (1000);
		if ( $tokugiritu < $tokugihatu ) {


$damasi = rand(2);
$damasi2 = int($damasi + 0);

$dmg = int( $str / 3 ) + $pow - $monsac;
		if ( $dmg < 1 ) { $dmg = 0; }
#srand;
$dmg += int(rand($chalvl));

if ( $damasi2 == 0 ) {

if ($chahpnow > $chahp){$chahpnow = $chahp;}
print "<b>$tokugiserifu</b><b><font size=5 color=#$mojiiro2>$tokuginame �I�I</b></font><br>��u�ɂ��ĕӂ肪ῂ����ɕ�܂��I<br><font color=blue>$monsname�̐S�Ɍ����h�����I</font><br>";
print "$monsname�͎c�����̗͂�$chaname���񕜂��Ă��ꂽ�B<br>";
print "$chaname��<b>HP</b>��<font color=#$mojiiro3> <b>$monshpnow</b> </font>�񕜂����I<br>";
$chahpnow += $monshpnow;
	if ( $chahpnow > $chastats[9] ) {$chahpnow = $chastats[9];}
$monshpnow = 0;
#srand;

} elsif ( $damasi2 == 1 ) {
$tp = int(rand(3));
$champ += $tp;
if ($champ > $chastats[16]){$champ = $chastats[16];}
print "<b>$tokugiserifu</b><b><font size=5 color=#$mojiiro2>$tokuginame �I�I</b></font><br>��u�ɂ��ĕӂ肪ῂ����ɕ�܂��I<br><font color=blue>$monsname�̐S�Ɍ����h�����I</font><br>";
print "$monsname��$chaname��<b>�s�o</b>���񕜂��Ă��ꂽ�B<br>";
print "$chaname��<b>TP</b>��<font color=#$mojiiro3> <b>$tp</b> </font>�񕜂����I";
$monshpnow = 0;
#srand;
}

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