open(BANK,"$maindir/$foldacha/bankg_$in{usrid}$bousi2cha$bousikts");
	$bankgold = <BANK>;
close(BANK);
if ( $bankgold eq "" ) { $bankgold = 0 ; }

open(HUKU,"$maindir/$foldacha/hukubiki_$in{usrid}$bousi2cha$bousikts");
	$bankhukubiki = <HUKU>;
close(HUKU);
if ( $bankhukubiki eq "" ) { $bankhukubiki = 0 ; }
&topsisetu;

if ( $in{riyou} eq "1"){

#　お金を預ける

#VER106 Start 正規表現
#$in{okane} = int($in{okane});
	if ( $in{okane} =~ /^[0-9]+$/ ) {
#VER106 End

if ( $in{okane} < 0 ) {
	&fuseisyori;
} else {
	if ( $chagold < 1 ) {
print <<"HTM";
「ショジキン　ガ　アリマセン」<br>
HTM

	} else {
		if( $chagold < $in{okane} ) {
		$in{okane} = $chagold;
		} 
$bankgold += $in{okane};
$chagold -= $in{okane};
&charadatawrt;
&bankwrt;
print <<"HTM";
「タシカ　ニ　オアズカリ　シマシタ」<br>
HTM
&bankform;
	}
}

#VER106 Start 正規表現
	} else {
		&fuseisyori;
	}
#VER106 End

} elsif ( $in{riyou} eq "2"){

#　お金を引き出す

#VER106 Start 正規表現
#$in{okane} = int($in{okane});
	if ( $in{okane} =~ /^[0-9]+$/ ) {
#VER106 End
if ( $in{okane} < 0 ) {
	&fuseisyori;
} else {
$in{okane} = int($in{okane});
	if ( $bankgold < 1 ) {
print <<"HTM";
「ヨキン　ハ　アリマセン」<br>
HTM



	} else {
		if( $bankgold < $in{okane} ) {
		$in{okane} = $bankgold;
		} 

$bankgold -= $in{okane};
$chagold += $in{okane};
	if ( $chagold > 1000000000 ) {
$chagold = 999999999;
}
&charadatawrt;
&bankwrt;
print <<"HTM";
「オヒキダシ　イタシマシタ」<br>
HTM
&bankform;
	}
}

#VER106 Start 正規表現
	} else {
		&fuseisyori;
	}
#VER106 End

















} elsif ( $in{riyou} eq "11"){
#　福引券を預ける

#VER106 Start 正規表現
#$in{hukubiki} = int($in{hukubiki});
	if ( $in{hukubiki} =~ /^[0-9]+$/ ) {
#VER106 End

if ( $in{hukubiki} < 0 ) {
	&fuseisyori;
} else {
	if ( $hukubiki < 1 ) {
print <<"HTM";
「１マイ　モ　モッテイマセン」<br>
HTM

	} else {
		if( $hukubiki < $in{hukubiki} ) {
		$in{hukubiki} = $hukubiki;
		} 
$bankhukubiki += $in{hukubiki};
$hukubiki -= $in{hukubiki};
&charadatawrt;
&bankwrt2;
print <<"HTM";
「タシカ　ニ　オアズカリ　シマシタ」<br>
HTM
&bankform;
	}
}

#VER106 Start 正規表現
	} else {
		&fuseisyori;
	}
#VER106 End

} elsif ( $in{riyou} eq "12"){

#　福引券を引き出す

#VER106 Start 正規表現
#$in{hukubiki} = int($in{hukubiki});
	if ( $in{hukubiki} =~ /^[0-9]+$/ ) {
#VER106 End
if ( $in{hukubiki} < 0 ) {
	&fuseisyori;
} else {
$in{hukubiki} = int($in{hukubiki});
	if ( $bankhukubiki < 1 ) {
print <<"HTM";
「１マイ　モ　アズカッテ　イマセン」<br>
HTM



	} else {
		if( $bankhukubiki < $in{hukubiki} ) {
		$in{hukubiki} = $bankhukubiki;
		} 

$bankhukubiki -= $in{hukubiki};
$hukubiki += $in{hukubiki};
	if ( $hukubiki > 1000000000 ) {
$chastats[14] = 999999999;
}
&charadatawrt;
&bankwrt2;
print <<"HTM";
「オヒキダシ　イタシマシタ」<br>
HTM
&bankform;
	}
}

#VER106 Start 正規表現
	} else {
		&fuseisyori;
	}
#VER106 End





} elsif ( $in{riyou} eq "3"){

#　アイテムを預ける

&itemsentaku;
} elsif ( $in{riyou} eq "31"){

open(BANKI,"$maindir/$foldacha/bankit_$in{usrid}$bousi2cha$bousikts");
  @item = <BANKI>;
close(BANKI);
  $itemsousuu = @item;
	if ( $itemsousuu >= 100 ) {
print <<"HTM";
「アイテム　ハ　１００コ　マデシカ<br>
　　オアズカリ　デキマセン。」<br>
HTM
        }elsif ( $in{itemde} eq "" ) {
print <<"HTM";
「アイテム　ガ　センタク<br>
　　サレテ　イマセン　デシタ」<br>
HTM
	} elsif ( $chaitem[$in{itemde}] eq "" ) {
&fuseisyori;
	} else {
		if ( $chaeff[$in{itemde}] eq "" ) {
&fuseisyori;
		} elsif ( $chaeff[$in{itemde}] > 1 ) {
$chaeff[$in{itemde}] --;
if (!open(BANKI,">>$maindir/$foldacha/bankit_$in{usrid}$bousi2cha$bousikts")) { &CgiError('エラー発生','ファイルオープンに失敗しました。'); }
flock(BANKI,2);
	print BANKI "$chaitem[$in{itemde}]/$chasetumei[$in{itemde}]\n";
flock(BANKI,8);
close(BANKI);
&charadatawrt;
print <<"HTM";
「１コ　ダケ　オアズカリ　シマシタ」<br>
HTM
&bankform;
		} else {
if (!open(BANKI,">>$maindir/$foldacha/bankit_$in{usrid}$bousi2cha$bousikts")) { &CgiError('エラー発生','ファイルオープンに失敗しました。'); }
flock(BANKI,2);
	print BANKI "$chaitem[$in{itemde}]/$chasetumei[$in{itemde}]\n";
flock(BANKI,8);
close(BANKI);
$chaitem[$in{itemde}] = $chaeff[$in{itemde}] = $chasetumei[$in{itemde}] = "";
&charadatawrt;
print <<"HTM";
「オアズカリ　シマシタ」<br>
HTM
&bankform;
		}
}

} elsif ( $in{riyou} eq "4"){

#　アイテムを引き出す

if (!open(BANKI,"$maindir/$foldacha/bankit_$in{usrid}$bousi2cha$bousikts")) { &CgiError('エラー発生','ファイルオープンに失敗しました。'); }
	$bchk = <BANKI>;
close(BANKI);
	if ( $bchk eq "" ) {
print <<"HTM";
「ゲンザイ　オアズカリ　シテイル<br>
　　　　アイテム　ハ　ゴザイマセン」<br>
HTM
&bankform;
	} else {
print <<"HTM";
「アイテム　ヲ　センタク　シテクダサイ」<br>
<form method="post" action="./$zonecgi">
<input type=hidden value="1" name="sisetu">
<input type=hidden value="41" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="　   引き出す  　" ><br>
<select name="itemds" size=10>
HTM
$abb = 0;
if (!open(BANKI,"$maindir/$foldacha/bankit_$in{usrid}$bousi2cha$bousikts")) { &CgiError('エラー発生','ファイルオープンに失敗しました。'); }
		while ( $bankno = <BANKI> ) {
		chop($bankno);
	($bankname,$bankbun) = split(/\//,$bankno);
print "<option value=\"$bankname/$bankbun/$abb\">$bankname（$bankbun）";
$abb ++;
		}
close(BANKI);
print <<"HTM";
</select></form><br>
HTM
	}
} elsif ( $in{riyou} eq "41"){
&itemkuuran;
	if ( $ccb eq "0" ) {
print <<"HTM";
「アイテム　ガ　イッパイ　デス」<br>
HTM

	} else {
	($bankname,$bankbun,$aba) = split(/\//,$in{itemds});
open(BANKI,"$maindir/$foldacha/bankit_$in{usrid}$bousi2cha$bousikts");
		@banban = <BANKI>;
close(BANKI);

$abd = 0;
open(BANN,">$maindir/$foldacha/$in{usrid}.tmp");
flock(BANN,2);
		foreach $a (@banban) {
			($kk,$ll) = split(/\//,$a);
#VER106 Start アイテム消失バグ修正
#			if ( $abd eq $aba && $bankname eq $kk ) {
			if ( $abd eq $aba && $bankname eq $kk && $puchk != 1) {
#VER106 End
				$puchk = 1;
			} else {
				print BANN "$a";
			} 
			$abd ++;
		}
flock(BANN,8);
close(BANN);

if ( $puchk ne "1" ) { &fuseisyori;exit;}

rename("$maindir/$foldacha/$in{usrid}.tmp","$maindir/$foldacha/bankit_$in{usrid}$bousi2cha$bousikts");

			$ccc = 1;$ccb = 0;
			while ( $ccc < 9 ) {
				if ( $chaitem[$ccc] eq $bankname ) {
					$cce = $ccc;$ccd = 1;last;
				} 
				$ccc ++;
			}
			$ccc = 1;
			while ( $ccc < 9 ) {
				if ( $chaitem[$ccc] eq "" ) {
				$ccb = $ccc;last;
				}
				$ccc ++;
			}
		if ( $ccd == 1 ) {
$chaeff[$cce] ++;
		} else {
$chaitem[$ccb] = $bankname;$chaeff[$ccb] = 1;$chasetumei[$ccb] = $bankbun;
		}
&charadatawrt;
print <<"HTM";
「オヒキダシ　イタシマシタ」<br>
HTM


	}
&bankform;
} elsif ( $in{riyou} eq "5"){

#　回復アイテムを使用する

			$ccc = 1;$cbc = 0;
			while ( $ccc < 9 ) {
				if ( $chaitem[$ccc] ne "" ) {
				$cbc ++;
				}
				$ccc ++;
			}
	if ( $cbc == 0 ) {
print <<"HTM";
「シヨウ　デキル　アイテム　ガ　アリマセン」<br>
&bankform;
HTM
	} else {
			$ccc = 1;$cba = 0;
			while ( $ccc < 9 ) {
				if ( $chaitem[$ccc] ne "" ) {
open(KAI,"$maindir/item$bousikts");
		while ( $kaitori = <KAI> ) {
			($kainame,$a,$a,$a,$a,$a,$itemstats,$itemstats2) = split(/,/,$kaitori);
			if ( $chaitem[$ccc] eq $kainame && $itemstats == 10) {
				push(@itemsuuji,$ccc);
				push(@itemkouka,$itemstats2);
				$cba ++;
			}
		}
close(KAI);
				}
$ccc ++;
			}
		if( $cba == 0 ) {
print <<"HTM";
「シヨウ　デキル　アイテム　ガ　アリマセン」<br>
HTM
&bankform;
		} else {
print <<"HTM";
「アイテム　ヲ　センタク　シテクダサイ」<br>
<form method="post" action="./$zonecgi">
<input type=hidden value="1" name="sisetu">
<input type=hidden value="51" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="　   使用する  　" ><br>
<select name="itemds" size=5>
HTM
$add = 0;
			foreach $atai (@itemsuuji) {
		print "<option value=\"$chaitem[$atai]/$atai/$itemkouka[$add]\">$chaitem[$atai] （$chasetumei[$atai]）";
$add ++;
			}
print <<"HTM";
</select></form><br>
HTM
		}
	}

} elsif ( $in{riyou} eq "51"){
($itemname,$itemnum,$itemstats) = split(/\//,$in{itemds});
	if ( $itemname ne $chaitem[$itemnum] ) {
		&CgiError('エラー発生','不正をした疑いがあります。');
	} elsif ( $chahp == $chastats[9] ) {
print <<"HTM";
「アナタ　ハ　ソ\レ　ヲ　シヨウ<br>
　　シテモ　イミ　ガ　アリマセン」<br>
HTM
&bankform;
	} else {
$chahp += $itemstats;
		if ( $chahp > $chastats[9] ) {
			$chahp = $chastats[9];
		}
		if ( $chaeff[$itemnum] == 1 ) {
$chaitem[$itemnum] = $chaeff[$itemnum] = $chasetumei[$itemnum] = "";
		} else {
$chaeff[$itemnum] --;
		}

&charadatawrt;
print <<"HTM";
「アイテム　ヲ　シヨウ　シマシタ」<br>
HTM
&bankform;
	}
} elsif ( $in{riyou} eq "6"){

#　武器防具の装備

&itemkuuran;
	if ( $ccb == 9 ) {
print <<"HTM";
「ソ\ウビ　デキル　アイテム　ガ　アリマセン」<br>
HTM
&bankform;
	} else {
&jobdataload;

	$bbb = 1;$bbc =0;
		while ( $bbb < 9 ) {
open(KAI,"$maindir/item$bousikts");
			while ( $kaitori = <KAI> ) {
				($itemname,$itembasyo,$itemjuuryou,$itemgazou,$itemgold,$itemkouka) = split(/,/,$kaitori);
				if ( $chaitem[$bbb] eq $itemname ) {
					if ( $itemjuuryou <= $jobweight && itemkouka <= 10 ) {
					push(@itemnum,$bbb);push(@itemdoko,$bui[$itembasyo]);
					push(@itemomosa,$omosa[$itemjuuryou]);push(@itemstats,$itemkouka);$bbc ++;
					}
last;
				}
			}
close(KAI);
$bbb ++;
		}


		if ( $bbc == 0 ) {
print <<"HTM";
「ソ\ウビ　デキル　アイテム　ガ　アリマセン」<br>
HTM
&bankform;
		} else {
print <<"HTM";
「アイテム　ヲ　センタク　シテクダサイ」<br>
<form method="post" action="./$zonecgi">
<input type=hidden value="1" name="sisetu">
<input type=hidden value="61" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="　    装備する   　" ><br>
<select name="itemde" size=6>
HTM
	$bbb = 0;
			foreach $num (@itemnum) {
print "<option value=\"$chaitem[$num]/$num\">$itemomosa[$bbb]/$itemdoko[$bbb]/ $chaitem[$num]（$itemstats[$bbb]）";
$bbb ++;
			}
print <<"HTM";
</select></form><br>
HTM
		}
	}
} elsif ( $in{riyou} eq "61"){
		($soubiname,$numa) = split(/\//,$in{itemde});
	if ( $in{itemde} eq "" ) {
print <<"HTM";
「アイテム　ガ　センタク　サレテイマセン」<br>
HTM
&bankform;

	} elsif ( $chaitem[$numa] ne $soubiname) {
		&CgiError('エラー発生','不正をした疑いがあります！');
	} else {
&jobdataload;

if (!open(BAN,"$maindir/item$bousikts")) { &CgiError('エラー発生','ファイル読み込みに失敗しました。'); }
			while ( $soubidayo = <BAN>) {
		($itemname,$itembasyo,$itemjuuryou,$itemga,$itemgold,$itemkouka,$itemstatus[0],$itemti[0],$itemstatus[1],$itemti[1],$itemstatus[2],$itemti[2],$itemstatus[3],$itemti[3],$itemlvl) = split(/,/,$soubidayo);
				if ( $itemname eq $chaitem[$numa] ) {
					last;
				}
			}
close(BAN);

		if ( $itemjuuryou > $jobweight ) {
&CgiError('エラー発生','不正をした疑いがあります！');
		} elsif ( $itemlvl > $chalvl ) {
print <<"HTM";
「レベル　ガ　タリマセン」<br>
HTM
&bankform;
		} else {
if (!open(BAN,"$maindir/item$bousikts")) { &CgiError('エラー発生','ファイル読み込みに失敗しました。'); }
			while ( $soubido = <BAN>) {
		($soubname,$soubbasyo,$soubjuuryou,$soubga,$soubgold,$soubkouka,$soubstatus[0],$soubti[0],$soubstatus[1],$soubti[1],$soubstatus[2],$soubti[2],$soubstatus[3],$soubti[3]) = split(/,/,$soubido);
				if ( $soubname eq $chasoubi[$itembasyo] ) {
					last;
				}
			}
close(BAN);

$kariname = $chasoubi[$itembasyo];$karisetumei = $chabun[$itembasyo];
$chasoubi[$itembasyo] = $chaitem[$numa];$chabun[$itembasyo] = $chasetumei[$numa];$chabougue[$itembasyo] = $itemga;

	$eaa = 0;
			while ( $eaa < 4 ) {
				if ( $itemstatus[$eaa] eq "" ) { last; } else {

				$karistats[$itemstatus[$eaa]] += $itemti[$eaa];

				}
		$eaa ++;
			}
			if ( $kariname ne "" ) {
	$eaq = 0;
				while ( $eaq < 4 ) {
					if ( $soubstatus[$eaq] eq "" ) { last; } else {
					$karistats[$soubstatus[$eaq]] -= $soubti[$eaq];


					}
		$eaq ++;
				}
			}
$chaitem[$numa] = $kariname;$chasetumei[$numa] = $karisetumei;
			if ( $chaitem[$numa] eq "" ) { $chaeff[$numa] ="";} else {$chaeff[$numa] = 1;}
&charadatawrt;
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
「<font size=4 color=#$mojiiro2><b>$chasoubi[$itembasyo] </font>($chabun[$itembasyo]) ヲ</b><br>
   ソ\ウビ　シマシタ」<br>
HTM
&bankform;
		}
	}







} elsif ( $in{riyou} eq "7"){

#　所持アイテムを捨てる

&itemsentaku;
} elsif ( $in{riyou} eq "71"){
print <<"HTM";
「<font size=4 color=#$mojiiro2><b>$chaitem[$in{itemde}]</font> ($chasetumei[$in{itemde}])</b>　ヲ　ステマシタ」<br>
HTM
$chaitem[$in{itemde}] = $chaeff[$in{itemde}] = $chasetumei[$in{itemde}] = "";
&charadatawrt;
&bankform;
} else {
$bankgold = &put_comma($bankgold);
#　銀行コマンド一覧

print <<"HTM";
「イラッシャイマセ  <b>$chaname</b>  サマ」<br>
HTM
&bankform;
}


&townmodori;
&pettukitable;
&itemtable;
&hpowari;

exit;

sub bankform {
print <<"HTM";
<center><br><table border=1>
<tr><td><table border=0>
<tr><td><nobr>預金：</nobr></td><td width=70 align=right><nobr><font color=#$chamoji><b>$bankgold</font> G</b></nobr></td></tr></table></td></tr></table>
　　　　<font size=1>（金額は半角数字で入力）</font><br>
</center>
<nobr><form method="post" action="./$zonecgi">
<input type=hidden value="1" name="sisetu">
<input type=hidden value="1" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="   所持金を預ける  ">
<input type=text value="$chagold" name="okane" size=7 maxlength=18>G
</form></nobr>
HTM

if ( $bankgold ne "0" ) {
print <<"HTM";
<nobr><form method="post" action="./$zonecgi">
<input type=hidden value="1" name="sisetu">
<input type=hidden value="2" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="  預金を引き出す  ">
<input type=text value="" name="okane" size=7 maxlength=18>G
</form></nobr>
HTM
}
print <<"HTM";
<nobr>
<form method="post" action="./$zonecgi">
<input type=hidden value="1" name="sisetu">
<input type=hidden value="3" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="  アイテムを預ける  ">
</form>
<form method="post" action="./$zonecgi">
<input type=hidden value="1" name="sisetu">
<input type=hidden value="4" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value=" アイテムを引き出す">
</form></td><td width=30></td><td>
<center><br><table border=1>
<tr><td><table border=0>
<tr><td><nobr>福引券：</nobr></td><td width=70 align=right><nobr><font color=#$chamoji><b>$bankhukubiki</font> 枚</b></nobr></td></tr></table></td></tr></table>
　　　　<font size=1>（数字は半角数字で入力）</font><br>
</center>
<nobr><form method="post" action="./$zonecgi">
<input type=hidden value="1" name="sisetu">
<input type=hidden value="11" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="  福引券を預ける ">
<input type=text value="$hukubiki" name="hukubiki" size=3 maxlength=18>枚
</form></nobr>
HTM
if ( $bankhukubiki ne "0" ) {
print <<"HTM";
<nobr><form method="post" action="./$zonecgi">
<input type=hidden value="1" name="sisetu">
<input type=hidden value="12" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="福引券を引き出す">
<input type=text value="$bankhukubiki" name="hukubiki" size=3 maxlength=18>枚
</form></nobr>
HTM
}

print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="1" name="sisetu">
<input type=hidden value="6" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="アイテムを装備する">
</form>
<form method="post" action="./$zonecgi">
<input type=hidden value="1" name="sisetu">
<input type=hidden value="7" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value=" アイテムを捨てる ">
</form>
HTM
}












sub bankwrt {
open(BANK,">$maindir/$foldacha/bankg_$in{usrid}$bousi2cha$bousikts");
	print BANK "$bankgold";
close(BANK);
}

sub bankwrt2 {
open(HUKU,">$maindir/$foldacha/hukubiki_$in{usrid}$bousi2cha$bousikts");
	print HUKU "$bankhukubiki";
close(HUKU);
}


sub itemsagasi {
			$ccc = 1;
			while ( $ccc < 9 ) {
				if ( $chaitem[$ccc] ne "" ) {
				print "<option value=\"$ccc\">$chaitem[$ccc] ($chasetumei[$ccc])";
				}
				$ccc ++;
			}
print <<"HTM";
</select></form><br>
HTM
}

sub itemkuuran {
			$ccc = 1;$ccb = 0;
			while ( $ccc < 9 ) {
				if ( $chaitem[$ccc] eq "" ) {
				$ccb ++;
				}
				$ccc ++;
			}

}
sub put_comma {
  my $num = $_[0];
  $num = reverse $num;
  $num =~ s/(\d{3})(?=\d)(?!\d*\.)/$1,/g;
  $num = reverse $num;
  return $num
}
sub itemsentaku {
&itemkuuran;
	if ( $ccb eq 8 ) {
print <<"HTM";
「アイテム　ガ　アリマセン」<br>
HTM

	} else {
		if ( $in{riyou} eq "3" ) {
$comme = "預ける";
$riyo = "31";
		} elsif ( $in{riyou} eq "7" ) {
$comme = "捨てる";
$riyo = "71";
		}
print <<"HTM";
「アイテム　ヲ　センタク　シテクダサイ」<br>
<form method="post" action="./$zonecgi">
<input type=hidden value="1" name="sisetu">
<input type=hidden value="$riyo" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="　    $comme   　" ><br>
<select name="itemde" size=6>
HTM
&itemsagasi;
	}

}

1;