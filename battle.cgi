#!/usr/bin/perl

#�@���T�[�o�[�̐ݒ�ɍ��킹�ĕύX���Ă��������B

#�@�X�e�[�^�X��
$statsname[2] = "�́iSTR)";$statsname[3] = "�f�����iAGI�j";$statsname[4] = "�m���iINT�j";$statsname[5] = "���́iCHA�j";
$statsname[6] = "�Αϐ��iSVF�j";$statsname[7] = "���ϐ��iSVC�j";$statsname[8] = "���ϐ��iSVM�j";

#########�@�ݒ�͂����܂Ł@##########

require "./settei.cgi";
require "./cgi-lib.pl";
&ReadParse;

&cookieget;
&ipblock;
&gaibublock;
&cookieset;
&hpsaisyo;
&charadataload;

require "$foldabattle/jobbattle$chaclass.pl";

if ( $in{boss} eq "" ) {$timesa = $now - $chajikan; } else { $timesa = $nexttime; }
if ( $timesa < $nexttime ) { &fuseisyori;exit; }

if ( $in{count} != $chacount ) { &fuseisyori;exit; }

#�@�����X�^�[�f�[�^�擾
open(MON,"$maindir/$monsfile/monster$chaplace$bousikts2");
@monster = <MON>;
close(MON);

	foreach $monsters ( @monster ) {
		($monspopp,$a) = split(/,/,$monsters);
		push(@monspo,$monspopp);
	}

foreach $monritu (@monspo) {
	$monrand = $monrand + $monritu;
}
# srand;
$monketu = int(rand($monrand));
$monnum = 0;
foreach $monritu (@monspo) {
	$monsuuji = $monsuuji + $monspo[$monnum];
	if ( $monketu < $monsuuji ) {
	last;
	}
	$monnum ++;
}
($monspop,$monsgif,$monsname,$monslvl,$monshp,$monsattack,$monsac,$monscha,$monssvf,$monssvc,$monssvm,$monsexp,$monsgold,$monskouka,$monsitem[0],$monsitem[1],$monsitem[2],$monsitem[3],$monsitem[4],$a) = split(/,/,$monster[$monnum]);
$battleturn = 1;
$mast = 0;
$monshp += $chalvl;
$monshpnow = $monshp;
$chahpnow = $chahp;
$chahpmax = $chastats[9] + $karistats[9];$pow = $chastats[0] + $karistats[0] + $kougeki;$ac = $chastats[1] + $karistats[1] + $mamori;$str = $chastats[2] + $karistats[2];
$agi = $chastats[3] + $karistats[3];$int = $chastats[4] + $karistats[4];$cha = $chastats[5] + $karistats[5];$svf = $chastats[6] + $karistats[6];$svc = $chastats[7] + $karistats[7];$svm = $chastats[8] + $karistats[8];
$lvlpoin = $monslvl - $chalvl;

if ( $lvlpoin < 0 ) { $lvlpoin = 0; }

