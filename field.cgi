#�@�`�����v���[���[�̏���
($sec,$min,$hour,$mday,$mon,$year,$wday) = localtime(time);
$year = $year + 1900;$mon ++;
@youbi = ('��','��','��','��','��','��','�y');
if ( length($min) == 1 ) { $min = "0$min"; }
$genzai ="$year�N$mon��$mday��($youbi[$wday]) $hour:$min";
open(NOW,"$maindir/playing$bousikts");
	while( $playnow = <NOW> ) {
		chop($playnow);
		($nowid,$nowname,$nowjikan) = split(/\//,$playnow);
		if ( $now < $nowjikan + 300 && $nowid ne $chaid ) {
			push(@playing,$playnow);
		}
	}
close(NOW);
$playnow = "$chaid/$chaname/$now\n";
push(@playing,$playnow);

open(NOW,">$maindir/playing$bousikts");
flock(NOW,2);
	foreach $playnow ( @playing ) {
print NOW "$playnow\n";
	}
flock(NOW,8);
close(NOW);
require "settei.cgi";
if ( $chastats[0] > $maxdmg ) { $chastats[0] = $maxdmg };
if ( $chastats[2] > $maxstr ) { $chastats[2] = $maxstr };
if ( $chastats[1] > $maxdef ) { $chastats[1] = $maxdef };
if ( $chastats[3] > $maxagi ) { $chastats[3] = $maxagi };
if ( $chastats[4] > $maxint ) { $chastats[4] = $maxint };
if ( $chastats[9] > $maxmhp ) { $chastats[9] = $maxmhp };
if ( $mente == 1 ){
&mente;
}
@omosa = ("","�y��","����","�d��");
@bui = ("����","�E��","����","��","��","�r","�r","�w","��");

$jobbarcha1 = int( ( $jobexpnow[$chaclass] / $jobexp[$chaclass] ) * 170 );
$jobritu = int($jobbarcha1 / 1.7); 
$jobritu2 = "<font color=darkblue>$jobritu<font size=-2>��</font></b></font>";
if ( $jobbarcha1 != 170 ) {
$jobbarcha2 = 170 - $jobbarcha1;
$hpbardmg3 = "<img src=\"$maindir/$imgfile/hpbar2.gif\" width=$jobbarcha2 height=\"8\">";
}

$playingkazu = @playing;
print <<"HTM";
<center>
<table border=0 width=800><tr>
<td align=right><nobr><font size=6 color=#$mojiiro2><b>$zone[$chaplace]</b></font></nobr></td><td width=30></td><td><nobr>
���݂̖`���ҁi$playingkazu�l�j/
HTM

foreach $playnow ( @playing ) {

	chop($playnow);
	($nowid,$nowname) = split(/\//,$playnow);
print " <a href=\"./$introcgi?usrid=$nowid\" target=\"intro\"><b>$nowname</font></b></a> /<wbr>";

}

$timesa = $chajikan - $now + $nexttime;

print <<"HTM";
<wbr></nobr></tr></table><br><hr>
<br>
<table border=0><tr><td>
<table border=1><tr><td>
<img src="$maindir/$imgfile/zonepic$chaplace.gif">
</td></tr></table>
</td><td width=10></td><td>
<table border=0><tr><td colspan=3>
HTM


$ryoukin1 = ( $chalvl ) * 3;
$ryoukin2 = ( $chastats[16] - $champ ) * 1;
$ryoukin = $ryoukin1 + $ryoukin2;
$tugilvl = $chanextlvl - $chaexp;
if ($jobexpnow[$chaclass] == $jobexp[$chaclass]){ $jobritu2 ="<font color=red><font size=-2> MASTER! </font></font>"; }
print <<"HTM";
<SCRIPT LANGUAGE="JavaScript">
defaultStatus="�E�N���b�N�ŃT�u���j���[��\\�����܂��B";

<!--
    //���j���[�\���֐�
    function Menu(){
        //��\���̏ꍇ�\���ɂ���
        if(menu.style.visibility == "hidden"){
            menu.style.posLeft = event.clientX;
            menu.style.posTop = event.clientY;
            menu.style.visibility = "visible";
        }
        //�\���̏ꍇ��\���ɂ���
        else if(menu.style.visibility == "visible"){
           menu.style.visibility = "hidden";
        }
        return false;
    }
    //���j���[��\���֐�
    function eraseMenu(){
        //�\���̏ꍇ��\���ɂ���
        if(menu.style.visibility == "visible"){
            menu.style.visibility = "hidden";
        }
    }
// -->
</SCRIPT>
</HEAD>
<BODY onclick="eraseMenu()" oncontextmenu="Menu();return false;">

<!--���j���[�p�^�O-->

<DIV id="menu" style={position:absolute;visibility:hidden;}>
    <TABLE border=3 bgcolor=gray cellpadding=5>
        <TR>
            <TD bgcolor="silver">
                <center><B><u><font color=darkblue><font face="Copperplate Gothic Bold">SUB MENU</font></font></u></B></center><P>
                <b>�������F <font color=#$chamoji>$hukubiki</b></font><font size=-1><b>��</b></font><br><hr>
                <b>���́iCHA�j�@�F<font color=#$chamoji>$chastats[5]</b></font> + <b><font color=palevioletred>$karistats[5]</font></b><br>
                <b>�Αϐ��iSVF�j�F<font color=#$chamoji>$chastats[6]</b></font> + <b><font color=palevioletred>$karistats[6]</font></b><br>
                <b>���ϐ��iSVC�j�F<font color=#$chamoji>$chastats[7]</b></font> + <b><font color=palevioletred>$karistats[7]</font></b><br>
                <b>���ϐ��iSVM�j�F<font color=#$chamoji>$chastats[8]</b></font> + <b><font color=palevioletred>$karistats[8]</font></b><br><hr>

                <font size=-1><b>�n���x�y$job[$chaclass]�z   <font color=palevioletred>$jobritu2</font><font size=-2></font></b></font><br>
<img src="$maindir/$imgfile/exp.gif" height="10"><img src="$maindir/$imgfile/jobbar1.gif" width=$jobbarcha1 height="8">$hpbardmg3<img src="$maindir/$imgfile/exp.gif" height="8"><br><hr>
                <b>����̎����F<font color=blue>$chastats[11]</font>�f<br>
                ���݂̕�V�F<font color=blue>$chastats[13]</font>�f<br>
                ���݂̏h��F<font color=red>$ryoukin</font>�f<br><hr>

                <font size=-1>����Lv�܂�</font><font color=#$chamoji>$tugilvl</font><font size=-1>EXP</font></b>

            <TD bgcolor="silver"><br>
<center>
<table bordercolor=#$wakuiro border=1>
<tr><td><nobr><b>S.EXP</b></nobr></td><td width=70 align=right><nobr><font color=palevioletred><b>$lvlpoint</font> pt</b></nobr></td></tr></table>
<form method="post" action="./$zonecgi">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="4" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="�@  �莆�𑗂�  �@">
</form>
<form method="post" action="./$zonecgi">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="8" name="useitem">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value=" �|�C���g�U�蕪�� " size=30>
</form>
<form method="post" action="./$zonecgi">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="3" name="useitem">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="     ����ύX     " size=30>
</form>
<form method="post" action="./$zonecgi">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="2" name="useitem">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value=" �A�C�e�����̂Ă�  " size=30>
</form>
<form method="post" action="./$zonecgi">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="21" name="useitem">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="�I�[�g�|�[�V���� " size=30>
</form>
<form method="post" action="./$zonecgi">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="80" name="useitem">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="   �R�����g�ύX   ">
</form>
<form action="$urlbbs" target=_blank>
<input type="submit" value="�@    �f����    �@" size=30>
</form>
<SCRIPT language="JavaScript">
<!--
function CloseWin(){
    window.close();
}
// -->
</SCRIPT>
</td>

            </TD>
        </TR>
    </TABLE>
</DIV>
<!--���j���[�p�^�O�����܂�-->
HTM

if ( $in{useitem} eq "1"){
#�@�A�C�e���g�p����
			$ccc = 1;$cbc = 0;
			while ( $ccc < 9 ) {
				if ( $chaitem[$ccc] ne "" ) {
				$cbc ++;
				}
				$ccc ++;
			}
	if ( $cbc == 0 ) {
print "<b>�g�p�ł���A�C�e��������܂���</b><br><br>";
&fieldform;
	} else {
			$ccc = 1;$cba = 0;
			while ( $ccc < 9 ) {
				if ( $chaitem[$ccc] ne "" ) {
open(KAI,"$maindir/item$bousikts");
		while ( $kaitori = <KAI> ) {
			($kainame,$a,$a,$a,$a,$a,$itemstats,$itemstats2) = split(/,/,$kaitori);
			if ( $chaitem[$ccc] eq $kainame && $itemstats >= 10) {
				push(@itemsuuji,$ccc);
				push(@itemkouka,$itemstats);
				push(@itemkouka2,$itemstats2);
				$cba ++;
			}
		}
close(KAI);
				}
$ccc ++;
			}
		if( $cba == 0 ) {
print "<b>�g�p�ł���A�C�e��������܂���<br><br></b>";

		} else {
print <<"HTM";
�u�A�C�e����I�����Ă��������v<br>
<form method="post" action="./$zonecgi">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="1a" name="useitem">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="     �g�p����    " onClick="this.disabled=true; this.value='     �g�p����    '; this.form.submit();"><br>
<select name="itemds" size=5>
HTM
$add = 0;
			foreach $atai (@itemsuuji) {
		print "<option value=\"$chaitem[$atai]/$atai/$itemkouka[$add]/$itemkouka2[$add]\">$chaitem[$atai] �i$chasetumei[$atai]�j";
$add ++;
			}
print <<"HTM";
</select></form><br>
HTM
		}
	}
&zoneform;

} elsif ( $in{useitem} eq "1a"){
($itemname,$itemnum,$itemstats,$itemstats2) = split(/\//,$in{itemds});
	if ( $itemname ne $chaitem[$itemnum] ) {
		&CgiError('�G���[����','�s���������^��������܂��B');
	} elsif ( $itemstats == 10 ) {

		if ( $chahp == $chastats[9] ) {
print "<b>������g�p���Ă��Ӗ�������܂���<br><br></b>";

		} else {
print "<b><font size=+1>$chaitem[$itemnum]</font> ���g�p���܂���</b><br><br>";
$chahp += $itemstats2;
			if ( $chahp > $chastats[9] ) {
			$chahp = $chastats[9];
			}
			if ( $chaeff[$itemnum] == 1 ) {
$chaitem[$itemnum] = $chaeff[$itemnum] = $chasetumei[$itemnum] = "";
			} elsif ( $chaeff[$itemnum] > 1 ) {
$chaeff[$itemnum] --;
			} else {
&fuseisyori;exit;
			}
&charadatawrt;
		}
&fieldform;


	} elsif ( $itemstats == 36 ) {

		if ( $champ == $chastats[16] ) {
print "<b>������g�p���Ă��Ӗ�������܂���<br><br></b>";

		} else {
print "<b><font size=+1>$chaitem[$itemnum]</font> ���g�p���܂���</b><br><br>";
$champ += $itemstats2;
			if ( $champ > $chastats[16] ) {
			$champ = $chastats[16];
			}
			if ( $chaeff[$itemnum] == 1 ) {
$chaitem[$itemnum] = $chaeff[$itemnum] = $chasetumei[$itemnum] = "";
			} elsif ( $chaeff[$itemnum] > 1 ) {
$chaeff[$itemnum] --;
			} else {
&fuseisyori;exit;
			}
&charadatawrt;
		}
&fieldform;



	} elsif ( $itemstats == 37 ) {

		if ( $chastats[12] == $chagold ) {
print "<b>������g�p���Ă��Ӗ�������܂���<br><br></b>";

		} else {
print "<b><font size=+1>$chaitem[$itemnum]</font> ���g�p���܂����B</b><br>";
$chastats[16] += 1;
print "<b>�ő�TP���A<font size=+1 color=#$mojiiro2>1</font><b> �オ�����I</b><br><br>";
			if ( $chahp > $chastats[9] ) {
			$chahp = $chastats[9];
			}
			if ( $chaeff[$itemnum] == 1 ) {
$chaitem[$itemnum] = $chaeff[$itemnum] = $chasetumei[$itemnum] = "";
			} elsif ( $chaeff[$itemnum] > 1 ) {
$chaeff[$itemnum] --;
			} else {
&fuseisyori;exit;
			}
&charadatawrt;
		}
&fieldform;


	} elsif ( $itemstats == 38 ) {

		if ( $chastats[12] == $chagold ) {
print "<b>������g�p���Ă��Ӗ�������܂���<br><br></b>";

		} else {
print "<b><font size=+1>$chaitem[$itemnum]</font> ���g�p���܂����B</b><br>";
$chastats[16] += 10;
print "<b>�ő�TP���A<font size=+1 color=#$mojiiro2>10</font><b> �オ�����I</b><br><br>";
			if ( $chahp > $chastats[9] ) {
			$chahp = $chastats[9];
			}
			if ( $chaeff[$itemnum] == 1 ) {
$chaitem[$itemnum] = $chaeff[$itemnum] = $chasetumei[$itemnum] = "";
			} elsif ( $chaeff[$itemnum] > 1 ) {
$chaeff[$itemnum] --;
			} else {
&fuseisyori;exit;
			}
&charadatawrt;
		}
&fieldform;


	} elsif ( $itemstats == 41 ) {

		if ( $chastats[12] == $chagold ) {
print "<b>������g�p���Ă��Ӗ�������܂���<br><br></b>";

		} else {
print "<b><font size=+1>$chaitem[$itemnum]</font> ���g�p���܂����B</b><br>";
$chastats[16] += 20;
$chastats[1] += 10;
$chastats[2] += 10;
$chastats[3] += 10;
$chastats[4] += 10;
$chastats[9] += 100;
print "<b>�ő�HP���A<font size=+1 color=#$mojiiro2>100</font><b> �オ�����I</b><br>";
print "<b>�ő�TP���A<font size=+1 color=#$mojiiro2>20</font><b> �オ�����I</b><br>";
print "<b>STR���A<font size=+1 color=#$mojiiro2>10</font><b> �オ�����I</b><br>";
print "<b>AC���A<font size=+1 color=#$mojiiro2>10</font><b> �オ�����I</b><br>";
print "<b>AGI���A<font size=+1 color=#$mojiiro2>10</font><b> �オ�����I</b><br>";
print "<b>INT���A<font size=+1 color=#$mojiiro2>10</font><b> �オ�����I</b><br>";
			if ( $chahp > $chastats[9] ) {
			$chahp = $chastats[9];
			}
			if ( $chaeff[$itemnum] == 1 ) {
$chaitem[$itemnum] = $chaeff[$itemnum] = $chasetumei[$itemnum] = "";
			} elsif ( $chaeff[$itemnum] > 1 ) {
$chaeff[$itemnum] --;
			} else {
&fuseisyori;exit;
			}
&charadatawrt;
		}
&fieldform;



	} elsif ( $itemstats == 40 ) {

		if ( $chastats[12] == $chagold ) {
print "<b>������g�p���Ă��Ӗ�������܂���<br><br></b>";

		} else {
print "<b><font size=+1>$chaitem[$itemnum]</font> ���g�p���܂����B</b><br>";
$chastats[16] += 30;
print "<b>�ő�TP���A<font size=+1 color=#$mojiiro2>30</font><b> �オ�����I</b><br><br>";
			if ( $chahp > $chastats[9] ) {
			$chahp = $chastats[9];
			}
			if ( $chaeff[$itemnum] == 1 ) {
$chaitem[$itemnum] = $chaeff[$itemnum] = $chasetumei[$itemnum] = "";
			} elsif ( $chaeff[$itemnum] > 1 ) {
$chaeff[$itemnum] --;
			} else {
&fuseisyori;exit;
			}
&charadatawrt;
		}
&fieldform;


	} elsif ( $itemstats == 39 ) {

		if ( $chastats[12] == $chagold ) {
print "<b>������g�p���Ă��Ӗ�������܂���<br><br></b>";

		} else {
$chahp = $chastats[9];
$champ = $chastats[16];
print "<b><font size=+1>$chaitem[$itemnum]</font> ���g�p���܂����B</b><br>";
print "<b>HP��TP���S�������I</b><br><br>";
			if ( $chahp > $chastats[9] ) {
			$chahp = $chastats[9];
			}
			if ( $chaeff[$itemnum] == 1 ) {
$chaitem[$itemnum] = $chaeff[$itemnum] = $chasetumei[$itemnum] = "";
			} elsif ( $chaeff[$itemnum] > 1 ) {
$chaeff[$itemnum] --;
			} else {
&fuseisyori;exit;
			}
&charadatawrt;
		}
&fieldform;


	} elsif ( $itemstats == 30 ) {

		if ( $chastats[12] == $chagold ) {
print "<b>������g�p���Ă��Ӗ�������܂���<br><br></b>";

		} else {
print "<b><font size=+1>$chaitem[$itemnum]</font> ���g�p���܂����B</b><br>";
$hpup = 10;
$chastats[9] += $hpup;
print "<b>�ő�HP���A<font size=+1 color=#$mojiiro2>$hpup</font><b> �オ�����I</b><br><br>";
			if ( $chahp > $chastats[9] ) {
			$chahp = $chastats[9];
			}
			if ( $chaeff[$itemnum] == 1 ) {
$chaitem[$itemnum] = $chaeff[$itemnum] = $chasetumei[$itemnum] = "";
			} elsif ( $chaeff[$itemnum] > 1 ) {
$chaeff[$itemnum] --;
			} else {
&fuseisyori;exit;
			}
&charadatawrt;
		}
&fieldform;


	} elsif ( $itemstats == 31 ) {

		if ( $chastats[12] == $chagold ) {
print "<b>������g�p���Ă��Ӗ�������܂���<br><br></b>";

		} else {
print "<b><font size=+1>$chaitem[$itemnum]</font> ���g�p���܂����B</b><br>";
$strup = 1;
$chastats[2] += $strup;
print "<b>STR���A<font size=+1 color=#$mojiiro2>$strup</font><b> �オ�����I</b><br><br>";
			if ( $chahp > $chastats[9] ) {
			$chahp = $chastats[9];
			}
			if ( $chaeff[$itemnum] == 1 ) {
$chaitem[$itemnum] = $chaeff[$itemnum] = $chasetumei[$itemnum] = "";
			} elsif ( $chaeff[$itemnum] > 1 ) {
$chaeff[$itemnum] --;
			} else {
&fuseisyori;exit;
			}
&charadatawrt;
		}
&fieldform;


	} elsif ( $itemstats == 32 ) {

		if ( $chastats[12] == $chagold ) {
print "<b>������g�p���Ă��Ӗ�������܂���<br><br></b>";

		} else {
print "<b><font size=+1>$chaitem[$itemnum]</font> ���g�p���܂����B</b><br>";
$acup = 1;
$chastats[1] += $acup;
print "<b>AC���A<font size=+1 color=#$mojiiro2>$acup</font><b> �オ�����I</b><br><br>";
			if ( $chahp > $chastats[9] ) {
			$chahp = $chastats[9];
			}
			if ( $chaeff[$itemnum] == 1 ) {
$chaitem[$itemnum] = $chaeff[$itemnum] = $chasetumei[$itemnum] = "";
			} elsif ( $chaeff[$itemnum] > 1 ) {
$chaeff[$itemnum] --;
			} else {
&fuseisyori;exit;
			}
&charadatawrt;
		}
&fieldform;


	} elsif ( $itemstats == 33 ) {

		if ( $chastats[12] == $chagold ) {
print "<b>������g�p���Ă��Ӗ�������܂���<br><br></b>";

		} else {
print "<b><font size=+1>$chaitem[$itemnum]</font> ���g�p���܂����B</b><br>";
$chaup = 1;
$chastats[5] += $chaup;
print "<b>CHA���A<font size=+1 color=#$mojiiro2>$chaup</font><b> �オ�����I</b><br><br>";
			if ( $chahp > $chastats[9] ) {
			$chahp = $chastats[9];
			}
			if ( $chaeff[$itemnum] == 1 ) {
$chaitem[$itemnum] = $chaeff[$itemnum] = $chasetumei[$itemnum] = "";
			} elsif ( $chaeff[$itemnum] > 1 ) {
$chaeff[$itemnum] --;
			} else {
&fuseisyori;exit;
			}
&charadatawrt;
		}
&fieldform;


	} elsif ( $itemstats == 34 ) {

		if ( $chastats[12] == $chagold ) {
print "<b>������g�p���Ă��Ӗ�������܂���<br><br></b>";

		} else {
print "<b><font size=+1>$chaitem[$itemnum]</font> ���g�p���܂����B</b><br>";
$intup = 1;
$chastats[4] += $intup;
print "<b>INT���A<font size=+1 color=#$mojiiro2>$intup</font><b> �オ�����I</b><br><br>";
			if ( $chahp > $chastats[9] ) {
			$chahp = $chastats[9];
			}
			if ( $chaeff[$itemnum] == 1 ) {
$chaitem[$itemnum] = $chaeff[$itemnum] = $chasetumei[$itemnum] = "";
			} elsif ( $chaeff[$itemnum] > 1 ) {
$chaeff[$itemnum] --;
			} else {
&fuseisyori;exit;
			}
&charadatawrt;
		}
&fieldform;


	} elsif ( $itemstats == 35 ) {

		if ( $chastats[12] == $chagold ) {
print "<b>������g�p���Ă��Ӗ�������܂���<br><br></b>";

		} else {
print "<b><font size=+1>$chaitem[$itemnum]</font> ���g�p���܂����B</b><br>";
$agiup = 1;
$chastats[3] += $agiup;
print "<b>AGI���A<font size=+1 color=#$mojiiro2>$agiup</font><b> �オ�����I</b><br><br>";
			if ( $chahp > $chastats[9] ) {
			$chahp = $chastats[9];
			}
			if ( $chaeff[$itemnum] == 1 ) {
$chaitem[$itemnum] = $chaeff[$itemnum] = $chasetumei[$itemnum] = "";
			} elsif ( $chaeff[$itemnum] > 1 ) {
$chaeff[$itemnum] --;
			} else {
&fuseisyori;exit;
			}
&charadatawrt;
		}
&fieldform;


	} elsif ( $itemstats == 51 ) {

		if ( $chastats[12] == $chagold ) {
print "<b>������g�p���Ă��Ӗ�������܂���<br><br></b>";

		} else {
print "<b><font size=+1>$chaitem[$itemnum]</font> ���g�p���܂����B</b><br>";
print "<b>���Z�w<font color=red>�P���̕�</font>�x<b>���K�������I</b><br><br>";
if ( $flag14 eq "" ) { $flag14 = 14; }
			if ( $chahp > $chastats[9] ) {
			$chahp = $chastats[9];
			}
			if ( $chaeff[$itemnum] == 1 ) {
$chaitem[$itemnum] = $chaeff[$itemnum] = $chasetumei[$itemnum] = "";
			} elsif ( $chaeff[$itemnum] > 1 ) {
$chaeff[$itemnum] --;
			} else {
&fuseisyori;exit;
			}
&charadatawrt;
		}
&fieldform;


	} elsif ( $itemstats == 52 ) {

		if ( $chastats[12] == $chagold ) {
print "<b>������g�p���Ă��Ӗ�������܂���<br><br></b>";

		} else {
print "<b><font size=+1>$chaitem[$itemnum]</font> ���g�p���܂����B</b><br>";
print "<b>���Z�w<font color=red>���o�C�u</font>�x<b>���K�������I</b><br><br>";
if ( $flag13 eq "" ) { $flag13 = 13; }
			if ( $chahp > $chastats[9] ) {
			$chahp = $chastats[9];
			}
			if ( $chaeff[$itemnum] == 1 ) {
$chaitem[$itemnum] = $chaeff[$itemnum] = $chasetumei[$itemnum] = "";
			} elsif ( $chaeff[$itemnum] > 1 ) {
$chaeff[$itemnum] --;
			} else {
&fuseisyori;exit;
			}
&charadatawrt;
		}
&fieldform;

	} elsif ( $itemstats == 11 ) {
print <<"HTM";
<font size=+1>$chaitem[$itemnum]</font> ���g�p�����I<br><br>
HTM
		if ( $chaeff[$itemnum] == 1 ) {
$chaitem[$itemnum] = $chaeff[$itemnum] = $chasetumei[$itemnum] = "";
		} elsif ( $chaeff[$itemnum] > 1 ) {
$chaeff[$itemnum] --;
		} else {
&fuseisyori;exit;
		}
$chaplace = $itemstats2;
&charadatawrt;
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="$itemstats2" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="$zone[$itemstats2] �֏u�Ԉړ�" ><br></td></tr></table>
</form>
HTM
	} else { &fuseisyori; 
	}


} elsif ( $in{riyou} eq "4" ) {
print <<"HTM";
����l��I�����A���e���L�����Ă��������B<br>
<form action="./$zonecgi" method="post">
<input type=hidden value="10" name="sisetu">
<input type=hidden value="41" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<select name="chara">
HTM

open(CHA,"$maindir/$foldacha/user_id$bousi2cha$bousikts2");
$tourokunum = 1;
		while ( $chadata = <CHA> ) {
		chop($chadata);
		($id,$name) = split(/\//,$chadata);
			if ( $name ne $chaname) {
print "<option value=\"$id\">$tourokunum.$name<br>";
$tourokunum ++;
			}
		}
close(CHA);
print <<"HTM";
</select>
<br><br>
<input type=text size=50 value="" name="tegami">(100�����ȓ�)<br><br>
<input type=submit value="�@�@�@ ���@�M �@�@�@">
</form>
HTM
&zoneform;

} elsif ( $in{riyou} eq "41" ) {
	if ( $in{tegami} eq "" ) {
print <<"HTM";
�莆�̓��e��������Ă��܂���B<br>
<br>
HTM
&zoneform;
	} elsif( length($in{tegami}) > 200 ) {
print <<"HTM";
���������P�O�O�������z���Ă��܂��B<br>
<br>
HTM
&zoneform;

	} else {
$in{tegami} =~ s/</&lt;/g;
$in{tegami} =~ s/>/&gt;/g;
$tegaminaiyou =  "$now\t$chaname\t$chamoji\t$in{tegami}\t$genzai\t\n";

open(BAN,"$maindir/$foldacha/tegami_$in{chara}$bousi2cha$bousikts");
   @letters = <BAN>;
close(BAN);
$letter = @letter;
           if ( $letter >= 20 ) {
              $letters[0] = "";
           }
unshift(@letters,"$now\t$chaname\t$chamoji\t$in{tegami}\t$genzai\t\n");
open(BAN,">$maindir/$foldacha/tegami_$in{chara}$bousi2cha$bousikts");
flock(BAN,2);
   print BAN @letters;
flock(BAN,8);
close(BAN);

print <<"HTM";
�莆�͖����͂����܂����B<br><br>
HTM
&zoneform;

     }

	} elsif ( $in{useitem} eq "80" ) {
print <<"HTM";
�V�����R�����g����͂��Ă��������B�i�S�p35�����E���p70�����ȓ��j<br>
<form action="./$zonecgi" method="post">
<input type=text value="" size=50 name="comment" maxlength=70>
<input type=submit value="  ���e�ύX  " onClick="this.disabled=true; this.value='  ���e�ύX  '; this.form.submit();">

<input type=hidden value="81" name="useitem">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
</form>
HTM
&zoneform;
	} elsif ( $in{useitem} eq "81" ) {
$in{comment} =~ s/,//g;
$maxcombo = $in{comment};
&charadatawrt;
print <<"HTM";
����ɕύX����܂����B<br><br>
HTM
&fieldform;



} elsif ( $in{useitem} eq "6"){

#�@����h��̑���

&itemkuuran;
	if ( $ccb == 9 ) {
print <<"HTM";
�u�����ł���A�C�e���������Ă��܂���B�v<br>
HTM
&zoneform;
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
�u�����ł���A�C�e���������Ă��܂���B�v<br>
HTM
&zoneform;
		} else {
print <<"HTM";
�u��������A�C�e����I�����Ă��������B�v<br>
<form method="post" action="./$zonecgi">
<input type=hidden value="20" name="useitem">
<input type=hidden value="61" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="�@    ��������   �@" onClick="this.disabled=true; this.value='      ��������     '; this.form.submit();"><br>
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
&zoneform;
		}
	}
} elsif ( $in{riyou} eq "61"){
		($soubiname,$numa) = split(/\//,$in{itemde});
	if ( $in{itemde} eq "" ) {
print <<"HTM";
�u��������A�C�e�����I������Ă��܂���B�v<br>
HTM
&zoneform;

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
�u���x��������܂���B�v<br>
HTM
&zoneform;
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
   �������܂����B�v<br>
HTM
&zoneform;
		}
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




} elsif ( $in{useitem} eq "2"){
#�@�A�C�e����������

			$ccc = 1;$ccb = 0;
			while ( $ccc < 9 ) {
				if ( $chaitem[$ccc] eq "" ) {
				$ccb ++;
				}
				$ccc ++;
			}

	if ( $ccb eq 8 ) {
print <<"HTM";
�A�C�e��������܂���<br>
HTM

	} else {
print <<"HTM";
<b><font color=#$mojiiro2>�̂Ă�</font></b>�A�C�e����I�����Ă�������<br>
<form method="post" action="./$zonecgi">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="2a" name="useitem">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="�@    �̂Ă�   �@" onClick="this.disabled=true; this.value='      �̂Ă�     '; this.form.submit();"><br>
<select name="itemde" size=6>
HTM
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

&zoneform;

} elsif ( $in{useitem} eq "2a"){
if ( $chaitem[$in{itemde}] eq "" ) { &fuseisyori;exit; }
print <<"HTM";
<font size=4 color=#$mojiiro2><b>$chaitem[$in{itemde}]</font> ($chasetumei[$in{itemde}])�@���̂Ă�</b><br><br>
HTM
$chaitem[$in{itemde}] = $chaeff[$in{itemde}] = $chasetumei[$in{itemde}] = "";
&charadatawrt;
&fieldform;




} elsif ( $in{useitem} eq "21"){
$bpo = "0";
#�@�I�[�g�|�[�V��������
$bpo = "0";
print <<"HTM";
<b>�I�[�g�|�[�V�����ݒ�</b><br>

<form action="./$zonecgi" method="post">
HP��
<input type=text value="$autop" size=5 name="autop" maxlength=5>
�ȉ��ɂȂ������ɁA<br>
<input type=text value="$potion" size=16 name="potion" maxlength=16>
���g�p����B
<input type=submit value="  �m��  " onClick="this.disabled=true; this.value='  �m��  '; this.form.submit();">
<input type=hidden value="7" name="sisetu">
<input type=hidden value="81" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
</form>
HTM
&zoneform;

	} elsif ( $in{riyou} eq "81" ) {
$in{comment} =~ s/,//g;
$autop = $in{autop};
$potion = $in{potion};
&charadatawrt;
print <<"HTM";

<form action="./$zonecgi" method="post">
�ݒ芮�����܂����B<br><br>
HTM

&zoneform;





} elsif ( $in{useitem} eq "2a"){
if ( $chaitem[$in{itemde}] eq "" ) { &fuseisyori;exit; }
print <<"HTM";
<font size=4 color=#$mojiiro2><b>$chaitem[$in{itemde}]</font> ($chasetumei[$in{itemde}])�@���̂Ă�</b><br><br>
HTM
$chaitem[$in{itemde}] = $chaeff[$in{itemde}] = $chasetumei[$in{itemde}] = "";
&charadatawrt;
&fieldform;


# �|�C���g�U�蕪������

} elsif ( $in{useitem} eq "8"){

&furiwake;

} elsif ( $in{point} eq "1"){
	if ( $lvlpoint < 1 ){
print <<"HTM";
<b>S.EXP</b>������܂���B<br>
HTM
&zoneform;
	} else {
$lvlpoint --;
$nowstrexp += 2;
	if ( $nowstrexp >= $strexp ) {
print <<"HTM";
<b><font color=darkorange>STR</font></b>���オ�����I<br>
HTM
$strexp *= 1.3;
if ($strexp > 1000){$strexp = 1000;}
$nowstrexp = 0;
$chastats[2] ++;
}
&charadatawrt;
&furiwake
}
} elsif ( $in{point} eq "1a"){
	if ( $lvlpoint < 10 ){
print <<"HTM";
<b>S.EXP</b>������܂���B<br>
HTM
&zoneform;
	} else {
$lvlpoint -= 10;
$nowstrexp += 20;
	if ( $nowstrexp >= $strexp ) {
print <<"HTM";
<b><font color=darkorange>STR</font></b>���オ�����I<br>
HTM
$strexp *= 1.3;
if ($strexp > 1000){$strexp = 1000;}
$nowstrexp = 0;
$chastats[2] ++;
}
&charadatawrt;
&furiwake
}

} elsif ( $in{point} eq "1c"){
	if ( $lvlpoint < 50 ){
print <<"HTM";
<b>S.EXP</b>������܂���B<br>
HTM
&zoneform;
	} else {
$lvlpoint -= 50;
$nowstrexp += 100;
	if ( $nowstrexp >= $strexp ) {
print <<"HTM";
<b><font color=darkorange>STR</font></b>���オ�����I<br>
HTM
$strexp *= 1.3;
if ($strexp > 1000){$strexp = 1000;}
$nowstrexp = 0;
$chastats[2] ++;
}
&charadatawrt;
&furiwake
}

} elsif ( $in{point} eq "1b"){
	if ( $lvlpoint < 100 ){
print <<"HTM";
<b>S.EXP</b>������܂���B<br>
HTM
&zoneform;
	} else {
$lvlpoint -= 100;
$nowstrexp += 200;
	if ( $nowstrexp >= $strexp ) {
print <<"HTM";
<b><font color=darkorange>STR</font></b>���オ�����I<br>
HTM
$strexp *= 1.3;
if ($strexp > 1000){$strexp = 1000;}
$nowstrexp = 0;
$chastats[2] ++;
}
&charadatawrt;
&furiwake
}

} elsif ( $in{point} eq "1d"){
	if ( $lvlpoint < 500 ){
print <<"HTM";
<b>S.EXP</b>������܂���B<br>
HTM
&zoneform;
	} else {
$lvlpoint -= 500;
$nowstrexp += 1000;
	if ( $nowstrexp >= $strexp ) {
print <<"HTM";
<b><font color=darkorange>STR</font></b>���オ�����I<br>
HTM
$strexp *= 1.3;
if ($strexp > 500){$strexp = 500;}
$nowstrexp = 0;
$chastats[2] ++;
}
&charadatawrt;
&furiwake
}

} elsif ( $in{point} eq "2"){
	if ( $lvlpoint < 1 ){
print <<"HTM";
<b>S.EXP</b>������܂���B<br>
HTM
&zoneform;
	} else {
$lvlpoint --;
$nowacexp += 15;
	if ( $nowacexp >= $acexp ) {
print <<"HTM";
<b><font color=lightsalmon>AC</font></b>���オ�����I<br>
HTM
$acexp *= 1.5;
if ($acexp > 1000000){$acexp = 1000000;}
$nowacexp = 0;
$chastats[1] ++;
}
&charadatawrt;
&furiwake
}
} elsif ( $in{point} eq "2a"){
	if ( $lvlpoint < 10 ){
print <<"HTM";
<b>S.EXP</b>������܂���B<br>
HTM
&zoneform;
	} else {
$lvlpoint -= 10;
$nowacexp += 150;
	if ( $nowacexp >= $acexp ) {
print <<"HTM";
<b><font color=lightsalmon>AC</font></b>���オ�����I<br>
HTM
$acexp *= 1.5;
if ($acexp > 1000000){$acexp = 1000000;}
$nowacexp = 0;
$chastats[1] ++;
}
&charadatawrt;
&furiwake
}

} elsif ( $in{point} eq "2c"){
	if ( $lvlpoint < 50 ){
print <<"HTM";
<b>S.EXP</b>������܂���B<br>
HTM
&zoneform;
	} else {
$lvlpoint -= 50;
$nowacexp += 750;
	if ( $nowacexp >= $acexp ) {
print <<"HTM";
<b><font color=lightsalmon>AC</font></b>���オ�����I<br>
HTM
$acexp *= 1.5;
if ($acexp > 1000000){$acexp = 1000000;}
$nowacexp = 0;
$chastats[1] ++;
}
&charadatawrt;
&furiwake
}

} elsif ( $in{point} eq "2b"){
	if ( $lvlpoint < 100 ){
print <<"HTM";
<b>S.EXP</b>������܂���B<br>
HTM
&zoneform;
	} else {
$lvlpoint -= 100;
$nowacexp += 1500;
	if ( $nowacexp >= $acexp ) {
print <<"HTM";
<b><font color=lightsalmon>AC</font></b>���オ�����I<br>
HTM
$acexp *= 1.5;
if ($acexp > 1000000){$acexp = 1000000;}
$nowacexp = 0;
$chastats[1] ++;
}
&charadatawrt;
&furiwake
}

} elsif ( $in{point} eq "2d"){
	if ( $lvlpoint < 500 ){
print <<"HTM";
<b>S.EXP</b>������܂���B<br>
HTM
&zoneform;
	} else {
$lvlpoint -= 500;
$nowacexp += 7500;
	if ( $nowacexp >= $acexp ) {
print <<"HTM";
<b><font color=lightsalmon>AC</font></b>���オ�����I<br>
HTM
$acexp *= 1.5;
if ($acexp > 1000000){$acexp = 1000000;}
$nowacexp = 0;
$chastats[1] ++;
}
&charadatawrt;
&furiwake
}

} elsif ( $in{point} eq "3"){
	if ( $lvlpoint < 1 ){
print <<"HTM";
<b>S.EXP</b>������܂���B<br>
HTM
&zoneform;
	} else {
$lvlpoint --;
$nowagiexp += 1;
	if ( $nowagiexp >= $agiexp ) {
print <<"HTM";
<b><font color=orchid>AGI</font></b>���オ�����I<br>
HTM
$agiexp *= 1.2;
if ($agiexp > 1000){$agiexp = 1000;}
$nowagiexp = 0;
$chastats[3] ++;
}
&charadatawrt;
&furiwake
}
} elsif ( $in{point} eq "3a"){
	if ( $lvlpoint < 10 ){
print <<"HTM";
<b>S.EXP</b>������܂���B<br>
HTM
&zoneform;
	} else {
$lvlpoint -= 10;
$nowagiexp += 10;
	if ( $nowagiexp >= $agiexp ) {
print <<"HTM";
<b><font color=orchid>AGI</font></b>���オ�����I<br>
HTM
$agiexp *= 1.2;
if ($agiexp > 1000){$agiexp = 1000;}
$nowagiexp = 0;
$chastats[3] ++;
}
&charadatawrt;
&furiwake
}

} elsif ( $in{point} eq "3c"){
	if ( $lvlpoint < 50 ){
print <<"HTM";
<b>S.EXP</b>������܂���B<br>
HTM
&zoneform;
	} else {
$lvlpoint -= 50;
$nowagiexp += 50;
	if ( $nowagiexp >= $agiexp ) {
print <<"HTM";
<b><font color=orchid>AGI</font></b>���オ�����I<br>
HTM
$agiexp *= 1.2;
if ($agiexp > 1000){$agiexp = 1000;}
$nowagiexp = 0;
$chastats[3] ++;
}
&charadatawrt;
&furiwake
}

} elsif ( $in{point} eq "3b"){
	if ( $lvlpoint < 100 ){
print <<"HTM";
<b>S.EXP</b>������܂���B<br>
HTM
&zoneform;
	} else {
$lvlpoint -= 100;
$nowagiexp += 100;
	if ( $nowagiexp >= $agiexp ) {
print <<"HTM";
<b><font color=orchid>AGI</font></b>���オ�����I<br>
HTM
$agiexp *= 1.2;
if ($agiexp > 1000){$agiexp = 1000;}
$nowagiexp = 0;
$chastats[3] ++;
}
&charadatawrt;
&furiwake
}

} elsif ( $in{point} eq "3d"){
	if ( $lvlpoint < 500 ){
print <<"HTM";
<b>S.EXP</b>������܂���B<br>
HTM
&zoneform;
	} else {
$lvlpoint -= 500;
$nowagiexp += 500;
	if ( $nowagiexp >= $agiexp ) {
print <<"HTM";
<b><font color=orchid>AGI</font></b>���オ�����I<br>
HTM
$agiexp *= 1.2;
if ($agiexp > 1000){$agiexp = 1000;}
$nowagiexp = 0;
$chastats[3] ++;
}
&charadatawrt;
&furiwake
}

} elsif ( $in{point} eq "4"){
	if ( $lvlpoint < 1 ){
print <<"HTM";
<b>S.EXP</b>������܂���B<br>
HTM
&zoneform;
	} else {
$lvlpoint --;
$nowintexp += 1;
	if ( $nowintexp >= $intexp ) {
print <<"HTM";
<b><font color=cornflowerblue>INT</font></b>���オ�����I<br>
HTM
$intexp *= 1.2;
if ($intexp > 1000){$intexp = 1000;}
$nowintexp = 0;
$chastats[4] ++;
}
&charadatawrt;
&furiwake
}
} elsif ( $in{point} eq "4a"){
	if ( $lvlpoint < 10 ){
print <<"HTM";
<b>S.EXP</b>������܂���B<br>
HTM
&zoneform;
	} else {
$lvlpoint -= 10;
$nowintexp += 10;
	if ( $nowintexp >= $intexp ) {
print <<"HTM";
<b><font color=cornflowerblue>INT</font></b>���オ�����I<br>
HTM
$intexp *= 1.2;
if ($intexp > 1000){$intexp = 1000;}
$nowintexp = 0;
$chastats[4] ++;
}
&charadatawrt;
&furiwake
	}

} elsif ( $in{point} eq "4c"){
	if ( $lvlpoint < 50 ){
print <<"HTM";
<b>S.EXP</b>������܂���B<br>
HTM
&zoneform;
	} else {
$lvlpoint -= 50;
$nowintexp += 50;
	if ( $nowintexp >= $intexp ) {
print <<"HTM";
<b><font color=cornflowerblue>INT</font></b>���オ�����I<br>
HTM
$intexp *= 1.2;
if ($intexp > 1000){$intexp = 1000;}
$nowintexp = 0;
$chastats[4] ++;
}
&charadatawrt;
&furiwake
	}

} elsif ( $in{point} eq "4b"){
	if ( $lvlpoint < 100 ){
print <<"HTM";
<b>S.EXP</b>������܂���B<br>
HTM
&zoneform;
	} else {
$lvlpoint -= 100;
$nowintexp += 100;
	if ( $nowintexp >= $intexp ) {
print <<"HTM";
<b><font color=cornflowerblue>INT</font></b>���オ�����I<br>
HTM
$intexp *= 1.2;
if ($intexp > 1000){$intexp = 1000;}
$nowintexp = 0;
$chastats[4] ++;
}
&charadatawrt;
&furiwake
	}

} elsif ( $in{point} eq "4d"){
	if ( $lvlpoint < 500 ){
print <<"HTM";
<b>S.EXP</b>������܂���B<br>
HTM
&zoneform;
	} else {
$lvlpoint -= 500;
$nowintexp += 500;
	if ( $nowintexp >= $intexp ) {
print <<"HTM";
<b><font color=cornflowerblue>INT</font></b>���オ�����I<br>
HTM
$intexp *= 1.2;
if ($intexp > 1000){$intexp = 1000;}
$nowintexp = 0;
$chastats[4] ++;
}
&charadatawrt;
&furiwake
	}


sub furiwake{
$strbarcha1 = int( ( $nowstrexp / $strexp ) * 180 );
$strritu = int($strbarcha1 / 1.8); 
if ( $strbarcha1 != 180 ) {
$strbarcha2 = 180 - $strbarcha1;
$strbardmg2 = "<img src=\"$maindir/$imgfile/hpbar2.gif\" width=$strbarcha2 height=\"8\" alt=$strritu��>";
}
$acbarcha1 = int( ( $nowacexp / $acexp ) * 180 );
$acritu = int($acbarcha1 / 1.8); 
if ( $acbarcha1 != 180 ) {
$acbarcha2 = 180 - $acbarcha1;
$acbardmg2 = "<img src=\"$maindir/$imgfile/hpbar2.gif\" width=$acbarcha2 height=\"8\" alt=$acritu��>";
}
$agibarcha1 = int( ( $nowagiexp / $agiexp ) * 180 );
$agiritu = int($agibarcha1 / 1.8); 
if ( $agibarcha1 != 180 ) {
$agibarcha2 = 180 - $agibarcha1;
$agibardmg2 = "<img src=\"$maindir/$imgfile/hpbar2.gif\" width=$agibarcha2 height=\"8\" alt=$agiritu��>";
}
$intbarcha1 = int( ( $nowintexp / $intexp ) * 180 );
$intritu = int($intbarcha1 / 1.8); 
if ( $intbarcha1 != 180 ) {
$intbarcha2 = 180 - $intbarcha1;
$intbardmg2 = "<img src=\"$maindir/$imgfile/hpbar2.gif\" width=$intbarcha2 height=\"8\" alt=$intritu��>";
}

print <<"HTM";
<b>S.EXP</b>�̐U�蕪�����s���܂��B<br><br>

<center>
<table bordercolor=#$wakuiro border=1>
<tr><td><nobr>���݂�<b>S.EXP</b></nobr></td><td width=70 align=right><nobr><font color=palevioletred><b>$lvlpoint</font> pt</b></nobr></td></tr></table>
</center>

<table border=2>
<tbody>
<tr>
<td><b>�ð��</td><td><b><center>�X�e�[�^�XEXP</td><td><b>����</td><td><center><b>1</td><td><center><b>10</td><td><center><b>50</td><td><center><b>100</td><td><center><b>500</td>
</td>
</tr>
<tr>
<td><b><center>STR</td><td><b><center><img src="$maindir/$imgfile/exp.gif" height="10"><img src="$maindir/$imgfile/mpbar1.gif" width=$strbarcha1 height="8" alt="$strritu��">$strbardmg2<img src="$maindir/$imgfile/exp.gif" height="8"></td><td align=right><b><font color=#$chamoji>$chastats[2] </td>
<td>
<form method="post" action="./$zonecgi" style="float:left">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="1" name="point">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="��" size=30>
</form>
</td>
<td>
<form method="post" action="./$zonecgi" style="float:left">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="1a" name="point">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="��" size=30>
</form>
</td>
<td>
<form method="post" action="./$zonecgi" style="float:left">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="1c" name="point">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="��" size=30>
</form>
</td>
<td>
<form method="post" action="./$zonecgi" style="float:left">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="1b" name="point">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="��" size=30>
</form>
</td>
<td>
<form method="post" action="./$zonecgi" style="float:left">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="1d" name="point">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="��" size=30>
</form>
</td>
</tr>
<tr>
<td><b><center>AC</td><td><b><center><img src="$maindir/$imgfile/exp.gif" height="10"><img src="$maindir/$imgfile/mpbar1.gif" width=$acbarcha1 height="8" alt="$strritu��">$acbardmg2<img src="$maindir/$imgfile/exp.gif" height="8"></td><td align=right><b><font color=#$chamoji>$chastats[1] </td>
<td>
<form method="post" action="./$zonecgi" style="float:left">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="2" name="point">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="��" size=30>
</form>
</td>
<td>
<form method="post" action="./$zonecgi" style="float:left">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="2a" name="point">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="��" size=30>
</form>
</td>
<td>
<form method="post" action="./$zonecgi" style="float:left">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="2c" name="point">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="��" size=30>
</form>
</td>
<td>
<form method="post" action="./$zonecgi" style="float:left">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="2b" name="point">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="��" size=30>
</form>
</td>
<td>
<form method="post" action="./$zonecgi" style="float:left">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="2d" name="point">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="��" size=30>
</form>
</td>
</tr>
<tr>
<td><b><center>AGI</td><td><b><center><img src="$maindir/$imgfile/exp.gif" height="10"><img src="$maindir/$imgfile/mpbar1.gif" width=$agibarcha1 height="8" alt="$strritu��">$agibardmg2<img src="$maindir/$imgfile/exp.gif" height="8"></td><td align=right><b><font color=#$chamoji>$chastats[3] </td>
<td>
<form method="post" action="./$zonecgi" style="float:left">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="3" name="point">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="��" size=30>
</form>
</td>
<td>
<form method="post" action="./$zonecgi" style="float:left">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="3a" name="point">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="��" size=30>
</form>
</td>
<td>
<form method="post" action="./$zonecgi" style="float:left">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="3c" name="point">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="��" size=30>
</form>
</td>
<td>
<form method="post" action="./$zonecgi" style="float:left">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="3b" name="point">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="��" size=30>
</form>
</td>
<td>
<form method="post" action="./$zonecgi" style="float:left">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="3d" name="point">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="��" size=30>
</form>
</td>
</tr>
<tr>
<td><b><center>INT</td><td><b><center><img src="$maindir/$imgfile/exp.gif" height="10"><img src="$maindir/$imgfile/mpbar1.gif" width=$intbarcha1 height="8" alt="$strritu��">$intbardmg2<img src="$maindir/$imgfile/exp.gif" height="8"></td><td align=right><b><font color=#$chamoji>$chastats[4] </td>
<td>
<form method="post" action="./$zonecgi" style="float:left">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="4" name="point">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="��" size=30>
</form>
</td>
<td>
<form method="post" action="./$zonecgi" style="float:left">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="4a" name="point">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="��" size=30>
</form>
</td>
<td>
<form method="post" action="./$zonecgi" style="float:left">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="4c" name="point">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="��" size=30>
</form>
</td>
<td>
<form method="post" action="./$zonecgi" style="float:left">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="4b" name="point">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="��" size=30>
</form>
</td>
<td>
<form method="post" action="./$zonecgi" style="float:left">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="4d" name="point">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="��" size=30>
</form>
</td>
</tr></table>
HTM
&zoneform;
}

#�@���@�g�p����

} elsif ( $in{mahou} eq "1"){
	if ( $champ < 3) {
print <<"HTM";
<b>TP</b>������Ȃ��ׁA<br>
<b>�q�[�����O</b>���g���Ȃ������B
HTM

	} elsif ( $chahp == $chastats[9] ){
print <<"HTM";
<b>����HP�����^���ׁ̈A<br>
�q�[�����O���g�p���Ă��Ӗ�������܂���B</b>
HTM
		} else {
$hiru1 = $chastats[0] + $chastats[1]+ $chastats[2]+ $chastats[3]+ $chastats[4]+ $chastats[5]+ $chastats[6]+ $chastats[7];
$hiru2 = $chalvl * 2;
$karikoka = int( $hiru1 / 3 );
$kaihuku = $karikoka + $hiru2;
$kaihuku += int(rand($chalvl));
$chahp += $kaihuku;
$champ -=3;
			if ( $chahp > $chastats[9] ) {
			$chahp = $chastats[9];
			}

print <<"HTM";
<font color=#$chamoji><b>$chaname</b></font>��<b>�q�[�����O</b>���������I<br>
<b>HP</b>��<b><font size=+1><font color=#$mojiiro3>$kaihuku</font></font></b>�񕜂����I
HTM
}
&charadatawrt;
&fieldform;

} elsif ( $in{mahou} eq "4"){
	if ( $champ < 7) {
print <<"HTM";
<b>TP</b>������Ȃ��ׁA<br>
<b>�n�C�q�[�����O</b>���g���Ȃ������B
HTM

	} elsif ( $chahp == $chastats[9] ){
print <<"HTM";
<b>����HP�����^���ׁ̈A<br>
�n�C�q�[�����O���g�p���Ă��Ӗ�������܂���B</b>
HTM

		} else {
$chahp = $chastats[9];
$champ -=7;
			if ( $chahp > $chastats[9] ) {
			$chahp = $chastats[9];
			}

print <<"HTM";
<font color=#$chamoji><b>$chaname</b></font>��<b>�n�C�q�[�����O</b>���������I<br>
<b>HP</b>��<b><font size=+1><font color=#$mojiiro3>�S��</font></font></b>�����I
HTM
}
&charadatawrt;
&fieldform;

} elsif ( $in{mahou} eq "3"){
	if ( $champ < 4) {
print <<"HTM";
<b>TP</b>������Ȃ��ׁA<br>
<b>�X�L�b�v</b>���g���Ȃ������B
HTM

		} else {
$chacount -=5;
$champ -=4;


print <<"HTM";
<font color=#$chamoji><b>$chaname</b></font>��<b>�X�L�b�v</b>�̓��Z���g�p�����I<br>
�ӂ肩�烂���X�^�[�̋C�z���������I
HTM
}
&charadatawrt;
&fieldform;




} elsif ( $in{mahou} eq "5"){
	if ( $champ < 10) {
print <<"HTM";
<b>TP</b>������Ȃ��ׁA<br>
<b>�p���[�A�b�v</b>���g���Ȃ������B
HTM

} elsif ( $kougekit > 0 ){
print <<"HTM";
<b>���ɂ��̓��Z�͔������Ă��܂��B<br></b>
HTM
		} else {
$champ -=10;
$kougeki += $chastats[2];
$kougekit = int(rand(5)) + 5;
print <<"HTM";
<font color=#$chamoji><b>$chaname</b></font>��<b>�p���[�A�b�v</b>�̓��Z���g�p�����I<br>
�݂�݂邤���ɋؗ͂��������Ă����I<br>
<FONT COLOR=GREEN><B>���΂炭�̊ԁA�U���͂��㏸���܂��B</B></FONT>
HTM
}
&charadatawrt;
&fieldform;


} elsif ( $in{mahou} eq "6"){
	if ( $champ < 10) {
print <<"HTM";
<b>TP</b>������Ȃ��ׁA<br>
<b>�V�[���h�A�b�v</b>���g���Ȃ������B
HTM

} elsif ( $mamorit > 0 ){
print <<"HTM";
<b>���ɂ��̓��Z�͔������Ă��܂��B<br></b>
HTM
		} else {
$champ -=10;
$acagari = int($chastats[1] / 4); 
$mamori += $acagari;
$mamorit = int(rand(5)) + 5;
print <<"HTM";
<font color=#$chamoji><b>$chaname</b></font>��<b>�V�[���h�A�b�v</b>�̓��Z���g�p�����I<br>
�݂�݂邤���ɋؗ͂��������Ă����I<br>
<FONT COLOR=GREEN><B>���΂炭�̊ԁA�h��͂��㏸���܂��B</B></FONT>
HTM
}
&charadatawrt;
&fieldform;


} elsif ( $in{mahou} eq "7"){
	if ( $champ < 20) {
print <<"HTM";
<b>TP</b>������Ȃ��ׁA<br>
<b>�P���̕�</b>���g���Ȃ������B
HTM

} elsif ( $houou > 0 ){
print <<"HTM";
<b>���ɂ��̓��Z�͔������Ă��܂��B<br></b>
HTM
		} else {
$champ -=20;
$houou = int(rand($chastats[4]) / 2) + 5;
print <<"HTM";
<font color=#$chamoji><b>$chaname</b></font>��<b>�P���̕�</b>���g�p�����I<br>
�P���̍���$chaname�̐g�̂ɏh�����I<br>
<FONT COLOR=GREEN><B>���΂炭�̊ԁA�U���񐔂��P�񑝂��܂��B</B></FONT>
HTM
}
&charadatawrt;
&fieldform;


} elsif ( $in{mahou} eq "8"){
	if ( $champ < 30) {
print <<"HTM";
<b>TP</b>������Ȃ��ׁA<br>
<b>���o�C�u</b>���g���Ȃ������B
HTM

} elsif ( $ribaibu > 0 ){
print <<"HTM";
<b>���̓��Z�̌��ʂ͎������Ă��܂��B<br></b>
HTM
		} else {
$champ -=30;
$ribaibu = int(rand($chastats[4])) + 10;
print <<"HTM";
<font color=#$chamoji><b>$chaname</b></font>��<b>���o�C�u</b>���g�p�����I<br>
���Ȃ鍰��$chaname�̐g�̂ɏh�����I<br>
<FONT COLOR=GREEN><B>��x�A���S���Ă��������܂��B</B></FONT>
HTM
}
&charadatawrt;
&fieldform;



} elsif ( $in{mahou} eq "2"){
	if ( $champ < 12) {
print <<"HTM";
<b>TP</b>������Ȃ��ׁA<br>
<b>�e���|�[�g</b>���g���Ȃ������B
HTM

		} else {
$champ -=12;

&charadatawrt;
print <<"HTM";
<font color=#$chamoji><b>$chaname</b></font>��<b>�e���|�[�g</b>���������I<br><br>
HTM

$chaplace = 0;
&charadatawrt;
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="0" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="$zone[$itemstats2] �֏u�Ԉړ�"><br></td></tr></table>
</form>
HTM
}



} elsif ( $in{useitem} eq "7"){
	if ($flag20 ) {
print <<"HTM";
�u�g�p������Z��I�����Ă��������B�v<br><br>
<form method="post" action="./$zonecgi">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="71" name="usemahou">
<input type=hidden value="1" name="mahou">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="�@�q�[�����O�@" size=30><font color=red><font size=-1>�@<b>����TP�F3</b>�iHP���񕜁j
</form>
HTM
	}

	if ($flag19 ) {
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="71" name="usemahou">
<input type=hidden value="3" name="mahou">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="�@ �X�L�b�v �@" size=30><font color=red><font size=-1>�@<b>����TP�F4</b>�i�K��퓬�񐔂������j
</form>
HTM
	}

	if ($flag18 ) {
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="71" name="usemahou">
<input type=hidden value="2" name="mahou">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="�@�e���|�[�g�@" size=30><font color=red><font size=-1>�@<b>����TP�F12</b>�i�X�p�j�A�[�g�̊X�֋A�ҁj
</form>
HTM
	}

	if ($flag17 ) {
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="71" name="usemahou">
<input type=hidden value="4" name="mahou">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="�n�C�q�[�����O" size=30><font color=red><font size=-1>�@<b>����TP�F7</b>�iHP��S�񕜁j
</form>
HTM
	}

	if ($flag16 ) {
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="71" name="usemahou">
<input type=hidden value="6" name="mahou">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="�V�[���h�A�b�v" size=30><font color=red><font size=-1>�@<b>����TP�F10</b>�i�퓬���̖h��͂��グ��j
</form>
HTM
	}

	if ($flag15 ) {
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="71" name="usemahou">
<input type=hidden value="5" name="mahou">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value=" �p���[�A�b�v " size=30><font color=red><font size=-1>�@<b>����TP�F10</b>�i�퓬���̍U���͂��グ��j
</form>
HTM
	}

	if ($flag14 ) {
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="71" name="usemahou">
<input type=hidden value="7" name="mahou">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="�@�P���̕��@" size=30><font color=red><font size=-1>�@<b>����TP�F20</b>�i�퓬���̍U���񐔂��P�񑝂₷�j
</form>
HTM
	}

	if ($flag13 ) {
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="71" name="usemahou">
<input type=hidden value="8" name="mahou">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="�@ ���o�C�u �@" size=30><font color=red><font size=-1>�@<b>����TP�F30</b>�i�P�x�������S���Ă������j
</form>
HTM
	}

&zoneform;




} elsif ( $in{useitem} eq "3"){
#�@�y�b�g�̑���ύX����
print <<"HTM";
�y�b�g�̑����ύX�ł��܂��B<br>
1�ԖځF�v���[���[����ɍs�����܂��B<br>
2�ԖځF�v���[���[�̍U����ɍs�����܂��B<br>
3�ԖځF�G�̍U����ɍs�����܂��B<br>
<form method="post" action="./$zonecgi">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="31" name="useitem">
<input type=hidden value="$chapass" name="usrpass">
<table border=0><tr><td>
<input type=radio value="0" name="tairetu1" checked>1�Ԗ�<br>
<input type=radio value="1" name="tairetu1">2�Ԗ�<br>
<input type=radio value="2" name="tairetu1">3�Ԗ�<br>
</td><td width=40 align=center><font size=4><b>��</b></font></td><td>
<input type=radio value="0" name="tairetu2" checked>1�Ԗ�<br>
<input type=radio value="1" name="tairetu2">2�Ԗ�<br>
<input type=radio value="2" name="tairetu2">3�Ԗ�<br>
</td></tr></table>
<input type=submit value="�����ύX����" size=30>
</form>
HTM
&zoneform;
} elsif ( $in{useitem} eq "31"){
$karicode = $petcode[$in{tairetu1}];$karilvl = $petlv[$in{tairetu1}];
$kariname = $petname[$in{tairetu1}];$karikouka = $petkouka[$in{tairetu1}];
$kariritu = $petritu[$in{tairetu1}];$karikouka2 = $petkouka2[$in{tairetu1}];
$karipic = $petpic[$in{tairetu1}];$karieff = $peteff[$in{tairetu1}];
$kariexp = $petexp[$in{tairetu1}];$karinowexp = $petnowexp[$in{tairetu1}];
$petcode[$in{tairetu1}] = $petcode[$in{tairetu2}];
$petlv[$in{tairetu1}] = $petlv[$in{tairetu2}];
$petname[$in{tairetu1}] = $petname[$in{tairetu2}];
$petritu[$in{tairetu1}] = $petritu[$in{tairetu2}];
$petkouka[$in{tairetu1}] = $petkouka[$in{tairetu2}];
$petkouka2[$in{tairetu1}] = $petkouka2[$in{tairetu2}];
$petpic[$in{tairetu1}] = $petpic[$in{tairetu2}];
$peteff[$in{tairetu1}] = $peteff[$in{tairetu2}];
$petexp[$in{tairetu1}] = $petexp[$in{tairetu2}];
$petnowexp[$in{tairetu1}] = $petnowexp[$in{tairetu2}];
$petcode[$in{tairetu2}] = $karicode;$petlv[$in{tairetu2}] = $karilvl;
$petname[$in{tairetu2}] = $kariname;$petritu[$in{tairetu2}] = $kariritu;
$petkouka[$in{tairetu2}] = $karikouka;$petkouka2[$in{tairetu2}] = $karikouka2;
$petpic[$in{tairetu2}] = $karipic;$peteff[$in{tairetu2}] = $karieff;
$petexp[$in{tairetu2}] = $kariexp;$petnowexp[$in{tairetu2}] = $karinowexp;
print "<b>�����ύX���܂����B</b><br><br>";
&charadatawrt;
&fieldform;





} else {
&fieldform;
}




#�@�J�E���g�_�E������
sub fieldform {
	if ( $chacount == 5 || $in{useitem} eq "1a" || $in{useitem} eq "2a" || $in{useitem} eq "31") {
		$timesa = $nexttime;
	}
print <<"HTM";
<SCRIPT LANGUAGE="JavaScript">
<!--
	var start=new Date();
	start=Date.parse(start)/1000;
	var counts=$nexttime;
	function CountDown(){
		var now=new Date();
		now=Date.parse(now)/1000;
		var x=parseInt(counts-(now-start),10);
		if(document.form1){document.form1.clock.value = x;}
		if(x>0){
			timerID=setTimeout("CountDown()", 100)
		}else{
			document.form1.clock.value = "0K!";
		}
	}
//-->
</SCRIPT>
<FORM NAME="form1"><INPUT TYPE="text" NAME="clock" SIZE="2" VALUE="$timesa" style="color: white;background-color: dimgray;border-color: black;"></form>
HTM


	if ($newtegami > 0) {


}

		if ( $champ <= 0) {
print <<"HTM";
<font color=red><font size=-1><b>(!�x��!�j</b><br>TP��0�ɂȂ��Ă��܂��I<br>
<nobr>���̂܂ܐ퓬������ƁA<br>HP���������܂��I</font></font><br><br>
HTM
}



		if ( $chahp <= $autop && $bpo == "1" && $potion eq "�|�[�V����" && $chaitem[1] eq "�|�[�V����" ) {
$chahp += 100;
$bpo = "0";
	if ( $chaeff[1] == 1 ) { $chaitem[1] = $chaeff[1] = $chasetumei[1] = "";
	} else { $chaeff[1] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>�|�[�V�������g�p���܂����B<br>
�|�[�V�����́A�c�� 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[1]</font></font></b> <font color=black>�ł��B</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "�|�[�V����" && $chaitem[2] eq "�|�[�V����" ) {
$chahp += 100;
$bpo = "0";
	if ( $chaeff[2] == 1 ) { $chaitem[2] = $chaeff[2] = $chasetumei[2] = "";
	} else { $chaeff[2] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>�|�[�V�������g�p���܂����B<br>
�|�[�V�����́A�c�� 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[2]</font></font></b> <font color=black>�ł��B</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "�|�[�V����" && $chaitem[3] eq "�|�[�V����" ) {
$chahp += 100;
$bpo = "0";
	if ( $chaeff[3] == 1 ) { $chaitem[3] = $chaeff[3] = $chasetumei[3] = "";
	} else { $chaeff[3] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>�|�[�V�������g�p���܂����B<br>
�|�[�V�����́A�c�� 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[3]</font></font></b> <font color=black>�ł��B</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "�|�[�V����" && $chaitem[4] eq "�|�[�V����" ) {
$chahp += 100;
$bpo = "0";
	if ( $chaeff[4] == 1 ) { $chaitem[4] = $chaeff[4] = $chasetumei[4] = "";
	} else { $chaeff[4] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>�|�[�V�������g�p���܂����B<br>
�|�[�V�����́A�c�� 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[4]</font></font></b> <font color=black>�ł��B</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "�|�[�V����" && $chaitem[5] eq "�|�[�V����" ) {
$chahp += 100;
$bpo = "0";
	if ( $chaeff[5] == 1 ) { $chaitem[5] = $chaeff[5] = $chasetumei[5] = "";
	} else { $chaeff[5] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>�|�[�V�������g�p���܂����B<br>
�|�[�V�����́A�c�� 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[5]</font></font></b> <font color=black>�ł��B</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "�|�[�V����" && $chaitem[6] eq "�|�[�V����" ) {
$chahp += 100;
$bpo = "0";
	if ( $chaeff[6] == 1 ) { $chaitem[6] = $chaeff[6] = $chasetumei[6] = "";
	} else { $chaeff[6] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>�|�[�V�������g�p���܂����B<br>
�|�[�V�����́A�c�� 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[6]</font></font></b> <font color=black>�ł��B</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "�|�[�V����" && $chaitem[7] eq "�|�[�V����" ) {
$chahp += 100;
$bpo = "0";
	if ( $chaeff[7] == 1 ) { $chaitem[7] = $chaeff[7] = $chasetumei[7] = "";
	} else { $chaeff[7] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>�|�[�V�������g�p���܂����B<br>
�|�[�V�����́A�c�� 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[7]</font></font></b> <font color=black>�ł��B</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "�|�[�V����" && $chaitem[8] eq "�|�[�V����" ) {
$chahp += 100;
$bpo = "0";
	if ( $chaeff[8] == 1 ) { $chaitem[8] = $chaeff[8] = $chasetumei[8] = "";
	} else { $chaeff[8] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>�|�[�V�������g�p���܂����B<br>
�|�[�V�����́A�c�� 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[8]</font></font></b> <font color=black>�ł��B</font></font>
</font><br><br>
HTM
&charadatawrt;
}



		if ( $chahp <= $autop && $bpo == "1" && $potion eq "�~�h���|�[�V����" && $chaitem[1] eq "�~�h���|�[�V����" ) {
$chahp += 300;
$bpo = "0";
	if ( $chaeff[1] == 1 ) { $chaitem[1] = $chaeff[1] = $chasetumei[1] = "";
	} else { $chaeff[1] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>�~�h���|�[�V�������g�p���܂����B<br>
�~�h���|�[�V�����́A�c�� 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[1]</font></font></b> <font color=black>�ł��B</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "�~�h���|�[�V����" && $chaitem[2] eq "�~�h���|�[�V����" ) {
$chahp += 300;
$bpo = "0";
	if ( $chaeff[2] == 1 ) { $chaitem[2] = $chaeff[2] = $chasetumei[2] = "";
	} else { $chaeff[2] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>�~�h���|�[�V�������g�p���܂����B<br>
�~�h���|�[�V�����́A�c�� 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[2]</font></font></b> <font color=black>�ł��B</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "�~�h���|�[�V����" && $chaitem[3] eq "�~�h���|�[�V����" ) {
$chahp += 300;
$bpo = "0";
	if ( $chaeff[3] == 1 ) { $chaitem[3] = $chaeff[3] = $chasetumei[3] = "";
	} else { $chaeff[3] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>�~�h���|�[�V�������g�p���܂����B<br>
�~�h���|�[�V�����́A�c�� 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[3]</font></font></b> <font color=black>�ł��B</font></font>
</font><br><br>
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "�~�h���|�[�V����" && $chaitem[4] eq "�~�h���|�[�V����" ) {
$chahp += 300;
$bpo = "0";
	if ( $chaeff[4] == 1 ) { $chaitem[4] = $chaeff[4] = $chasetumei[4] = "";
	} else { $chaeff[4] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>�~�h���|�[�V�������g�p���܂����B<br>
�~�h���|�[�V�����́A�c�� 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[4]</font></font></b> <font color=black>�ł��B</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "�~�h���|�[�V����" && $chaitem[5] eq "�~�h���|�[�V����" ) {
$chahp += 300;
$bpo = "0";
	if ( $chaeff[5] == 1 ) { $chaitem[5] = $chaeff[5] = $chasetumei[5] = "";
	} else { $chaeff[5] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>�~�h���|�[�V�������g�p���܂����B<br>
�~�h���|�[�V�����́A�c�� 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[5]</font></font></b> <font color=black>�ł��B</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "�~�h���|�[�V����" && $chaitem[6] eq "�~�h���|�[�V����" ) {
$chahp += 300;
$bpo = "0";
	if ( $chaeff[6] == 1 ) { $chaitem[6] = $chaeff[6] = $chasetumei[6] = "";
	} else { $chaeff[6] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>�~�h���|�[�V�������g�p���܂����B<br>
�~�h���|�[�V�����́A�c�� 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[6]</font></font></b> <font color=black>�ł��B</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "�~�h���|�[�V����" && $chaitem[7] eq "�~�h���|�[�V����" ) {
$chahp += 300;
$bpo = "0";
	if ( $chaeff[7] == 1 ) { $chaitem[7] = $chaeff[7] = $chasetumei[7] = "";
	} else { $chaeff[7] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>�~�h���|�[�V�������g�p���܂����B<br>
�~�h���|�[�V�����́A�c�� 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[7]</font></font></b> <font color=black>�ł��B</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "�~�h���|�[�V����" && $chaitem[8] eq "�~�h���|�[�V����" ) {
$chahp += 300;
$bpo = "0";
	if ( $chaeff[8] == 1 ) { $chaitem[8] = $chaeff[8] = $chasetumei[8] = "";
	} else { $chaeff[8] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>�~�h���|�[�V�������g�p���܂����B<br>
�~�h���|�[�V�����́A�c�� 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[8]</font></font></b> <font color=black>�ł��B</font></font>
</font><br><br>
HTM
&charadatawrt;
}


		if ( $chahp <= $autop && $bpo == "1" && $potion eq "�n�C�|�[�V����" && $chaitem[1] eq "�n�C�|�[�V����" ) {
$chahp += 700;
$bpo = "0";
	if ( $chaeff[1] == 1 ) { $chaitem[1] = $chaeff[1] = $chasetumei[1] = "";
	} else { $chaeff[1] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>�n�C�|�[�V�������g�p���܂����B<br>
�n�C�|�[�V�����́A�c�� 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[1]</font></font></b> <font color=black>�ł��B</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "�n�C�|�[�V����" && $chaitem[2] eq "�n�C�|�[�V����" ) {
$chahp += 700;
$bpo = "0";
	if ( $chaeff[2] == 1 ) { $chaitem[2] = $chaeff[2] = $chasetumei[2] = "";
	} else { $chaeff[2] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>�n�C�|�[�V�������g�p���܂����B<br>
�n�C�|�[�V�����́A�c�� 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[2]</font></font></b> <font color=black>�ł��B</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "�n�C�|�[�V����" && $chaitem[3] eq "�n�C�|�[�V����" ) {
$chahp += 700;
$bpo = "0";
	if ( $chaeff[3] == 1 ) { $chaitem[3] = $chaeff[3] = $chasetumei[3] = "";
	} else { $chaeff[3] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>�n�C�|�[�V�������g�p���܂����B<br>
�n�C�|�[�V�����́A�c�� 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[3]</font></font></b> <font color=black>�ł��B</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "�n�C�|�[�V����" && $chaitem[4] eq "�n�C�|�[�V����" ) {
$chahp += 700;
$bpo = "0";
	if ( $chaeff[4] == 1 ) { $chaitem[4] = $chaeff[4] = $chasetumei[4] = "";
	} else { $chaeff[4] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>�n�C�|�[�V�������g�p���܂����B<br>
�n�C�|�[�V�����́A�c�� 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[4]</font></font></b> <font color=black>�ł��B</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "�n�C�|�[�V����" && $chaitem[5] eq "�n�C�|�[�V����" ) {
$chahp += 700;
$bpo = "0";
	if ( $chaeff[5] == 1 ) { $chaitem[5] = $chaeff[5] = $chasetumei[5] = "";
	} else { $chaeff[5] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>�n�C�|�[�V�������g�p���܂����B<br>
�n�C�|�[�V�����́A�c�� 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[5]</font></font></b> <font color=black>�ł��B</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "�n�C�|�[�V����" && $chaitem[6] eq "�n�C�|�[�V����" ) {
$chahp += 700;
$bpo = "0";
	if ( $chaeff[6] == 1 ) { $chaitem[6] = $chaeff[6] = $chasetumei[6] = "";
	} else { $chaeff[6] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>�n�C�|�[�V�������g�p���܂����B<br>
�n�C�|�[�V�����́A�c�� 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[6]</font></font></b> <font color=black>�ł��B</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "�n�C�|�[�V����" && $chaitem[7] eq "�n�C�|�[�V����" ) {
$chahp += 700;
$bpo = "0";
	if ( $chaeff[7] == 1 ) { $chaitem[7] = $chaeff[7] = $chasetumei[7] = "";
	} else { $chaeff[7] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>�n�C�|�[�V�������g�p���܂����B<br>
�n�C�|�[�V�����́A�c�� 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[7]</font></font></b> <font color=black>�ł��B</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "�n�C�|�[�V����" && $chaitem[8] eq "�n�C�|�[�V����" ) {
$chahp += 700;
$bpo = "0";
	if ( $chaeff[8] == 1 ) { $chaitem[8] = $chaeff[8] = $chasetumei[8] = "";
	} else { $chaeff[8] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>�n�C�|�[�V�������g�p���܂����B<br>
�n�C�|�[�V�����́A�c�� 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[8]</font></font></b> <font color=black>�ł��B</font></font>
</font><br><br>
HTM
&charadatawrt;
}


		if ( $chahp <= $autop && $bpo == "1" && $potion eq "�G�N�X�|�[�V����" && $chaitem[1] eq "�G�N�X�|�[�V����" ) {
$chahp += 1200;
$bpo = "0";
	if ( $chaeff[1] == 1 ) { $chaitem[1] = $chaeff[1] = $chasetumei[1] = "";
	} else { $chaeff[1] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>�G�N�X�|�[�V�������g�p���܂����B<br>
�G�N�X�|�[�V�����́A�c�� 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[1]</font></font></b> <font color=black>�ł��B</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "�G�N�X�|�[�V����" && $chaitem[2] eq "�G�N�X�|�[�V����" ) {
$chahp += 1200;
$bpo = "0";
	if ( $chaeff[2] == 1 ) { $chaitem[2] = $chaeff[2] = $chasetumei[2] = "";
	} else { $chaeff[2] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>�G�N�X�|�[�V�������g�p���܂����B<br>
�G�N�X�|�[�V�����́A�c�� 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[2]</font></font></b> <font color=black>�ł��B</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "�G�N�X�|�[�V����" && $chaitem[3] eq "�G�N�X�|�[�V����" ) {
$chahp += 1200;
$bpo = "0";
	if ( $chaeff[3] == 1 ) { $chaitem[3] = $chaeff[3] = $chasetumei[3] = "";
	} else { $chaeff[3] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>�G�N�X�|�[�V�������g�p���܂����B<br>
�G�N�X�|�[�V�����́A�c�� 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[3]</font></font></b> <font color=black>�ł��B</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "�G�N�X�|�[�V����" && $chaitem[4] eq "�G�N�X�|�[�V����" ) {
$chahp += 1200;
$bpo = "0";
	if ( $chaeff[4] == 1 ) { $chaitem[4] = $chaeff[4] = $chasetumei[4] = "";
	} else { $chaeff[4] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>�G�N�X�|�[�V�������g�p���܂����B<br>
�G�N�X�|�[�V�����́A�c�� 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[4]</font></font></b> <font color=black>�ł��B</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "�G�N�X�|�[�V����" && $chaitem[5] eq "�G�N�X�|�[�V����" ) {
$chahp += 1200;
$bpo = "0";
	if ( $chaeff[5] == 1 ) { $chaitem[5] = $chaeff[5] = $chasetumei[5] = "";
	} else { $chaeff[5] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>�G�N�X�|�[�V�������g�p���܂����B<br>
�G�N�X�|�[�V�����́A�c�� 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[5]</font></font></b> <font color=black>�ł��B</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "�G�N�X�|�[�V����" && $chaitem[6] eq "�G�N�X�|�[�V����" ) {
$chahp += 1200;
$bpo = "0";
	if ( $chaeff[6] == 1 ) { $chaitem[6] = $chaeff[6] = $chasetumei[6] = "";
	} else { $chaeff[6] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>�G�N�X�|�[�V�������g�p���܂����B<br>
�G�N�X�|�[�V�����́A�c�� 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[6]</font></font></b> <font color=black>�ł��B</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "�G�N�X�|�[�V����" && $chaitem[7] eq "�G�N�X�|�[�V����" ) {
$chahp += 1200;
$bpo = "0";
	if ( $chaeff[7] == 1 ) { $chaitem[7] = $chaeff[7] = $chasetumei[7] = "";
	} else { $chaeff[7] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>�G�N�X�|�[�V�������g�p���܂����B<br>
�G�N�X�|�[�V�����́A�c�� 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[7]</font></font></b> <font color=black>�ł��B</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "�G�N�X�|�[�V����" && $chaitem[8] eq "�G�N�X�|�[�V����" ) {
$chahp += 1200;
$bpo = "0";
	if ( $chaeff[8] == 1 ) { $chaitem[8] = $chaeff[8] = $chasetumei[8] = "";
	} else { $chaeff[8] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>�G�N�X�|�[�V�������g�p���܂����B<br>
�G�N�X�|�[�V�����́A�c�� 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[8]</font></font></b> <font color=black>�ł��B</font></font>
</font><br><br>
HTM
&charadatawrt;
}



		if ( $chahp <= $autop && $bpo == "1" && $potion eq "���K�G���N�T�[" && $chaitem[1] eq "���K�G���N�T�[" ) {
$chahp += 1800;
$bpo = "0";
	if ( $chaeff[1] == 1 ) { $chaitem[1] = $chaeff[1] = $chasetumei[1] = "";
	} else { $chaeff[1] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>���K�G���N�T�[���g�p���܂����B<br>
���K�G���N�T�[�́A�c�� 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[1]</font></font></b> <font color=black>�ł��B</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "���K�G���N�T�[" && $chaitem[2] eq "���K�G���N�T�[" ) {
$chahp += 1800;
$bpo = "0";
	if ( $chaeff[2] == 1 ) { $chaitem[2] = $chaeff[2] = $chasetumei[2] = "";
	} else { $chaeff[2] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>���K�G���N�T�[���g�p���܂����B<br>
���K�G���N�T�[�́A�c�� 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[2]</font></font></b> <font color=black>�ł��B</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "���K�G���N�T�[" && $chaitem[3] eq "���K�G���N�T�[" ) {
$chahp += 1800;
$bpo = "0";
	if ( $chaeff[3] == 1 ) { $chaitem[3] = $chaeff[3] = $chasetumei[3] = "";
	} else { $chaeff[3] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>���K�G���N�T�[���g�p���܂����B<br>
���K�G���N�T�[�́A�c�� 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[3]</font></font></b> <font color=black>�ł��B</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "���K�G���N�T�[" && $chaitem[4] eq "���K�G���N�T�[" ) {
$chahp += 1800;
$bpo = "0";
	if ( $chaeff[4] == 1 ) { $chaitem[4] = $chaeff[4] = $chasetumei[4] = "";
	} else { $chaeff[4] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>���K�G���N�T�[���g�p���܂����B<br>
���K�G���N�T�[�́A�c�� 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[4]</font></font></b> <font color=black>�ł��B</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "���K�G���N�T�[" && $chaitem[5] eq "���K�G���N�T�[" ) {
$chahp += 1800;
$bpo = "0";
	if ( $chaeff[5] == 1 ) { $chaitem[5] = $chaeff[5] = $chasetumei[5] = "";
	} else { $chaeff[5] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>���K�G���N�T�[���g�p���܂����B<br>
���K�G���N�T�[�́A�c�� 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[5]</font></font></b> <font color=black>�ł��B</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "���K�G���N�T�[" && $chaitem[6] eq "���K�G���N�T�[" ) {
$chahp += 1800;
$bpo = "0";
	if ( $chaeff[6] == 1 ) { $chaitem[6] = $chaeff[6] = $chasetumei[6] = "";
	} else { $chaeff[6] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>���K�G���N�T�[���g�p���܂����B<br>
���K�G���N�T�[�́A�c�� 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[6]</font></font></b> <font color=black>�ł��B</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "���K�G���N�T�[" && $chaitem[7] eq "���K�G���N�T�[" ) {
$chahp += 1800;
$bpo = "0";
	if ( $chaeff[7] == 1 ) { $chaitem[7] = $chaeff[7] = $chasetumei[7] = "";
	} else { $chaeff[7] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>���K�G���N�T�[���g�p���܂����B<br>
���K�G���N�T�[�́A�c�� 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[7]</font></font></b> <font color=black>�ł��B</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "���K�G���N�T�[" && $chaitem[8] eq "���K�G���N�T�[" ) {
$chahp += 1800;
$bpo = "0";
	if ( $chaeff[8] == 1 ) { $chaitem[8] = $chaeff[8] = $chasetumei[8] = "";
	} else { $chaeff[8] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>���K�G���N�T�[���g�p���܂����B<br>
���K�G���N�T�[�́A�c�� 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[8]</font></font></b> <font color=black>�ł��B</font></font>
</font><br><br>
HTM
&charadatawrt;
}


		if ( $chahp <= $autop && $bpo == "1" && $potion eq "�M�K�G���N�T�[" && $chaitem[1] eq "�M�K�G���N�T�[" ) {
$chahp += 2400;
$bpo = "0";
	if ( $chaeff[1] == 1 ) { $chaitem[1] = $chaeff[1] = $chasetumei[1] = "";
	} else { $chaeff[1] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>�M�K�G���N�T�[���g�p���܂����B<br>
�M�K�G���N�T�[�́A�c�� 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[1]</font></font></b> <font color=black>�ł��B</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "�M�K�G���N�T�[" && $chaitem[2] eq "�M�K�G���N�T�[" ) {
$chahp += 2400;
$bpo = "0";
	if ( $chaeff[2] == 1 ) { $chaitem[2] = $chaeff[2] = $chasetumei[2] = "";
	} else { $chaeff[2] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>�M�K�G���N�T�[���g�p���܂����B<br>
�M�K�G���N�T�[�́A�c�� 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[2]</font></font></b> <font color=black>�ł��B</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "�M�K�G���N�T�[" && $chaitem[3] eq "�M�K�G���N�T�[" ) {
$chahp += 2400;
$bpo = "0";
	if ( $chaeff[3] == 1 ) { $chaitem[3] = $chaeff[3] = $chasetumei[3] = "";
	} else { $chaeff[3] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>�M�K�G���N�T�[���g�p���܂����B<br>
�M�K�G���N�T�[�́A�c�� 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[3]</font></font></b> <font color=black>�ł��B</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "�M�K�G���N�T�[" && $chaitem[4] eq "�M�K�G���N�T�[" ) {
$chahp += 2400;
$bpo = "0";
	if ( $chaeff[4] == 1 ) { $chaitem[4] = $chaeff[4] = $chasetumei[4] = "";
	} else { $chaeff[4] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>�M�K�G���N�T�[���g�p���܂����B<br>
�M�K�G���N�T�[�́A�c�� 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[4]</font></font></b> <font color=black>�ł��B</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "�M�K�G���N�T�[" && $chaitem[5] eq "�M�K�G���N�T�[" ) {
$chahp += 2400;
$bpo = "0";
	if ( $chaeff[5] == 1 ) { $chaitem[5] = $chaeff[5] = $chasetumei[5] = "";
	} else { $chaeff[5] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>�M�K�G���N�T�[���g�p���܂����B<br>
�M�K�G���N�T�[�́A�c�� 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[5]</font></font></b> <font color=black>�ł��B</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "�M�K�G���N�T�[" && $chaitem[6] eq "�M�K�G���N�T�[" ) {
$chahp += 2400;
$bpo = "0";
	if ( $chaeff[6] == 1 ) { $chaitem[6] = $chaeff[6] = $chasetumei[6] = "";
	} else { $chaeff[6] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>�M�K�G���N�T�[���g�p���܂����B<br>
�M�K�G���N�T�[�́A�c�� 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[6]</font></font></b> <font color=black>�ł��B</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "�M�K�G���N�T�[" && $chaitem[7] eq "�M�K�G���N�T�[" ) {
$chahp += 2400;
$bpo = "0";
	if ( $chaeff[7] == 1 ) { $chaitem[7] = $chaeff[7] = $chasetumei[7] = "";
	} else { $chaeff[7] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>�M�K�G���N�T�[���g�p���܂����B<br>
�M�K�G���N�T�[�́A�c�� 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[7]</font></font></b> <font color=black>�ł��B</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "�M�K�G���N�T�[" && $chaitem[8] eq "�M�K�G���N�T�[" ) {
$chahp += 2400;
$bpo = "0";
	if ( $chaeff[8] == 1 ) { $chaitem[8] = $chaeff[8] = $chasetumei[8] = "";
	} else { $chaeff[8] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>�M�K�G���N�T�[���g�p���܂����B<br>
�M�K�G���N�T�[�́A�c�� 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[8]</font></font></b> <font color=black>�ł��B</font></font>
</font><br><br>
HTM
&charadatawrt;
}


		if ( $chahp <= $autop && $bpo == "1" && $potion eq "�e���G���N�T�[" && $chaitem[1] eq "�e���G���N�T�[" ) {
$chahp += 3000;
$bpo = "0";
	if ( $chaeff[1] == 1 ) { $chaitem[1] = $chaeff[1] = $chasetumei[1] = "";
	} else { $chaeff[1] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>�e���G���N�T�[���g�p���܂����B<br>
�e���G���N�T�[�́A�c�� 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[1]</font></font></b> <font color=black>�ł��B</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "�e���G���N�T�[" && $chaitem[2] eq "�e���G���N�T�[" ) {
$chahp += 3000;
$bpo = "0";
	if ( $chaeff[2] == 1 ) { $chaitem[2] = $chaeff[2] = $chasetumei[2] = "";
	} else { $chaeff[2] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>�e���G���N�T�[���g�p���܂����B<br>
�e���G���N�T�[�́A�c�� 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[2]</font></font></b> <font color=black>�ł��B</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "�e���G���N�T�[" && $chaitem[3] eq "�e���G���N�T�[" ) {
$chahp += 3000;
$bpo = "0";
	if ( $chaeff[3] == 1 ) { $chaitem[3] = $chaeff[3] = $chasetumei[3] = "";
	} else { $chaeff[3] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>�e���G���N�T�[���g�p���܂����B<br>
�e���G���N�T�[�́A�c�� 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[3]</font></font></b> <font color=black>�ł��B</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "�e���G���N�T�[" && $chaitem[4] eq "�e���G���N�T�[" ) {
$chahp += 3000;
$bpo = "0";
	if ( $chaeff[4] == 1 ) { $chaitem[4] = $chaeff[4] = $chasetumei[4] = "";
	} else { $chaeff[4] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>�e���G���N�T�[���g�p���܂����B<br>
�e���G���N�T�[�́A�c�� 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[4]</font></font></b> <font color=black>�ł��B</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "�e���G���N�T�[" && $chaitem[5] eq "�e���G���N�T�[" ) {
$chahp += 3000;
$bpo = "0";
	if ( $chaeff[5] == 1 ) { $chaitem[5] = $chaeff[5] = $chasetumei[5] = "";
	} else { $chaeff[5] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>�e���G���N�T�[���g�p���܂����B<br>
�e���G���N�T�[�́A�c�� 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[5]</font></font></b> <font color=black>�ł��B</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "�e���G���N�T�[" && $chaitem[6] eq "�e���G���N�T�[" ) {
$chahp += 3000;
$bpo = "0";
	if ( $chaeff[6] == 1 ) { $chaitem[6] = $chaeff[6] = $chasetumei[6] = "";
	} else { $chaeff[6] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>�e���G���N�T�[���g�p���܂����B<br>
�e���G���N�T�[�́A�c�� 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[6]</font></font></b> <font color=black>�ł��B</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "�e���G���N�T�[" && $chaitem[7] eq "�e���G���N�T�[" ) {
$chahp += 3000;
$bpo = "0";
	if ( $chaeff[7] == 1 ) { $chaitem[7] = $chaeff[7] = $chasetumei[7] = "";
	} else { $chaeff[7] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>�e���G���N�T�[���g�p���܂����B<br>
�e���G���N�T�[�́A�c�� 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[7]</font></font></b> <font color=black>�ł��B</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "�e���G���N�T�[" && $chaitem[8] eq "�e���G���N�T�[" ) {
$chahp += 3000;
$bpo = "0";
	if ( $chaeff[8] == 1 ) { $chaitem[8] = $chaeff[8] = $chasetumei[8] = "";
	} else { $chaeff[8] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>�e���G���N�T�[���g�p���܂����B<br>
�e���G���N�T�[�́A�c�� 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[8]</font></font></b> <font color=black>�ł��B</font></font>
</font><br><br>
HTM
&charadatawrt;
}


print <<"HTM";
<form method="post" action="./$battlecgi">
<onClick="window.location.replace>
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=hidden value="$chacount" name="count">
<input type=submit value="�@�@�@���@�G�@�@�@" size=30 onClick="this.disabled=true; this.value='       ��  �G       '; this.form.submit();">
</form>

<form method="post" action="./$zonecgi">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="1" name="useitem">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="�A�C�e�����g�p����" size=30 onClick="this.disabled=true; this.value='�A�C�e�����g�p����'; this.form.submit();">
</form>
HTM

	if ($flag20 ) {
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="7" name="useitem">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="�@���Z���g�p����@" size=30 onClick="this.disabled=true; this.value='  ���Z���g�p����  '; this.form.submit();">
</form>
HTM
}

print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="6" name="useitem">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="�A�C�e���𑕔�����" size=30 onClick="this.disabled=true; this.value='�A�C�e���𑕔�����'; this.form.submit();">
</form>

</td></tr></table></td><td width=30></td><td>
HTM


sub kouji {
open(NOW,">$maindir/kouji$bousikts");
flock(NOW,2);
	$ttt = 0;
	while ( $ttt < 50 ) {
		print NOW $res[$ttt] ;
		$ttt ++;
	}
flock(NOW,8);
close(NOW);
}



	if ( $chacount <= 0 ) {
print "���̃]�[���ֈړ���\�\\�ł��B<br>";

@movin = split(/\//,$move[$chaplace]);

		foreach $moved (@movin) {
			if ( $moved ne "" ) {
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="$moved" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="$zone[$moved]�@��" size=30 onClick="this.disabled=true; this.value='���҂���������'; this.form.submit();">
</form>
HTM
			}
		}
	} else {
print "���� <b><font size=7 color=#$mojiiro3>$chacount</font> �� </b><br>�@�̐퓬������ƈړ���\�\\�ł��B";
	}



}



print <<"HTM";
</td></tr></table><br><hr>
HTM

if ( $in{useitem} eq "1" || $in{useitem} eq "2" || $in{useitem} eq "3" || $in{useitem} eq "6" ||  $in{useitem} eq "21" || $in{riyou} eq "4" || $in{useitem} eq "7" || $in{useitem} eq "8" || $in{point} eq "1" || $in{point} eq "1a" || $in{point} eq "2" || $in{point} eq "2a" || $in{point} eq "3" || $in{point} eq "3a" || $in{point} eq "4" || $in{point} eq "4a" || $in{point} eq "3b" || $in{point} eq "2b" || $in{point} eq "1b" || $in{point} eq "4b" || $in{point} eq "1c" || $in{point} eq "1d" || $in{point} eq "2c" || $in{point} eq "2d" || $in{point} eq "3c" || $in{point} eq "3d" || $in{point} eq "4c" || $in{point} eq "4d" || $in{riyou} eq "61") { &itemtable;
} else {
print <<"HTM";
<SCRIPT language="JavaScript">
<!--
window.setTimeout('CountDown()',100);
//-->
</SCRIPT>
HTM
}
&pettukitable;









############################################

$playingkazu = @playing;
print <<"HTM";


<form method="post" action="./bar.cgi" target="sakaba">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value=" �`���b�g ">
<br></form>
HTM




require "./settei.cgi";
print <<"HTM";

<center><font size=4 color=#$mojiiro4><b><A NAME="end">�莆 �ꗗ</a></b></font><br>
(�ێ����Ԃ�3���ԁA���邢�͕ێ�������30����������Ǝ�����������܂�)$tegamicount
<table border=0 width=70%><tr><td>
HTM
$tegamicount = 0;
open(BAN,">>$maindir/$foldacha/tegami2_$chaid.tmp");
flock(BAN,2);
	open(BANN,"$maindir/$foldacha/tegami_$chaid$bousi2cha$bousikts");
		while ( $yuubin = <BANN> ) {
			if ( $tegamicount > 29 ) { last; }
($kako,$chanamez,$chamojiz,$tegami,$genzai2) = split(/\t/,$yuubin);
			if ( $now < $kako + (3*24*60*60) ) {

print "<hr><font color=#$chamojiz><b>$chanamez</b></font> �F $tegami <nobr>($genzai2)</nobr>\n";
		print BAN "$yuubin";
			}
$tegamicount ++;

		}
	close(BANN);

flock(BAN,8);
close(BAN);

rename("$maindir/$foldacha/tegami2_$chaid.tmp","$maindir/$foldacha/tegami_$chaid$bousi2cha$bousikts");


################################################

sub zoneform {
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="  �]�[����ʂ֖߂�  " onClick="this.disabled=true; this.value='  �]�[����ʂ֖߂�  '; this.form.submit();"><br></td></tr></table>
</form>
HTM
}



1;