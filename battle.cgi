#!/usr/bin/perl

#　↑サーバーの設定に合わせて変更してください。

#　ステータス名
$statsname[2] = "力（STR)";$statsname[3] = "素早さ（AGI）";$statsname[4] = "知性（INT）";$statsname[5] = "魅力（CHA）";
$statsname[6] = "火耐性（SVF）";$statsname[7] = "水耐性（SVC）";$statsname[8] = "魔耐性（SVM）";

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

require "$foldabattle/jobbattle$chaclass.pl";

if ( $in{boss} eq "" ) {$timesa = $now - $chajikan; } else { $timesa = $nexttime; }
if ( $timesa < $nexttime ) { &fuseisyori;exit; }

if ( $in{count} != $chacount ) { &fuseisyori;exit; }

#　モンスターデータ取得
open(MON,"$maindir/$monsfile/monster$chaplace$bousikts2");
@monster = <MON>;
close(MON);

	foreach $monsters ( @monster ) {
		($monspopp,$a) = split(/,/,$monsters);
		push(@monspo,$monspopp);
	}

foreach $monritu (@monspo) {
	$monrand = $monrand + $monritu;
}
# srand;
$monketu = int(rand($monrand));
$monnum = 0;
foreach $monritu (@monspo) {
	$monsuuji = $monsuuji + $monspo[$monnum];
	if ( $monketu < $monsuuji ) {
	last;
	}
	$monnum ++;
}
($monspop,$monsgif,$monsname,$monslvl,$monshp,$monsattack,$monsac,$monscha,$monssvf,$monssvc,$monssvm,$monsexp,$monsgold,$monskouka,$monsitem[0],$monsitem[1],$monsitem[2],$monsitem[3],$monsitem[4],$a) = split(/,/,$monster[$monnum]);
$battleturn = 1;
$mast = 0;
$monshp += $chalvl;
$monshpnow = $monshp;
$chahpnow = $chahp;
$chahpmax = $chastats[9] + $karistats[9];$pow = $chastats[0] + $karistats[0] + $kougeki;$ac = $chastats[1] + $karistats[1] + $mamori;$str = $chastats[2] + $karistats[2];
$agi = $chastats[3] + $karistats[3];$int = $chastats[4] + $karistats[4];$cha = $chastats[5] + $karistats[5];$svf = $chastats[6] + $karistats[6];$svc = $chastats[7] + $karistats[7];$svm = $chastats[8] + $karistats[8];
$lvlpoin = $monslvl - $chalvl;

if ( $lvlpoin < 0 ) { $lvlpoin = 0; }

print <<"HTM";
<SCRIPT LANGUAGE="JavaScript">
defaultStatus="『○ターン目』をクリックすると、戦闘結果まで短縮します。";
<!--
    //メニュー表示関数
    function Menu(){
        //非表示の場合表示にする
        if(menu.style.visibility == "hidden"){
            menu.style.posLeft = event.clientX;
            menu.style.posTop = event.clientY;
            menu.style.visibility = "visible";
        }
        //表示の場合非表示にする
        else if(menu.style.visibility == "visible"){
           menu.style.visibility = "hidden";
        }
        return false;
    }
    //メニュー非表示関数
    function eraseMenu(){
        //表示の場合非表示にする
        if(menu.style.visibility == "visible"){
            menu.style.visibility = "hidden";
        }
    }
// -->
</SCRIPT>
</HEAD>
<BODY onclick="eraseMenu()" oncontextmenu="Menu();return false;">
<!--メニュー用タグ-->
<DIV id="menu" style={position:absolute;visibility:hidden;}>
    <TABLE border=3 bgcolor=gray cellpadding=5>
        <TR>
            <TD bgcolor="silver">
                <center><B>MENU</B></center><P>
                ・<A HREF="#exit">結果表\示<BR></a>
                ・<A HREF="$urlbbs" target="blank">掲示板<BR></a>
                ・<a href="javascript:close()">ゲーム終了</a>
            </TD>
        </TR>
    </TABLE>
</DIV>
<!--メニュー用タグここまで-->
HTM

print <<"HTM";

<center><font size=6 color=#$mojiiro2><b>$monsname</b> が現れた！！</font><hr><br>
HTM
if ( $in{boss} eq "" ) { $limit = $maxturn; } else { $limit = $maxturn; }

#　戦闘処理

while ( $battleturn <= $limit ) {
&deathchk;

print <<"HTM";
<table border=0><tr><td bgcolor=#$tableiro align=center><font size=4><nobr><b><center><A HREF="#exit"><font color=black>$battleturn ターン目</font></a></b></nobr></font></td></tr><tr><td>
<table border=0>
HTM

if ($battleturn == 1 ) {
print <<"HTM";
<tr align=center valign="baseline"><td>
<img src="$maindir/$imgfile/$monsgif.gif"></td><td></td><td>
HTM
if($petcode[1] ne ""){ print "<img src=\"$maindir/$imgfile/$petpic[1].gif\" alt=\"$petname[1]\">";}
print "</td><td>";
&charaga;
print "</td><td>";
if($petcode[0] ne ""){ print "<img src=\"$maindir/$imgfile/$petpic[0].gif\" alt=\"$petname[0]\">";}
print "</td><td>";
if($petcode[2] ne ""){ print "<img src=\"$maindir/$imgfile/$petpic[2].gif\" alt=\"$petname[2]\">";}
print "</td></tr>";
} else {
print "<tr><td colspan=3 height=5></td></tr>";

}

$hpbarcha1 = int( ( $chahpnow / $chastats[9] ) * 150 );
if ( $hpbarcha1 != 150 ) {
$hpbarcha2 = 150 - $hpbarcha1;
$hpbardmg2 = "<img src=\"$maindir/$imgfile/hpbar2.gif\" width=$hpbarcha2 height=\"8\">";
}

$hpbarmon1 = int( ( $monshpnow / $monshp ) * 150 );
if ( $hpbarmon1 != 150 ) {
$hpbarmon2 = 150 - $hpbarmon1;
$hpbardmg1 = "<img src=\"$maindir/$imgfile/hpbar2.gif\" width=$hpbarmon2 height=\"8\">";
}

print <<"HTM";
<tr align=center><td>
<font size=4><nobr>$monsname</font></nobr></td><td width=20 rowspan=2><nobr><font size=4 color=#$mojiiro2><b>VS</b></font></nobr></td><td colspan=3><font size=4><nobr>$chaname</font></nobr></td><td></td></tr>
<tr><td><nobr><img src="$maindir/$imgfile/exp.gif" height="10"><img src="$maindir/$imgfile/hpbar1.gif" width=$hpbarmon1 height="8">$hpbardmg1<img src="$maindir/$imgfile/exp.gif" height="10"></nobr></td><td colspan=3><font size=4><nobr><img src="$maindir/$imgfile/exp.gif" height="10"><img src="$maindir/$imgfile/hpbar1.gif" width=$hpbarcha1 height="8">$hpbardmg2<img src="$maindir/$imgfile/exp.gif" height="8"></nobr></td><td></td></tr>
</table><font size=-1><center><b>$monshpnow / $monshp	　　　　　　　　　　　　　	$chahpnow / $chastats[9]</center></b></font><br><br><font size=4>

HTM

$number = 0;
&pethatudou;

#　キャラの攻撃処理
$chastats[13] ++;
$jobexpnow[$chaclass] ++;
if ( $jobexpnow[$chaclass] >= $jobexp[$chaclass] ){
$jobexpnow[$chaclass] = $jobexp[$chaclass];
}

if ( $chasoubi[7] eq "ダブルアタックリング") {
print "<font color=#$chamoji><b>$chaname</b></font> の連続攻撃！！<br>";
} else{
print "<font color=#$chamoji><b>$chaname</b></font> の攻撃！！<br>";
}
$nowstrexp ++;
	if ( $nowstrexp >= $strexp ) {

print <<"HTM";
<center>
<font size=5><span style={filter:glow(color=darkorange,strength=5);position:relative;height:50;width:100%;}>
<font color=white><b>$chaname</b> のSTRが上がった！</font>
</span></font></center>
HTM


$strexp *= 1.3;
if ($strexp > 1000){$strexp = 1000;}
$nowstrexp = 0;
$chastats[2] ++;
	}


# srand;
$monsagi = rand(10);
	if ( $monsagi < 1 ) {
print "<font color=#$mojiiro4>$monsname はヒラリと身をかわした！<br></font>"; 
$nowintexp ++;
	if ( $nowintexp >= $intexp ) {
print <<"HTM";
<center>
<font size=5><span style={filter:glow(color=cornflowerblue,strength=5);position:relative;height:50;width:100%;}>
<font color=white><b>$chaname</b> のINTが上がった！</font>
</span></font></center>
HTM

$intexp *= 1.2;
if ($intexp > 1000){$intexp = 1000;}
$nowintexp = 0;
$chastats[4] ++;
	}
	} else {
&jobatk;
if ($chastats[3] + $karistats[3] > 149 ) { &jobatk; }
if ($chastats[3] + $karistats[3] > 299 ) { &jobatk; }
if ($chastats[3] + $karistats[3] > 449 ) { &jobatk; }
if ($chastats[3] + $karistats[3] > 599 ) { &jobatk; }
if ( $job[$chaclass] eq "勇者") { &jobatk; }
if ( $chasoubi[7] eq "ダブルアタックリング") { &jobatk; }
if ( $houou > 0) { &jobatk; }
&tokunou;
	}

&deathchk;

$number = 1;
&pethatudou;

#　モンスターの攻撃処理
$mitore = rand(3);
$counter = rand(7);

if ( $chaclass == 8 && $counter < 1) {
print "<br><b>$monsname</b> の攻撃！！<br>";

print "<b>$chaname</b>「見切った！」<br>";
} elsif ( $chaclass == 8 && $counter < 2) {
print "<br><b>$monsname</b> の攻撃！！<br>";
print "<b>$chaname</b>「遅い！」<br>";
} elsif ( $chaclass == 80 && $mitore < 1) {
print "<br><b>$monsname</b> は、<b>$chaname</b>に見惚れている！<br>";
} else {
print "<br><b>$monsname</b> の攻撃！！<br>";
$kawasi = 200 - $agi;
# srand;
}
if ( $kawasi < 29 ) {
$kawasi = 30;
}

$kawasiritu = rand( $kawasi );
if ( $kawasiritu < 10 ) {
print "<font color=#$mojiiro4>$chaname は素早い動きで攻撃を避けた！！<br></font>"; 
$nowagiexp ++;
	if ( $nowagiexp >= $agiexp ) {
print <<"HTM";
<center>
<font size=5><span style={filter:glow(color=orchid,strength=5);position:relative;height:50;width:100%;}>
<font color=white><b>$chaname</b> のAGIが上がった！</font>
</span></font></center>
HTM

$agiexp *= 1.2;
if ($agiexp > 1000){$agiexp = 1000;}
$nowagiexp = 0;
$chastats[3] ++;

	}
} else {
$zokuhantei = rand(3);
	if ( $monskouka > 0 && $zokuhantei < 1 ) {
	$zokusei[1] = "火";$zokusei[2] = "水";$zokusei[3] = "魔";$zokusei[4] = "無";
	$zokuatk[1] = $svf - 10;$zokuatk[2] = $svc - 10;$zokuatk[3] = $svm - 10;$zokuatk[4] = 0;
		if ($monskouka != 5 ) {
print "<font color=#$mojiiro2><b>$zokusei[$monskouka]属性攻撃！</b></font><br>";
$dmg2 = $monsattack - int( $ac / 2 ) - $zokuatk[$monskouka] + $lvlpoin;
		} else {
# srand;
$monskouka = int( rand(3)) + 1;
print "<font color=#$mojiiro2><b>$zokusei[$monskouka]属性攻撃！</b></font><br>";
$dmg2 = $monsattack - int( $ac / 2 ) - $zokuatk[$monskouka] + $lvlpoin;
$monskouka = 5;
		}
	} else {
$dmg2 = $monsattack - $ac + $lvlpoin;
	}
	if ( $dmg2 < 1 ) { $dmg2 = 0; }
# srand;
$dmg2 += int(rand($monslvl));

$critritu = rand(20);
if ( $critritu < 1 ) {
 $dmg2 *= 2;
print "<font size=4 color=#$mojiiro2>痛恨の一撃！<br></font>"; 
}

	if ( $dmg2 == 0 ) {
print "<font color=#$mojiiro4>$chaname はヒラリと身をかわした！<br></font>"; 
$nowagiexp += 2;
	if ( $nowagiexp >= $agiexp ) {
print <<"HTM";
<center>
<font size=5><span style={filter:glow(color=orchid,strength=5);position:relative;height:50;width:100%;}>
<font color=white><b>$chaname</b> のAGIが上がった！</font>
</span></font></center>
HTM
$agiexp *= 1.2;
if ($agiexp > 300){$agiexp = 300;}
$nowagiexp = 0;
$chastats[3] ++;
	}
} elsif ( $chaclass == 8 && $counter < 1) {
print "$chaname は素早い動きで、奇麗にカウンターを決めた！<br>";
print "$monsname に<font color=#$mojiiro2><b>$dmg2</b></font> のダメージを与えた！<br>";
$dmg2 * 2;
$monshpnow -= $dmg2;
} elsif ( $chaclass == 8 && $counter < 2) {
print "$chaname は素早い動きで、奇麗にカウンターを決めた！<br>";
print "$monsname に<font color=#$mojiiro2><b>$dmg2</b></font> のダメージを与えた！<br>";
$dmg2 * 2;
$monshpnow -= $dmg2;

} elsif ( $chaclass == 80 && $mitore < 1) {
} else {
$chahpnow -= $dmg2;
print "$chaname は <font color=#$mojiiro2><b>$dmg2</b></font> のダメージを受けた！<br>";
$nowacexp += $dmg2;
	if ( $nowacexp >= $acexp ) {

print <<"HTM";
<center>
<font size=5><span style={filter:glow(color=lightsalmon,strength=5);position:relative;height:50;width:100%;}>
<font color=white><b>$chaname</b> のACが上がった！</font>
</span></font></center>
HTM
$acexp *= 1.5;
if ($acexp > 1000000){$acexp = 1000000;}
$nowacexp = 0;
$chastats[1] ++;
	}
	}
if ( $chahpnow <= 0 && $ribaibu > 0) {
print "</td></tr></table><br><br><font size=5 color=#$mojiiro4><b>$chaname は倒れた・・・・</b></font><br><br>";
$chahpnow = 0;
$kaihuku = int($chastats[9] / 2);
$chahpnow += $kaihuku;
print <<"HTM";
薄れ行く意識の中、まばゆい光が$chanameの身体全体を包んだ！<br>
命の光を浴び、$chanameは起き上がった！<br>
<font color=red>リバイブの効果が切れた。</font><br>
HTM
$ribaibu = -1;


	} elsif ( $chahpnow <= 0 && $chasoubi[7] eq "復活の指輪") {
print "</td></tr></table><br><br><font size=5 color=#$mojiiro4><b>$chaname は倒れた・・・・</b></font><br><br>";
$chahpnow = 0;
$kaihuku = int($chastats[9] / 2);
$chahpnow += $kaihuku;
print <<"HTM";
薄れ行く意識の中、復活の指輪が激しく輝きだした！<br>
命の光を浴び、$chanameは起き上がった！<br>
復活の指輪は音もなく崩れ去った。<br>
HTM
$chasoubi[7] = "";

	} elsif ( $chahpnow <= 0 && $chasoubi[7] eq "息吹の指輪") {
print "</td></tr></table><br><br><font size=5 color=#$mojiiro4><b>$chaname は倒れた・・・・</b></font><br><br>";
$chahpnow = 0;
$chahpnow = $chahp;
$chahpnow --;
print <<"HTM";
薄れ行く意識の中、息吹の指輪が激しく輝きだした！<br>
命の光を浴び、$chanameは起き上がった！<br>
息吹の指輪は音もなく崩れ去った。<br>
HTM
$chasoubi[7] = "";

	} elsif ( $chahpnow <= 0 && $chasoubi[7] eq "命の指輪") {
print "</td></tr></table><br><br><font size=5 color=#$mojiiro4><b>$chaname は倒れた・・・・</b></font><br><br>";
$chahpnow = 0;
$chahpnow = $chastats[9];
$chahpnow --;
$champ = $chastats[16];
print <<"HTM";
薄れ行く意識の中、命の指輪が激しく輝きだした！<br>
命の光を浴び、$chanameは起き上がった！<br>
命の指輪は音もなく崩れ去った。<br>
TPが全回復した！<br>
HTM
$chasoubi[7] = "";

} else {
&deathchk;
}
$number = 2;
&pethatudou;

}

print <<"HTM";
</font></td></tr></table><br><br>
HTM
$battleturn ++;
}

