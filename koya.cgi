#�@�푰���ݒ�
$syuok[1] = "����";$syuok[2] = "���l";$syuok[3] = "��b";

#########�@�ݒ�͂����܂Ł@##########

&topsisetu;
&jobdataload;

&chkchk;

#�@�y�b�g�A��o������
if ( $in{riyou} == 1 ) {
print <<"HTM";
�͂��͂��B<br>�ǂ̃y�b�g��A��o���񂾂��H<br><br>

<form method="post" action="./$zonecgi">
<input type=hidden value="4" name="sisetu">
<input type=hidden value="11" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<select name="pet" size=8>
HTM
open(PET,"$maindir/$foldacha/pet_$in{usrid}$bousi2cha$bousikts");
	while ( $petka = <PET> ) {
chop($petka);
print "<option value=\"$petka\">$petka";
	}
close(PET);
print <<"HTM";
</select><br><br>
���O�����Ă����Ă�����B<br>
<input type=text size=17 name="petnamae" value=""><br>
</td><td width=30></td><td>�z�u�͂ǂ��ɂ���H<br><ul>
HTM
$waa = 0;
	while ( $waa < 3 ) {
		if ( $petcode[$waa] eq "" ) {
$wss = $waa + 1;
print "<input type=radio name=\"iti\" value=\"$waa\" checked>$wss�Ԗ�<br>";
		}
	$waa ++;
	}

print <<"HTM";
</ul>
<input type=submit value="�@   �A��o��  �@" ><br>
</form><br>
HTM


} elsif ( $in{riyou} == 11 ) {
&jobdataload;
	for ( $i=0;$i<3;$i++ ) {
		if($petcode[$i] ne "") { $petpp ++; }
	}
	if ( $petpp >= $jobpet ) { &fuseisyori;exit; }

	if ( $in{petnamae} eq "" ) {
print <<"HTM";
���񂽁A�y�b�g�ɖ��O��<br>
�@�@�t���Ă����Ȃ��Ɖ���������B<br><br>
���ɂ��p���͂��邩���H<br>
HTM
&koyaform;
	} elsif ( $in{pet} eq "" ) {
print <<"HTM";
���񂽁A�y�b�g��<br>
�@�@�I�����Ă���Ȃ��ƍ����B<br><br>
���ɂ��p���͂��邩���H<br>
HTM
&koyaform;
	} elsif ( length($in{petnamae}) > 16 ) {
print <<"HTM";
���񂽁A�y�b�g�̖��O������������B<br>
�@�S�p�łW�����܂łɂ��Ă�����B<br><br>
���ɂ��p���͂��邩���H<br>
HTM
&koyaform;
	} elsif ( $petcode[$in{iti}] ne "" || $in{iti} eq "") {
&fuseisyori;exit;
	} elsif ( $petcode[0] eq $in{pet} || $petcode[1] eq $in{pet} || $petcode[2] eq $in{pet}) {
&fuseisyori;exit;
	} else {

open(PET,"$maindir/pet$bousikts");
		while ( $petmatch = <PET> ) {
		($petgousei,$petnam,$pete,$petlvl,$petderu,$petatk,$petatk2) = split(/,/,$petmatch);
		if ( $in{pet} eq $petnam ) { $dad = 1;last; }
		}
close(PET);
		if ( $dad != 1 ) { &fuseisyori;exit; }
		if ( $petlvl > $chalvl ) {
print <<"HTM";
���`��A<font size=+1><b> $petnam </b></font>�����B<br>
���񂽂ɂႱ�̃y�b�g�͈����Ȃ��˂��B<br>
����������Ǝ�����b���Ă��炾�ˁB<br><br>
���ɂ��p���͂��邩���H
HTM
&koyaform;
		} else {
$in{petnamae} =~ s/</&lt;/g;
$in{petnamae} =~ s/>/&gt;/g;
$in{petnamae} =~ s/,/./g;
$in{petnamae} =~ s/\//_/g;
$petcode[$in{iti}] = $petnam;$petpic[$in{iti}] = $pete;
$petritu[$in{iti}] = $petderu;$petname[$in{iti}] = $in{petnamae};
$petkouka[$in{iti}] = $petatk;$petkouka2[$in{iti}] = $petatk2;$petlv[$in{iti}] = $petlvl;
&charadatawrt;
open(PET,"$maindir/$foldacha/pet_$in{usrid}$bousi2cha$bousikts");
	while ( $petkai = <PET> ) {
		push(@petnakama,$petkai);
	}
close(PET);
open(PET2,">>$maindir/$foldacha/pet_$in{usrid}.tmp");
	foreach $petbu (@petnakama) {
		chop($petbu);
		if ( $petbu ne $petnam ) {
print PET2 "$petbu\n";
		}
	}
close(PET2);
rename("$maindir/$foldacha/pet_$in{usrid}.tmp","$maindir/$foldacha/pet_$in{usrid}$bousi2cha$bousikts");

$basyo = $in{iti} + 1;
print <<"HTM";
�͂��͂��A<font size=+1><b> $petnam </b></font>���ˁB<br>
<font size=+1 color=#$chamoji><b>$petname[$in{iti}] </b></font>�����B<br>
�������O�������˂��`�B<br>
<font size=+1 color=#$mojiiro4><b>$basyo </font>�Ԗ�</b>�ɔz�u���Ă�������B<br>
���킢�����Ă���Ă������B<br><br>
���ɂ��p���͂��邩���H
HTM
$www ++;
&koyaform;
		}


	}

#�@�y�b�g�a������
} elsif ( $in{riyou} == 2 ) {
	if ( $www == 0 ) { &fuseisyori;exit; }
print <<"HTM";
������B<br>
�ŁA�ǂ̃y�b�g��a����񂾂��H<br><br>
<form method="post" action="./$zonecgi">
<input type=hidden value="4" name="sisetu">
<input type=hidden value="21" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="�@     �a����    �@"><br><br>
HTM
$waa = 0;$waw =1;
	while ( $waa < 3 ) {
		if ( $petcode[$waa] ne "" ) {
print "<input type=radio name=\"pet\" value=\"$waa\" checked>$waw�ԖځF<font size=4><b>$petname[$waa]</b></font> ($petcode[$waa])<br>";
		}
$waa ++;$waw ++;
	}
print <<"HTM";
</form></td><td width=30></td><td>
HTM

} elsif ( $in{riyou} == 21 ) {
	if ( $petcode[$in{pet}] eq "" ) { &fuseisyori;exit; }
open(PET,"$maindir/$foldacha/pet_$in{usrid}$bousi2cha$bousikts");
   @pets = <PET>;
close(PET);
  $pet = @pets;
  if ( $pet >= 30 ) {
print <<"HTM";
���₨��A���񂽂̏����͂����y�b�g�ł����ς�����B<br>
����ȏ�͂Ђ��Ƃ�Ȃ���B<br><br>
���ɂ��p���͂��邩���H
HTM

  }else{
push(@pets,"$petcode[$in{pet}]\n");
open(PET,">$maindir/$foldacha/pet_$in{usrid}$bousi2cha$bousikts");
flock(PET,2);
    print PET @pets;
flock(PET,8);
close(PET);


print <<"HTM";
�͂��͂��A<font size=4><b>$petname[$in{pet}] </font>($petcode[$in{pet}])</b>���ˁB<br>
�厖�ɗa�����Ă�����B<br><br>
���ɂ��p���͂��邩���H
HTM
$www --;

$petcode[$in{pet}] = $petpic[$in{pet}] = $petritu[$in{pet}] = $petname[$in{pet}] = $petkouka[$in{pet}] = $petkouka2[$in{pet}] = $petlv[$in{pet}] = $petkouka[$in{pet}] = "";
$petexp[$in{pet}] = 10;
$petnowexp[$in{pet}] = 0;
&charadatawrt;
  }
&koyaform;

#�@�y�b�g�ڍ׏�񏈗�
} elsif ( $in{riyou} == 3 ) {
print <<"HTM";
�ӂނӂށB�y�b�g�̂��ƂȂ玄�ɂ��C���B<br>
�ǂ̃y�b�g�̏���m�肽���񂾂��H<br>
HTM
&syousaipet;


} elsif ( $in{riyou} == 31 ) {
$uuu = 0;
open(PET,"$maindir/pet$bousikts");
		while ( $petka = <PET> ) {
		($petgousei,$petnam,$pete,$petlvl,$petderu,$petatk,$petatk2) = split(/,/,$petka);
			if ( $petnam eq $in{jouhou} ) {
				$uuu ++;last;
			}
		}
close(PET);
	if ( $uuu == 0 ) { &fuseisyori;exit; }
($syu,$gouseinum1) = split(/\//,$petgousei);

print <<"HTM";
<b>$petnam</b>�̏ڍ׏�񂾂�B<br><br>
<table border=1><tr><td rowspan=3>
<img src="$maindir/$imgfile/$pete.gif"></td><td colspan=2><nobr>
���O(�푰)�F<font color=#$chamoji><b>$petnam</b></font> ( $syuok[$syu] )</nobr>
</td></tr><tr><td>
<nobr>Lvl�F<font color=#$chamoji><b> $petlvl</b></font></nobr>
</td><td><nobr>�퓬�Q���l�F <font color=#$chamoji><b>$petderu</b></font></nobr></td></tr><tr>
<td><nobr>���ʒl�F<font color=#$chamoji><b> $petatk2</b></font></nobr></td>
<td><nobr><font color=#$chamoji><b>
HTM
	if ( $petatk == 16 ) {
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
	} elsif ( $petatk == 15 ) {
		print"����s��";
	} else {
		print"�X�e�[�^�X�A�b�v";
	}
print <<"HTM";
</b></font></nobr></td></tr></table><br>�܂��������ׂ邩���H
HTM
&syousaipet;
print "</td><td width=30></td><td>";
&koyaform;

} elsif ( $in{riyou} == 4 ) {
print <<"HTM";
�ǂ̃y�b�g���f�ڂ���񂾂��H<br>
HTM

&zukanpet;

} elsif ( $in{riyou} == 41 ) {
	if ( $in{jouhou} eq "" ) { &fuseisyori;exit;}
$uuu = 0;
open(PET,"$maindir/pet$bousikts");
		while ( $petka = <PET> ) {
		($petgousei,$petnam,$pete,$petlvl,$petderu,$petatk,$petatk2) = split(/,/,$petka);
			if ( $petnam eq $in{jouhou} ) {
				$uuu ++;print"";last;
			}
		}
close(PET);
	if ( $uuu == 0 ) { &fuseisyori;exit; }
($syu,$gouseinum) = split(/\//,$petgousei);


$uuu = 0;
open(PET,"$maindir/$foldazukan/pet$syu$in{usrid}$bousicha$bousikts");
@zukankeisai = <PET>;
close(PET);
		foreach $petka( @zukankeisai ) {
		($petgousei2,$petnam2,$pete2) = split(/,/,$petka);
			if ( $petnam2 eq $in{jouhou} ) {
				$uuu ++;
			}
			$karipet2 ="$petnam2,$pete2";
			$keisaizumi{$karipet2} = $petgousei2;
		}

		if ( $uuu == 1 ) {
print <<"HTM";
<b>$petnam</b>�����B<br>
���̃y�b�g�͂��łɌf�ڍς݂݂������ˁB<br>
���Ɍf�ڂ���y�b�g�͂��邩���H<br>
HTM
		} else {
$karipet = "$petnam,$pete";
$keisaizumi{$karipet} = $gouseinum;
@zukankeisai2 = sort by_character keys(%keisaizumi);

open(PET,">$maindir/$foldazukan/pet$syu$in{usrid}$bousicha$bousikts");
flock(PET,2);
	foreach $zukan3 (@zukankeisai2) {
		print PET "$keisaizumi{$zukan3},$zukan3,\n";
	}
flock(PET,8);
close(PET);
$zukan4 = @zukankeisai2;

print <<"HTM";
<b>$petnam</b>���ˁB<br>
�f�ڂ��Ă�������B<br>
�����<b>$syuok[$syu]</b>�� <b>$zukan4</b> �C�ɂȂ����ˁB<br><br>
���Ɍf�ڂ���y�b�g�͂��邩���H<br>
HTM
		}

&zukanpet;
print "</td><td width=30></td><td>";
&koyaform;


#VER106 Start �y�b�g�������R�}���h
} elsif ( $in{riyou} == 6 ) {
print <<"HTM";
�ǂ̃y�b�g�𓦂����񂾂��H<br>
��x���������猳�ɂ͖߂�Ȃ�����<br>
�T�d�ɑI�����Ȃ�B<br><br>
HTM
  
&sakujopet;
  
} elsif ( $in{riyou} == 61 ) {
	if ( $in{jouhou} eq "" ) { &fuseisyori;exit;}
$uuu = 0;


open(PET,"$maindir/$foldacha/pet_$in{usrid}$bousi2cha$bousikts");

		($petgousei,$petnam,$pete,$petlvl,$petderu,$petatk,$petatk2) = split(/,/,$petka);


  @sakujo = <PET>;
close(PET);
  
  foreach $a (@sakujo){
		chop($a);
	if ( $a eq $in{jouhou} ) {
		$uuu ++;$petnam = $a;
    } else {
      push(@sakujo2,"$a\n");
    }
  }

  if ( $uuu == 0 ) { &fuseisyori;exit; }

open(PET,">$maindir/$foldacha/pet_$in{usrid}$bousi2cha$bousikts");
  flock(PET,2);
    print PET @sakujo2;
  flock(PET,8);
close(PET);

print <<"HTM";

<b>$petnam</b>���ˁB<br>
�������Ă�������B<br>
���ɓ����������y�b�g�͂��邩���H<br>
HTM

&sakujopet;
print "</td><td width=30></td><td>";
&koyaform;


#VER106 End

} else {
print <<"HTM";
����A<font color=#$chamoji><b>$chaname</b></font> �����B<br><br>
���񂽂̃y�b�g�͂����Ɨa�����Ă����B<br>
�����͂ǂ�ȗp�������H<br><br>
HTM
&koyaform;

}

sub koyaform {

	if ( $www < $jobpet ) {
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="4" name="sisetu">
<input type=hidden value="1" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="�@ �y�b�g��A��o�� �@">
</form>
HTM
	}
	if ( $www != 0 ) {
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="4" name="sisetu">
<input type=hidden value="2" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="�@  �y�b�g��a����  �@">
</form>
HTM
	}
	if ( $in{riyou} != 3 ) {
		if ( $in{riyou} != 31 ) {
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="4" name="sisetu">
<input type=hidden value="3" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="   �y�b�g�ڍ׏�� �@">
</form>
HTM
		}
	}

	if ( $in{riyou} != 4 ) {
		if ( $in{riyou} != 41 ) {
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="4" name="sisetu">
<input type=hidden value="4" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="  �y�b�g�}�ӂɌf�ځ@">
</form>
HTM
		}
	}

	if ( $in{riyou} != 5 ) {
print <<"HTM";
<form method="post" action="./zukan.cgi" target="petzukan">
<input type=hidden value="1" name="syuzoku">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="   �y�b�g�}�Ӊ{�� �@">
</form>
HTM
	}

#VER106 Start �y�b�g�������R�}���h
  if ( $in{riyou} != 61 ) {
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="4" name="sisetu">
<input type=hidden value="6" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="�@ �y�b�g�𓦂��� �@">
</form>
HTM
  }
#VER106END

print "</td><td width=30></td><td>";
}
&townmodori;
	if ( $in{riyou} != 3 ) {
		if ( $in{riyou} != 31 ) {
&pettukitable;
		}
	}
&itemtable;
&hpowari;

exit;
sub chkchk {
	$www = 0;$wwa =0;
	while ( $wwa < 3 ) {
		if ( $petcode[$wwa] ne "" ) { $www ++; }
	$wwa ++;
	}
}

sub syousaipet{
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="4" name="sisetu">
<input type=hidden value="31" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<select name="jouhou">
HTM
open(PET,"$maindir/$foldacha/pet_$in{usrid}$bousi2cha$bousikts");
	while ( $petkai = <PET> ) {
		chop($petkai);
print "<option value=\"$petkai\">$petkai";
	}
close(PET);
print <<"HTM";
</select>
<input type=submit value="�@ �ڍ׏�� �@"><br>
</form>
HTM

}

sub zukanpet{
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="4" name="sisetu">
<input type=hidden value="41" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<select name="jouhou">
HTM
open(PET,"$maindir/$foldacha/pet_$in{usrid}$bousi2cha$bousikts");
	while ( $petkai = <PET> ) {
		chop($petkai);
print "<option value=\"$petkai\">$petkai";
	}
close(PET);
print <<"HTM";
</select>
<input type=submit value="�@ �}�ӂɌf�� �@"><br>
</form>
HTM

}

sub by_character {
	$keisaizumi{$a} <=> $keisaizumi{$b};
}

#VER106 Start �y�b�g�������R�}���h
sub sakujopet {
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="4" name="sisetu">
<input type=hidden value="61" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<select name="jouhou">
HTM
open(PET,"$maindir/$foldacha/pet_$in{usrid}$bousi2cha$bousikts");
  @sakujo = <PET>;
close(PET);
  foreach $a (@sakujo){
		chop($a);
    print "<option value=\"$a\">$a";
  }
print <<"HTM";
</select>
<input type=submit value="�y�b�g�𓦂���"><br>
</form>
HTM
}
#VER106 End

1;