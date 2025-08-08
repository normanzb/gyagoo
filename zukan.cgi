#!/usr/bin/perl

#　↑サーバーの設定に合わせて変更してください。
#　種族名設定
$syuok[1] = "精霊";$syuok[2] = "魔人";$syuok[3] = "霊獣";

#########　設定はここまで　##########


require "./settei.cgi";
require "./cgi-lib.pl";
&ReadParse;

&cookieget;
&ipblock;
&gaibublock;
&cookieset;
&hpsaisyo;
&charadataload;
if ( $chapass ne $in{usrpass} ) { &CgiError('パスワードエラー','パスワードが違います。再度ログイン画面からやり直してください。');exit; }
print "<center><font size=7 color=#$mojiiro2><b>ペット図鑑</b></font><br><br>";

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
現在の総掲載数： <font size=+1><b>$soukeisai</b></font> 匹<br><hr>
HTM
print "<table border=0><tr>";
 if ( $in{syuzoku} != 1 ) {
print <<"HTM";
<td>
<form method="post" action="./zukan.cgi">
<input type=hidden value="1" name="syuzoku">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="   精霊 　">
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
<input type=submit value="   魔人 　">
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
<input type=submit value="   霊獣 　">
</form></td>
HTM
}
print "</tr></table><br>";

print <<"HTM";
<font size=6 color=#$mojiiro4><b>$syuok[$in{syuzoku}]</b></font>
<font size=+2>( $keisai[$in{syuzoku}] 匹 )</font><br><br><table border=1 bgcolor=#$bgclr><tr>
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