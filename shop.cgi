&topsisetu;

#�@�A�C�e���w������
if ( $in{riyou} eq "1"){
print <<"HTM";
�����������i�����Ă邺�B�ւցB<br>
���������A�C�e����I�����Ă���B<br><br>
HTM
&kounyuu;
} elsif ( $in{riyou} eq "11"){
($itemname,$itemjuuryou,$itemgold,$itemkouka) = split(/\//,$in{itemkai});
	if ( $chagold < $itemgold ) {
print <<"HTM";
�I�C�I�C�A��k�����Ă�������႟���邺�B<br>
��������˃F��B�{�P�Ă񂶂�˂����āB<br><br>
������ďo�����Ă��ȁB
HTM
&shopform;
	} elsif ( $in{itemkai} eq "" ) {
print <<"HTM";
���H�@���𔃂��񂾁H<br>
������Ɣ��������A�C�e����I�����Ă���B<br><br>
��₩���Ȃ�A���Ă��炤���B
HTM
&shopform;
	} else {
			$ddd = 1;
		if ( $itemjuuryou >= 10 && $itemjuuryou <= 49 ) {
			while ( $ddd < 9 ) {
				if ( $chaitem[$ddd] eq $itemname ) {
				last;
				}
				$ddd ++;
			}
			if ( $ddd > 8 ) {
&itemkuuran;
				if ( $ccc > 8 ) {
print <<"HTM";
�������Ă₪�񂾁B<br>
�I���F�A�����������ς�����ˁ[���B<br>
����Ȃ�̂Ă�Ȃ肵�Ă��ȁB
HTM
&shopform;
				
				} else {
$chagold -= $itemgold;
$chaitem[$ccc] = $itemname;
$chaeff[$ccc] = 1;
$chasetumei[$ccc] = $itemkouka;
&charadatawrt;
print <<"HTM";
<font size=4 color=#$mojiiro3><b>$itemname</b></font> ($itemkouka) ���ȁB<br>
���x���肪�Ƃ�B<br>
�܂����������Ă������H<br>
HTM
&kounyuu;
&shopform;
				}
			} elsif ( $chaeff[$ddd] > 998 ) {
print <<"HTM";
���̃A�C�e���͂��łɗe�ʂ����ς��̂悤���ȁB<br>
���������ł���A�C�e���͍ō�999�܂ł������ĂȂ��񂾁B<br>
�o���Ă����Ƃ������B<br>
�܂����������Ă������H<br>
HTM
&kounyuu;
&shopform;
			} else {
$chaeff[$ddd] ++;
$chagold -= $itemgold;
$chasetumei[$ddd] = $itemkouka;
&charadatawrt;
print <<"HTM";
<font size=4 color=#$mojiiro3><b>$itemname</b></font> ($itemkouka) ���ȁB<br>
���𑝂₵�Ă��������B�m�F���ȁB<br>
�܂����������Ă������H
HTM
&kounyuu;
&shopform;
			}

		} elsif ( $itemjuuryou >= 50 ) {
			if ( $itemjuuryou == 50 ) { $itemname = "�|�[�V����"; }
			if ( $itemjuuryou == 51 ) { $itemname = "�n�C�|�[�V����"; }
			if ( $itemjuuryou == 52 ) { $itemname = "�~�h���|�[�V����"; }
			if ( $itemjuuryou == 53 ) { $itemname = "�s�v�c�ȗ�"; }
			if ( $itemjuuryou == 54 ) { $itemname = "�G�N�X�|�[�V����"; }
			if ( $itemjuuryou == 59 ) { $itemname = "���K�G���N�T�["; }
			if ( $itemjuuryou == 60 ) { $itemname = "�M�K�G���N�T�["; }
			if ( $itemjuuryou == 61 ) { $itemname = "�e���G���N�T�["; }
			if ( $itemjuuryou == 62 ) { $itemname = "�^�u���b�g��"; }
			if ( $itemjuuryou == 63 ) { $itemname = "�^�u���b�g��"; }
			if ( $itemjuuryou == 64 ) { $itemname = "�^�u���b�g��"; }

$ddd = 1;
			while ( $ddd < 9 ) {
				if ( $chaitem[$ddd] eq $itemname ) {
				last;
				}
				$ddd ++;
			}
			if ( $ddd > 8 ) {
print <<"HTM";
�c�O�����A�Z�b�g�A�C�e����<br>
�����A�C�e���ɂP�ł������Ă��Ȃ���<br>
�����Ă��˂��񂾁B���܂�B<br>
HTM
&shopform;
			} elsif ( $chaeff[$ddd] > 989 ) {
print <<"HTM";
�����ƁA���Z�b�g�A�C�e���������܂���<br>
�ő�e�ʂ��z�����܂����B<br>
�ő�999�܂ł������Ă˂��񂾁B<br>
�o���Ă����ȁB<br>
HTM
&shopform;
			} else {
$chaeff[$ddd] += 10;
$chagold -= $itemgold;
&charadatawrt;
print <<"HTM";
<font size=4 color=#$mojiiro3><b>$itemname</font></b> ($itemkouka) ���ȁB<br>
�����₵�Ă��������B<br>
�m�F����<br>
�܂����������Ă������H
HTM
&kounyuu;
&shopform;			}

		} else {
&itemkuuran;
			if ( $ccc > 9 ) {
print <<"HTM";
�������Ă₪�񂾁B<br>
�I���F�A�����������ς�����ˁ[���B<br>
����Ȃ�̂Ă�Ȃ肵�Ă��ȁB
HTM
&shopform;
			} else {
$chagold -= $itemgold;
$chaitem[$ccc] = $itemname;
$chaeff[$ccc] = 1;
$chasetumei[$ccc] = $itemkouka;
&charadatawrt;
print <<"HTM";
<font size=4 color=#$mojiiro3><b>$itemname</font></b> ($itemkouka) ���ȁB<br>
���x���肪�Ƃ�B<br>
HTM
&jobdataload;
				if ( $itemjuuryou > $jobweight) {
print <<"HTM";
<br>�����$omosa[$itemjuuryou]����������<br>
���̂��O�̐E�Ƃ��ᑕ���ł��˂����ǂȁB<br>
�������܂�������͂��傤���Ȃ���ȁB<br>
HTM
				}
print <<"HTM";
�܂����������Ă������H
HTM
&kounyuu;
&shopform;
			} 
		}
	}

#�@�A�C�e�����p����
} elsif ( $in{riyou} eq "2"){
print <<"HTM";
�I�[�P�B�B�Ȃ�ł���������Ă�邺�B<br>
���肽�����̂�I�����Ă���B<br>
HTM
&baikyaku;
} elsif ( $in{riyou} eq "21"){
($kainame,$kaigold,$itemnum,$itemkouka) = split(/\//,$in{itemuri});
	if ( $kainame eq "" ) {
print <<"HTM";
���H�@���𔄂�񂾁H<br>
������Ɣ��肽���A�C�e����I�����Ă���B<br><br>
��₩���Ȃ�A���Ă��炤���B
HTM
&shopform;

	} else {
print <<"HTM";
<b><font size=5 color=#$mojiiro2>$kainame</font></b> ($itemkouka)  ���B
<b><font size=5 color=#$mojiiro3>$kaigold</font> G</b> ���ĂƂ����ȁB<br><br>
HTM

		if ( $chaitem[$itemnum] eq $kainame && $chaeff[$itemnum] eq "1" ) {
$chaitem[$itemnum] = $chaeff[$itemnum] = $chasetumei[$itemnum] = "";$chagold += $kaigold;
&charadatawrt;
		} elsif ( $chaitem[$itemnum] eq $kainame && $chaeff[$itemnum] ne "1" ) {
$chaeff[$itemnum] --;$chagold += $kaigold;
&charadatawrt;
		} else { &fuseisyori;exit;
		}
print <<"HTM";
�܂������@��o���������������낵���B<br>
�܂���������ė~�������̂͂��邩�H
HTM
	}
&baikyaku;
&shopform;

#�@�A�C�e���Ӓ菈��
} elsif ( $in{riyou} eq "3"){
print <<"HTM";
���ށB���̖ڂ͊m�������B<br>
�ǂ���Ӓ肵�ė~�����񂾂��H<br>
HTM
&kantei;
&shopform;
} elsif ( $in{riyou} eq "31"){
open(KAI,"$maindir/item$bousikts");
		while ( $kaitori = <KAI> ) {
			($itemname,$itembasyo,$itemjuuryou,$itemga,$itemgold,$itemkouka,$itemstatus[0],$itemti[0],$itemstatus[1],$itemti[1],$itemstatus[2],$itemti[2],$itemstatus[3],$itemti[3],$itemlvl) = split(/,/,$kaitori);
			if ( $chaitem[$in{kantei}] eq $itemname ) {
			last;
			}
		}
close(KAI);
print <<"HTM";
�ӂށB<font size=+1><b>$itemname</b></font>���B<br>
����Ȋ������ȁB<br><br>
<table border=1><tr>
<td>���O</td><td colspan=3><nobr>$itemname</nobr></td></tr>
<tr><td><nobr>����</nobr></td><td><nobr>$bui[$itembasyo]</nobr></td></tr>
<tr><td>���l</td><td><nobr>$itemgold G</nobr></td><td><nobr>����</nobr></td><td><nobr>$itemkouka</nobr></td></tr>
<tr><td colspan=4>�K�v���x�� : <b>$itemlvl</b></td></tr>
</table><br>�܂��Ӓ肵�ė~�������̂͂��邩�H
HTM
&kantei;
&shopform;


} else {
print <<"HTM";
�悤�A<font color=#$chamoji><b>$chaname</font></b> ����Ȃ����B<br>
�悭���Ă��ꂽ�ȁB�ǂ�ȗp�������H<br><br>
HTM
&shopform;
}


&townmodori;
&pettukitable;
&itemtable;
&hpowari;

exit;

sub shopform {
	if ( $in{riyou} ne "" ) {
print "<br>���ɂ��p���͂��邩�H<br>";
	}
	if ( $in{riyou} eq "" || $in{riyou} == 2 || $in{riyou} == 21 || $in{riyou} == 3 || $in{riyou} == 31 ) {
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="3" name="sisetu">
<input type=hidden value="1" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="   �A�C�e���w��   ">
</form>
HTM
	}
	if ( $in{riyou} eq "" || $in{riyou} == 1 || $in{riyou} == 11 || $in{riyou} == 3 || $in{riyou} == 31 ) {
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="3" name="sisetu">
<input type=hidden value="2" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="   �A�C�e�����p   ">
</form>
HTM
	}
	if ( $in{riyou} eq "" || $in{riyou} == 1 || $in{riyou} == 11 || $in{riyou} == 2 || $in{riyou} == 21 ) {
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="3" name="sisetu">
<input type=hidden value="3" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="   �A�C�e���Ӓ�   ">
</form>
HTM
	}
}

sub itemkuuran {
			$ccc = 1;
			while ( $ccc < 9 ) {
				if ( $chaitem[$ccc] eq "" ) {
				last;
				}
				$ccc ++;
}
}
sub kounyuu {
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="3" name="sisetu">
<input type=hidden value="11" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="�@   �w������  �@" ><br>
<select name="itemkai" size=20>
HTM
	open(ITEM,"$maindir/shop$bousikts");
while ( $itemda = <ITEM> ) {
	@itemdaa = split(/,/,$itemda);
	($itemname,$itembasyo,$itemjuuryou,$itemga,$itemgold,$itemkouka,$itemstatus[0],$itemti[0],$itemstatus[1],$itemti[1],$itemstatus[2],$itemti[2],$itemstatus[3],$itemti[3]) = @itemdaa;
print "<option value=\"$itemname/$itemjuuryou/$itemgold/$itemkouka\">$itemgold G:$omosa[$itemjuuryou]/$bui[$itembasyo] �� $itemname �i$itemkouka�j";
	}
close(ITEM);
print <<"HTM";
</select></form></td><td width=30></td><td>
HTM
}

sub baikyaku {

print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="3" name="sisetu">
<input type=hidden value="21" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value=" ���悵�Ă��炤 " ><br>
<select name="itemuri" size=8>
HTM

$bbb = 1;
	while ( $bbb < 9 ) {
	if ( $chaitem[$bbb] ne "" ) {
open(KAI,"$maindir/item$bousikts");
		while ( $kaitori = <KAI> ) {
			($kainame,$a,$b,$c,$kaigold,$itemkouka) = split(/,/,$kaitori);
			if ( $chaitem[$bbb] eq $kainame ) {
			last;
			}
		}
		$kaigold = int($kaigold / 2);
		print "<option value=\"$chaitem[$bbb]/$kaigold/$bbb/$itemkouka\">$kaigold G: $chaitem[$bbb] �i$itemkouka�j";
close(KAI);
	}
		$bbb = $bbb + 1;
	}
print <<"HTM";
</select>
<input type=hidden value="$bbc" name="itemnu">
</form></td><td width=30></td><td>
HTM

}

sub kantei {
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="3" name="sisetu">
<input type=hidden value="31" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<select name="kantei">
HTM
$yyy = 1;
	while ( $yyy < 9 ) {
		if ( $chaitem[$yyy] ne "" ) {
print "<option value=\"$yyy\">$chaitem[$yyy]<br>";
		}
	$yyy ++;
	}
print <<"HTM";
</select>
<input type=submit value="  �Ӓ肵�Ă��炤  ">
</form></td><td width=30></td><td>
HTM

}
1;