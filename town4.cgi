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
		if ( $now < $nowjikan + 100 && $nowid ne $chaid ) {
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
if ( $mente == 1 ){
&mente;
}

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
<td align=right><nobr><font size=6 color=#$mojiiro2><b></b></font></nobr></td><td width=30></td><td><nobr>
���݂̖`���ҁi$playingkazu�l�j/
HTM

foreach $playnow ( @playing ) {
	chop($playnow);
	($nowid,$nowname) = split(/\//,$playnow);
print " <a href=\"./$introcgi?usrid=$nowid\" target=\"intro\"><b>$nowname</b></a> /<wbr>";

}
$bpo = "0";
$chastats[11] = 0;
&charadatawrt;
$timesa = $chajikan - $now + $nexttime;

print <<"HTM";
<wbr></nobr></tr></table>

</td></tr></table>
</td><td width=10></td><td>
<table border=0><tr><td colspan=3>
HTM

$chastats[11] = 0;
$ryoukin1 = ( $chalvl ) * 3;
$ryoukin2 = ( $chastats[16] - $champ ) * 1;
$ryoukin = $ryoukin1 + $ryoukin2;
$tugilvl = $chanextlvl - $chaexp;

if ($jobexpnow[$chaclass] == $jobexp[$chaclass]){ $mas ="<center><font color=red><font size=-2>- MASTER! -</font></font></center>"; }
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
                �E<A HREF="http://gyagoo.mine.nu/gyagoo/wforum/wforum.cgi" target="blank">�f����</a>
                �E<a href="javascript:close()">�Q�[���I��</a><br><hr>
                <b> �������F <font color=#$chamoji>$hukubiki</b></font><font size=-1><b>��</b></font><br><hr>
                <b> ���́iCHA�j�@�F<font color=#$chamoji>$chastats[5]</b></font> + <b><font color=palevioletred>$karistats[5]</font></b><br>
                <b> �Αϐ��iSVF�j�F<font color=#$chamoji>$chastats[6]</b></font> + <b><font color=palevioletred>$karistats[6]</font></b><br>
                <b> ���ϐ��iSVC�j�F<font color=#$chamoji>$chastats[7]</b></font> + <b><font color=palevioletred>$karistats[7]</font></b><br>
                <b> ���ϐ��iSVM�j�F<font color=#$chamoji>$chastats[8]</b></font> + <b><font color=palevioletred>$karistats[8]</font></b><br><hr>
                <font size=-1><b>�n���x�y$job[$chaclass]�z   <font color=palevioletred>$jobritu2</font><font size=-2></font></b></font><br>
<img src="$maindir/$imgfile/exp.gif" height="10"><img src="$maindir/$imgfile/jobbar1.gif" width=$jobbarcha1 height="8">$hpbardmg3<img src="$maindir/$imgfile/exp.gif" height="8"><br><hr>
                <b> ���݂̕�V�F<font color=blue>$chastats[13]</font>�f<br>
                 ���݂̏h��F<font color=red>$ryoukin</font>�f<br><hr>

                <font size=-1> ����Lv�܂�</font><font color=#$chamoji>$tugilvl</font><font size=-1>EXP</font></b>
            </TD>
        </TR>
    </TABLE>
</DIV>
<!--���j���[�p�^�O�����܂�-->
HTM
$timesa = $chajikan - $now + $nexttime;

print <<"HTM";
<wbr></nobr></tr></table><br><hr>
<br>

</td></tr></table>
</td><td width=10></td><td>
<table border=0><tr><td colspan=3>
HTM




$sisetu[1] = "�`���҃M���h";
$sisetu[2] = "���̋�������";
$sisetu[3] = "�G�݉�";
$sisetu[4] = "�y�b�g����";
$sisetu[5] = "������";
$sisetu[6] = "���@";
$sisetu[7] = "���V�̉�";
$sisetu[8] = "�d�q�f����";
$sisetu[9] = "�@�@  �d�q����  �@�@";
$sisetu[10] = " �@�@�@�X�֋ǁ@�@ �@";
$sisetu[11] = "����";


@omosa = ("","�y��","����","�d��");
@bui = ("����","�E��","����","��","��","�r","�r","�w","��");

################################
if ( $in{sisetu} eq "1"){
require "./$bankcgi";
} elsif ( $in{sisetu} eq "2"){
&topsisetu;




$ryoukin = $chagold;

	if ( $in{riyou} eq "1"){
		if ( $chagold < 100000) {
print <<"HTM";
�Ȃ񂾁H�@�������́A<b>100,000</b>�f�������ĂȂ��̂��B<br>
�n�R�l�ɗp�͂Ȃ��E�E�E�������ƋA��ȁB
HTM
&townmodori;
		} else {

$chagold -= $ryoukin;
$hpup += int ( $ryoukin / 2055 );
$chastats[9] += $hpup;
$strup = int ( $ryoukin / 58255 );
$acup = int ( $ryoukin / 58355 );
$intup = int ( $ryoukin / 58155 );
$agiup = int ( $ryoukin / 58255 );
$chaup = int ( $ryoukin / 58055 );

$chastats[2] += $strup;
$chastats[1] += $acup;
$chastats[4] += $intup;
$chastats[3] += $agiup;
$chastats[5] += $chaup;

print <<"HTM";
<b><font size=2 color=#$mojiiro1>�ő�g�o��<font size=3 color=#$mojiiro2>$hpup</font>�オ�����I</font></b><br>
<b><font size=2 color=#$mojiiro1>STR��<font size=3 color=#$mojiiro2>$strup</font>���������I</font></b><br>
<b><font size=2 color=#$mojiiro1>AC��<font size=3 color=#$mojiiro2>$acup</font>���������I</font></b><br>
<b><font size=2 color=#$mojiiro1>INT��<font size=3 color=#$mojiiro2>$intup</font>���������I</font></b><br>
<b><font size=2 color=#$mojiiro1>AGI��<font size=3 color=#$mojiiro2>$agiup</font>���������I</font></b><br>
<b><font size=2 color=#$mojiiro1>CHA��<font size=3 color=#$mojiiro2>$chaup</font>���������I</font></b><br><br>

</nobr>�킨�I�@�u<b><font color=#$mojiiro3>$ryoukin</b></font>�v G�������Ȃ�āA�����Ƒ��������˂��`�B<br>
�m���ɖ��@�������Ƃ��Ă�������B�@�܂����W�܂������Η�����I<br>
HTM
&charadatawrt;
&townmodori;
		}
	} else {
print <<"HTM";
�����A������Ⴂ�B<br>���O�����l�̖��@��\�\\��\��\���ė����̂��H<br>
<nobr>���O���������Ă���z���A<br>
���̉��l�̖��@�ŋ������Ă���B<br></nobr><br>

HTM
	
		if ( $chastats[12] eq $chagold ){
print <<"HTM";
$chaname�l�͂��łɌ��C�����ς��̂悤�ł��ˁ�<br>
�܂��̂����������҂����Ă���܁`���B<br>
HTM
&townmodori;
		} else {
print <<"HTM";
<nobr>�Œ�ł�<b>100,000</b>�f�����Ă���Ȃ��Ⴀ�A<br>���̖��@�͎g���Ă��Ȃ��񂾂��B</nobr><br>
�������񂾂�H<br><br></td><td>
<form method="post" action="./$zonecgi">
<input type=hidden value="2" name="sisetu">
<input type=hidden value="1" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="     �S�z����     ">
</form><br>

HTM
&townmodori;
		}







	}
} elsif ( $in{sisetu} eq "3"){
require "./$shopcgi";
} elsif ( $in{sisetu} eq "4"){
require "./$koyacgi";
} elsif ( $in{sisetu} eq "5"){
require "./$kenkyucgi";
} elsif ( $in{sisetu} eq "6"){
require "./$jiincgi";
} elsif ( $in{sisetu} eq "7"){
require "./$tyouroucgi";
} elsif ( $in{sisetu} eq "10"){
require "./$yuubincgi";
} elsif ( $in{sisetu} eq "11"){
require "./$sitiyacgi";
} elsif ( $in{sisetu} eq "12"){
require "./kojin.cgi";
} elsif ( $in{sisetu} eq "13"){
require "./daiku.cgi";

} else {
	if ($chatwin == 1 ) { $chatoth = "target=\"sakaba\""; }
print <<"HTM";
<center>
<table border=0><tr>
<td width=300><nobr><font size=6 color=#$mojiiro2><b>$zone[115]</b></font></nobr></td>
<td align=center>
<form method="post" action="./$zonecgi">
<input type=hidden value="116" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="�X�m�[�q���@��" size=30>
</form>
</td></tr></table><br><hr>
<br>
<table border=0><tr><td>
<table border=1><tr><td>
<img src="$maindir/$imgfile/zonepic115.gif">
</td></tr></table>
</td><td width=100></td><td>
<table border=0><tr><td colspan=3 align=center>
<font size=5 color=#$mojiiro3><b>�X�̎{��  </b></font><br><br></td></tr>
</td><td width=100>
<form method="post" action="./$zonecgi">
<input type=hidden value="1" name="sisetu">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="�@  $sisetu[1]  �@">
</form>
</td></tr>

</td><td width=100>
<form method="post" action="./$zonecgi">
<input type=hidden value="2" name="sisetu">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="�@ $sisetu[2] �@">
</form>
</td></tr>



</td><td width=100>
<form method="post" action="./$zonecgi">
<input type=hidden value="10" name="sisetu">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="$sisetu[10]">
</form>
</td></tr>




</td><td width=100>
<form method="post" action="./bar.cgi" $chatoth>
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="$sisetu[9]">
</form></td></tr>


</table>

</td></tr></table>
<br><br>
HTM

}

&pettukitable;
&hpowari;

sub topsisetu {
print <<"HTM";
<center>
<table border=0><tr>
<td width=400><nobr><font size=6 color=#$mojiiro2><b>$zone[115]�u$sisetu[$in{sisetu}]�v</b></font></nobr></td>
<td align=center width=200>
</td></tr></table><br><hr>
<br>
<table border=0><tr><td>
<table border=1><tr><td>
<img src="$imgfile/sisetupic$in{sisetu}.gif"></td></tr></table></td><td width=40></td><td>
HTM
}

sub townmodori {
print <<"HTM";
<br>
<form method="post" action="./$zonecgi">
<input type=hidden value="" name="sisetu">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="     �X�֖߂�     ">
</form></td></tr></table>
<br>
<hr>
HTM
}
1;