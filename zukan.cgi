#!/usr/bin/perl

#�@���T�[�o�[�̐ݒ�ɍ��킹�ĕύX���Ă��������B
#�@�푰���ݒ�
$syuok[1] = "����";$syuok[2] = "���l";$syuok[3] = "��b";

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
if ( $chapass ne $in{usrpass} ) { &CgiError('�p�X���[�h�G���[','�p�X���[�h���Ⴂ�܂��B�ēx���O�C����ʂ����蒼���Ă��������B');exit; }
print "<center><font size=7 color=#$mojiiro2><b>�y�b�g�}��</b></font><br><br>";

open(PET,"$maindir/$foldazukan/pet1$in{usrid}$bousicha$bousikts");
@zukankeisai1 = <PET>;
close(PET);

open(PET,"$maindir/$foldazukan/pet2$in{usrid}$bousicha$bousikts");
@zukankeisai2 = <PET>;
close(PET);

open(PET,"$maindir/$foldazukan/pet3$in{usrid}$bousicha$bousikts");
@zukankeisai3 = <PET>;
close(PET);

$keisai[1] = @zukankeisai1;$keisai[2] = @zukankeisai2;$keisai[3] = @zukankeisai3;$soukeisai = $keisai[1] + $keisai[2] + $keisai[3];
$number =1;
print <<"HTM";
���݂̑��f�ڐ��F <font size=+1><b>$soukeisai</b></font> �C<br><hr>
HTM
print "<table border=0><tr>";
 if ( $in{syuzoku} != 1 ) {
print <<"HTM";
<td>
<form method="post" action="./zukan.cgi">
<input type=hidden value="1" name="syuzoku">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="   ���� �@">
</form></td>
HTM
}

 if ( $in{syuzoku} != 2 ) {
print <<"HTM";
<td>
<form method="post" action="./zukan.cgi">
<input type=hidden value="2" name="syuzoku">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="   ���l �@">
</form></td>
HTM
}

 if ( $in{syuzoku} != 3 ) {
print <<"HTM";
<td>
<form method="post" action="./zukan.cgi">
<input type=hidden value="3" name="syuzoku">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="   ��b �@">
</form></td>
HTM
}
print "</tr></table><br>";

print <<"HTM";
<font size=6 color=#$mojiiro4><b>$syuok[$in{syuzoku}]</b></font>
<font size=+2>( $keisai[$in{syuzoku}] �C )</font><br><br><table border=1 bgcolor=#$bgclr><tr>
HTM

if ( $in{syuzoku} == 1 ) {
	foreach $ppet (@zukankeisai1) {
		($a,$zukanname,$zukane) = split(/,/,$ppet);
print <<"HTM";
<td><b>$number</b><br><img src="$maindir/$imgfile/$zukane.gif" width="60" height="60" alt="$zukanname"></td>
HTM
		if ($number % 5 == 0 ) {
print "</tr><tr>";
		}
$number ++;
	}
} elsif ( $in{syuzoku} == 2 ) {
	foreach $ppet (@zukankeisai2) {
		($a,$zukanname,$zukane) = split(/,/,$ppet);
print <<"HTM";
<td><b>$number</b><br><img src="$maindir/$imgfile/$zukane.gif" width="60" height="60" alt="$zukanname"></td>
HTM
		if ($number % 5 == 0 ) {
print "</tr><tr>";
		}
$number ++;
	}
} elsif ( $in{syuzoku} == 3 ) {
	foreach $ppet (@zukankeisai3) {
		($a,$zukanname,$zukane) = split(/,/,$ppet);
print <<"HTM";
<td><b>$number</b><br><img src="$maindir/$imgfile/$zukane.gif" width="60" height="60" alt="$zukanname"></td>
HTM
		if ($number % 5 == 0 ) {
print "</tr><tr>";
		}
$number ++;
	}
}

print"</tr></table></center>";
&hpowari;
exit;