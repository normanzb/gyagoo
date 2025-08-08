#!/usr/bin/perl
#　↑サーバーの設定に合わせて変更してください。

@last = ("長老の家・奥の間","次元の狭間","この世の果て");

####################
require "./settei.cgi";
require "./cgi-lib.pl";
&ReadParse;

&cookieget;
&ipblock;
&gaibublock;

&charadataload;


if ( $chapass ne $in{usrpass} ) { &CgiError('パスワードエラー','パスワードが違います。再度ログイン画面からやり直してください。');exit; }
&cookieset;

if ( $flag2 == 2 ) { $flag2 = 3;&charadatawrt;}
if ( $bgurl ne "" ){
	$bgmode = "background=\"$bgurl\"";
} else {
	$bgmode = "bgcolor=\#$bgclr";
}

print <<"HTM";
Content-type: text/html

<html><head><title>$title</title>
<STYLE type="text/css">
A { text-decoration: none }
</STYLE>

</head>
<body $bgmode link=#$linkiro vlink=#$vlinkiro>
<basefont size=2 color=#$mojiiro><br>
<center>
HTM

if ( $in{key} < 11 ) {
print <<"HTM";
<table border=0><tr>
<td width=300><nobr><font size=6 color=#$mojiiro2><b>$last[$in{last}]</b></font></nobr></td>
</td></tr></table><br><hr>
<br>
<table border=0><tr><td>
<table border=1><tr><td>
<img src="$maindir/$imgfile/lastpic$in{last}.gif">
</td></tr></table>
</td><td width=100></td><td>
HTM
}

