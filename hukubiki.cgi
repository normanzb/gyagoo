&topsisetu;
print <<"HTM";
��������Ⴂ�I<br>
�������������Ă���Ε������o�����I<br><br>
HTM
if ( $in{riyou} eq "1" ) {
	if ( $hukubiki < 1) {
print <<"HTM";
<b><font color=red>�������������Ă��܂���B</font></b><br>
HTM
		} else {
$keihin = int( rand(5000) );
		if ( $keihin < 1 ) {
if (!open(BANKI,">>$maindir/$foldacha/bankit_$in{usrid}$bousi2cha$bousikts")) { &CgiError('�G���[����','�t�@�C���I�[�v���Ɏ��s���܂����B'); }
flock(BANKI,2);
	print BANKI "�������O�i���N/DMG 50�ASTR +30�AAGI +30�ASVM +30\n";
flock(BANKI,8);
close(BANKI);
print <<"HTM";
<font size=6 color=#$mojiiro3><b>����</b></font>�@<font color=#$chamoji><b>�������O�i���N</b></font>��������܂����I<br><br>
HTM
$hukubiki --;
&charadatawrt;

		} elsif ( $keihin < 3 ) {
if (!open(BANKI,">>$maindir/$foldacha/bankit_$in{usrid}$bousi2cha$bousikts")) { &CgiError('�G���[����','�t�@�C���I�[�v���Ɏ��s���܂����B'); }
flock(BANKI,2);
	print BANKI "�}�[���C�h�����O/�l��EXP��2�{�ɂ���\n";
flock(BANKI,8);
close(BANKI);
print <<"HTM";
<font size=6 color=#$mojiiro3><b>�P��</b></font>�@<font color=#$chamoji><b>�}�[���C�h�����O</b></font>��������܂����I<br><br>
HTM
$hukubiki --;
&charadatawrt;

		} elsif ( $keihin < 10 ) {
if (!open(BANKI,">>$maindir/$foldacha/bankit_$in{usrid}$bousi2cha$bousikts")) { &CgiError('�G���[����','�t�@�C���I�[�v���Ɏ��s���܂����B'); }
flock(BANKI,2);
	print BANKI "�S�_�̔��/�e�X�e�[�^�X��啝�ɏグ��\n";
flock(BANKI,8);
close(BANKI);
print <<"HTM";
<font size=6 color=#$mojiiro3><b>�Q��</b></font>�@<font color=#$chamoji><b>�S�_�̔��</b></font>��������܂����I<br><br>
HTM
$hukubiki --;
&charadatawrt;

		} elsif ( $keihin < 20 ) {
if (!open(BANKI,">>$maindir/$foldacha/bankit_$in{usrid}$bousi2cha$bousikts")) { &CgiError('�G���[����','�t�@�C���I�[�v���Ɏ��s���܂����B'); }
flock(BANKI,2);
	print BANKI "�_���ۖ�/�ő�TP��30�グ��\n";
flock(BANKI,8);
close(BANKI);
print <<"HTM";
<font size=6 color=#$mojiiro3><b>�R��</b></font>�@<font color=#$chamoji><b>�_���ۖ�</b></font>��������܂����I<br><br>
HTM
$hukubiki --;
&charadatawrt;

		} elsif ( $keihin < 35 ) {
if (!open(BANKI,">>$maindir/$foldacha/bankit_$in{usrid}$bousi2cha$bousikts")) { &CgiError('�G���[����','�t�@�C���I�[�v���Ɏ��s���܂����B'); }
flock(BANKI,2);
	print BANKI "�V���ۖ�/�ő�TP��10�グ��\n";
flock(BANKI,8);
close(BANKI);
print <<"HTM";
<font size=6 color=#$mojiiro3><b>�S��</b></font>�@<font color=#$chamoji><b>�V���ۖ�</b></font>��������܂����I<br><br>
HTM
$hukubiki --;
&charadatawrt;

		} elsif ( $keihin < 100 ) {
print <<"HTM";
<font size=6 color=#$mojiiro3><b>�T��</b></font>�@<font color=#$chamoji><b>700</b></font>�b�o��������܂����I<br><br>
HTM
$chastats[14] += 700;
$hukubiki --;
&charadatawrt;

		} elsif ( $keihin < 200 ) {
print <<"HTM";
<font size=6 color=#$mojiiro3><b>�U��</b></font>�@<font color=#$chamoji><b>5000</b></font>�f��������܂����I<br><br>
HTM
$chagold += 5000;
$hukubiki --;
&charadatawrt;

		} elsif ( $keihin < 300 ) {
print <<"HTM";
<font size=6 color=#$mojiiro3><b>�V��</b></font>�@<font color=#$chamoji><b>������</b></font>�T����������܂����I<br><br>
HTM
$hukubiki --;
$hukubiki += 5;
&charadatawrt;

		} elsif ( $keihin < 450 ) {
if (!open(BANKI,">>$maindir/$foldacha/bankit_$in{usrid}$bousi2cha$bousikts")) { &CgiError('�G���[����','�t�@�C���I�[�v���Ɏ��s���܂����B'); }
flock(BANKI,2);
	print BANKI "�_��/HP�TP��S��\n";
flock(BANKI,8);
close(BANKI);
print <<"HTM";
<font size=6 color=#$mojiiro3><b>�W��</b></font>�@<font color=#$chamoji><b>�_��</b></font>��������܂����I<br><br>
HTM
$hukubiki --;
&charadatawrt;

		} elsif ( $keihin < 1200 ) {
if (!open(BANKI,">>$maindir/$foldacha/bankit_$in{usrid}$bousi2cha$bousikts")) { &CgiError('�G���[����','�t�@�C���I�[�v���Ɏ��s���܂����B'); }
flock(BANKI,2);
	print BANKI "�^�u���b�g��/TP��120��\n";
flock(BANKI,8);
close(BANKI);
print <<"HTM";
<font size=6 color=#$mojiiro3><b>�X��</b></font>�@<font color=#$chamoji><b>�^�u���b�g��</b></font>��������܂����I<br><br>
HTM
$hukubiki --;
&charadatawrt;

		} elsif ( $keihin < 2500 ) {
if (!open(BANKI,">>$maindir/$foldacha/bankit_$in{usrid}$bousi2cha$bousikts")) { &CgiError('�G���[����','�t�@�C���I�[�v���Ɏ��s���܂����B'); }
flock(BANKI,2);
	print BANKI "�G�N�X�|�[�V����/HP��1200��\n";
flock(BANKI,8);
close(BANKI);
print <<"HTM";
<font size=6 color=#$mojiiro3><b>�P�O��</b></font>�@<font color=#$chamoji><b>�G�N�X�|�[�V����</b></font>��������܂����I<br><br>
HTM
$hukubiki --;
&charadatawrt;

		} else {
print <<"HTM";
<font size=6><b>�c�O�E�E�E�n�Y���I</b></font><br><br>
HTM
$hukubiki --;
&charadatawrt;

}
	}
}



