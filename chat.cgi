#!/usr/bin/perl

#　↑サーバーの設定に合わせて変更してください。

$serifu1 = "さんが来店しました。ごゆっくりどうぞ。"; #　入室時のコメント
$serifu2 = "さんが退店しました。"; #　退室時のコメント

$timeclr = "909090"; #　時間の文字色
###############

require "./settei.cgi";
require "./cgi-lib.pl";
&ReadParse;

&cookieget;
&ipblock;
&cookieset;
&charadataload;
if ( $chapass ne $in{usrpass} ) { &CgiError('パスワードエラー','パスワードが違います。再度ログイン画面からやり直してください。');exit; }

open(NOW,"$maindir/chat$bousikts");
	while( $playnow = <NOW> ) {
		chop($playnow);
		($nowid,$nowname,$nowjikan) = split(/\//,$playnow);
		if ( $now < $nowjikan + 100 && $nowid ne $chaid ) {
			push(@playing,$playnow);
		}
	}
close(NOW);
if ($in{key} ne "back" ) {
$playnow = "$chaid/$chaname/$now\n";
push(@playing,$playnow);
}
open(NOW,">$maindir/chat$bousikts");
  flock(NOW,2);
    foreach $playnow ( @playing ) {
      print NOW "$playnow\n";
    }
  flock(NOW,8);
close(NOW);

	foreach $kyaku (@playing) {
		chop($kyaku);
		($nowid,$nowname) = split(/\//,$kyaku);
}

$playingkazu = @playing;
($secl,$minl,$hourl,$mdayl,$monl,$yearl,$wdayl) = localtime($now);
@weekl = ('Sun','Mon','Tue','Wed','Thu','Fri','Sat');$monl ++;$wdayl = $weekl[$wdayl];
$minl = sprintf("%.2d",$minl);
$secl = sprintf("%.2d",$secl);
$hourl = sprintf("%.2d",$hourl);

open(NOW,"$maindir/chat2$bousikts");
	@res = <NOW>;
close(NOW);
	foreach $kyaku (@playing) {
		chop($kyaku);
		($nowid,$nowname) = split(/\//,$kyaku);
}

$moji1 = "/1";$moji2 = "/2";$moji3 = "/3";$moji4 = "/4";$moji5 = "/5";$moji6 = "/6";$moji7 = "/7";$moji8 = "/8";$moji9 = "/9";$moji0 = "/0";

if ( $in{key} eq "enter") {
	$enter = "<hr><b>★ <font color=#$chamoji>$chaname</font> <font color=#$mojiiro4>$serifu1</font></b> <font size=-1 color=#$timeclr>$monl/$mdayl ($wdayl) $hourl:$minl:$secl</font>\n";
	unshift(@res,$enter);&kakikomi;
} elsif ( $in{key} eq "back") {
	$back = "<hr><b>★ <font color=#$chamoji>$chaname</font> <font color=#$mojiiro2>$serifu2</font></b> <font size=-1 color=#$timeclr>$monl/$mdayl ($wdayl) $hourl:$minl:$secl</font>\n";
	unshift(@res,$back);&kakikomi;
} elsif ( $in{hatugen} eq "/調べる" && $flag3 ) {
	$in{hatugen} =~ s/</&lt;/g;$in{hatugen} =~ s/>/&gt;/g;
	$hatugen = "<br><br>$chanameは酒場の中を見渡すと、小さな紙切れを発見した。<br>紙切れには『<font color=red>$karistats[10]</font>』と書かれている。\n";
	unshift(@res,$hatugen);

} elsif ( $in{hatugen} =~ /$moji1/) {
$in{hatugen} =~ s/$moji1//g;
	$in{hatugen} =~ s/</&lt;/g;$in{hatugen} =~ s/>/&gt;/g;
	$hatugen = "<hr><b><font color=#$chamoji>$chaname</font> :</b><font color=red> $in{hatugen} </font><font color=#$timeclr> 　 $monl/$mdayl ($wdayl) $hourl:$minl:$secl</font>\n";
	unshift(@res,$hatugen);&kakikomi;
} elsif ( $in{hatugen} =~ /$moji2/) {
$in{hatugen} =~ s/$moji2//g;
	$in{hatugen} =~ s/</&lt;/g;$in{hatugen} =~ s/>/&gt;/g;
	$hatugen = "<hr><b><font color=#$chamoji>$chaname</font> :</b><font color=blue> $in{hatugen} </font><font color=#$timeclr> 　 $monl/$mdayl ($wdayl) $hourl:$minl:$secl</font>\n";
	unshift(@res,$hatugen);&kakikomi;
} elsif ( $in{hatugen} =~ /$moji3/) {
$in{hatugen} =~ s/$moji3//g;
	$in{hatugen} =~ s/</&lt;/g;$in{hatugen} =~ s/>/&gt;/g;
	$hatugen = "<hr><b><font color=#$chamoji>$chaname</font> :</b><font color=green> $in{hatugen} </font><font color=#$timeclr> 　 $monl/$mdayl ($wdayl) $hourl:$minl:$secl</font>\n";
	unshift(@res,$hatugen);&kakikomi;
} elsif ( $in{hatugen} =~ /$moji4/) {
$in{hatugen} =~ s/$moji4//g;
	$in{hatugen} =~ s/</&lt;/g;$in{hatugen} =~ s/>/&gt;/g;
	$hatugen = "<hr><b><font color=#$chamoji>$chaname</font> :</b><font color=coral> $in{hatugen} </font><font color=#$timeclr> 　 $monl/$mdayl ($wdayl) $hourl:$minl:$secl</font>\n";
	unshift(@res,$hatugen);&kakikomi;
} elsif ( $in{hatugen} =~ /$moji5/) {
$in{hatugen} =~ s/$moji5//g;
	$in{hatugen} =~ s/</&lt;/g;$in{hatugen} =~ s/>/&gt;/g;
	$hatugen = "<hr><b><font color=#$chamoji>$chaname</font> :</b><font color=violet> $in{hatugen} </font><font color=#$timeclr> 　 $monl/$mdayl ($wdayl) $hourl:$minl:$secl</font>\n";
	unshift(@res,$hatugen);&kakikomi;
} elsif ( $in{hatugen} =~ /$moji6/) {
$in{hatugen} =~ s/$moji6//g;
	$in{hatugen} =~ s/</&lt;/g;$in{hatugen} =~ s/>/&gt;/g;
	$hatugen = "<hr><b><font color=#$chamoji>$chaname</font> :</b><font color=slategray> $in{hatugen} </font><font color=#$timeclr> 　 $monl/$mdayl ($wdayl) $hourl:$minl:$secl</font>\n";
	unshift(@res,$hatugen);&kakikomi;
} elsif ( $in{hatugen} =~ /$moji7/) {
$in{hatugen} =~ s/$moji7//g;
	$in{hatugen} =~ s/</&lt;/g;$in{hatugen} =~ s/>/&gt;/g;
	$hatugen = "<hr><b><font color=#$chamoji>$chaname</font> :</b><font color=steelblue> $in{hatugen} </font><font color=#$timeclr> 　 $monl/$mdayl ($wdayl) $hourl:$minl:$secl</font>\n";
	unshift(@res,$hatugen);&kakikomi;
} elsif ( $in{hatugen} =~ /$moji8/) {
$in{hatugen} =~ s/$moji8//g;
	$in{hatugen} =~ s/</&lt;/g;$in{hatugen} =~ s/>/&gt;/g;
	$hatugen = "<hr><b><font color=#$chamoji>$chaname</font> :</b><font color=azure> $in{hatugen} </font><font color=#$timeclr> 　 $monl/$mdayl ($wdayl) $hourl:$minl:$secl</font>\n";
	unshift(@res,$hatugen);&kakikomi;
} elsif ( $in{hatugen} =~ /$moji9/) {
$in{hatugen} =~ s/$moji9//g;
	$in{hatugen} =~ s/</&lt;/g;$in{hatugen} =~ s/>/&gt;/g;
	$hatugen = "<hr><b><font color=#$chamoji>$chaname</font> :</b><font color=deepskyblue> $in{hatugen} </font><font color=#$timeclr> 　 $monl/$mdayl ($wdayl) $hourl:$minl:$secl</font>\n";
	unshift(@res,$hatugen);&kakikomi;
} elsif ( $in{hatugen} =~ /$moji0/) {
$in{hatugen} =~ s/$moji0//g;
	$in{hatugen} =~ s/</&lt;/g;$in{hatugen} =~ s/>/&gt;/g;
	$hatugen = "<hr><b><font color=#$chamoji>$chaname</font> :</b><font color=indigo> $in{hatugen} </font><font color=#$timeclr> 　 $monl/$mdayl ($wdayl) $hourl:$minl:$secl</font>\n";
	unshift(@res,$hatugen);&kakikomi;

} elsif ( $in{key} eq "hatugen" && $in{hatugen}) {
	$in{hatugen} =~ s/</&lt;/g;$in{hatugen} =~ s/>/&gt;/g;
	$hatugen = "<hr><b><font color=#$chamoji>$chaname</font> :</b> $in{hatugen} <font color=#$timeclr> 　 $monl/$mdayl ($wdayl) $hourl:$minl:$secl</font>\n";
	unshift(@res,$hatugen);&kakikomi;
}

if ( $in{key} ne "back") {
	if ( $bgurl ne "" ){
		$bgmode = "background=\"$bgurl\"";
	} else {
		$bgmode = "bgcolor=\#$bgclr";
	}

print <<HTM;
Content-type: text/html

<html><head><title>Gyagoo電子酒場</title>
<meta http-equiv="Refresh" content="60;url=chat.cgi?usrid=$in{usrid}&usrpass=$in{usrpass}">
<STYLE type="text/css">
A { text-decoration: none }
</STYLE>

</head>
<body $bgmode link=#$linkiro vlink=#$vlinkiro>
<basefont size=2 color=#$mojiiro><br>
<nobr>現在の来店者($playingkazu人):
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
&hpsaisyo;
print <<"HTM";
<center><br><br><font size=6><b>退室しました</b></font><br><br>
HTM

	if ($chatwin == 1 ) {
print <<"HTM";
そのままブラウザを閉じてください。<br><br>
HTM
	} else {
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="$chaplace" name="place">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value=" ゾーンに戻る " ></form>
</center>
HTM
	}
}

sub kakikomi {

$hatugen =~ s/(https?)\:([\w|\:\!\#\$\%\=\&\-\^\`\\\|\@\~\[\{\]\}\;\+\*\,\.\?\/]+)/
				<A href=\"$1\:$2\" target=\"_blank\">$1\:$2<\/A>/ig;


open(NOW,">$maindir/chat2$bousikts");
flock(NOW,2);
	$ttt = 0;
	while ( $ttt < 50 ) {
		print NOW $res[$ttt] ;
		$ttt ++;
	}
flock(NOW,8);
close(NOW);
}

&hpowari;
exit;