


if ( $bankgold eq "" ) { $bankgold = 0 ; }

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

} elsif ( $in{riyou} eq "3"){

#　アイテムを預ける

&itemsentaku;
} elsif ( $in{riyou} eq "31"){
open(DASU,"$maindir/$foldamarket/market_data$bousi3cha$bousi2kts");
  @item = <DASU>;
close(DASU);
  $itemsousuu = @item;
	if ( $itemsousuu >= 300 ) {
print <<"HTM";
「アイテムは３００個までしか入りません。」<br>
HTM
        }elsif ( $in{itemde} eq "" ) {
print <<"HTM";
「アイテムが選択されていませんでした。」<br>

HTM
	} elsif ( $chaitem[$in{itemde}] eq "" ) {
&fuseisyori;
	} else {
		if ( $chaeff[$in{itemde}] eq "" ) {
&fuseisyori;
		} elsif ( $chaeff[$in{itemde}] > 1 ) {
$chaeff[$in{itemde}] --;
if (!open(DASU,">>$maindir/$foldamarket/market_data$bousi3cha$bousi2kts")) { &CgiError('エラー発生','ファイルオープンに失敗しました。'); }
flock(DASU,2);
	print DASU "$chaitem[$in{itemde}]/$chasetumei[$in{itemde}]\n";
flock(DASU,8);
close(DASU);
$morai += 0.3;
&charadatawrt;
print <<"HTM";

「１個だけ寄付しました。ありがとうございました。」<br>
HTM
&bankform;
		} else {
if (!open(DASU,">>$maindir/$foldamarket/market_data$bousi3cha$bousi2kts")) { &CgiError('エラー発生','ファイルオープンに失敗しました。'); }
flock(DASU,2);
	print DASU "$chaitem[$in{itemde}]/$chasetumei[$in{itemde}]\n";
flock(DASU,8);
close(DASU);
$chaitem[$in{itemde}] = $chaeff[$in{itemde}] = $chasetumei[$in{itemde}] = "";
$morai += 0.4;
&charadatawrt;
print <<"HTM";

「確かに寄付しました。ありがとうございました。」<br>
HTM

&bankform;
		}
	}

} elsif ( $in{riyou} eq "4"){

#　アイテムを引き出す

if (!open(DASU,"$maindir/$foldamarket/market_data$bousi3cha$bousi2kts")) { &CgiError('エラー発生','ファイルオープンに失敗しました。'); }
	$bchk = <DASU>;
close(DASU);
	if ( $bchk eq "" ) {
int ($morai);
print <<"HTM";
「残念ながら、アイテムは入っていないようです。」<br>
HTM
&bankform;
	} else {
print <<"HTM";
「以下のアイテムが収められています。」<br>
<form method="post" action="./$zonecgi">
<input type=hidden value="14" name="sisetu">
<input type=hidden value="41" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="　   貰う  　" ><br>
<select name="itemds" size=20>
HTM
$abb = 0;
if (!open(MARK,"$maindir/$foldamarket/market_data$bousi3cha$bousi2kts")) { &CgiError('エラー発生','ファイルオープンに失敗しました。'); }
		while ( $bankno = <MARK> ) {
		chop($bankno);
	($urimononame,$bankbun) = split(/\//,$bankno);
print "<option value=\"$urimononame/$bankbun/$abb\">$urimononame（$bankbun）";
$abb ++;
		}
close(MARK);
print <<"HTM";
</select></form><br>
HTM
	}
} elsif ( $in{riyou} eq "41"){
&itemkuuran;

	if ( $morai < 1 ) {
print <<"HTM";
$chanameが箱からアイテムを取り出そうとした時、<br>
背後から長老が現れた。<br><br>
長老「$chaname・・・。ちょっと欲張りすぎではないか？」<br>
$chaname「・・・。」<br><br>
$chanameはしぶしぶアイテムを箱の中に戻し、その場を立ち去る事にした。
HTM


	} elsif ( $ccb eq "0" ) {
print <<"HTM";
「持ち物がいっぱいで持てません。」<br>
HTM



	} else {
	($urimononame,$bankbun,$aba) = split(/\//,$in{itemds});
open(MARK,"$maindir/$foldamarket/market_data$bousi3cha$bousi2kts");
		@banban = <MARK>;
close(MARK);

$abd = 0;
open(BANN,">$maindir/$foldamarket/$in{usrid}.tmp");
flock(BANN,2);
		foreach $a (@banban) {
			($kk,$ll) = split(/\//,$a);
#VER106 Start アイテム消失バグ修正
#			if ( $abd eq $aba && $urimononame eq $kk ) {
			if ( $abd eq $aba && $urimononame eq $kk && $puchk != 1) {
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

rename("$maindir/$foldamarket/$in{usrid}.tmp","$maindir/$foldamarket/market_data$bousi3cha$bousi2kts");

	if($chastats[2] > 12){
			$ccc = 1;$ccb = 0;
			while ( $ccc < 10 ) {
				if ( $chaitem[$ccc] eq $urimononame ) {
					$cce = $ccc;$ccd = 1;last;
				} 
				$ccc ++;
			}
			$ccc = 1;
	} elsif ($chastats[2] > 17){
			$ccc = 1;$ccb = 0;
			while ( $ccc < 11 ) {
				if ( $chaitem[$ccc] eq $urimononame ) {
					$cce = $ccc;$ccd = 1;last;
				} 
				$ccc ++;
			}
			$ccc = 1;
	} elsif ($chastats[2] > 19){
			$ccc = 1;$ccb = 0;
			while ( $ccc < 12 ) {
				if ( $chaitem[$ccc] eq $urimononame ) {
					$cce = $ccc;$ccd = 1;last;
				} 
				$ccc ++;
			}
			$ccc = 1;
	} elsif ($chastats[2] > 21){
			$ccc = 1;$ccb = 0;
			while ( $ccc < 12 ) {
				if ( $chaitem[$ccc] eq $urimononame ) {
					$cce = $ccc;$ccd = 1;last;
				} 
				$ccc ++;
			}
			$ccc = 1;
	} else {
			$ccc = 1;$ccb = 0;
			while ( $ccc < 9 ) {
				if ( $chaitem[$ccc] eq $urimononame ) {
					$cce = $ccc;$ccd = 1;last;
				} 
				$ccc ++;
			}
			$ccc = 1;
	}




			while ( $ccc < 9 ) {
				if ( $chaitem[$ccc] eq "" ) {
				$ccb = $ccc;last;
				}
				$ccc ++;
	}


		if ( $ccd == 1 ) {
$chaeff[$cce] ++;
$morai --;
		} else {
$chaitem[$ccb] = $urimononame;$chaeff[$ccb] = 1;$chasetumei[$ccb] = $bankbun;
		}
&charadatawrt;
print <<"HTM";
「$urimononameを貰いました。」<br>
HTM

&bankform;

	}
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
				$chastats[$itemstatus[$eaa]] += $itemti[$eaa];
				}
		$eaa ++;
			}
			if ( $kariname ne "" ) {
	$eaq = 0;
				while ( $eaq < 4 ) {
					if ( $soubstatus[$eaq] eq "" ) { last; } else {
					$chastats[$soubstatus[$eaq]] -= $soubti[$eaq];
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

#　銀行コマンド一覧

print <<"HTM";
「リサイクルボックス」<br>
HTM
&bankform;
}


&townmodori;
&pettukitable;
&itemtable;
&hpowari;

exit;

sub bankform {


if ( $bankgold ne "0" ) {
print <<"HTM";
<nobr><form method="post" action="./$zonecgi">
<input type=hidden value="14" name="sisetu">
<input type=hidden value="2" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="  預金を引き出す  ">
<input type=text value="$bankgold" name="okane" size=7 maxlength=18>G
</form></nobr>
HTM
}
print <<"HTM";
<nobr>
<form method="post" action="./$zonecgi">
<input type=hidden value="14" name="sisetu">
<input type=hidden value="4" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="ボックスの中身を見る">
</form>
<form method="post" action="./$zonecgi">
<input type=hidden value="14" name="sisetu">
<input type=hidden value="3" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value=" アイテムを寄付する ">
</form>
HTM
}





sub bankwrt {
open(MARK,">$maindir/$foldamarket/market_data$bousi2cha$bousikts");
	print MARK "$bankgold";
close(MARK);
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
sub itemsentaku {
&itemkuuran;
	if ( $ccb eq 12 ) {
print <<"HTM";
「アイテムを持っていません。」<br>
HTM

	} else {
		if ( $in{riyou} eq "3" ) {
$comme = "寄付する";
$riyo = "31";
		} elsif ( $in{riyou} eq "7" ) {
$comme = "捨てる";
$riyo = "71";
		}
print <<"HTM";
「寄付するアイテムを選択してください。」<br>
<form method="post" action="./$zonecgi">
<input type=hidden value="14" name="sisetu">
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