# �S���҂̐퓬�f�[�^
$tokuginame = "�n����";
$tokugiserifu ="<font color=#$chamoji><b>$chaname</b></font> �͕���ŋ�ɉ~��`�����I";
$tokugiserifu2 ="�󒆂Ɍ����󂫁A��������G�̃G�l���M�|���z���񂹂�I";
$jobhpuprand = "10";
$jobhpup = "16";
$jobrand[2] = "3";
$jobrand[3] = "3";
$jobrand[4] = "5";
$jobrand[5] = "5";
$jobrand[6] = "1";
$jobrand[7] = "1";
$jobrand[8] = "5";
$crit = 250 + $agi + $int;

##############

sub jobatk {


$dmg = int( $str / 3 ) + $pow - $monsac;
		if ( $dmg < 1 ) { $dmg = 0; }
#srand;
$dmg += int(rand($chalvl));

#srand;
$critritu = rand(1000);
		if ( $critritu < $crit ) {
#srand;
$tokugiritu = rand (4);
			if ( $tokugiritu < 1 ) {
$dmg = int(( $dmg - ($monsac / 2)) * $chalvl / 20 );
print "$tokugiserifu<br><font size=5 color=#$mojiiro2><b>$tokuginame �I�I</b></font><br>$tokugiserifu2<br>";
$chahpnow += $dmg;
print "<font color=#$chamoji><b>$chaname</b></font> ��HP��<font color=#$mojiiro3><b>$dmg</b></font>�񕜂����I<br>";
				if ( $chahpnow > $chastats[9] ) {
$chahpnow = $chastats[9];

				}
			} else {
 $dmg *= 2;
print "<font size=4 color=#$mojiiro4>�N���e�B�J���q�b�g�I<br></font>"; 
			}
		}

		if ( $dmg < 1 ) {
print "<font color=#$mojiiro4>$monsname �̓q�����Ɛg�����킵���I<br></font>"; 
		} else {
$monshpnow -= $dmg;
print "$monsname �� <font size=4 color=#$mojiiro2><b>$dmg</b></font> �̃_���[�W��^�����I<br>";
		}

}



1;