open(BANK,"$maindir/$foldacha/bankg_$in{usrid}$bousi2cha$bousikts");
	$bankgold = <BANK>;
close(BANK);
if ( $bankgold eq "" ) { $bankgold = 0 ; }

open(HUKU,"$maindir/$foldacha/hukubiki_$in{usrid}$bousi2cha$bousikts");
	$bankhukubiki = <HUKU>;
close(HUKU);
if ( $bankhukubiki eq "" ) { $bankhukubiki = 0 ; }
&topsisetu;

if ( $in{riyou} eq "1"){

#�@������a����

#VER106 Start ���K�\��
#$in{okane} = int($in{okane});
	if ( $in{okane} =~ /^[0-9]+$/ ) {
#VER106 End

if ( $in{okane} < 0 ) {
	&fuseisyori;
} else {
	if ( $chagold < 1 ) {
print <<"HTM";
�u�V���W�L���@�K�@�A���}�Z���v<br>
HTM

	} else {
		if( $chagold < $in{okane} ) {
		$in{okane} = $chagold;
		} 
$bankgold += $in{okane};
$chagold -= $in{okane};
&charadatawrt;
&bankwrt;
print <<"HTM";
�u�^�V�J�@�j�@�I�A�Y�J���@�V�}�V�^�v<br>
HTM
&bankform;
	}
}

#VER106 Start ���K�\��
	} else {
		&fuseisyori;
	}
#VER106 End

} elsif ( $in{riyou} eq "2"){

#�@�����������o��

#VER106 Start ���K�\��
#$in{okane} = int($in{okane});
	if ( $in{okane} =~ /^[0-9]+$/ ) {
#VER106 End
if ( $in{okane} < 0 ) {
	&fuseisyori;
} else {
$in{okane} = int($in{okane});
	if ( $bankgold < 1 ) {
print <<"HTM";
�u���L���@�n�@�A���}�Z���v<br>
HTM



	} else {
		if( $bankgold < $in{okane} ) {
		$in{okane} = $bankgold;
		} 

$bankgold -= $in{okane};
$chagold += $in{okane};
	if ( $chagold > 1000000000 ) {
$chagold = 999999999;
}
&charadatawrt;
&bankwrt;
print <<"HTM";
�u�I�q�L�_�V�@�C�^�V�}�V�^�v<br>
HTM
&bankform;
	}
}

#VER106 Start ���K�\��
	} else {
		&fuseisyori;
	}
#VER106 End

















} elsif ( $in{riyou} eq "11"){
#�@��������a����

#VER106 Start ���K�\��
#$in{hukubiki} = int($in{hukubiki});
	if ( $in{hukubiki} =~ /^[0-9]+$/ ) {
#VER106 End

if ( $in{hukubiki} < 0 ) {
	&fuseisyori;
} else {
	if ( $hukubiki < 1 ) {
print <<"HTM";
�u�P�}�C�@���@���b�e�C�}�Z���v<br>
HTM

	} else {
		if( $hukubiki < $in{hukubiki} ) {
		$in{hukubiki} = $hukubiki;
		} 
$bankhukubiki += $in{hukubiki};
$hukubiki -= $in{hukubiki};
&charadatawrt;
&bankwrt2;
print <<"HTM";
�u�^�V�J�@�j�@�I�A�Y�J���@�V�}�V�^�v<br>
HTM
&bankform;
	}
}

#VER106 Start ���K�\��
	} else {
		&fuseisyori;
	}
#VER106 End

} elsif ( $in{riyou} eq "12"){

#�@�������������o��

#VER106 Start ���K�\��
#$in{hukubiki} = int($in{hukubiki});
	if ( $in{hukubiki} =~ /^[0-9]+$/ ) {
#VER106 End
if ( $in{hukubiki} < 0 ) {
	&fuseisyori;
} else {
$in{hukubiki} = int($in{hukubiki});
	if ( $bankhukubiki < 1 ) {
print <<"HTM";
�u�P�}�C�@���@�A�Y�J�b�e�@�C�}�Z���v<br>
HTM



	} else {
		if( $bankhukubiki < $in{hukubiki} ) {
		$in{hukubiki} = $bankhukubiki;
		} 

$bankhukubiki -= $in{hukubiki};
$hukubiki += $in{hukubiki};
	if ( $hukubiki > 1000000000 ) {
$chastats[14] = 999999999;
}
&charadatawrt;
&bankwrt2;
print <<"HTM";
�u�I�q�L�_�V�@�C�^�V�}�V�^�v<br>
HTM
&bankform;
	}
}

