#�@�_���T�[�̐퓬�f�[�^
$tokuginame = "�ؒ�����";
$tokugiserifu ="<font color=#$chamoji><b>$chaname</b></font> �����Y�~�J���ɗx�肾���I";
$tokugiturn = "2";
$jobhpuprand = "14";
$jobhpup = "12";
$jobrand[2] = "5";
$jobrand[3] = "1";
$jobrand[4] = "3";
$jobrand[5] = "3";
$jobrand[6] = "4";
$jobrand[7] = "4";
$jobrand[8] = "4";
$crit = 240 + $agi;
$tokugihatu = 230 + int (( $cha / 2 ) + ( $int / 2 ));
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
$cha += ( $chastats[5] * 9);
$ac += int( $chastats[1] / 5 );
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
$cha -= ( $chastats[5] * 9);
$ac -= int( $chastats[1] / 5 );
print "<font color=#$mojiiro4>���Z�̌��ʂ��؂ꂽ</font><br>";
	}
$tokugikouka --;
}


1;