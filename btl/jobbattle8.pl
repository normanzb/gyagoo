#�@�k�l�̐퓬�f�[�^
$tokuginame = "����";
$tokugiserifu ="<font color=#$chamoji><b>$chaname</b></font> �͕������蓊���A���ɋC���W�����͂��߂��I";
$jobhpuprand = "13";
$jobhpup = "20";
$jobrand[2] = "1";
$jobrand[3] = "2";
$jobrand[4] = "5";
$jobrand[5] = "4";
$jobrand[6] = "5";
$jobrand[7] = "5";
$jobrand[8] = "5";
$crit = 150 + $agi;
$tokugihatu = 180 + $int;

##############

sub jobatk {
if ( $master[$chaclass] == 1 && $mast == 0) { $tokugihatu += 50;$mast = 1;}

#srand;
$hissatu = int ( rand(1000) );

	if ( $hissatu < $tokugihatu ) {
print <<"HTM";
$tokugiserifu<br><br>
<font size=+2 color=#$mojiiro3><b>$tokuginame �I�I</b></font><br>
<font size=+1>����P���I�[�����܂Ƃ�������<b>$monsname</b>�̐g�̂�A�ł���I</font><br>
HTM

#srand;
$hissatu = rand ( int ( $chalvl / 3 ) );
$hissatu2 = 0;
		while ( $hissatu2 < $hissatu ) {
$dmg = int( $str / 5 ) - $monsac;
#srand;
$dmg += int(rand($chalvl));
			if ( $dmg < 1 ) { $dmg = 0; }
			if ( $dmg == 0 ) {
print "<font color=#$mojiiro4>$monsname �̓q�����Ɛg�����킵���I<br></font>"; 
			} else {
$monshpnow -= $dmg;
print "$monsname �� <font size=4 color=#$mojiiro2><b>$dmg</b></font> �̃_���[�W��^�����I<br>";
			}
			if ( $monshp < 0 ) { last; }


$hissatu2 ++;
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