#VER106 Start ���K�\��
	} else {
		&fuseisyori;
	}
#VER106 End





} elsif ( $in{riyou} eq "3"){

#�@�A�C�e����a����

&itemsentaku;
} elsif ( $in{riyou} eq "31"){

open(BANKI,"$maindir/$foldacha/bankit_$in{usrid}$bousi2cha$bousikts");
  @item = <BANKI>;
close(BANKI);
  $itemsousuu = @item;
	if ( $itemsousuu >= 100 ) {
print <<"HTM";
�u�A�C�e���@�n�@�P�O�O�R�@�}�f�V�J<br>
�@�@�I�A�Y�J���@�f�L�}�Z���B�v<br>
HTM
        }elsif ( $in{itemde} eq "" ) {
print <<"HTM";
�u�A�C�e���@�K�@�Z���^�N<br>
�@�@�T���e�@�C�}�Z���@�f�V�^�v<br>
HTM
	} elsif ( $chaitem[$in{itemde}] eq "" ) {
&fuseisyori;
	} else {
		if ( $chaeff[$in{itemde}] eq "" ) {
&fuseisyori;
		} elsif ( $chaeff[$in{itemde}] > 1 ) {
$chaeff[$in{itemde}] --;
if (!open(BANKI,">>$maindir/$foldacha/bankit_$in{usrid}$bousi2cha$bousikts")) { &CgiError('�G���[����','�t�@�C���I�[�v���Ɏ��s���܂����B'); }
flock(BANKI,2);
	print BANKI "$chaitem[$in{itemde}]/$chasetumei[$in{itemde}]\n";
flock(BANKI,8);
close(BANKI);
&charadatawrt;
print <<"HTM";
�u�P�R�@�_�P�@�I�A�Y�J���@�V�}�V�^�v<br>
HTM
&bankform;
		} else {
if (!open(BANKI,">>$maindir/$foldacha/bankit_$in{usrid}$bousi2cha$bousikts")) { &CgiError('�G���[����','�t�@�C���I�[�v���Ɏ��s���܂����B'); }
flock(BANKI,2);
	print BANKI "$chaitem[$in{itemde}]/$chasetumei[$in{itemde}]\n";
flock(BANKI,8);
close(BANKI);
$chaitem[$in{itemde}] = $chaeff[$in{itemde}] = $chasetumei[$in{itemde}] = "";
&charadatawrt;
print <<"HTM";
�u�I�A�Y�J���@�V�}�V�^�v<br>
HTM
&bankform;
		}
}

} elsif ( $in{riyou} eq "4"){

#�@�A�C�e���������o��

if (!open(BANKI,"$maindir/$foldacha/bankit_$in{usrid}$bousi2cha$bousikts")) { &CgiError('�G���[����','�t�@�C���I�[�v���Ɏ��s���܂����B'); }
	$bchk = <BANKI>;
close(BANKI);
	if ( $bchk eq "" ) {
print <<"HTM";
�u�Q���U�C�@�I�A�Y�J���@�V�e�C��<br>
�@�@�@�@�A�C�e���@�n�@�S�U�C�}�Z���v<br>
HTM
&bankform;
	} else {
print <<"HTM";
�u�A�C�e���@���@�Z���^�N�@�V�e�N�_�T�C�v<br>
<form method="post" action="./$zonecgi">
<input type=hidden value="1" name="sisetu">
<input type=hidden value="41" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="�@   �����o��  �@" ><br>
<select name="itemds" size=10>
HTM
$abb = 0;
if (!open(BANKI,"$maindir/$foldacha/bankit_$in{usrid}$bousi2cha$bousikts")) { &CgiError('�G���[����','�t�@�C���I�[�v���Ɏ��s���܂����B'); }
		while ( $bankno = <BANKI> ) {
		chop($bankno);
	($bankname,$bankbun) = split(/\//,$bankno);
print "<option value=\"$bankname/$bankbun/$abb\">$bankname�i$bankbun�j";
$abb ++;
		}
close(BANKI);
print <<"HTM";
</select></form><br>
HTM
	}
} elsif ( $in{riyou} eq "41"){
&itemkuuran;
	if ( $ccb eq "0" ) {
print <<"HTM";
�u�A�C�e���@�K�@�C�b�p�C�@�f�X�v<br>
HTM

	} else {
	($bankname,$bankbun,$aba) = split(/\//,$in{itemds});
open(BANKI,"$maindir/$foldacha/bankit_$in{usrid}$bousi2cha$bousikts");
		@banban = <BANKI>;
close(BANKI);

$abd = 0;
open(BANN,">$maindir/$foldacha/$in{usrid}.tmp");
flock(BANN,2);
		foreach $a (@banban) {
			($kk,$ll) = split(/\//,$a);
#VER106 Start �A�C�e�������o�O�C��
#			if ( $abd eq $aba && $bankname eq $kk ) {
			if ( $abd eq $aba && $bankname eq $kk && $puchk != 1) {
#VER106 End
				$puchk = 1;
			} else {
				print BANN "$a";
			} 
			$abd ++;
		}
flock(BANN,8);
close(BANN);

if ( $puchk ne "1" ) { &fuseisyori;exit;}

rename("$maindir/$foldacha/$in{usrid}.tmp","$maindir/$foldacha/bankit_$in{usrid}$bousi2cha$bousikts");

			$ccc = 1;$ccb = 0;
			while ( $ccc < 9 ) {
				if ( $chaitem[$ccc] eq $bankname ) {
					$cce = $ccc;$ccd = 1;last;
				} 
				$ccc ++;
			}
			$ccc = 1;
			while ( $ccc < 9 ) {
				if ( $chaitem[$ccc] eq "" ) {
				$ccb = $ccc;last;
				}
				$ccc ++;
			}
		if ( $ccd == 1 ) {
$chaeff[$cce] ++;
		} else {
$chaitem[$ccb] = $bankname;$chaeff[$ccb] = 1;$chasetumei[$ccb] = $bankbun;
		}
&charadatawrt;
print <<"HTM";
�u�I�q�L�_�V�@�C�^�V�}�V�^�v<br>
HTM


	}
&bankform;
} elsif ( $in{riyou} eq "5"){

#�@�񕜃A�C�e�����g�p����

			$ccc = 1;$cbc = 0;
			while ( $ccc < 9 ) {
				if ( $chaitem[$ccc] ne "" ) {
				$cbc ++;
				}
				$ccc ++;
			}
	if ( $cbc == 0 ) {
print <<"HTM";
�u�V���E�@�f�L���@�A�C�e���@�K�@�A���}�Z���v<br>
&bankform;
HTM
	} else {
			$ccc = 1;$cba = 0;
			while ( $ccc < 9 ) {
				if ( $chaitem[$ccc] ne "" ) {
open(KAI,"$maindir/item$bousikts");
		while ( $kaitori = <KAI> ) {
			($kainame,$a,$a,$a,$a,$a,$itemstats,$itemstats2) = split(/,/,$kaitori);
			if ( $chaitem[$ccc] eq $kainame && $itemstats == 10) {
				push(@itemsuuji,$ccc);
				push(@itemkouka,$itemstats2);
				$cba ++;
			}
		}
close(KAI);
				}
$ccc ++;
			}
		if( $cba == 0 ) {
print <<"HTM";
�u�V���E�@�f�L���@�A�C�e���@�K�@�A���}�Z���v<br>
HTM
&bankform;
		} else {
print <<"HTM";
�u�A�C�e���@���@�Z���^�N�@�V�e�N�_�T�C�v<br>
<form method="post" action="./$zonecgi">
<input type=hidden value="1" name="sisetu">
<input type=hidden value="51" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="�@   �g�p����  �@" ><br>
<select name="itemds" size=5>
HTM
$add = 0;
			foreach $atai (@itemsuuji) {
		print "<option value=\"$chaitem[$atai]/$atai/$itemkouka[$add]\">$chaitem[$atai] �i$chasetumei[$atai]�j";
$add ++;
			}
print <<"HTM";
</select></form><br>
HTM
		}
	}

} elsif ( $in{riyou} eq "51"){
($itemname,$itemnum,$itemstats) = split(/\//,$in{itemds});
	if ( $itemname ne $chaitem[$itemnum] ) {
		&CgiError('�G���[����','�s���������^��������܂��B');
	} elsif ( $chahp == $chastats[9] ) {
print <<"HTM";
�u�A�i�^�@�n�@�\\���@���@�V���E<br>
�@�@�V�e���@�C�~�@�K�@�A���}�Z���v<br>
HTM
&bankform;
	} else {
$chahp += $itemstats;
		if ( $chahp > $chastats[9] ) {
			$chahp = $chastats[9];
		}
		if ( $chaeff[$itemnum] == 1 ) {
$chaitem[$itemnum] = $chaeff[$itemnum] = $chasetumei[$itemnum] = "";
		} else {
$chaeff[$itemnum] --;
		}

&charadatawrt;
print <<"HTM";
�u�A�C�e���@���@�V���E�@�V�}�V�^�v<br>
HTM
&bankform;
	}
} elsif ( $in{riyou} eq "6"){

#�@����h��̑���

&itemkuuran;
	if ( $ccb == 9 ) {
print <<"HTM";
�u�\\�E�r�@�f�L���@�A�C�e���@�K�@�A���}�Z���v<br>
HTM
&bankform;
	} else {
&jobdataload;

	$bbb = 1;$bbc =0;
		while ( $bbb < 9 ) {
open(KAI,"$maindir/item$bousikts");
			while ( $kaitori = <KAI> ) {
				($itemname,$itembasyo,$itemjuuryou,$itemgazou,$itemgold,$itemkouka) = split(/,/,$kaitori);
				if ( $chaitem[$bbb] eq $itemname ) {
					if ( $itemjuuryou <= $jobweight && itemkouka <= 10 ) {
					push(@itemnum,$bbb);push(@itemdoko,$bui[$itembasyo]);
					push(@itemomosa,$omosa[$itemjuuryou]);push(@itemstats,$itemkouka);$bbc ++;
					}
last;
				}
			}
close(KAI);
$bbb ++;
		}


		if ( $bbc == 0 ) {
print <<"HTM";
�u�\\�E�r�@�f�L���@�A�C�e���@�K�@�A���}�Z���v<br>
HTM
&bankform;
		} else {
print <<"HTM";
�u�A�C�e���@���@�Z���^�N�@�V�e�N�_�T�C�v<br>
<form method="post" action="./$zonecgi">
<input type=hidden value="1" name="sisetu">
<input type=hidden value="61" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="�@    ��������   �@" ><br>
<select name="itemde" size=6>
HTM
	$bbb = 0;
			foreach $num (@itemnum) {
print "<option value=\"$chaitem[$num]/$num\">$itemomosa[$bbb]/$itemdoko[$bbb]/ $chaitem[$num]�i$itemstats[$bbb]�j";
$bbb ++;
			}
print <<"HTM";
</select></form><br>
HTM
		}
	}
} elsif ( $in{riyou} eq "61"){
		($soubiname,$numa) = split(/\//,$in{itemde});
	if ( $in{itemde} eq "" ) {
print <<"HTM";
�u�A�C�e���@�K�@�Z���^�N�@�T���e�C�}�Z���v<br>
HTM
&bankform;

	} elsif ( $chaitem[$numa] ne $soubiname) {
		&CgiError('�G���[����','�s���������^��������܂��I');
	} else {
&jobdataload;

if (!open(BAN,"$maindir/item$bousikts")) { &CgiError('�G���[����','�t�@�C���ǂݍ��݂Ɏ��s���܂����B'); }
			while ( $soubidayo = <BAN>) {
		($itemname,$itembasyo,$itemjuuryou,$itemga,$itemgold,$itemkouka,$itemstatus[0],$itemti[0],$itemstatus[1],$itemti[1],$itemstatus[2],$itemti[2],$itemstatus[3],$itemti[3],$itemlvl) = split(/,/,$soubidayo);
				if ( $itemname eq $chaitem[$numa] ) {
					last;
				}
			}
close(BAN);

		if ( $itemjuuryou > $jobweight ) {
&CgiError('�G���[����','�s���������^��������܂��I');
		} elsif ( $itemlvl > $chalvl ) {
print <<"HTM";
�u���x���@�K�@�^���}�Z���v<br>
HTM
&bankform;
		} else {
if (!open(BAN,"$maindir/item$bousikts")) { &CgiError('�G���[����','�t�@�C���ǂݍ��݂Ɏ��s���܂����B'); }
			while ( $soubido = <BAN>) {
		($soubname,$soubbasyo,$soubjuuryou,$soubga,$soubgold,$soubkouka,$soubstatus[0],$soubti[0],$soubstatus[1],$soubti[1],$soubstatus[2],$soubti[2],$soubstatus[3],$soubti[3]) = split(/,/,$soubido);
				if ( $soubname eq $chasoubi[$itembasyo] ) {
					last;
				}
			}
close(BAN);

$kariname = $chasoubi[$itembasyo];$karisetumei = $chabun[$itembasyo];
$chasoubi[$itembasyo] = $chaitem[$numa];$chabun[$itembasyo] = $chasetumei[$numa];$chabougue[$itembasyo] = $itemga;

	$eaa = 0;
			while ( $eaa < 4 ) {
				if ( $itemstatus[$eaa] eq "" ) { last; } else {

				$karistats[$itemstatus[$eaa]] += $itemti[$eaa];

				}
		$eaa ++;
			}
			if ( $kariname ne "" ) {
	$eaq = 0;
				while ( $eaq < 4 ) {
					if ( $soubstatus[$eaq] eq "" ) { last; } else {
					$karistats[$soubstatus[$eaq]] -= $soubti[$eaq];


					}
		$eaq ++;
				}
			}
$chaitem[$numa] = $kariname;$chasetumei[$numa] = $karisetumei;
			if ( $chaitem[$numa] eq "" ) { $chaeff[$numa] ="";} else {$chaeff[$numa] = 1;}
&charadatawrt;
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
�u<font size=4 color=#$mojiiro2><b>$chasoubi[$itembasyo] </font>($chabun[$itembasyo]) ��</b><br>
   �\\�E�r�@�V�}�V�^�v<br>
HTM
&bankform;
		}
	}







} elsif ( $in{riyou} eq "7"){

#�@�����A�C�e�����̂Ă�

&itemsentaku;
} elsif ( $in{riyou} eq "71"){
print <<"HTM";
�u<font size=4 color=#$mojiiro2><b>$chaitem[$in{itemde}]</font> ($chasetumei[$in{itemde}])</b>�@���@�X�e�}�V�^�v<br>
HTM
$chaitem[$in{itemde}] = $chaeff[$in{itemde}] = $chasetumei[$in{itemde}] = "";
&charadatawrt;
&bankform;
} else {
$bankgold = &put_comma($bankgold);
#�@��s�R�}���h�ꗗ

print <<"HTM";
�u�C���b�V���C�}�Z  <b>$chaname</b>  �T�}�v<br>
HTM
&bankform;
}


