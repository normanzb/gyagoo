#�@�ҏb�g���̐퓬�f�[�^
$jobhpuprand = "15";
$jobhpup = "8";
$jobrand[2] = "9";
$jobrand[3] = "7";
$jobrand[4] = "4";
$jobrand[5] = "7";
$jobrand[6] = "9";
$jobrand[7] = "9";
$jobrand[8] = "5";
$crit = 280 + $agi;
$tokugihatu = 200 + $int;

##############

sub jobatk {
if ( $master[$chaclass] == 1 && $mast == 0) { $tokugihatu += 50;$mast = 1;}
#srand;

$tokugiritu = rand (1000);
		if ( $tokugiritu < $tokugihatu ) {
print "<font color=#$chamoji><b>$chaname</b></font> �͓ˑR���J�𐁂��A��u�ɂ���$monsname�̐S��a�܂����I<br>$monsname�͈��S�������āA$chaname�ɋ߂Â��Ă����B<br>";

$damasi = rand(3);
$damasi2 = int($damasi + 0);

$dmg = int( $str / 3 ) + $pow - $monsac;
		if ( $dmg < 1 ) { $dmg = 0; }
#srand;
$dmg += int(rand($chalvl));

if ( $damasi2 == 0 ) {
$dmg *= 3;
print "$chaname�́A��������$monsname�ɏP�����������I<br>";
print "$monsname �� <font size=4 color=#$mojiiro2><b>$dmg</b></font> �̃_���[�W��^�����I<br>";
#srand;
$monshpnow -= $dmg;
} elsif ( $damasi2 == 1 ) {
 $dmg = int($dmg / 1.5);
print "$chaname�́A�������� $monsname �̉�����A<font color=blue><b>$dmg</font>G</b>���񂾁I<br>";
$chagold += $dmg;

} elsif ( $damasi2 == 2 ) {
print "$chaname�́A��������$monsname����A<font color=#$mojiiro3><b>$chalvl</font>EXP</b>���񂾁I<br>";
$chaexp += $chalvl;
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