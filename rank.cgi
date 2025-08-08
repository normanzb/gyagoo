#　種族名設定
$syuok[1] = "精霊";$syuok[2] = "魔人";$syuok[3] = "霊獣";

#########　設定はここまで　##########

&topsisetu;

if ( $in{riyou} == 1 ) {
	if ( $in{pet1} eq "" ) {
print <<"HTM";
んむ？<br>
ちゃんと選択されてないようだ。<br>
私も忙しいのでね。<br>
失礼するよ。
HTM
	} else {
print <<"HTM";
ベースとなるモンスターは、<br>
<font size=+1><b>$petname[$in{pet1}]</b><font size=-1>($petcode[$in{pet1}])</font></font> で間違いはないな？<br><br>
では、どのモンスターを<br>イケニエとして捧げるのだ？・・・<br></td><td width=30></td><td>
<form method="post" action="./$zonecgi">
<input type=hidden value="16" name="sisetu">
<input type=hidden value="11" name="riyou">
<input type=hidden value="$in{pet1}" name="pet1">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="　 イケニエを選択 　" onClick="this.disabled=true; this.value='  お待ちください  '; this.form.submit();"><br><br>
HTM
$petcode[$in{pet1}] = "";
$waa = 0;$waw =1;
	while ( $waa < 3 ) {
		if ( $petcode[$waa] ne "" ) {
print "<input type=radio name=\"pet2\" value=\"$waa\" checked>$waw番目：<font size=4><b>$petname[$waa]</b></font> ($petcode[$waa])<br>";
		}

$waa ++;$waw ++;
	}
close(PET);
print <<"HTM";
</select></form><br>
HTM
	}
} elsif ( $in{riyou} == 11 ) {
	if ( $in{pet2} eq "" || $in{pet1} eq "") {
print <<"HTM";
んん？<br>
ちゃんと選択されてないようだ。<br>
私も忙しいのでね。<br>
失礼するよ。
HTM
	} else {

$newpetlv1 = $petlv[$in{pet1}] + $petlv[$in{pet2}];
$ryoukin = $newpetlv1 * 3;
print <<"HTM";
<font size=+1><b>$petname[$in{pet2}]</b><font size=-1>($petcode[$in{pet2}])</font></font> を、<br>イケニエとして捧げるのだな。<br>
イケニエとして捧げられたモンスターは、<br>もう戻りはせん。<br><br>
手数料として、<b><font size=+2><font color=blue>$ryoukin</font></font></b> <b>G</b>いただこうか。<br><br>
<b>$petname[$in{pet1}]</b><font size=-1>($petcode[$in{pet1}])</font> の能\力\は<br>次のように変化するが、<br>本当にいいのだな？
</td><td width=30></td><td>
HTM
print <<"HTM";
<center><font color=red><font color=red>合体前</font></font></center>
<table border=1><tr><td rowspan=3>
<img src=\"$maindir/$imgfile/$petpic[$in{pet1}].gif\"></td><td colspan=2><nobr>
名前：<font color=#$chamoji><b>$petname[$in{pet1}]<font size=-1></b>($petcode[$in{pet1}])</font></b></font></nobr>
</td></tr><tr><td>
<nobr>Lvl：<font color=#$chamoji><b> $petlv[$in{pet1}]</b></font></nobr>
</td><td><nobr>参加値(PP)： <font color=#$chamoji><b>$petritu[$in{pet1}]</b></font></nobr></td></tr><tr><td><nobr><font color=#$chamoji><b>
HTM
	if ( $petkouka[$in{pet1}] == 16 ) {
		print"物理攻撃";
	} elsif ( $petkouka[$in{pet1}] == 1 ) {
		print"火属性攻撃";
	} elsif ( $petkouka[$in{pet1}] == 2 ) {
		print"水属性攻撃";
	} elsif ( $petkouka[$in{pet1}] == 3 ) {
		print"魔属性攻撃";
	} elsif ( $petkouka[$in{pet1}] == 4 ) {
		print"無属性攻撃";
	} elsif ( $petkouka[$in{pet1}] == 5 ) {
		print"？属性攻撃";
	} elsif ( $petkouka[$in{pet1}] == 6 ) {
		print"お金を奪う";
	} elsif ( $petkouka[$in{pet1}] == 8 ) {
		print"HP回復";
	} else {
		print"ステータスアップ";
	}
print <<"HTM";
</b></font></nobr></td><td>
<nobr>効果値(EF)：<font color=#$chamoji><b> $petkouka2[$in{pet1}]</b></font></nobr></td></tr></table>
<br>
HTM



$karicode = $petcode[$in{pet1}];$karilvl = $petlv[$in{pet1}];
$kariname = $petname[$in{pet1}];$karikouka = $petkouka[$in{pet1}];
$kariritu = $petritu[$in{pet1}];$karikouka2 = $petkouka2[$in{pet1}];
$karipic = $petpic[$in{pet1}];$karieff = $peteff[$in{pet1}];
$kariexp = $petexp[$in{pet1}];$karinowexp = $petnowexp[$in{pet1}];
$kariatk = $petatk[$in{pet1}];

$newpetlv1 = $petlv[$in{pet1}] + $petlv[$in{pet2}];
$newpetlv = int($newpetlv1 / 2);
$newpetkouka1 = $petkouka2[$in{pet1}] + $petkouka2[$in{pet2}] + $petlv[$in{pet2}];
$newpetkouka = int($newpetkouka1 / 2);
$newpetritu1 = $petritu[$in{pet1}] + $petritu[$in{pet2}] + $petlv[$in{pet2}];
$newpetritu = int($newpetritu1 / 2);
$newpeteff1 = $peteff[$in{pet1}] + $peteff[$in{pet2}];

print <<"HTM";
<center><font color=red>合体後</font></center>
<table border=1><tr><td rowspan=3>
<img src=\"$maindir/$imgfile/$petpic[$in{pet1}].gif\"></td><td colspan=2><nobr>
名前：<font color=#$chamoji><b>$petname[$in{pet1}]<font size=-1></b>($petcode[$in{pet1}])</font></b></font></nobr>
</td></tr><tr><td>
<nobr>Lvl：<font color=#$chamoji><b> $newpetlv</b></font></nobr>
</td><td><nobr>参加値(PP)： <font color=#$chamoji><b>$newpetritu</b></font></nobr></td></tr><tr><td><nobr><font color=#$chamoji><b>
HTM
	if ( $petkouka[$in{pet1}] == 16 ) {
		print"物理攻撃";
	} elsif ( $petkouka[$in{pet1}] == 1 ) {
		print"火属性攻撃";
	} elsif ( $petkouka[$in{pet1}] == 2 ) {
		print"水属性攻撃";
	} elsif ( $petkouka[$in{pet1}] == 3 ) {
		print"魔属性攻撃";
	} elsif ( $petkouka[$in{pet1}] == 4 ) {
		print"無属性攻撃";
	} elsif ( $petkouka[$in{pet1}] == 5 ) {
		print"？属性攻撃";
	} elsif ( $petkouka[$in{pet1}] == 6 ) {
		print"お金を奪う";
	} elsif ( $petkouka[$in{pet1}] == 8 ) {
		print"HP回復";
	} else {
		print"ステータスアップ";
	}
print <<"HTM";
</b></font></nobr></td><td>
<nobr>効果値(EF)：<font color=#$chamoji><b> $newpetkouka</b></font></nobr></td></tr></table>
HTM



	if ( $uuu == 1 ) {
print <<"HTM";
<br><font size=+3><b>不正な処理が行われました！</b></font><br>
<font color=red>データ破損の恐れがあります。</font><br>
HTM

	} else {
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="16" name="sisetu">
<input type=hidden value="12" name="riyou">
<input type=hidden value="$in{pet1}" name="pet1">
<input type=hidden value="$in{pet2}" name="pet2">
<input type=hidden value="$petnam" name="petnam">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="　これでいい　" onClick="this.disabled=true; this.value='お待ちください'; this.form.submit();"><br>
</form>
HTM
	}
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="16" name="sisetu">
<input type=hidden value="1" name="onemore">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="　 やり直す 　" onClick="this.disabled=true; this.value='お待ちください'; this.form.submit();"><br>
</form>
HTM
	}
} elsif ( $in{riyou} == 12 ) {
	if($chagold < $ryoukin) {
print <<"HTM";
金銭が足りないようだが。・・・<br>
残念だが、金銭を払わぬ者には合体させてやる事はできん。<br>
お金を貯めてから、もう一度来なさい。<br>
HTM
	} else {

$newpetlv1 = $petlv[$in{pet1}] + $petlv[$in{pet2}];
$newpetlv = int($newpetlv1 / 2);
$newpetkouka1 = $petkouka2[$in{pet1}] + $petkouka2[$in{pet2}]  + $petlv[$in{pet2}];
$newpetkouka = int($newpetkouka1 / 2);
$newpetritu1 = $petritu[$in{pet1}] + $petritu[$in{pet2}] + $petlv[$in{pet2}];
$newpetritu = int($newpetritu1 / 2);
$newpeteff1 = $peteff[$in{pet1}] + $peteff[$in{pet2}];

$petlv[$in{pet1}] = $newpetlv;
$petritu[$in{pet1}] = $newpetritu;
$petkouka2[$in{pet1}] = $newpetkouka;
$petnowexp[$in{pet1}] = 0;
$petexp[$in{pet1}] = int($petexp[$in{pet1}] / 5);
if($petexp[$in{pet1}] < 10) {$petexp[$in{pet1}] = 10;}

$petcode[$in{pet2}] = $petpic[$in{pet2}] = $petritu[$in{pet2}] = $petname[$in{pet2}] = $petkouka[$in{pet2}] = $petkouka2[$in{pet2}] = $petlv[$in{pet2}] = $petkouka[$in{pet2}] = "";
$petexp[$in{pet2}] = 15;
$petnowexp[$in{pet2}] = 0;
$ryoukin = $newpetlv1 * 3;
$chagold -= $ryoukin;

print <<"HTM";
<font size=+3><b>合体完了！</b></font><br><br>
うむ。無事に合体が終了したようだ。<br><br>
合体したいモンスターがいたら、<br>いつでも来なさい。<br>
HTM
&charadatawrt;
}
} else {
	if ( $in{onemore} == 1 ) {
print <<"HTM";
うむ、もう一度選択しなおすのだな。<br><br>
HTM
	} else {
print <<"HTM";
彷徨える旅人よ。よくぞ参られた。<br>
この館では、お主の連れているモンスターを<br>
合体させる事が出来る。<br><br>
HTM
}

$www = 0;$wwa =0;
while ( $wwa < 3 ) {
	if ( $petcode[$wwa] ne "" ) { $www ++; }
$wwa ++;
}
	if ( $www <= 1 ) {
print <<"HTM";
しかし、その為にはモンスターを<b>２匹以上</b><br>
連れている必要がある。<br>
どうやらお主は、モンスターを２匹以上<br>
連れていないようだな。<br><br>
モンスターを連れて、また来なさい。
HTM

	} else {
print <<"HTM";
まずは、ベースとなるモンスターを選択しなさい。<br></td><td width=30></td><td>
<form method="post" action="./$zonecgi">
<input type=hidden value="16" name="sisetu">
<input type=hidden value="1" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="　 ベースを選択 　" onClick="this.disabled=true; this.value='  お待ちください  '; this.form.submit();"><br><br>
HTM
$waa = 0;$waw =1;
	while ( $waa < 3 ) {
		if ( $petcode[$waa] ne "" ) {
print "<input type=radio name=\"pet1\" value=\"$waa\" checked>$waw番目：<font size=4><b>$petname[$waa]</b></font> ($petcode[$waa])<br>";
		}
$waa ++;$waw ++;



	}
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