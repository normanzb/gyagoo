#�@���Z�𖳌��ɂ��郂���X�^�[��
$none = "�����X�^�[�̖��O";
$none = "�����X�^�[�̖��O";
$none = "�����X�^�[�̖��O";
$none = "�����X�^�[�̖��O";
$none = "�����X�^�[�̖��O";
$none = "�����X�^�[�̖��O";

#�@���̐퓬�f�[�^
$tokuginame = "�򉍎a�S��";
$tokugiserifu ="�u�䂪�錕���󂯂�E�E�v <font color=#$chamoji><b>$chaname</b></font> �͒Ⴂ�p���Ń_�b�V�������I";
$jobhpuprand = "10";
$jobhpup = "19";
$jobrand[2] = "1";
$jobrand[3] = "2";
$jobrand[4] = "5";
$jobrand[5] = "4";
$jobrand[6] = "5";
$jobrand[7] = "5";
$jobrand[8] = "5";
$crit = 250 + $agi;
$tokugihatu = 120 + $int;

##############

sub jobatk {
if ( $master[$chaclass] == 1 && $mast == 0) { $tokugihatu += 50;$mast = 1;}
#srand;
$hissatu = int ( rand(1000) );

	if ( $hissatu < $tokugihatu && $monspop > 40 ) {
print <<"HTM";
$tokugiserifu<br>
<font size=+2 color=#$mojiiro3><b>$tokuginame �I�I</b></font><br>
HTM

	if ($none eq $monsname){
print <<"HTM";
<font color=red>�������A$monsname �ɂ��킳��Ă��܂����I</font><br>
HTM
}else{
print <<"HTM";
�ꌂ�̂��ƂɓG���a����������I�I<br>
HTM
$monshpnow = 0;
}
	} else {

$dmg = int( $str / 3 ) + $pow - $monsac;
#srand;
$dmg += int(rand($chalvl));
		if ( $dmg < 1 ) { $dmg = 0; }
	if ( $usepotion == 1 ) { $dmg = int( $dmg / 3 ); }
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