#�@�����s�y�b�g�̖��O�����
@badname = ( '�o�O�^�[�~�l�[�^�[','���O����','���O����','���O����','���O����' );

#�@�푰���ݒ�
$syuok[1] = "����";$syuok[2] = "���l";$syuok[3] = "��b";

#########�@�ݒ�͂����܂Ł@##########

&topsisetu;

if ( $in{riyou} == 1 ) {
	if ( $in{pet1} eq "" ) {
print <<"HTM";
�w�C�w�C�I<br>
�����ƃy�b�g��I�����ăv���[�Y�B<br>
���Ȃ��ƗV��ł�ɂȂ���B<br>
�O�b�o�C�I
HTM
	} else {
print <<"HTM";
�I�[�C�F�[�B<br>
<font size=+1><b>$in{pet1}</b></font> �ˁB<br><br>
�l�N�X�g�̓j�C�ڂ�I�����ăv���[�Y�B<br></td><td width=30></td><td>
<form method="post" action="./$zonecgi">
<input type=hidden value="5" name="sisetu">
<input type=hidden value="11" name="riyou">
<input type=hidden value="$in{pet1}" name="pet1">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="�@ �Q�C�ڂ�I�� �@" onClick="this.disabled=true; this.value='  ���҂���������  '; this.form.submit();"><br>
<select name="pet2" size=6>
HTM
open(PET,"$maindir/$foldacha/pet_$in{usrid}$bousi2cha$bousikts");
		while ( $petka = <PET> ) {
			chop($petka);
			if ( $petka ne $in{pet1} ) {
print "<option value=\"$petka\">$petka";
			}
		}
close(PET);
print <<"HTM";
</select></form><br>
HTM
	}
} elsif ( $in{riyou} == 11 ) {
	if ( $in{pet2} eq "" || $in{pet1} eq "") {
print <<"HTM";
�w�C�w�C�I<br>
�����ƃy�b�g��I�����ăv���[�Y�B<br>
���Ȃ��ƗV��ł�ɂȂ���B<br>
�O�b�o�C�I
HTM
	} else {
$uuu = 0;
open(PET,"$maindir/pet$bousikts");
		while ( $petka = <PET> ) {
			if ( $uuu == 2 ) { last; }
		($petgousei,$petnam) = split(/,/,$petka);
			if ( $petnam eq $in{pet1} ) {
				$petok1 = $petgousei;$uuu ++;
			}
			if ( $petnam eq $in{pet2} ) {
				$petok2 = $petgousei;$uuu ++;
			}
		}
close(PET);
	if ( $uuu != 2 ) { &fuseisyori;exit;}
($syuzoku1,$gouseinum1) = split(/\//,$petok1);
($syuzoku2,$gouseinum2) = split(/\//,$petok2);
	if ( $syuzoku1 == $syuzoku2 ) {
		if ( $syuzoku1 == 3 ) {
		$syu = 1;
		} else {
		$syu = $syuzoku1 + 1;
		}
	} else {
		$syu = $syuzoku1 + $syuzoku2;
		if ( $syu > 3 ) { $syu = $syu - 3;}
	}
	$syu2 = int(( $gouseinum1 + $gouseinum2 ) / 2);
$sinpet = "$syu/$syu2";
$uuu = 0;
open(PET,"$maindir/pet$bousikts");
		while ( $petka = <PET> ) {
		($petgousei,$petnam,$pete,$petlvl,$petderu,$petatk,$petatk2) = split(/,/,$petka);
			if ( $petgousei eq $sinpet ) {
				$uuu ++;last;
			}
		}
close(PET);

	foreach $i (@badname) {
		if ( $petnam eq $i ) {
print <<"HTM";
�\\�[���[�I<br>
<font size=+1><b>$in{pet1}</b> �� <b>$in{pet2}</b></font> ��<br>
�����������č����ł��Ȃ���B<br><br>
�Ⴄ�y�b�g��I�����ăv���[�Y�B<br>
</td><td width=30></td><td>
HTM
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="5" name="sisetu">
<input type=hidden value="1" name="onemore">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="�@ ��蒼�� �@" onClick="this.disabled=true; this.value='  ���҂���������  '; this.form.submit();"><br>
</form>
HTM
&townmodori;
&pettukitable;
&hpowari;
exit;
		}
	}

print <<"HTM";
�O�b�h�I<br>
<font size=+1><b>$in{pet2}</b></font> �ˁB<br><br>
���̂Q�C�����������<br>���̃y�b�g������������B<br>
</td><td width=30></td><td>
HTM

$uuu = 0;
open(PET,"$maindir/pet$bousikts");
		while ( $petka = <PET> ) {
			if ( $uuu == 2 ) { last; }
		($petgousei,$petnam) = split(/,/,$petka);
			if ( $petnam eq $in{pet1} ) {
				$petok1 = $petgousei;$uuu ++;
			}
			if ( $petnam eq $in{pet2} ) {
				$petok2 = $petgousei;$uuu ++;
			}
		}
close(PET);
	if ( $uuu != 2 ) { &fuseisyori;exit;}
($syuzoku1,$gouseinum1) = split(/\//,$petok1);
($syuzoku2,$gouseinum2) = split(/\//,$petok2);
	if ( $syuzoku1 == $syuzoku2 ) {
		if ( $syuzoku1 == 3 ) {
		$syu = 1;
		} else {
		$syu = $syuzoku1 + 1;
		}
	} else {
		$syu = $syuzoku1 + $syuzoku2;
		if ( $syu > 3 ) { $syu = $syu - 3;}
	}
	$syu2 = int(( $gouseinum1 + $gouseinum2 ) / 2);
$sinpet = "$syu/$syu2";
$uuu = 0;
open(PET,"$maindir/pet$bousikts");
		while ( $petka = <PET> ) {
		($petgousei,$petnam,$pete,$petlvl,$petderu,$petatk,$petatk2) = split(/,/,$petka);
			if ( $petgousei eq $sinpet ) {
				$uuu ++;last;
			}
		}
close(PET);
	if ( $uuu == 0 ) { &fuseisyori;exit; }


print <<"HTM";
<table border=1><tr><td rowspan=3>
<img src="$maindir/$imgfile/$pete.gif"></td><td colspan=2><nobr>
���O(�푰)�F<font color=#$chamoji><b>$petnam</b></font> ( $syuok[$syu] )</nobr>
</td></tr><tr><td>
<nobr>Lvl�F<font color=#$chamoji><b> $petlvl</b></font></nobr>
</td><td><nobr>�퓬�Q���l�F <font color=#$chamoji><b>$petderu</b></font></nobr></td></tr><tr><td><nobr><font color=#$chamoji><b>
HTM

	if ( $petatk == 0 ) {
		print"�����U��";
	} elsif ( $petatk == 1 ) {
		print"�Α����U��";
	} elsif ( $petatk == 2 ) {
		print"�������U��";
	} elsif ( $petatk == 3 ) {
		print"�������U��";
	} elsif ( $petatk == 4 ) {
		print"�������U��";
	} elsif ( $petatk == 5 ) {
		print"�����_�������U��";
	} elsif ( $petatk == 6 ) {
		print"������D��";
	} elsif ( $petatk == 7 ) {
		print"�X�^������";
	} elsif ( $petatk == 8 ) {
		print"HP��";
	} else {
		print"�X�e�[�^�X�A�b�v";
	}
print <<"HTM";
</b></font></nobr></td><td>
<nobr>���ʒl�F<font color=#$chamoji><b> $petatk2</b></font></nobr></td></tr></table>
HTM

$uuu = 0;
open(PET,"$maindir/$foldacha/pet_$in{usrid}$bousi2cha$bousikts");
		while ( $petka = <PET> ) {
			chop($petka);
			if ( $petka eq $petnam ) {
$uuu = 1;last;
			}
		}
close(PET);
	if ( $petcode[0] eq $petnam || $petcode[1] eq $petnam || $petcode[2] eq $petnam ) {
$uuu = 1
	}
open(SHOP,"$maindir/$foldakojin/kojin_$in{usrid}$bousi2cha$bousikts");
$a = <SHOP>;
close(SHOP);
		($shopserifu,$shopserifu2,$shopsina) = split(/,/,$a);
@syouhin = split(/\t/,$shopsina);
	foreach $a ( @syouhin ) {
		($snedana,$snamea) = split(/\//,$a);
		if ( $snamea eq $monsname ) {$uuu = 1;last;}
	}

	if ( $uuu == 1 ) {


print <<"HTM";
<br>�o�[�[�b�g�B<br>���łɂ��Ȃ��͂��̃y�b�g����ˁB<br>
�����獇�����Ă��Ӗ��Ȃ��ˁB
HTM

	} else {
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="5" name="sisetu">
<input type=hidden value="12" name="riyou">
<input type=hidden value="$in{pet1}" name="pet1">
<input type=hidden value="$in{pet2}" name="pet2">
<input type=hidden value="$petnam" name="petnam">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="�@ �������� �@" onClick="this.disabled=true; this.value='  ���҂���������  '; this.form.submit();"><br>
</form>
HTM
	}
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="5" name="sisetu">
<input type=hidden value="1" name="onemore">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="�@ ��蒼�� �@" onClick="this.disabled=true; this.value='  ���҂���������  '; this.form.submit();"><br>
</form>
HTM
	}
} elsif ( $in{riyou} == 12 ) {
	if ( $in{pet1} eq "" || $in{pet2} eq "" || $in{petnam} eq "" ) { &fuseisyori;exit; }
$uuu = 0;
open(PET,"$maindir/$foldacha/pet_$in{usrid}$bousi2cha$bousikts");
		while ( $petka = <PET> ) {
			if ( $uuu == 2 ) { last; }
		chop($petka);
			if ( $petka eq $in{pet1} ) { $uuu ++; }
			if ( $petka eq $in{pet2} ) { $uuu ++; }
		}
close(PET);

	if ( $uuu != 2 ) { &fuseisyori;exit; }

open(PET2,">>$maindir/$foldacha/pet_$in{usrid}.tmp");
flock(PET2,2);
	open(PET,"$maindir/$foldacha/pet_$in{usrid}$bousi2cha$bousikts");
		while ( $petka = <PET> ) {
chop($petka);
			if ( $petka eq $in{pet1} || $petka eq $in{pet2} ) { 
			} else {
print PET2 "$petka\n";
			}
		}
	close(PET);
print PET2 "$in{petnam}\n";
flock(PET2,8);
close(PET2);

rename("$maindir/$foldacha/pet_$in{usrid}.tmp","$maindir/$foldacha/pet_$in{usrid}$bousi2cha$bousikts");

print <<"HTM";
���t�[�[�[�I<br><br>
<font size=+1 color=#$chamoji><b>$in{petnam}</b></font> �����������I<br><br>
$sisetu[4] �ɑ����Ă����ˁB<br>
<form method="post" action="$cgiurl$zonecgi">
<input type=hidden value="5" name="sisetu">
<input type=hidden value="1" name="onemore">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="�@ �������� �@"><br>
</form>

HTM


} else {
	if ( $in{onemore} == 1 ) {
print <<"HTM";
�N�[���b�I<br><br>
���႟����1��g���C���Ă݂�ˁB<br><br>
HTM
	} else {
print <<"HTM";
�n���[�A<font color=#$chamoji><b>$chaname</b></font> �I<br><br>
�������y�b�g�������ɂ����̂����H<br><br>
HTM
	}
$jjj = 0;$jja = 0;
open(PET,"$maindir/$foldacha/pet_$in{usrid}$bousi2cha$bousikts");
	while ( $petka = <PET> ) {
		if ( $jjj > 2 ) { last; }
		if ( $petka ne "" ) { $jja ++; }
$jjj ++;
	}
close(PET);

	if ( $jja < 2 ) {
print <<"HTM";
�m�[�I�@��������̂ɂ�<b>�Q�C�ȏ�</b>�̃y�b�g��<br>
  $sisetu[4] �ɂ��邱�Ƃ��K�v���B<br>
�����ƃy�b�g�𑝂₵�Ă��Ă���B<br>
�@�V�[���[�A�Q�C���I�I<br><br>
HTM
	} else {
print <<"HTM";
�I�[�P�[�x�C�x�[�B<br>
�@���ꂶ�႟�����������y�b�g��<br>
�܂���C�I�����ăv���[�Y�B<br></td><td width=30></td><td>
<form method="post" action="./$zonecgi">
<input type=hidden value="5" name="sisetu">
<input type=hidden value="1" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="�@ �P�C�ڂ�I�� �@" onClick="this.disabled=true; this.value='  ���҂���������  '; this.form.submit();"><br>
<select name="pet1" size=6>
HTM
open(PET,"$maindir/$foldacha/pet_$in{usrid}$bousi2cha$bousikts");
		while ( $petka = <PET> ) {
			chop($petka);
print "<option value=\"$petka\">$petka";
		}
close(PET);
print <<"HTM";
</select></form><br>
HTM

	}

}

&townmodori;
&pettukitable;
&hpowari;

exit;


1;