&townmodori;
&pettukitable;
&itemtable;
&hpowari;

exit;

sub bankform {
print <<"HTM";
<center><br><table border=1>
<tr><td><table border=0>
<tr><td><nobr>�a���F</nobr></td><td width=70 align=right><nobr><font color=#$chamoji><b>$bankgold</font> G</b></nobr></td></tr></table></td></tr></table>
�@�@�@�@<font size=1>�i���z�͔��p�����œ��́j</font><br>
</center>
<nobr><form method="post" action="./$zonecgi">
<input type=hidden value="1" name="sisetu">
<input type=hidden value="1" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="   ��������a����  ">
<input type=text value="$chagold" name="okane" size=7 maxlength=18>G
</form></nobr>
HTM

if ( $bankgold ne "0" ) {
print <<"HTM";
<nobr><form method="post" action="./$zonecgi">
<input type=hidden value="1" name="sisetu">
<input type=hidden value="2" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="  �a���������o��  ">
<input type=text value="" name="okane" size=7 maxlength=18>G
</form></nobr>
HTM
}
print <<"HTM";
<nobr>
<form method="post" action="./$zonecgi">
<input type=hidden value="1" name="sisetu">
<input type=hidden value="3" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="  �A�C�e����a����  ">
</form>
<form method="post" action="./$zonecgi">
<input type=hidden value="1" name="sisetu">
<input type=hidden value="4" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value=" �A�C�e���������o��">
</form></td><td width=30></td><td>
<center><br><table border=1>
<tr><td><table border=0>
<tr><td><nobr>�������F</nobr></td><td width=70 align=right><nobr><font color=#$chamoji><b>$bankhukubiki</font> ��</b></nobr></td></tr></table></td></tr></table>
�@�@�@�@<font size=1>�i�����͔��p�����œ��́j</font><br>
</center>
<nobr><form method="post" action="./$zonecgi">
<input type=hidden value="1" name="sisetu">
<input type=hidden value="11" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="  ��������a���� ">
<input type=text value="$hukubiki" name="hukubiki" size=3 maxlength=18>��
</form></nobr>
HTM
if ( $bankhukubiki ne "0" ) {
print <<"HTM";
<nobr><form method="post" action="./$zonecgi">
<input type=hidden value="1" name="sisetu">
<input type=hidden value="12" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="�������������o��">
<input type=text value="$bankhukubiki" name="hukubiki" size=3 maxlength=18>��
</form></nobr>
HTM
}

print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="1" name="sisetu">
<input type=hidden value="6" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="�A�C�e���𑕔�����">
</form>
<form method="post" action="./$zonecgi">
<input type=hidden value="1" name="sisetu">
<input type=hidden value="7" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value=" �A�C�e�����̂Ă� ">
</form>
HTM
}