&hpcheck;

#　戦闘終了後の処理
sub hpcheck {
if ( $chahpnow <= 0 ) { 
#　キャラ死亡処理
$chastats[12] += 1;
print "</td></tr></table><br><br><font size=5 color=#$mojiiro4><b>$chaname は戦闘に負けた・・・・</b></font><br><br>";

if ( $chasoubi[7] eq "ペットカバーリング" and $petcode[0] ne "" || $petcode[1] ne "" || $petcode[2] ne "" ) {
print "ペットカバーリングの効果でペットが逃げなかった。<br><br>";

} elsif ( $petcode[0] ne "" || $petcode[1] ne "" || $petcode[2] ne "" ) {
$petcode[0] = $petcode[1] = $petcode[2] = $petname[0] = $petname[1] = $petname[2] = "";
$petnowexp[0] = $petnowexp[1] = $petnowexp[2] = 0;
$petexp[0] = $petexp[1] = $petexp[2] = 10;
$petlv[0] = $petlv[1] = $petlv[2] = $petkouka[0] = $petkouka[1] = $petkouka[2] = $petkouka2[0] = $petkouka2[1] = $petkouka2[2] = $peteff[0] = $peteff[1] = $peteff[2] = $petritu[0] = $petritu[1] = $petritu[2] = $petpic[0] = $petpic[1] = $petpic[2] = "";
print "ペットが逃げていってしまった・・・・<br><br>";
	}

if ( $chahpnow <= 0 && $chasoubi[7] eq "ゴールドカバーリング") {
print "ゴールドカバーリングが敵から所持金を守った。<br><br>";
} else {
$chagold = int( $chagold / 2 );
print "所持金が半分になってしまった・・・・<br><br>";
}

$chahp = $chastats[9];
$chaplace = 0;
$kougeki = 0;
$mamori = 0;
if ( $master[$chaclass] == 1) {
$jobexpnow[$chaclass] = $jobexp[$chaclass];
}
print <<"HTM";

<A NAME="exit"></a>

強制的にスタート地点に戻されます。</font>
<form method="post" action="./$zonecgi">
<input type=hidden value="0" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value=" スタートの街に戻る " onClick="this.disabled=true; this.value=' スタートの街に戻る '; this.form.submit();"></form></td></tr></table>
HTM


} elsif ( $monshpnow <= 0 ) {
print <<"HTM";
<A NAME="exit"></a>
HTM
print "</td></tr></table><br><br><font size=5 color=#$mojiiro3><b>$chaname</b> は戦闘に勝利した！！</font><br><br>";
# srand;
$bpo = "1";
$chastats[10] += 1;

	if ( $chastats[10] == 1000 || $chastats[10] == 2000 || $chastats[10] == 3000 || $chastats[10] == 4000 || $chastats[10] == 5000 || $chastats[10] == 6000 || $chastats[10] == 7000 || $chastats[10] == 8000 || $chastats[10] == 9000 || $chastats[10] == 10000 || $chastats[10] == 11000 || $chastats[10] == 12000 || $chastats[10] == 13000 || $chastats[10] == 14000 || $chastats[10] == 15000 || $chastats[10] == 16000 || $chastats[10] == 17000 || $chastats[10] == 18000 || $chastats[10] == 19000 || $chastats[10] == 20000 || $chastats[10] == 21000 || $chastats[10] == 22000 || $chastats[10] == 23000 || $chastats[10] == 24000 || $chastats[10] == 25000 || $chastats[10] == 26000 || $chastats[10] == 27000 || $chastats[10] == 28000 || $chastats[10] == 29000 || $chastats[10] == 30000 || $chastats[10] == 31000 || $chastats[10] == 32000 || $chastats[10] == 33000 || $chastats[10] == 34000 || $chastats[10] == 35000 || $chastats[10] == 36000 || $chastats[10] == 37000 || $chastats[10] == 38000 || $chastats[10] == 39000 || $chastats[10] == 40000 || $chastats[10] == 41000 || $chastats[10] == 42000 || $chastats[10] == 43000 || $chastats[10] == 44000 || $chastats[10] == 45000 || $chastats[10] == 46000 || $chastats[10] == 47000 || $chastats[10] == 48000 || $chastats[10] == 49000 || $chastats[10] == 50000 || $chastats[10] == 51000 || $chastats[10] == 52000 || $chastats[10] == 53000 || $chastats[10] == 54000 || $chastats[10] == 55000 || $chastats[10] == 56000 || $chastats[10] == 57000 || $chastats[10] == 58000 || $chastats[10] == 59000 || $chastats[10] == 60000 || $chastats[10] == 61000 || $chastats[10] == 62000 || $chastats[10] == 63000 || $chastats[10] == 64000 ) {
$chaage ++;
print <<"HTM";
<b>$chaname</b> は、<b>$chaage歳</b>になった。（<font color=green><b>TP</b></font>+<b>5</b>）</b><br><br>
HTM
$chastats[16] += 5;
}

$hukuget = $chalvl + $chastats[2] + $chastats[1] + $chastats[3] + $chastats[4] + $chastats[9];
$hukuget *= 3;
if ( $chasoubi[7] eq "ラックリング") {int($hukuget1 / 2);}
$hukuget1 = rand ($hukuget);
$hukuget2 = $monshp / 2;

$chastats[15] += $monsexp;
$getgold = int( $monsgold + rand($monslvl) );
$chastats[11] += $getgold;
$morai += 0.05;

if ( $chasoubi[7] eq "チャクラリング") {
$kaihuku = int($chastats[9] / 10);
print <<"HTM";
<font size=-1>チャクラリングの癒しの効果で、HPが<font size=4 color=#$mojiiro3><b>$kaihuku</b></font>回復した。</font><br>
HTM
$chahpnow += $kaihuku;
	if ( $chahpnow > $chastats[9] ) {$chahpnow = $chastats[9];}

	} elsif ( $chasoubi[7] eq "ハイチャクラリング") {
$kaihuku = int($chastats[9] / 5);
print <<"HTM";
<font size=-1>ハイチャクラリングの癒しの効果で、HPが<font size=4 color=#$mojiiro3><b>$kaihuku</b></font>回復した。</font><br>
HTM
$chahpnow += $kaihuku;
	if ( $chahpnow > $chastats[9] ) {$chahpnow = $chastats[9];}


	}
if ( $chasoubi[7] eq "リッチリング") {
$getgold = int($getgold * 1.5);
print <<"HTM";
<font size=-1>リッチリングの効果で、<b>Gold</b>が<b>1.5</b>倍になった！</font><br>
HTM
	}
if ( $chasoubi[7] eq "マーメイドリング") {
$monsexp = int($monsexp * 1.3);
print <<"HTM";
<font size=-1>マーメイドリングの効果で、<b>EXP</b>が<b>1.3</b>倍になった！</font><br>
HTM
	}
$monsexp = int( $monsexp * $expmode);
$chaexp += $monsexp;

if($petcode[0] ne ""){
$petnowexp[0] += $monsexp;
}
if($petcode[1] ne ""){
$petnowexp[1] += $monsexp;
}
if($petcode[2] ne ""){
$petnowexp[2] += $monsexp;
}
$tugipet0 = $petexp[0] - $petnowexp[0];
$tugipet1 = $petexp[1] - $petnowexp[1];
$tugipet2 = $petexp[2] - $petnowexp[2];
if($tugipet0 < 0){$tugipet0 = "<font color=red><FONT FACE=Times New Roman>LV UP!!</font></font>"};
if($tugipet1 < 0){$tugipet1 = "<font color=red><FONT FACE=Times New Roman>LV UP!!</font></font>"};
if($tugipet2 < 0){$tugipet2 = "<font color=red><FONT FACE=Times New Roman>LV UP!!</font></font>"};

$tugilvl = $chanextlvl - $chaexp;
	if($tugilvl < 0){$tugilvl = "<font color=red><FONT FACE=Times New Roman>LV UP!!</font></font>";}
$getgold = int($getgold * $goldmode);
$chagold += $getgold;
print "<font color=#$mojiiro4><FONT FACE=Times New Roman><b><font size=4>$getgold</font></font> </font><FONT FACE=Times New Roman>G</font></b> を手に入れた！<br>";
print "<font color=#$mojiiro3><FONT FACE=Times New Roman><b><font size=4>$monsexp</font></font> </font><FONT FACE=Times New Roman>EXP</font></b>を獲得！<br><br>";
print "<font color=darkblue><b><FONT FACE=Times New Roman>Next Level</b></font><br><table border=1><TBODY><TR><TD>$chaname</TD><TD> <b><FONT FACE=Times New Roman>$tugilvl</td></tr></b>";

if($petcode[0] ne ""){print "<td>$petname[0]  <b></td><td><b><FONT FACE=Times New Roman>$tugipet0</font></b></td></tr>";}
if($petcode[1] ne ""){print "<td>$petname[1]  <b></td><td><b><FONT FACE=Times New Roman>$tugipet1</font></b></td></tr>";}
if($petcode[2] ne ""){print "<td>$petname[2]  <b></td><td><b><FONT FACE=Times New Roman>$tugipet2</font></b></td>";}
print "</tr></table><br>";
	if ( $chagold > 1000000000 ) { $chagold = 999999999;}

		if ( $hukuget1 < $hukuget2 ) {
print "<font color=green><b>$monsname</font> から</b> <font color=brown><b>福引券</b></font>を手に入れた！<br><br>";
$hukubiki ++;
}

	if ( $chastats[10] == 120 ) {
if ( $flag20 eq "" ) { $flag20 = 20; }
print "<font color=red><b>特技「ヒーリング」を習得した！</b></font><br><br>";
}

	if ( $chastats[10] == 300 ) {
if ( $flag19 eq "" ) { $flag19 = 19; }
print "<font color=red><b>特技「スキップ」を習得した！</b></font><br><br>";
}

	if ( $chastats[10] == 700 ) {
if ( $flag18 eq "" ) { $flag18 = 18; }
print "<font color=red><b>特技「テレポート」を習得した！</b></font><br><br>";
}

	if ( $chastats[10] == 1250 ) {
if ( $flag17 eq "" ) { $flag17 = 17; }
print "<font color=red><b>特技「ハイヒーリング」を習得した！</b></font><br><br>";
}

	if ( $chastats[10] == 1800 ) {
if ( $flag16 eq "" ) { $flag16 = 16; }
print "<font color=red><b>特技「シールドアップ」を習得した！</b></font><br><br>";
}

	if ( $chastats[10] == 2600 ) {
if ( $flag15 eq "" ) { $flag15 = 15; }
print "<font color=red><b>特技「パワーアップ」を習得した！</b></font><br><br>";
}

if ( $master[$chaclass] == 1) {
$jobexpnow[$chaclass] = $jobexp[$chaclass];
} elsif ( $jobexpnow[$chaclass] >= $jobexp[$chaclass] ){
$master[$chaclass] = 1;
print "<font size=4 color=darkblue><b>$job[$chaclass]の極意を習得した！</b></font><br><br>";
print "<font size=2 color=darkblue><b><font color=green>TPが2上がった！</font></b></font><br><br>";
$jobexpnow[$chaclass] = $jobexp[$chaclass];
$masterjob ++;
$chastats[16] += 2;
}

		if ( $champ <= 0) {
$hpdmg = int($chahp / 8);
$chahpnow -= $hpdmg;
print <<"HTM";
<font size=3><font color=red><b>疲労のせいでHPが $hpdmg 減少した！<br></b></font></font>
<br><br>
HTM
}

$tp --;
if($tp == 0){
$champ -= 1;
$tp = 3;
}
	if ( $champ <= 0 ) { $champ = 0; }

if ( $petnowexp[0] >= $petexp[0] ){
$petlv[0] ++;
print "<font size=5 color=#$mojiiro4><b>$petname[0]</b> のレベルが $petlv[0] に上がった！</font><br><br>";
print "効果値(EF) + <b>1</b>　（<b><font color=palevioletred>$petkouka2[0]</font>　⇒　";
$petkouka2[0] ++;
print "<font color=green>$petkouka2[0]</font></b>）<br>";
$petkaku = int(rand(3)) + 1;
print "参加値(PP) + <b>$petkaku</b>　（<b><font color=palevioletred>$petritu[0]</font>　⇒　";
$petritu[0] += $petkaku;
print "<font color=green>$petritu[0]</font></b>）<br><br>";
$petnowexp[0] = 0;
$exprand = rand(100);
if ( $exprand < 60 ) {
$petexp[0] = int($petexp[0] * 1.2) + int(rand(3));
	} else {$petexp[0] = int($petexp[0] * 1.3) + int(rand(3));}
if($petexp[0] > 50000){$petexp = 50000;}

$omake = int(rand(100));
if( $omake < 10 ) {
$omake2 = int(rand(2));
if ( $omake2 == 0 ){
print "$petname[0] は $chaname の戦いぶりに圧倒されたようだ。<br>";
print "$petname[0] は $chaname の<b>HP</b>を全快してくれた！<br>";
$chahpnow = $chastats[9];
	} elsif ( $omake2 == 1 ){
print "$petname[0] は $chaname の戦いぶりに感動したようだ。<br>";
print "$petname[0] は $chaname の<b>TP</b>を全快してくれた！<br>";
$champ = $chastats[16];
	} elsif ( $omake2 == 2 ){
print "$petname[0] は $chaname の見事な戦いぶりに感服したようだ。<br>";
print "$petname[0] は $chaname の<b>HP,TP</b>を全快してくれた！<br>";
$chahpnow = $chastats[9];
$champ = $chastats[16];
		}
	}
}

if ( $petnowexp[1] >= $petexp[1] ){
$petlv[1] ++;
print "<font size=5 color=#$mojiiro4><b>$petname[1]</b> のレベルが $petlv[1] に上がった！</font><br><br>";
print "効果値(EF) + <b>1</b>　（<b><font color=palevioletred>$petkouka2[1]</font>　⇒　";
$petkouka2[1] ++;
print "<font color=green>$petkouka2[1]</font></b>）<br>";
$petkaku = int(rand(3)) + 1;
print "参加値(PP) + <b>$petkaku</b>　（<b><font color=palevioletred>$petritu[1]</font>　⇒　";
$petritu[1] += $petkaku;
print "<font color=green>$petritu[1]</font></b>）<br><br>";
$petnowexp[1] = 0;
$exprand = rand(100);
if ( $exprand < 60 ) {
$petexp[1] = int($petexp[1] * 1.2) + int(rand(3));
	} else {$petexp[1] = int($petexp[1] * 1.3) + int(rand(3));}
if($petexp[1] > 50000){$petexp = 50000;}

$omake = int(rand(100));
if( $omake < 10 ) {
$omake2 = int(rand(2));
if ( $omake2 == 0 ){
print "$petname[1] は $chaname の戦いぶりに圧倒されたようだ。<br>";
print "$petname[1] は $chaname の<b>HP</b>を全快してくれた！<br>";
$chahpnow = $chastats[9];
	} elsif ( $omake2 == 1 ){
print "$petname[1] は $chaname の戦いぶりに感動したようだ。<br>";
print "$petname[1] は $chaname の<b>TP</b>を全快してくれた！<br>";
$champ = $chastats[16];
	} elsif ( $omake2 == 2 ){
print "$petname[1] は $chaname の見事な戦いぶりに感服したようだ。<br>";
print "$petname[1] は $chaname の<b>HP,TP</b>を全快してくれた！<br>";
$chahpnow = $chastats[9];
$champ = $chastats[16];
		}
	}
}

if ( $petnowexp[2] >= $petexp[2] ){
$petlv[2] ++;
print "<font size=5 color=#$mojiiro4><b>$petname[2]</b> のレベルが $petlv[2] に上がった！</font><br><br>";
print "効果値(EF) + <b>1</b>　（<b><font color=palevioletred>$petkouka2[2]</font>　⇒　";
$petkouka2[2] ++;
print "<font color=green>$petkouka2[2]</font></b>）<br>";
$petkaku = int(rand(3)) + 1;
print "参加値(PP) + <b>$petkaku</b>　（<b><font color=palevioletred>$petritu[2]</font>　⇒　";
$petritu[2] += $petkaku;
print "<font color=green>$petritu[2]</font></b>）<br><br>";
$petnowexp[2] = 0;
$exprand = rand(100);
if ( $exprand < 60 ) {
$petexp[2] = int($petexp[2] * 1.2) + int(rand(3));
	} else {$petexp[2] = int($petexp[2] * 1.3) + int(rand(3));}
if($petexp[2] > 50000){$petexp = 50000;}

$omake = int(rand(100));
if( $omake < 10 ) {
$omake2 = int(rand(2));
if ( $omake2 == 0 ){
print "$petname[2] は $chaname の戦いぶりに圧倒したようだ。<br>";
print "$petname[2] は $chaname の<b>HP</b>を全快してくれた！<br>";
$chahpnow = $chastats[9];
	} elsif ( $omake2 == 1 ){
print "$petname[2] は $chaname の戦いぶりに感動したようだ。<br>";
print "$petname[2] は $chaname の<b>TP</b>を全快してくれた！<br>";
$champ = $chastats[16];
	} elsif ( $omake2 == 2 ){
print "$petname[2] は $chaname の見事な戦いぶりに感服したようだ。<br>";
print "$petname[2] は $chaname の<b>HP,TP</b>を全快してくれた！<br>";
$chahpnow = $chastats[9];
$champ = $chastats[16];
		}
	}
}

	if ( $chaexp >= $chanextlvl && $chalvl != 10000000 ) {
$chaexp = 0;$chalvl ++;$chastats[0] ++;

open(EXP,"./exp$bousikts");
$expnum = 0;
		while ( $exptugi = <EXP> ) {
			if ($expnum == $chalvl ) {
			chop($exptugi);$chanextlvl = $exptugi;last;
			}
$expnum ++;
		}
close(EXP);

print "<font size=5 color=#$mojiiro4><b>$chaname</b> はレベルが上がった！</font><br><br>";

	if ( $chalvl == 10 || $chalvl == 20 || $chalvl == 30 || $chalvl == 40 || $chalvl == 50 || $chalvl == 60 || $chalvl == 70 || $chalvl == 80 || $chalvl == 90 || $chalvl == 100 || $chalvl == 110 || $chalvl == 120 || $chalvl == 130 || $chalvl == 140 || $chalvl == 150 || $chalvl == 160 || $chalvl == 170 || $chalvl == 180 || $chalvl == 190 || $chalvl == 200 || $chalvl == 210 || $chalvl == 220 || $chalvl == 230 || $chalvl == 240 || $chalvl == 250 || $chalvl == 260 || $chalvl == 270 || $chalvl == 280 || $chalvl == 290 || $chalvl == 300 || $chalvl == 310 || $chalvl == 320 || $chalvl == 330 || $chalvl == 340 || $chalvl == 350 || $chalvl == 360 || $chalvl == 370 || $chalvl == 380 || $chalvl == 390 || $chalvl == 400 || $chalvl == 410 || $chalvl == 420 || $chalvl == 430 || $chalvl == 440 || $chalvl == 450 || $chalvl == 460 || $chalvl == 470 || $chalvl == 480 || $chalvl == 490 || $chalvl == 500 ) {
print "<font color=green><b>TP</b>が<b>1</b>上がった！</font><br>";
$chastats[16] ++;
}

&levelup;


	}
#　アイテム獲得処理

$randitem = int( rand(3));
	if ( $randitem > 0 ) {
$itembangou = 0;
	} else {

$randitem = int( rand(3));
		if ( $randitem > 0 ) {
$itembangou = 1;
		} else {

$randitem = int( rand(2));
			if ( $randitem == 0 ) {
$itembangou = 2;
			} elsif ( $randitem == 1 ) {
$itembangou = 3;
			} else {
$itembangou = 4;
			}
		}
	}

	if ( $monsitem[$itembangou] ne "" ) {
print "$monsname は「<font size=4 color=#$mojiiro4><b>$monsitem[$itembangou]</b></font>」を持っていた！<br><br>";

open(KAI,"$maindir/item$bousikts");
		while ( $kaitori = <KAI> ) {
			($kainame,$a,$b,$c,$d,$itemkouka,$itemstats) = split(/,/,$kaitori);
			if ( $monsitem[$itembangou] eq $kainame ) {
			last;
			}
		}
close(KAI);
		if ( $itemstats >= 10 ) {
		$bbb = 1;
			while ( $bbb < 9 ) {
				if ( $chaitem[$bbb] eq $monsitem[$itembangou] ) {
			last;
				}
			$bbb ++;
			}

			if ( $bbb >=9 ) {
		$ccc = 1;
				while ( $ccc < 9 ) {
					if ( $chaitem[$ccc] eq "" ) {
			last;
					}
			$ccc ++;
				}
				if( $ccc <= 9 ) {
$chaitem[$ccc] = $monsitem[$itembangou];$chaeff[$ccc] = 1;$chasetumei[$ccc] =$itemkouka;
				} else {
			print "持ち物がいっぱいだったのであきらめた・・・<br>";
				}
			} elsif ( $chaeff[$bbb] < 99 ) { $chaeff[$bbb] ++; 
			} else { print "個数がいっぱいだったのであきらめた・・・<br>";
			}


		} else {
		$ccc = 1;
			while ( $ccc < 9 ) {
				if ( $chaitem[$ccc] eq "" ) {
			last;
				}
			$ccc ++;
			}
			if( $ccc <= 9 ) {
$chaitem[$ccc] = $monsitem[$itembangou];$chaeff[$ccc] = 1;$chasetumei[$ccc] =$itemkouka;
			} else {
			print "持ち物がいっぱいだったのであきらめた・・・<br>";
			}
		}
	}
	if ( $chaclass == 7 && $tokugikouka > 1 ) { $cha -= ($chastats[5] * 9 ); }
	if ( $chaclass == 71 && $tokugikouka > 1 ) { $cha -= 1000; }
	if ( $chaclass == 72 && $tokugikouka > 1 ) { $cha -= ($chastats[5] * 9 ); }
	if ( $chaclass == 82 && $tokugikouka > 1 ) { $cha -= ($chastats[5] * 12 ); }

$turepet = 0;$turepetti = 0;
	while ( $turepet < 3 ) {
		if ( $petcode[$turepet] ne "" ) { $turepetti ++; }
$turepet ++;
	}
#　ペット獲得処理
# srand;
$petgetritu = int( rand(1000) ) - int((($cha - 10 )/2) * $turepetti);
	if ( $petgetritu <= $monscha ) {

open(PET,"$maindir/$foldacha/pet_$in{usrid}$bousi2cha$bousikts");
$ppp = 0;
		while ( $petnakama = <PET> ) {
			chop($petnakama);
			if ( $petnakama eq $monsname ) {
				$ppp ++;last;
			}
		}
close(PET);
open(PET,"$maindir/$foldacha/pet_$in{usrid}$bousi2cha$bousikts");
			$petsousuu = <PET>;
close(PET);

		if ( $ppp == 0 && $petcode[0] ne $monsname && $petcode[1] ne $monsname && $petcode[2] ne $monsname && $petsousuu <= 200) {
open(PET,">>$maindir/$foldacha/pet_$in{usrid}$bousi2cha$bousikts");
			print PET "$monsname\n";
close(PET);
print <<"HTM";
<br><font size=4 color=#$monsname><b>$monsname</font></b> が仲間になりたそうにこちらを見つめている・・・<br><br>
<font color=#$chamoji><b>$chaname</font></b> は <font size=4 color=#$monsname><b>$monsname</font></b> をペット小屋に送った！！<br>
HTM

		}
	}

$chahp = $chahpnow;
$chacount --;
	if( $chasoubi[7] eq "スキップリング" ) { $chacount --;}
if ( $kougekit > 0 ) {$kougekit --;}
if ( $kougekit == 0 ) {
print "<font color=red>パワーアップの効果が切れた。</font><br><br>";
$kougekit --;
$kougeki = 0;
	}

if ( $mamorit > 0 ) {$mamorit --;}
if ( $mamorit == 0 ) {
print "<font color=red>シールドアップの効果が切れた。</font><br><br>";
$mamorit --;
$mamori = 0;
	}

if ( $houou > 0 ) {$houou --;}
if ( $houou == 0 ) {
print "<font color=red>鳳凰の舞の効果が切れた。</font><br><br>";
$houou --;
	}

if ( $ribaibu > 0 ) {$ribaibu --;}
if ( $ribaibu == 0 ) {
print "<font color=red>リバイブの効果が切れてしまった。</font><br><br>";
$ribaibu --;
	}

print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$in{boss}" name="boss">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value=" ゾーンに戻る " onClick="this.disabled=true; this.value=' ゾーンに戻る '; this.form.submit();"></form></td></tr></table>
HTM

} else {
$tp --;
if($tp == 0){
$champ -= 1;
$tp = 3;
}
$chahp = $chahpnow;
$chacount --;
	if( $chasoubi[7] eq "スキップリング" ) { $chacount --;}
$kougeki = 0;
$mamori = 0;
	if ( $champ <= 0 ) { $champ = 0; }


print <<"HTM";
<A NAME="exit"></a>
</td></tr></table><br><br>
<font size=5 color=#$mojiiro4><b>$monsname</b> は逃げ出した・・・・</font><br><br>
<form method="post" action="./$zonecgi">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value=" ゾーンに戻る " onClick="this.disabled=true; this.value=' ゾーンに戻る '; this.form.submit();"></form></td></tr></table>
HTM

}

&charadatawrt;
&hpowari;exit;
}