if ( $in{key} == 1 ) {
print <<"HTM";
激しい痛みが電光石火に体中を貫く。<br>
今にも体が引きちぎれそうだ。<br><br>
（このまま死んでしまうのでは・・・・）<br><br>
そんな考えが頭をよぎった矢先、<br>
<font color=#$chamoji><b>$chaname</b></font> は見知らぬ場所に立っていた。<br>
<form method="post" action="./last.cgi">
<input type=hidden value="2" name="last">
<input type=hidden value="2" name="key">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="  次へ  ">
</form>
HTM

} elsif ( $in{key} == 2 ) {
print <<"HTM";
雲海のようなものが辺り一面に広がっている。<br><br>
（どこだここは？　天界？　神の国？）<br><br>
そこは正に人間が語りついできた<br>
極楽浄土そのものだったのだ。<br><br>
<font size=+1 color=#$mojiiro2>「ち、またバグりやがったかっ！」</font><br><br>
突然、雷鳴のような怒鳴り声が響き渡った！<br>
<font color=#$chamoji><b>$chaname</b></font> は反射的に身構\える！<br>
しかし、慎重に辺りを見回したが何も見当たらなかった。<br><br>
<form method="post" action="./last.cgi">
<input type=hidden value="2" name="last">
<input type=hidden value="3" name="key">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="  次へ  ">
</form>
HTM
} elsif ( $in{key} == 3 ) {
print <<"HTM";
しばらくすると、目前にスーッと見知らぬ人物が現れた！<br>
見るからに高貴な姿をしている。<br>
人間ではないようだ・・・・神か！？<br>
その人物は独り言のようにしゃべりだした。<br><br>
「開発者め、いったいいつになったら<br>
　このバグを直してくれるんだ。<br>
　連絡すらよこさねぇし・・・ヒドイ話だ。」<br><br>
（開発者？　バグ？）<br>
<form method="post" action="./last.cgi">
<input type=hidden value="2" name="last">
<input type=hidden value="4" name="key">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="  次へ  ">
</form>
HTM
} elsif ( $in{key} == 4 ) {
print <<"HTM";
「おっと、すまんな。<br>
　つい怒りで我を忘れてしまった。<br>
　いきなりのことで何が起こったのか<br>
　わからないといったところだろう。<br>
　私が少し状況説明をしてやろうじゃないか。」<br>
<form method="post" action="./last.cgi">
<input type=hidden value="2" name="last">
<input type=hidden value="5" name="key">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="  次へ  ">
</form>

HTM
} elsif ( $in{key} == 5 ) {
print <<"HTM";
「私はこのゲームの管理人だ。<br>
　お前らは神という呼び方で呼んでいるがな。」<br><br>
<font color=#$chamoji>「ゲームだと？　どういう意味だ！」</font><br><br>
「そうだ。ゲームだ。<br>
　お前らは全員、私のプレーする<br>
　ゲームの中の住民なのだよ。<br>
　ま、突然こんなことを言われても<br>
　信じられないとは思うがな。」<br><br>
言葉が出ない・・・。<br>
さらに神と名乗る者は続けた。<br>
<form method="post" action="./last.cgi">
<input type=hidden value="2" name="last">
<input type=hidden value="6" name="key">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="  次へ  ">
</form>
HTM
} elsif ( $in{key} == 6 ) {
print <<"HTM";
「かれこれもう数千万年プレーし続けている。<br>
　いやー、お前達人間という種族が誕生した時は<br>
　本当に喜んだよ。<br>
　実に素晴らしい頭脳を持っていたからな。<br>
　他のプレーヤーに自慢しまくったさ。」<br><br>
（こいつの話は真実なのだろうか・・）<br>
<form method="post" action="./last.cgi">
<input type=hidden value="2" name="last">
<input type=hidden value="7" name="key">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="  次へ  ">
</form>
HTM
} elsif ( $in{key} == 7 ) {
print <<"HTM";
「が、しかし。この人間という種族は<br>
　実はゲームのプレーに大きな害をもたらす<br>
　種族だったのだ。<br>
　時が経つにつれそれが顕著に表\れだした。<br><br>
  お前ら人間は戦闘意欲が強すぎるのだよ。<br>
　せっかく私が誕生させた新種族をすぐに絶滅、<br>
　己の欲を満たすために環境破壊、<br>
　あげくの果てにはゲームの世界から<br>
　現実へ飛び出すバグまで起こすようになりやがった。」<br><br>
（・・・・・。）<br>
<form method="post" action="./last.cgi">
<input type=hidden value="2" name="last">
<input type=hidden value="8" name="key">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="  次へ  ">
</form>
HTM
} elsif ( $in{key} == 8 ) {
print <<"HTM";
「いいか。よく聞け。<br>
　このゲームは星が滅んだ時点で<br>
　ゲームオーバーになってしまうのだよ。<br>
　お前達人間がもしこのまま自らの欲望のために<br>
　横暴\を続けたら困るのはお前達自身ではないのか？」<br>
　
<form method="post" action="./last.cgi">
<input type=hidden value="2" name="last">
<input type=hidden value="9" name="key">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="  たしかにそのとおりかもしれない・・  "><br>
<input type=submit value="  例えそうだとしても・・・・  "><br>
<input type=submit value="  だとしたら人間は滅ぶしかないのか・・？  "><br>
</form>

HTM
} elsif ( $in{key} == 9 ) {
print <<"HTM";
「よくよく考えることだな。己の行動を。<br>
　まぁ、良い、ここへたどり着いた褒美をやろう。」<br><br>
<font color=#$chamoji>「褒美？」</font><br><br>
「そうだ。お前の望む願いを<br>
　何でもかなえてやるぞ。<br>
　何を願う？」<br>
<form method="post" action="./last.cgi">
<input type=hidden value="2" name="last">
<input type=hidden value="10" name="key">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=text name="negai" maxlength=41 size=40>(20字以内)<br><br>
<input type=submit value="  次へ  ">
</form>

HTM
} elsif ( $in{key} == 10 ) {
	if ( $in{negai} eq "" ) {
print <<"HTM";
「フハハハハハ！<br>
　何でも願いをかなえてやるというのに<br>
　望みがないだと？<br>
HTM
        } elsif ( length($in{negai}) > 40 ) {
print <<"HTM";
「馬鹿者がっ！<br>
　願いは20字以内だといったであろうがっ！<br>
HTM
	} else {
print <<"HTM";
「ハーハハハハハッ！<br>
　<b>$in{negai}</b><br>
　だと？　何でも願いをかなえてやるというのに<br>
　出た言葉がそれか？<br>
　なんたる未熟。<br>
HTM
	}
print <<"HTM";
<br>
　我がゲームの万物の霊長は<br>
　この程度のレベルだったとはな。<br>
　お前達には失望したよ。<br><br>
　気が変わった。<br>
　やはりお前ら人間は滅ぼすことにしよう。<br>
　まずはお前が最初だ！！！<br><br>
<form method="post" action="./last.cgi">
<input type=hidden value="2" name="last">
<input type=hidden value="11" name="key">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="  戦闘開始！  ">
</form>
HTM

} elsif ( $in{key} == 11 ) {
print <<"HTM";
<center><font size=6 color=#ff00ff><b>神</b> との戦闘開始！！</font><hr><br>
<table border=0><tr><td bgcolor=#009900 align=center>
  <font size=4><nobr><b>1 ターン目</b></nobr></font></td></tr><tr><td>
<table border=0>
<tr align=center valign="baseline"><td>
<img src="./pics/god.gif"></td><td></td><td>
</td><td>
<iframe name="charaga" src="./charapic.cgi?atama=8&hada=d0ffd0&eye=2&hana=14&kuti=16&kami=3&leg=tabi&arm=&hlm=&che=tabi&wp=dagger&sld=" frameborder=0 scrolling=no width=100 height=125></iframe>
</td><td></td><td></td></tr><tr align=center><td>
<font size=4><nobr>神</font></nobr></td>
<td width=20 rowspan=2><nobr><font size=4 color=#ff0000><b>VS</b></font></nobr></td>
<td colspan=3><font size=4><nobr>$chaname</font></nobr></td><td></td></tr>
<tr><td><nobr><img src="./pics/exp.gif" height="8"><img src="./pics/expbar1.gif" width=150 height="8"><img src="./pics/exp.gif" height="8"></nobr></td><td colspan=3><font size=4><nobr><img src="./pics/exp.gif" height="8"><img src="./pics/expbar1.gif" width=150 height="8"><img src="./pics/exp.gif" height="8"></nobr></td><td></td></tr>
</table><br><br><font size=4>
<font color=#$chamoji><b>$chaname</b></font> の攻撃！！<br>しかし、神は微動だにしなかった！<br><br>
<b>神</b> の攻撃！！<br>
  「一瞬で楽にしてやろう。」<br>
    まばゆい光が神の右手に集中しだした！！<br><br>
      <font size=+2 color=#007700><b>ゴッドハンド　！！！</b></font> <br><br>
<font color=#0000ff>$chaname は<font color=#ff0000>21589</font>のダメージを受けた！！<br></font></td></tr></table><br><br>
<br><br><font size=5 color=#0000ff><b>$chaname</b> は戦闘に負けた・・・</font><br><br>
<form method="post" action="./last.cgi">
<input type=hidden value="12" name="key">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value=" 次へ " ></form></td></tr></table>
<br><hr>
HTM

} elsif ( $in{key} == 12 ) {
print <<"HTM";
  <font size=6 color=#ff0000><b>エンディング</b></font><br><br>
  薄れゆく意識の中、神の独り言が耳に入った。<br><br>
<table border=0><tr><td>
「フン。愚か者が・・・・。<br>
　万が一でも私に勝てるとでも思ったのか？<br>
　神さえも手にかけようとするその戦闘意欲・・・。<br>
　早めにお前ら人間をなんとかせねば<br>
　このままゲームが終了してしまいそうだな。<br><br>
　とりあえず、このバグを修正してもらうのが先か・・・・　」<br>
</td></tr></table><br>
・・・・・・・・・・・・・・・・<br><br>
・・・・・・・・・・・・・<br><br>
・・・・・・・・・・<br><br>
・・・・・・・<br><br>
・・・・<br><br>
  <br><br><br>
意識が戻るとそこは元の世界だった。<br><br>
我々人間はこの先どうすればいいのか・・・<br><br>
いつまで考えても答えは出てこなかった。<br><br><br>
しかし、ただ一つはっきりしていることがある。<br><br>
それは我々がヤツのプレーするゲームの中の住人であることだ。<br><br><br><br>
HTM

} else {
print <<"HTM";
<font color=#$chamoji><b>$chaname</b></font> は恐る恐る奥の部屋へと進んだ。<br>
何一つ明かりのない暗闇だったが、前方に何か違和感を感じた。<br>
よく見るとその部分だけ空間が歪んでいるようだ。<br><br>
（これから何が起こるんだろう・・・）<br><br>
勇気を振り絞りその歪みに飛び込んだ！！<br>
HTM


$chaplace = 301;
if ( $flag2 eq "" ) { $flag2 = 3; }
&charadatawrt;
	foreach $serifu (@boss7) {
		print "$serifu<br>";
	}

print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="高みの洞窟　へ" ><br></td></tr></table>
</form>
HTM
}
print "</td></tr></table>";
&hpowari;
exit;
