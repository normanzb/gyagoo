#�@�{�X�̖��O
$bossname ="�o�O�^�[�~�l�[�^�[";

#�@�퓬�J�n�O�̃Z���t
@boss = ( "�O�c�O�c�Ǝς�������n��̂�����",
	"��������̂��ꂵ���قǂ̏����������B<br>",
	"$chaname �͓����ւƑ����^�񂾁E�E�E");
@boss1 = ("��̐��u���҂��E�E�E�v<br>",
	"�h�X���������������ɋ����n��B",
	"�ǂ����O���̈ł̒��ɂ����߂�",
	"����ȕ��̂��甭�����Ă��鐺�̂悤���B",
	"�Â����Ďp���m�F�ł��Ȃ��B");
@boss2 = ("��̐��u�n�n�n�n�A�����Ǝv������",
	"�o�O�̌����̂��o�܂����B�v<br>",
	"(�o�O�̌����H�H�@�ǂ������Ӗ����낤�E�E",
	"�������A�o�O�H�@���@�O�[�Ƃ͂܂��ʂ̕����H)<br>",
	"��̐��u�I�}�G�B����킴�킴�o�����Ă���Ƃ͂ȁB",
	"�܁[�悢�B�������낻��s�����N��������",
	"�v���Ă����Ƃ��낾�B<br>",
	"(���̘b���H�@�S���������ł��Ȃ��E�E)<br>");
@boss3 = ("�u�䂪���� <b>$bossname</b> �I�I",
	"�o�O���I�������邽�߂ɐ��܂ꂵ�ҁB",
	"�l�Ԃǂ����ł����邽�߂�",
	"���̐��ɐ����󂯂��̂��I<br>",
	"�I�}�G�B�Ɏc���ꂽ���͂�����B",
	"���̎��ɎE����邱�Ƃ��I�I�v<br>",
	"���̕��͓̂ˑR�P���������Ă������I�I");

#�@�퓬�I����̃Z���t
@boss4 = ("�u������������������������",
	"�ȁA���̂��I�@���̂��̎���������̂��I",
	"���͖��G�ȑ��݂Ƃ��Ă��̐��E�ɐ��a���ꂽ�͂������I",
	"������o�O�̈���Ƃ����̂��E�E�E�v<br>",
	"(���G�H ���a�H �o�O�H ��͐[�܂�΂��肾�E�E�E)");
@boss5 = ("�u�o���Ă����A�o�O�̌�����",
	"�I�}�G�B���ł�����܂�",
	"���͉��x�ł���݂�����ł��낤�B",
	"���c�̎�ɂ���ĂȁB�n�n�n�n�n�n�n�n�v<br>",
	"�傫�ȏ΂����ƂƂ��� $bossname �͏��ł����B");
@boss6 = ("(���c���ƁH ���҂��̎�ɂ����",
	"�A�C�c�͐��ݏo���ꂽ�Ƃ����̂��H�H",
	"$bossname �̓��@�O�[�ł͂Ȃ��o�O�ƌ������E�E",
	"����Ȃ����Ƃ���������ȁE�E�E)<br>",
	"�������̓���c���A���̏����ɂ����B");

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
$chaplace = 0;
if ( $flag3 eq "" ) { $flag3 = 3; }
&charadatawrt;
	foreach $serifu (@boss6) {
		print "$serifu<br>";
	}

print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="$itemstats2" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="$zone[0] �֋A��" ><br></td></tr></table>
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
<input type=submit value="  ����  " ><br></td></tr></table>
</form>
HTM
}
1;