#　ボスの名前
$bossname ="バグターミネーター";

#　戦闘開始前のセリフ
@boss = ( "グツグツと煮えたぎる溶岩のせいで",
	"息をするのも苦しいほどの蒸し暑さだ。<br>",
	"$chaname は洞穴へと足を運んだ・・・");
@boss1 = ("謎の声「何者だ・・・」<br>",
	"ドス黒い声が洞穴中に響き渡る。",
	"どうやら前方の闇の中にうごめく",
	"巨大な物体から発せられている声のようだ。",
	"暗すぎて姿を確認できない。");
@boss2 = ("謎の声「ハハハハ、何かと思いきや",
	"バグの元凶のお出ましか。」<br>",
	"(バグの元凶？？　どういう意味だろう・・",
	"しかし、バグ？　ヴァグーとはまた別の物か？)<br>",
	"謎の声「オマエ達からわざわざ出向いてくるとはな。",
	"まーよい。私もそろそろ行動を起こそうと",
	"思っていたところだ。<br>",
	"(何の話だ？　全く理解ができない・・)<br>");
@boss3 = ("「我が名は <b>$bossname</b> ！！",
	"バグを終焉させるために生まれし者。",
	"人間どもを絶滅させるために",
	"この世に生を受けたのだ！<br>",
	"オマエ達に残された道はただ一つ。",
	"この私に殺されることだ！！」<br>",
	"その物体は突然襲いかかってきたっ！！");

#　戦闘終了後のセリフ
@boss4 = ("「ぐぁぁぁぁぁぁぁぁっっっ",
	"な、何故だ！　何故この私が負けるのだ！",
	"私は無敵な存在としてこの世界に生誕されたはずだっ！",
	"これもバグの一つだというのか・・・」<br>",
	"(無敵？ 生誕？ バグ？ 謎は深まるばかりだ・・・)");
@boss5 = ("「覚えておけ、バグの元凶よ",
	"オマエ達を絶滅させるまで",
	"私は何度でもよみがえるであろう。",
	"ヤツの手によってな。ハハハハハハハハ」<br>",
	"大きな笑い声とともに $bossname は消滅した。");
@boss6 = ("(ヤツだと？ 何者かの手によって",
	"アイツは生み出されたというのか？？",
	"$bossname はヴァグーではなくバグと言った・・",
	"判らないことが多すぎるな・・・)<br>",
	"いくつかの謎を残しつつ、その場を後にした。");

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
$chaplace = 0;
if ( $flag3 eq "" ) { $flag3 = 3; }
&charadatawrt;
	foreach $serifu (@boss6) {
		print "$serifu<br>";
	}

print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="$itemstats2" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="$zone[0] へ帰る" ><br></td></tr></table>
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
<input type=submit value="  次へ  " ><br></td></tr></table>
</form>
HTM
}
1;