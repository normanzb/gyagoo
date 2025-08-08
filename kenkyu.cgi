#　合成不可ペットの名前を入力
@badname = ( 'バグターミネーター','名前入力','名前入力','名前入力','名前入力' );

#　種族名設定
$syuok[1] = "精霊";$syuok[2] = "魔人";$syuok[3] = "霊獣";

#########　設定はここまで　##########

&topsisetu;

if ( $in{riyou} == 1 ) {
	if ( $in{pet1} eq "" ) {
print <<"HTM";
ヘイヘイ！<br>
ちゃんとペットを選択してプリーズ。<br>
あなたと遊んでる暇ないよ。<br>
グッバイ！
HTM
	} else {
print <<"HTM";
オーイェー。<br>
<font size=+1><b>$in{pet1}</b></font> ね。<br><br>
ネクストはニ匹目を選択してプリーズ。<br></td><td width=30></td><td>
<form method="post" action="./$zonecgi">
<input type=hidden value="5" name="sisetu">
<input type=hidden value="11" name="riyou">
<input type=hidden value="$in{pet1}" name="pet1">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="　 ２匹目を選択 　" onClick="this.disabled=true; this.value='  お待ちください  '; this.form.submit();"><br>
<select name="pet2" size=6>
HTM
open(PET,"$maindir/$foldacha/pet_$in{usrid}$bousi2cha$bousikts");
		while ( $petka = <PET> ) {
			chop($petka);
			if ( $petka ne $in{pet1} ) {
print "<option value=\"$petka\">$petka";
			}
		}
close(PET);
print <<"HTM";
</select></form><br>
HTM
	}
} elsif ( $in{riyou} == 11 ) {
	if ( $in{pet2} eq "" || $in{pet1} eq "") {
print <<"HTM";
ヘイヘイ！<br>
ちゃんとペットを選択してプリーズ。<br>
あなたと遊んでる暇ないよ。<br>
グッバイ！
HTM
	} else {
$uuu = 0;
open(PET,"$maindir/pet$bousikts");
		while ( $petka = <PET> ) {
			if ( $uuu == 2 ) { last; }
		($petgousei,$petnam) = split(/,/,$petka);
			if ( $petnam eq $in{pet1} ) {
				$petok1 = $petgousei;$uuu ++;
			}
			if ( $petnam eq $in{pet2} ) {
				$petok2 = $petgousei;$uuu ++;
			}
		}
close(PET);
	if ( $uuu != 2 ) { &fuseisyori;exit;}
($syuzoku1,$gouseinum1) = split(/\//,$petok1);
($syuzoku2,$gouseinum2) = split(/\//,$petok2);
	if ( $syuzoku1 == $syuzoku2 ) {
		if ( $syuzoku1 == 3 ) {
		$syu = 1;
		} else {
		$syu = $syuzoku1 + 1;
		}
	} else {
		$syu = $syuzoku1 + $syuzoku2;
		if ( $syu > 3 ) { $syu = $syu - 3;}
	}
	$syu2 = int(( $gouseinum1 + $gouseinum2 ) / 2);
$sinpet = "$syu/$syu2";
$uuu = 0;
open(PET,"$maindir/pet$bousikts");
		while ( $petka = <PET> ) {
		($petgousei,$petnam,$pete,$petlvl,$petderu,$petatk,$petatk2) = split(/,/,$petka);
			if ( $petgousei eq $sinpet ) {
				$uuu ++;last;
			}
		}
close(PET);

	foreach $i (@badname) {
		if ( $petnam eq $i ) {
print <<"HTM";
ソ\ーリー！<br>
<font size=+1><b>$in{pet1}</b> と <b>$in{pet2}</b></font> は<br>
相性が悪くて合成できないよ。<br><br>
違うペットを選択してプリーズ。<br>
</td><td width=30></td><td>
HTM
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="5" name="sisetu">
<input type=hidden value="1" name="onemore">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="　 やり直す 　" onClick="this.disabled=true; this.value='  お待ちください  '; this.form.submit();"><br>
</form>
HTM
&townmodori;
&pettukitable;
&hpowari;
exit;
		}
	}

print <<"HTM";
グッド！<br>
<font size=+1><b>$in{pet2}</b></font> ね。<br><br>
この２匹を合成すると<br>このペットが生成されるよ。<br>
</td><td width=30></td><td>
HTM

$uuu = 0;
open(PET,"$maindir/pet$bousikts");
		while ( $petka = <PET> ) {
			if ( $uuu == 2 ) { last; }
		($petgousei,$petnam) = split(/,/,$petka);
			if ( $petnam eq $in{pet1} ) {
				$petok1 = $petgousei;$uuu ++;
			}
			if ( $petnam eq $in{pet2} ) {
				$petok2 = $petgousei;$uuu ++;
			}
		}
close(PET);
	if ( $uuu != 2 ) { &fuseisyori;exit;}
($syuzoku1,$gouseinum1) = split(/\//,$petok1);
($syuzoku2,$gouseinum2) = split(/\//,$petok2);
	if ( $syuzoku1 == $syuzoku2 ) {
		if ( $syuzoku1 == 3 ) {
		$syu = 1;
		} else {
		$syu = $syuzoku1 + 1;
		}
	} else {
		$syu = $syuzoku1 + $syuzoku2;
		if ( $syu > 3 ) { $syu = $syu - 3;}
	}
	$syu2 = int(( $gouseinum1 + $gouseinum2 ) / 2);
$sinpet = "$syu/$syu2";
$uuu = 0;
open(PET,"$maindir/pet$bousikts");
		while ( $petka = <PET> ) {
		($petgousei,$petnam,$pete,$petlvl,$petderu,$petatk,$petatk2) = split(/,/,$petka);
			if ( $petgousei eq $sinpet ) {
				$uuu ++;last;
			}
		}
close(PET);
	if ( $uuu == 0 ) { &fuseisyori;exit; }


print <<"HTM";
<table border=1><tr><td rowspan=3>
<img src="$maindir/$imgfile/$pete.gif"></td><td colspan=2><nobr>
名前(種族)：<font color=#$chamoji><b>$petnam</b></font> ( $syuok[$syu] )</nobr>
</td></tr><tr><td>
<nobr>Lvl：<font color=#$chamoji><b> $petlvl</b></font></nobr>
</td><td><nobr>戦闘参加値： <font color=#$chamoji><b>$petderu</b></font></nobr></td></tr><tr><td><nobr><font color=#$chamoji><b>
HTM

	if ( $petatk == 0 ) {
		print"物理攻撃";
	} elsif ( $petatk == 1 ) {
		print"火属性攻撃";
	} elsif ( $petatk == 2 ) {
		print"水属性攻撃";
	} elsif ( $petatk == 3 ) {
		print"魔属性攻撃";
	} elsif ( $petatk == 4 ) {
		print"無属性攻撃";
	} elsif ( $petatk == 5 ) {
		print"ランダム属性攻撃";
	} elsif ( $petatk == 6 ) {
		print"お金を奪う";
	} elsif ( $petatk == 7 ) {
		print"スタン効果";
	} elsif ( $petatk == 8 ) {
		print"HP回復";
	} else {
		print"ステータスアップ";
	}
print <<"HTM";
</b></font></nobr></td><td>
<nobr>効果値：<font color=#$chamoji><b> $petatk2</b></font></nobr></td></tr></table>
HTM

$uuu = 0;
open(PET,"$maindir/$foldacha/pet_$in{usrid}$bousi2cha$bousikts");
		while ( $petka = <PET> ) {
			chop($petka);
			if ( $petka eq $petnam ) {
$uuu = 1;last;
			}
		}
close(PET);
	if ( $petcode[0] eq $petnam || $petcode[1] eq $petnam || $petcode[2] eq $petnam ) {
$uuu = 1
	}
open(SHOP,"$maindir/$foldakojin/kojin_$in{usrid}$bousi2cha$bousikts");
$a = <SHOP>;
close(SHOP);
		($shopserifu,$shopserifu2,$shopsina) = split(/,/,$a);
@syouhin = split(/\t/,$shopsina);
	foreach $a ( @syouhin ) {
		($snedana,$snamea) = split(/\//,$a);
		if ( $snamea eq $monsname ) {$uuu = 1;last;}
	}

	if ( $uuu == 1 ) {


print <<"HTM";
<br>バーーット。<br>すでにあなたはこのペットいるね。<br>
だから合成しても意味ないね。
HTM

	} else {
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="5" name="sisetu">
<input type=hidden value="12" name="riyou">
<input type=hidden value="$in{pet1}" name="pet1">
<input type=hidden value="$in{pet2}" name="pet2">
<input type=hidden value="$petnam" name="petnam">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="　 合成する 　" onClick="this.disabled=true; this.value='  お待ちください  '; this.form.submit();"><br>
</form>
HTM
	}
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="5" name="sisetu">
<input type=hidden value="1" name="onemore">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="　 やり直す 　" onClick="this.disabled=true; this.value='  お待ちください  '; this.form.submit();"><br>
</form>
HTM
	}
} elsif ( $in{riyou} == 12 ) {
	if ( $in{pet1} eq "" || $in{pet2} eq "" || $in{petnam} eq "" ) { &fuseisyori;exit; }
$uuu = 0;
open(PET,"$maindir/$foldacha/pet_$in{usrid}$bousi2cha$bousikts");
		while ( $petka = <PET> ) {
			if ( $uuu == 2 ) { last; }
		chop($petka);
			if ( $petka eq $in{pet1} ) { $uuu ++; }
			if ( $petka eq $in{pet2} ) { $uuu ++; }
		}
close(PET);

	if ( $uuu != 2 ) { &fuseisyori;exit; }

open(PET2,">>$maindir/$foldacha/pet_$in{usrid}.tmp");
flock(PET2,2);
	open(PET,"$maindir/$foldacha/pet_$in{usrid}$bousi2cha$bousikts");
		while ( $petka = <PET> ) {
chop($petka);
			if ( $petka eq $in{pet1} || $petka eq $in{pet2} ) { 
			} else {
print PET2 "$petka\n";
			}
		}
	close(PET);
print PET2 "$in{petnam}\n";
flock(PET2,8);
close(PET2);

rename("$maindir/$foldacha/pet_$in{usrid}.tmp","$maindir/$foldacha/pet_$in{usrid}$bousi2cha$bousikts");

print <<"HTM";
ヤフーーー！<br><br>
<font size=+1 color=#$chamoji><b>$in{petnam}</b></font> を合成完了！<br><br>
$sisetu[4] に送っておくね。<br>
<form method="post" action="$cgiurl$zonecgi">
<input type=hidden value="5" name="sisetu">
<input type=hidden value="1" name="onemore">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="　 合成する 　"><br>
</form>

HTM


} else {
	if ( $in{onemore} == 1 ) {
print <<"HTM";
クールッ！<br><br>
じゃぁもう1回トライしてみるね。<br><br>
HTM
	} else {
print <<"HTM";
ハロー、<font color=#$chamoji><b>$chaname</b></font> ！<br><br>
今日もペット合成しにきたのかい？<br><br>
HTM
	}
$jjj = 0;$jja = 0;
open(PET,"$maindir/$foldacha/pet_$in{usrid}$bousi2cha$bousikts");
	while ( $petka = <PET> ) {
		if ( $jjj > 2 ) { last; }
		if ( $petka ne "" ) { $jja ++; }
$jjj ++;
	}
close(PET);

	if ( $jja < 2 ) {
print <<"HTM";
ノー！　合成するのには<b>２匹以上</b>のペットが<br>
  $sisetu[4] にいることが必要だ。<br>
もっとペットを増やしてきてちょ。<br>
　シーユーアゲイン！！<br><br>
HTM
	} else {
print <<"HTM";
オーケーベイベー。<br>
　それじゃぁ合成したいペットを<br>
まず一匹選択してプリーズ。<br></td><td width=30></td><td>
<form method="post" action="./$zonecgi">
<input type=hidden value="5" name="sisetu">
<input type=hidden value="1" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="　 １匹目を選択 　" onClick="this.disabled=true; this.value='  お待ちください  '; this.form.submit();"><br>
<select name="pet1" size=6>
HTM
open(PET,"$maindir/$foldacha/pet_$in{usrid}$bousi2cha$bousikts");
		while ( $petka = <PET> ) {
			chop($petka);
print "<option value=\"$petka\">$petka";
		}
close(PET);
print <<"HTM";
</select></form><br>
HTM

	}

}

&townmodori;
&pettukitable;
&hpowari;

exit;


1;