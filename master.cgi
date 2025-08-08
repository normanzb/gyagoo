#!/usr/bin/perl

#　↑サーバーの設定に合わせて変更してください。

###############
#
# 「Vagoo(ver1.03)」　2001年10月26日配布開始
#　　　スクリプト製作者　スカイ（game@sky-wing.com）
#
#　ダウンロード規定を同意した方のみ、「Vagoo」スクリプト類の使用を許可します。
#
#　配布元HP「うぇぶなげぇむ」http://www.sky-wing.com/~game/
#
###########

require "./settei.cgi";
require "./cgi-lib.pl";
&ReadParse;
&ipblock;
&gaibublock;
&hpsaisyo;

if ( $in{mode} ne "" && $adminp ne $in{adminpass}) {
print <<"HTM";
<center><font size=7>パスワードエラー</font></center>
HTM
exit;
}

print "<center><font size=6 color=#$mojiiro2><b>管理モード</b></font><br><hr>";

if ( $in{mode} == 1 ){
&adminform;
} elsif ( $in{mode} == 2 ){

# 期限切れ削除

&adminback;
print "以下のIDが期限切れで削除されました。<br><br><table border=0><tr><td>";

open(CHA,"$maindir/$foldacha/user_id$bousi2cha$bousikts2");
	while ( $chadata = <CHA> ) {
		chop($chadata);
		($id,$name) = split(/\//,$chadata);
open(DAT,"$maindir/$foldacha/$bousicha$id$bousikts");
	($chaid,$chapass,$chaname,$chaurl,$chamoji,$chaip,$chajikan) = split(/,/,<DAT>);
		if ($now > $chajikan + ($datadelete*24*60*60) ) { push(@sakujo,$chaid); }
close(DAT);
	}

close(CHA);

	foreach $kesi (@sakujo) {
unlink("$maindir/$foldacha/$bousicha$kesi$bousikts");
unlink("$maindir/$foldacha/bankit_$kesi$bousi2cha$bousikts");
unlink("$maindir/$foldacha/pet_$kesi$bousi2cha$bousikts");
unlink("$maindir/$foldacha/bankg_$kesi$bousi2cha$bousikts");
unlink("$maindir/$foldacha/tegami_$kesi$bousi2cha$bousikts");
unlink("$maindir/$foldazukan/pet1$kesi$bousicha$bousikts");
unlink("$maindir/$foldazukan/pet2$kesi$bousicha$bousikts");
unlink("$maindir/$foldazukan/pet3$kesi$bousicha$bousikts");
	}

open(CHA,"$maindir/$foldacha/user_id$bousi2cha$bousikts2");
open(DEL,">$maindir/$foldacha/user_id.tmp");
	while ( $chadata = <CHA> ) {
	chop($chadata);
	($id,$name) = split(/\//,$chadata);
		foreach $kesi (@sakujo) {
			if ( $id eq $kesi ) { print "・ $kesi<br>\n";$abes = 1;next; } 
		}
	if ( $abes != 1 ) {print DEL "$chadata\n";}
	$abes = 0;
	}
close(DEL);
close(CHA);

rename("$maindir/$foldacha/user_id.tmp","$maindir/$foldacha/user_id$bousi2cha$bousikts2");
print "</td></tr></table>";

} elsif ( $in{mode} == 3 ){

#　指定キャラデータ削除

&adminback;
print <<"HTM";
削除するキャラにチェックを入れてください（複数可）。<br>
１度削除したデータはもう戻りません。<br>
慎重に操作を行ってください。<br><br>
<form action="./$admincgi" method="post">
<input type=hidden name="adminpass" value="$in{adminpass}">
<input type=hidden name="mode" value="31">
<input type=submit value="選択キャラデータ削除">
<table border=1>
HTM
$tourokunum = 1;
open(CHA,"$maindir/$foldacha/user_id$bousi2cha$bousikts2");
flock(CHA,2);
	while ( $chadata = <CHA> ) {
		chop($chadata);
		($id,$name) = split(/\//,$chadata);
	open(DAT,"$maindir/$foldacha/$bousicha$id$bousikts");
		($chaid,$chapass,$chaname,$chaurl,$chamoji,$chaip) = split(/,/,<DAT>);
print <<"HTM";
<tr><td><input type=checkbox name="kariusrid" value="$chaid\"></td><td>$tourokunum</td><td><nobr>$chaid</nobr></td>
<td><nobr>$chapass</nobr></td><td><nobr>$chaname</nobr></td><td><nobr>$chaip</nobr></td></tr>
HTM
	close(DAT);
$tourokunum ++;
	}
flock(CHA,8);
close(CHA);

print "</table></form>";

} elsif ( $in{mode} == 31 ){
&adminback;
print "以下のIDが削除されました。<br><br>";
	@sakujo = split(/\0/,$in{usrid});
open(CHA,"$maindir/$foldacha/user_id$bousi2cha$bousikts2");
	open(DEL,">>$maindir/$foldacha/user_id.tmp");
	while ( $chadata = <CHA> ) {
		chop($chadata);
		($id,$name) = split(/\//,$chadata);
		foreach $kesi (@sakujo) {
			if ( $id eq $kesi ) { print "・ $kesi<br>\n";$abes = 1;next; } 
		}
		if ( $abes != 1 ) {print DEL "$chadata\n";}
		$abes = 0;
	}
	close(DEL);
close(CHA);
unlink("$maindir/$foldacha/$bousicha$kesi$bousikts");
unlink("$maindir/$foldacha/bankit_$kesi$bousi2cha$bousikts");
unlink("$maindir/$foldacha/pet_$kesi$bousi2cha$bousikts");
unlink("$maindir/$foldacha/bankg_$kesi$bousi2cha$bousikts");
unlink("$maindir/$foldacha/tegami_$kesi$bousi2cha$bousikts");
unlink("$maindir/$foldazukan/pet1$kesi$bousicha$bousikts");
unlink("$maindir/$foldazukan/pet2$kesi$bousicha$bousikts");
unlink("$maindir/$foldazukan/pet3$kesi$bousicha$bousikts");
rename("$maindir/$foldacha/user_id.tmp","$foldacha/user_id$bousi2cha$bousikts2");

} elsif ( $in{mode} == 4 ){

#　現在プレイしているキャラ

open(NOW,"$maindir/playing$bousikts");
	while( $playnow = <NOW> ) {
		chop($playnow);
		($nowid,$nowname,$nowjikan) = split(/\//,$playnow);
		if ( $now < $nowjikan + 200 && $nowid ne $chaid ) {
			push(@playing,$playnow);
		}
	}
close(NOW);
$playingkazu = @playing;
&adminback;
print <<"HTM";
<center>
<table border=0 width=200><tr>
<td align=center>
現在の冒険者（$playingkazu人）</td></tr>
HTM

foreach $playnow ( @playing ) {
	chop($playnow);
	($nowid,$nowname) = split(/\//,$playnow);
print "<tr><td>・<a href=\"./$introcgi?usrid=$nowid\" target=\"intro\"><b>$nowname</b></a> </td></tr>";
}
print <<"HTM";
</table><br>
HTM

} elsif ( $in{mode} == 5 ){

#　登録者一覧

&adminback;
$tourokunum = 1;
print <<"HTM";
<form action="./$admincgi" method="post">
<input type=hidden name="adminpass" value="$in{adminpass}">
<input type=hidden name="mode" value="51">
<input type=submit value="選択ID詳細データ">

<table border=1><tr align=center><td>-</td><td><b><nobr>No.</nobr></b></td><td><b>ID</b></td><td><b>PASS</b></td><td><b>キャラ名</b></td><td><b><nobr>Lv</nobr></b></td><td><b><nobr>ジョブ</nobr></b></td><td><b>IP</b></td><td><b>最終アクセス日</b></td></tr>
HTM

open(CHA,"$maindir/$foldacha/user_id$bousi2cha$bousikts2");
flock(CHA,2);
	while ( $chadata = <CHA> ) {
		chop($chadata);
		($id,$name) = split(/\//,$chadata);
	open(DAT,"$maindir/$foldacha/$bousicha$id$bousikts");
		($chaid,$chapass,$chaname,$chaurl,$chamoji,$chaip,$chajikan,$a,$a,$a,$a,$chaclass,$a,$a,$a,$chalvl) = split(/,/,<DAT>);
($secl,$minl,$hourl,$mdayl,$monl,$yearl,$wdayl) = localtime($chajikan);
@weekl = ('日','月','火','水','木','金','土');$monl ++;$wdayl = $weekl[$wdayl];
$minl = sprintf("%.2d",$minl);
$secl = sprintf("%.2d",$secl);
$hourl = sprintf("%.2d",$hourl);
print <<"HTM";
<tr><td><input type=radio name="usrid" value="$chaid"></td><td>$tourokunum</td><td><nobr>$chaid</nobr></td><td><nobr>$chapass</nobr></td><td><nobr>$chaname</nobr></td><td>$chalvl</td><td>$job[$chaclass]</td><td><nobr>$chaip</nobr></td><td><nobr>$monl月$mdayl日($wdayl) $hourl:$minl:$secl</nobr></td>
<td>
<a href="./zone.cgi?usrid=$chaid&usrpass=$chapass" target="_zone">●</a>
</td>
</tr>

HTM
	close(DAT);
$tourokunum ++;
	}
flock(CHA,8);
close(CHA);

print <<"HTM";
</table></form>
HTM

} elsif ( $in{mode} == 51 ){
	if ( $in{usrid} eq "" ) { print "参照キャラが選択されていません。<br>";&adminback;exit; }

require "./zone.pl";

&charadataload;
&adminback;

print <<"HTM";
<center><font size=6 color=#$mojiiro2><b><font size=7 color=#$chamoji>$chaname
</font>さんのステータス</b></font><br><br>
<b><font size=+1>ゾーン名 [ $zone[$chaplace] ]</b></font><br><br>

HTM
&pettukitable;
&itemtable;
open(BANK,"$maindir/$foldacha/bankg_$in{usrid}$bousi2cha$bousikts");
	$bankgold = <BANK>;
close(BANK);
print "<br><table border=0><tr><td>銀行の預金： <b>$bankgold</b> G";
print "</td><td width=30></td><td><form>銀行のアイテム：<br><select size=10>";

open(BANKI,"$maindir/$foldacha/bankit_$in{usrid}$bousi2cha$bousikts");
		while ( $bankno = <BANKI> ) {
		chop($bankno);
	($bankname,$bankbun) = split(/\//,$bankno);
print "<option value=\"$bankname/$bankbun/$abb\">$bankname（$bankbun）";
		}
close(BANKI);
print "</form></td><td width=30></td><td><form>ペット小屋：<br><select size=10>";
open(PET,"$maindir/$foldacha/pet_$in{usrid}$bousi2cha$bousikts");
	while ( $petkai = <PET> ) {
		chop($petkai);
print "<option value=\"$petkai\">$petkai";
	}
close(PET);
print "</select></form></td></tr></table><hr><center><font size=6 color=#$mojiiro4><b>手紙 一覧</b></font><br><table border=0 width=70%><tr><td>";
	open(BANN,"$maindir/$foldacha/tegami_$in{usrid}$bousi2cha$bousikts");
		while ( $yuubin = <BANN> ) {
($kako,$chanamez,$chamojiz,$tegami,$genzai2) = split(/\t/,$yuubin);
print "<hr><font color=#$chamojiz><b>$chanamez</b></font> ： $tegami <nobr>($genzai2)</nobr>\n";
		}
	close(BANN);
print <<"HTM";
</td></tr></table><hr></center>
HTM
} elsif ( $in{mode} == 6 ){
&adminback;

open(NOW,"$maindir/chat$bousikts");
@playing = <NOW>;
close(NOW);
$playingkazu = @playing;

open(NOW,"$maindir/chat2$bousikts");
	@res = <NOW>;
close(NOW);

print <<"HTM";
<form action="./$admincgi" method="post">
<input type=hidden name="adminpass" value="$in{adminpass}">
<input type=hidden name="mode" value="6">
<input type=submit value="酒場ログ閲覧">
</form>

</center><nobr>現在の来店者($playingkazu人):
HTM
	foreach $kyaku (@playing) {
		chop($kyaku);
		($nowid,$nowname) = split(/\//,$kyaku);
		print "/ <a href=\"./$introcgi?usrid=$nowid\" target=\"intro\"><b>$nowname</b></a> <wbr>";
	}

print <<"HTM";
</nobr>
@res
HTM


} else {
print <<"HTM";
<form action="./$admincgi" method="post">
管理パスワードを入力してください。<br><br>
<input type=test size=12 name="adminpass" maxlength=10><br><br>
<input type=hidden name="mode" value="1">
<input type=submit value="   実行   ">
</form>
HTM
}
&hpowari;

sub adminform {
print <<"HTM";
<font size=5>管理コマンド一覧</font><br>
<form action="./$admincgi" method="post">

<input type=hidden name="adminpass" value="$in{adminpass}">
<input type=hidden name="mode" value="2">
<input type=submit value="期限切れデータ自動削除">
</form>
<form action="./$admincgi" method="post">
<input type=hidden name="adminpass" value="$in{adminpass}">
<input type=hidden name="mode" value="3">
<input type=submit value="手動キャラデータ削除">
</form>
<form action="./$admincgi" method="post">
<input type=hidden name="adminpass" value="$in{adminpass}">
<input type=hidden name="mode" value="4">
<input type=submit value="現在の冒険者一覧">
</form>
<form action="./$admincgi" method="post">
<input type=hidden name="adminpass" value="$in{adminpass}">
<input type=hidden name="mode" value="5">
<input type=submit value="登録データ一覧">
</form>
<form action="./$admincgi" method="post">
<input type=hidden name="adminpass" value="$in{adminpass}">
<input type=hidden name="mode" value="6">
<input type=submit value="酒場ログ閲覧">
</form>
HTM
}

sub adminback {
print <<"HTM";
<form action="./$admincgi" method="post">
<input type=hidden name="adminpass" value="$in{adminpass}">
<input type=hidden name="mode" value="1">
<input type=submit value="管理コマンド一覧へ戻る">
</form><hr>
HTM
}

 

exit;
