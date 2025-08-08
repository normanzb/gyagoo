#　種族名設定
$syuok[1] = "精霊";$syuok[2] = "魔人";$syuok[3] = "霊獣";

#########　設定はここまで　##########

&topsisetu;
&jobdataload;

&chkchk;

#　ペット連れ出し処理
if ( $in{riyou} == 1 ) {
print <<"HTM";
はいはい。<br>どのペットを連れ出すんだい？<br><br>

<form method="post" action="./$zonecgi">
<input type=hidden value="4" name="sisetu">
<input type=hidden value="11" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<select name="pet" size=8>
HTM
open(PET,"$maindir/$foldacha/pet_$in{usrid}$bousi2cha$bousikts");
	while ( $petka = <PET> ) {
chop($petka);
print "<option value=\"$petka\">$petka";
	}
close(PET);
print <<"HTM";
</select><br><br>
名前をつけてあげておくれ。<br>
<input type=text size=17 name="petnamae" value=""><br>
</td><td width=30></td><td>配置はどこにする？<br><ul>
HTM
$waa = 0;
	while ( $waa < 3 ) {
		if ( $petcode[$waa] eq "" ) {
$wss = $waa + 1;
print "<input type=radio name=\"iti\" value=\"$waa\" checked>$wss番目<br>";
		}
	$waa ++;
	}

print <<"HTM";
</ul>
<input type=submit value="　   連れ出す  　" ><br>
</form><br>
HTM


} elsif ( $in{riyou} == 11 ) {
&jobdataload;
	for ( $i=0;$i<3;$i++ ) {
		if($petcode[$i] ne "") { $petpp ++; }
	}
	if ( $petpp >= $jobpet ) { &fuseisyori;exit; }

	if ( $in{petnamae} eq "" ) {
print <<"HTM";
あんた、ペットに名前を<br>
　　付けてあげないと可愛そうだよ。<br><br>
他にも用事はあるかい？<br>
HTM
&koyaform;
	} elsif ( $in{pet} eq "" ) {
print <<"HTM";
あんた、ペットを<br>
　　選択してくれないと困るよ。<br><br>
他にも用事はあるかい？<br>
HTM
&koyaform;
	} elsif ( length($in{petnamae}) > 16 ) {
print <<"HTM";
あんた、ペットの名前が長すぎだよ。<br>
　全角で８文字までにしておくれ。<br><br>
他にも用事はあるかい？<br>
HTM
&koyaform;
	} elsif ( $petcode[$in{iti}] ne "" || $in{iti} eq "") {
&fuseisyori;exit;
	} elsif ( $petcode[0] eq $in{pet} || $petcode[1] eq $in{pet} || $petcode[2] eq $in{pet}) {
&fuseisyori;exit;
	} else {

open(PET,"$maindir/pet$bousikts");
		while ( $petmatch = <PET> ) {
		($petgousei,$petnam,$pete,$petlvl,$petderu,$petatk,$petatk2) = split(/,/,$petmatch);
		if ( $in{pet} eq $petnam ) { $dad = 1;last; }
		}
close(PET);
		if ( $dad != 1 ) { &fuseisyori;exit; }
		if ( $petlvl > $chalvl ) {
print <<"HTM";
う～ん、<font size=+1><b> $petnam </b></font>かい。<br>
あんたにゃこのペットは扱えないねぇ。<br>
もうちょっと自分を鍛えてからだね。<br><br>
他にも用事はあるかい？
HTM
&koyaform;
		} else {
$in{petnamae} =~ s/</&lt;/g;
$in{petnamae} =~ s/>/&gt;/g;
$in{petnamae} =~ s/,/./g;
$in{petnamae} =~ s/\//_/g;
$petcode[$in{iti}] = $petnam;$petpic[$in{iti}] = $pete;
$petritu[$in{iti}] = $petderu;$petname[$in{iti}] = $in{petnamae};
$petkouka[$in{iti}] = $petatk;$petkouka2[$in{iti}] = $petatk2;$petlv[$in{iti}] = $petlvl;
&charadatawrt;
open(PET,"$maindir/$foldacha/pet_$in{usrid}$bousi2cha$bousikts");
	while ( $petkai = <PET> ) {
		push(@petnakama,$petkai);
	}
close(PET);
open(PET2,">>$maindir/$foldacha/pet_$in{usrid}.tmp");
	foreach $petbu (@petnakama) {
		chop($petbu);
		if ( $petbu ne $petnam ) {
print PET2 "$petbu\n";
		}
	}
close(PET2);
rename("$maindir/$foldacha/pet_$in{usrid}.tmp","$maindir/$foldacha/pet_$in{usrid}$bousi2cha$bousikts");

$basyo = $in{iti} + 1;
print <<"HTM";
はいはい、<font size=+1><b> $petnam </b></font>だね。<br>
<font size=+1 color=#$chamoji><b>$petname[$in{iti}] </b></font>かい。<br>
いい名前をつけたねぇ～。<br>
<font size=+1 color=#$mojiiro4><b>$basyo </font>番目</b>に配置しておいたよ。<br>
かわいがってやっておくれよ。<br><br>
他にも用事はあるかい？
HTM
$www ++;
&koyaform;
		}


	}

#　ペット預け処理
} elsif ( $in{riyou} == 2 ) {
	if ( $www == 0 ) { &fuseisyori;exit; }
print <<"HTM";
あいよ。<br>
で、どのペットを預けるんだい？<br><br>
<form method="post" action="./$zonecgi">
<input type=hidden value="4" name="sisetu">
<input type=hidden value="21" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="　     預ける    　"><br><br>
HTM
$waa = 0;$waw =1;
	while ( $waa < 3 ) {
		if ( $petcode[$waa] ne "" ) {
print "<input type=radio name=\"pet\" value=\"$waa\" checked>$waw番目：<font size=4><b>$petname[$waa]</b></font> ($petcode[$waa])<br>";
		}
$waa ++;$waw ++;
	}
print <<"HTM";
</form></td><td width=30></td><td>
HTM

} elsif ( $in{riyou} == 21 ) {
	if ( $petcode[$in{pet}] eq "" ) { &fuseisyori;exit; }
open(PET,"$maindir/$foldacha/pet_$in{usrid}$bousi2cha$bousikts");
   @pets = <PET>;
close(PET);
  $pet = @pets;
  if ( $pet >= 30 ) {
print <<"HTM";
おやおや、あんたの小屋はもうペットでいっぱいだよ。<br>
これ以上はひきとれないよ。<br><br>
他にも用事はあるかい？
HTM

  }else{
push(@pets,"$petcode[$in{pet}]\n");
open(PET,">$maindir/$foldacha/pet_$in{usrid}$bousi2cha$bousikts");
flock(PET,2);
    print PET @pets;
flock(PET,8);
close(PET);


print <<"HTM";
はいはい、<font size=4><b>$petname[$in{pet}] </font>($petcode[$in{pet}])</b>だね。<br>
大事に預かっておくよ。<br><br>
他にも用事はあるかい？
HTM
$www --;

$petcode[$in{pet}] = $petpic[$in{pet}] = $petritu[$in{pet}] = $petname[$in{pet}] = $petkouka[$in{pet}] = $petkouka2[$in{pet}] = $petlv[$in{pet}] = $petkouka[$in{pet}] = "";
$petexp[$in{pet}] = 10;
$petnowexp[$in{pet}] = 0;
&charadatawrt;
  }
&koyaform;

#　ペット詳細情報処理
} elsif ( $in{riyou} == 3 ) {
print <<"HTM";
ふむふむ。ペットのことなら私にお任せ。<br>
どのペットの情報を知りたいんだい？<br>
HTM
&syousaipet;


} elsif ( $in{riyou} == 31 ) {
$uuu = 0;
open(PET,"$maindir/pet$bousikts");
		while ( $petka = <PET> ) {
		($petgousei,$petnam,$pete,$petlvl,$petderu,$petatk,$petatk2) = split(/,/,$petka);
			if ( $petnam eq $in{jouhou} ) {
				$uuu ++;last;
			}
		}
close(PET);
	if ( $uuu == 0 ) { &fuseisyori;exit; }
($syu,$gouseinum1) = split(/\//,$petgousei);

print <<"HTM";
<b>$petnam</b>の詳細情報だよ。<br><br>
<table border=1><tr><td rowspan=3>
<img src="$maindir/$imgfile/$pete.gif"></td><td colspan=2><nobr>
名前(種族)：<font color=#$chamoji><b>$petnam</b></font> ( $syuok[$syu] )</nobr>
</td></tr><tr><td>
<nobr>Lvl：<font color=#$chamoji><b> $petlvl</b></font></nobr>
</td><td><nobr>戦闘参加値： <font color=#$chamoji><b>$petderu</b></font></nobr></td></tr><tr>
<td><nobr>効果値：<font color=#$chamoji><b> $petatk2</b></font></nobr></td>
<td><nobr><font color=#$chamoji><b>
HTM
	if ( $petatk == 16 ) {
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
	} elsif ( $petatk == 15 ) {
		print"特殊行動";
	} else {
		print"ステータスアップ";
	}
print <<"HTM";
</b></font></nobr></td></tr></table><br>まだ何か調べるかい？
HTM
&syousaipet;
print "</td><td width=30></td><td>";
&koyaform;

} elsif ( $in{riyou} == 4 ) {
print <<"HTM";
どのペットを掲載するんだい？<br>
HTM

&zukanpet;

} elsif ( $in{riyou} == 41 ) {
	if ( $in{jouhou} eq "" ) { &fuseisyori;exit;}
$uuu = 0;
open(PET,"$maindir/pet$bousikts");
		while ( $petka = <PET> ) {
		($petgousei,$petnam,$pete,$petlvl,$petderu,$petatk,$petatk2) = split(/,/,$petka);
			if ( $petnam eq $in{jouhou} ) {
				$uuu ++;print"";last;
			}
		}
close(PET);
	if ( $uuu == 0 ) { &fuseisyori;exit; }
($syu,$gouseinum) = split(/\//,$petgousei);


$uuu = 0;
open(PET,"$maindir/$foldazukan/pet$syu$in{usrid}$bousicha$bousikts");
@zukankeisai = <PET>;
close(PET);
		foreach $petka( @zukankeisai ) {
		($petgousei2,$petnam2,$pete2) = split(/,/,$petka);
			if ( $petnam2 eq $in{jouhou} ) {
				$uuu ++;
			}
			$karipet2 ="$petnam2,$pete2";
			$keisaizumi{$karipet2} = $petgousei2;
		}

		if ( $uuu == 1 ) {
print <<"HTM";
<b>$petnam</b>かい。<br>
そのペットはすでに掲載済みみたいだね。<br>
他に掲載するペットはあるかい？<br>
HTM
		} else {
$karipet = "$petnam,$pete";
$keisaizumi{$karipet} = $gouseinum;
@zukankeisai2 = sort by_character keys(%keisaizumi);

open(PET,">$maindir/$foldazukan/pet$syu$in{usrid}$bousicha$bousikts");
flock(PET,2);
	foreach $zukan3 (@zukankeisai2) {
		print PET "$keisaizumi{$zukan3},$zukan3,\n";
	}
flock(PET,8);
close(PET);
$zukan4 = @zukankeisai2;

print <<"HTM";
<b>$petnam</b>だね。<br>
掲載しておいたよ。<br>
これで<b>$syuok[$syu]</b>は <b>$zukan4</b> 匹になったね。<br><br>
他に掲載するペットはあるかい？<br>
HTM
		}

&zukanpet;
print "</td><td width=30></td><td>";
&koyaform;


#VER106 Start ペット逃がすコマンド
} elsif ( $in{riyou} == 6 ) {
print <<"HTM";
どのペットを逃がすんだい？<br>
一度逃がしたら元には戻らないから<br>
慎重に選択しなよ。<br><br>
HTM
  
&sakujopet;
  
} elsif ( $in{riyou} == 61 ) {
	if ( $in{jouhou} eq "" ) { &fuseisyori;exit;}
$uuu = 0;


open(PET,"$maindir/$foldacha/pet_$in{usrid}$bousi2cha$bousikts");

		($petgousei,$petnam,$pete,$petlvl,$petderu,$petatk,$petatk2) = split(/,/,$petka);


  @sakujo = <PET>;
close(PET);
  
  foreach $a (@sakujo){
		chop($a);
	if ( $a eq $in{jouhou} ) {
		$uuu ++;$petnam = $a;
    } else {
      push(@sakujo2,"$a\n");
    }
  }

  if ( $uuu == 0 ) { &fuseisyori;exit; }

open(PET,">$maindir/$foldacha/pet_$in{usrid}$bousi2cha$bousikts");
  flock(PET,2);
    print PET @sakujo2;
  flock(PET,8);
close(PET);

print <<"HTM";

<b>$petnam</b>だね。<br>
逃がしておいたよ。<br>
他に逃がしたいペットはいるかい？<br>
HTM

&sakujopet;
print "</td><td width=30></td><td>";
&koyaform;


#VER106 End

} else {
print <<"HTM";
おや、<font color=#$chamoji><b>$chaname</b></font> かい。<br><br>
あんたのペットはちゃんと預かっているよ。<br>
今日はどんな用事だい？<br><br>
HTM
&koyaform;

}

sub koyaform {

	if ( $www < $jobpet ) {
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="4" name="sisetu">
<input type=hidden value="1" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="　 ペットを連れ出す 　">
</form>
HTM
	}
	if ( $www != 0 ) {
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="4" name="sisetu">
<input type=hidden value="2" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="　  ペットを預ける  　">
</form>
HTM
	}
	if ( $in{riyou} != 3 ) {
		if ( $in{riyou} != 31 ) {
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="4" name="sisetu">
<input type=hidden value="3" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="   ペット詳細情報 　">
</form>
HTM
		}
	}

	if ( $in{riyou} != 4 ) {
		if ( $in{riyou} != 41 ) {
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="4" name="sisetu">
<input type=hidden value="4" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="  ペット図鑑に掲載　">
</form>
HTM
		}
	}

	if ( $in{riyou} != 5 ) {
print <<"HTM";
<form method="post" action="./zukan.cgi" target="petzukan">
<input type=hidden value="1" name="syuzoku">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="   ペット図鑑閲覧 　">
</form>
HTM
	}

#VER106 Start ペット逃がすコマンド
  if ( $in{riyou} != 61 ) {
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="4" name="sisetu">
<input type=hidden value="6" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="　 ペットを逃がす 　">
</form>
HTM
  }
#VER106END

print "</td><td width=30></td><td>";
}
&townmodori;
	if ( $in{riyou} != 3 ) {
		if ( $in{riyou} != 31 ) {
&pettukitable;
		}
	}
&itemtable;
&hpowari;

exit;
sub chkchk {
	$www = 0;$wwa =0;
	while ( $wwa < 3 ) {
		if ( $petcode[$wwa] ne "" ) { $www ++; }
	$wwa ++;
	}
}

sub syousaipet{
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="4" name="sisetu">
<input type=hidden value="31" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<select name="jouhou">
HTM
open(PET,"$maindir/$foldacha/pet_$in{usrid}$bousi2cha$bousikts");
	while ( $petkai = <PET> ) {
		chop($petkai);
print "<option value=\"$petkai\">$petkai";
	}
close(PET);
print <<"HTM";
</select>
<input type=submit value="　 詳細情報 　"><br>
</form>
HTM

}

sub zukanpet{
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="4" name="sisetu">
<input type=hidden value="41" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<select name="jouhou">
HTM
open(PET,"$maindir/$foldacha/pet_$in{usrid}$bousi2cha$bousikts");
	while ( $petkai = <PET> ) {
		chop($petkai);
print "<option value=\"$petkai\">$petkai";
	}
close(PET);
print <<"HTM";
</select>
<input type=submit value="　 図鑑に掲載 　"><br>
</form>
HTM

}

sub by_character {
	$keisaizumi{$a} <=> $keisaizumi{$b};
}

#VER106 Start ペット逃がすコマンド
sub sakujopet {
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="4" name="sisetu">
<input type=hidden value="61" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<select name="jouhou">
HTM
open(PET,"$maindir/$foldacha/pet_$in{usrid}$bousi2cha$bousikts");
  @sakujo = <PET>;
close(PET);
  foreach $a (@sakujo){
		chop($a);
    print "<option value=\"$a\">$a";
  }
print <<"HTM";
</select>
<input type=submit value="ペットを逃がす"><br>
</form>
HTM
}
#VER106 End

1;