sub deathchk {
	if ( $chahpnow <= 0 ) { last; }
	if ( $monshpnow <= 0 ) { last; }
}



#　ペットの攻撃処理
sub petdmg {
		if ( $dmg < 1 ) { $dmg = 0; }
# srand;
$dmg += int(rand($petlv[$number]));
		if ( $dmg == 0 ) {
print "<font color=#$mojiiro4>$monsname はヒラリと身をかわした！<br><br></font>"; 
		} else {
$monshpnow -= $dmg;
print "$monsname に <font size=4 color=#$mojiiro2><b>$dmg</b></font> のダメージを与えた！<br><br>";

		}
}

sub pethatudou {
	if ( $petcode[$number] ne "" ) {
		if ( $petkoukaturn[$number] == 1 && $petkouka[$number] >= 9) {
&petadd;
print "<font color=#$chamoji><b>$petname[$number]</font> </b>のアシスト効果が切れた<br><br>";

		} elsif ( $petkoukaturn[$number] <= 0 ) {
# srand;
$petsanka = rand(1000);
			if ( $petsanka < ($petritu[$number] + $cha) ) {
print "<br><font color=#$chamoji><b>$petname[$number]</b></font> のアシスト！<br>";
&petadd;
			}
		} 
$petkoukaturn[$number] --;
	}
&deathchk;

}