if ( $in{riyou} eq "2" ) {
	if ( $hukubiki < 10) {
print <<"HTM";
<b><font color=red>������������܂���B</font></b><br>
HTM
		} else {
if (!open(BANKI,">>$maindir/$foldacha/bankit_$in{usrid}$bousi2cha$bousikts")) { &CgiError('�G���[����','�t�@�C���I�[�v���Ɏ��s���܂����B'); }
flock(BANKI,2);
	print BANKI "�ۖ�/�ő�TP��1�グ��\n";
flock(BANKI,8);
close(BANKI);
print <<"HTM";
<b>������10���ƁA�ۖ���������܂����B</b><br><br>
HTM
$hukubiki -= 10;
}
&charadatawrt;
}

if ( $in{riyou} eq "3" ) {
	if ( $hukubiki < 50) {
print <<"HTM";
<b><font color=red>������������܂���B</font></b><br>
HTM
		} else {
if (!open(BANKI,">>$maindir/$foldacha/bankit_$in{usrid}$bousi2cha$bousikts")) { &CgiError('�G���[����','�t�@�C���I�[�v���Ɏ��s���܂����B'); }
flock(BANKI,2);
	print BANKI "�V���ۖ�/�ő�TP��10�グ��\n";
flock(BANKI,8);
close(BANKI);
print <<"HTM";
<b>������50���ƁA�V���ۖ���������܂����B</b><br><br>
HTM
$hukubiki -= 50;
}
&charadatawrt;
}




&kunrenform;
sub kunrenform {
print <<"HTM";
<font size=-1>���݂̕�����</font>�F<b>$hukubiki</b><font size=-1>��</font>
<form method="post" action="./$zonecgi">
<input type=hidden value="15" name="sisetu">
<input type=hidden value="1" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="   ����������   " size=30>�@�y������<b>�P</b>���z
</form>
<form method="post" action="./$zonecgi">
<input type=hidden value="15" name="sisetu">
<input type=hidden value="2" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="   �ۖ�ƌ���   " size=30>�@�y������<b>�P�O</b>���z
</form>
<form method="post" action="./$zonecgi">
<input type=hidden value="15" name="sisetu">
<input type=hidden value="3" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="�V���ۖ�ƌ���" size=30>�@�y������<b>�T�O</b>���z
</form>

<SCRIPT language="JavaScript">
<!--
function OpenWin(){
win=window.open("./fukubiki.html","new","width=240,height=305");
}
// -->

</SCRIPT>
</HEAD>

<BODY>
<INPUT type="button" value="�@�@�i�i�ꗗ�@�@" onClick="OpenWin()">
</BODY>



HTM
}
&townmodori;
1;