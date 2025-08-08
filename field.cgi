#　冒険中プレーヤーの処理
($sec,$min,$hour,$mday,$mon,$year,$wday) = localtime(time);
$year = $year + 1900;$mon ++;
@youbi = ('日','月','火','水','木','金','土');
if ( length($min) == 1 ) { $min = "0$min"; }
$genzai ="$year年$mon月$mday日($youbi[$wday]) $hour:$min";
open(NOW,"$maindir/playing$bousikts");
	while( $playnow = <NOW> ) {
		chop($playnow);
		($nowid,$nowname,$nowjikan) = split(/\//,$playnow);
		if ( $now < $nowjikan + 300 && $nowid ne $chaid ) {
			push(@playing,$playnow);
		}
	}
close(NOW);
$playnow = "$chaid/$chaname/$now\n";
push(@playing,$playnow);

open(NOW,">$maindir/playing$bousikts");
flock(NOW,2);
	foreach $playnow ( @playing ) {
print NOW "$playnow\n";
	}
flock(NOW,8);
close(NOW);
require "settei.cgi";
if ( $chastats[0] > $maxdmg ) { $chastats[0] = $maxdmg };
if ( $chastats[2] > $maxstr ) { $chastats[2] = $maxstr };
if ( $chastats[1] > $maxdef ) { $chastats[1] = $maxdef };
if ( $chastats[3] > $maxagi ) { $chastats[3] = $maxagi };
if ( $chastats[4] > $maxint ) { $chastats[4] = $maxint };
if ( $chastats[9] > $maxmhp ) { $chastats[9] = $maxmhp };
if ( $mente == 1 ){
&mente;
}
@omosa = ("","軽量","中量","重量");
@bui = ("道具","右手","左手","頭","胸","脚","腕","指","首");

$jobbarcha1 = int( ( $jobexpnow[$chaclass] / $jobexp[$chaclass] ) * 170 );
$jobritu = int($jobbarcha1 / 1.7); 
$jobritu2 = "<font color=darkblue>$jobritu<font size=-2>％</font></b></font>";
if ( $jobbarcha1 != 170 ) {
$jobbarcha2 = 170 - $jobbarcha1;
$hpbardmg3 = "<img src=\"$maindir/$imgfile/hpbar2.gif\" width=$jobbarcha2 height=\"8\">";
}

$playingkazu = @playing;
print <<"HTM";
<center>
<table border=0 width=800><tr>
<td align=right><nobr><font size=6 color=#$mojiiro2><b>$zone[$chaplace]</b></font></nobr></td><td width=30></td><td><nobr>
現在の冒険者（$playingkazu人）/
HTM

foreach $playnow ( @playing ) {

	chop($playnow);
	($nowid,$nowname) = split(/\//,$playnow);
print " <a href=\"./$introcgi?usrid=$nowid\" target=\"intro\"><b>$nowname</font></b></a> /<wbr>";

}

$timesa = $chajikan - $now + $nexttime;

print <<"HTM";
<wbr></nobr></tr></table><br><hr>
<br>
<table border=0><tr><td>
<table border=1><tr><td>
<img src="$maindir/$imgfile/zonepic$chaplace.gif">
</td></tr></table>
</td><td width=10></td><td>
<table border=0><tr><td colspan=3>
HTM


$ryoukin1 = ( $chalvl ) * 3;
$ryoukin2 = ( $chastats[16] - $champ ) * 1;
$ryoukin = $ryoukin1 + $ryoukin2;
$tugilvl = $chanextlvl - $chaexp;
if ($jobexpnow[$chaclass] == $jobexp[$chaclass]){ $jobritu2 ="<font color=red><font size=-2> MASTER! </font></font>"; }
print <<"HTM";
<SCRIPT LANGUAGE="JavaScript">
defaultStatus="右クリックでサブメニューを表\示します。";

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
                <center><B><u><font color=darkblue><font face="Copperplate Gothic Bold">SUB MENU</font></font></u></B></center><P>
                <b>福引券： <font color=#$chamoji>$hukubiki</b></font><font size=-1><b>枚</b></font><br><hr>
                <b>魅力（CHA）　：<font color=#$chamoji>$chastats[5]</b></font> + <b><font color=palevioletred>$karistats[5]</font></b><br>
                <b>火耐性（SVF）：<font color=#$chamoji>$chastats[6]</b></font> + <b><font color=palevioletred>$karistats[6]</font></b><br>
                <b>水耐性（SVC）：<font color=#$chamoji>$chastats[7]</b></font> + <b><font color=palevioletred>$karistats[7]</font></b><br>
                <b>魔耐性（SVM）：<font color=#$chamoji>$chastats[8]</b></font> + <b><font color=palevioletred>$karistats[8]</font></b><br><hr>

                <font size=-1><b>熟練度【$job[$chaclass]】   <font color=palevioletred>$jobritu2</font><font size=-2></font></b></font><br>
<img src="$maindir/$imgfile/exp.gif" height="10"><img src="$maindir/$imgfile/jobbar1.gif" width=$jobbarcha1 height="8">$hpbardmg3<img src="$maindir/$imgfile/exp.gif" height="8"><br><hr>
                <b>今回の収入：<font color=blue>$chastats[11]</font>Ｇ<br>
                現在の報酬：<font color=blue>$chastats[13]</font>Ｇ<br>
                現在の宿代：<font color=red>$ryoukin</font>Ｇ<br><hr>

                <font size=-1>次のLvまで</font><font color=#$chamoji>$tugilvl</font><font size=-1>EXP</font></b>

            <TD bgcolor="silver"><br>
<center>
<table bordercolor=#$wakuiro border=1>
<tr><td><nobr><b>S.EXP</b></nobr></td><td width=70 align=right><nobr><font color=palevioletred><b>$lvlpoint</font> pt</b></nobr></td></tr></table>
<form method="post" action="./$zonecgi">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="4" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="　  手紙を送る  　">
</form>
<form method="post" action="./$zonecgi">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="8" name="useitem">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value=" ポイント振り分け " size=30>
</form>
<form method="post" action="./$zonecgi">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="3" name="useitem">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="     隊列変更     " size=30>
</form>
<form method="post" action="./$zonecgi">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="2" name="useitem">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value=" アイテムを捨てる  " size=30>
</form>
<form method="post" action="./$zonecgi">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="21" name="useitem">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="オートポーション " size=30>
</form>
<form method="post" action="./$zonecgi">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="80" name="useitem">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="   コメント変更   ">
</form>
<form action="$urlbbs" target=_blank>
<input type="submit" value="　    掲示板    　" size=30>
</form>
<SCRIPT language="JavaScript">
<!--
function CloseWin(){
    window.close();
}
// -->
</SCRIPT>
</td>

            </TD>
        </TR>
    </TABLE>
</DIV>
<!--メニュー用タグここまで-->
HTM

if ( $in{useitem} eq "1"){
#　アイテム使用処理
			$ccc = 1;$cbc = 0;
			while ( $ccc < 9 ) {
				if ( $chaitem[$ccc] ne "" ) {
				$cbc ++;
				}
				$ccc ++;
			}
	if ( $cbc == 0 ) {
print "<b>使用できるアイテムがありません</b><br><br>";
&fieldform;
	} else {
			$ccc = 1;$cba = 0;
			while ( $ccc < 9 ) {
				if ( $chaitem[$ccc] ne "" ) {
open(KAI,"$maindir/item$bousikts");
		while ( $kaitori = <KAI> ) {
			($kainame,$a,$a,$a,$a,$a,$itemstats,$itemstats2) = split(/,/,$kaitori);
			if ( $chaitem[$ccc] eq $kainame && $itemstats >= 10) {
				push(@itemsuuji,$ccc);
				push(@itemkouka,$itemstats);
				push(@itemkouka2,$itemstats2);
				$cba ++;
			}
		}
close(KAI);
				}
$ccc ++;
			}
		if( $cba == 0 ) {
print "<b>使用できるアイテムがありません<br><br></b>";

		} else {
print <<"HTM";
「アイテムを選択してください」<br>
<form method="post" action="./$zonecgi">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="1a" name="useitem">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="     使用する    " onClick="this.disabled=true; this.value='     使用する    '; this.form.submit();"><br>
<select name="itemds" size=5>
HTM
$add = 0;
			foreach $atai (@itemsuuji) {
		print "<option value=\"$chaitem[$atai]/$atai/$itemkouka[$add]/$itemkouka2[$add]\">$chaitem[$atai] （$chasetumei[$atai]）";
$add ++;
			}
print <<"HTM";
</select></form><br>
HTM
		}
	}
&zoneform;

} elsif ( $in{useitem} eq "1a"){
($itemname,$itemnum,$itemstats,$itemstats2) = split(/\//,$in{itemds});
	if ( $itemname ne $chaitem[$itemnum] ) {
		&CgiError('エラー発生','不正をした疑いがあります。');
	} elsif ( $itemstats == 10 ) {

		if ( $chahp == $chastats[9] ) {
print "<b>それを使用しても意味がありません<br><br></b>";

		} else {
print "<b><font size=+1>$chaitem[$itemnum]</font> を使用しました</b><br><br>";
$chahp += $itemstats2;
			if ( $chahp > $chastats[9] ) {
			$chahp = $chastats[9];
			}
			if ( $chaeff[$itemnum] == 1 ) {
$chaitem[$itemnum] = $chaeff[$itemnum] = $chasetumei[$itemnum] = "";
			} elsif ( $chaeff[$itemnum] > 1 ) {
$chaeff[$itemnum] --;
			} else {
&fuseisyori;exit;
			}
&charadatawrt;
		}
&fieldform;


	} elsif ( $itemstats == 36 ) {

		if ( $champ == $chastats[16] ) {
print "<b>それを使用しても意味がありません<br><br></b>";

		} else {
print "<b><font size=+1>$chaitem[$itemnum]</font> を使用しました</b><br><br>";
$champ += $itemstats2;
			if ( $champ > $chastats[16] ) {
			$champ = $chastats[16];
			}
			if ( $chaeff[$itemnum] == 1 ) {
$chaitem[$itemnum] = $chaeff[$itemnum] = $chasetumei[$itemnum] = "";
			} elsif ( $chaeff[$itemnum] > 1 ) {
$chaeff[$itemnum] --;
			} else {
&fuseisyori;exit;
			}
&charadatawrt;
		}
&fieldform;



	} elsif ( $itemstats == 37 ) {

		if ( $chastats[12] == $chagold ) {
print "<b>それを使用しても意味がありません<br><br></b>";

		} else {
print "<b><font size=+1>$chaitem[$itemnum]</font> を使用しました。</b><br>";
$chastats[16] += 1;
print "<b>最大TPが、<font size=+1 color=#$mojiiro2>1</font><b> 上がった！</b><br><br>";
			if ( $chahp > $chastats[9] ) {
			$chahp = $chastats[9];
			}
			if ( $chaeff[$itemnum] == 1 ) {
$chaitem[$itemnum] = $chaeff[$itemnum] = $chasetumei[$itemnum] = "";
			} elsif ( $chaeff[$itemnum] > 1 ) {
$chaeff[$itemnum] --;
			} else {
&fuseisyori;exit;
			}
&charadatawrt;
		}
&fieldform;


	} elsif ( $itemstats == 38 ) {

		if ( $chastats[12] == $chagold ) {
print "<b>それを使用しても意味がありません<br><br></b>";

		} else {
print "<b><font size=+1>$chaitem[$itemnum]</font> を使用しました。</b><br>";
$chastats[16] += 10;
print "<b>最大TPが、<font size=+1 color=#$mojiiro2>10</font><b> 上がった！</b><br><br>";
			if ( $chahp > $chastats[9] ) {
			$chahp = $chastats[9];
			}
			if ( $chaeff[$itemnum] == 1 ) {
$chaitem[$itemnum] = $chaeff[$itemnum] = $chasetumei[$itemnum] = "";
			} elsif ( $chaeff[$itemnum] > 1 ) {
$chaeff[$itemnum] --;
			} else {
&fuseisyori;exit;
			}
&charadatawrt;
		}
&fieldform;


	} elsif ( $itemstats == 41 ) {

		if ( $chastats[12] == $chagold ) {
print "<b>それを使用しても意味がありません<br><br></b>";

		} else {
print "<b><font size=+1>$chaitem[$itemnum]</font> を使用しました。</b><br>";
$chastats[16] += 20;
$chastats[1] += 10;
$chastats[2] += 10;
$chastats[3] += 10;
$chastats[4] += 10;
$chastats[9] += 100;
print "<b>最大HPが、<font size=+1 color=#$mojiiro2>100</font><b> 上がった！</b><br>";
print "<b>最大TPが、<font size=+1 color=#$mojiiro2>20</font><b> 上がった！</b><br>";
print "<b>STRが、<font size=+1 color=#$mojiiro2>10</font><b> 上がった！</b><br>";
print "<b>ACが、<font size=+1 color=#$mojiiro2>10</font><b> 上がった！</b><br>";
print "<b>AGIが、<font size=+1 color=#$mojiiro2>10</font><b> 上がった！</b><br>";
print "<b>INTが、<font size=+1 color=#$mojiiro2>10</font><b> 上がった！</b><br>";
			if ( $chahp > $chastats[9] ) {
			$chahp = $chastats[9];
			}
			if ( $chaeff[$itemnum] == 1 ) {
$chaitem[$itemnum] = $chaeff[$itemnum] = $chasetumei[$itemnum] = "";
			} elsif ( $chaeff[$itemnum] > 1 ) {
$chaeff[$itemnum] --;
			} else {
&fuseisyori;exit;
			}
&charadatawrt;
		}
&fieldform;



	} elsif ( $itemstats == 40 ) {

		if ( $chastats[12] == $chagold ) {
print "<b>それを使用しても意味がありません<br><br></b>";

		} else {
print "<b><font size=+1>$chaitem[$itemnum]</font> を使用しました。</b><br>";
$chastats[16] += 30;
print "<b>最大TPが、<font size=+1 color=#$mojiiro2>30</font><b> 上がった！</b><br><br>";
			if ( $chahp > $chastats[9] ) {
			$chahp = $chastats[9];
			}
			if ( $chaeff[$itemnum] == 1 ) {
$chaitem[$itemnum] = $chaeff[$itemnum] = $chasetumei[$itemnum] = "";
			} elsif ( $chaeff[$itemnum] > 1 ) {
$chaeff[$itemnum] --;
			} else {
&fuseisyori;exit;
			}
&charadatawrt;
		}
&fieldform;


	} elsif ( $itemstats == 39 ) {

		if ( $chastats[12] == $chagold ) {
print "<b>それを使用しても意味がありません<br><br></b>";

		} else {
$chahp = $chastats[9];
$champ = $chastats[16];
print "<b><font size=+1>$chaitem[$itemnum]</font> を使用しました。</b><br>";
print "<b>HPとTPが全快した！</b><br><br>";
			if ( $chahp > $chastats[9] ) {
			$chahp = $chastats[9];
			}
			if ( $chaeff[$itemnum] == 1 ) {
$chaitem[$itemnum] = $chaeff[$itemnum] = $chasetumei[$itemnum] = "";
			} elsif ( $chaeff[$itemnum] > 1 ) {
$chaeff[$itemnum] --;
			} else {
&fuseisyori;exit;
			}
&charadatawrt;
		}
&fieldform;


	} elsif ( $itemstats == 30 ) {

		if ( $chastats[12] == $chagold ) {
print "<b>それを使用しても意味がありません<br><br></b>";

		} else {
print "<b><font size=+1>$chaitem[$itemnum]</font> を使用しました。</b><br>";
$hpup = 10;
$chastats[9] += $hpup;
print "<b>最大HPが、<font size=+1 color=#$mojiiro2>$hpup</font><b> 上がった！</b><br><br>";
			if ( $chahp > $chastats[9] ) {
			$chahp = $chastats[9];
			}
			if ( $chaeff[$itemnum] == 1 ) {
$chaitem[$itemnum] = $chaeff[$itemnum] = $chasetumei[$itemnum] = "";
			} elsif ( $chaeff[$itemnum] > 1 ) {
$chaeff[$itemnum] --;
			} else {
&fuseisyori;exit;
			}
&charadatawrt;
		}
&fieldform;


	} elsif ( $itemstats == 31 ) {

		if ( $chastats[12] == $chagold ) {
print "<b>それを使用しても意味がありません<br><br></b>";

		} else {
print "<b><font size=+1>$chaitem[$itemnum]</font> を使用しました。</b><br>";
$strup = 1;
$chastats[2] += $strup;
print "<b>STRが、<font size=+1 color=#$mojiiro2>$strup</font><b> 上がった！</b><br><br>";
			if ( $chahp > $chastats[9] ) {
			$chahp = $chastats[9];
			}
			if ( $chaeff[$itemnum] == 1 ) {
$chaitem[$itemnum] = $chaeff[$itemnum] = $chasetumei[$itemnum] = "";
			} elsif ( $chaeff[$itemnum] > 1 ) {
$chaeff[$itemnum] --;
			} else {
&fuseisyori;exit;
			}
&charadatawrt;
		}
&fieldform;


	} elsif ( $itemstats == 32 ) {

		if ( $chastats[12] == $chagold ) {
print "<b>それを使用しても意味がありません<br><br></b>";

		} else {
print "<b><font size=+1>$chaitem[$itemnum]</font> を使用しました。</b><br>";
$acup = 1;
$chastats[1] += $acup;
print "<b>ACが、<font size=+1 color=#$mojiiro2>$acup</font><b> 上がった！</b><br><br>";
			if ( $chahp > $chastats[9] ) {
			$chahp = $chastats[9];
			}
			if ( $chaeff[$itemnum] == 1 ) {
$chaitem[$itemnum] = $chaeff[$itemnum] = $chasetumei[$itemnum] = "";
			} elsif ( $chaeff[$itemnum] > 1 ) {
$chaeff[$itemnum] --;
			} else {
&fuseisyori;exit;
			}
&charadatawrt;
		}
&fieldform;


	} elsif ( $itemstats == 33 ) {

		if ( $chastats[12] == $chagold ) {
print "<b>それを使用しても意味がありません<br><br></b>";

		} else {
print "<b><font size=+1>$chaitem[$itemnum]</font> を使用しました。</b><br>";
$chaup = 1;
$chastats[5] += $chaup;
print "<b>CHAが、<font size=+1 color=#$mojiiro2>$chaup</font><b> 上がった！</b><br><br>";
			if ( $chahp > $chastats[9] ) {
			$chahp = $chastats[9];
			}
			if ( $chaeff[$itemnum] == 1 ) {
$chaitem[$itemnum] = $chaeff[$itemnum] = $chasetumei[$itemnum] = "";
			} elsif ( $chaeff[$itemnum] > 1 ) {
$chaeff[$itemnum] --;
			} else {
&fuseisyori;exit;
			}
&charadatawrt;
		}
&fieldform;


	} elsif ( $itemstats == 34 ) {

		if ( $chastats[12] == $chagold ) {
print "<b>それを使用しても意味がありません<br><br></b>";

		} else {
print "<b><font size=+1>$chaitem[$itemnum]</font> を使用しました。</b><br>";
$intup = 1;
$chastats[4] += $intup;
print "<b>INTが、<font size=+1 color=#$mojiiro2>$intup</font><b> 上がった！</b><br><br>";
			if ( $chahp > $chastats[9] ) {
			$chahp = $chastats[9];
			}
			if ( $chaeff[$itemnum] == 1 ) {
$chaitem[$itemnum] = $chaeff[$itemnum] = $chasetumei[$itemnum] = "";
			} elsif ( $chaeff[$itemnum] > 1 ) {
$chaeff[$itemnum] --;
			} else {
&fuseisyori;exit;
			}
&charadatawrt;
		}
&fieldform;


	} elsif ( $itemstats == 35 ) {

		if ( $chastats[12] == $chagold ) {
print "<b>それを使用しても意味がありません<br><br></b>";

		} else {
print "<b><font size=+1>$chaitem[$itemnum]</font> を使用しました。</b><br>";
$agiup = 1;
$chastats[3] += $agiup;
print "<b>AGIが、<font size=+1 color=#$mojiiro2>$agiup</font><b> 上がった！</b><br><br>";
			if ( $chahp > $chastats[9] ) {
			$chahp = $chastats[9];
			}
			if ( $chaeff[$itemnum] == 1 ) {
$chaitem[$itemnum] = $chaeff[$itemnum] = $chasetumei[$itemnum] = "";
			} elsif ( $chaeff[$itemnum] > 1 ) {
$chaeff[$itemnum] --;
			} else {
&fuseisyori;exit;
			}
&charadatawrt;
		}
&fieldform;


	} elsif ( $itemstats == 51 ) {

		if ( $chastats[12] == $chagold ) {
print "<b>それを使用しても意味がありません<br><br></b>";

		} else {
print "<b><font size=+1>$chaitem[$itemnum]</font> を使用しました。</b><br>";
print "<b>特技『<font color=red>鳳凰の舞</font>』<b>を習得した！</b><br><br>";
if ( $flag14 eq "" ) { $flag14 = 14; }
			if ( $chahp > $chastats[9] ) {
			$chahp = $chastats[9];
			}
			if ( $chaeff[$itemnum] == 1 ) {
$chaitem[$itemnum] = $chaeff[$itemnum] = $chasetumei[$itemnum] = "";
			} elsif ( $chaeff[$itemnum] > 1 ) {
$chaeff[$itemnum] --;
			} else {
&fuseisyori;exit;
			}
&charadatawrt;
		}
&fieldform;


	} elsif ( $itemstats == 52 ) {

		if ( $chastats[12] == $chagold ) {
print "<b>それを使用しても意味がありません<br><br></b>";

		} else {
print "<b><font size=+1>$chaitem[$itemnum]</font> を使用しました。</b><br>";
print "<b>特技『<font color=red>リバイブ</font>』<b>を習得した！</b><br><br>";
if ( $flag13 eq "" ) { $flag13 = 13; }
			if ( $chahp > $chastats[9] ) {
			$chahp = $chastats[9];
			}
			if ( $chaeff[$itemnum] == 1 ) {
$chaitem[$itemnum] = $chaeff[$itemnum] = $chasetumei[$itemnum] = "";
			} elsif ( $chaeff[$itemnum] > 1 ) {
$chaeff[$itemnum] --;
			} else {
&fuseisyori;exit;
			}
&charadatawrt;
		}
&fieldform;

	} elsif ( $itemstats == 11 ) {
print <<"HTM";
<font size=+1>$chaitem[$itemnum]</font> を使用した！<br><br>
HTM
		if ( $chaeff[$itemnum] == 1 ) {
$chaitem[$itemnum] = $chaeff[$itemnum] = $chasetumei[$itemnum] = "";
		} elsif ( $chaeff[$itemnum] > 1 ) {
$chaeff[$itemnum] --;
		} else {
&fuseisyori;exit;
		}
$chaplace = $itemstats2;
&charadatawrt;
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="$itemstats2" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="$zone[$itemstats2] へ瞬間移動" ><br></td></tr></table>
</form>
HTM
	} else { &fuseisyori; 
	}


} elsif ( $in{riyou} eq "4" ) {
print <<"HTM";
送る人を選択し、内容を記入してください。<br>
<form action="./$zonecgi" method="post">
<input type=hidden value="10" name="sisetu">
<input type=hidden value="41" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<select name="chara">
HTM

open(CHA,"$maindir/$foldacha/user_id$bousi2cha$bousikts2");
$tourokunum = 1;
		while ( $chadata = <CHA> ) {
		chop($chadata);
		($id,$name) = split(/\//,$chadata);
			if ( $name ne $chaname) {
print "<option value=\"$id\">$tourokunum.$name<br>";
$tourokunum ++;
			}
		}
close(CHA);
print <<"HTM";
</select>
<br><br>
<input type=text size=50 value="" name="tegami">(100文字以内)<br><br>
<input type=submit value="　　　 送　信 　　　">
</form>
HTM
&zoneform;

} elsif ( $in{riyou} eq "41" ) {
	if ( $in{tegami} eq "" ) {
print <<"HTM";
手紙の内容が書かれていません。<br>
<br>
HTM
&zoneform;
	} elsif( length($in{tegami}) > 200 ) {
print <<"HTM";
文字数が１００文字を越えています。<br>
<br>
HTM
&zoneform;

	} else {
$in{tegami} =~ s/</&lt;/g;
$in{tegami} =~ s/>/&gt;/g;
$tegaminaiyou =  "$now\t$chaname\t$chamoji\t$in{tegami}\t$genzai\t\n";

open(BAN,"$maindir/$foldacha/tegami_$in{chara}$bousi2cha$bousikts");
   @letters = <BAN>;
close(BAN);
$letter = @letter;
           if ( $letter >= 20 ) {
              $letters[0] = "";
           }
unshift(@letters,"$now\t$chaname\t$chamoji\t$in{tegami}\t$genzai\t\n");
open(BAN,">$maindir/$foldacha/tegami_$in{chara}$bousi2cha$bousikts");
flock(BAN,2);
   print BAN @letters;
flock(BAN,8);
close(BAN);

print <<"HTM";
手紙は無事届けられました。<br><br>
HTM
&zoneform;

     }

	} elsif ( $in{useitem} eq "80" ) {
print <<"HTM";
新しいコメントを入力してください。（全角35文字・半角70文字以内）<br>
<form action="./$zonecgi" method="post">
<input type=text value="" size=50 name="comment" maxlength=70>
<input type=submit value="  内容変更  " onClick="this.disabled=true; this.value='  内容変更  '; this.form.submit();">

<input type=hidden value="81" name="useitem">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
</form>
HTM
&zoneform;
	} elsif ( $in{useitem} eq "81" ) {
$in{comment} =~ s/,//g;
$maxcombo = $in{comment};
&charadatawrt;
print <<"HTM";
正常に変更されました。<br><br>
HTM
&fieldform;



} elsif ( $in{useitem} eq "6"){

#　武器防具の装備

&itemkuuran;
	if ( $ccb == 9 ) {
print <<"HTM";
「装備できるアイテムを持っていません。」<br>
HTM
&zoneform;
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
「装備できるアイテムを持っていません。」<br>
HTM
&zoneform;
		} else {
print <<"HTM";
「装備するアイテムを選択してください。」<br>
<form method="post" action="./$zonecgi">
<input type=hidden value="20" name="useitem">
<input type=hidden value="61" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="　    装備する   　" onClick="this.disabled=true; this.value='      装備する     '; this.form.submit();"><br>
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
&zoneform;
		}
	}
} elsif ( $in{riyou} eq "61"){
		($soubiname,$numa) = split(/\//,$in{itemde});
	if ( $in{itemde} eq "" ) {
print <<"HTM";
「装備するアイテムが選択されていません。」<br>
HTM
&zoneform;

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
「レベルが足りません。」<br>
HTM
&zoneform;
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
「<font size=4 color=#$mojiiro2><b>$chasoubi[$itembasyo] </font>($chabun[$itembasyo]) を</b><br>
   装備しました。」<br>
HTM
&zoneform;
		}
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




} elsif ( $in{useitem} eq "2"){
#　アイテム投棄処理

			$ccc = 1;$ccb = 0;
			while ( $ccc < 9 ) {
				if ( $chaitem[$ccc] eq "" ) {
				$ccb ++;
				}
				$ccc ++;
			}

	if ( $ccb eq 8 ) {
print <<"HTM";
アイテムがありません<br>
HTM

	} else {
print <<"HTM";
<b><font color=#$mojiiro2>捨てる</font></b>アイテムを選択してください<br>
<form method="post" action="./$zonecgi">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="2a" name="useitem">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="　    捨てる   　" onClick="this.disabled=true; this.value='      捨てる     '; this.form.submit();"><br>
<select name="itemde" size=6>
HTM
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

&zoneform;

} elsif ( $in{useitem} eq "2a"){
if ( $chaitem[$in{itemde}] eq "" ) { &fuseisyori;exit; }
print <<"HTM";
<font size=4 color=#$mojiiro2><b>$chaitem[$in{itemde}]</font> ($chasetumei[$in{itemde}])　を捨てた</b><br><br>
HTM
$chaitem[$in{itemde}] = $chaeff[$in{itemde}] = $chasetumei[$in{itemde}] = "";
&charadatawrt;
&fieldform;




} elsif ( $in{useitem} eq "21"){
$bpo = "0";
#　オートポーション処理
$bpo = "0";
print <<"HTM";
<b>オートポーション設定</b><br>

<form action="./$zonecgi" method="post">
HPが
<input type=text value="$autop" size=5 name="autop" maxlength=5>
以下になった時に、<br>
<input type=text value="$potion" size=16 name="potion" maxlength=16>
を使用する。
<input type=submit value="  確定  " onClick="this.disabled=true; this.value='  確定  '; this.form.submit();">
<input type=hidden value="7" name="sisetu">
<input type=hidden value="81" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
</form>
HTM
&zoneform;

	} elsif ( $in{riyou} eq "81" ) {
$in{comment} =~ s/,//g;
$autop = $in{autop};
$potion = $in{potion};
&charadatawrt;
print <<"HTM";

<form action="./$zonecgi" method="post">
設定完了しました。<br><br>
HTM

&zoneform;





} elsif ( $in{useitem} eq "2a"){
if ( $chaitem[$in{itemde}] eq "" ) { &fuseisyori;exit; }
print <<"HTM";
<font size=4 color=#$mojiiro2><b>$chaitem[$in{itemde}]</font> ($chasetumei[$in{itemde}])　を捨てた</b><br><br>
HTM
$chaitem[$in{itemde}] = $chaeff[$in{itemde}] = $chasetumei[$in{itemde}] = "";
&charadatawrt;
&fieldform;


# ポイント振り分け処理

} elsif ( $in{useitem} eq "8"){

&furiwake;

} elsif ( $in{point} eq "1"){
	if ( $lvlpoint < 1 ){
print <<"HTM";
<b>S.EXP</b>が足りません。<br>
HTM
&zoneform;
	} else {
$lvlpoint --;
$nowstrexp += 2;
	if ( $nowstrexp >= $strexp ) {
print <<"HTM";
<b><font color=darkorange>STR</font></b>が上がった！<br>
HTM
$strexp *= 1.3;
if ($strexp > 1000){$strexp = 1000;}
$nowstrexp = 0;
$chastats[2] ++;
}
&charadatawrt;
&furiwake
}
} elsif ( $in{point} eq "1a"){
	if ( $lvlpoint < 10 ){
print <<"HTM";
<b>S.EXP</b>が足りません。<br>
HTM
&zoneform;
	} else {
$lvlpoint -= 10;
$nowstrexp += 20;
	if ( $nowstrexp >= $strexp ) {
print <<"HTM";
<b><font color=darkorange>STR</font></b>が上がった！<br>
HTM
$strexp *= 1.3;
if ($strexp > 1000){$strexp = 1000;}
$nowstrexp = 0;
$chastats[2] ++;
}
&charadatawrt;
&furiwake
}

} elsif ( $in{point} eq "1c"){
	if ( $lvlpoint < 50 ){
print <<"HTM";
<b>S.EXP</b>が足りません。<br>
HTM
&zoneform;
	} else {
$lvlpoint -= 50;
$nowstrexp += 100;
	if ( $nowstrexp >= $strexp ) {
print <<"HTM";
<b><font color=darkorange>STR</font></b>が上がった！<br>
HTM
$strexp *= 1.3;
if ($strexp > 1000){$strexp = 1000;}
$nowstrexp = 0;
$chastats[2] ++;
}
&charadatawrt;
&furiwake
}

} elsif ( $in{point} eq "1b"){
	if ( $lvlpoint < 100 ){
print <<"HTM";
<b>S.EXP</b>が足りません。<br>
HTM
&zoneform;
	} else {
$lvlpoint -= 100;
$nowstrexp += 200;
	if ( $nowstrexp >= $strexp ) {
print <<"HTM";
<b><font color=darkorange>STR</font></b>が上がった！<br>
HTM
$strexp *= 1.3;
if ($strexp > 1000){$strexp = 1000;}
$nowstrexp = 0;
$chastats[2] ++;
}
&charadatawrt;
&furiwake
}

} elsif ( $in{point} eq "1d"){
	if ( $lvlpoint < 500 ){
print <<"HTM";
<b>S.EXP</b>が足りません。<br>
HTM
&zoneform;
	} else {
$lvlpoint -= 500;
$nowstrexp += 1000;
	if ( $nowstrexp >= $strexp ) {
print <<"HTM";
<b><font color=darkorange>STR</font></b>が上がった！<br>
HTM
$strexp *= 1.3;
if ($strexp > 500){$strexp = 500;}
$nowstrexp = 0;
$chastats[2] ++;
}
&charadatawrt;
&furiwake
}

} elsif ( $in{point} eq "2"){
	if ( $lvlpoint < 1 ){
print <<"HTM";
<b>S.EXP</b>が足りません。<br>
HTM
&zoneform;
	} else {
$lvlpoint --;
$nowacexp += 15;
	if ( $nowacexp >= $acexp ) {
print <<"HTM";
<b><font color=lightsalmon>AC</font></b>が上がった！<br>
HTM
$acexp *= 1.5;
if ($acexp > 1000000){$acexp = 1000000;}
$nowacexp = 0;
$chastats[1] ++;
}
&charadatawrt;
&furiwake
}
} elsif ( $in{point} eq "2a"){
	if ( $lvlpoint < 10 ){
print <<"HTM";
<b>S.EXP</b>が足りません。<br>
HTM
&zoneform;
	} else {
$lvlpoint -= 10;
$nowacexp += 150;
	if ( $nowacexp >= $acexp ) {
print <<"HTM";
<b><font color=lightsalmon>AC</font></b>が上がった！<br>
HTM
$acexp *= 1.5;
if ($acexp > 1000000){$acexp = 1000000;}
$nowacexp = 0;
$chastats[1] ++;
}
&charadatawrt;
&furiwake
}

} elsif ( $in{point} eq "2c"){
	if ( $lvlpoint < 50 ){
print <<"HTM";
<b>S.EXP</b>が足りません。<br>
HTM
&zoneform;
	} else {
$lvlpoint -= 50;
$nowacexp += 750;
	if ( $nowacexp >= $acexp ) {
print <<"HTM";
<b><font color=lightsalmon>AC</font></b>が上がった！<br>
HTM
$acexp *= 1.5;
if ($acexp > 1000000){$acexp = 1000000;}
$nowacexp = 0;
$chastats[1] ++;
}
&charadatawrt;
&furiwake
}

} elsif ( $in{point} eq "2b"){
	if ( $lvlpoint < 100 ){
print <<"HTM";
<b>S.EXP</b>が足りません。<br>
HTM
&zoneform;
	} else {
$lvlpoint -= 100;
$nowacexp += 1500;
	if ( $nowacexp >= $acexp ) {
print <<"HTM";
<b><font color=lightsalmon>AC</font></b>が上がった！<br>
HTM
$acexp *= 1.5;
if ($acexp > 1000000){$acexp = 1000000;}
$nowacexp = 0;
$chastats[1] ++;
}
&charadatawrt;
&furiwake
}

} elsif ( $in{point} eq "2d"){
	if ( $lvlpoint < 500 ){
print <<"HTM";
<b>S.EXP</b>が足りません。<br>
HTM
&zoneform;
	} else {
$lvlpoint -= 500;
$nowacexp += 7500;
	if ( $nowacexp >= $acexp ) {
print <<"HTM";
<b><font color=lightsalmon>AC</font></b>が上がった！<br>
HTM
$acexp *= 1.5;
if ($acexp > 1000000){$acexp = 1000000;}
$nowacexp = 0;
$chastats[1] ++;
}
&charadatawrt;
&furiwake
}

} elsif ( $in{point} eq "3"){
	if ( $lvlpoint < 1 ){
print <<"HTM";
<b>S.EXP</b>が足りません。<br>
HTM
&zoneform;
	} else {
$lvlpoint --;
$nowagiexp += 1;
	if ( $nowagiexp >= $agiexp ) {
print <<"HTM";
<b><font color=orchid>AGI</font></b>が上がった！<br>
HTM
$agiexp *= 1.2;
if ($agiexp > 1000){$agiexp = 1000;}
$nowagiexp = 0;
$chastats[3] ++;
}
&charadatawrt;
&furiwake
}
} elsif ( $in{point} eq "3a"){
	if ( $lvlpoint < 10 ){
print <<"HTM";
<b>S.EXP</b>が足りません。<br>
HTM
&zoneform;
	} else {
$lvlpoint -= 10;
$nowagiexp += 10;
	if ( $nowagiexp >= $agiexp ) {
print <<"HTM";
<b><font color=orchid>AGI</font></b>が上がった！<br>
HTM
$agiexp *= 1.2;
if ($agiexp > 1000){$agiexp = 1000;}
$nowagiexp = 0;
$chastats[3] ++;
}
&charadatawrt;
&furiwake
}

} elsif ( $in{point} eq "3c"){
	if ( $lvlpoint < 50 ){
print <<"HTM";
<b>S.EXP</b>が足りません。<br>
HTM
&zoneform;
	} else {
$lvlpoint -= 50;
$nowagiexp += 50;
	if ( $nowagiexp >= $agiexp ) {
print <<"HTM";
<b><font color=orchid>AGI</font></b>が上がった！<br>
HTM
$agiexp *= 1.2;
if ($agiexp > 1000){$agiexp = 1000;}
$nowagiexp = 0;
$chastats[3] ++;
}
&charadatawrt;
&furiwake
}

} elsif ( $in{point} eq "3b"){
	if ( $lvlpoint < 100 ){
print <<"HTM";
<b>S.EXP</b>が足りません。<br>
HTM
&zoneform;
	} else {
$lvlpoint -= 100;
$nowagiexp += 100;
	if ( $nowagiexp >= $agiexp ) {
print <<"HTM";
<b><font color=orchid>AGI</font></b>が上がった！<br>
HTM
$agiexp *= 1.2;
if ($agiexp > 1000){$agiexp = 1000;}
$nowagiexp = 0;
$chastats[3] ++;
}
&charadatawrt;
&furiwake
}

} elsif ( $in{point} eq "3d"){
	if ( $lvlpoint < 500 ){
print <<"HTM";
<b>S.EXP</b>が足りません。<br>
HTM
&zoneform;
	} else {
$lvlpoint -= 500;
$nowagiexp += 500;
	if ( $nowagiexp >= $agiexp ) {
print <<"HTM";
<b><font color=orchid>AGI</font></b>が上がった！<br>
HTM
$agiexp *= 1.2;
if ($agiexp > 1000){$agiexp = 1000;}
$nowagiexp = 0;
$chastats[3] ++;
}
&charadatawrt;
&furiwake
}

} elsif ( $in{point} eq "4"){
	if ( $lvlpoint < 1 ){
print <<"HTM";
<b>S.EXP</b>が足りません。<br>
HTM
&zoneform;
	} else {
$lvlpoint --;
$nowintexp += 1;
	if ( $nowintexp >= $intexp ) {
print <<"HTM";
<b><font color=cornflowerblue>INT</font></b>が上がった！<br>
HTM
$intexp *= 1.2;
if ($intexp > 1000){$intexp = 1000;}
$nowintexp = 0;
$chastats[4] ++;
}
&charadatawrt;
&furiwake
}
} elsif ( $in{point} eq "4a"){
	if ( $lvlpoint < 10 ){
print <<"HTM";
<b>S.EXP</b>が足りません。<br>
HTM
&zoneform;
	} else {
$lvlpoint -= 10;
$nowintexp += 10;
	if ( $nowintexp >= $intexp ) {
print <<"HTM";
<b><font color=cornflowerblue>INT</font></b>が上がった！<br>
HTM
$intexp *= 1.2;
if ($intexp > 1000){$intexp = 1000;}
$nowintexp = 0;
$chastats[4] ++;
}
&charadatawrt;
&furiwake
	}

} elsif ( $in{point} eq "4c"){
	if ( $lvlpoint < 50 ){
print <<"HTM";
<b>S.EXP</b>が足りません。<br>
HTM
&zoneform;
	} else {
$lvlpoint -= 50;
$nowintexp += 50;
	if ( $nowintexp >= $intexp ) {
print <<"HTM";
<b><font color=cornflowerblue>INT</font></b>が上がった！<br>
HTM
$intexp *= 1.2;
if ($intexp > 1000){$intexp = 1000;}
$nowintexp = 0;
$chastats[4] ++;
}
&charadatawrt;
&furiwake
	}

} elsif ( $in{point} eq "4b"){
	if ( $lvlpoint < 100 ){
print <<"HTM";
<b>S.EXP</b>が足りません。<br>
HTM
&zoneform;
	} else {
$lvlpoint -= 100;
$nowintexp += 100;
	if ( $nowintexp >= $intexp ) {
print <<"HTM";
<b><font color=cornflowerblue>INT</font></b>が上がった！<br>
HTM
$intexp *= 1.2;
if ($intexp > 1000){$intexp = 1000;}
$nowintexp = 0;
$chastats[4] ++;
}
&charadatawrt;
&furiwake
	}

} elsif ( $in{point} eq "4d"){
	if ( $lvlpoint < 500 ){
print <<"HTM";
<b>S.EXP</b>が足りません。<br>
HTM
&zoneform;
	} else {
$lvlpoint -= 500;
$nowintexp += 500;
	if ( $nowintexp >= $intexp ) {
print <<"HTM";
<b><font color=cornflowerblue>INT</font></b>が上がった！<br>
HTM
$intexp *= 1.2;
if ($intexp > 1000){$intexp = 1000;}
$nowintexp = 0;
$chastats[4] ++;
}
&charadatawrt;
&furiwake
	}


sub furiwake{
$strbarcha1 = int( ( $nowstrexp / $strexp ) * 180 );
$strritu = int($strbarcha1 / 1.8); 
if ( $strbarcha1 != 180 ) {
$strbarcha2 = 180 - $strbarcha1;
$strbardmg2 = "<img src=\"$maindir/$imgfile/hpbar2.gif\" width=$strbarcha2 height=\"8\" alt=$strritu％>";
}
$acbarcha1 = int( ( $nowacexp / $acexp ) * 180 );
$acritu = int($acbarcha1 / 1.8); 
if ( $acbarcha1 != 180 ) {
$acbarcha2 = 180 - $acbarcha1;
$acbardmg2 = "<img src=\"$maindir/$imgfile/hpbar2.gif\" width=$acbarcha2 height=\"8\" alt=$acritu％>";
}
$agibarcha1 = int( ( $nowagiexp / $agiexp ) * 180 );
$agiritu = int($agibarcha1 / 1.8); 
if ( $agibarcha1 != 180 ) {
$agibarcha2 = 180 - $agibarcha1;
$agibardmg2 = "<img src=\"$maindir/$imgfile/hpbar2.gif\" width=$agibarcha2 height=\"8\" alt=$agiritu％>";
}
$intbarcha1 = int( ( $nowintexp / $intexp ) * 180 );
$intritu = int($intbarcha1 / 1.8); 
if ( $intbarcha1 != 180 ) {
$intbarcha2 = 180 - $intbarcha1;
$intbardmg2 = "<img src=\"$maindir/$imgfile/hpbar2.gif\" width=$intbarcha2 height=\"8\" alt=$intritu％>";
}

print <<"HTM";
<b>S.EXP</b>の振り分けを行います。<br><br>

<center>
<table bordercolor=#$wakuiro border=1>
<tr><td><nobr>現在の<b>S.EXP</b></nobr></td><td width=70 align=right><nobr><font color=palevioletred><b>$lvlpoint</font> pt</b></nobr></td></tr></table>
</center>

<table border=2>
<tbody>
<tr>
<td><b>ｽﾃｰﾀｽ</td><td><b><center>ステータスEXP</td><td><b>現在</td><td><center><b>1</td><td><center><b>10</td><td><center><b>50</td><td><center><b>100</td><td><center><b>500</td>
</td>
</tr>
<tr>
<td><b><center>STR</td><td><b><center><img src="$maindir/$imgfile/exp.gif" height="10"><img src="$maindir/$imgfile/mpbar1.gif" width=$strbarcha1 height="8" alt="$strritu％">$strbardmg2<img src="$maindir/$imgfile/exp.gif" height="8"></td><td align=right><b><font color=#$chamoji>$chastats[2] </td>
<td>
<form method="post" action="./$zonecgi" style="float:left">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="1" name="point">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="△" size=30>
</form>
</td>
<td>
<form method="post" action="./$zonecgi" style="float:left">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="1a" name="point">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="▲" size=30>
</form>
</td>
<td>
<form method="post" action="./$zonecgi" style="float:left">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="1c" name="point">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="○" size=30>
</form>
</td>
<td>
<form method="post" action="./$zonecgi" style="float:left">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="1b" name="point">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="●" size=30>
</form>
</td>
<td>
<form method="post" action="./$zonecgi" style="float:left">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="1d" name="point">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="☆" size=30>
</form>
</td>
</tr>
<tr>
<td><b><center>AC</td><td><b><center><img src="$maindir/$imgfile/exp.gif" height="10"><img src="$maindir/$imgfile/mpbar1.gif" width=$acbarcha1 height="8" alt="$strritu％">$acbardmg2<img src="$maindir/$imgfile/exp.gif" height="8"></td><td align=right><b><font color=#$chamoji>$chastats[1] </td>
<td>
<form method="post" action="./$zonecgi" style="float:left">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="2" name="point">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="△" size=30>
</form>
</td>
<td>
<form method="post" action="./$zonecgi" style="float:left">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="2a" name="point">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="▲" size=30>
</form>
</td>
<td>
<form method="post" action="./$zonecgi" style="float:left">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="2c" name="point">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="○" size=30>
</form>
</td>
<td>
<form method="post" action="./$zonecgi" style="float:left">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="2b" name="point">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="●" size=30>
</form>
</td>
<td>
<form method="post" action="./$zonecgi" style="float:left">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="2d" name="point">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="☆" size=30>
</form>
</td>
</tr>
<tr>
<td><b><center>AGI</td><td><b><center><img src="$maindir/$imgfile/exp.gif" height="10"><img src="$maindir/$imgfile/mpbar1.gif" width=$agibarcha1 height="8" alt="$strritu％">$agibardmg2<img src="$maindir/$imgfile/exp.gif" height="8"></td><td align=right><b><font color=#$chamoji>$chastats[3] </td>
<td>
<form method="post" action="./$zonecgi" style="float:left">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="3" name="point">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="△" size=30>
</form>
</td>
<td>
<form method="post" action="./$zonecgi" style="float:left">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="3a" name="point">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="▲" size=30>
</form>
</td>
<td>
<form method="post" action="./$zonecgi" style="float:left">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="3c" name="point">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="○" size=30>
</form>
</td>
<td>
<form method="post" action="./$zonecgi" style="float:left">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="3b" name="point">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="●" size=30>
</form>
</td>
<td>
<form method="post" action="./$zonecgi" style="float:left">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="3d" name="point">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="☆" size=30>
</form>
</td>
</tr>
<tr>
<td><b><center>INT</td><td><b><center><img src="$maindir/$imgfile/exp.gif" height="10"><img src="$maindir/$imgfile/mpbar1.gif" width=$intbarcha1 height="8" alt="$strritu％">$intbardmg2<img src="$maindir/$imgfile/exp.gif" height="8"></td><td align=right><b><font color=#$chamoji>$chastats[4] </td>
<td>
<form method="post" action="./$zonecgi" style="float:left">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="4" name="point">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="△" size=30>
</form>
</td>
<td>
<form method="post" action="./$zonecgi" style="float:left">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="4a" name="point">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="▲" size=30>
</form>
</td>
<td>
<form method="post" action="./$zonecgi" style="float:left">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="4c" name="point">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="○" size=30>
</form>
</td>
<td>
<form method="post" action="./$zonecgi" style="float:left">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="4b" name="point">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="●" size=30>
</form>
</td>
<td>
<form method="post" action="./$zonecgi" style="float:left">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="4d" name="point">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="☆" size=30>
</form>
</td>
</tr></table>
HTM
&zoneform;
}

#　魔法使用処理

} elsif ( $in{mahou} eq "1"){
	if ( $champ < 3) {
print <<"HTM";
<b>TP</b>が足りない為、<br>
<b>ヒーリング</b>を使えなかった。
HTM

	} elsif ( $chahp == $chastats[9] ){
print <<"HTM";
<b>既にHPが満タンの為、<br>
ヒーリングを使用しても意味がありません。</b>
HTM
		} else {
$hiru1 = $chastats[0] + $chastats[1]+ $chastats[2]+ $chastats[3]+ $chastats[4]+ $chastats[5]+ $chastats[6]+ $chastats[7];
$hiru2 = $chalvl * 2;
$karikoka = int( $hiru1 / 3 );
$kaihuku = $karikoka + $hiru2;
$kaihuku += int(rand($chalvl));
$chahp += $kaihuku;
$champ -=3;
			if ( $chahp > $chastats[9] ) {
			$chahp = $chastats[9];
			}

print <<"HTM";
<font color=#$chamoji><b>$chaname</b></font>は<b>ヒーリング</b>を唱えた！<br>
<b>HP</b>が<b><font size=+1><font color=#$mojiiro3>$kaihuku</font></font></b>回復した！
HTM
}
&charadatawrt;
&fieldform;

} elsif ( $in{mahou} eq "4"){
	if ( $champ < 7) {
print <<"HTM";
<b>TP</b>が足りない為、<br>
<b>ハイヒーリング</b>を使えなかった。
HTM

	} elsif ( $chahp == $chastats[9] ){
print <<"HTM";
<b>既にHPが満タンの為、<br>
ハイヒーリングを使用しても意味がありません。</b>
HTM

		} else {
$chahp = $chastats[9];
$champ -=7;
			if ( $chahp > $chastats[9] ) {
			$chahp = $chastats[9];
			}

print <<"HTM";
<font color=#$chamoji><b>$chaname</b></font>は<b>ハイヒーリング</b>を唱えた！<br>
<b>HP</b>が<b><font size=+1><font color=#$mojiiro3>全快</font></font></b>した！
HTM
}
&charadatawrt;
&fieldform;

} elsif ( $in{mahou} eq "3"){
	if ( $champ < 4) {
print <<"HTM";
<b>TP</b>が足りない為、<br>
<b>スキップ</b>を使えなかった。
HTM

		} else {
$chacount -=5;
$champ -=4;


print <<"HTM";
<font color=#$chamoji><b>$chaname</b></font>は<b>スキップ</b>の特技を使用した！<br>
辺りからモンスターの気配が消えた！
HTM
}
&charadatawrt;
&fieldform;




} elsif ( $in{mahou} eq "5"){
	if ( $champ < 10) {
print <<"HTM";
<b>TP</b>が足りない為、<br>
<b>パワーアップ</b>を使えなかった。
HTM

} elsif ( $kougekit > 0 ){
print <<"HTM";
<b>既にこの特技は発動しています。<br></b>
HTM
		} else {
$champ -=10;
$kougeki += $chastats[2];
$kougekit = int(rand(5)) + 5;
print <<"HTM";
<font color=#$chamoji><b>$chaname</b></font>は<b>パワーアップ</b>の特技を使用した！<br>
みるみるうちに筋力が増加していく！<br>
<FONT COLOR=GREEN><B>しばらくの間、攻撃力が上昇します。</B></FONT>
HTM
}
&charadatawrt;
&fieldform;


} elsif ( $in{mahou} eq "6"){
	if ( $champ < 10) {
print <<"HTM";
<b>TP</b>が足りない為、<br>
<b>シールドアップ</b>を使えなかった。
HTM

} elsif ( $mamorit > 0 ){
print <<"HTM";
<b>既にこの特技は発動しています。<br></b>
HTM
		} else {
$champ -=10;
$acagari = int($chastats[1] / 4); 
$mamori += $acagari;
$mamorit = int(rand(5)) + 5;
print <<"HTM";
<font color=#$chamoji><b>$chaname</b></font>は<b>シールドアップ</b>の特技を使用した！<br>
みるみるうちに筋力が増加していく！<br>
<FONT COLOR=GREEN><B>しばらくの間、防御力が上昇します。</B></FONT>
HTM
}
&charadatawrt;
&fieldform;


} elsif ( $in{mahou} eq "7"){
	if ( $champ < 20) {
print <<"HTM";
<b>TP</b>が足りない為、<br>
<b>鳳凰の舞</b>を使えなかった。
HTM

} elsif ( $houou > 0 ){
print <<"HTM";
<b>既にこの特技は発動しています。<br></b>
HTM
		} else {
$champ -=20;
$houou = int(rand($chastats[4]) / 2) + 5;
print <<"HTM";
<font color=#$chamoji><b>$chaname</b></font>は<b>鳳凰の舞</b>を使用した！<br>
鳳凰の魂が$chanameの身体に宿った！<br>
<FONT COLOR=GREEN><B>しばらくの間、攻撃回数が１回増えます。</B></FONT>
HTM
}
&charadatawrt;
&fieldform;


} elsif ( $in{mahou} eq "8"){
	if ( $champ < 30) {
print <<"HTM";
<b>TP</b>が足りない為、<br>
<b>リバイブ</b>を使えなかった。
HTM

} elsif ( $ribaibu > 0 ){
print <<"HTM";
<b>この特技の効果は持続しています。<br></b>
HTM
		} else {
$champ -=30;
$ribaibu = int(rand($chastats[4])) + 10;
print <<"HTM";
<font color=#$chamoji><b>$chaname</b></font>は<b>リバイブ</b>を使用した！<br>
聖なる魂が$chanameの身体に宿った！<br>
<FONT COLOR=GREEN><B>一度、死亡しても復活します。</B></FONT>
HTM
}
&charadatawrt;
&fieldform;



} elsif ( $in{mahou} eq "2"){
	if ( $champ < 12) {
print <<"HTM";
<b>TP</b>が足りない為、<br>
<b>テレポート</b>を使えなかった。
HTM

		} else {
$champ -=12;

&charadatawrt;
print <<"HTM";
<font color=#$chamoji><b>$chaname</b></font>は<b>テレポート</b>を唱えた！<br><br>
HTM

$chaplace = 0;
&charadatawrt;
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="0" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="$zone[$itemstats2] へ瞬間移動"><br></td></tr></table>
</form>
HTM
}



} elsif ( $in{useitem} eq "7"){
	if ($flag20 ) {
print <<"HTM";
「使用する特技を選択してください。」<br><br>
<form method="post" action="./$zonecgi">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="71" name="usemahou">
<input type=hidden value="1" name="mahou">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="　ヒーリング　" size=30><font color=red><font size=-1>　<b>消費TP：3</b>（HPを回復）
</form>
HTM
	}

	if ($flag19 ) {
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="71" name="usemahou">
<input type=hidden value="3" name="mahou">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="　 スキップ 　" size=30><font color=red><font size=-1>　<b>消費TP：4</b>（規定戦闘回数を解除）
</form>
HTM
	}

	if ($flag18 ) {
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="71" name="usemahou">
<input type=hidden value="2" name="mahou">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="　テレポート　" size=30><font color=red><font size=-1>　<b>消費TP：12</b>（スパニアートの街へ帰還）
</form>
HTM
	}

	if ($flag17 ) {
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="71" name="usemahou">
<input type=hidden value="4" name="mahou">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="ハイヒーリング" size=30><font color=red><font size=-1>　<b>消費TP：7</b>（HPを全回復）
</form>
HTM
	}

	if ($flag16 ) {
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="71" name="usemahou">
<input type=hidden value="6" name="mahou">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="シールドアップ" size=30><font color=red><font size=-1>　<b>消費TP：10</b>（戦闘時の防御力を上げる）
</form>
HTM
	}

	if ($flag15 ) {
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="71" name="usemahou">
<input type=hidden value="5" name="mahou">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value=" パワーアップ " size=30><font color=red><font size=-1>　<b>消費TP：10</b>（戦闘時の攻撃力を上げる）
</form>
HTM
	}

	if ($flag14 ) {
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="71" name="usemahou">
<input type=hidden value="7" name="mahou">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="　鳳凰の舞　" size=30><font color=red><font size=-1>　<b>消費TP：20</b>（戦闘時の攻撃回数を１回増やす）
</form>
HTM
	}

	if ($flag13 ) {
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="71" name="usemahou">
<input type=hidden value="8" name="mahou">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="　 リバイブ 　" size=30><font color=red><font size=-1>　<b>消費TP：30</b>（１度だけ死亡しても復活）
</form>
HTM
	}

&zoneform;




} elsif ( $in{useitem} eq "3"){
#　ペットの隊列変更処理
print <<"HTM";
ペットの隊列を変更できます。<br>
1番目：プレーヤーより先に行動します。<br>
2番目：プレーヤーの攻撃後に行動します。<br>
3番目：敵の攻撃後に行動します。<br>
<form method="post" action="./$zonecgi">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="31" name="useitem">
<input type=hidden value="$chapass" name="usrpass">
<table border=0><tr><td>
<input type=radio value="0" name="tairetu1" checked>1番目<br>
<input type=radio value="1" name="tairetu1">2番目<br>
<input type=radio value="2" name="tairetu1">3番目<br>
</td><td width=40 align=center><font size=4><b>→</b></font></td><td>
<input type=radio value="0" name="tairetu2" checked>1番目<br>
<input type=radio value="1" name="tairetu2">2番目<br>
<input type=radio value="2" name="tairetu2">3番目<br>
</td></tr></table>
<input type=submit value="隊列を変更する" size=30>
</form>
HTM
&zoneform;
} elsif ( $in{useitem} eq "31"){
$karicode = $petcode[$in{tairetu1}];$karilvl = $petlv[$in{tairetu1}];
$kariname = $petname[$in{tairetu1}];$karikouka = $petkouka[$in{tairetu1}];
$kariritu = $petritu[$in{tairetu1}];$karikouka2 = $petkouka2[$in{tairetu1}];
$karipic = $petpic[$in{tairetu1}];$karieff = $peteff[$in{tairetu1}];
$kariexp = $petexp[$in{tairetu1}];$karinowexp = $petnowexp[$in{tairetu1}];
$petcode[$in{tairetu1}] = $petcode[$in{tairetu2}];
$petlv[$in{tairetu1}] = $petlv[$in{tairetu2}];
$petname[$in{tairetu1}] = $petname[$in{tairetu2}];
$petritu[$in{tairetu1}] = $petritu[$in{tairetu2}];
$petkouka[$in{tairetu1}] = $petkouka[$in{tairetu2}];
$petkouka2[$in{tairetu1}] = $petkouka2[$in{tairetu2}];
$petpic[$in{tairetu1}] = $petpic[$in{tairetu2}];
$peteff[$in{tairetu1}] = $peteff[$in{tairetu2}];
$petexp[$in{tairetu1}] = $petexp[$in{tairetu2}];
$petnowexp[$in{tairetu1}] = $petnowexp[$in{tairetu2}];
$petcode[$in{tairetu2}] = $karicode;$petlv[$in{tairetu2}] = $karilvl;
$petname[$in{tairetu2}] = $kariname;$petritu[$in{tairetu2}] = $kariritu;
$petkouka[$in{tairetu2}] = $karikouka;$petkouka2[$in{tairetu2}] = $karikouka2;
$petpic[$in{tairetu2}] = $karipic;$peteff[$in{tairetu2}] = $karieff;
$petexp[$in{tairetu2}] = $kariexp;$petnowexp[$in{tairetu2}] = $karinowexp;
print "<b>隊列を変更しました。</b><br><br>";
&charadatawrt;
&fieldform;





} else {
&fieldform;
}




#　カウントダウン処理
sub fieldform {
	if ( $chacount == 5 || $in{useitem} eq "1a" || $in{useitem} eq "2a" || $in{useitem} eq "31") {
		$timesa = $nexttime;
	}
print <<"HTM";
<SCRIPT LANGUAGE="JavaScript">
<!--
	var start=new Date();
	start=Date.parse(start)/1000;
	var counts=$nexttime;
	function CountDown(){
		var now=new Date();
		now=Date.parse(now)/1000;
		var x=parseInt(counts-(now-start),10);
		if(document.form1){document.form1.clock.value = x;}
		if(x>0){
			timerID=setTimeout("CountDown()", 100)
		}else{
			document.form1.clock.value = "0K!";
		}
	}
//-->
</SCRIPT>
<FORM NAME="form1"><INPUT TYPE="text" NAME="clock" SIZE="2" VALUE="$timesa" style="color: white;background-color: dimgray;border-color: black;"></form>
HTM


	if ($newtegami > 0) {


}

		if ( $champ <= 0) {
print <<"HTM";
<font color=red><font size=-1><b>(!警告!）</b><br>TPが0になっています！<br>
<nobr>このまま戦闘をすると、<br>HPが減少します！</font></font><br><br>
HTM
}



		if ( $chahp <= $autop && $bpo == "1" && $potion eq "ポーション" && $chaitem[1] eq "ポーション" ) {
$chahp += 100;
$bpo = "0";
	if ( $chaeff[1] == 1 ) { $chaitem[1] = $chaeff[1] = $chasetumei[1] = "";
	} else { $chaeff[1] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>ポーションを使用しました。<br>
ポーションは、残り 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[1]</font></font></b> <font color=black>個です。</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "ポーション" && $chaitem[2] eq "ポーション" ) {
$chahp += 100;
$bpo = "0";
	if ( $chaeff[2] == 1 ) { $chaitem[2] = $chaeff[2] = $chasetumei[2] = "";
	} else { $chaeff[2] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>ポーションを使用しました。<br>
ポーションは、残り 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[2]</font></font></b> <font color=black>個です。</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "ポーション" && $chaitem[3] eq "ポーション" ) {
$chahp += 100;
$bpo = "0";
	if ( $chaeff[3] == 1 ) { $chaitem[3] = $chaeff[3] = $chasetumei[3] = "";
	} else { $chaeff[3] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>ポーションを使用しました。<br>
ポーションは、残り 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[3]</font></font></b> <font color=black>個です。</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "ポーション" && $chaitem[4] eq "ポーション" ) {
$chahp += 100;
$bpo = "0";
	if ( $chaeff[4] == 1 ) { $chaitem[4] = $chaeff[4] = $chasetumei[4] = "";
	} else { $chaeff[4] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>ポーションを使用しました。<br>
ポーションは、残り 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[4]</font></font></b> <font color=black>個です。</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "ポーション" && $chaitem[5] eq "ポーション" ) {
$chahp += 100;
$bpo = "0";
	if ( $chaeff[5] == 1 ) { $chaitem[5] = $chaeff[5] = $chasetumei[5] = "";
	} else { $chaeff[5] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>ポーションを使用しました。<br>
ポーションは、残り 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[5]</font></font></b> <font color=black>個です。</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "ポーション" && $chaitem[6] eq "ポーション" ) {
$chahp += 100;
$bpo = "0";
	if ( $chaeff[6] == 1 ) { $chaitem[6] = $chaeff[6] = $chasetumei[6] = "";
	} else { $chaeff[6] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>ポーションを使用しました。<br>
ポーションは、残り 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[6]</font></font></b> <font color=black>個です。</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "ポーション" && $chaitem[7] eq "ポーション" ) {
$chahp += 100;
$bpo = "0";
	if ( $chaeff[7] == 1 ) { $chaitem[7] = $chaeff[7] = $chasetumei[7] = "";
	} else { $chaeff[7] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>ポーションを使用しました。<br>
ポーションは、残り 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[7]</font></font></b> <font color=black>個です。</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "ポーション" && $chaitem[8] eq "ポーション" ) {
$chahp += 100;
$bpo = "0";
	if ( $chaeff[8] == 1 ) { $chaitem[8] = $chaeff[8] = $chasetumei[8] = "";
	} else { $chaeff[8] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>ポーションを使用しました。<br>
ポーションは、残り 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[8]</font></font></b> <font color=black>個です。</font></font>
</font><br><br>
HTM
&charadatawrt;
}



		if ( $chahp <= $autop && $bpo == "1" && $potion eq "ミドルポーション" && $chaitem[1] eq "ミドルポーション" ) {
$chahp += 300;
$bpo = "0";
	if ( $chaeff[1] == 1 ) { $chaitem[1] = $chaeff[1] = $chasetumei[1] = "";
	} else { $chaeff[1] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>ミドルポーションを使用しました。<br>
ミドルポーションは、残り 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[1]</font></font></b> <font color=black>個です。</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "ミドルポーション" && $chaitem[2] eq "ミドルポーション" ) {
$chahp += 300;
$bpo = "0";
	if ( $chaeff[2] == 1 ) { $chaitem[2] = $chaeff[2] = $chasetumei[2] = "";
	} else { $chaeff[2] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>ミドルポーションを使用しました。<br>
ミドルポーションは、残り 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[2]</font></font></b> <font color=black>個です。</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "ミドルポーション" && $chaitem[3] eq "ミドルポーション" ) {
$chahp += 300;
$bpo = "0";
	if ( $chaeff[3] == 1 ) { $chaitem[3] = $chaeff[3] = $chasetumei[3] = "";
	} else { $chaeff[3] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>ミドルポーションを使用しました。<br>
ミドルポーションは、残り 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[3]</font></font></b> <font color=black>個です。</font></font>
</font><br><br>
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "ミドルポーション" && $chaitem[4] eq "ミドルポーション" ) {
$chahp += 300;
$bpo = "0";
	if ( $chaeff[4] == 1 ) { $chaitem[4] = $chaeff[4] = $chasetumei[4] = "";
	} else { $chaeff[4] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>ミドルポーションを使用しました。<br>
ミドルポーションは、残り 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[4]</font></font></b> <font color=black>個です。</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "ミドルポーション" && $chaitem[5] eq "ミドルポーション" ) {
$chahp += 300;
$bpo = "0";
	if ( $chaeff[5] == 1 ) { $chaitem[5] = $chaeff[5] = $chasetumei[5] = "";
	} else { $chaeff[5] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>ミドルポーションを使用しました。<br>
ミドルポーションは、残り 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[5]</font></font></b> <font color=black>個です。</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "ミドルポーション" && $chaitem[6] eq "ミドルポーション" ) {
$chahp += 300;
$bpo = "0";
	if ( $chaeff[6] == 1 ) { $chaitem[6] = $chaeff[6] = $chasetumei[6] = "";
	} else { $chaeff[6] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>ミドルポーションを使用しました。<br>
ミドルポーションは、残り 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[6]</font></font></b> <font color=black>個です。</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "ミドルポーション" && $chaitem[7] eq "ミドルポーション" ) {
$chahp += 300;
$bpo = "0";
	if ( $chaeff[7] == 1 ) { $chaitem[7] = $chaeff[7] = $chasetumei[7] = "";
	} else { $chaeff[7] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>ミドルポーションを使用しました。<br>
ミドルポーションは、残り 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[7]</font></font></b> <font color=black>個です。</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "ミドルポーション" && $chaitem[8] eq "ミドルポーション" ) {
$chahp += 300;
$bpo = "0";
	if ( $chaeff[8] == 1 ) { $chaitem[8] = $chaeff[8] = $chasetumei[8] = "";
	} else { $chaeff[8] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>ミドルポーションを使用しました。<br>
ミドルポーションは、残り 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[8]</font></font></b> <font color=black>個です。</font></font>
</font><br><br>
HTM
&charadatawrt;
}


		if ( $chahp <= $autop && $bpo == "1" && $potion eq "ハイポーション" && $chaitem[1] eq "ハイポーション" ) {
$chahp += 700;
$bpo = "0";
	if ( $chaeff[1] == 1 ) { $chaitem[1] = $chaeff[1] = $chasetumei[1] = "";
	} else { $chaeff[1] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>ハイポーションを使用しました。<br>
ハイポーションは、残り 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[1]</font></font></b> <font color=black>個です。</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "ハイポーション" && $chaitem[2] eq "ハイポーション" ) {
$chahp += 700;
$bpo = "0";
	if ( $chaeff[2] == 1 ) { $chaitem[2] = $chaeff[2] = $chasetumei[2] = "";
	} else { $chaeff[2] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>ハイポーションを使用しました。<br>
ハイポーションは、残り 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[2]</font></font></b> <font color=black>個です。</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "ハイポーション" && $chaitem[3] eq "ハイポーション" ) {
$chahp += 700;
$bpo = "0";
	if ( $chaeff[3] == 1 ) { $chaitem[3] = $chaeff[3] = $chasetumei[3] = "";
	} else { $chaeff[3] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>ハイポーションを使用しました。<br>
ハイポーションは、残り 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[3]</font></font></b> <font color=black>個です。</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "ハイポーション" && $chaitem[4] eq "ハイポーション" ) {
$chahp += 700;
$bpo = "0";
	if ( $chaeff[4] == 1 ) { $chaitem[4] = $chaeff[4] = $chasetumei[4] = "";
	} else { $chaeff[4] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>ハイポーションを使用しました。<br>
ハイポーションは、残り 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[4]</font></font></b> <font color=black>個です。</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "ハイポーション" && $chaitem[5] eq "ハイポーション" ) {
$chahp += 700;
$bpo = "0";
	if ( $chaeff[5] == 1 ) { $chaitem[5] = $chaeff[5] = $chasetumei[5] = "";
	} else { $chaeff[5] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>ハイポーションを使用しました。<br>
ハイポーションは、残り 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[5]</font></font></b> <font color=black>個です。</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "ハイポーション" && $chaitem[6] eq "ハイポーション" ) {
$chahp += 700;
$bpo = "0";
	if ( $chaeff[6] == 1 ) { $chaitem[6] = $chaeff[6] = $chasetumei[6] = "";
	} else { $chaeff[6] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>ハイポーションを使用しました。<br>
ハイポーションは、残り 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[6]</font></font></b> <font color=black>個です。</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "ハイポーション" && $chaitem[7] eq "ハイポーション" ) {
$chahp += 700;
$bpo = "0";
	if ( $chaeff[7] == 1 ) { $chaitem[7] = $chaeff[7] = $chasetumei[7] = "";
	} else { $chaeff[7] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>ハイポーションを使用しました。<br>
ハイポーションは、残り 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[7]</font></font></b> <font color=black>個です。</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "ハイポーション" && $chaitem[8] eq "ハイポーション" ) {
$chahp += 700;
$bpo = "0";
	if ( $chaeff[8] == 1 ) { $chaitem[8] = $chaeff[8] = $chasetumei[8] = "";
	} else { $chaeff[8] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>ハイポーションを使用しました。<br>
ハイポーションは、残り 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[8]</font></font></b> <font color=black>個です。</font></font>
</font><br><br>
HTM
&charadatawrt;
}


		if ( $chahp <= $autop && $bpo == "1" && $potion eq "エクスポーション" && $chaitem[1] eq "エクスポーション" ) {
$chahp += 1200;
$bpo = "0";
	if ( $chaeff[1] == 1 ) { $chaitem[1] = $chaeff[1] = $chasetumei[1] = "";
	} else { $chaeff[1] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>エクスポーションを使用しました。<br>
エクスポーションは、残り 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[1]</font></font></b> <font color=black>個です。</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "エクスポーション" && $chaitem[2] eq "エクスポーション" ) {
$chahp += 1200;
$bpo = "0";
	if ( $chaeff[2] == 1 ) { $chaitem[2] = $chaeff[2] = $chasetumei[2] = "";
	} else { $chaeff[2] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>エクスポーションを使用しました。<br>
エクスポーションは、残り 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[2]</font></font></b> <font color=black>個です。</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "エクスポーション" && $chaitem[3] eq "エクスポーション" ) {
$chahp += 1200;
$bpo = "0";
	if ( $chaeff[3] == 1 ) { $chaitem[3] = $chaeff[3] = $chasetumei[3] = "";
	} else { $chaeff[3] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>エクスポーションを使用しました。<br>
エクスポーションは、残り 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[3]</font></font></b> <font color=black>個です。</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "エクスポーション" && $chaitem[4] eq "エクスポーション" ) {
$chahp += 1200;
$bpo = "0";
	if ( $chaeff[4] == 1 ) { $chaitem[4] = $chaeff[4] = $chasetumei[4] = "";
	} else { $chaeff[4] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>エクスポーションを使用しました。<br>
エクスポーションは、残り 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[4]</font></font></b> <font color=black>個です。</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "エクスポーション" && $chaitem[5] eq "エクスポーション" ) {
$chahp += 1200;
$bpo = "0";
	if ( $chaeff[5] == 1 ) { $chaitem[5] = $chaeff[5] = $chasetumei[5] = "";
	} else { $chaeff[5] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>エクスポーションを使用しました。<br>
エクスポーションは、残り 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[5]</font></font></b> <font color=black>個です。</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "エクスポーション" && $chaitem[6] eq "エクスポーション" ) {
$chahp += 1200;
$bpo = "0";
	if ( $chaeff[6] == 1 ) { $chaitem[6] = $chaeff[6] = $chasetumei[6] = "";
	} else { $chaeff[6] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>エクスポーションを使用しました。<br>
エクスポーションは、残り 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[6]</font></font></b> <font color=black>個です。</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "エクスポーション" && $chaitem[7] eq "エクスポーション" ) {
$chahp += 1200;
$bpo = "0";
	if ( $chaeff[7] == 1 ) { $chaitem[7] = $chaeff[7] = $chasetumei[7] = "";
	} else { $chaeff[7] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>エクスポーションを使用しました。<br>
エクスポーションは、残り 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[7]</font></font></b> <font color=black>個です。</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "エクスポーション" && $chaitem[8] eq "エクスポーション" ) {
$chahp += 1200;
$bpo = "0";
	if ( $chaeff[8] == 1 ) { $chaitem[8] = $chaeff[8] = $chasetumei[8] = "";
	} else { $chaeff[8] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>エクスポーションを使用しました。<br>
エクスポーションは、残り 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[8]</font></font></b> <font color=black>個です。</font></font>
</font><br><br>
HTM
&charadatawrt;
}



		if ( $chahp <= $autop && $bpo == "1" && $potion eq "メガエリクサー" && $chaitem[1] eq "メガエリクサー" ) {
$chahp += 1800;
$bpo = "0";
	if ( $chaeff[1] == 1 ) { $chaitem[1] = $chaeff[1] = $chasetumei[1] = "";
	} else { $chaeff[1] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>メガエリクサーを使用しました。<br>
メガエリクサーは、残り 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[1]</font></font></b> <font color=black>個です。</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "メガエリクサー" && $chaitem[2] eq "メガエリクサー" ) {
$chahp += 1800;
$bpo = "0";
	if ( $chaeff[2] == 1 ) { $chaitem[2] = $chaeff[2] = $chasetumei[2] = "";
	} else { $chaeff[2] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>メガエリクサーを使用しました。<br>
メガエリクサーは、残り 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[2]</font></font></b> <font color=black>個です。</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "メガエリクサー" && $chaitem[3] eq "メガエリクサー" ) {
$chahp += 1800;
$bpo = "0";
	if ( $chaeff[3] == 1 ) { $chaitem[3] = $chaeff[3] = $chasetumei[3] = "";
	} else { $chaeff[3] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>メガエリクサーを使用しました。<br>
メガエリクサーは、残り 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[3]</font></font></b> <font color=black>個です。</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "メガエリクサー" && $chaitem[4] eq "メガエリクサー" ) {
$chahp += 1800;
$bpo = "0";
	if ( $chaeff[4] == 1 ) { $chaitem[4] = $chaeff[4] = $chasetumei[4] = "";
	} else { $chaeff[4] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>メガエリクサーを使用しました。<br>
メガエリクサーは、残り 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[4]</font></font></b> <font color=black>個です。</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "メガエリクサー" && $chaitem[5] eq "メガエリクサー" ) {
$chahp += 1800;
$bpo = "0";
	if ( $chaeff[5] == 1 ) { $chaitem[5] = $chaeff[5] = $chasetumei[5] = "";
	} else { $chaeff[5] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>メガエリクサーを使用しました。<br>
メガエリクサーは、残り 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[5]</font></font></b> <font color=black>個です。</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "メガエリクサー" && $chaitem[6] eq "メガエリクサー" ) {
$chahp += 1800;
$bpo = "0";
	if ( $chaeff[6] == 1 ) { $chaitem[6] = $chaeff[6] = $chasetumei[6] = "";
	} else { $chaeff[6] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>メガエリクサーを使用しました。<br>
メガエリクサーは、残り 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[6]</font></font></b> <font color=black>個です。</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "メガエリクサー" && $chaitem[7] eq "メガエリクサー" ) {
$chahp += 1800;
$bpo = "0";
	if ( $chaeff[7] == 1 ) { $chaitem[7] = $chaeff[7] = $chasetumei[7] = "";
	} else { $chaeff[7] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>メガエリクサーを使用しました。<br>
メガエリクサーは、残り 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[7]</font></font></b> <font color=black>個です。</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "メガエリクサー" && $chaitem[8] eq "メガエリクサー" ) {
$chahp += 1800;
$bpo = "0";
	if ( $chaeff[8] == 1 ) { $chaitem[8] = $chaeff[8] = $chasetumei[8] = "";
	} else { $chaeff[8] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>メガエリクサーを使用しました。<br>
メガエリクサーは、残り 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[8]</font></font></b> <font color=black>個です。</font></font>
</font><br><br>
HTM
&charadatawrt;
}


		if ( $chahp <= $autop && $bpo == "1" && $potion eq "ギガエリクサー" && $chaitem[1] eq "ギガエリクサー" ) {
$chahp += 2400;
$bpo = "0";
	if ( $chaeff[1] == 1 ) { $chaitem[1] = $chaeff[1] = $chasetumei[1] = "";
	} else { $chaeff[1] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>ギガエリクサーを使用しました。<br>
ギガエリクサーは、残り 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[1]</font></font></b> <font color=black>個です。</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "ギガエリクサー" && $chaitem[2] eq "ギガエリクサー" ) {
$chahp += 2400;
$bpo = "0";
	if ( $chaeff[2] == 1 ) { $chaitem[2] = $chaeff[2] = $chasetumei[2] = "";
	} else { $chaeff[2] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>ギガエリクサーを使用しました。<br>
ギガエリクサーは、残り 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[2]</font></font></b> <font color=black>個です。</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "ギガエリクサー" && $chaitem[3] eq "ギガエリクサー" ) {
$chahp += 2400;
$bpo = "0";
	if ( $chaeff[3] == 1 ) { $chaitem[3] = $chaeff[3] = $chasetumei[3] = "";
	} else { $chaeff[3] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>ギガエリクサーを使用しました。<br>
ギガエリクサーは、残り 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[3]</font></font></b> <font color=black>個です。</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "ギガエリクサー" && $chaitem[4] eq "ギガエリクサー" ) {
$chahp += 2400;
$bpo = "0";
	if ( $chaeff[4] == 1 ) { $chaitem[4] = $chaeff[4] = $chasetumei[4] = "";
	} else { $chaeff[4] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>ギガエリクサーを使用しました。<br>
ギガエリクサーは、残り 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[4]</font></font></b> <font color=black>個です。</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "ギガエリクサー" && $chaitem[5] eq "ギガエリクサー" ) {
$chahp += 2400;
$bpo = "0";
	if ( $chaeff[5] == 1 ) { $chaitem[5] = $chaeff[5] = $chasetumei[5] = "";
	} else { $chaeff[5] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>ギガエリクサーを使用しました。<br>
ギガエリクサーは、残り 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[5]</font></font></b> <font color=black>個です。</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "ギガエリクサー" && $chaitem[6] eq "ギガエリクサー" ) {
$chahp += 2400;
$bpo = "0";
	if ( $chaeff[6] == 1 ) { $chaitem[6] = $chaeff[6] = $chasetumei[6] = "";
	} else { $chaeff[6] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>ギガエリクサーを使用しました。<br>
ギガエリクサーは、残り 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[6]</font></font></b> <font color=black>個です。</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "ギガエリクサー" && $chaitem[7] eq "ギガエリクサー" ) {
$chahp += 2400;
$bpo = "0";
	if ( $chaeff[7] == 1 ) { $chaitem[7] = $chaeff[7] = $chasetumei[7] = "";
	} else { $chaeff[7] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>ギガエリクサーを使用しました。<br>
ギガエリクサーは、残り 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[7]</font></font></b> <font color=black>個です。</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "ギガエリクサー" && $chaitem[8] eq "ギガエリクサー" ) {
$chahp += 2400;
$bpo = "0";
	if ( $chaeff[8] == 1 ) { $chaitem[8] = $chaeff[8] = $chasetumei[8] = "";
	} else { $chaeff[8] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>ギガエリクサーを使用しました。<br>
ギガエリクサーは、残り 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[8]</font></font></b> <font color=black>個です。</font></font>
</font><br><br>
HTM
&charadatawrt;
}


		if ( $chahp <= $autop && $bpo == "1" && $potion eq "テラエリクサー" && $chaitem[1] eq "テラエリクサー" ) {
$chahp += 3000;
$bpo = "0";
	if ( $chaeff[1] == 1 ) { $chaitem[1] = $chaeff[1] = $chasetumei[1] = "";
	} else { $chaeff[1] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>テラエリクサーを使用しました。<br>
テラエリクサーは、残り 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[1]</font></font></b> <font color=black>個です。</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "テラエリクサー" && $chaitem[2] eq "テラエリクサー" ) {
$chahp += 3000;
$bpo = "0";
	if ( $chaeff[2] == 1 ) { $chaitem[2] = $chaeff[2] = $chasetumei[2] = "";
	} else { $chaeff[2] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>テラエリクサーを使用しました。<br>
テラエリクサーは、残り 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[2]</font></font></b> <font color=black>個です。</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "テラエリクサー" && $chaitem[3] eq "テラエリクサー" ) {
$chahp += 3000;
$bpo = "0";
	if ( $chaeff[3] == 1 ) { $chaitem[3] = $chaeff[3] = $chasetumei[3] = "";
	} else { $chaeff[3] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>テラエリクサーを使用しました。<br>
テラエリクサーは、残り 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[3]</font></font></b> <font color=black>個です。</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "テラエリクサー" && $chaitem[4] eq "テラエリクサー" ) {
$chahp += 3000;
$bpo = "0";
	if ( $chaeff[4] == 1 ) { $chaitem[4] = $chaeff[4] = $chasetumei[4] = "";
	} else { $chaeff[4] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>テラエリクサーを使用しました。<br>
テラエリクサーは、残り 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[4]</font></font></b> <font color=black>個です。</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "テラエリクサー" && $chaitem[5] eq "テラエリクサー" ) {
$chahp += 3000;
$bpo = "0";
	if ( $chaeff[5] == 1 ) { $chaitem[5] = $chaeff[5] = $chasetumei[5] = "";
	} else { $chaeff[5] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>テラエリクサーを使用しました。<br>
テラエリクサーは、残り 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[5]</font></font></b> <font color=black>個です。</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "テラエリクサー" && $chaitem[6] eq "テラエリクサー" ) {
$chahp += 3000;
$bpo = "0";
	if ( $chaeff[6] == 1 ) { $chaitem[6] = $chaeff[6] = $chasetumei[6] = "";
	} else { $chaeff[6] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>テラエリクサーを使用しました。<br>
テラエリクサーは、残り 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[6]</font></font></b> <font color=black>個です。</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "テラエリクサー" && $chaitem[7] eq "テラエリクサー" ) {
$chahp += 3000;
$bpo = "0";
	if ( $chaeff[7] == 1 ) { $chaitem[7] = $chaeff[7] = $chasetumei[7] = "";
	} else { $chaeff[7] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>テラエリクサーを使用しました。<br>
テラエリクサーは、残り 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[7]</font></font></b> <font color=black>個です。</font></font>
</font><br><br>
HTM
&charadatawrt;
}
		if ( $chahp <= $autop && $bpo == "1" && $potion eq "テラエリクサー" && $chaitem[8] eq "テラエリクサー" ) {
$chahp += 3000;
$bpo = "0";
	if ( $chaeff[8] == 1 ) { $chaitem[8] = $chaeff[8] = $chasetumei[8] = "";
	} else { $chaeff[8] --; }
	if ( $chahp > $chastats[9] ) { $chahp = $chastats[9]; }
print <<"HTM";
<font size=3><b><FONT FACE="Times New Roman"><font color=#F20000>-<font color=#F20000>A<font color=#E80000>u<font color=#DB0000>t<font color=#C80000>o <font color=#F20000>P<font color=#E80000>o<font color=#DB0000>t<font color=#C80000>i<font color=#B30000>o<font color=#990000>n-</font><br></b><font size=-2>
<font color=black>テラエリクサーを使用しました。<br>
テラエリクサーは、残り 
<font size=+1><b><FONT FACE="Times New Roman">
</font><font color=#990000>$chaeff[8]</font></font></b> <font color=black>個です。</font></font>
</font><br><br>
HTM
&charadatawrt;
}


print <<"HTM";
<form method="post" action="./$battlecgi">
<onClick="window.location.replace>
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=hidden value="$chacount" name="count">
<input type=submit value="　　　索　敵　　　" size=30 onClick="this.disabled=true; this.value='       索  敵       '; this.form.submit();">
</form>

<form method="post" action="./$zonecgi">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="1" name="useitem">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="アイテムを使用する" size=30 onClick="this.disabled=true; this.value='アイテムを使用する'; this.form.submit();">
</form>
HTM

	if ($flag20 ) {
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="7" name="useitem">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="　特技を使用する　" size=30 onClick="this.disabled=true; this.value='  特技を使用する  '; this.form.submit();">
</form>
HTM
}

print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="6" name="useitem">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="アイテムを装備する" size=30 onClick="this.disabled=true; this.value='アイテムを装備する'; this.form.submit();">
</form>

</td></tr></table></td><td width=30></td><td>
HTM


sub kouji {
open(NOW,">$maindir/kouji$bousikts");
flock(NOW,2);
	$ttt = 0;
	while ( $ttt < 50 ) {
		print NOW $res[$ttt] ;
		$ttt ++;
	}
flock(NOW,8);
close(NOW);
}



	if ( $chacount <= 0 ) {
print "次のゾーンへ移動可\能\です。<br>";

@movin = split(/\//,$move[$chaplace]);

		foreach $moved (@movin) {
			if ( $moved ne "" ) {
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="$moved" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="$zone[$moved]　へ" size=30 onClick="this.disabled=true; this.value='お待ちください'; this.form.submit();">
</form>
HTM
			}
		}
	} else {
print "あと <b><font size=7 color=#$mojiiro3>$chacount</font> 回 </b><br>　の戦闘をすると移動可\能\です。";
	}



}



print <<"HTM";
</td></tr></table><br><hr>
HTM

if ( $in{useitem} eq "1" || $in{useitem} eq "2" || $in{useitem} eq "3" || $in{useitem} eq "6" ||  $in{useitem} eq "21" || $in{riyou} eq "4" || $in{useitem} eq "7" || $in{useitem} eq "8" || $in{point} eq "1" || $in{point} eq "1a" || $in{point} eq "2" || $in{point} eq "2a" || $in{point} eq "3" || $in{point} eq "3a" || $in{point} eq "4" || $in{point} eq "4a" || $in{point} eq "3b" || $in{point} eq "2b" || $in{point} eq "1b" || $in{point} eq "4b" || $in{point} eq "1c" || $in{point} eq "1d" || $in{point} eq "2c" || $in{point} eq "2d" || $in{point} eq "3c" || $in{point} eq "3d" || $in{point} eq "4c" || $in{point} eq "4d" || $in{riyou} eq "61") { &itemtable;
} else {
print <<"HTM";
<SCRIPT language="JavaScript">
<!--
window.setTimeout('CountDown()',100);
//-->
</SCRIPT>
HTM
}
&pettukitable;









############################################

$playingkazu = @playing;
print <<"HTM";


<form method="post" action="./bar.cgi" target="sakaba">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value=" チャット ">
<br></form>
HTM




require "./settei.cgi";
print <<"HTM";

<center><font size=4 color=#$mojiiro4><b><A NAME="end">手紙 一覧</a></b></font><br>
(保持期間が3日間、あるいは保持件数が30件をこえると自動消去されます)$tegamicount
<table border=0 width=70%><tr><td>
HTM
$tegamicount = 0;
open(BAN,">>$maindir/$foldacha/tegami2_$chaid.tmp");
flock(BAN,2);
	open(BANN,"$maindir/$foldacha/tegami_$chaid$bousi2cha$bousikts");
		while ( $yuubin = <BANN> ) {
			if ( $tegamicount > 29 ) { last; }
($kako,$chanamez,$chamojiz,$tegami,$genzai2) = split(/\t/,$yuubin);
			if ( $now < $kako + (3*24*60*60) ) {

print "<hr><font color=#$chamojiz><b>$chanamez</b></font> ： $tegami <nobr>($genzai2)</nobr>\n";
		print BAN "$yuubin";
			}
$tegamicount ++;

		}
	close(BANN);

flock(BAN,8);
close(BAN);

rename("$maindir/$foldacha/tegami2_$chaid.tmp","$maindir/$foldacha/tegami_$chaid$bousi2cha$bousikts");


################################################

sub zoneform {
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="  ゾーン画面へ戻る  " onClick="this.disabled=true; this.value='  ゾーン画面へ戻る  '; this.form.submit();"><br></td></tr></table>
</form>
HTM
}



1;