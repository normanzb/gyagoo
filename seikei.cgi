


if ( $bankgold eq "" ) { $bankgold = 0 ; }

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

} elsif ( $in{riyou} eq "3"){

#�@�A�C�e����a����

&itemsentaku;
} elsif ( $in{riyou} eq "31"){
open(DASU,"$maindir/$foldamarket/market_data$bousi3cha$bousi2kts");
  @item = <DASU>;
close(DASU);
  $itemsousuu = @item;
	if ( $itemsousuu >= 300 ) {
print <<"HTM";
�u�A�C�e���͂R�O�O�܂ł�������܂���B�v<br>
HTM
        }elsif ( $in{itemde} eq "" ) {
print <<"HTM";
�u�A�C�e�����I������Ă��܂���ł����B�v<br>

HTM
	} elsif ( $chaitem[$in{itemde}] eq "" ) {
&fuseisyori;
	} else {
		if ( $chaeff[$in{itemde}] eq "" ) {
&fuseisyori;
		} elsif ( $chaeff[$in{itemde}] > 1 ) {
$chaeff[$in{itemde}] --;
if (!open(DASU,">>$maindir/$foldamarket/market_data$bousi3cha$bousi2kts")) { &CgiError('�G���[����','�t�@�C���I�[�v���Ɏ��s���܂����B'); }
flock(DASU,2);
	print DASU "$chaitem[$in{itemde}]/$chasetumei[$in{itemde}]\n";
flock(DASU,8);
close(DASU);
$morai += 0.3;
&charadatawrt;
print <<"HTM";

�u�P������t���܂����B���肪�Ƃ��������܂����B�v<br>
HTM
&bankform;
		} else {
if (!open(DASU,">>$maindir/$foldamarket/market_data$bousi3cha$bousi2kts")) { &CgiError('�G���[����','�t�@�C���I�[�v���Ɏ��s���܂����B'); }
flock(DASU,2);
	print DASU "$chaitem[$in{itemde}]/$chasetumei[$in{itemde}]\n";
flock(DASU,8);
close(DASU);
$chaitem[$in{itemde}] = $chaeff[$in{itemde}] = $chasetumei[$in{itemde}] = "";
$morai += 0.4;
&charadatawrt;
print <<"HTM";

�u�m���Ɋ�t���܂����B���肪�Ƃ��������܂����B�v<br>
HTM

&bankform;
		}
	}

} elsif ( $in{riyou} eq "4"){

#�@�A�C�e���������o��

if (!open(DASU,"$maindir/$foldamarket/market_data$bousi3cha$bousi2kts")) { &CgiError('�G���[����','�t�@�C���I�[�v���Ɏ��s���܂����B'); }
	$bchk = <DASU>;
close(DASU);
	if ( $bchk eq "" ) {
int ($morai);
print <<"HTM";
�u�c�O�Ȃ���A�A�C�e���͓����Ă��Ȃ��悤�ł��B�v<br>
HTM
&bankform;
	} else {
print <<"HTM";
�u�ȉ��̃A�C�e�������߂��Ă��܂��B�v<br>
<form method="post" action="./$zonecgi">
<input type=hidden value="14" name="sisetu">
<input type=hidden value="41" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="�@   �Ⴄ  �@" ><br>
<select name="itemds" size=20>
HTM
$abb = 0;
if (!open(MARK,"$maindir/$foldamarket/market_data$bousi3cha$bousi2kts")) { &CgiError('�G���[����','�t�@�C���I�[�v���Ɏ��s���܂����B'); }
		while ( $bankno = <MARK> ) {
		chop($bankno);
	($urimononame,$bankbun) = split(/\//,$bankno);
print "<option value=\"$urimononame/$bankbun/$abb\">$urimononame�i$bankbun�j";
$abb ++;
		}
close(MARK);
print <<"HTM";
</select></form><br>
HTM
	}
} elsif ( $in{riyou} eq "41"){
&itemkuuran;

	if ( $morai < 1 ) {
print <<"HTM";
$chaname��������A�C�e�������o�����Ƃ������A<br>
�w�ォ�璷�V�����ꂽ�B<br><br>
���V�u$chaname�E�E�E�B������Ɨ~���肷���ł͂Ȃ����H�v<br>
$chaname�u�E�E�E�B�v<br><br>
$chaname�͂��Ԃ��ԃA�C�e���𔠂̒��ɖ߂��A���̏�𗧂����鎖�ɂ����B
HTM


	} elsif ( $ccb eq "0" ) {
print <<"HTM";
�u�������������ς��Ŏ��Ă܂���B�v<br>
HTM



	} else {
	($urimononame,$bankbun,$aba) = split(/\//,$in{itemds});
open(MARK,"$maindir/$foldamarket/market_data$bousi3cha$bousi2kts");
		@banban = <MARK>;
close(MARK);

$abd = 0;
open(BANN,">$maindir/$foldamarket/$in{usrid}.tmp");
flock(BANN,2);
		foreach $a (@banban) {
			($kk,$ll) = split(/\//,$a);
#VER106 Start �A�C�e�������o�O�C��
#			if ( $abd eq $aba && $urimononame eq $kk ) {
			if ( $abd eq $aba && $urimononame eq $kk && $puchk != 1) {
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

rename("$maindir/$foldamarket/$in{usrid}.tmp","$maindir/$foldamarket/market_data$bousi3cha$bousi2kts");

	if($chastats[2] > 12){
			$ccc = 1;$ccb = 0;
			while ( $ccc < 10 ) {
				if ( $chaitem[$ccc] eq $urimononame ) {
					$cce = $ccc;$ccd = 1;last;
				} 
				$ccc ++;
			}
			$ccc = 1;
	} elsif ($chastats[2] > 17){
			$ccc = 1;$ccb = 0;
			while ( $ccc < 11 ) {
				if ( $chaitem[$ccc] eq $urimononame ) {
					$cce = $ccc;$ccd = 1;last;
				} 
				$ccc ++;
			}
			$ccc = 1;
	} elsif ($chastats[2] > 19){
			$ccc = 1;$ccb = 0;
			while ( $ccc < 12 ) {
				if ( $chaitem[$ccc] eq $urimononame ) {
					$cce = $ccc;$ccd = 1;last;
				} 
				$ccc ++;
			}
			$ccc = 1;
	} elsif ($chastats[2] > 21){
			$ccc = 1;$ccb = 0;
			while ( $ccc < 12 ) {
				if ( $chaitem[$ccc] eq $urimononame ) {
					$cce = $ccc;$ccd = 1;last;
				} 
				$ccc ++;
			}
			$ccc = 1;
	} else {
			$ccc = 1;$ccb = 0;
			while ( $ccc < 9 ) {
				if ( $chaitem[$ccc] eq $urimononame ) {
					$cce = $ccc;$ccd = 1;last;
				} 
				$ccc ++;
			}
			$ccc = 1;
	}




			while ( $ccc < 9 ) {
				if ( $chaitem[$ccc] eq "" ) {
				$ccb = $ccc;last;
				}
				$ccc ++;
	}


		if ( $ccd == 1 ) {
$chaeff[$cce] ++;
$morai --;
		} else {
$chaitem[$ccb] = $urimononame;$chaeff[$ccb] = 1;$chasetumei[$ccb] = $bankbun;
		}
&charadatawrt;
print <<"HTM";
�u$urimononame��Ⴂ�܂����B�v<br>
HTM

&bankform;

	}
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
				$chastats[$itemstatus[$eaa]] += $itemti[$eaa];
				}
		$eaa ++;
			}
			if ( $kariname ne "" ) {
	$eaq = 0;
				while ( $eaq < 4 ) {
					if ( $soubstatus[$eaq] eq "" ) { last; } else {
					$chastats[$soubstatus[$eaq]] -= $soubti[$eaq];
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

#�@��s�R�}���h�ꗗ

print <<"HTM";
�u���T�C�N���{�b�N�X�v<br>
HTM
&bankform;
}


&townmodori;
&pettukitable;
&itemtable;
&hpowari;

exit;

sub bankform {


if ( $bankgold ne "0" ) {
print <<"HTM";
<nobr><form method="post" action="./$zonecgi">
<input type=hidden value="14" name="sisetu">
<input type=hidden value="2" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="  �a���������o��  ">
<input type=text value="$bankgold" name="okane" size=7 maxlength=18>G
</form></nobr>
HTM
}
print <<"HTM";
<nobr>
<form method="post" action="./$zonecgi">
<input type=hidden value="14" name="sisetu">
<input type=hidden value="4" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="�{�b�N�X�̒��g������">
</form>
<form method="post" action="./$zonecgi">
<input type=hidden value="14" name="sisetu">
<input type=hidden value="3" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value=" �A�C�e������t���� ">
</form>
HTM
}





sub bankwrt {
open(MARK,">$maindir/$foldamarket/market_data$bousi2cha$bousikts");
	print MARK "$bankgold";
close(MARK);
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
sub itemsentaku {
&itemkuuran;
	if ( $ccb eq 12 ) {
print <<"HTM";
�u�A�C�e���������Ă��܂���B�v<br>
HTM

	} else {
		if ( $in{riyou} eq "3" ) {
$comme = "��t����";
$riyo = "31";
		} elsif ( $in{riyou} eq "7" ) {
$comme = "�̂Ă�";
$riyo = "71";
		}
print <<"HTM";
�u��t����A�C�e����I�����Ă��������B�v<br>
<form method="post" action="./$zonecgi">
<input type=hidden value="14" name="sisetu">
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