sub petadd {
	if ( $petkouka[$number] == 16 ) {
$dmg = $petkouka2[$number] - $monsac + int(rand($petlv[$number]));
&petdmg;

	} elsif ( $petkouka[$number] == 1 ) {
$dmg = $petkouka2[$number] - int($monsac / 2 ) - $monssvf + int(rand($petlv[$number]));
print "<font color=#$mojiiro2><b>火属性ダメージ</b></font><br>";
&petdmg;

	} elsif ( $petkouka[$number] == 2 ) {
$dmg = $petkouka2[$number] - int($monsac / 2 ) - $monssvc + int(rand($petlv[$number]));
print "<font color=#$mojiiro2><b>水属性ダメージ</b></font><br>";
&petdmg;

	} elsif ( $petkouka[$number] == 3 ) {
$dmg = $petkouka2[$number] - int($monsac / 2 ) - $monssvm + int(rand($petlv[$number]));
print "<font color=#$mojiiro2><b>魔属性ダメージ</b></font><br>";
&petdmg;

	} elsif ( $petkouka[$number] == 4 ) {
$dmg = $petkouka2[$number] - int($monsac / 2 ) + int(rand($petlv[$number]));
print "<font color=#$mojiiro2><b>無属性ダメージ</b></font><br>";
&petdmg;

	} elsif ( $petkouka[$number] == 5 ) {
# srand;
$abe = rand (3);
		if ( $abe < 1 ) {
$dmg = $petkouka2[$number] - int($monsac / 2 ) - $monssvf + int(rand($petlv[$number]));
print "<font color=#$mojiiro2><b>火属性ダメージ</b></font><br>";
		} elsif ( $abe < 1 ) {
$dmg = $petkouka2[$number] - int($monsac / 2 ) - $monssvc + int(rand($petlv[$number]));
print "<font color=#$mojiiro2><b>水属性ダメージ</b></font><br>";
		} else {
$dmg = $petkouka2[$number] - int($monsac / 2 ) - $monssvm + int(rand($petlv[$number]));
print "<font color=#$mojiiro2><b>魔属性ダメージ</b></font><br>";
		}
&petdmg;

	} elsif ( $petkouka[$number] == 6 ) {
$dmg = $petkouka2[$number] + int(rand($petlv[$number]));
$dmg2 = int( $dmg / 3 );
$chagold += $dmg2;
print "<b>$monsname</b> から <font color=#$mojiiro4><b>$dmg2</font> G</b> 盗んだ！<br><br>";

	} elsif ( $petkouka[$number] == 7 ) { #########
	} elsif ( $petkouka[$number] == 8 ) {
$dmg = $petkouka2[$number] + int(rand($petlv[$number]));
$chahpnow += $dmg;
		if($chahpnow > $chastats[9] ) {
$chahpnow = $chastats[9];
		}
print "HPが<font color=#$mojiiro2><b> $dmg</font> </b>回復した！<br><br>";

	} elsif ( $petkouka[$number] == 9 ) {
		if($petkoukaturn[$number] <= 0 ) {
$ac += $petkouka2[$number];
$petkoukaturn[$number] = 3;
print "<font color=#$chamoji><b>$chaname</font> </b>の防御力がアップ！<br><br>";
		} elsif ( $petkoukaturn[$number] == 1 ) {
$ac -= $petkouka2[$number];
		}

	} elsif ( $petkouka[$number] == 10 ) {
		if($petkoukaturn[$number] <= 0 ) {
$str += $petkouka2[$number];
$petkoukaturn[$number] = 3;
print "<font color=#$chamoji><b>$chaname</font> </b>の力がアップ！<br><br>";
		} elsif ( $petkoukaturn[$number] == 1 ) {
$str -= $petkouka2[$number];
		}

	} elsif ( $petkouka[$number] == 11 ) {
		if($petkoukaturn[$number] <= 0 ) {
$agi += $petkouka2[$number];
$petkoukaturn[$number] = 3;
print "<font color=#$chamoji><b>$chaname</font> </b>の素早さがアップ！<br><br>";
		} elsif ( $petkoukaturn[$number] == 1 ) {
$agi -= $petkouka2[$number];
		}

	} elsif ( $petkouka[$number] == 12 ) {
		if($petkoukaturn[$number] <= 0 ) {
$int += $petkouka2[$number];
$petkoukaturn[$number] = 3;
print "<font color=#$chamoji><b>$chaname</font> </b>の知性がアップ！<br><br>";
		} elsif ( $petkoukaturn[$number] == 1 ) {
$int -= $petkouka2[$number];
		}

	} elsif ( $petkouka[$number] == 13 ) {
		if($petkoukaturn[$number] <= 0 ) {
$cha += $petkouka2[$number];
$petkoukaturn[$number] = 3;
print "<font color=#$chamoji><b>$chaname</font> </b>の魅力がアップ！<br><br>";
		} elsif ( $petkoukaturn[$number] == 1 ) {
$cha -= $petkouka2[$number];
		}

	} elsif ( $petkouka[$number] == 14 ) {
		if($petkoukaturn[$number] <= 0 ) {
$svf += $petkouka2[$number];$svc += $petkouka2[$number];$svm += $petkouka2[$number];
$petkoukaturn[$number] = 3;
print "<font color=#$chamoji><b>$chaname</font> </b>の耐性がアップ！<br><br>";
		} elsif ( $petkoukaturn[$number] == 1 ) {
$svf -= $petkouka2[$number];$svc -= $petkouka2[$number];$svm -= $petkouka2[$number];
		}

	} elsif ( $petkouka[$number] == 15 ) {
$dhuran = int( rand(35) );

		if ( $dhuran == 0 ) {
print "<b>$petname[$number]</b>は天高くジャンプした！<br>";
print "・・・そのまま帰ってこなかった。<br><br>";


		} elsif ( $dhuran == 1 ) {
$dmg = int( $str / 3 ) + $pow - $monsac;
		if ( $dmg < 1 ) { $dmg = 0; }
# srand;
$dmg += int(rand($chalvl));
$monshpnow -= $dmg;
print "<b>$petname[$number]</b>は天高くジャンプした！<br>";
print "<font size=5 color=#$mojiiro2><b>飛龍落撃衝 ！！</b></font><br><br>";
print "$monsname に <font size=4 color=#$mojiiro2><b>$dmg</b></font> のダメージを与えた！<br><br>";


		} elsif ( $dhuran == 2 ) {
$dmg = int( $str / 3 ) + $pow - $monsac;
		if ( $dmg < 1 ) { $dmg = 0; }
# srand;
$dmg += int(rand($chalvl));
$dmg = int ($dmg / 2);
$chagold += $dmg;
print "<b>$petname[$number]</b>は目にもとまらぬ速さで敵の懐に潜り込んだ！<br>";
print "<b>$petname[$number]</b>「あらよっと！」<br><br>";
print "$monsname から <font size=4 color=#$mojiiro4><b>$dmg</b></font> Gを盗んだ！<br><br>";


		} elsif ( $dhuran == 3 ) {
print "<b>$petname[$number]</b>「俺の秘技に耐えられるかな・・・」<br>";
print "<font size=5 color=#$mojiiro2><b>斬鉄剣 ！！</b></font><br><br>";
print "一瞬で敵を真っ二つにした！<br><br>";
$monshpnow = 0;


		} elsif ( $dhuran == 4 ) {
$dmg = $chastats[0] - $chastats[1];

print "<b>$petname[$number]</b>は間違えて<font color=#$chamoji><b>$chaname</font></b>に攻撃をしてしまった！<br>";
print "<font color=#$chamoji><b>$chaname</font></b>は<font size=4 color=#$mojiiro2><b>$dmg</b></font> のダメージを受けた！<br><br>";
print "<b>$petname[$number]</b>「げ・・・！　すまねぇ！　許せ！」<br><br>";
$chahpnow -= $dmg;

		} elsif ( $dhuran == 5 ) {
$dmg = 100;
$monshpnow -= $dmg;
print "<b>$petname[$number]</b>は武器を投げ捨て、敵に往復ビンタを張り出した！<br><br>";
print "$monsnameに<font size=4 color=#$mojiiro2><b>10</b></font> のダメージを与えた！<br>";
print "$monsnameに<font size=4 color=#$mojiiro2><b>10</b></font> のダメージを与えた！<br>";
print "$monsnameに<font size=4 color=#$mojiiro2><b>10</b></font> のダメージを与えた！<br>";
print "$monsnameに<font size=4 color=#$mojiiro2><b>10</b></font> のダメージを与えた！<br>";
print "$monsnameに<font size=4 color=#$mojiiro2><b>10</b></font> のダメージを与えた！<br>";
print "$monsnameに<font size=4 color=#$mojiiro2><b>10</b></font> のダメージを与えた！<br>";
print "$monsnameに<font size=4 color=#$mojiiro2><b>10</b></font> のダメージを与えた！<br>";
print "$monsnameに<font size=4 color=#$mojiiro2><b>10</b></font> のダメージを与えた！<br>";
print "$monsnameに<font size=4 color=#$mojiiro2><b>10</b></font> のダメージを与えた！<br>";
print "$monsnameに<font size=4 color=#$mojiiro2><b>10</b></font> のダメージを与えた！<br>";


		} elsif ( $dhuran == 6 ) {
$dmg = 100;
$chahpnow += $dmg;

print "<b>$petname[$number]</b>「$chaname ！　これを使え！」<br>";
print "<b>$petname[$number]</b>は$chaname に<font size=4 color=#$mojiiro4><b>ポーション</b></font> を投げた！<br><br>";
print "<font color=#$chamoji><b>$chaname</font></b>のHPが<font size=4 color=#$mojiiro3><b>$dmg</b></font>回復した！<br><br>";
				if ( $chahpnow > $chastats[9] ) {
$chahpnow = $chastats[9];
				}

		} elsif ( $dhuran == 7 ) {
$dmg = 300;
$chahpnow += $dmg;

print "<b>$petname[$number]</b>「$chaname ！　これを使え！」<br>";
print "<b>$petname[$number]</b>は$chaname に<font size=4 color=#$mojiiro4><b>ミドルポーション</b></font> を投げた！<br><br>";
print "<font color=#$chamoji><b>$chaname</font></b>のHPが<font size=4 color=#$mojiiro3><b>$dmg</b></font>回復した！<br><br>";
				if ( $chahpnow > $chastats[9] ) {
$chahpnow = $chastats[9];
				}


		} elsif ( $dhuran == 8 ) {
$dmg = 10 + int(rand($chalvl));
$chahpnow -= $dmg;
$monshpnow -= $dmg;
print "<b>$petname[$number]</b>はどこからか爆弾を拾ってきた・・・<br>";
print "<b>$petname[$number]</b>「$chaname ！　伏せ・・・」<br>";
print "<b>$chaname</b>「・・・え？」<br><br>";
print "無残にも爆弾は爆発を巻き起こした！<br><br>";

print "$chanameは<font size=4 color=#$mojiiro2><b>$dmg</b></font> のダメージを受けた！<br>";
print "$monsnameは<font size=4 color=#$mojiiro2><b>$dmg</b></font> のダメージを受けた！<br>";
print "<b>$petname[$number]</b>は<font size=4 color=#$mojiiro2><b>$dmg</b></font> のダメージを受けた！<br><br>";


		} elsif ( $dhuran == 9 ) {
print "<b>$petname[$number]</b>は$chanameの影に隠れている。<br><br>";


		} elsif ( $dhuran == 10 ) {
print "<b>$petname[$number]</b>はボーっとしている。<br><br>";


		} elsif ( $dhuran == 11 ) {
$dmg = int( $str / 3 ) + $pow - $monsac;
		if ( $dmg < 1 ) { $dmg = 0; }
# srand;
$dmg += int(rand($chalvl));
$dmg = int($dmg / 1.5);
$dmg * 4;
$monshpnow -= $dmg;

print "<b>$petname[$number]</b>は武器を大きく振り上げ、$monsname に叩きつけた！<br>";
print "<b>$petname[$number]</b>「うおぉ～ッ！」<br>";
print "$monsname に<font size=4 color=#$mojiiro2><b>$dmg</b></font>のダメージを与えた！<br><br>";


		} elsif ( $dhuran == 12 ) {
$dmg = int( $str / 3 ) + $pow - $monsac;
		if ( $dmg < 1 ) { $dmg = 0; }
# srand;
$dmg += int(rand($chalvl));
$dmg * 5;
$monshpnow -= $dmg;

$dmg1 = int( $str / 3 ) + $pow - $monsac;
		if ( $dmg1 < 1 ) { $dmg1 = 0; }
# srand;
$dmg1 += int(rand($chalvl));
$dmg1 * 5;
$monshpnow -= $dmg1;
print "デュランは武器を振りかざし、呪文を唱え始めた！<br>";
print "たちまち暗雲が辺りを包み込む！<br>";
print "<font size=5 color=#$mojiiro2><b>双龍波 ！！</b></font><br>";
print "２匹の巨大な龍が$monsname に襲い掛かる！<br><br>";
print "紫炎龍は鋭い爪で$monsname を引っ掻いた！<br>";
print "$monsname に<font size=4 color=#$mojiiro2><b>$dmg</b></font>のダメージを与えた！<br><br>";
print "青海龍は鋭い牙で$monsname に喰らいついた！<br>";
print "$monsname に<font size=4 color=#$mojiiro2><b>$dmg1</b></font>のダメージを与えた！<br><br>";

		} else  {
$dmg = int( $str / 3 ) + $pow - $monsac;
		if ( $dmg < 1 ) { $dmg = 0; }
# srand;
$dmg += int(rand($chalvl));
$dmg = int($dmg / 1.5);
$monshpnow -= $dmg;
print "$monsname に<font size=4 color=#$mojiiro2><b>$dmg</b></font>のダメージを与えた！<br><br>";

		}

	} else {
	&fuseisyori;exit;
	}
}



