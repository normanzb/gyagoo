#�@�{�X�̖��O
$bossname ="�o�O�^�[�~�l�[�^�[";

#�@�퓬�J�n�O�̃Z���t
@boss = ( "���Ă��Ȃ��܂܁A�Ɋ��̎R��f�r�������Ă��邤���ɁA",
	"�ӂ�͂������łɕ�܂�Ă����B<br>",
	"<b>$chaname</b>�u��́A�ǂ��܂ő����񂾁B�@���̎R�́E�E�E�B�v<br>",
	"�����Ă������Ă������悤�ȕ��i�������A",
	"�����Ɣ�J�ŁA$chaname�̗̑͂͌��E�𒴂��Ă����B<br>",
	"�E�E�E���̎��A�O���ɍ����l�e���������B<br>");

@boss1 = ("���̐l�e�́A�܂�$chaname�̑��݂ɋC�t���Ă��Ȃ��炵���A",
	"�H��̂悤�ȁA���ア���ŁA�Ȃɂ��Ƃ茾���Ԃ₢�Ă���E�E�E�B<br>",
	"<b>�H��̂悤�Ȑ�</b><font face=�L�V�s��>�u�n���������悧�`�E�E�E����ȂƂ���Ŏ��ɂ����Ȃ��悧�`�E�E�E�B�v</font><br>",
	"<b>$chaname</b>�u�E�E�E�B�v<br>");

@boss2 = ("���̐l�e�̓t���t���ɂȂ�Ȃ�����A�����ÂA������ɋ߂Â��Ă���B",
	"���ɂ��|��Ă��܂������ȑ��悾�B<br>",
	"<b>$chaname</b>�u�E�E�E�E�E�b�I�H�v<br>",
	"���̐l�e�̔w��ɁA�����X�^�[�̉e��������E�E�E�I",
	"���̂܂܂ł́A���̐l����Ȃ��I�I");

@boss3 = ("$chaname�́A���̐l�����ׁA�����X�^�[�Ɍ������đ����Ă������I<br>");

#�@�퓬�I����̃Z���t
@boss4 = ("<b>$chaname</b>�u�n�@�E�E�n�@�E�E�E�B�v",
	"�����X�^�[�Ƃ̐퓬�ɏ�������$chaname�́A",
	"�t���t���ɂȂ��Ă����l�e�̖������m�F����ׁA���`�����񂾁B<br>",
	"<b>$chaname</b>�u���A���O�́E�E�E�I�@�f�������E�E�E�I�H�v");
@boss5 = ("<b>$chaname</b>�u�E�E�E�E�E�B�v",
	"<b>�f������</b>�u�E�E�E�E�E�B�v<br>",
	"�Q�l�͌��ߍ������܂܁A���ق̎����������E�E�E�B");
@boss6 = ("���΂炭����ƁA�f�������͂������܂œ|�ꂻ���������̂��R�̂悤�ɁA",
	"�����������łǂ����֑����čs���Ă��܂����B<br>",
	"���̌�p�́A�ǂ����p���������Ɍ������E�E�E�B<br>",
	"<b>$chaname</b>�i����ɂ��Ă��A�z�͂���ȏ��ŉ������Ă����񂾁H�j<br>",
	"���炭�A����낤��\�\\�z\���A$chaname�͂��̏�𗣂�鎖�ɂ����B");

#################

if ( $in{boss} eq "" ) { $in{boss} = 0;}
print <<"HTM";
<center>
<table border=0 width=800><tr>
<td align=center><nobr><font size=6 color=#$mojiiro2><b>$zone[$chaplace]</b></font></nobr></td><td width=30></td><td><nobr>
HTM

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

if ( $in{boss} eq "3"){
	foreach $serifu (@boss3) {
		print "$serifu<br>";
	}
$in{boss} ++;
print <<"HTM";
<form method="post" action="./$battlecgi">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$in{boss}" name="boss">
<input type=hidden value="$chapass" name="usrpass">
<input type=hidden value="$chacount" name="count">
<input type=submit value="    �@ �퓬�J�n�I�@     " size=30>
</form></td></tr></table>
HTM
} elsif ( $in{boss} eq "6"){
$chaplace = 124;
if ( $flag1 eq "" ) { $flag1 = 1; }
&charadatawrt;
	foreach $serifu (@boss6) {
		print "$serifu<br>";
	}

print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="$itemstats2" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="$zone[124] ��" ><br></td></tr></table>
</form></td></tr></table>
HTM
} elsif ( $in{boss} eq "1"){
	foreach $serifu (@boss1) {
		print "$serifu<br>";
	}
&nextform;

} elsif ( $in{boss} eq "2"){
	foreach $serifu (@boss2) {
		print "$serifu<br>";
	}
&nextform;

} elsif ( $in{boss} eq "4"){
	foreach $serifu (@boss4) {
		print "$serifu<br>";
	}
&nextform;

} elsif ( $in{boss} eq "5"){
	foreach $serifu (@boss5) {
		print "$serifu<br>";
	}
&nextform;

} elsif ( $in{boss} eq "6"){
	foreach $serifu (@boss6) {
		print "$serifu<br>";
	}
&nextform;

} else {
	foreach $serifu (@boss) {
		print "$serifu<br>";
	}
&nextform;

}
print "</td></tr></table><hr>";
&pettukitable;

sub nextform {
$in{boss} ++;
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$in{boss}" name="boss">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="  ����  " onClick="window.location.replace" ><br></td></tr></table>
</form>
HTM
}
1;