sub bankwrt {
open(BANK,">$maindir/$foldacha/bankg_$in{usrid}$bousi2cha$bousikts");
	print BANK "$bankgold";
close(BANK);
}

sub bankwrt2 {
open(HUKU,">$maindir/$foldacha/hukubiki_$in{usrid}$bousi2cha$bousikts");
	print HUKU "$bankhukubiki";
close(HUKU);
}


sub itemsagasi {
			$ccc = 1;
			while ( $ccc < 9 ) {
				if ( $chaitem[$ccc] ne "" ) {
				print "<option value=\"$ccc\">$chaitem[$ccc] ($chasetumei[$ccc])";
				}
				$ccc ++;
			}
print <<"HTM";
</select></form><br>
HTM
}

sub itemkuuran {
			$ccc = 1;$ccb = 0;
			while ( $ccc < 9 ) {
				if ( $chaitem[$ccc] eq "" ) {
				$ccb ++;
				}
				$ccc ++;
			}

}
sub put_comma {
  my $num = $_[0];
  $num = reverse $num;
  $num =~ s/(\d{3})(?=\d)(?!\d*\.)/$1,/g;
  $num = reverse $num;
  return $num
}
sub itemsentaku {
&itemkuuran;
	if ( $ccb eq 8 ) {
print <<"HTM";
�u�A�C�e���@�K�@�A���}�Z���v<br>
HTM

	} else {
		if ( $in{riyou} eq "3" ) {
$comme = "�a����";
$riyo = "31";
		} elsif ( $in{riyou} eq "7" ) {
$comme = "�̂Ă�";
$riyo = "71";
		}
print <<"HTM";
�u�A�C�e���@���@�Z���^�N�@�V�e�N�_�T�C�v<br>
<form method="post" action="./$zonecgi">
<input type=hidden value="1" name="sisetu">
<input type=hidden value="$riyo" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="�@    $comme   �@" ><br>
<select name="itemde" size=6>
HTM
&itemsagasi;
	}

}

1;