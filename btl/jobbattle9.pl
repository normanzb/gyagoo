#�@���҂̐퓬�f�[�^
$tokuginame = "�n�C�p�[�q�[�����O";
$tokugiserifu ="<font color=#$chamoji><b>$chaname</b></font> �͓ˑR�F�肾�����I�u�_��I�@��ɂ�������I�v";
$jobhpuprand = "14";
$jobhpup = "14";
$jobrand[2] = "4";
$jobrand[3] = "5";
$jobrand[4] = "1";
$jobrand[5] = "3";
$jobrand[6] = "3";
$jobrand[7] = "3";
$jobrand[8] = "3";
$crit = 300 + $agi;
$tokugihatu = 150 + $int;

##############

sub jobatk {
if ( $master[$chaclass] == 1 && $mast == 0) { $tokugihatu += 50;$mast = 1;}
#srand;
$tokugiritu = rand (1000);
		if ( $tokugiritu < $tokugihatu ) {
print "$tokugiserifu<br><font size=5 color=#$mojiiro2><b>$tokuginame �I�I</b></font><br>";
$dmg = int( ($int * 3 ) + rand($chalvl) );
			if ( $dmg < 1 ) { $dmg = 0; }
#srand;
$dmg += int(rand($chalvl));
#srand;
$critritu = rand(1000);
			if ( $critritu < $crit ) {
$dmg *= 5;
print "<font size=4 color=#$mojiiro4>�F�肪�͂����I<br></font>"; 
			}
$chahpnow += $dmg;
				if ( $chahpnow > $chastats[9] ) {
$chahpnow = $chastats[9];
				}
print "HP�� <font color=#$mojiiro4><b>$dmg</b></font> �񕜂����I<br>";

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