print <<"HTM";
<SCRIPT LANGUAGE="JavaScript">
defaultStatus="�w���^�[���ځx���N���b�N����ƁA�퓬���ʂ܂ŒZ�k���܂��B";
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
                <center><B>MENU</B></center><P>
                �E<A HREF="#exit">���ʕ\\��<BR></a>
                �E<A HREF="$urlbbs" target="blank">�f����<BR></a>
                �E<a href="javascript:close()">�Q�[���I��</a>
            </TD>
        </TR>
    </TABLE>
</DIV>
<!--���j���[�p�^�O�����܂�-->
HTM

print <<"HTM";

<center><font size=6 color=#$mojiiro2><b>$monsname</b> �����ꂽ�I�I</font><hr><br>
HTM
if ( $in{boss} eq "" ) { $limit = $maxturn; } else { $limit = $maxturn; }

#�@�퓬����

while ( $battleturn <= $limit ) {
&deathchk;

print <<"HTM";
<table border=0><tr><td bgcolor=#$tableiro align=center><font size=4><nobr><b><center><A HREF="#exit"><font color=black>$battleturn �^�[����</font></a></b></nobr></font></td></tr><tr><td>
<table border=0>
HTM

if ($battleturn == 1 ) {
print <<"HTM";
<tr align=center valign="baseline"><td>
<img src="$maindir/$imgfile/$monsgif.gif"></td><td></td><td>
HTM
if($petcode[1] ne ""){ print "<img src=\"$maindir/$imgfile/$petpic[1].gif\" alt=\"$petname[1]\">";}
print "</td><td>";
&charaga;
print "</td><td>";
if($petcode[0] ne ""){ print "<img src=\"$maindir/$imgfile/$petpic[0].gif\" alt=\"$petname[0]\">";}
print "</td><td>";
if($petcode[2] ne ""){ print "<img src=\"$maindir/$imgfile/$petpic[2].gif\" alt=\"$petname[2]\">";}
print "</td></tr>";
} else {
print "<tr><td colspan=3 height=5></td></tr>";

}

$hpbarcha1 = int( ( $chahpnow / $chastats[9] ) * 150 );
if ( $hpbarcha1 != 150 ) {
$hpbarcha2 = 150 - $hpbarcha1;
$hpbardmg2 = "<img src=\"$maindir/$imgfile/hpbar2.gif\" width=$hpbarcha2 height=\"8\">";
}

$hpbarmon1 = int( ( $monshpnow / $monshp ) * 150 );
if ( $hpbarmon1 != 150 ) {
$hpbarmon2 = 150 - $hpbarmon1;
$hpbardmg1 = "<img src=\"$maindir/$imgfile/hpbar2.gif\" width=$hpbarmon2 height=\"8\">";
}

print <<"HTM";
<tr align=center><td>
<font size=4><nobr>$monsname</font></nobr></td><td width=20 rowspan=2><nobr><font size=4 color=#$mojiiro2><b>VS</b></font></nobr></td><td colspan=3><font size=4><nobr>$chaname</font></nobr></td><td></td></tr>
<tr><td><nobr><img src="$maindir/$imgfile/exp.gif" height="10"><img src="$maindir/$imgfile/hpbar1.gif" width=$hpbarmon1 height="8">$hpbardmg1<img src="$maindir/$imgfile/exp.gif" height="10"></nobr></td><td colspan=3><font size=4><nobr><img src="$maindir/$imgfile/exp.gif" height="10"><img src="$maindir/$imgfile/hpbar1.gif" width=$hpbarcha1 height="8">$hpbardmg2<img src="$maindir/$imgfile/exp.gif" height="8"></nobr></td><td></td></tr>
</table><font size=-1><center><b>$monshpnow / $monshp	�@�@�@�@�@�@�@�@�@�@�@�@�@	$chahpnow / $chastats[9]</center></b></font><br><br><font size=4>

HTM

$number = 0;
&pethatudou;

#�@�L�����̍U������
$chastats[13] ++;
$jobexpnow[$chaclass] ++;
if ( $jobexpnow[$chaclass] >= $jobexp[$chaclass] ){
$jobexpnow[$chaclass] = $jobexp[$chaclass];
}

if ( $chasoubi[7] eq "�_�u���A�^�b�N�����O") {
print "<font color=#$chamoji><b>$chaname</b></font> �̘A���U���I�I<br>";
} else{
print "<font color=#$chamoji><b>$chaname</b></font> �̍U���I�I<br>";
}
$nowstrexp ++;
	if ( $nowstrexp >= $strexp ) {

print <<"HTM";
<center>
<font size=5><span style={filter:glow(color=darkorange,strength=5);position:relative;height:50;width:100%;}>
<font color=white><b>$chaname</b> ��STR���オ�����I</font>
</span></font></center>
HTM


$strexp *= 1.3;
if ($strexp > 1000){$strexp = 1000;}
$nowstrexp = 0;
$chastats[2] ++;
	}


# srand;
$monsagi = rand(10);
	if ( $monsagi < 1 ) {
print "<font color=#$mojiiro4>$monsname �̓q�����Ɛg�����킵���I<br></font>"; 
$nowintexp ++;
	if ( $nowintexp >= $intexp ) {
print <<"HTM";
<center>
<font size=5><span style={filter:glow(color=cornflowerblue,strength=5);position:relative;height:50;width:100%;}>
<font color=white><b>$chaname</b> ��INT���オ�����I</font>
</span></font></center>
HTM

$intexp *= 1.2;
if ($intexp > 1000){$intexp = 1000;}
$nowintexp = 0;
$chastats[4] ++;
	}
	} else {
&jobatk;
if ($chastats[3] + $karistats[3] > 149 ) { &jobatk; }
if ($chastats[3] + $karistats[3] > 299 ) { &jobatk; }
if ($chastats[3] + $karistats[3] > 449 ) { &jobatk; }
if ($chastats[3] + $karistats[3] > 599 ) { &jobatk; }
if ( $job[$chaclass] eq "�E��") { &jobatk; }
if ( $chasoubi[7] eq "�_�u���A�^�b�N�����O") { &jobatk; }
if ( $houou > 0) { &jobatk; }
&tokunou;
	}

&deathchk;

$number = 1;
&pethatudou;

#�@�����X�^�[�̍U������
$mitore = rand(3);
$counter = rand(7);

if ( $chaclass == 8 && $counter < 1) {
print "<br><b>$monsname</b> �̍U���I�I<br>";

print "<b>$chaname</b>�u���؂����I�v<br>";
} elsif ( $chaclass == 8 && $counter < 2) {
print "<br><b>$monsname</b> �̍U���I�I<br>";
print "<b>$chaname</b>�u�x���I�v<br>";
} elsif ( $chaclass == 80 && $mitore < 1) {
print "<br><b>$monsname</b> �́A<b>$chaname</b>�Ɍ�����Ă���I<br>";
} else {
print "<br><b>$monsname</b> �̍U���I�I<br>";
$kawasi = 200 - $agi;
# srand;
}
if ( $kawasi < 29 ) {
$kawasi = 30;
}

$kawasiritu = rand( $kawasi );
if ( $kawasiritu < 10 ) {
print "<font color=#$mojiiro4>$chaname �͑f���������ōU����������I�I<br></font>"; 
$nowagiexp ++;
	if ( $nowagiexp >= $agiexp ) {
print <<"HTM";
<center>
<font size=5><span style={filter:glow(color=orchid,strength=5);position:relative;height:50;width:100%;}>
<font color=white><b>$chaname</b> ��AGI���オ�����I</font>
</span></font></center>
HTM

$agiexp *= 1.2;
if ($agiexp > 1000){$agiexp = 1000;}
$nowagiexp = 0;
$chastats[3] ++;

	}
} else {
$zokuhantei = rand(3);
	if ( $monskouka > 0 && $zokuhantei < 1 ) {
	$zokusei[1] = "��";$zokusei[2] = "��";$zokusei[3] = "��";$zokusei[4] = "��";
	$zokuatk[1] = $svf - 10;$zokuatk[2] = $svc - 10;$zokuatk[3] = $svm - 10;$zokuatk[4] = 0;
		if ($monskouka != 5 ) {
print "<font color=#$mojiiro2><b>$zokusei[$monskouka]�����U���I</b></font><br>";
$dmg2 = $monsattack - int( $ac / 2 ) - $zokuatk[$monskouka] + $lvlpoin;
		} else {
# srand;
$monskouka = int( rand(3)) + 1;
print "<font color=#$mojiiro2><b>$zokusei[$monskouka]�����U���I</b></font><br>";
$dmg2 = $monsattack - int( $ac / 2 ) - $zokuatk[$monskouka] + $lvlpoin;
$monskouka = 5;
		}
	} else {
$dmg2 = $monsattack - $ac + $lvlpoin;
	}
	if ( $dmg2 < 1 ) { $dmg2 = 0; }
# srand;
$dmg2 += int(rand($monslvl));

$critritu = rand(20);
if ( $critritu < 1 ) {
 $dmg2 *= 2;
print "<font size=4 color=#$mojiiro2>�ɍ��̈ꌂ�I<br></font>"; 
}

	if ( $dmg2 == 0 ) {
print "<font color=#$mojiiro4>$chaname �̓q�����Ɛg�����킵���I<br></font>"; 
$nowagiexp += 2;
	if ( $nowagiexp >= $agiexp ) {
print <<"HTM";
<center>
<font size=5><span style={filter:glow(color=orchid,strength=5);position:relative;height:50;width:100%;}>
<font color=white><b>$chaname</b> ��AGI���オ�����I</font>
</span></font></center>
HTM
$agiexp *= 1.2;
if ($agiexp > 300){$agiexp = 300;}
$nowagiexp = 0;
$chastats[3] ++;
	}
} elsif ( $chaclass == 8 && $counter < 1) {
print "$chaname �͑f���������ŁA���ɃJ�E���^�[�����߂��I<br>";
print "$monsname ��<font color=#$mojiiro2><b>$dmg2</b></font> �̃_���[�W��^�����I<br>";
$dmg2 * 2;
$monshpnow -= $dmg2;
} elsif ( $chaclass == 8 && $counter < 2) {
print "$chaname �͑f���������ŁA���ɃJ�E���^�[�����߂��I<br>";
print "$monsname ��<font color=#$mojiiro2><b>$dmg2</b></font> �̃_���[�W��^�����I<br>";
$dmg2 * 2;
$monshpnow -= $dmg2;

} elsif ( $chaclass == 80 && $mitore < 1) {
} else {
$chahpnow -= $dmg2;
print "$chaname �� <font color=#$mojiiro2><b>$dmg2</b></font> �̃_���[�W���󂯂��I<br>";
$nowacexp += $dmg2;
	if ( $nowacexp >= $acexp ) {

print <<"HTM";
<center>
<font size=5><span style={filter:glow(color=lightsalmon,strength=5);position:relative;height:50;width:100%;}>
<font color=white><b>$chaname</b> ��AC���オ�����I</font>
</span></font></center>
HTM
$acexp *= 1.5;
if ($acexp > 1000000){$acexp = 1000000;}
$nowacexp = 0;
$chastats[1] ++;
	}
	}
if ( $chahpnow <= 0 && $ribaibu > 0) {
print "</td></tr></table><br><br><font size=5 color=#$mojiiro4><b>$chaname �͓|�ꂽ�E�E�E�E</b></font><br><br>";
$chahpnow = 0;
$kaihuku = int($chastats[9] / 2);
$chahpnow += $kaihuku;
print <<"HTM";
����s���ӎ��̒��A�܂΂䂢����$chaname�̐g�̑S�̂��񂾁I<br>
���̌��𗁂сA$chaname�͋N���オ�����I<br>
<font color=red>���o�C�u�̌��ʂ��؂ꂽ�B</font><br>
HTM
$ribaibu = -1;


	} elsif ( $chahpnow <= 0 && $chasoubi[7] eq "�����̎w��") {
print "</td></tr></table><br><br><font size=5 color=#$mojiiro4><b>$chaname �͓|�ꂽ�E�E�E�E</b></font><br><br>";
$chahpnow = 0;
$kaihuku = int($chastats[9] / 2);
$chahpnow += $kaihuku;
print <<"HTM";
����s���ӎ��̒��A�����̎w�ւ��������P���������I<br>
���̌��𗁂сA$chaname�͋N���オ�����I<br>
�����̎w�ւ͉����Ȃ����ꋎ�����B<br>
HTM
$chasoubi[7] = "";

	} elsif ( $chahpnow <= 0 && $chasoubi[7] eq "�����̎w��") {
print "</td></tr></table><br><br><font size=5 color=#$mojiiro4><b>$chaname �͓|�ꂽ�E�E�E�E</b></font><br><br>";
$chahpnow = 0;
$chahpnow = $chahp;
$chahpnow --;
print <<"HTM";
����s���ӎ��̒��A�����̎w�ւ��������P���������I<br>
���̌��𗁂сA$chaname�͋N���オ�����I<br>
�����̎w�ւ͉����Ȃ����ꋎ�����B<br>
HTM
$chasoubi[7] = "";

	} elsif ( $chahpnow <= 0 && $chasoubi[7] eq "���̎w��") {
print "</td></tr></table><br><br><font size=5 color=#$mojiiro4><b>$chaname �͓|�ꂽ�E�E�E�E</b></font><br><br>";
$chahpnow = 0;
$chahpnow = $chastats[9];
$chahpnow --;
$champ = $chastats[16];
print <<"HTM";
����s���ӎ��̒��A���̎w�ւ��������P���������I<br>
���̌��𗁂сA$chaname�͋N���オ�����I<br>
���̎w�ւ͉����Ȃ����ꋎ�����B<br>
TP���S�񕜂����I<br>
HTM
$chasoubi[7] = "";

} else {
&deathchk;
}
$number = 2;
&pethatudou;

}

print <<"HTM";
</font></td></tr></table><br><br>
HTM
$battleturn ++;
}

&hpcheck;

#�@�퓬�I����̏���
sub hpcheck {
if ( $chahpnow <= 0 ) { 
#�@�L�������S����
$chastats[12] += 1;
print "</td></tr></table><br><br><font size=5 color=#$mojiiro4><b>$chaname �͐퓬�ɕ������E�E�E�E</b></font><br><br>";

if ( $chasoubi[7] eq "�y�b�g�J�o�[�����O" and $petcode[0] ne "" || $petcode[1] ne "" || $petcode[2] ne "" ) {
print "�y�b�g�J�o�[�����O�̌��ʂŃy�b�g�������Ȃ������B<br><br>";

} elsif ( $petcode[0] ne "" || $petcode[1] ne "" || $petcode[2] ne "" ) {
$petcode[0] = $petcode[1] = $petcode[2] = $petname[0] = $petname[1] = $petname[2] = "";
$petnowexp[0] = $petnowexp[1] = $petnowexp[2] = 0;
$petexp[0] = $petexp[1] = $petexp[2] = 10;
$petlv[0] = $petlv[1] = $petlv[2] = $petkouka[0] = $petkouka[1] = $petkouka[2] = $petkouka2[0] = $petkouka2[1] = $petkouka2[2] = $peteff[0] = $peteff[1] = $peteff[2] = $petritu[0] = $petritu[1] = $petritu[2] = $petpic[0] = $petpic[1] = $petpic[2] = "";
print "�y�b�g�������Ă����Ă��܂����E�E�E�E<br><br>";
	}

if ( $chahpnow <= 0 && $chasoubi[7] eq "�S�[���h�J�o�[�����O") {
print "�S�[���h�J�o�[�����O���G���珊������������B<br><br>";
} else {
$chagold = int( $chagold / 2 );
print "�������������ɂȂ��Ă��܂����E�E�E�E<br><br>";
}

$chahp = $chastats[9];
$chaplace = 0;
$kougeki = 0;
$mamori = 0;
if ( $master[$chaclass] == 1) {
$jobexpnow[$chaclass] = $jobexp[$chaclass];
}
print <<"HTM";

<A NAME="exit"></a>

�����I�ɃX�^�[�g�n�_�ɖ߂���܂��B</font>
<form method="post" action="./$zonecgi">
<input type=hidden value="0" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value=" �X�^�[�g�̊X�ɖ߂� " onClick="this.disabled=true; this.value=' �X�^�[�g�̊X�ɖ߂� '; this.form.submit();"></form></td></tr></table>
HTM


} elsif ( $monshpnow <= 0 ) {
print <<"HTM";
<A NAME="exit"></a>
HTM
print "</td></tr></table><br><br><font size=5 color=#$mojiiro3><b>$chaname</b> �͐퓬�ɏ��������I�I</font><br><br>";
# srand;
$bpo = "1";
$chastats[10] += 1;

	if ( $chastats[10] == 1000 || $chastats[10] == 2000 || $chastats[10] == 3000 || $chastats[10] == 4000 || $chastats[10] == 5000 || $chastats[10] == 6000 || $chastats[10] == 7000 || $chastats[10] == 8000 || $chastats[10] == 9000 || $chastats[10] == 10000 || $chastats[10] == 11000 || $chastats[10] == 12000 || $chastats[10] == 13000 || $chastats[10] == 14000 || $chastats[10] == 15000 || $chastats[10] == 16000 || $chastats[10] == 17000 || $chastats[10] == 18000 || $chastats[10] == 19000 || $chastats[10] == 20000 || $chastats[10] == 21000 || $chastats[10] == 22000 || $chastats[10] == 23000 || $chastats[10] == 24000 || $chastats[10] == 25000 || $chastats[10] == 26000 || $chastats[10] == 27000 || $chastats[10] == 28000 || $chastats[10] == 29000 || $chastats[10] == 30000 || $chastats[10] == 31000 || $chastats[10] == 32000 || $chastats[10] == 33000 || $chastats[10] == 34000 || $chastats[10] == 35000 || $chastats[10] == 36000 || $chastats[10] == 37000 || $chastats[10] == 38000 || $chastats[10] == 39000 || $chastats[10] == 40000 || $chastats[10] == 41000 || $chastats[10] == 42000 || $chastats[10] == 43000 || $chastats[10] == 44000 || $chastats[10] == 45000 || $chastats[10] == 46000 || $chastats[10] == 47000 || $chastats[10] == 48000 || $chastats[10] == 49000 || $chastats[10] == 50000 || $chastats[10] == 51000 || $chastats[10] == 52000 || $chastats[10] == 53000 || $chastats[10] == 54000 || $chastats[10] == 55000 || $chastats[10] == 56000 || $chastats[10] == 57000 || $chastats[10] == 58000 || $chastats[10] == 59000 || $chastats[10] == 60000 || $chastats[10] == 61000 || $chastats[10] == 62000 || $chastats[10] == 63000 || $chastats[10] == 64000 ) {
$chaage ++;
print <<"HTM";
<b>$chaname</b> �́A<b>$chaage��</b>�ɂȂ����B�i<font color=green><b>TP</b></font>+<b>5</b>�j</b><br><br>
HTM
$chastats[16] += 5;
}

$hukuget = $chalvl + $chastats[2] + $chastats[1] + $chastats[3] + $chastats[4] + $chastats[9];
$hukuget *= 3;
if ( $chasoubi[7] eq "���b�N�����O") {int($hukuget1 / 2);}
$hukuget1 = rand ($hukuget);
$hukuget2 = $monshp / 2;

$chastats[15] += $monsexp;
$getgold = int( $monsgold + rand($monslvl) );
$chastats[11] += $getgold;
$morai += 0.05;

if ( $chasoubi[7] eq "�`���N�������O") {
$kaihuku = int($chastats[9] / 10);
print <<"HTM";
<font size=-1>�`���N�������O�̖����̌��ʂŁAHP��<font size=4 color=#$mojiiro3><b>$kaihuku</b></font>�񕜂����B</font><br>
HTM
$chahpnow += $kaihuku;
	if ( $chahpnow > $chastats[9] ) {$chahpnow = $chastats[9];}

	} elsif ( $chasoubi[7] eq "�n�C�`���N�������O") {
$kaihuku = int($chastats[9] / 5);
print <<"HTM";
<font size=-1>�n�C�`���N�������O�̖����̌��ʂŁAHP��<font size=4 color=#$mojiiro3><b>$kaihuku</b></font>�񕜂����B</font><br>
HTM
$chahpnow += $kaihuku;
	if ( $chahpnow > $chastats[9] ) {$chahpnow = $chastats[9];}


	}
if ( $chasoubi[7] eq "���b�`�����O") {
$getgold = int($getgold * 1.5);
print <<"HTM";
<font size=-1>���b�`�����O�̌��ʂŁA<b>Gold</b>��<b>1.5</b>�{�ɂȂ����I</font><br>
HTM
	}
if ( $chasoubi[7] eq "�}�[���C�h�����O") {
$monsexp = int($monsexp * 1.3);
print <<"HTM";
<font size=-1>�}�[���C�h�����O�̌��ʂŁA<b>EXP</b>��<b>1.3</b>�{�ɂȂ����I</font><br>
HTM
	}
$monsexp = int( $monsexp * $expmode);
$chaexp += $monsexp;

if($petcode[0] ne ""){
$petnowexp[0] += $monsexp;
}
if($petcode[1] ne ""){
$petnowexp[1] += $monsexp;
}
if($petcode[2] ne ""){
$petnowexp[2] += $monsexp;
}
$tugipet0 = $petexp[0] - $petnowexp[0];
$tugipet1 = $petexp[1] - $petnowexp[1];
$tugipet2 = $petexp[2] - $petnowexp[2];
if($tugipet0 < 0){$tugipet0 = "<font color=red><FONT FACE=Times New Roman>LV UP!!</font></font>"};
if($tugipet1 < 0){$tugipet1 = "<font color=red><FONT FACE=Times New Roman>LV UP!!</font></font>"};
if($tugipet2 < 0){$tugipet2 = "<font color=red><FONT FACE=Times New Roman>LV UP!!</font></font>"};

$tugilvl = $chanextlvl - $chaexp;
	if($tugilvl < 0){$tugilvl = "<font color=red><FONT FACE=Times New Roman>LV UP!!</font></font>";}
$getgold = int($getgold * $goldmode);
$chagold += $getgold;
print "<font color=#$mojiiro4><FONT FACE=Times New Roman><b><font size=4>$getgold</font></font> </font><FONT FACE=Times New Roman>G</font></b> ����ɓ��ꂽ�I<br>";
print "<font color=#$mojiiro3><FONT FACE=Times New Roman><b><font size=4>$monsexp</font></font> </font><FONT FACE=Times New Roman>EXP</font></b>���l���I<br><br>";
print "<font color=darkblue><b><FONT FACE=Times New Roman>Next Level</b></font><br><table border=1><TBODY><TR><TD>$chaname</TD><TD> <b><FONT FACE=Times New Roman>$tugilvl</td></tr></b>";

if($petcode[0] ne ""){print "<td>$petname[0]  <b></td><td><b><FONT FACE=Times New Roman>$tugipet0</font></b></td></tr>";}
if($petcode[1] ne ""){print "<td>$petname[1]  <b></td><td><b><FONT FACE=Times New Roman>$tugipet1</font></b></td></tr>";}
if($petcode[2] ne ""){print "<td>$petname[2]  <b></td><td><b><FONT FACE=Times New Roman>$tugipet2</font></b></td>";}
print "</tr></table><br>";
	if ( $chagold > 1000000000 ) { $chagold = 999999999;}

		if ( $hukuget1 < $hukuget2 ) {
print "<font color=green><b>$monsname</font> ����</b> <font color=brown><b>������</b></font>����ɓ��ꂽ�I<br><br>";
$hukubiki ++;
}

	if ( $chastats[10] == 120 ) {
if ( $flag20 eq "" ) { $flag20 = 20; }
print "<font color=red><b>���Z�u�q�[�����O�v���K�������I</b></font><br><br>";
}

	if ( $chastats[10] == 300 ) {
if ( $flag19 eq "" ) { $flag19 = 19; }
print "<font color=red><b>���Z�u�X�L�b�v�v���K�������I</b></font><br><br>";
}

	if ( $chastats[10] == 700 ) {
if ( $flag18 eq "" ) { $flag18 = 18; }
print "<font color=red><b>���Z�u�e���|�[�g�v���K�������I</b></font><br><br>";
}

	if ( $chastats[10] == 1250 ) {
if ( $flag17 eq "" ) { $flag17 = 17; }
print "<font color=red><b>���Z�u�n�C�q�[�����O�v���K�������I</b></font><br><br>";
}

	if ( $chastats[10] == 1800 ) {
if ( $flag16 eq "" ) { $flag16 = 16; }
print "<font color=red><b>���Z�u�V�[���h�A�b�v�v���K�������I</b></font><br><br>";
}

	if ( $chastats[10] == 2600 ) {
if ( $flag15 eq "" ) { $flag15 = 15; }
print "<font color=red><b>���Z�u�p���[�A�b�v�v���K�������I</b></font><br><br>";
}

if ( $master[$chaclass] == 1) {
$jobexpnow[$chaclass] = $jobexp[$chaclass];
} elsif ( $jobexpnow[$chaclass] >= $jobexp[$chaclass] ){
$master[$chaclass] = 1;
print "<font size=4 color=darkblue><b>$job[$chaclass]�̋Ɉӂ��K�������I</b></font><br><br>";
print "<font size=2 color=darkblue><b><font color=green>TP��2�オ�����I</font></b></font><br><br>";
$jobexpnow[$chaclass] = $jobexp[$chaclass];
$masterjob ++;
$chastats[16] += 2;
}

		if ( $champ <= 0) {
$hpdmg = int($chahp / 8);
$chahpnow -= $hpdmg;
print <<"HTM";
<font size=3><font color=red><b>��J�̂�����HP�� $hpdmg ���������I<br></b></font></font>
<br><br>
HTM
}

$tp --;
if($tp == 0){
$champ -= 1;
$tp = 3;
}
	if ( $champ <= 0 ) { $champ = 0; }

if ( $petnowexp[0] >= $petexp[0] ){
$petlv[0] ++;
print "<font size=5 color=#$mojiiro4><b>$petname[0]</b> �̃��x���� $petlv[0] �ɏオ�����I</font><br><br>";
print "���ʒl(EF) + <b>1</b>�@�i<b><font color=palevioletred>$petkouka2[0]</font>�@�ˁ@";
$petkouka2[0] ++;
print "<font color=green>$petkouka2[0]</font></b>�j<br>";
$petkaku = int(rand(3)) + 1;
print "�Q���l(PP) + <b>$petkaku</b>�@�i<b><font color=palevioletred>$petritu[0]</font>�@�ˁ@";
$petritu[0] += $petkaku;
print "<font color=green>$petritu[0]</font></b>�j<br><br>";
$petnowexp[0] = 0;
$exprand = rand(100);
if ( $exprand < 60 ) {
$petexp[0] = int($petexp[0] * 1.2) + int(rand(3));
	} else {$petexp[0] = int($petexp[0] * 1.3) + int(rand(3));}
if($petexp[0] > 50000){$petexp = 50000;}

$omake = int(rand(100));
if( $omake < 10 ) {
$omake2 = int(rand(2));
if ( $omake2 == 0 ){
print "$petname[0] �� $chaname �̐킢�Ԃ�Ɉ��|���ꂽ�悤���B<br>";
print "$petname[0] �� $chaname ��<b>HP</b>��S�����Ă��ꂽ�I<br>";
$chahpnow = $chastats[9];
	} elsif ( $omake2 == 1 ){
print "$petname[0] �� $chaname �̐킢�Ԃ�Ɋ��������悤���B<br>";
print "$petname[0] �� $chaname ��<b>TP</b>��S�����Ă��ꂽ�I<br>";
$champ = $chastats[16];
	} elsif ( $omake2 == 2 ){
print "$petname[0] �� $chaname �̌����Ȑ킢�Ԃ�Ɋ��������悤���B<br>";
print "$petname[0] �� $chaname ��<b>HP,TP</b>��S�����Ă��ꂽ�I<br>";
$chahpnow = $chastats[9];
$champ = $chastats[16];
		}
	}
}

if ( $petnowexp[1] >= $petexp[1] ){
$petlv[1] ++;
print "<font size=5 color=#$mojiiro4><b>$petname[1]</b> �̃��x���� $petlv[1] �ɏオ�����I</font><br><br>";
print "���ʒl(EF) + <b>1</b>�@�i<b><font color=palevioletred>$petkouka2[1]</font>�@�ˁ@";
$petkouka2[1] ++;
print "<font color=green>$petkouka2[1]</font></b>�j<br>";
$petkaku = int(rand(3)) + 1;
print "�Q���l(PP) + <b>$petkaku</b>�@�i<b><font color=palevioletred>$petritu[1]</font>�@�ˁ@";
$petritu[1] += $petkaku;
print "<font color=green>$petritu[1]</font></b>�j<br><br>";
$petnowexp[1] = 0;
$exprand = rand(100);
if ( $exprand < 60 ) {
$petexp[1] = int($petexp[1] * 1.2) + int(rand(3));
	} else {$petexp[1] = int($petexp[1] * 1.3) + int(rand(3));}
if($petexp[1] > 50000){$petexp = 50000;}

$omake = int(rand(100));
if( $omake < 10 ) {
$omake2 = int(rand(2));
if ( $omake2 == 0 ){
print "$petname[1] �� $chaname �̐킢�Ԃ�Ɉ��|���ꂽ�悤���B<br>";
print "$petname[1] �� $chaname ��<b>HP</b>��S�����Ă��ꂽ�I<br>";
$chahpnow = $chastats[9];
	} elsif ( $omake2 == 1 ){
print "$petname[1] �� $chaname �̐킢�Ԃ�Ɋ��������悤���B<br>";
print "$petname[1] �� $chaname ��<b>TP</b>��S�����Ă��ꂽ�I<br>";
$champ = $chastats[16];
	} elsif ( $omake2 == 2 ){
print "$petname[1] �� $chaname �̌����Ȑ킢�Ԃ�Ɋ��������悤���B<br>";
print "$petname[1] �� $chaname ��<b>HP,TP</b>��S�����Ă��ꂽ�I<br>";
$chahpnow = $chastats[9];
$champ = $chastats[16];
		}
	}
}

if ( $petnowexp[2] >= $petexp[2] ){
$petlv[2] ++;
print "<font size=5 color=#$mojiiro4><b>$petname[2]</b> �̃��x���� $petlv[2] �ɏオ�����I</font><br><br>";
print "���ʒl(EF) + <b>1</b>�@�i<b><font color=palevioletred>$petkouka2[2]</font>�@�ˁ@";
$petkouka2[2] ++;
print "<font color=green>$petkouka2[2]</font></b>�j<br>";
$petkaku = int(rand(3)) + 1;
print "�Q���l(PP) + <b>$petkaku</b>�@�i<b><font color=palevioletred>$petritu[2]</font>�@�ˁ@";
$petritu[2] += $petkaku;
print "<font color=green>$petritu[2]</font></b>�j<br><br>";
$petnowexp[2] = 0;
$exprand = rand(100);
if ( $exprand < 60 ) {
$petexp[2] = int($petexp[2] * 1.2) + int(rand(3));
	} else {$petexp[2] = int($petexp[2] * 1.3) + int(rand(3));}
if($petexp[2] > 50000){$petexp = 50000;}

$omake = int(rand(100));
if( $omake < 10 ) {
$omake2 = int(rand(2));
if ( $omake2 == 0 ){
print "$petname[2] �� $chaname �̐킢�Ԃ�Ɉ��|�����悤���B<br>";
print "$petname[2] �� $chaname ��<b>HP</b>��S�����Ă��ꂽ�I<br>";
$chahpnow = $chastats[9];
	} elsif ( $omake2 == 1 ){
print "$petname[2] �� $chaname �̐킢�Ԃ�Ɋ��������悤���B<br>";
print "$petname[2] �� $chaname ��<b>TP</b>��S�����Ă��ꂽ�I<br>";
$champ = $chastats[16];
	} elsif ( $omake2 == 2 ){
print "$petname[2] �� $chaname �̌����Ȑ킢�Ԃ�Ɋ��������悤���B<br>";
print "$petname[2] �� $chaname ��<b>HP,TP</b>��S�����Ă��ꂽ�I<br>";
$chahpnow = $chastats[9];
$champ = $chastats[16];
		}
	}
}

	if ( $chaexp >= $chanextlvl && $chalvl != 10000000 ) {
$chaexp = 0;$chalvl ++;$chastats[0] ++;

open(EXP,"./exp$bousikts");
$expnum = 0;
		while ( $exptugi = <EXP> ) {
			if ($expnum == $chalvl ) {
			chop($exptugi);$chanextlvl = $exptugi;last;
			}
$expnum ++;
		}
close(EXP);

print "<font size=5 color=#$mojiiro4><b>$chaname</b> �̓��x�����オ�����I</font><br><br>";

	if ( $chalvl == 10 || $chalvl == 20 || $chalvl == 30 || $chalvl == 40 || $chalvl == 50 || $chalvl == 60 || $chalvl == 70 || $chalvl == 80 || $chalvl == 90 || $chalvl == 100 || $chalvl == 110 || $chalvl == 120 || $chalvl == 130 || $chalvl == 140 || $chalvl == 150 || $chalvl == 160 || $chalvl == 170 || $chalvl == 180 || $chalvl == 190 || $chalvl == 200 || $chalvl == 210 || $chalvl == 220 || $chalvl == 230 || $chalvl == 240 || $chalvl == 250 || $chalvl == 260 || $chalvl == 270 || $chalvl == 280 || $chalvl == 290 || $chalvl == 300 || $chalvl == 310 || $chalvl == 320 || $chalvl == 330 || $chalvl == 340 || $chalvl == 350 || $chalvl == 360 || $chalvl == 370 || $chalvl == 380 || $chalvl == 390 || $chalvl == 400 || $chalvl == 410 || $chalvl == 420 || $chalvl == 430 || $chalvl == 440 || $chalvl == 450 || $chalvl == 460 || $chalvl == 470 || $chalvl == 480 || $chalvl == 490 || $chalvl == 500 ) {
print "<font color=green><b>TP</b>��<b>1</b>�オ�����I</font><br>";
$chastats[16] ++;
}

&levelup;


	}
#�@�A�C�e���l������

$randitem = int( rand(3));
	if ( $randitem > 0 ) {
$itembangou = 0;
	} else {

$randitem = int( rand(3));
		if ( $randitem > 0 ) {
$itembangou = 1;
		} else {

$randitem = int( rand(2));
			if ( $randitem == 0 ) {
$itembangou = 2;
			} elsif ( $randitem == 1 ) {
$itembangou = 3;
			} else {
$itembangou = 4;
			}
		}
	}

	if ( $monsitem[$itembangou] ne "" ) {
print "$monsname �́u<font size=4 color=#$mojiiro4><b>$monsitem[$itembangou]</b></font>�v�������Ă����I<br><br>";

open(KAI,"$maindir/item$bousikts");
		while ( $kaitori = <KAI> ) {
			($kainame,$a,$b,$c,$d,$itemkouka,$itemstats) = split(/,/,$kaitori);
			if ( $monsitem[$itembangou] eq $kainame ) {
			last;
			}
		}
close(KAI);
		if ( $itemstats >= 10 ) {
		$bbb = 1;
			while ( $bbb < 9 ) {
				if ( $chaitem[$bbb] eq $monsitem[$itembangou] ) {
			last;
				}
			$bbb ++;
			}

			if ( $bbb >=9 ) {
		$ccc = 1;
				while ( $ccc < 9 ) {
					if ( $chaitem[$ccc] eq "" ) {
			last;
					}
			$ccc ++;
				}
				if( $ccc <= 9 ) {
$chaitem[$ccc] = $monsitem[$itembangou];$chaeff[$ccc] = 1;$chasetumei[$ccc] =$itemkouka;
				} else {
			print "�������������ς��������̂ł�����߂��E�E�E<br>";
				}
			} elsif ( $chaeff[$bbb] < 99 ) { $chaeff[$bbb] ++; 
			} else { print "���������ς��������̂ł�����߂��E�E�E<br>";
			}


		} else {
		$ccc = 1;
			while ( $ccc < 9 ) {
				if ( $chaitem[$ccc] eq "" ) {
			last;
				}
			$ccc ++;
			}
			if( $ccc <= 9 ) {
$chaitem[$ccc] = $monsitem[$itembangou];$chaeff[$ccc] = 1;$chasetumei[$ccc] =$itemkouka;
			} else {
			print "�������������ς��������̂ł�����߂��E�E�E<br>";
			}
		}
	}
	if ( $chaclass == 7 && $tokugikouka > 1 ) { $cha -= ($chastats[5] * 9 ); }
	if ( $chaclass == 71 && $tokugikouka > 1 ) { $cha -= 1000; }
	if ( $chaclass == 72 && $tokugikouka > 1 ) { $cha -= ($chastats[5] * 9 ); }
	if ( $chaclass == 82 && $tokugikouka > 1 ) { $cha -= ($chastats[5] * 12 ); }

$turepet = 0;$turepetti = 0;
	while ( $turepet < 3 ) {
		if ( $petcode[$turepet] ne "" ) { $turepetti ++; }
$turepet ++;
	}
#�@�y�b�g�l������
# srand;
$petgetritu = int( rand(1000) ) - int((($cha - 10 )/2) * $turepetti);
	if ( $petgetritu <= $monscha ) {

open(PET,"$maindir/$foldacha/pet_$in{usrid}$bousi2cha$bousikts");
$ppp = 0;
		while ( $petnakama = <PET> ) {
			chop($petnakama);
			if ( $petnakama eq $monsname ) {
				$ppp ++;last;
			}
		}
close(PET);
open(PET,"$maindir/$foldacha/pet_$in{usrid}$bousi2cha$bousikts");
			$petsousuu = <PET>;
close(PET);

		if ( $ppp == 0 && $petcode[0] ne $monsname && $petcode[1] ne $monsname && $petcode[2] ne $monsname && $petsousuu <= 200) {
open(PET,">>$maindir/$foldacha/pet_$in{usrid}$bousi2cha$bousikts");
			print PET "$monsname\n";
close(PET);
print <<"HTM";
<br><font size=4 color=#$monsname><b>$monsname</font></b> �����ԂɂȂ肽�����ɂ���������߂Ă���E�E�E<br><br>
<font color=#$chamoji><b>$chaname</font></b> �� <font size=4 color=#$monsname><b>$monsname</font></b> ���y�b�g�����ɑ������I�I<br>
HTM

		}
	}

$chahp = $chahpnow;
$chacount --;
	if( $chasoubi[7] eq "�X�L�b�v�����O" ) { $chacount --;}
if ( $kougekit > 0 ) {$kougekit --;}
if ( $kougekit == 0 ) {
print "<font color=red>�p���[�A�b�v�̌��ʂ��؂ꂽ�B</font><br><br>";
$kougekit --;
$kougeki = 0;
	}

if ( $mamorit > 0 ) {$mamorit --;}
if ( $mamorit == 0 ) {
print "<font color=red>�V�[���h�A�b�v�̌��ʂ��؂ꂽ�B</font><br><br>";
$mamorit --;
$mamori = 0;
	}

if ( $houou > 0 ) {$houou --;}
if ( $houou == 0 ) {
print "<font color=red>�P���̕��̌��ʂ��؂ꂽ�B</font><br><br>";
$houou --;
	}

if ( $ribaibu > 0 ) {$ribaibu --;}
if ( $ribaibu == 0 ) {
print "<font color=red>���o�C�u�̌��ʂ��؂�Ă��܂����B</font><br><br>";
$ribaibu --;
	}

print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$in{boss}" name="boss">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value=" �]�[���ɖ߂� " onClick="this.disabled=true; this.value=' �]�[���ɖ߂� '; this.form.submit();"></form></td></tr></table>
HTM

} else {
$tp --;
if($tp == 0){
$champ -= 1;
$tp = 3;
}
$chahp = $chahpnow;
$chacount --;
	if( $chasoubi[7] eq "�X�L�b�v�����O" ) { $chacount --;}
$kougeki = 0;
$mamori = 0;
	if ( $champ <= 0 ) { $champ = 0; }


print <<"HTM";
<A NAME="exit"></a>
</td></tr></table><br><br>
<font size=5 color=#$mojiiro4><b>$monsname</b> �͓����o�����E�E�E�E</font><br><br>
<form method="post" action="./$zonecgi">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value=" �]�[���ɖ߂� " onClick="this.disabled=true; this.value=' �]�[���ɖ߂� '; this.form.submit();"></form></td></tr></table>
HTM

}

&charadatawrt;
&hpowari;exit;
}

sub deathchk {
	if ( $chahpnow <= 0 ) { last; }
	if ( $monshpnow <= 0 ) { last; }
}



#�@�y�b�g�̍U������
sub petdmg {
		if ( $dmg < 1 ) { $dmg = 0; }
# srand;
$dmg += int(rand($petlv[$number]));
		if ( $dmg == 0 ) {
print "<font color=#$mojiiro4>$monsname �̓q�����Ɛg�����킵���I<br><br></font>"; 
		} else {
$monshpnow -= $dmg;
print "$monsname �� <font size=4 color=#$mojiiro2><b>$dmg</b></font> �̃_���[�W��^�����I<br><br>";

		}
}

sub pethatudou {
	if ( $petcode[$number] ne "" ) {
		if ( $petkoukaturn[$number] == 1 && $petkouka[$number] >= 9) {
&petadd;
print "<font color=#$chamoji><b>$petname[$number]</font> </b>�̃A�V�X�g���ʂ��؂ꂽ<br><br>";

		} elsif ( $petkoukaturn[$number] <= 0 ) {
# srand;
$petsanka = rand(1000);
			if ( $petsanka < ($petritu[$number] + $cha) ) {
print "<br><font color=#$chamoji><b>$petname[$number]</b></font> �̃A�V�X�g�I<br>";
&petadd;
			}
		} 
$petkoukaturn[$number] --;
	}
&deathchk;

}

sub petadd {
	if ( $petkouka[$number] == 16 ) {
$dmg = $petkouka2[$number] - $monsac + int(rand($petlv[$number]));
&petdmg;

	} elsif ( $petkouka[$number] == 1 ) {
$dmg = $petkouka2[$number] - int($monsac / 2 ) - $monssvf + int(rand($petlv[$number]));
print "<font color=#$mojiiro2><b>�Α����_���[�W</b></font><br>";
&petdmg;

	} elsif ( $petkouka[$number] == 2 ) {
$dmg = $petkouka2[$number] - int($monsac / 2 ) - $monssvc + int(rand($petlv[$number]));
print "<font color=#$mojiiro2><b>�������_���[�W</b></font><br>";
&petdmg;

	} elsif ( $petkouka[$number] == 3 ) {
$dmg = $petkouka2[$number] - int($monsac / 2 ) - $monssvm + int(rand($petlv[$number]));
print "<font color=#$mojiiro2><b>�������_���[�W</b></font><br>";
&petdmg;

	} elsif ( $petkouka[$number] == 4 ) {
$dmg = $petkouka2[$number] - int($monsac / 2 ) + int(rand($petlv[$number]));
print "<font color=#$mojiiro2><b>�������_���[�W</b></font><br>";
&petdmg;

	} elsif ( $petkouka[$number] == 5 ) {
# srand;
$abe = rand (3);
		if ( $abe < 1 ) {
$dmg = $petkouka2[$number] - int($monsac / 2 ) - $monssvf + int(rand($petlv[$number]));
print "<font color=#$mojiiro2><b>�Α����_���[�W</b></font><br>";
		} elsif ( $abe < 1 ) {
$dmg = $petkouka2[$number] - int($monsac / 2 ) - $monssvc + int(rand($petlv[$number]));
print "<font color=#$mojiiro2><b>�������_���[�W</b></font><br>";
		} else {
$dmg = $petkouka2[$number] - int($monsac / 2 ) - $monssvm + int(rand($petlv[$number]));
print "<font color=#$mojiiro2><b>�������_���[�W</b></font><br>";
		}
&petdmg;

	} elsif ( $petkouka[$number] == 6 ) {
$dmg = $petkouka2[$number] + int(rand($petlv[$number]));
$dmg2 = int( $dmg / 3 );
$chagold += $dmg2;
print "<b>$monsname</b> ���� <font color=#$mojiiro4><b>$dmg2</font> G</b> ���񂾁I<br><br>";

	} elsif ( $petkouka[$number] == 7 ) { #########
	} elsif ( $petkouka[$number] == 8 ) {
$dmg = $petkouka2[$number] + int(rand($petlv[$number]));
$chahpnow += $dmg;
		if($chahpnow > $chastats[9] ) {
$chahpnow = $chastats[9];
		}
print "HP��<font color=#$mojiiro2><b> $dmg</font> </b>�񕜂����I<br><br>";

	} elsif ( $petkouka[$number] == 9 ) {
		if($petkoukaturn[$number] <= 0 ) {
$ac += $petkouka2[$number];
$petkoukaturn[$number] = 3;
print "<font color=#$chamoji><b>$chaname</font> </b>�̖h��͂��A�b�v�I<br><br>";
		} elsif ( $petkoukaturn[$number] == 1 ) {
$ac -= $petkouka2[$number];
		}

	} elsif ( $petkouka[$number] == 10 ) {
		if($petkoukaturn[$number] <= 0 ) {
$str += $petkouka2[$number];
$petkoukaturn[$number] = 3;
print "<font color=#$chamoji><b>$chaname</font> </b>�̗͂��A�b�v�I<br><br>";
		} elsif ( $petkoukaturn[$number] == 1 ) {
$str -= $petkouka2[$number];
		}

	} elsif ( $petkouka[$number] == 11 ) {
		if($petkoukaturn[$number] <= 0 ) {
$agi += $petkouka2[$number];
$petkoukaturn[$number] = 3;
print "<font color=#$chamoji><b>$chaname</font> </b>�̑f�������A�b�v�I<br><br>";
		} elsif ( $petkoukaturn[$number] == 1 ) {
$agi -= $petkouka2[$number];
		}

	} elsif ( $petkouka[$number] == 12 ) {
		if($petkoukaturn[$number] <= 0 ) {
$int += $petkouka2[$number];
$petkoukaturn[$number] = 3;
print "<font color=#$chamoji><b>$chaname</font> </b>�̒m�����A�b�v�I<br><br>";
		} elsif ( $petkoukaturn[$number] == 1 ) {
$int -= $petkouka2[$number];
		}

	} elsif ( $petkouka[$number] == 13 ) {
		if($petkoukaturn[$number] <= 0 ) {
$cha += $petkouka2[$number];
$petkoukaturn[$number] = 3;
print "<font color=#$chamoji><b>$chaname</font> </b>�̖��͂��A�b�v�I<br><br>";
		} elsif ( $petkoukaturn[$number] == 1 ) {
$cha -= $petkouka2[$number];
		}

	} elsif ( $petkouka[$number] == 14 ) {
		if($petkoukaturn[$number] <= 0 ) {
$svf += $petkouka2[$number];$svc += $petkouka2[$number];$svm += $petkouka2[$number];
$petkoukaturn[$number] = 3;
print "<font color=#$chamoji><b>$chaname</font> </b>�̑ϐ����A�b�v�I<br><br>";
		} elsif ( $petkoukaturn[$number] == 1 ) {
$svf -= $petkouka2[$number];$svc -= $petkouka2[$number];$svm -= $petkouka2[$number];
		}

	} elsif ( $petkouka[$number] == 15 ) {
$dhuran = int( rand(35) );

		if ( $dhuran == 0 ) {
print "<b>$petname[$number]</b>�͓V�����W�����v�����I<br>";
print "�E�E�E���̂܂܋A���Ă��Ȃ������B<br><br>";


		} elsif ( $dhuran == 1 ) {
$dmg = int( $str / 3 ) + $pow - $monsac;
		if ( $dmg < 1 ) { $dmg = 0; }
# srand;
$dmg += int(rand($chalvl));
$monshpnow -= $dmg;
print "<b>$petname[$number]</b>�͓V�����W�����v�����I<br>";
print "<font size=5 color=#$mojiiro2><b>�򗴗����� �I�I</b></font><br><br>";
print "$monsname �� <font size=4 color=#$mojiiro2><b>$dmg</b></font> �̃_���[�W��^�����I<br><br>";


		} elsif ( $dhuran == 2 ) {
$dmg = int( $str / 3 ) + $pow - $monsac;
		if ( $dmg < 1 ) { $dmg = 0; }
# srand;
$dmg += int(rand($chalvl));
$dmg = int ($dmg / 2);
$chagold += $dmg;
print "<b>$petname[$number]</b>�͖ڂɂ��Ƃ܂�ʑ����œG�̉��ɐ��荞�񂾁I<br>";
print "<b>$petname[$number]</b>�u�������ƁI�v<br><br>";
print "$monsname ���� <font size=4 color=#$mojiiro4><b>$dmg</b></font> G�𓐂񂾁I<br><br>";


		} elsif ( $dhuran == 3 ) {
print "<b>$petname[$number]</b>�u���̔�Z�ɑς����邩�ȁE�E�E�v<br>";
print "<font size=5 color=#$mojiiro2><b>�a�S�� �I�I</b></font><br><br>";
print "��u�œG��^����ɂ����I<br><br>";
$monshpnow = 0;


		} elsif ( $dhuran == 4 ) {
$dmg = $chastats[0] - $chastats[1];

print "<b>$petname[$number]</b>�͊ԈႦ��<font color=#$chamoji><b>$chaname</font></b>�ɍU�������Ă��܂����I<br>";
print "<font color=#$chamoji><b>$chaname</font></b>��<font size=4 color=#$mojiiro2><b>$dmg</b></font> �̃_���[�W���󂯂��I<br><br>";
print "<b>$petname[$number]</b>�u���E�E�E�I�@���܂˂��I�@�����I�v<br><br>";
$chahpnow -= $dmg;

		} elsif ( $dhuran == 5 ) {
$dmg = 100;
$monshpnow -= $dmg;
print "<b>$petname[$number]</b>�͕���𓊂��̂āA�G�ɉ����r���^�𒣂�o�����I<br><br>";
print "$monsname��<font size=4 color=#$mojiiro2><b>10</b></font> �̃_���[�W��^�����I<br>";
print "$monsname��<font size=4 color=#$mojiiro2><b>10</b></font> �̃_���[�W��^�����I<br>";
print "$monsname��<font size=4 color=#$mojiiro2><b>10</b></font> �̃_���[�W��^�����I<br>";
print "$monsname��<font size=4 color=#$mojiiro2><b>10</b></font> �̃_���[�W��^�����I<br>";
print "$monsname��<font size=4 color=#$mojiiro2><b>10</b></font> �̃_���[�W��^�����I<br>";
print "$monsname��<font size=4 color=#$mojiiro2><b>10</b></font> �̃_���[�W��^�����I<br>";
print "$monsname��<font size=4 color=#$mojiiro2><b>10</b></font> �̃_���[�W��^�����I<br>";
print "$monsname��<font size=4 color=#$mojiiro2><b>10</b></font> �̃_���[�W��^�����I<br>";
print "$monsname��<font size=4 color=#$mojiiro2><b>10</b></font> �̃_���[�W��^�����I<br>";
print "$monsname��<font size=4 color=#$mojiiro2><b>10</b></font> �̃_���[�W��^�����I<br>";


		} elsif ( $dhuran == 6 ) {
$dmg = 100;
$chahpnow += $dmg;

print "<b>$petname[$number]</b>�u$chaname �I�@������g���I�v<br>";
print "<b>$petname[$number]</b>��$chaname ��<font size=4 color=#$mojiiro4><b>�|�[�V����</b></font> �𓊂����I<br><br>";
print "<font color=#$chamoji><b>$chaname</font></b>��HP��<font size=4 color=#$mojiiro3><b>$dmg</b></font>�񕜂����I<br><br>";
				if ( $chahpnow > $chastats[9] ) {
$chahpnow = $chastats[9];
				}

		} elsif ( $dhuran == 7 ) {
$dmg = 300;
$chahpnow += $dmg;

print "<b>$petname[$number]</b>�u$chaname �I�@������g���I�v<br>";
print "<b>$petname[$number]</b>��$chaname ��<font size=4 color=#$mojiiro4><b>�~�h���|�[�V����</b></font> �𓊂����I<br><br>";
print "<font color=#$chamoji><b>$chaname</font></b>��HP��<font size=4 color=#$mojiiro3><b>$dmg</b></font>�񕜂����I<br><br>";
				if ( $chahpnow > $chastats[9] ) {
$chahpnow = $chastats[9];
				}


		} elsif ( $dhuran == 8 ) {
$dmg = 10 + int(rand($chalvl));
$chahpnow -= $dmg;
$monshpnow -= $dmg;
print "<b>$petname[$number]</b>�͂ǂ����炩���e���E���Ă����E�E�E<br>";
print "<b>$petname[$number]</b>�u$chaname �I�@�����E�E�E�v<br>";
print "<b>$chaname</b>�u�E�E�E���H�v<br><br>";
print "���c�ɂ����e�͔����������N�������I<br><br>";

print "$chaname��<font size=4 color=#$mojiiro2><b>$dmg</b></font> �̃_���[�W���󂯂��I<br>";
print "$monsname��<font size=4 color=#$mojiiro2><b>$dmg</b></font> �̃_���[�W���󂯂��I<br>";
print "<b>$petname[$number]</b>��<font size=4 color=#$mojiiro2><b>$dmg</b></font> �̃_���[�W���󂯂��I<br><br>";


		} elsif ( $dhuran == 9 ) {
print "<b>$petname[$number]</b>��$chaname�̉e�ɉB��Ă���B<br><br>";


		} elsif ( $dhuran == 10 ) {
print "<b>$petname[$number]</b>�̓{�[���Ƃ��Ă���B<br><br>";


		} elsif ( $dhuran == 11 ) {
$dmg = int( $str / 3 ) + $pow - $monsac;
		if ( $dmg < 1 ) { $dmg = 0; }
# srand;
$dmg += int(rand($chalvl));
$dmg = int($dmg / 1.5);
$dmg * 4;
$monshpnow -= $dmg;

print "<b>$petname[$number]</b>�͕����傫���U��グ�A$monsname �ɒ@�������I<br>";
print "<b>$petname[$number]</b>�u�������`�b�I�v<br>";
print "$monsname ��<font size=4 color=#$mojiiro2><b>$dmg</b></font>�̃_���[�W��^�����I<br><br>";


		} elsif ( $dhuran == 12 ) {
$dmg = int( $str / 3 ) + $pow - $monsac;
		if ( $dmg < 1 ) { $dmg = 0; }
# srand;
$dmg += int(rand($chalvl));
$dmg * 5;
$monshpnow -= $dmg;

$dmg1 = int( $str / 3 ) + $pow - $monsac;
		if ( $dmg1 < 1 ) { $dmg1 = 0; }
# srand;
$dmg1 += int(rand($chalvl));
$dmg1 * 5;
$monshpnow -= $dmg1;
print "�f�������͕����U�肩�����A�����������n�߂��I<br>";
print "�����܂��É_���ӂ���ݍ��ށI<br>";
print "<font size=5 color=#$mojiiro2><b>�o���g �I�I</b></font><br>";
print "�Q�C�̋���ȗ���$monsname �ɏP���|����I<br><br>";
print "�������͉s���܂�$monsname �������~�����I<br>";
print "$monsname ��<font size=4 color=#$mojiiro2><b>$dmg</b></font>�̃_���[�W��^�����I<br><br>";
print "�C���͉s�����$monsname �ɋ�炢�����I<br>";
print "$monsname ��<font size=4 color=#$mojiiro2><b>$dmg1</b></font>�̃_���[�W��^�����I<br><br>";

		} else  {
$dmg = int( $str / 3 ) + $pow - $monsac;
		if ( $dmg < 1 ) { $dmg = 0; }
# srand;
$dmg += int(rand($chalvl));
$dmg = int($dmg / 1.5);
$monshpnow -= $dmg;
print "$monsname ��<font size=4 color=#$mojiiro2><b>$dmg</b></font>�̃_���[�W��^�����I<br><br>";

		}

	} else {
	&fuseisyori;exit;
	}
}



sub tokunou {
if ( $chasoubi[7] eq "�X���C�������O") {
$kaihuku = int(rand(4)) + 1;
print <<"HTM";
<font size=-1>�X���C�������O�̖����̌��ʂŁA<b>HP</b>��<font size=4 color=#$mojiiro3><b>$kaihuku</b></font>�񕜂����B</font><br>
HTM
$chahpnow += $kaihuku;
	if ( $chahpnow > $chastats[9] ) {$chahpnow = $chastats[9];}
	}

if ( $chasoubi[1] eq "�����̏�") {
$kaihuku = int(rand(30)) + 5;
print <<"HTM";
<font size=-1>�����̏�̖����̌��ʂŁA<b>HP</b>��<font size=4 color=#$mojiiro3><b>$kaihuku</b></font>�񕜂����B</font><br>
HTM
$chahpnow += $kaihuku;
	if ( $chahpnow > $chastats[9] ) {$chahpnow = $chastats[9];}
	}

if ( $chasoubi[7] eq "�P���w��") {
$kaihuku = int(rand(7)) + 13;
print <<"HTM";
<font size=-1>�P���w�ւ̖����̌��ʂŁA<b>HP</b>��<font size=4 color=#$mojiiro3><b>$kaihuku</b></font>�񕜂����B</font><br>
HTM
$chahpnow += $kaihuku;
	if ( $chahpnow > $chastats[9] ) {$chahpnow = $chastats[9];}
	}

if ( $chasoubi[4] eq "�~�m���[�u") {
$kaihuku = int(rand(4)) + 8;
print <<"HTM";
<font size=-1>�~�m���[�u�̖����̌��ʂŁA<b>HP</b>��<font size=4 color=#$mojiiro3><b>$kaihuku</b></font>�񕜂����B</font><br>
HTM
$chahpnow += $kaihuku;
	if ( $chahpnow > $chastats[9] ) {$chahpnow = $chastats[9];}
	}

if ( $chasoubi[4] eq "�X���C�����[�u") {
$kaihuku = int(rand(5)) + 6;
print <<"HTM";
<font size=-1>�X���C�����[�u�̖����̌��ʂŁA<b>HP</b>��<font size=4 color=#$mojiiro3><b>$kaihuku</b></font>�񕜂����B</font><br>
HTM
$chahpnow += $kaihuku;
	if ( $chahpnow > $chastats[9] ) {$chahpnow = $chastats[9];}
	}

if ( $chasoubi[4] eq "���C�g�v���[�g�`�F�X�g") {
$kaihuku = int(rand(9)) + 2;
print <<"HTM";
<font size=-1>���C�g�v���[�g�`�F�X�g����g������������I�@<b>HP</b>��<font size=4 color=#$mojiiro3><b>$kaihuku</b></font>�񕜂����B</font><br>
HTM
$chahpnow += $kaihuku;
	if ( $chahpnow > $chastats[9] ) {$chahpnow = $chastats[9];}
	}

if ( $chasoubi[4] eq "�v�����X�N���E�Y") {
$kaihuku = int(rand(15)) + 12;
print <<"HTM";
<font size=-1>�v�����X�N���E�Y����g������������I�@<b>HP</b>��<font size=4 color=#$mojiiro3><b>$kaihuku</b></font>�񕜂����B</font><br>
HTM
$chahpnow += $kaihuku;
	if ( $chahpnow > $chastats[9] ) {$chahpnow = $chastats[9];}
	}

if ( $chasoubi[3] eq "�t�����[�w����") {
$kaihuku = int(rand(7)) + 2;
print <<"HTM";
<font size=-1>�t�����[�w�����̖����̌��ʂŁA<b>HP</b>��<font size=4 color=#$mojiiro3><b>$kaihuku</b></font>�񕜂����B</font><br>
HTM
$chahpnow += $kaihuku;
	if ( $chahpnow > $chastats[9] ) {$chahpnow = $chastats[9];}
	}

if ( $chasoubi[1] eq "�品") {
$kaihuku = int(rand(3));
if ( $kaihuku == 1 ) {
$tuika = int($str / 2);
print <<"HTM";
<font size=-1>�品�̐n���G�̋}�����a�����I�@�����<font size=4 color=#$mojiiro2><b>$tuika</b></font>�̃_���[�W��^�����I</font><br>
HTM
$monshpnow -= $tuika;
}
	}

if ( $chasoubi[2] eq "�t�F�j�b�N�X�\�[�h") {
$kaihuku = int(rand(2));
if ( $kaihuku == 1 ) {
$tuika = int($str / 2);
print <<"HTM";
<font size=-1>�t�F�j�b�N�X�\�[�h�őf�����a������I�@�����<font size=4 color=#$mojiiro2><b>$tuika</b></font>�̃_���[�W��^�����I</font><br>
HTM
$monshpnow -= $tuika;
}
	}


if ( $chasoubi[1] eq "�\�E���C�[�^�[") {
$intup = int($dmg / 5) + 1;

print <<"HTM";
<font size=-1>�\�E���C�[�^�[�͓G��HP��<font size=4 color=#$mojiiro2><b>$intup</b></font>�z��������I�@<b>HP</b>��<font size=4 color=#$mojiiro3><b>$intup</b></font>�񕜂����B</font><br>
HTM
$chahpnow += $intup;
$monshpnow -= $intup;
	if ( $chahpnow > $chastats[9] ) {$chahpnow = $chastats[9];}
	}

if ( $chasoubi[1] eq "�X�p�i") {
$kaihuku = int(rand(2));
if ( $kaihuku == 1 ) {
$tuika = int($str / 4);
print <<"HTM";
<font size=-1>���łɁA�����P���X�p�i�ŉ����Ă������B�@�����<font size=4 color=#$mojiiro2><b>$tuika</b></font>�̃_���[�W��^�����I</font><br>
HTM
$monshpnow -= $tuika;
}
	}

if ( $chasoubi[6] eq "�f�X�^�[�N�O���[�u") {
$kaihuku = int(rand(3));
if ( $kaihuku == 1 ) {
$tuika = int($str / 2);
print <<"HTM";
<font size=-1>�f�X�^�[�N�O���[�u�̌��ʂŁA�����<font size=4 color=#$mojiiro2><b>$tuika</b></font>�̃_���[�W��^�����I</font><br>
HTM
$monshpnow -= $tuika;
}
	}

if ( $chasoubi[1] eq "���K�\�[�h") {
$kaihuku = int(rand(3));
if ( $kaihuku == 1 ) {
$tuika = int($str / 2);
print <<"HTM";
<font size=-1>���K�\�[�h�̐n���G�̋}�����a�����I�@�����<font size=4 color=#$mojiiro2><b>$tuika</b></font>�̃_���[�W��^�����I</font><br>
HTM
$monshpnow -= $tuika;
}
	}

if ( $chasoubi[7] eq "���K�����O") {
$kaihuku = int(rand(3));
if ( $kaihuku == 1 ) {
$tuika = int($str / 2);
print <<"HTM";
<font size=-1>���K�����O�͍����g����������I�@�����<font size=4 color=#$mojiiro2><b>$tuika</b></font>�̃_���[�W��^�����I</font><br>
HTM
$monshpnow -= $tuika;
}
	}

if ( $chasoubi[2] eq "���t�g�S�u�����N���E") {
$kaihuku = int(rand(3));
if ( $kaihuku == 1 ) {
$tuika = int($str / 3);
print <<"HTM";
<font size=-1>���t�g�S�u�����N���E�őf�����ǉ��U���I�@�����<font size=4 color=#$mojiiro2><b>$tuika</b></font>�̃_���[�W��^�����I</font><br>
HTM
$monshpnow -= $tuika;
}
	}

if ( $chasoubi[5] eq "�u���b�O���b�O�X") {
$kaihuku = int(rand(4));
if ( $kaihuku == 1 ) {
$intup = int($dmg / 4) + 1;
$chahpnow += $intup;
$monshpnow -= $intup;
print <<"HTM";
<font size=-1>�u���b�O���b�O�X�͓G��HP��<font size=4 color=#$mojiiro2><b>$intup</b></font>�z��������I�@<b>HP</b>��<font size=4 color=#$mojiiro3><b>$intup</b></font>�񕜂����B</font><br>
HTM
$chahpnow += $kaihuku;
	if ( $chahpnow > $chastats[9] ) {$chahpnow = $chastats[9];}
}
	}

if ( $chasoubi[1] eq "�l�N���}���T�[") {
$intup = int($dmg / 5) + 1;
$chahpnow += $intup;
$monshpnow -= $intup;
print <<"HTM";
<font size=-1>�l�N���}���T�[�͓G��HP��<font size=4 color=#$mojiiro2><b>$intup</b></font>�z��������I�@<b>HP</b>��<font size=4 color=#$mojiiro3><b>$intup</b></font>�񕜂����B</font><br>
HTM
$chahpnow += $kaihuku;
	if ( $chahpnow > $chastats[9] ) {$chahpnow = $chastats[9];}
	}


if ( $chasoubi[3] eq "�S�u�����X�L���t�[�h") {
$kaihuku = int(rand(4));
if ( $kaihuku == 1 ) {
$intup = int(rand(3)) + 1;
$str += $intup;
print <<"HTM";
<font size=-1>�S�u�����X�L���t�[�h�̌��ʂŁA�ꎞ�I��<b>STR</b>��<font size=4 color=#$mojiiro1><b>$intup</b></font>�オ�����I</font><br>
HTM
}
	}

if ( $chasoubi[6] eq "�����̘r�Z") {
$kaihuku = int(rand(5));
if ( $kaihuku == 1 ) {
print <<"HTM";
<font size=-1>�����̘r�Z�̌��ʂŒǉ��U���I</font><br>
HTM
&jobatk;
}
	}

if ( $chasoubi[1] eq "�T�C�o�[�\�[�h") {
$kaihuku = int(rand(4));
if ( $kaihuku == 1 ) {
print <<"HTM";
<font size=-1>�T�C�o�[�\�[�h�őf�����ǉ��U���I</font><br>
HTM
&jobatk;
}
	}

if ( $chasoubi[1] eq "�����̐j") {
$kaihuku = int(rand(10));
if ( $kaihuku == 1 ) {
print <<"HTM";
<font size=-1>�����̐j�œG�̋}���������I</font><br>
HTM
$monshpnow = 0;
}
	}

if ( $chasoubi[4] eq "�E�r����") {
$kaihuku = int(rand(5));
if ( $kaihuku == 1 ) {
print <<"HTM";
<font size=-1>�E�r�����̌��ʂŒǉ��U���I</font><br>
HTM
&jobatk;
}
	}

if ( $chasoubi[8] eq "�f�U�[�g�l�b�N���X") {
$kaihuku = int(rand(3));
if ( $kaihuku == 1 ) {
$intup = int(rand(5)) + 5;
$svf += $intup;
print <<"HTM";
<font size=-1>�f�U�[�g�l�b�N���X�̌��ʂŁA�ꎞ�I��<b>SVF</b>��<font size=4 color=#$mojiiro1><b>$intup</b></font>�オ�����I</font><br>
HTM
}
	}

if ( $chasoubi[3] eq "�t�F�j�b�N�X�t�[�h") {
$kaihuku = int(rand(3));
if ( $kaihuku == 1 ) {
$intup = int(rand(25)) + 15;
$svf += $intup;
print <<"HTM";
<font size=-1>�t�F�j�b�N�X�t�[�h�̌��ʂŁA�ꎞ�I��<b>SVF</b>��<font size=4 color=#$mojiiro1><b>$intup</b></font>�オ�����I</font><br>
HTM
}
	}

if ( $chasoubi[5] eq "�����O���C�����b�O�X") {
$kaihuku = int(rand(3));
if ( $kaihuku == 1 ) {
$intup = int(rand(10)) + 7;
$svc += $intup;
print <<"HTM";
<font size=-1>�����O���C�����b�O�X�̌��ʂŁA�ꎞ�I��<b>SVC</b>��<font size=4 color=#$mojiiro1><b>$intup</b></font>�オ�����I</font><br>
HTM
}
	}

if ( $chasoubi[2] eq "�g�t���̏�") {
$kaihuku = int(rand(3));
if ( $kaihuku == 1 ) {
$intup = int(rand(5)) + 5;
$ac += $intup;
print <<"HTM";
<font size=-1>�g�t���̏��̌��ʂŁA�ꎞ�I��<b>AC</b>��<font size=4 color=#$mojiiro1><b>$intup</b></font>�オ�����I</font><br>
HTM
}
	}

if ( $chasoubi[2] eq "�X�N���[�����b�h") {
$kaihuku = int(rand(3));
if ( $kaihuku == 1 ) {
$intup = int(rand(10)) + 7;
$svf += $intup;
print <<"HTM";
<font size=-1>�X�N���[�����b�h�̌��ʂŁA�ꎞ�I��<b>SVF</b>��<font size=4 color=#$mojiiro1><b>$intup</b></font>�オ�����I</font><br>
HTM
}
	}

if ( $chasoubi[2] eq "���b�v�\�[�h") {
$kaihuku = int(rand(4));
if ( $kaihuku == 1 ) {
$intup = int(rand(10)) + 7;
$cha += $intup;
print <<"HTM";
<font size=-1>���b�v�\�[�h�̌��ʂŁA�ꎞ�I��<b>CHA</b>��<font size=4 color=#$mojiiro1><b>$intup</b></font>�オ�����I</font><br>
HTM
}
	}

if ( $chasoubi[7] eq "�A�_�}���^�C�g�����O") {
$kaihuku = int(rand(6));
if ( $kaihuku == 1 ) {
$intup = int(rand(1)) + 1;
$champ += $intup;
print <<"HTM";
<font size=-1>�A�_�}���^�C�g�����O�̌��ʂŁA<b>TP</b>��<font size=4 color=#$mojiiro3><b>$intup</b></font>�񕜂����B</font><br>
HTM
	if ( $champ > $chastats[16] ) {$champ = $chastats[16];}
}
	}

if ( $chasoubi[3] eq "���@�̊�") {
$kaihuku = int(rand(7));
if ( $kaihuku == 1 ) {
$intup = int(rand(2)) + 2;
$champ += $intup;
print <<"HTM";
<font size=-1>���@�̊��̌��ʂŁA<b>TP</b>��<font size=4 color=#$mojiiro3><b>$intup</b></font>�񕜂����B</font><br>
HTM
	if ( $champ > $chastats[16] ) {$champ = $chastats[16];}
}
	}

if ( $chasoubi[2] eq "���Ȃ鏂") {
$kaihuku = int(rand(3));
if ( $kaihuku == 1 ) {
$chahpnow += $chalvl;
print <<"HTM";
<font size=-1>���Ȃ鏂�̖����̌��ʂŁA<b>HP</b>��<font size=4 color=#$mojiiro3><b>$chalvl</b></font>�񕜂����B</font><br>
HTM
	if ( $chahpnow > $chastats[9] ) {$chahpnow = $chastats[9];}
}
	}

if ( $chasoubi[2] eq "����̏�") {
$kaihuku = int(rand(2));
if ( $kaihuku == 1 ) {
$intup = int(rand(15)) + 10;
print <<"HTM";
<font size=-1>����̏��̖����̌��ʂŁA<b>HP</b>��<font size=4 color=#$mojiiro3><b>$intup</b></font>�񕜂����B</font><br>
HTM
$chahpnow += $intup;
	if ( $chahpnow > $chastats[9] ) {$chahpnow = $chastats[9];}
}
	}

if ( $chasoubi[3] eq "����̊�") {
$kaihuku = int(rand(2));
if ( $kaihuku == 1 ) {
$intup = int(rand(15)) + 10;
print <<"HTM";
<font size=-1>����̊��̖����̌��ʂŁA<b>HP</b>��<font size=4 color=#$mojiiro3><b>$intup</b></font>�񕜂����B</font><br>
HTM
$chahpnow += $intup;
	if ( $chahpnow > $chastats[9] ) {$chahpnow = $chastats[9];}
}
	}

if ( $chasoubi[2] eq "���ꂽ�ڋ�") {
$kaihuku = int(rand(2));
if ( $kaihuku == 1 ) {
$intup = int(rand(6)) + 10;
$cha += $intup;
print <<"HTM";
<font size=-1>���ꂽ�ڋʂ̌��ʂŁA�ꎞ�I��<b>CHA</b>��<font size=4 color=#$mojiiro1><b>$intup</b></font>�オ�����I</font><br>
HTM
}
	}

if ( $chasoubi[2] eq "�v���Y�}�u���[�h") {
$kaihuku = int(rand(4));
if ( $kaihuku == 1 ) {
$intup = int(rand(6)) + 5;
$ac += $intup;
print <<"HTM";
<font size=-1>�v���Y�}�u���[�h��$chaname��<b>AC</b>���ꎞ�I��<font size=4 color=#$mojiiro1><b>$intup</b></font>���߂��I</font><br>
HTM
}
	}

if ( $chasoubi[3] eq "�}���V�t�[�h") {
$intup = int(rand(2)) + 1;
$svm += $intup;
print <<"HTM";
<font size=-1>�}���V�t�[�h�̌��ʂŁA�ꎞ�I��<b>SVM</b>��<font size=4 color=#$mojiiro1><b>$intup</b></font>�オ�����I</font><br>
HTM
	}

if ( $chasoubi[5] eq "�w���A�[�}�[���b�O�X") {
$intup = int(rand(6)) + 14;
$svm += $intup;
print <<"HTM";
<font size=-1>�w���A�[�}�[���b�O�X�̌��ʂŁA�ꎞ�I��<b>SVM</b>��<font size=4 color=#$mojiiro1><b>$intup</b></font>�オ�����I</font><br>
HTM
	}

if ( $chasoubi[4] eq "�u���U�[�h���[�u") {
$intup = int(rand(2)) + 3;
$svc += $intup;
print <<"HTM";
<font size=-1>�u���U�[�h���[�u�̌��ʂŁA�ꎞ�I��<b>SVC</b>��<font size=4 color=#$mojiiro1><b>$intup</b></font>�オ�����I</font><br>
HTM
	}

if ( $chasoubi[4] eq "�A�C�X�N�B�[�����[�u") {
$intup = int(rand(2)) + 3;
$svc += $intup;
print <<"HTM";
<font size=-1>�A�C�X�N�B�[�����[�u�̌��ʂŁA�ꎞ�I��<b>SVC</b>��<font size=4 color=#$mojiiro1><b>$intup</b></font>�オ�����I</font><br>
HTM
	}

if ( $chasoubi[2] eq "�m�[���N���[") {
$kaihuku = int(rand(3));
if ( $kaihuku == 1 ) {
$tuika = int($str / 3);
print <<"HTM";
<font size=-1>�m�[���N���[�őf�����ǉ��U���I�@�����<font size=4 color=#$mojiiro2><b>$tuika</b></font>�̃_���[�W��^�����I</font><br>
HTM
$monshpnow -= $tuika;
}
	}

if ( $chasoubi[1] eq "�i�C�g�����X") {
$kaihuku = int(rand(3));
if ( $kaihuku == 1 ) {
$tuika = int($str / 3);
print <<"HTM";
<font size=-1>�i�C�g�����X�őf�����ǉ��U���I�@�����<font size=4 color=#$mojiiro2><b>$tuika</b></font>�̃_���[�W��^�����I</font><br>
HTM
$monshpnow -= $tuika;
}
	}

if ( $chasoubi[4] eq "�����l�̕�") {
$kaihuku = int(rand(70));
if ( $kaihuku == 1 ) {
$tuika = int(rand(5)) + 5;
$chastats[9] += $tuika;
print <<"HTM";
<font size=-1>�����l�̕���$chaname�̓��̂𑝋������I�@�ő�HP��<font size=4 color=#$mojiiro1><b>$tuika</b></font>�オ�����I</font><br>
HTM
}
	}

if ( $chasoubi[5] eq "�u���b�h���b�O�X") {
$kaihuku = int(rand(5));
if ( $kaihuku == 1 ) {
$intup = int($dmg / 3) + 1;
$chahpnow += $intup;
print <<"HTM";
<font size=-1>�u���b�h���b�O�X�͓G��HP��<font size=4 color=#$mojiiro2><b>$intup</b></font>�z��������I�@<b>HP</b>��<font size=4 color=#$mojiiro3><b>$intup</b></font>�񕜂����B</font><br>
HTM
	if ( $chahpnow > $chastats[9] ) {$chahpnow = $chastats[9];}
}
	}

if ( $chasoubi[3] eq "���F�̔�蕨") {
$kaihuku = int(rand(3));
if ( $kaihuku == 1 ) {
$intup = int(rand(10)) + 6;
$str += $intup;
print <<"HTM";
<font size=-1>���F�̔�蕨�̌��ʂŁA�ꎞ�I��<b>STR</b>��<font size=4 color=#$mojiiro1><b>$intup</b></font>�オ�����I</font><br>
HTM
}
	}

if ( $chasoubi[1] eq "�O���[�g�{�[���\�[�h") {
$kaihuku = int(rand(3));
if ( $kaihuku == 1 ) {
$intup = int(rand(20)) + 10;
$str += $intup;
print <<"HTM";
<font size=-1>�O���[�g�{�[���\�[�h�̌��ʂŁA�ꎞ�I��<b>STR</b>��<font size=4 color=#$mojiiro1><b>$intup</b></font>�オ�����I</font><br>
HTM
}
	}

if ( $chasoubi[4] eq "�f�[�����X�L���`���j�b�N") {
$kaihuku = int(rand(3));
if ( $kaihuku == 1 ) {
$intup = int(rand(10)) + 15;
$svm += $intup;
print <<"HTM";
<font size=-1>�f�[�����X�L���`���j�b�N�̌��ʂŁA�ꎞ�I��<b>SVM</b>��<font size=4 color=#$mojiiro1><b>$intup</b></font>�オ�����I</font><br>
HTM
}
	}

if ( $chasoubi[4] eq "�t���C���A�[�}�[�w����") {
$intup = int(rand(10)) + 11;
$svc += $intup;
print <<"HTM";
<font size=-1>�t���C���A�[�}�[�w�����̌��ʂŁA�ꎞ�I��<b>SVC</b>��<font size=4 color=#$mojiiro1><b>$intup</b></font>�オ�����I</font><br>
HTM
	}

if ( $chasoubi[6] eq "�_�[�N�A�[�}�[�O���[�u") {
$kaihuku = int(rand(3));
if ( $kaihuku == 1 ) {
$intup = int(rand(10)) + 18;
$svm += $intup;
print <<"HTM";
<font size=-1>�_�[�N�A�[�}�[�O���[�u�̌��ʂŁA�ꎞ�I��<b>SVM</b>��<font size=4 color=#$mojiiro1><b>$intup</b></font>�オ�����I</font><br>
HTM
}
	}

if ( $chasoubi[4] eq "�A�C�X�A�[�}�[�`�F�X�g") {
$kaihuku = int(rand(3));
if ( $kaihuku == 1 ) {
$intup = int(rand(10)) + 15;
$svc += $intup;
print <<"HTM";
<font size=-1>�A�C�X�A�[�}�[�`�F�X�g�̌��ʂŁA�ꎞ�I��<b>SVM</b>��<font size=4 color=#$mojiiro1><b>$intup</b></font>�オ�����I</font><br>
HTM
}
	}

if ( $chasoubi[1] eq "�t�@�C�A�[�\�[�h") {
$kaihuku = int(rand(3));
if ( $kaihuku == 1 ) {
$intup = int(rand(10)) + 13;
$svf += $intup;
print <<"HTM";
<font size=-1>�t�@�C�A�[�\�[�h�̌��ʂŁA�ꎞ�I��<b>SVF</b>��<font size=4 color=#$mojiiro1><b>$intup</b></font>�オ�����I</font><br>
HTM
}
	}

if ( $chasoubi[3] eq "�A�V�����̉���") {
$kaihuku = int(rand(3));
if ( $kaihuku == 1 ) {
$intup = int(rand(20)) + 15;
$agi += $intup;
print <<"HTM";
<font size=-1>�A�V�����̉��ʂ̌��ʂŁA�ꎞ�I��<b>AGI</b>��<font size=4 color=#$mojiiro1><b>$intup</b></font>�オ�����I</font><br>
HTM
}
	}

if ( $chasoubi[3] eq "�S�u�����X�L���`���j�b�N") {
$kaihuku = int(rand(3));
if ( $kaihuku == 1 ) {
$intup = int(rand(8)) + 3;
$agi += $intup;
print <<"HTM";
<font size=-1>�S�u�����X�L���`���j�b�N�̌��ʂŁA�ꎞ�I��<b>AGI</b>��<font size=4 color=#$mojiiro1><b>$intup</b></font>�オ�����I</font><br>
HTM
}
	}

if ( $chasoubi[4] eq "�C�G�e�B�X�L���`�F�X�g") {
$intup = int(rand(3)) + 2;
$str += $intup;
print <<"HTM";
<font size=-1>�C�G�e�B�X�L���`�F�X�g�̌��ʂŁA�ꎞ�I��<b>STR</b>��<font size=4 color=#$mojiiro1><b>$intup</b></font>�オ�����I</font><br>
HTM
	}

if ( $chasoubi[4] eq "�A�C�X���[�u") {
$intup = int(rand(2)) + 2;
$svf += $intup;
$str += $intup;
print <<"HTM";
<font size=-1>�A�C�X���[�u�̌��ʂŁA�ꎞ�I��<b>STR,SVF</b>��<font size=4 color=#$mojiiro1><b>$intup</b></font>�オ�����I</font><br>
HTM
	}

if ( $chasoubi[2] eq "���@��") {
$intup = int(rand(13)) + 10;
$int += $intup;
print <<"HTM";
<font size=-1>���@���̌��ʂŁA�ꎞ�I��<b>INT</b>��<font size=4 color=#$mojiiro1><b>$intup</b></font>�オ�����I</font><br>
HTM
	}

if ( $chasoubi[4] eq "�P���x���X�̕�") {
$intup = int(rand(5)) + 5;
$agi += $intup;
print <<"HTM";
<font size=-1>�P���x���X�̕��̌��ʂŁA�ꎞ�I��<b>AGI</b>��<font size=4 color=#$mojiiro1><b>$intup</b></font>�オ�����I</font><br>
HTM
	}

if ( $chasoubi[3] eq "�P���x���X�̔�蕨") {
$intup = int(rand(3)) + 4;
$agi += $intup;
print <<"HTM";
<font size=-1>�P���x���X�̔�蕨�̌��ʂŁA�ꎞ�I��<b>AGI</b>��<font size=4 color=#$mojiiro1><b>$intup</b></font>�オ�����I</font><br>
HTM
	}

if ( $chasoubi[3] eq "�P���x���X�̘r") {
$intup = int(rand(4)) + 4;
$agi += $intup;
print <<"HTM";
<font size=-1>�P���x���X�̘r�̌��ʂŁA�ꎞ�I��<b>AGI</b>��<font size=4 color=#$mojiiro1><b>$intup</b></font>�オ�����I</font><br>
HTM
	}

if ( $chasoubi[4] eq "���l�̈�") {
$kaihuku = int(rand(4));
if ( $kaihuku == 1 ) {
$intup2 = int(rand(10)) + 8;
$intup = int($dmg / 2) + 1;
$str += $intup2;
$chahpnow += $intup;
print <<"HTM";
<font size=-1>���l�̈߂̌��ʂŁA<b>STR</b>���ꎞ�I��<b>$intup2</b>�㏸���A<b>HP</b>��<font size=4 color=#$mojiiro3><b>$intup</b></font>�񕜂����B</font><br>
HTM
	if ( $chahpnow > $chastats[9] ) {$chahpnow = $chastats[9];}
}
	}
}


#�@���x���A�b�v����
sub levelup {
$statsban = 2;
		while ( $statsban < 9 ) {
# srand;
$lvlrand = rand ($jobrand[$statsban]);
			if ( $lvlrand < 1 ) {

print "$statsname[$statsban] + <b>1</b>�@�i<b><font color=palevioletred>$chastats[$statsban]</font>�@�ˁ@";
$chastats[$statsban] ++;
print "<font color=green>$chastats[$statsban]</font></b>�j<br>";
			}
$statsban ++;
		}
# srand;
$lvlpt += 2 + $chalvl;
$lvlpoint += $lvlpt;
$chastats[14] += $chalvl;
$hpup = int ( rand ($jobhpuprand) ) + int ( $chalvl / 5 ) + $jobhpup;
print "�ő�HP + <b>$hpup</b>�@�i<b><font color=palevioletred>$chastats[9]</font>�@�ˁ@";
$chastats[9] += $hpup;
print "<font color=green>$chastats[9]</font></b>�j<br><br>";
if ( $chasoubi[7] eq "�L���p�V�e�B�����O") { $chastats[14] += int($chalvl * 1.3) }
$chastats[14] += $chalvl;
}

exit;