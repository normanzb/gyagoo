#�@���p�t�̐퓬�f�[�^
$tokuginame = "�t���A�{��";
$tokugiserifu ="<font color=#$chamoji><b>$chaname</b></font> �͐Â��Ɏ����������������I";
$jobhpuprand = "5";
$jobhpup = "7";
$jobrand[2] = "10";
$jobrand[3] = "9";
$jobrand[4] = "3";
$jobrand[5] = "6";
$jobrand[6] = "5";
$jobrand[7] = "5";
$jobrand[8] = "10";
$crit = 200 + $agi;
$tokugihatu = 150 + $int;

##############

sub jobatk {
if ( $master[$chaclass] == 1 && $mast == 0) { $tokugihatu += 50;$mast = 1;}
#srand;
$tokugiritu = rand (1000);
		if ( $tokugiritu < $tokugihatu ) {
print "$tokugiserifu<br><font size=5 color=#$mojiiro3><b>$tokuginame �I�I</b></font><br>";
$dmg = int( $int / 3 ) + $pow - int( $monsac / 2 );
		} else {

#srand;
$svritu = rand(6);
			if ( $svritu < 1 ) {
$svkei = $monssvf;
print "<font size=4 color=#$mojiiro2><b>�΂̎������������I</b></font><br>";
$dmg = int( $int / 3 ) + $pow - int( $monsac / 2 ) - $svkei;
			} elsif ( $svritu < 2 ) {
$svkei = $monssvc;
print "<font size=4 color=#$mojiiro4><b>���̎������������I</b></font><br>";
$dmg = int( $int / 3 ) + $pow - int( $monsac / 2 ) - $svkei;
			} elsif ( $svritu < 3 ) {
$svkei = $monssvm;
print "<font size=4><b>���̎������������I</b></font><br>";
$dmg = int( $int / 3 ) + $pow - int( $monsac / 2 ) - $svkei;
			} else {
$dmg = int( $str / 3 ) + $pow - $monsac;
			}

		}

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


1;