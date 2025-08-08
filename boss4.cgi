#　ボスの名前
$bossname ="バグターミネーター";

#　戦闘開始前のセリフ
@boss = ( "宛てもないまま、極寒の山を彷徨い続けているうちに、",
	"辺りはいつしか闇に包まれていた。<br>",
	"<b>$chaname</b>「一体、どこまで続くんだ。　この山は・・・。」<br>",
	"歩いても歩いても同じような風景が続き、",
	"寒さと疲労で、$chanameの体力は限界を超えていた。<br>",
	"・・・その時、前方に黒い人影が見えた。<br>");

@boss1 = ("その人影は、まだ$chanameの存在に気付いていないらしく、",
	"幽霊のような、か弱い声で、なにやら独り言をつぶやいている・・・。<br>",
	"<b>幽霊のような声</b><font face=有澤行書>「ハラ減ったよぉ～・・・こんなところで死にたくないよぉ～・・・。」</font><br>",
	"<b>$chaname</b>「・・・。」<br>");

@boss2 = ("その人影はフラフラになりながらも、少しづつ、こちらに近づいてくる。",
	"今にも倒れてしまいそうな足取だ。<br>",
	"<b>$chaname</b>「・・・・・ッ！？」<br>",
	"その人影の背後に、モンスターの影が見える・・・！",
	"このままでは、あの人が危ない！！");

@boss3 = ("$chanameは、その人を守る為、モンスターに向かって走っていった！<br>");

#　戦闘終了後のセリフ
@boss4 = ("<b>$chaname</b>「ハァ・・ハァ・・・。」",
	"モンスターとの戦闘に勝利した$chanameは、",
	"フラフラになっていた人影の無事を確認する為、顔を覗き込んだ。<br>",
	"<b>$chaname</b>「お、お前は・・・！　デュラン・・・！？」");
@boss5 = ("<b>$chaname</b>「・・・・・。」",
	"<b>デュラン</b>「・・・・・。」<br>",
	"２人は見つめ合ったまま、沈黙の時が続いた・・・。");
@boss6 = ("しばらくすると、デュランはさっきまで倒れそうだったのが嘘のように、",
	"物凄い勢いでどこかへ走って行ってしまった。<br>",
	"その後姿は、どこか恥ずかしげに見えた・・・。<br>",
	"<b>$chaname</b>（それにしても、奴はこんな所で何をしていたんだ？）<br>",
	"恐らく、遭難だろうと\予\想\しつつ、$chanameはその場を離れる事にした。");

#################

if ( $in{boss} eq "" ) { $in{boss} = 0;}
print <<"HTM";
<center>
<table border=0 width=800><tr>
<td align=center><nobr><font size=6 color=#$mojiiro2><b>$zone[$chaplace]</b></font></nobr></td><td width=30></td><td><nobr>
HTM

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

if ( $in{boss} eq "3"){
	foreach $serifu (@boss3) {
		print "$serifu<br>";
	}
$in{boss} ++;
print <<"HTM";
<form method="post" action="./$battlecgi">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$in{boss}" name="boss">
<input type=hidden value="$chapass" name="usrpass">
<input type=hidden value="$chacount" name="count">
<input type=submit value="    　 戦闘開始！　     " size=30>
</form></td></tr></table>
HTM
} elsif ( $in{boss} eq "6"){
$chaplace = 124;
if ( $flag1 eq "" ) { $flag1 = 1; }
&charadatawrt;
	foreach $serifu (@boss6) {
		print "$serifu<br>";
	}

print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="$itemstats2" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="$zone[124] へ" ><br></td></tr></table>
</form></td></tr></table>
HTM
} elsif ( $in{boss} eq "1"){
	foreach $serifu (@boss1) {
		print "$serifu<br>";
	}
&nextform;

} elsif ( $in{boss} eq "2"){
	foreach $serifu (@boss2) {
		print "$serifu<br>";
	}
&nextform;

} elsif ( $in{boss} eq "4"){
	foreach $serifu (@boss4) {
		print "$serifu<br>";
	}
&nextform;

} elsif ( $in{boss} eq "5"){
	foreach $serifu (@boss5) {
		print "$serifu<br>";
	}
&nextform;

} elsif ( $in{boss} eq "6"){
	foreach $serifu (@boss6) {
		print "$serifu<br>";
	}
&nextform;

} else {
	foreach $serifu (@boss) {
		print "$serifu<br>";
	}
&nextform;

}
print "</td></tr></table><hr>";
&pettukitable;

sub nextform {
$in{boss} ++;
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$in{boss}" name="boss">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="  次へ  " onClick="window.location.replace" ><br></td></tr></table>
</form>
HTM
}
1;