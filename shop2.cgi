&topsisetu;

#�@�A�C�e���w������
if ( $in{riyou} eq "1"){
print <<"HTM";
���ƕϊ�����񂾂��H<br>
<b>CP</b>�͋M�d�Ȃ��̂�����悭�l���Ďg���񂾂�B<br>
�q�b�q�b�q�B<br><br>
HTM
&kounyuu;
} elsif ( $in{riyou} eq "11"){
($itemname,$itemjuuryou,$itemgold,$itemkouka) = split(/\//,$in{itemkai});
	if ( $chastats[14] < $itemgold ) {
print <<"HTM";
���₨��A<b>CP</b>������Ȃ��悤����B<br>
���ꂪ�~�����Ȃ�A�����ƌo����ς�ł��痈��Ƃ悩�낤�B<br><br>
�q�b�q�B
HTM
&shopform;
	} elsif ( $in{itemkai} eq "" ) {
print <<"HTM";
���H�@�ǂ�ƕϊ��������񂾂��H<br>
������ƕϊ��������A�C�e����I�����Ȃ����B<br><br>
�q�b�q�b�q�B
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
�ӂށB<br>
�c�O���Ⴊ�A���O�͂���ȏ㕨�����ĂȂ��悤����̂��B<br>
�ו��𐮗����Ă���܂�����Ƃ悩�낤�B
HTM
&shopform;
				
				} else {
$chastats[14] -= $itemgold;
$chaitem[$ccc] = $itemname;
$chaeff[$ccc] = 1;
$chasetumei[$ccc] = $itemkouka;
&charadatawrt;
print <<"HTM";
<font size=4 color=#$mojiiro3><b>$itemname</b></font> ($itemkouka)  �ł����񂾂ˁB<br>
<b><font color=red>�A�C���`�`�`�b�I�I</b></font><br>
�ӂ��A�ł�����������B�����Ă������B
HTM
&kounyuu;
&shopform;
				}
			} elsif ( $chaeff[$ddd] > 998 ) {
print <<"HTM";
���̃A�C�e���͂��łɗe�ʂ����ς��̂悤����B<br>
���������ł���A�C�e���͍ō�999�܂ł������ĂȂ��̂���B<br>
�o���Ă����Ƃ������B<br>
���ɉ����������ė~�������͂��邩���H<br>
HTM
&kounyuu;
&shopform;
			} else {
$chaeff[$ddd] ++;
$chastats[14] -= $itemgold;
$chasetumei[$ddd] = $itemkouka;
&charadatawrt;
print <<"HTM";
<font size=4 color=#$mojiiro3><b>$itemname</b></font> ($itemkouka) ����ȁB<br>
�����₵�Ă���������B<br>
�܂��ϊ����镨�͂���̂����H
HTM
&kounyuu;
&shopform;
			}

		} elsif ( $itemjuuryou >= 50 ) {
			if ( $itemjuuryou == 50 ) { $itemname = "�|�[�V����"; }
			if ( $itemjuuryou == 51 ) { $itemname = "�n�C�|�[�V����"; }
			if ( $itemjuuryou == 52 ) { $itemname = "�~�h���|�[�V����"; }
			if ( $itemjuuryou == 53 ) { $itemname = "�G�N�X�|�[�V����"; }
			if ( $itemjuuryou == 54 ) { $itemname = "�G���N�T�["; }
			if ( $itemjuuryou == 55 ) { $itemname = "�s�v�c�ȗ�"; }
			if ( $itemjuuryou == 56 ) { $itemname = "�n�C�G���N�T�["; }
			if ( $itemjuuryou == 57 ) { $itemname = "���X�g�G���N�T�["; }
			if ( $itemjuuryou == 58 ) { $itemname = "�X�[�p�[�G���N�T�["; }
			if ( $itemjuuryou == 59 ) { $itemname = "���K�G���N�T�["; }
			if ( $itemjuuryou == 60 ) { $itemname = "�M�K�G���N�T�["; }
			if ( $itemjuuryou == 61 ) { $itemname = "�e���G���N�T�["; }
			if ( $itemjuuryou == 62 ) { $itemname = "�_��"; }
$ddd = 1;
			while ( $ddd < 9 ) {
				if ( $chaitem[$ddd] eq $itemname ) {
				last;
				}
				$ddd ++;
			}
			if ( $ddd > 8 ) {
print <<"HTM";
�c�O���Ⴊ�A�Z�b�g�A�C�e����<br>
�����A�C�e���ɂP�ł������Ă��Ȃ���<br>
�������邱�Ƃ͂ł���̂���B���܂�̂��B<br>
HTM
&shopform;
			} elsif ( $chaeff[$ddd] > 998 ) {
print <<"HTM";
����A�~���肾�˂��B<br>
���̃A�C�e���́A�����\��������قǎ����Ă邶��낤�B<br>
������x�Ȃ��Ȃ����琶�����Ă�낤�����̂��B�q�q�B<br>
HTM
&shopform;
			} else {
$chaeff[$ddd] += 10;
$chastats[14] -= $itemgold;
&charadatawrt;
print <<"HTM";
<font size=4 color=#$mojiiro3><b>$itemname</font></b> ($itemkouka) ����ȁB<br>
�����₵�Ă���������B<br>
�܂��ϊ����镨�͂���̂����H
HTM
&kounyuu;
&shopform;			}

		} else {
&itemkuuran;
			if ( $ccc > 8 ) {
print <<"HTM";
�ӂށB<br>
�c�O���Ⴊ�A���O�͂���ȏ㕨�����ĂȂ��悤����̂��B<br>
�ו��𐮗����Ă���܂�����Ƃ悩�낤�B
HTM
&shopform;
			} else {
$chastats[14] -= $itemgold;
$chaitem[$ccc] = $itemname;
$chaeff[$ccc] = 1;
$chasetumei[$ccc] = $itemkouka;
&charadatawrt;
print <<"HTM";
<font size=4 color=#$mojiiro3><b>$itemname</font></b> ($itemkouka) �ł����񂾂ˁB<br>
<b><font color=red>�A�C���`�`�`�b�I�I</b></font><br>
�ӂ��A�ł�����������B�����Ă������B
HTM
&jobdataload;
				if ( $itemjuuryou > $jobweight) {
print <<"HTM";
<br>����A�����$omosa[$itemjuuryou]�������Ⴉ��<br>
���̂��񂽂̐E�Ƃ��ᑕ���ł��񂼂��B<br>
�܂��A�������Ă��܂������͎d���Ȃ��ˁB<br>
<br>
HTM
				}
print <<"HTM";
�܂��ϊ�����̂����H�q�b�q�B
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
<tr><td><nobr>����</nobr></td><td><nobr>$bui[$itembasyo]</nobr></td><td>�d��</td><td>$omosa[$itemjuuryou]</td></tr>
<tr><td>���l</td><td><nobr>$itemgold G</nobr></td><td><nobr>����</nobr></td><td><nobr>$itemkouka</nobr></td></tr>
<tr><td colspan=4>�K�v���x�� : <b>$itemlvl</b></td></tr>
</table><br>�܂��Ӓ肵�ė~�������̂͂��邩�H
HTM
&kantei;
&shopform;


} else {
print <<"HTM";
��������Ⴂ�A�悭�����˂��B<br>
�����ŁA<b>CP</b>���A�C�e���ɕϊ����鎖���o�����B<br>
�q�b�q�b�q�B<br><br>
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

	}
	if ( $in{riyou} eq "" || $in{riyou} == 2 || $in{riyou} == 21 || $in{riyou} == 3 || $in{riyou} == 31 ) {
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="11" name="sisetu">
<input type=hidden value="1" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="   �i��������   ">
</form>
HTM
	}
	if ( $in{riyou} eq "" || $in{riyou} == 1 || $in{riyou} == 11 || $in{riyou} == 3 || $in{riyou} == 31 ) {

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
<input type=hidden value="11" name="sisetu">
<input type=hidden value="11" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="�@   �ϊ�����  �@" >�@�@
<font size=-1>���݂�CP</font>�F<b>$chastats[14]</b><br>
<select name="itemkai" size=20>
HTM
	open(ITEM,"$maindir/shop2$bousikts");
while ( $itemda = <ITEM> ) {
	@itemdaa = split(/,/,$itemda);
	($itemname,$itembasyo,$itemjuuryou,$itemga,$itemgold,$itemkouka,$itemstatus[0],$itemti[0],$itemstatus[1],$itemti[1],$itemstatus[2],$itemti[2],$itemstatus[3],$itemti[3]) = @itemdaa;
print "<option value=\"$itemname/$itemjuuryou/$itemgold/$itemkouka\">�y$itemgold CP�z$omosa[$itemjuuryou]/$bui[$itembasyo] �� $itemname �i$itemkouka�j";
	}
close(ITEM);
print <<"HTM";
</select></form></td><td width=30></td><td>
HTM
}

sub baikyaku {

print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="11" name="sisetu">
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
<input type=hidden value="11" name="sisetu">
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