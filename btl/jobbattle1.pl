#�@��m�̐퓬�f�[�^
$tokuginame = "��ɂ̗Y����";
$tokugiserifu ="�u��������������v<font color=#$chamoji><b>$chaname</b></font> �̋ؗ͂��������Ă����I";
$tokugiturn = "3";
$jobhpuprand = "5";
$jobhpup = "10";
$jobrand[2] = "3";
$jobrand[3] = "5";
$jobrand[4] = "10";
$jobrand[5] = "8";
$jobrand[6] = "10";
$jobrand[7] = "10";
$jobrand[8] = "10";
$crit = 170 + $agi;
$tokugihatu = 130 + $int;
##############
$tokugikouka = 0;

sub jobatk {
if ( $master[$chaclass] == 1 && $mast == 0) { $tokugihatu += 50;$mast = 1;}
	if ( $tokugikouka <= 0 ) {
#srand;
$tokugiritu = rand (1000);
		if ( $tokugiritu < $tokugihatu ) {
print "$tokugiserifu<br><font size=5 color=#$mojiiro3><b>$tokuginame �I�I</b></font><br>";
$tokugikouka = $tokugiturn;
$str += $chastats[2];
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
$str -= $chastats[2];
print "<font color=#$mojiiro2>���Z�̌��ʂ��؂ꂽ</font><br>";
	}
$tokugikouka --;
}



1;