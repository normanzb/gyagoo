#�@�푰���ݒ�
$syuok[1] = "����";$syuok[2] = "���l";$syuok[3] = "��b";

#########�@�ݒ�͂����܂Ł@##########

&topsisetu;

if ( $in{riyou} == 1 ) {
	if ( $in{pet1} eq "" ) {
print <<"HTM";
��ށH<br>
�����ƑI������ĂȂ��悤���B<br>
�����Z�����̂łˁB<br>
���炷���B
HTM
	} else {
print <<"HTM";
�x�[�X�ƂȂ郂���X�^�[�́A<br>
<font size=+1><b>$petname[$in{pet1}]</b><font size=-1>($petcode[$in{pet1}])</font></font> �ŊԈႢ�͂Ȃ��ȁH<br><br>
�ł́A�ǂ̃����X�^�[��<br>�C�P�j�G�Ƃ��ĕ�����̂��H�E�E�E<br></td><td width=30></td><td>
<form method="post" action="./$zonecgi">
<input type=hidden value="16" name="sisetu">
<input type=hidden value="11" name="riyou">
<input type=hidden value="$in{pet1}" name="pet1">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="�@ �C�P�j�G��I�� �@" onClick="this.disabled=true; this.value='  ���҂���������  '; this.form.submit();"><br><br>
HTM
$petcode[$in{pet1}] = "";
$waa = 0;$waw =1;
	while ( $waa < 3 ) {
		if ( $petcode[$waa] ne "" ) {
print "<input type=radio name=\"pet2\" value=\"$waa\" checked>$waw�ԖځF<font size=4><b>$petname[$waa]</b></font> ($petcode[$waa])<br>";
		}

$waa ++;$waw ++;
	}
close(PET);
print <<"HTM";
</select></form><br>
HTM
	}
} elsif ( $in{riyou} == 11 ) {
	if ( $in{pet2} eq "" || $in{pet1} eq "") {
print <<"HTM";
���H<br>
�����ƑI������ĂȂ��悤���B<br>
�����Z�����̂łˁB<br>
���炷���B
HTM
	} else {

$newpetlv1 = $petlv[$in{pet1}] + $petlv[$in{pet2}];
$ryoukin = $newpetlv1 * 3;
print <<"HTM";
<font size=+1><b>$petname[$in{pet2}]</b><font size=-1>($petcode[$in{pet2}])</font></font> ���A<br>�C�P�j�G�Ƃ��ĕ�����̂��ȁB<br>
�C�P�j�G�Ƃ��ĕ�����ꂽ�����X�^�[�́A<br>�����߂�͂���B<br><br>
�萔���Ƃ��āA<b><font size=+2><font color=blue>$ryoukin</font></font></b> <b>G</b>�������������B<br><br>
<b>$petname[$in{pet1}]</b><font size=-1>($petcode[$in{pet1}])</font> �̔\\��\��<br>���̂悤�ɕω����邪�A<br>�{���ɂ����̂��ȁH
</td><td width=30></td><td>
HTM
print <<"HTM";
<center><font color=red><font color=red>���̑O</font></font></center>
<table border=1><tr><td rowspan=3>
<img src=\"$maindir/$imgfile/$petpic[$in{pet1}].gif\"></td><td colspan=2><nobr>
���O�F<font color=#$chamoji><b>$petname[$in{pet1}]<font size=-1></b>($petcode[$in{pet1}])</font></b></font></nobr>
</td></tr><tr><td>
<nobr>Lvl�F<font color=#$chamoji><b> $petlv[$in{pet1}]</b></font></nobr>
</td><td><nobr>�Q���l(PP)�F <font color=#$chamoji><b>$petritu[$in{pet1}]</b></font></nobr></td></tr><tr><td><nobr><font color=#$chamoji><b>
HTM
	if ( $petkouka[$in{pet1}] == 16 ) {
		print"�����U��";
	} elsif ( $petkouka[$in{pet1}] == 1 ) {
		print"�Α����U��";
	} elsif ( $petkouka[$in{pet1}] == 2 ) {
		print"�������U��";
	} elsif ( $petkouka[$in{pet1}] == 3 ) {
		print"�������U��";
	} elsif ( $petkouka[$in{pet1}] == 4 ) {
		print"�������U��";
	} elsif ( $petkouka[$in{pet1}] == 5 ) {
		print"�H�����U��";
	} elsif ( $petkouka[$in{pet1}] == 6 ) {
		print"������D��";
	} elsif ( $petkouka[$in{pet1}] == 8 ) {
		print"HP��";
	} else {
		print"�X�e�[�^�X�A�b�v";
	}
print <<"HTM";
</b></font></nobr></td><td>
<nobr>���ʒl(EF)�F<font color=#$chamoji><b> $petkouka2[$in{pet1}]</b></font></nobr></td></tr></table>
<br>
HTM



$karicode = $petcode[$in{pet1}];$karilvl = $petlv[$in{pet1}];
$kariname = $petname[$in{pet1}];$karikouka = $petkouka[$in{pet1}];
$kariritu = $petritu[$in{pet1}];$karikouka2 = $petkouka2[$in{pet1}];
$karipic = $petpic[$in{pet1}];$karieff = $peteff[$in{pet1}];
$kariexp = $petexp[$in{pet1}];$karinowexp = $petnowexp[$in{pet1}];
$kariatk = $petatk[$in{pet1}];

$newpetlv1 = $petlv[$in{pet1}] + $petlv[$in{pet2}];
$newpetlv = int($newpetlv1 / 2);
$newpetkouka1 = $petkouka2[$in{pet1}] + $petkouka2[$in{pet2}] + $petlv[$in{pet2}];
$newpetkouka = int($newpetkouka1 / 2);
$newpetritu1 = $petritu[$in{pet1}] + $petritu[$in{pet2}] + $petlv[$in{pet2}];
$newpetritu = int($newpetritu1 / 2);
$newpeteff1 = $peteff[$in{pet1}] + $peteff[$in{pet2}];

print <<"HTM";
<center><font color=red>���̌�</font></center>
<table border=1><tr><td rowspan=3>
<img src=\"$maindir/$imgfile/$petpic[$in{pet1}].gif\"></td><td colspan=2><nobr>
���O�F<font color=#$chamoji><b>$petname[$in{pet1}]<font size=-1></b>($petcode[$in{pet1}])</font></b></font></nobr>
</td></tr><tr><td>
<nobr>Lvl�F<font color=#$chamoji><b> $newpetlv</b></font></nobr>
</td><td><nobr>�Q���l(PP)�F <font color=#$chamoji><b>$newpetritu</b></font></nobr></td></tr><tr><td><nobr><font color=#$chamoji><b>
HTM
	if ( $petkouka[$in{pet1}] == 16 ) {
		print"�����U��";
	} elsif ( $petkouka[$in{pet1}] == 1 ) {
		print"�Α����U��";
	} elsif ( $petkouka[$in{pet1}] == 2 ) {
		print"�������U��";
	} elsif ( $petkouka[$in{pet1}] == 3 ) {
		print"�������U��";
	} elsif ( $petkouka[$in{pet1}] == 4 ) {
		print"�������U��";
	} elsif ( $petkouka[$in{pet1}] == 5 ) {
		print"�H�����U��";
	} elsif ( $petkouka[$in{pet1}] == 6 ) {
		print"������D��";
	} elsif ( $petkouka[$in{pet1}] == 8 ) {
		print"HP��";
	} else {
		print"�X�e�[�^�X�A�b�v";
	}
print <<"HTM";
</b></font></nobr></td><td>
<nobr>���ʒl(EF)�F<font color=#$chamoji><b> $newpetkouka</b></font></nobr></td></tr></table>
HTM



	if ( $uuu == 1 ) {
print <<"HTM";
<br><font size=+3><b>�s���ȏ������s���܂����I</b></font><br>
<font color=red>�f�[�^�j���̋��ꂪ����܂��B</font><br>
HTM

	} else {
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="16" name="sisetu">
<input type=hidden value="12" name="riyou">
<input type=hidden value="$in{pet1}" name="pet1">
<input type=hidden value="$in{pet2}" name="pet2">
<input type=hidden value="$petnam" name="petnam">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="�@����ł����@" onClick="this.disabled=true; this.value='���҂���������'; this.form.submit();"><br>
</form>
HTM
	}
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="16" name="sisetu">
<input type=hidden value="1" name="onemore">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="�@ ��蒼�� �@" onClick="this.disabled=true; this.value='���҂���������'; this.form.submit();"><br>
</form>
HTM
	}
} elsif ( $in{riyou} == 12 ) {
	if($chagold < $ryoukin) {
print <<"HTM";
���K������Ȃ��悤�����B�E�E�E<br>
�c�O�����A���K�𕥂�ʎ҂ɂ͍��̂����Ă�鎖�͂ł���B<br>
�����𒙂߂Ă���A������x���Ȃ����B<br>
HTM
	} else {

$newpetlv1 = $petlv[$in{pet1}] + $petlv[$in{pet2}];
$newpetlv = int($newpetlv1 / 2);
$newpetkouka1 = $petkouka2[$in{pet1}] + $petkouka2[$in{pet2}]  + $petlv[$in{pet2}];
$newpetkouka = int($newpetkouka1 / 2);
$newpetritu1 = $petritu[$in{pet1}] + $petritu[$in{pet2}] + $petlv[$in{pet2}];
$newpetritu = int($newpetritu1 / 2);
$newpeteff1 = $peteff[$in{pet1}] + $peteff[$in{pet2}];

$petlv[$in{pet1}] = $newpetlv;
$petritu[$in{pet1}] = $newpetritu;
$petkouka2[$in{pet1}] = $newpetkouka;
$petnowexp[$in{pet1}] = 0;
$petexp[$in{pet1}] = int($petexp[$in{pet1}] / 5);
if($petexp[$in{pet1}] < 10) {$petexp[$in{pet1}] = 10;}

$petcode[$in{pet2}] = $petpic[$in{pet2}] = $petritu[$in{pet2}] = $petname[$in{pet2}] = $petkouka[$in{pet2}] = $petkouka2[$in{pet2}] = $petlv[$in{pet2}] = $petkouka[$in{pet2}] = "";
$petexp[$in{pet2}] = 15;
$petnowexp[$in{pet2}] = 0;
$ryoukin = $newpetlv1 * 3;
$chagold -= $ryoukin;

print <<"HTM";
<font size=+3><b>���̊����I</b></font><br><br>
���ށB�����ɍ��̂��I�������悤���B<br><br>
���̂����������X�^�[��������A<br>���ł����Ȃ����B<br>
HTM
&charadatawrt;
}
} else {
	if ( $in{onemore} == 1 ) {
print <<"HTM";
���ށA������x�I�����Ȃ����̂��ȁB<br><br>
HTM
	} else {
print <<"HTM";
�f�r���闷�l��B�悭���Q��ꂽ�B<br>
���̊قł́A����̘A��Ă��郂���X�^�[��<br>
���̂����鎖���o����B<br><br>
HTM
}

$www = 0;$wwa =0;
while ( $wwa < 3 ) {
	if ( $petcode[$wwa] ne "" ) { $www ++; }
$wwa ++;
}
	if ( $www <= 1 ) {
print <<"HTM";
�������A���ׂ̈ɂ̓����X�^�[��<b>�Q�C�ȏ�</b><br>
�A��Ă���K�v������B<br>
�ǂ���炨��́A�����X�^�[���Q�C�ȏ�<br>
�A��Ă��Ȃ��悤���ȁB<br><br>
�����X�^�[��A��āA�܂����Ȃ����B
HTM

	} else {
print <<"HTM";
�܂��́A�x�[�X�ƂȂ郂���X�^�[��I�����Ȃ����B<br></td><td width=30></td><td>
<form method="post" action="./$zonecgi">
<input type=hidden value="16" name="sisetu">
<input type=hidden value="1" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="�@ �x�[�X��I�� �@" onClick="this.disabled=true; this.value='  ���҂���������  '; this.form.submit();"><br><br>
HTM
$waa = 0;$waw =1;
	while ( $waa < 3 ) {
		if ( $petcode[$waa] ne "" ) {
print "<input type=radio name=\"pet1\" value=\"$waa\" checked>$waw�ԖځF<font size=4><b>$petname[$waa]</b></font> ($petcode[$waa])<br>";
		}
$waa ++;$waw ++;



	}
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