#�@���@���m�̐퓬�f�[�^
$tokuginame = "���@��";
$tokugiserifu ="<font color=#$chamoji><b>$chaname</b></font> �͕���ɖ��@�����ߎn�߂��I";
$tokugiturn = "3";
$jobhpuprand = "5";
$jobhpup = "8";
$jobrand[2] = "5";
$jobrand[3] = "7";
$jobrand[4] = "6";
$jobrand[5] = "10";
$jobrand[6] = "7";
$jobrand[7] = "7";
$jobrand[8] = "7";
$crit = 170 + $agi;
$tokugihatu = 200 + $int;

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
		}
	}

	if ( $tokugikouka > 0 ) {
#srand;
$svritu = rand(2);
		if ( $svritu < 1 ) {
$svkei = $monssvf;
print "<font size=4 color=#$mojiiro2><b>�Α����U���I</b></font><br>";
		} else {
$svkei = $monssvc;
print "<font size=4 color=#$mojiiro4><b>�������U���I</b></font><br>";
		}
$dmg = int( $str / 3 ) + $pow - int( $monsac / 2 ) - $svkei;
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