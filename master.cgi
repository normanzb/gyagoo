#!/usr/bin/perl

#�@���T�[�o�[�̐ݒ�ɍ��킹�ĕύX���Ă��������B

###############
#
# �uVagoo(ver1.03)�v�@2001�N10��26���z�z�J�n
#�@�@�@�X�N���v�g����ҁ@�X�J�C�igame@sky-wing.com�j
#
#�@�_�E�����[�h�K��𓯈ӂ������̂݁A�uVagoo�v�X�N���v�g�ނ̎g�p�������܂��B
#
#�@�z�z��HP�u�����ԂȂ����ށvhttp://www.sky-wing.com/~game/
#
###########

require "./settei.cgi";
require "./cgi-lib.pl";
&ReadParse;
&ipblock;
&gaibublock;
&hpsaisyo;

if ( $in{mode} ne "" && $adminp ne $in{adminpass}) {
print <<"HTM";
<center><font size=7>�p�X���[�h�G���[</font></center>
HTM
exit;
}

print "<center><font size=6 color=#$mojiiro2><b>�Ǘ����[�h</b></font><br><hr>";

if ( $in{mode} == 1 ){
&adminform;
} elsif ( $in{mode} == 2 ){

# �����؂�폜

&adminback;
print "�ȉ���ID�������؂�ō폜����܂����B<br><br><table border=0><tr><td>";

open(CHA,"$maindir/$foldacha/user_id$bousi2cha$bousikts2");
	while ( $chadata = <CHA> ) {
		chop($chadata);
		($id,$name) = split(/\//,$chadata);
open(DAT,"$maindir/$foldacha/$bousicha$id$bousikts");
	($chaid,$chapass,$chaname,$chaurl,$chamoji,$chaip,$chajikan) = split(/,/,<DAT>);
		if ($now > $chajikan + ($datadelete*24*60*60) ) { push(@sakujo,$chaid); }
close(DAT);
	}

close(CHA);

	foreach $kesi (@sakujo) {
unlink("$maindir/$foldacha/$bousicha$kesi$bousikts");
unlink("$maindir/$foldacha/bankit_$kesi$bousi2cha$bousikts");
unlink("$maindir/$foldacha/pet_$kesi$bousi2cha$bousikts");
unlink("$maindir/$foldacha/bankg_$kesi$bousi2cha$bousikts");
unlink("$maindir/$foldacha/tegami_$kesi$bousi2cha$bousikts");
unlink("$maindir/$foldazukan/pet1$kesi$bousicha$bousikts");
unlink("$maindir/$foldazukan/pet2$kesi$bousicha$bousikts");
unlink("$maindir/$foldazukan/pet3$kesi$bousicha$bousikts");
	}

open(CHA,"$maindir/$foldacha/user_id$bousi2cha$bousikts2");
open(DEL,">$maindir/$foldacha/user_id.tmp");
	while ( $chadata = <CHA> ) {
	chop($chadata);
	($id,$name) = split(/\//,$chadata);
		foreach $kesi (@sakujo) {
			if ( $id eq $kesi ) { print "�E $kesi<br>\n";$abes = 1;next; } 
		}
	if ( $abes != 1 ) {print DEL "$chadata\n";}
	$abes = 0;
	}
close(DEL);
close(CHA);

rename("$maindir/$foldacha/user_id.tmp","$maindir/$foldacha/user_id$bousi2cha$bousikts2");
print "</td></tr></table>";

} elsif ( $in{mode} == 3 ){

#�@�w��L�����f�[�^�폜

&adminback;
print <<"HTM";
�폜����L�����Ƀ`�F�b�N�����Ă��������i�����j�B<br>
�P�x�폜�����f�[�^�͂����߂�܂���B<br>
�T�d�ɑ�����s���Ă��������B<br><br>
<form action="./$admincgi" method="post">
<input type=hidden name="adminpass" value="$in{adminpass}">
<input type=hidden name="mode" value="31">
<input type=submit value="�I���L�����f�[�^�폜">
<table border=1>
HTM
$tourokunum = 1;
open(CHA,"$maindir/$foldacha/user_id$bousi2cha$bousikts2");
flock(CHA,2);
	while ( $chadata = <CHA> ) {
		chop($chadata);
		($id,$name) = split(/\//,$chadata);
	open(DAT,"$maindir/$foldacha/$bousicha$id$bousikts");
		($chaid,$chapass,$chaname,$chaurl,$chamoji,$chaip) = split(/,/,<DAT>);
print <<"HTM";
<tr><td><input type=checkbox name="kariusrid" value="$chaid\"></td><td>$tourokunum</td><td><nobr>$chaid</nobr></td>
<td><nobr>$chapass</nobr></td><td><nobr>$chaname</nobr></td><td><nobr>$chaip</nobr></td></tr>
HTM
	close(DAT);
$tourokunum ++;
	}
flock(CHA,8);
close(CHA);

print "</table></form>";

} elsif ( $in{mode} == 31 ){
&adminback;
print "�ȉ���ID���폜����܂����B<br><br>";
	@sakujo = split(/\0/,$in{usrid});
open(CHA,"$maindir/$foldacha/user_id$bousi2cha$bousikts2");
	open(DEL,">>$maindir/$foldacha/user_id.tmp");
	while ( $chadata = <CHA> ) {
		chop($chadata);
		($id,$name) = split(/\//,$chadata);
		foreach $kesi (@sakujo) {
			if ( $id eq $kesi ) { print "�E $kesi<br>\n";$abes = 1;next; } 
		}
		if ( $abes != 1 ) {print DEL "$chadata\n";}
		$abes = 0;
	}
	close(DEL);
close(CHA);
unlink("$maindir/$foldacha/$bousicha$kesi$bousikts");
unlink("$maindir/$foldacha/bankit_$kesi$bousi2cha$bousikts");
unlink("$maindir/$foldacha/pet_$kesi$bousi2cha$bousikts");
unlink("$maindir/$foldacha/bankg_$kesi$bousi2cha$bousikts");
unlink("$maindir/$foldacha/tegami_$kesi$bousi2cha$bousikts");
unlink("$maindir/$foldazukan/pet1$kesi$bousicha$bousikts");
unlink("$maindir/$foldazukan/pet2$kesi$bousicha$bousikts");
unlink("$maindir/$foldazukan/pet3$kesi$bousicha$bousikts");
rename("$maindir/$foldacha/user_id.tmp","$foldacha/user_id$bousi2cha$bousikts2");

} elsif ( $in{mode} == 4 ){

#�@���݃v���C���Ă���L����

open(NOW,"$maindir/playing$bousikts");
	while( $playnow = <NOW> ) {
		chop($playnow);
		($nowid,$nowname,$nowjikan) = split(/\//,$playnow);
		if ( $now < $nowjikan + 200 && $nowid ne $chaid ) {
			push(@playing,$playnow);
		}
	}
close(NOW);
$playingkazu = @playing;
&adminback;
print <<"HTM";
<center>
<table border=0 width=200><tr>
<td align=center>
���݂̖`���ҁi$playingkazu�l�j</td></tr>
HTM

foreach $playnow ( @playing ) {
	chop($playnow);
	($nowid,$nowname) = split(/\//,$playnow);
print "<tr><td>�E<a href=\"./$introcgi?usrid=$nowid\" target=\"intro\"><b>$nowname</b></a> </td></tr>";
}
print <<"HTM";
</table><br>
HTM

} elsif ( $in{mode} == 5 ){

#�@�o�^�҈ꗗ

&adminback;
$tourokunum = 1;
print <<"HTM";
<form action="./$admincgi" method="post">
<input type=hidden name="adminpass" value="$in{adminpass}">
<input type=hidden name="mode" value="51">
<input type=submit value="�I��ID�ڍ׃f�[�^">

<table border=1><tr align=center><td>-</td><td><b><nobr>No.</nobr></b></td><td><b>ID</b></td><td><b>PASS</b></td><td><b>�L������</b></td><td><b><nobr>Lv</nobr></b></td><td><b><nobr>�W���u</nobr></b></td><td><b>IP</b></td><td><b>�ŏI�A�N�Z�X��</b></td></tr>
HTM

open(CHA,"$maindir/$foldacha/user_id$bousi2cha$bousikts2");
flock(CHA,2);
	while ( $chadata = <CHA> ) {
		chop($chadata);
		($id,$name) = split(/\//,$chadata);
	open(DAT,"$maindir/$foldacha/$bousicha$id$bousikts");
		($chaid,$chapass,$chaname,$chaurl,$chamoji,$chaip,$chajikan,$a,$a,$a,$a,$chaclass,$a,$a,$a,$chalvl) = split(/,/,<DAT>);
($secl,$minl,$hourl,$mdayl,$monl,$yearl,$wdayl) = localtime($chajikan);
@weekl = ('��','��','��','��','��','��','�y');$monl ++;$wdayl = $weekl[$wdayl];
$minl = sprintf("%.2d",$minl);
$secl = sprintf("%.2d",$secl);
$hourl = sprintf("%.2d",$hourl);
print <<"HTM";
<tr><td><input type=radio name="usrid" value="$chaid"></td><td>$tourokunum</td><td><nobr>$chaid</nobr></td><td><nobr>$chapass</nobr></td><td><nobr>$chaname</nobr></td><td>$chalvl</td><td>$job[$chaclass]</td><td><nobr>$chaip</nobr></td><td><nobr>$monl��$mdayl��($wdayl) $hourl:$minl:$secl</nobr></td>
<td>
<a href="./zone.cgi?usrid=$chaid&usrpass=$chapass" target="_zone">��</a>
</td>
</tr>

HTM
	close(DAT);
$tourokunum ++;
	}
flock(CHA,8);
close(CHA);

print <<"HTM";
</table></form>
HTM

} elsif ( $in{mode} == 51 ){
	if ( $in{usrid} eq "" ) { print "�Q�ƃL�������I������Ă��܂���B<br>";&adminback;exit; }

require "./zone.pl";

&charadataload;
&adminback;

print <<"HTM";
<center><font size=6 color=#$mojiiro2><b><font size=7 color=#$chamoji>$chaname
</font>����̃X�e�[�^�X</b></font><br><br>
<b><font size=+1>�]�[���� [ $zone[$chaplace] ]</b></font><br><br>

HTM
&pettukitable;
&itemtable;
open(BANK,"$maindir/$foldacha/bankg_$in{usrid}$bousi2cha$bousikts");
	$bankgold = <BANK>;
close(BANK);
print "<br><table border=0><tr><td>��s�̗a���F <b>$bankgold</b> G";
print "</td><td width=30></td><td><form>��s�̃A�C�e���F<br><select size=10>";

open(BANKI,"$maindir/$foldacha/bankit_$in{usrid}$bousi2cha$bousikts");
		while ( $bankno = <BANKI> ) {
		chop($bankno);
	($bankname,$bankbun) = split(/\//,$bankno);
print "<option value=\"$bankname/$bankbun/$abb\">$bankname�i$bankbun�j";
		}
close(BANKI);
print "</form></td><td width=30></td><td><form>�y�b�g�����F<br><select size=10>";
open(PET,"$maindir/$foldacha/pet_$in{usrid}$bousi2cha$bousikts");
	while ( $petkai = <PET> ) {
		chop($petkai);
print "<option value=\"$petkai\">$petkai";
	}
close(PET);
print "</select></form></td></tr></table><hr><center><font size=6 color=#$mojiiro4><b>�莆 �ꗗ</b></font><br><table border=0 width=70%><tr><td>";
	open(BANN,"$maindir/$foldacha/tegami_$in{usrid}$bousi2cha$bousikts");
		while ( $yuubin = <BANN> ) {
($kako,$chanamez,$chamojiz,$tegami,$genzai2) = split(/\t/,$yuubin);
print "<hr><font color=#$chamojiz><b>$chanamez</b></font> �F $tegami <nobr>($genzai2)</nobr>\n";
		}
	close(BANN);
print <<"HTM";
</td></tr></table><hr></center>
HTM
} elsif ( $in{mode} == 6 ){
&adminback;

open(NOW,"$maindir/chat$bousikts");
@playing = <NOW>;
close(NOW);
$playingkazu = @playing;

open(NOW,"$maindir/chat2$bousikts");
	@res = <NOW>;
close(NOW);

print <<"HTM";
<form action="./$admincgi" method="post">
<input type=hidden name="adminpass" value="$in{adminpass}">
<input type=hidden name="mode" value="6">
<input type=submit value="���ꃍ�O�{��">
</form>

</center><nobr>���݂̗��X��($playingkazu�l):
HTM
	foreach $kyaku (@playing) {
		chop($kyaku);
		($nowid,$nowname) = split(/\//,$kyaku);
		print "/ <a href=\"./$introcgi?usrid=$nowid\" target=\"intro\"><b>$nowname</b></a> <wbr>";
	}

print <<"HTM";
</nobr>
@res
HTM


} else {
print <<"HTM";
<form action="./$admincgi" method="post">
�Ǘ��p�X���[�h����͂��Ă��������B<br><br>
<input type=test size=12 name="adminpass" maxlength=10><br><br>
<input type=hidden name="mode" value="1">
<input type=submit value="   ���s   ">
</form>
HTM
}
&hpowari;

sub adminform {
print <<"HTM";
<font size=5>�Ǘ��R�}���h�ꗗ</font><br>
<form action="./$admincgi" method="post">

<input type=hidden name="adminpass" value="$in{adminpass}">
<input type=hidden name="mode" value="2">
<input type=submit value="�����؂�f�[�^�����폜">
</form>
<form action="./$admincgi" method="post">
<input type=hidden name="adminpass" value="$in{adminpass}">
<input type=hidden name="mode" value="3">
<input type=submit value="�蓮�L�����f�[�^�폜">
</form>
<form action="./$admincgi" method="post">
<input type=hidden name="adminpass" value="$in{adminpass}">
<input type=hidden name="mode" value="4">
<input type=submit value="���݂̖`���҈ꗗ">
</form>
<form action="./$admincgi" method="post">
<input type=hidden name="adminpass" value="$in{adminpass}">
<input type=hidden name="mode" value="5">
<input type=submit value="�o�^�f�[�^�ꗗ">
</form>
<form action="./$admincgi" method="post">
<input type=hidden name="adminpass" value="$in{adminpass}">
<input type=hidden name="mode" value="6">
<input type=submit value="���ꃍ�O�{��">
</form>
HTM
}

sub adminback {
print <<"HTM";
<form action="./$admincgi" method="post">
<input type=hidden name="adminpass" value="$in{adminpass}">
<input type=hidden name="mode" value="1">
<input type=submit value="�Ǘ��R�}���h�ꗗ�֖߂�">
</form><hr>
HTM
}

 

exit;
