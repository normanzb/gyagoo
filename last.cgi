#!/usr/bin/perl
#�@���T�[�o�[�̐ݒ�ɍ��킹�ĕύX���Ă��������B

@last = ("���V�̉ƁE���̊�","�����̋���","���̐��̉ʂ�");

####################
require "./settei.cgi";
require "./cgi-lib.pl";
&ReadParse;

&cookieget;
&ipblock;
&gaibublock;

&charadataload;


if ( $chapass ne $in{usrpass} ) { &CgiError('�p�X���[�h�G���[','�p�X���[�h���Ⴂ�܂��B�ēx���O�C����ʂ����蒼���Ă��������B');exit; }
&cookieset;

if ( $flag2 == 2 ) { $flag2 = 3;&charadatawrt;}
if ( $bgurl ne "" ){
	$bgmode = "background=\"$bgurl\"";
} else {
	$bgmode = "bgcolor=\#$bgclr";
}

print <<"HTM";
Content-type: text/html

<html><head><title>$title</title>
<STYLE type="text/css">
A { text-decoration: none }
</STYLE>

</head>
<body $bgmode link=#$linkiro vlink=#$vlinkiro>
<basefont size=2 color=#$mojiiro><br>
<center>
HTM

if ( $in{key} < 11 ) {
print <<"HTM";
<table border=0><tr>
<td width=300><nobr><font size=6 color=#$mojiiro2><b>$last[$in{last}]</b></font></nobr></td>
</td></tr></table><br><hr>
<br>
<table border=0><tr><td>
<table border=1><tr><td>
<img src="$maindir/$imgfile/lastpic$in{last}.gif">
</td></tr></table>
</td><td width=100></td><td>
HTM
}

