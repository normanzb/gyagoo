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

if ( $mente == 1 ){
&mente;
}

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
<td align=right><nobr><font size=6 color=#$mojiiro2><b></b></font></nobr></td><td width=30></td><td><nobr>
現在の冒険者（$playingkazu人）/
HTM
$chastats[11] = 0;
foreach $playnow ( @playing ) {
	chop($playnow);
	($nowid,$nowname) = split(/\//,$playnow);
print " <a href=\"./$introcgi?usrid=$nowid\" target=\"intro\"><b>$nowname</b></a> /<wbr>";

}
$bpo = "0";
$chastats[11] = 0;
&charadatawrt;
$timesa = $chajikan - $now + $nexttime;

print <<"HTM";
<wbr></nobr></tr></table><br><hr>
<br>

</td></tr></table>
</td><td width=10></td><td>
<table border=0><tr><td colspan=3>
HTM

$chastats[11] = 0;
$ryoukin1 = ( $chalvl ) * 3;
$ryoukin2 = ( $chastats[16] - $champ ) * 1;
$ryoukin = $ryoukin1 + $ryoukin2;
$tugilvl = $chanextlvl - $chaexp;

if ($jobexpnow[$chaclass] == $jobexp[$chaclass]){ $mas ="<center><font color=red><font size=-2>- MASTER! -</font></font></center>"; }
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
                ・<A HREF="http://gyagoo.mine.nu/gyagoo/wforum/wforum.cgi" target="blank">掲示板</a>
                ・<a href="javascript:close()">ゲーム終了</a><br><hr>
                <b> 福引券： <font color=#$chamoji>$hukubiki</b></font><font size=-1><b>枚</b></font><br><hr>
                <b> 魅力（CHA）　：<font color=#$chamoji>$chastats[5]</b></font> + <b><font color=palevioletred>$karistats[5]</font></b><br>
                <b> 火耐性（SVF）：<font color=#$chamoji>$chastats[6]</b></font> + <b><font color=palevioletred>$karistats[6]</font></b><br>
                <b> 水耐性（SVC）：<font color=#$chamoji>$chastats[7]</b></font> + <b><font color=palevioletred>$karistats[7]</font></b><br>
                <b> 魔耐性（SVM）：<font color=#$chamoji>$chastats[8]</b></font> + <b><font color=palevioletred>$karistats[8]</font></b><br><hr>
                <font size=-1><b>熟練度【$job[$chaclass]】   <font color=palevioletred>$jobritu2</font><font size=-2></font></b></font><br>
<img src="$maindir/$imgfile/exp.gif" height="10"><img src="$maindir/$imgfile/jobbar1.gif" width=$jobbarcha1 height="8">$hpbardmg3<img src="$maindir/$imgfile/exp.gif" height="8"><br><hr>
                <b> 現在の報酬：<font color=blue>$chastats[13]</font>Ｇ<br>
                 現在の宿代：<font color=red>$ryoukin</font>Ｇ<br><hr>

                <font size=-1> 次のLvまで</font><font color=#$chamoji>$tugilvl</font><font size=-1>EXP</font></b>
            </TD>
        </TR>
    </TABLE>
</DIV>
<!--メニュー用タグここまで-->
HTM



$sisetu[1] = " 冒険者ギルド ";
$sisetu[2] = " 宿屋 ";
$sisetu[3] = " 雑貨屋 ";
$sisetu[4] = " ペット小屋 ";
$sisetu[5] = " 研究所 ";
$sisetu[6] = " 寺院 ";
$sisetu[7] = " 長老の家 ";
$sisetu[8] = " 電子掲示板 ";
$sisetu[9] = " 電子酒場 ";
$sisetu[10] = " 郵便局 ";
$sisetu[11] = " 生成屋 ";
$sisetu[12] = " 教会 ";
$sisetu[13] = " 肉\体\強\化\場 ";
$sisetu[14] = " ﾘｻｲｸﾙBOX ";
$sisetu[15] = " 福引所 ";
$sisetu[16] = "生贄合体の館";
$sisetu[17] = "コールド";
@omosa = ("","軽量","中量","重量");
@bui = ("道具","右手","左手","頭","胸","脚","腕","指","首");

################################

if ( $in{sisetu} eq "1"){
require "./$bankcgi";
} elsif ( $in{sisetu} eq "2"){
&topsisetu;
$ryoukin1 = ( $chalvl ) * 3;
$ryoukin2 = ( $chastats[16] - $champ ) * 1;
$ryoukin = $ryoukin1 + $ryoukin2;
	if ( $in{riyou} eq "1"){
		if ( $chagold < $ryoukin) {
print <<"HTM";
あらら～、お金が足りないようですね♪<br>
さっさと帰りなっ！！
HTM
&townmodori;
		} else {
$chagold -= $ryoukin;
$chahp = $chastats[9];
$champ = $chastats[16];
print <<"HTM";
<nobr><b><font size=5 color=#$mojiiro2><font color=#$chamoji>$chaname</font> は全快した！</font></b><br><br>
</nobr>ご利用ありがとうございました～。<br>
またのおこしをお待ちしております♪<br>
HTM
&charadatawrt;
&townmodori;
		}
	} else {
print <<"HTM";
いらっしゃいませ～♪<br>
<nobr>ここは傷ついた旅人達の安らぎの場所です。</nobr><br><br>
HTM
		if ( $chastats[9] eq $chahp && $chastats[16] eq $champ ){

print <<"HTM";
$chaname様はすでに元気いっぱいのようですね♪<br>
またのおこしをお待ちしておりま～す。<br>
HTM
&townmodori;
		} else {
print <<"HTM";
<font color=#$chamoji><b>$chaname</b></font> 様は一泊「<b><font color=#$mojiiro3>$ryoukin</b></font>」G です♪<br>
お泊りになられますか？<br><br></td><td>
<form method="post" action="./$zonecgi">
<input type=hidden value="2" name="sisetu">
<input type=hidden value="1" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="     宿泊する     " onClick="this.disabled=true; this.value='     宿泊する     '; this.form.submit();">
</form><br>
HTM
&townmodori;

}

	}





} elsif ( $in{sisetu} eq "3"){
require "./$shopcgi";
} elsif ( $in{sisetu} eq "4"){
require "./$koyacgi";
} elsif ( $in{sisetu} eq "5"){
require "./$kenkyucgi";
} elsif ( $in{sisetu} eq "6"){
require "./$jiincgi";
} elsif ( $in{sisetu} eq "7"){
require "./$tyouroucgi";
} elsif ( $in{sisetu} eq "10"){
require "./$yuubincgi";
} elsif ( $in{sisetu} eq "11"){
require "./$shop2cgi";
} elsif ( $in{sisetu} eq "12"){
require "./kunren.cgi";
} elsif ( $in{sisetu} eq "13"){
require "./kojin.cgi";
} elsif ( $in{sisetu} eq "14"){
require "./seikei.cgi";
} elsif ( $in{sisetu} eq "15"){
require "./hukubiki.cgi";
} elsif ( $in{sisetu} eq "16"){
require "./rank.cgi";
} elsif ( $in{sisetu} eq "17"){
require "./cold.cgi";
} else {
	if ($chatwin == 1 ) { $chatoth = "target=\"sakaba\""; }
$chastats[11] = 0;
print <<"HTM";
<center>
<table border=0><tr>
<td width=300><nobr><font size=6 color=#$mojiiro2><b>$zone[0]</b></font></nobr></td>
<td align=center>
HTM

print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="1" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<FONT FACE="Times New Roman"><font color=#$chamoji></font></font>　<input type=submit value="旅立ちの草原へ" size=30 onClick="this.disabled=true; this.value='旅立ちの草原へ'; this.form.submit();">　
</form>
HTM
$chastats[11] = 0;
print <<"HTM";
<wbr></nobr></tr></table><br><hr>

<br>
<table border=0><tr><td>
<table border=1><tr><td>
<img src="$maindir/$imgfile/zonepic0.gif">
</td></tr></table>
</td><td width=100></td><td>
<table border=0><tr><td colspan=3 align=center>
<font size=5 color=#$mojiiro3><b>街の施設  </b></font><br><br></td></tr>
<tr><td width=150>
<form method="post" action="./$zonecgi">
<input type=hidden value="1" name="sisetu">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="$sisetu[1]" onClick="this.disabled=true; this.value='$sisetu[1]'; this.form.submit();">
</form>
</td><td width=100>
<form method="post" action="./$zonecgi">
<input type=hidden value="2" name="sisetu">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="　  $sisetu[2]  　" onClick="this.disabled=true; this.value='    $sisetu[2]    '; this.form.submit();">
</form>
</td></tr>
<tr><td width=100>
<form method="post" action="./$zonecgi">
<input type=hidden value="3" name="sisetu">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="　 $sisetu[3] 　" onClick="this.disabled=true; this.value='   $sisetu[3]   '; this.form.submit();">
</form>
</td><td width=100>
<form method="post" action="./$zonecgi">
<input type=hidden value="4" name="sisetu">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value=" $sisetu[4] " onClick="this.disabled=true; this.value=' $sisetu[4] '; this.form.submit();">
</form>
</td></tr>
<tr><td width=100>
<form method="post" action="./$zonecgi">
<input type=hidden value="5" name="sisetu">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="　 $sisetu[5] 　" onClick="this.disabled=true; this.value='   $sisetu[5]   '; this.form.submit();">
</form>
</td><td width=100>
<form method="post" action="./$zonecgi">
<input type=hidden value="6" name="sisetu">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="　  $sisetu[6]  　" onClick="this.disabled=true; this.value='    $sisetu[6]    '; this.form.submit();">
</form>
</td></tr>
<tr><td width=100>
<form method="post" action="./$zonecgi">
<input type=hidden value="7" name="sisetu">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value=" $sisetu[7]　" onClick="this.disabled=true; this.value=' $sisetu[7]  '; this.form.submit();">
</form>
</td><td width=100>
<form method="post" action="./$zonecgi">
<input type=hidden value="10" name="sisetu">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="  $sisetu[10]　 " onClick="this.disabled=true; this.value='  $sisetu[10]   '; this.form.submit();">
</form>
</td></tr>
<tr><td width=100>
<form method="post" action="./$zonecgi">
<input type=hidden value="11" name="sisetu">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="  $sisetu[11]　 " onClick="this.disabled=true; this.value='  $sisetu[11]   '; this.form.submit();">
</form>

</td><td width=100>
<form method="post" action="./$zonecgi">
<input type=hidden value="12" name="sisetu">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="　  $sisetu[12]  　" onClick="this.disabled=true; this.value='    $sisetu[12]    '; this.form.submit();">
</form>
</td></tr>

</td><td width=100>
<form method="post" action="./$zonecgi">
<input type=hidden value="15" name="sisetu">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="   $sisetu[15]   " onClick="this.disabled=true; this.value='   $sisetu[15]   '; this.form.submit();">
</form>

</td><td width=100>
<form method="post" action="./$zonecgi">
<input type=hidden value="16" name="sisetu">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="$sisetu[16]" onClick="this.disabled=true; this.value='$sisetu[16]'; this.form.submit();">
</form>
</td></tr>

</td><td width=100>
<form method="post" action="./$zonecgi">
<input type=hidden value="14" name="sisetu">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="$sisetu[14]" onClick="this.disabled=true; this.value='$sisetu[14]'; this.form.submit();">
</form>

HTM
	if ($flag3 ) {
print <<"HTM";
</td><td width=100>
<form method="post" action="./$zonecgi">
<input type=hidden value="13" name="sisetu">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="$sisetu[13]" onClick="this.disabled=true; this.value='$sisetu[13]'; this.form.submit();">
</form>
</td></tr>
HTM
}

print <<"HTM";
</td><td width=100>
<form method="post" action="./bar.cgi" $chatoth>
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value=" $sisetu[9] " onClick="this.disabled=true; this.value=' $sisetu[9] '; this.form.submit();">
<tr><td width=100>
</form>


</table>

</td></tr></table>
<br><br>
HTM

}

&pettukitable;
&hpowari;

sub topsisetu {
print <<"HTM";
<center>
<table border=0><tr>
<td width=400><nobr><font size=6 color=#$mojiiro2><b>$zone[0]「$sisetu[$in{sisetu}]」</b></font></nobr></td>
<td align=center width=200>
</td></tr></table><br><hr>
<br>
<table border=0><tr><td>
<table border=1><tr><td>
<img src="$imgfile/sisetupic$in{sisetu}.gif"></td></tr></table></td><td width=40></td><td>
HTM
}

sub townmodori {
print <<"HTM";
<br>
<form method="post" action="./$zonecgi">
<input type=hidden value="" name="sisetu">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="     街へ戻る     " onClick="this.disabled=true; this.value='     街へ戻る     '; this.form.submit();">
</form></td></tr></table>
<br>
<hr>
HTM
}

sub modori {
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="" name="sisetu">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="     街へ戻る     " onClick="this.disabled=true; this.value='     街へ戻る     '; this.form.submit();">
</form></td></tr></table>
<br>
<hr>
HTM
}
1;