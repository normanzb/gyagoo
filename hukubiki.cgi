&topsisetu;
print <<"HTM";
いらっしゃい！<br>
福引券を持っていれば福引が出来るよ！<br><br>
HTM
if ( $in{riyou} eq "1" ) {
	if ( $hukubiki < 1) {
print <<"HTM";
<b><font color=red>福引券を持っていません。</font></b><br>
HTM
		} else {
$keihin = int( rand(5000) );
		if ( $keihin < 1 ) {
if (!open(BANKI,">>$maindir/$foldacha/bankit_$in{usrid}$bousi2cha$bousikts")) { &CgiError('エラー発生','ファイルオープンに失敗しました。'); }
flock(BANKI,2);
	print BANKI "魔剣ラグナロク/DMG 50、STR +30、AGI +30、SVM +30\n";
flock(BANKI,8);
close(BANKI);
print <<"HTM";
<font size=6 color=#$mojiiro3><b>特賞</b></font>　<font color=#$chamoji><b>魔剣ラグナロク</b></font>が当たりました！<br><br>
HTM
$hukubiki --;
&charadatawrt;

		} elsif ( $keihin < 3 ) {
if (!open(BANKI,">>$maindir/$foldacha/bankit_$in{usrid}$bousi2cha$bousikts")) { &CgiError('エラー発生','ファイルオープンに失敗しました。'); }
flock(BANKI,2);
	print BANKI "マーメイドリング/獲得EXPを2倍にする\n";
flock(BANKI,8);
close(BANKI);
print <<"HTM";
<font size=6 color=#$mojiiro3><b>１等</b></font>　<font color=#$chamoji><b>マーメイドリング</b></font>が当たりました！<br><br>
HTM
$hukubiki --;
&charadatawrt;

		} elsif ( $keihin < 10 ) {
if (!open(BANKI,">>$maindir/$foldacha/bankit_$in{usrid}$bousi2cha$bousikts")) { &CgiError('エラー発生','ファイルオープンに失敗しました。'); }
flock(BANKI,2);
	print BANKI "鬼神の秘薬/各ステータスを大幅に上げる\n";
flock(BANKI,8);
close(BANKI);
print <<"HTM";
<font size=6 color=#$mojiiro3><b>２等</b></font>　<font color=#$chamoji><b>鬼神の秘薬</b></font>が当たりました！<br><br>
HTM
$hukubiki --;
&charadatawrt;

		} elsif ( $keihin < 20 ) {
if (!open(BANKI,">>$maindir/$foldacha/bankit_$in{usrid}$bousi2cha$bousikts")) { &CgiError('エラー発生','ファイルオープンに失敗しました。'); }
flock(BANKI,2);
	print BANKI "神龍丸薬/最大TPを30上げる\n";
flock(BANKI,8);
close(BANKI);
print <<"HTM";
<font size=6 color=#$mojiiro3><b>３等</b></font>　<font color=#$chamoji><b>神龍丸薬</b></font>が当たりました！<br><br>
HTM
$hukubiki --;
&charadatawrt;

		} elsif ( $keihin < 35 ) {
if (!open(BANKI,">>$maindir/$foldacha/bankit_$in{usrid}$bousi2cha$bousikts")) { &CgiError('エラー発生','ファイルオープンに失敗しました。'); }
flock(BANKI,2);
	print BANKI "天龍丸薬/最大TPを10上げる\n";
flock(BANKI,8);
close(BANKI);
print <<"HTM";
<font size=6 color=#$mojiiro3><b>４等</b></font>　<font color=#$chamoji><b>天龍丸薬</b></font>が当たりました！<br><br>
HTM
$hukubiki --;
&charadatawrt;

		} elsif ( $keihin < 100 ) {
print <<"HTM";
<font size=6 color=#$mojiiro3><b>５等</b></font>　<font color=#$chamoji><b>700</b></font>ＣＰが当たりました！<br><br>
HTM
$chastats[14] += 700;
$hukubiki --;
&charadatawrt;

		} elsif ( $keihin < 200 ) {
print <<"HTM";
<font size=6 color=#$mojiiro3><b>６等</b></font>　<font color=#$chamoji><b>5000</b></font>Ｇが当たりました！<br><br>
HTM
$chagold += 5000;
$hukubiki --;
&charadatawrt;

		} elsif ( $keihin < 300 ) {
print <<"HTM";
<font size=6 color=#$mojiiro3><b>７等</b></font>　<font color=#$chamoji><b>福引券</b></font>５枚が当たりました！<br><br>
HTM
$hukubiki --;
$hukubiki += 5;
&charadatawrt;

		} elsif ( $keihin < 450 ) {
if (!open(BANKI,">>$maindir/$foldacha/bankit_$in{usrid}$bousi2cha$bousikts")) { &CgiError('エラー発生','ファイルオープンに失敗しました。'); }
flock(BANKI,2);
	print BANKI "神薬/HP･TPを全回復\n";
flock(BANKI,8);
close(BANKI);
print <<"HTM";
<font size=6 color=#$mojiiro3><b>８等</b></font>　<font color=#$chamoji><b>神薬</b></font>が当たりました！<br><br>
HTM
$hukubiki --;
&charadatawrt;

		} elsif ( $keihin < 1200 ) {
if (!open(BANKI,">>$maindir/$foldacha/bankit_$in{usrid}$bousi2cha$bousikts")) { &CgiError('エラー発生','ファイルオープンに失敗しました。'); }
flock(BANKI,2);
	print BANKI "タブレットγ/TPを120回復\n";
flock(BANKI,8);
close(BANKI);
print <<"HTM";
<font size=6 color=#$mojiiro3><b>９等</b></font>　<font color=#$chamoji><b>タブレットγ</b></font>が当たりました！<br><br>
HTM
$hukubiki --;
&charadatawrt;

		} elsif ( $keihin < 2500 ) {
if (!open(BANKI,">>$maindir/$foldacha/bankit_$in{usrid}$bousi2cha$bousikts")) { &CgiError('エラー発生','ファイルオープンに失敗しました。'); }
flock(BANKI,2);
	print BANKI "エクスポーション/HPを1200回復\n";
flock(BANKI,8);
close(BANKI);
print <<"HTM";
<font size=6 color=#$mojiiro3><b>１０等</b></font>　<font color=#$chamoji><b>エクスポーション</b></font>が当たりました！<br><br>
HTM
$hukubiki --;
&charadatawrt;

		} else {
print <<"HTM";
<font size=6><b>残念・・・ハズレ！</b></font><br><br>
HTM
$hukubiki --;
&charadatawrt;

}
	}
}