if ( $in{key} == 1 ) {
print <<"HTM";
�������ɂ݂��d���Ή΂ɑ̒����т��B<br>
���ɂ��̂����������ꂻ�����B<br><br>
�i���̂܂܎���ł��܂��̂ł́E�E�E�E�j<br><br>
����ȍl���������悬�������A<br>
<font color=#$chamoji><b>$chaname</b></font> �͌��m��ʏꏊ�ɗ����Ă����B<br>
<form method="post" action="./last.cgi">
<input type=hidden value="2" name="last">
<input type=hidden value="2" name="key">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="  ����  ">
</form>
HTM

} elsif ( $in{key} == 2 ) {
print <<"HTM";
�_�C�̂悤�Ȃ��̂��ӂ��ʂɍL�����Ă���B<br><br>
�i�ǂ��������́H�@�V�E�H�@�_�̍��H�j<br><br>
�����͐��ɐl�Ԃ������ł���<br>
�Ɋy��y���̂��̂������̂��B<br><br>
<font size=+1 color=#$mojiiro2>�u���A�܂��o�O��₪���������I�v</font><br><br>
�ˑR�A���̂悤�ȓ{�萺�������n�����I<br>
<font color=#$chamoji><b>$chaname</b></font> �͔��˓I�ɐg�\\����I<br>
�������A�T�d�ɕӂ�����񂵂���������������Ȃ������B<br><br>
<form method="post" action="./last.cgi">
<input type=hidden value="2" name="last">
<input type=hidden value="3" name="key">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="  ����  ">
</form>
HTM
} elsif ( $in{key} == 3 ) {
print <<"HTM";
���΂炭����ƁA�ڑO�ɃX�[�b�ƌ��m��ʐl�������ꂽ�I<br>
���邩��ɍ��M�Ȏp�����Ă���B<br>
�l�Ԃł͂Ȃ��悤���E�E�E�E�_���I�H<br>
���̐l���͓Ƃ茾�̂悤�ɂ���ׂ肾�����B<br><br>
�u�J���҂߁A�����������ɂȂ�����<br>
�@���̃o�O�𒼂��Ă����񂾁B<br>
�@�A������悱���˂����E�E�E�q�h�C�b���B�v<br><br>
�i�J���ҁH�@�o�O�H�j<br>
<form method="post" action="./last.cgi">
<input type=hidden value="2" name="last">
<input type=hidden value="4" name="key">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="  ����  ">
</form>
HTM
} elsif ( $in{key} == 4 ) {
print <<"HTM";
�u�����ƁA���܂�ȁB<br>
�@���{��ŉ��Y��Ă��܂����B<br>
�@�����Ȃ�̂��Ƃŉ����N�������̂�<br>
�@�킩��Ȃ��Ƃ������Ƃ��낾�낤�B<br>
�@���������󋵐��������Ă�낤����Ȃ����B�v<br>
<form method="post" action="./last.cgi">
<input type=hidden value="2" name="last">
<input type=hidden value="5" name="key">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="  ����  ">
</form>

HTM
} elsif ( $in{key} == 5 ) {
print <<"HTM";
�u���͂��̃Q�[���̊Ǘ��l���B<br>
�@���O��͐_�Ƃ����Ăѕ��ŌĂ�ł��邪�ȁB�v<br><br>
<font color=#$chamoji>�u�Q�[�����ƁH�@�ǂ������Ӗ����I�v</font><br><br>
�u�������B�Q�[�����B<br>
�@���O��͑S���A���̃v���[����<br>
�@�Q�[���̒��̏Z���Ȃ̂���B<br>
�@�܁A�ˑR����Ȃ��Ƃ������Ă�<br>
�@�M�����Ȃ��Ƃ͎v�����ȁB�v<br><br>
���t���o�Ȃ��E�E�E�B<br>
����ɐ_�Ɩ����҂͑������B<br>
<form method="post" action="./last.cgi">
<input type=hidden value="2" name="last">
<input type=hidden value="6" name="key">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="  ����  ">
</form>
HTM
} elsif ( $in{key} == 6 ) {
print <<"HTM";
�u���ꂱ��������疜�N�v���[�������Ă���B<br>
�@����[�A���O�B�l�ԂƂ����푰���a����������<br>
�@�{���Ɋ�񂾂�B<br>
�@���ɑf���炵�����]�������Ă�������ȁB<br>
�@���̃v���[���[�Ɏ������܂��������B�v<br><br>
�i�����̘b�͐^���Ȃ̂��낤���E�E�j<br>
<form method="post" action="./last.cgi">
<input type=hidden value="2" name="last">
<input type=hidden value="7" name="key">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="  ����  ">
</form>
HTM
} elsif ( $in{key} == 7 ) {
print <<"HTM";
�u���A�������B���̐l�ԂƂ����푰��<br>
�@���̓Q�[���̃v���[�ɑ傫�ȊQ�������炷<br>
�@�푰�������̂��B<br>
�@�����o�ɂꂻ�ꂪ�����ɕ\\�ꂾ�����B<br><br>
  ���O��l�Ԃ͐퓬�ӗ~����������̂���B<br>
�@�������������a���������V�푰�������ɐ�ŁA<br>
�@�Ȃ̗~�𖞂������߂Ɋ��j��A<br>
�@�������̉ʂĂɂ̓Q�[���̐��E����<br>
�@�����֔�яo���o�O�܂ŋN�����悤�ɂȂ�₪�����B�v<br><br>
�i�E�E�E�E�E�B�j<br>
<form method="post" action="./last.cgi">
<input type=hidden value="2" name="last">
<input type=hidden value="8" name="key">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="  ����  ">
</form>
HTM
} elsif ( $in{key} == 8 ) {
print <<"HTM";
�u�������B�悭�����B<br>
�@���̃Q�[���͐����ł񂾎��_��<br>
�@�Q�[���I�[�o�[�ɂȂ��Ă��܂��̂���B<br>
�@���O�B�l�Ԃ��������̂܂܎���̗~�]�̂��߂�<br>
�@���\\�𑱂����獢��̂͂��O�B���g�ł͂Ȃ��̂��H�v<br>
�@
<form method="post" action="./last.cgi">
<input type=hidden value="2" name="last">
<input type=hidden value="9" name="key">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="  �������ɂ��̂Ƃ��肩������Ȃ��E�E  "><br>
<input type=submit value="  �Ⴆ�������Ƃ��Ă��E�E�E�E  "><br>
<input type=submit value="  ���Ƃ�����l�Ԃ͖łԂ����Ȃ��̂��E�E�H  "><br>
</form>

HTM
} elsif ( $in{key} == 9 ) {
print <<"HTM";
�u�悭�悭�l���邱�Ƃ��ȁB�Ȃ̍s�����B<br>
�@�܂��A�ǂ��A�����ւ��ǂ蒅�����J������낤�B�v<br><br>
<font color=#$chamoji>�u�J���H�v</font><br><br>
�u�������B���O�̖]�ފ肢��<br>
�@���ł����Ȃ��Ă�邼�B<br>
�@�����肤�H�v<br>
<form method="post" action="./last.cgi">
<input type=hidden value="2" name="last">
<input type=hidden value="10" name="key">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=text name="negai" maxlength=41 size=40>(20���ȓ�)<br><br>
<input type=submit value="  ����  ">
</form>

HTM
} elsif ( $in{key} == 10 ) {
	if ( $in{negai} eq "" ) {
print <<"HTM";
�u�t�n�n�n�n�n�I<br>
�@���ł��肢�����Ȃ��Ă��Ƃ����̂�<br>
�@�]�݂��Ȃ����ƁH<br>
HTM
        } elsif ( length($in{negai}) > 40 ) {
print <<"HTM";
�u�n���҂����I<br>
�@�肢��20���ȓ����Ƃ������ł��낤�����I<br>
HTM
	} else {
print <<"HTM";
�u�n�[�n�n�n�n�n�b�I<br>
�@<b>$in{negai}</b><br>
�@���ƁH�@���ł��肢�����Ȃ��Ă��Ƃ����̂�<br>
�@�o�����t�����ꂩ�H<br>
�@�Ȃ񂽂関�n�B<br>
HTM
	}
print <<"HTM";
<br>
�@�䂪�Q�[���̖����̗쒷��<br>
�@���̒��x�̃��x���������Ƃ͂ȁB<br>
�@���O�B�ɂ͎��]������B<br><br>
�@�C���ς�����B<br>
�@��͂肨�O��l�Ԃ͖łڂ����Ƃɂ��悤�B<br>
�@�܂��͂��O���ŏ����I�I�I<br><br>
<form method="post" action="./last.cgi">
<input type=hidden value="2" name="last">
<input type=hidden value="11" name="key">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="  �퓬�J�n�I  ">
</form>
HTM

} elsif ( $in{key} == 11 ) {
print <<"HTM";
<center><font size=6 color=#ff00ff><b>�_</b> �Ƃ̐퓬�J�n�I�I</font><hr><br>
<table border=0><tr><td bgcolor=#009900 align=center>
  <font size=4><nobr><b>1 �^�[����</b></nobr></font></td></tr><tr><td>
<table border=0>
<tr align=center valign="baseline"><td>
<img src="./pics/god.gif"></td><td></td><td>
</td><td>
<iframe name="charaga" src="./charapic.cgi?atama=8&hada=d0ffd0&eye=2&hana=14&kuti=16&kami=3&leg=tabi&arm=&hlm=&che=tabi&wp=dagger&sld=" frameborder=0 scrolling=no width=100 height=125></iframe>
</td><td></td><td></td></tr><tr align=center><td>
<font size=4><nobr>�_</font></nobr></td>
<td width=20 rowspan=2><nobr><font size=4 color=#ff0000><b>VS</b></font></nobr></td>
<td colspan=3><font size=4><nobr>$chaname</font></nobr></td><td></td></tr>
<tr><td><nobr><img src="./pics/exp.gif" height="8"><img src="./pics/expbar1.gif" width=150 height="8"><img src="./pics/exp.gif" height="8"></nobr></td><td colspan=3><font size=4><nobr><img src="./pics/exp.gif" height="8"><img src="./pics/expbar1.gif" width=150 height="8"><img src="./pics/exp.gif" height="8"></nobr></td><td></td></tr>
</table><br><br><font size=4>
<font color=#$chamoji><b>$chaname</b></font> �̍U���I�I<br>�������A�_�͔������ɂ��Ȃ������I<br><br>
<b>�_</b> �̍U���I�I<br>
  �u��u�Ŋy�ɂ��Ă�낤�B�v<br>
    �܂΂䂢�����_�̉E��ɏW�����������I�I<br><br>
      <font size=+2 color=#007700><b>�S�b�h�n���h�@�I�I�I</b></font> <br><br>
<font color=#0000ff>$chaname ��<font color=#ff0000>21589</font>�̃_���[�W���󂯂��I�I<br></font></td></tr></table><br><br>
<br><br><font size=5 color=#0000ff><b>$chaname</b> �͐퓬�ɕ������E�E�E</font><br><br>
<form method="post" action="./last.cgi">
<input type=hidden value="12" name="key">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value=" ���� " ></form></td></tr></table>
<br><hr>
HTM

} elsif ( $in{key} == 12 ) {
print <<"HTM";
  <font size=6 color=#ff0000><b>�G���f�B���O</b></font><br><br>
  ����䂭�ӎ��̒��A�_�̓Ƃ茾�����ɓ������B<br><br>
<table border=0><tr><td>
�u�t���B�����҂��E�E�E�E�B<br>
�@������ł����ɏ��Ă�Ƃł��v�����̂��H<br>
�@�_��������ɂ����悤�Ƃ��邻�̐퓬�ӗ~�E�E�E�B<br>
�@���߂ɂ��O��l�Ԃ��Ȃ�Ƃ����˂�<br>
�@���̂܂܃Q�[�����I�����Ă��܂��������ȁB<br><br>
�@�Ƃ肠�����A���̃o�O���C�����Ă��炤�̂��悩�E�E�E�E�@�v<br>
</td></tr></table><br>
�E�E�E�E�E�E�E�E�E�E�E�E�E�E�E�E<br><br>
�E�E�E�E�E�E�E�E�E�E�E�E�E<br><br>
�E�E�E�E�E�E�E�E�E�E<br><br>
�E�E�E�E�E�E�E<br><br>
�E�E�E�E<br><br>
  <br><br><br>
�ӎ����߂�Ƃ����͌��̐��E�������B<br><br>
��X�l�Ԃ͂��̐�ǂ�����΂����̂��E�E�E<br><br>
���܂ōl���Ă������͏o�Ă��Ȃ������B<br><br><br>
�������A������͂����肵�Ă��邱�Ƃ�����B<br><br>
����͉�X�����c�̃v���[����Q�[���̒��̏Z�l�ł��邱�Ƃ��B<br><br><br><br>
HTM

} else {
print <<"HTM";
<font color=#$chamoji><b>$chaname</b></font> �͋��鋰�鉜�̕����ւƐi�񂾁B<br>
���������̂Ȃ��Èł��������A�O���ɉ�����a�����������B<br>
�悭����Ƃ��̕���������Ԃ��c��ł���悤���B<br><br>
�i���ꂩ�牽���N����񂾂낤�E�E�E�j<br><br>
�E�C��U��i�肻�̘c�݂ɔ�э��񂾁I�I<br>
HTM


$chaplace = 301;
if ( $flag2 eq "" ) { $flag2 = 3; }
&charadatawrt;
	foreach $serifu (@boss7) {
		print "$serifu<br>";
	}

print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="���݂̓��A�@��" ><br></td></tr></table>
</form>
HTM
}
print "</td></tr></table>";
&hpowari;
exit;
