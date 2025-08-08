&topsisetu;

#　アイテム購入処理
if ( $in{riyou} eq "1"){
print <<"HTM";
何と変換するんだい？<br>
<b>CP</b>は貴重なものだからよく考えて使うんだよ。<br>
ヒッヒッヒ。<br><br>
HTM
&kounyuu;
} elsif ( $in{riyou} eq "11"){
($itemname,$itemjuuryou,$itemgold,$itemkouka) = split(/\//,$in{itemkai});
	if ( $chastats[14] < $itemgold ) {
print <<"HTM";
おやおや、<b>CP</b>が足りないようじゃ。<br>
それが欲しいなら、もっと経験を積んでから来るとよかろう。<br><br>
ヒッヒ。
HTM
&shopform;
	} elsif ( $in{itemkai} eq "" ) {
print <<"HTM";
んん？　どれと変換したいんだい？<br>
きちんと変換したいアイテムを選択しなさい。<br><br>
ヒッヒッヒ。
HTM
&shopform;
	} else {
			$ddd = 1;
		if ( $itemjuuryou >= 10 && $itemjuuryou <= 49 ) {
			while ( $ddd < 9 ) {
				if ( $chaitem[$ddd] eq $itemname ) {
				last;
				}
				$ddd ++;
			}
			if ( $ddd > 8 ) {
&itemkuuran;
				if ( $ccc > 8 ) {
print <<"HTM";
ふむ。<br>
残念じゃが、お前はそれ以上物を持てないようじゃのう。<br>
荷物を整理してからまた来るとよかろう。
HTM
&shopform;
				
				} else {
$chastats[14] -= $itemgold;
$chaitem[$ccc] = $itemname;
$chaeff[$ccc] = 1;
$chasetumei[$ccc] = $itemkouka;
&charadatawrt;
print <<"HTM";
<font size=4 color=#$mojiiro3><b>$itemname</b></font> ($itemkouka)  でいいんだね。<br>
<b><font color=red>アイヤ～～～ッ！！</b></font><br>
ふぅ、できあがったよ。持っておいき。
HTM
&kounyuu;
&shopform;
				}
			} elsif ( $chaeff[$ddd] > 998 ) {
print <<"HTM";
そのアイテムはすでに容量いっぱいのようじゃ。<br>
複数個所持できるアイテムは最高999個までしか持てないのじゃ。<br>
覚えておくといいぜ。<br>
他に何か生成して欲しい物はあるかい？<br>
HTM
&kounyuu;
&shopform;
			} else {
$chaeff[$ddd] ++;
$chastats[14] -= $itemgold;
$chasetumei[$ddd] = $itemkouka;
&charadatawrt;
print <<"HTM";
<font size=4 color=#$mojiiro3><b>$itemname</b></font> ($itemkouka) じゃな。<br>
個数増やしておいたぞよ。<br>
まだ変換する物はあるのかい？
HTM
&kounyuu;
&shopform;
			}

		} elsif ( $itemjuuryou >= 50 ) {
			if ( $itemjuuryou == 50 ) { $itemname = "ポーション"; }
			if ( $itemjuuryou == 51 ) { $itemname = "ハイポーション"; }
			if ( $itemjuuryou == 52 ) { $itemname = "ミドルポーション"; }
			if ( $itemjuuryou == 53 ) { $itemname = "エクスポーション"; }
			if ( $itemjuuryou == 54 ) { $itemname = "エリクサー"; }
			if ( $itemjuuryou == 55 ) { $itemname = "不思議な翼"; }
			if ( $itemjuuryou == 56 ) { $itemname = "ハイエリクサー"; }
			if ( $itemjuuryou == 57 ) { $itemname = "ラストエリクサー"; }
			if ( $itemjuuryou == 58 ) { $itemname = "スーパーエリクサー"; }
			if ( $itemjuuryou == 59 ) { $itemname = "メガエリクサー"; }
			if ( $itemjuuryou == 60 ) { $itemname = "ギガエリクサー"; }
			if ( $itemjuuryou == 61 ) { $itemname = "テラエリクサー"; }
			if ( $itemjuuryou == 62 ) { $itemname = "神薬"; }
$ddd = 1;
			while ( $ddd < 9 ) {
				if ( $chaitem[$ddd] eq $itemname ) {
				last;
				}
				$ddd ++;
			}
			if ( $ddd > 8 ) {
print <<"HTM";
残念じゃが、セットアイテムは<br>
所持アイテムに１つでも持っていないと<br>
生成することはできんのじゃ。すまんのぅ。<br>
HTM
&shopform;
			} elsif ( $chaeff[$ddd] > 998 ) {
print <<"HTM";
おや、欲張りだねぇ。<br>
そのアイテムは、もう十分すぎるほど持ってるじゃろう。<br>
ある程度なくなったら生成してやろうかいのう。ヒヒ。<br>
HTM
&shopform;
			} else {
$chaeff[$ddd] += 10;
$chastats[14] -= $itemgold;
&charadatawrt;
print <<"HTM";
<font size=4 color=#$mojiiro3><b>$itemname</font></b> ($itemkouka) じゃな。<br>
個数増やしておいたぞよ。<br>
まだ変換する物はあるのかい？
HTM
&kounyuu;
&shopform;			}

		} else {
&itemkuuran;
			if ( $ccc > 8 ) {
print <<"HTM";
ふむ。<br>
残念じゃが、お前はそれ以上物を持てないようじゃのう。<br>
荷物を整理してからまた来るとよかろう。
HTM
&shopform;
			} else {
$chastats[14] -= $itemgold;
$chaitem[$ccc] = $itemname;
$chaeff[$ccc] = 1;
$chasetumei[$ccc] = $itemkouka;
&charadatawrt;
print <<"HTM";
<font size=4 color=#$mojiiro3><b>$itemname</font></b> ($itemkouka) でいいんだね。<br>
<b><font color=red>アイヤ～～～ッ！！</b></font><br>
ふぅ、できあがったよ。持っておいき。
HTM
&jobdataload;
				if ( $itemjuuryou > $jobweight) {
print <<"HTM";
<br>おや、これは$omosa[$itemjuuryou]装備じゃから<br>
今のあんたの職業じゃ装備できんぞい。<br>
まぁ、生成してしまった物は仕方ないね。<br>
<br>
HTM
				}
print <<"HTM";
まだ変換するのかい？ヒッヒ。
HTM
&kounyuu;
&shopform;
			} 
		}
	}

#　アイテム売却処理
} elsif ( $in{riyou} eq "2"){
print <<"HTM";
オーケィ。なんでも買い取ってやるぜ。<br>
売りたいものを選択してくれ。<br>
HTM
&baikyaku;
} elsif ( $in{riyou} eq "21"){
($kainame,$kaigold,$itemnum,$itemkouka) = split(/\//,$in{itemuri});
	if ( $kainame eq "" ) {
print <<"HTM";
んん？　何を売るんだ？<br>
きちんと売りたいアイテムを選択してくれ。<br><br>
冷やかしなら帰ってもらうぜ。
HTM
&shopform;

	} else {
print <<"HTM";
<b><font size=5 color=#$mojiiro2>$kainame</font></b> ($itemkouka)  か。
<b><font size=5 color=#$mojiiro3>$kaigold</font> G</b> ってとこだな。<br><br>
HTM

		if ( $chaitem[$itemnum] eq $kainame && $chaeff[$itemnum] eq "1" ) {
$chaitem[$itemnum] = $chaeff[$itemnum] = $chasetumei[$itemnum] = "";$chagold += $kaigold;
&charadatawrt;
		} elsif ( $chaitem[$itemnum] eq $kainame && $chaeff[$itemnum] ne "1" ) {
$chaeff[$itemnum] --;$chagold += $kaigold;
&charadatawrt;
		} else { &fuseisyori;exit;
		}
print <<"HTM";
また何か掘り出し物を見つけたらよろしく。<br>
まだ買い取って欲しいものはあるか？
HTM
	}
&baikyaku;
&shopform;

#　アイテム鑑定処理
} elsif ( $in{riyou} eq "3"){
print <<"HTM";
うむ。俺の目は確かだぜ。<br>
どれを鑑定して欲しいんだい？<br>
HTM
&kantei;
&shopform;
} elsif ( $in{riyou} eq "31"){
open(KAI,"$maindir/item$bousikts");
		while ( $kaitori = <KAI> ) {
			($itemname,$itembasyo,$itemjuuryou,$itemga,$itemgold,$itemkouka,$itemstatus[0],$itemti[0],$itemstatus[1],$itemti[1],$itemstatus[2],$itemti[2],$itemstatus[3],$itemti[3],$itemlvl) = split(/,/,$kaitori);
			if ( $chaitem[$in{kantei}] eq $itemname ) {
			last;
			}
		}
close(KAI);
print <<"HTM";
ふむ。<font size=+1><b>$itemname</b></font>か。<br>
こんな感じだな。<br><br>
<table border=1><tr>
<td>名前</td><td colspan=3><nobr>$itemname</nobr></td></tr>
<tr><td><nobr>部位</nobr></td><td><nobr>$bui[$itembasyo]</nobr></td><td>重量</td><td>$omosa[$itemjuuryou]</td></tr>
<tr><td>価値</td><td><nobr>$itemgold G</nobr></td><td><nobr>効果</nobr></td><td><nobr>$itemkouka</nobr></td></tr>
<tr><td colspan=4>必要レベル : <b>$itemlvl</b></td></tr>
</table><br>まだ鑑定して欲しいものはあるか？
HTM
&kantei;
&shopform;


} else {
print <<"HTM";
いらっしゃい、よく来たねぇ。<br>
ここで、<b>CP</b>をアイテムに変換する事が出来るよ。<br>
ヒッヒッヒ。<br><br>
HTM
&shopform;
}


&townmodori;
&pettukitable;
&itemtable;
&hpowari;

exit;

sub shopform {
	if ( $in{riyou} ne "" ) {

	}
	if ( $in{riyou} eq "" || $in{riyou} == 2 || $in{riyou} == 21 || $in{riyou} == 3 || $in{riyou} == 31 ) {
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="11" name="sisetu">
<input type=hidden value="1" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="   品物を見る   ">
</form>
HTM
	}
	if ( $in{riyou} eq "" || $in{riyou} == 1 || $in{riyou} == 11 || $in{riyou} == 3 || $in{riyou} == 31 ) {

	}
}

sub itemkuuran {
			$ccc = 1;
			while ( $ccc < 9 ) {
				if ( $chaitem[$ccc] eq "" ) {
				last;
				}
				$ccc ++;
			}
}

sub kounyuu {
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="11" name="sisetu">
<input type=hidden value="11" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="　   変換する  　" >　　
<font size=-1>現在のCP</font>：<b>$chastats[14]</b><br>
<select name="itemkai" size=20>
HTM
	open(ITEM,"$maindir/shop2$bousikts");
while ( $itemda = <ITEM> ) {
	@itemdaa = split(/,/,$itemda);
	($itemname,$itembasyo,$itemjuuryou,$itemga,$itemgold,$itemkouka,$itemstatus[0],$itemti[0],$itemstatus[1],$itemti[1],$itemstatus[2],$itemti[2],$itemstatus[3],$itemti[3]) = @itemdaa;
print "<option value=\"$itemname/$itemjuuryou/$itemgold/$itemkouka\">【$itemgold CP】$omosa[$itemjuuryou]/$bui[$itembasyo] ● $itemname （$itemkouka）";
	}
close(ITEM);
print <<"HTM";
</select></form></td><td width=30></td><td>
HTM
}

sub baikyaku {

print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="11" name="sisetu">
<input type=hidden value="21" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value=" 買取してもらう " ><br>
<select name="itemuri" size=8>
HTM

$bbb = 1;
	while ( $bbb < 9 ) {
	if ( $chaitem[$bbb] ne "" ) {
open(KAI,"$maindir/item$bousikts");
		while ( $kaitori = <KAI> ) {
			($kainame,$a,$b,$c,$kaigold,$itemkouka) = split(/,/,$kaitori);
			if ( $chaitem[$bbb] eq $kainame ) {
			last;
			}
		}
		$kaigold = int($kaigold / 2);
		print "<option value=\"$chaitem[$bbb]/$kaigold/$bbb/$itemkouka\">$kaigold G: $chaitem[$bbb] （$itemkouka）";
close(KAI);
	}
		$bbb = $bbb + 1;
	}
print <<"HTM";
</select>
<input type=hidden value="$bbc" name="itemnu">
</form></td><td width=30></td><td>
HTM

}

sub kantei {
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="11" name="sisetu">
<input type=hidden value="31" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<select name="kantei">
HTM
$yyy = 1;
	while ( $yyy < 9 ) {
		if ( $chaitem[$yyy] ne "" ) {
print "<option value=\"$yyy\">$chaitem[$yyy]<br>";
		}
	$yyy ++;
	}
print <<"HTM";
</select>
<input type=submit value="  鑑定してもらう  ">
</form></td><td width=30></td><td>
HTM

}
1;