if ( $in{riyou} eq "2" ) {
	if ( $hukubiki < 10) {
print <<"HTM";
<b><font color=red>福引券が足りません。</font></b><br>
HTM
		} else {
if (!open(BANKI,">>$maindir/$foldacha/bankit_$in{usrid}$bousi2cha$bousikts")) { &CgiError('エラー発生','ファイルオープンに失敗しました。'); }
flock(BANKI,2);
	print BANKI "丸薬/最大TPを1上げる\n";
flock(BANKI,8);
close(BANKI);
print <<"HTM";
<b>福引券10枚と、丸薬を交換しました。</b><br><br>
HTM
$hukubiki -= 10;
}
&charadatawrt;
}

if ( $in{riyou} eq "3" ) {
	if ( $hukubiki < 50) {
print <<"HTM";
<b><font color=red>福引券が足りません。</font></b><br>
HTM
		} else {
if (!open(BANKI,">>$maindir/$foldacha/bankit_$in{usrid}$bousi2cha$bousikts")) { &CgiError('エラー発生','ファイルオープンに失敗しました。'); }
flock(BANKI,2);
	print BANKI "天龍丸薬/最大TPを10上げる\n";
flock(BANKI,8);
close(BANKI);
print <<"HTM";
<b>福引券50枚と、天龍丸薬を交換しました。</b><br><br>
HTM
$hukubiki -= 50;
}
&charadatawrt;
}




&kunrenform;
sub kunrenform {
print <<"HTM";
<font size=-1>現在の福引券</font>：<b>$hukubiki</b><font size=-1>枚</font>
<form method="post" action="./$zonecgi">
<input type=hidden value="15" name="sisetu">
<input type=hidden value="1" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="   福引をする   " size=30>　【福引券<b>１</b>枚】
</form>
<form method="post" action="./$zonecgi">
<input type=hidden value="15" name="sisetu">
<input type=hidden value="2" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="   丸薬と交換   " size=30>　【福引券<b>１０</b>枚】
</form>
<form method="post" action="./$zonecgi">
<input type=hidden value="15" name="sisetu">
<input type=hidden value="3" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="天龍丸薬と交換" size=30>　【福引券<b>５０</b>枚】
</form>

<SCRIPT language="JavaScript">
<!--
function OpenWin(){
win=window.open("./fukubiki.html","new","width=240,height=305");
}
// -->

</SCRIPT>
</HEAD>

<BODY>
<INPUT type="button" value="　　景品一覧　　" onClick="OpenWin()">
</BODY>



HTM
}
&townmodori;
1;