sub tokunou {
if ( $chasoubi[7] eq "スライムリング") {
$kaihuku = int(rand(4)) + 1;
print <<"HTM";
<font size=-1>スライムリングの癒しの効果で、<b>HP</b>が<font size=4 color=#$mojiiro3><b>$kaihuku</b></font>回復した。</font><br>
HTM
$chahpnow += $kaihuku;
	if ( $chahpnow > $chastats[9] ) {$chahpnow = $chastats[9];}
	}

if ( $chasoubi[1] eq "癒しの杖") {
$kaihuku = int(rand(30)) + 5;
print <<"HTM";
<font size=-1>癒しの杖の癒しの効果で、<b>HP</b>が<font size=4 color=#$mojiiro3><b>$kaihuku</b></font>回復した。</font><br>
HTM
$chahpnow += $kaihuku;
	if ( $chahpnow > $chastats[9] ) {$chahpnow = $chastats[9];}
	}

if ( $chasoubi[7] eq "輝く指輪") {
$kaihuku = int(rand(7)) + 13;
print <<"HTM";
<font size=-1>輝く指輪の癒しの効果で、<b>HP</b>が<font size=4 color=#$mojiiro3><b>$kaihuku</b></font>回復した。</font><br>
HTM
$chahpnow += $kaihuku;
	if ( $chahpnow > $chastats[9] ) {$chahpnow = $chastats[9];}
	}

if ( $chasoubi[4] eq "ミノローブ") {
$kaihuku = int(rand(4)) + 8;
print <<"HTM";
<font size=-1>ミノローブの癒しの効果で、<b>HP</b>が<font size=4 color=#$mojiiro3><b>$kaihuku</b></font>回復した。</font><br>
HTM
$chahpnow += $kaihuku;
	if ( $chahpnow > $chastats[9] ) {$chahpnow = $chastats[9];}
	}

if ( $chasoubi[4] eq "スライムローブ") {
$kaihuku = int(rand(5)) + 6;
print <<"HTM";
<font size=-1>スライムローブの癒しの効果で、<b>HP</b>が<font size=4 color=#$mojiiro3><b>$kaihuku</b></font>回復した。</font><br>
HTM
$chahpnow += $kaihuku;
	if ( $chahpnow > $chastats[9] ) {$chahpnow = $chastats[9];}
	}

if ( $chasoubi[4] eq "ライトプレートチェスト") {
$kaihuku = int(rand(9)) + 2;
print <<"HTM";
<font size=-1>ライトプレートチェストから暖かい光が溢れる！　<b>HP</b>が<font size=4 color=#$mojiiro3><b>$kaihuku</b></font>回復した。</font><br>
HTM
$chahpnow += $kaihuku;
	if ( $chahpnow > $chastats[9] ) {$chahpnow = $chastats[9];}
	}

if ( $chasoubi[4] eq "プリンスクロウズ") {
$kaihuku = int(rand(15)) + 12;
print <<"HTM";
<font size=-1>プリンスクロウズから暖かい光が溢れる！　<b>HP</b>が<font size=4 color=#$mojiiro3><b>$kaihuku</b></font>回復した。</font><br>
HTM
$chahpnow += $kaihuku;
	if ( $chahpnow > $chastats[9] ) {$chahpnow = $chastats[9];}
	}

if ( $chasoubi[3] eq "フラワーヘルム") {
$kaihuku = int(rand(7)) + 2;
print <<"HTM";
<font size=-1>フラワーヘルムの癒しの効果で、<b>HP</b>が<font size=4 color=#$mojiiro3><b>$kaihuku</b></font>回復した。</font><br>
HTM
$chahpnow += $kaihuku;
	if ( $chahpnow > $chastats[9] ) {$chahpnow = $chastats[9];}
	}

if ( $chasoubi[1] eq "大刀") {
$kaihuku = int(rand(3));
if ( $kaihuku == 1 ) {
$tuika = int($str / 2);
print <<"HTM";
<font size=-1>大刀の刃が敵の急所を斬った！　さらに<font size=4 color=#$mojiiro2><b>$tuika</b></font>のダメージを与えた！</font><br>
HTM
$monshpnow -= $tuika;
}
	}

if ( $chasoubi[2] eq "フェニックスソード") {
$kaihuku = int(rand(2));
if ( $kaihuku == 1 ) {
$tuika = int($str / 2);
print <<"HTM";
<font size=-1>フェニックスソードで素早く斬りつけた！　さらに<font size=4 color=#$mojiiro2><b>$tuika</b></font>のダメージを与えた！</font><br>
HTM
$monshpnow -= $tuika;
}
	}


if ( $chasoubi[1] eq "ソウルイーター") {
$intup = int($dmg / 5) + 1;

print <<"HTM";
<font size=-1>ソウルイーターは敵のHPを<font size=4 color=#$mojiiro2><b>$intup</b></font>吸い取った！　<b>HP</b>が<font size=4 color=#$mojiiro3><b>$intup</b></font>回復した。</font><br>
HTM
$chahpnow += $intup;
$monshpnow -= $intup;
	if ( $chahpnow > $chastats[9] ) {$chahpnow = $chastats[9];}
	}

if ( $chasoubi[1] eq "スパナ") {
$kaihuku = int(rand(2));
if ( $kaihuku == 1 ) {
$tuika = int($str / 4);
print <<"HTM";
<font size=-1>ついでに、もう１発スパナで殴っておいた。　さらに<font size=4 color=#$mojiiro2><b>$tuika</b></font>のダメージを与えた！</font><br>
HTM
$monshpnow -= $tuika;
}
	}

if ( $chasoubi[6] eq "デスタークグローブ") {
$kaihuku = int(rand(3));
if ( $kaihuku == 1 ) {
$tuika = int($str / 2);
print <<"HTM";
<font size=-1>デスタークグローブの効果で、さらに<font size=4 color=#$mojiiro2><b>$tuika</b></font>のダメージを与えた！</font><br>
HTM
$monshpnow -= $tuika;
}
	}

if ( $chasoubi[1] eq "メガソード") {
$kaihuku = int(rand(3));
if ( $kaihuku == 1 ) {
$tuika = int($str / 2);
print <<"HTM";
<font size=-1>メガソードの刃が敵の急所を斬った！　さらに<font size=4 color=#$mojiiro2><b>$tuika</b></font>のダメージを与えた！</font><br>
HTM
$monshpnow -= $tuika;
}
	}

if ( $chasoubi[7] eq "メガリング") {
$kaihuku = int(rand(3));
if ( $kaihuku == 1 ) {
$tuika = int($str / 2);
print <<"HTM";
<font size=-1>メガリングは黒い波動を放った！　さらに<font size=4 color=#$mojiiro2><b>$tuika</b></font>のダメージを与えた！</font><br>
HTM
$monshpnow -= $tuika;
}
	}

if ( $chasoubi[2] eq "レフトゴブリンクロウ") {
$kaihuku = int(rand(3));
if ( $kaihuku == 1 ) {
$tuika = int($str / 3);
print <<"HTM";
<font size=-1>レフトゴブリンクロウで素早く追加攻撃！　さらに<font size=4 color=#$mojiiro2><b>$tuika</b></font>のダメージを与えた！</font><br>
HTM
$monshpnow -= $tuika;
}
	}

if ( $chasoubi[5] eq "ブラッグレッグス") {
$kaihuku = int(rand(4));
if ( $kaihuku == 1 ) {
$intup = int($dmg / 4) + 1;
$chahpnow += $intup;
$monshpnow -= $intup;
print <<"HTM";
<font size=-1>ブラッグレッグスは敵のHPを<font size=4 color=#$mojiiro2><b>$intup</b></font>吸い取った！　<b>HP</b>が<font size=4 color=#$mojiiro3><b>$intup</b></font>回復した。</font><br>
HTM
$chahpnow += $kaihuku;
	if ( $chahpnow > $chastats[9] ) {$chahpnow = $chastats[9];}
}
	}

if ( $chasoubi[1] eq "ネクロマンサー") {
$intup = int($dmg / 5) + 1;
$chahpnow += $intup;
$monshpnow -= $intup;
print <<"HTM";
<font size=-1>ネクロマンサーは敵のHPを<font size=4 color=#$mojiiro2><b>$intup</b></font>吸い取った！　<b>HP</b>が<font size=4 color=#$mojiiro3><b>$intup</b></font>回復した。</font><br>
HTM
$chahpnow += $kaihuku;
	if ( $chahpnow > $chastats[9] ) {$chahpnow = $chastats[9];}
	}


if ( $chasoubi[3] eq "ゴブリンスキンフード") {
$kaihuku = int(rand(4));
if ( $kaihuku == 1 ) {
$intup = int(rand(3)) + 1;
$str += $intup;
print <<"HTM";
<font size=-1>ゴブリンスキンフードの効果で、一時的に<b>STR</b>が<font size=4 color=#$mojiiro1><b>$intup</b></font>上がった！</font><br>
HTM
}
	}

if ( $chasoubi[6] eq "源氏の腕鎧") {
$kaihuku = int(rand(5));
if ( $kaihuku == 1 ) {
print <<"HTM";
<font size=-1>源氏の腕鎧の効果で追加攻撃！</font><br>
HTM
&jobatk;
}
	}

if ( $chasoubi[1] eq "サイバーソード") {
$kaihuku = int(rand(4));
if ( $kaihuku == 1 ) {
print <<"HTM";
<font size=-1>サイバーソードで素早く追加攻撃！</font><br>
HTM
&jobatk;
}
	}

if ( $chasoubi[1] eq "即死の針") {
$kaihuku = int(rand(10));
if ( $kaihuku == 1 ) {
print <<"HTM";
<font size=-1>即死の針で敵の急所をついた！</font><br>
HTM
$monshpnow = 0;
}
	}

if ( $chasoubi[4] eq "忍脚装束") {
$kaihuku = int(rand(5));
if ( $kaihuku == 1 ) {
print <<"HTM";
<font size=-1>忍脚装束の効果で追加攻撃！</font><br>
HTM
&jobatk;
}
	}

if ( $chasoubi[8] eq "デザートネックレス") {
$kaihuku = int(rand(3));
if ( $kaihuku == 1 ) {
$intup = int(rand(5)) + 5;
$svf += $intup;
print <<"HTM";
<font size=-1>デザートネックレスの効果で、一時的に<b>SVF</b>が<font size=4 color=#$mojiiro1><b>$intup</b></font>上がった！</font><br>
HTM
}
	}

if ( $chasoubi[3] eq "フェニックスフード") {
$kaihuku = int(rand(3));
if ( $kaihuku == 1 ) {
$intup = int(rand(25)) + 15;
$svf += $intup;
print <<"HTM";
<font size=-1>フェニックスフードの効果で、一時的に<b>SVF</b>が<font size=4 color=#$mojiiro1><b>$intup</b></font>上がった！</font><br>
HTM
}
	}

if ( $chasoubi[5] eq "リングメイルレッグス") {
$kaihuku = int(rand(3));
if ( $kaihuku == 1 ) {
$intup = int(rand(10)) + 7;
$svc += $intup;
print <<"HTM";
<font size=-1>リングメイルレッグスの効果で、一時的に<b>SVC</b>が<font size=4 color=#$mojiiro1><b>$intup</b></font>上がった！</font><br>
HTM
}
	}

if ( $chasoubi[2] eq "紅葉樹の盾") {
$kaihuku = int(rand(3));
if ( $kaihuku == 1 ) {
$intup = int(rand(5)) + 5;
$ac += $intup;
print <<"HTM";
<font size=-1>紅葉樹の盾の効果で、一時的に<b>AC</b>が<font size=4 color=#$mojiiro1><b>$intup</b></font>上がった！</font><br>
HTM
}
	}

if ( $chasoubi[2] eq "スクリームロッド") {
$kaihuku = int(rand(3));
if ( $kaihuku == 1 ) {
$intup = int(rand(10)) + 7;
$svf += $intup;
print <<"HTM";
<font size=-1>スクリームロッドの効果で、一時的に<b>SVF</b>が<font size=4 color=#$mojiiro1><b>$intup</b></font>上がった！</font><br>
HTM
}
	}

if ( $chasoubi[2] eq "リップソード") {
$kaihuku = int(rand(4));
if ( $kaihuku == 1 ) {
$intup = int(rand(10)) + 7;
$cha += $intup;
print <<"HTM";
<font size=-1>リップソードの効果で、一時的に<b>CHA</b>が<font size=4 color=#$mojiiro1><b>$intup</b></font>上がった！</font><br>
HTM
}
	}

if ( $chasoubi[7] eq "アダマンタイトリング") {
$kaihuku = int(rand(6));
if ( $kaihuku == 1 ) {
$intup = int(rand(1)) + 1;
$champ += $intup;
print <<"HTM";
<font size=-1>アダマンタイトリングの効果で、<b>TP</b>が<font size=4 color=#$mojiiro3><b>$intup</b></font>回復した。</font><br>
HTM
	if ( $champ > $chastats[16] ) {$champ = $chastats[16];}
}
	}

if ( $chasoubi[3] eq "政宗の兜") {
$kaihuku = int(rand(7));
if ( $kaihuku == 1 ) {
$intup = int(rand(2)) + 2;
$champ += $intup;
print <<"HTM";
<font size=-1>政宗の兜の効果で、<b>TP</b>が<font size=4 color=#$mojiiro3><b>$intup</b></font>回復した。</font><br>
HTM
	if ( $champ > $chastats[16] ) {$champ = $chastats[16];}
}
	}

if ( $chasoubi[2] eq "聖なる盾") {
$kaihuku = int(rand(3));
if ( $kaihuku == 1 ) {
$chahpnow += $chalvl;
print <<"HTM";
<font size=-1>聖なる盾の癒しの効果で、<b>HP</b>が<font size=4 color=#$mojiiro3><b>$chalvl</b></font>回復した。</font><br>
HTM
	if ( $chahpnow > $chastats[9] ) {$chahpnow = $chastats[9];}
}
	}

if ( $chasoubi[2] eq "清浄の盾") {
$kaihuku = int(rand(2));
if ( $kaihuku == 1 ) {
$intup = int(rand(15)) + 10;
print <<"HTM";
<font size=-1>清浄の盾の癒しの効果で、<b>HP</b>が<font size=4 color=#$mojiiro3><b>$intup</b></font>回復した。</font><br>
HTM
$chahpnow += $intup;
	if ( $chahpnow > $chastats[9] ) {$chahpnow = $chastats[9];}
}
	}

if ( $chasoubi[3] eq "清浄の冠") {
$kaihuku = int(rand(2));
if ( $kaihuku == 1 ) {
$intup = int(rand(15)) + 10;
print <<"HTM";
<font size=-1>清浄の冠の癒しの効果で、<b>HP</b>が<font size=4 color=#$mojiiro3><b>$intup</b></font>回復した。</font><br>
HTM
$chahpnow += $intup;
	if ( $chahpnow > $chastats[9] ) {$chahpnow = $chastats[9];}
}
	}

if ( $chasoubi[2] eq "汚れた目玉") {
$kaihuku = int(rand(2));
if ( $kaihuku == 1 ) {
$intup = int(rand(6)) + 10;
$cha += $intup;
print <<"HTM";
<font size=-1>汚れた目玉の効果で、一時的に<b>CHA</b>が<font size=4 color=#$mojiiro1><b>$intup</b></font>上がった！</font><br>
HTM
}
	}

if ( $chasoubi[2] eq "プラズマブレード") {
$kaihuku = int(rand(4));
if ( $kaihuku == 1 ) {
$intup = int(rand(6)) + 5;
$ac += $intup;
print <<"HTM";
<font size=-1>プラズマブレードは$chanameの<b>AC</b>を一時的に<font size=4 color=#$mojiiro1><b>$intup</b></font>高めた！</font><br>
HTM
}
	}

if ( $chasoubi[3] eq "マムシフード") {
$intup = int(rand(2)) + 1;
$svm += $intup;
print <<"HTM";
<font size=-1>マムシフードの効果で、一時的に<b>SVM</b>が<font size=4 color=#$mojiiro1><b>$intup</b></font>上がった！</font><br>
HTM
	}

if ( $chasoubi[5] eq "ヘルアーマーレッグス") {
$intup = int(rand(6)) + 14;
$svm += $intup;
print <<"HTM";
<font size=-1>ヘルアーマーレッグスの効果で、一時的に<b>SVM</b>が<font size=4 color=#$mojiiro1><b>$intup</b></font>上がった！</font><br>
HTM
	}

if ( $chasoubi[4] eq "ブリザードローブ") {
$intup = int(rand(2)) + 3;
$svc += $intup;
print <<"HTM";
<font size=-1>ブリザードローブの効果で、一時的に<b>SVC</b>が<font size=4 color=#$mojiiro1><b>$intup</b></font>上がった！</font><br>
HTM
	}

if ( $chasoubi[4] eq "アイスクィーンローブ") {
$intup = int(rand(2)) + 3;
$svc += $intup;
print <<"HTM";
<font size=-1>アイスクィーンローブの効果で、一時的に<b>SVC</b>が<font size=4 color=#$mojiiro1><b>$intup</b></font>上がった！</font><br>
HTM
	}

if ( $chasoubi[2] eq "ノールクロー") {
$kaihuku = int(rand(3));
if ( $kaihuku == 1 ) {
$tuika = int($str / 3);
print <<"HTM";
<font size=-1>ノールクローで素早く追加攻撃！　さらに<font size=4 color=#$mojiiro2><b>$tuika</b></font>のダメージを与えた！</font><br>
HTM
$monshpnow -= $tuika;
}
	}

if ( $chasoubi[1] eq "ナイトランス") {
$kaihuku = int(rand(3));
if ( $kaihuku == 1 ) {
$tuika = int($str / 3);
print <<"HTM";
<font size=-1>ナイトランスで素早く追加攻撃！　さらに<font size=4 color=#$mojiiro2><b>$tuika</b></font>のダメージを与えた！</font><br>
HTM
$monshpnow -= $tuika;
}
	}

if ( $chasoubi[4] eq "女王様の服") {
$kaihuku = int(rand(70));
if ( $kaihuku == 1 ) {
$tuika = int(rand(5)) + 5;
$chastats[9] += $tuika;
print <<"HTM";
<font size=-1>女王様の服は$chanameの肉体を増強した！　最大HPが<font size=4 color=#$mojiiro1><b>$tuika</b></font>上がった！</font><br>
HTM
}
	}

if ( $chasoubi[5] eq "ブラッドレッグス") {
$kaihuku = int(rand(5));
if ( $kaihuku == 1 ) {
$intup = int($dmg / 3) + 1;
$chahpnow += $intup;
print <<"HTM";
<font size=-1>ブラッドレッグスは敵のHPを<font size=4 color=#$mojiiro2><b>$intup</b></font>吸い取った！　<b>HP</b>が<font size=4 color=#$mojiiro3><b>$intup</b></font>回復した。</font><br>
HTM
	if ( $chahpnow > $chastats[9] ) {$chahpnow = $chastats[9];}
}
	}

if ( $chasoubi[3] eq "白熊の被り物") {
$kaihuku = int(rand(3));
if ( $kaihuku == 1 ) {
$intup = int(rand(10)) + 6;
$str += $intup;
print <<"HTM";
<font size=-1>白熊の被り物の効果で、一時的に<b>STR</b>が<font size=4 color=#$mojiiro1><b>$intup</b></font>上がった！</font><br>
HTM
}
	}

if ( $chasoubi[1] eq "グレートボーンソード") {
$kaihuku = int(rand(3));
if ( $kaihuku == 1 ) {
$intup = int(rand(20)) + 10;
$str += $intup;
print <<"HTM";
<font size=-1>グレートボーンソードの効果で、一時的に<b>STR</b>が<font size=4 color=#$mojiiro1><b>$intup</b></font>上がった！</font><br>
HTM
}
	}

if ( $chasoubi[4] eq "デーモンスキンチュニック") {
$kaihuku = int(rand(3));
if ( $kaihuku == 1 ) {
$intup = int(rand(10)) + 15;
$svm += $intup;
print <<"HTM";
<font size=-1>デーモンスキンチュニックの効果で、一時的に<b>SVM</b>が<font size=4 color=#$mojiiro1><b>$intup</b></font>上がった！</font><br>
HTM
}
	}

if ( $chasoubi[4] eq "フレイムアーマーヘルム") {
$intup = int(rand(10)) + 11;
$svc += $intup;
print <<"HTM";
<font size=-1>フレイムアーマーヘルムの効果で、一時的に<b>SVC</b>が<font size=4 color=#$mojiiro1><b>$intup</b></font>上がった！</font><br>
HTM
	}

if ( $chasoubi[6] eq "ダークアーマーグローブ") {
$kaihuku = int(rand(3));
if ( $kaihuku == 1 ) {
$intup = int(rand(10)) + 18;
$svm += $intup;
print <<"HTM";
<font size=-1>ダークアーマーグローブの効果で、一時的に<b>SVM</b>が<font size=4 color=#$mojiiro1><b>$intup</b></font>上がった！</font><br>
HTM
}
	}

if ( $chasoubi[4] eq "アイスアーマーチェスト") {
$kaihuku = int(rand(3));
if ( $kaihuku == 1 ) {
$intup = int(rand(10)) + 15;
$svc += $intup;
print <<"HTM";
<font size=-1>アイスアーマーチェストの効果で、一時的に<b>SVM</b>が<font size=4 color=#$mojiiro1><b>$intup</b></font>上がった！</font><br>
HTM
}
	}

if ( $chasoubi[1] eq "ファイアーソード") {
$kaihuku = int(rand(3));
if ( $kaihuku == 1 ) {
$intup = int(rand(10)) + 13;
$svf += $intup;
print <<"HTM";
<font size=-1>ファイアーソードの効果で、一時的に<b>SVF</b>が<font size=4 color=#$mojiiro1><b>$intup</b></font>上がった！</font><br>
HTM
}
	}

if ( $chasoubi[3] eq "アシュラの仮面") {
$kaihuku = int(rand(3));
if ( $kaihuku == 1 ) {
$intup = int(rand(20)) + 15;
$agi += $intup;
print <<"HTM";
<font size=-1>アシュラの仮面の効果で、一時的に<b>AGI</b>が<font size=4 color=#$mojiiro1><b>$intup</b></font>上がった！</font><br>
HTM
}
	}

if ( $chasoubi[3] eq "ゴブリンスキンチュニック") {
$kaihuku = int(rand(3));
if ( $kaihuku == 1 ) {
$intup = int(rand(8)) + 3;
$agi += $intup;
print <<"HTM";
<font size=-1>ゴブリンスキンチュニックの効果で、一時的に<b>AGI</b>が<font size=4 color=#$mojiiro1><b>$intup</b></font>上がった！</font><br>
HTM
}
	}

if ( $chasoubi[4] eq "イエティスキンチェスト") {
$intup = int(rand(3)) + 2;
$str += $intup;
print <<"HTM";
<font size=-1>イエティスキンチェストの効果で、一時的に<b>STR</b>が<font size=4 color=#$mojiiro1><b>$intup</b></font>上がった！</font><br>
HTM
	}

if ( $chasoubi[4] eq "アイスローブ") {
$intup = int(rand(2)) + 2;
$svf += $intup;
$str += $intup;
print <<"HTM";
<font size=-1>アイスローブの効果で、一時的に<b>STR,SVF</b>が<font size=4 color=#$mojiiro1><b>$intup</b></font>上がった！</font><br>
HTM
	}

if ( $chasoubi[2] eq "兵法書") {
$intup = int(rand(13)) + 10;
$int += $intup;
print <<"HTM";
<font size=-1>兵法書の効果で、一時的に<b>INT</b>が<font size=4 color=#$mojiiro1><b>$intup</b></font>上がった！</font><br>
HTM
	}

if ( $chasoubi[4] eq "ケルベロスの服") {
$intup = int(rand(5)) + 5;
$agi += $intup;
print <<"HTM";
<font size=-1>ケルベロスの服の効果で、一時的に<b>AGI</b>が<font size=4 color=#$mojiiro1><b>$intup</b></font>上がった！</font><br>
HTM
	}

if ( $chasoubi[3] eq "ケルベロスの被り物") {
$intup = int(rand(3)) + 4;
$agi += $intup;
print <<"HTM";
<font size=-1>ケルベロスの被り物の効果で、一時的に<b>AGI</b>が<font size=4 color=#$mojiiro1><b>$intup</b></font>上がった！</font><br>
HTM
	}

if ( $chasoubi[3] eq "ケルベロスの腕") {
$intup = int(rand(4)) + 4;
$agi += $intup;
print <<"HTM";
<font size=-1>ケルベロスの腕の効果で、一時的に<b>AGI</b>が<font size=4 color=#$mojiiro1><b>$intup</b></font>上がった！</font><br>
HTM
	}

if ( $chasoubi[4] eq "魔人の衣") {
$kaihuku = int(rand(4));
if ( $kaihuku == 1 ) {
$intup2 = int(rand(10)) + 8;
$intup = int($dmg / 2) + 1;
$str += $intup2;
$chahpnow += $intup;
print <<"HTM";
<font size=-1>魔人の衣の効果で、<b>STR</b>が一時的に<b>$intup2</b>上昇し、<b>HP</b>が<font size=4 color=#$mojiiro3><b>$intup</b></font>回復した。</font><br>
HTM
	if ( $chahpnow > $chastats[9] ) {$chahpnow = $chastats[9];}
}
	}
}


#　レベルアップ処理
sub levelup {
$statsban = 2;
		while ( $statsban < 9 ) {
# srand;
$lvlrand = rand ($jobrand[$statsban]);
			if ( $lvlrand < 1 ) {

print "$statsname[$statsban] + <b>1</b>　（<b><font color=palevioletred>$chastats[$statsban]</font>　⇒　";
$chastats[$statsban] ++;
print "<font color=green>$chastats[$statsban]</font></b>）<br>";
			}
$statsban ++;
		}
# srand;
$lvlpt += 2 + $chalvl;
$lvlpoint += $lvlpt;
$chastats[14] += $chalvl;
$hpup = int ( rand ($jobhpuprand) ) + int ( $chalvl / 5 ) + $jobhpup;
print "最大HP + <b>$hpup</b>　（<b><font color=palevioletred>$chastats[9]</font>　⇒　";
$chastats[9] += $hpup;
print "<font color=green>$chastats[9]</font></b>）<br><br>";
if ( $chasoubi[7] eq "キャパシティリング") { $chastats[14] += int($chalvl * 1.3) }
$chastats[14] += $chalvl;
}

exit;