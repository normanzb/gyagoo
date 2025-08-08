#!/usr/bin/perl

#　↑サーバーの設定に合わせて変更してください。

require "./settei.cgi";
require "./cgi-lib.pl";
&ReadParse;

&cookieget;
&ipblock;
&gaibublock;
&proxychk;

&charadataload;


if ( $chapass ne $in{usrpass} ) {
&CgiError('<body background="./pics/Image11.gif"><body bgcolor=snow link=snow vlink=snow><font color=silver><center>パスワードエラー','<font color=white><b>パスワードが違います。<br>再度ログイン画面からやり直してください。</b><br><br>');exit;}
if (length($in{usrpass}) < 1 ) { &CgiError('<body background="./pics/Image11.gif"><font color=silver><center>パスワードエラー','<font color=white><b>パスワードが入力されていませんでした。<br>再度ログイン画面からやり直してください。</b><br><br>');exit;}
&cookieset;

require "./zone.pl";

@movin = split(/\//,$move[$chaplace]);
$moveok = 0;
	if( $in{place} != $chaplace && $in{place} ne "") {
		foreach $moved (@movin) {
			if ($moved == $in{place} ) {
				$moveok = 1;$chaplace = $moved;$chacount = $kiteisentou;&charadatawrt;last;
			}
		}
	if ( $moveok != 1 ) { &fuseisyori; }
	}
&hpsaisyo;

if ( $chaplace eq "0" ){
require "./$towncgi";exit;
} elsif ( $chaplace eq "200" ){
require "./$town2cgi";exit;
} elsif ( $chaplace eq "201" ){
require "./$town3cgi";exit;
} elsif ( $chaplace eq "115" ){
require "./$town4cgi";exit;
} elsif ( $chaplace eq "202" ){
require "./$town5cgi";exit;

} elsif ( $chaplace eq "151" ){
require "./$boss2cgi";exit;

} elsif ( $chaplace eq "27" ){
require "./$bosscgi";exit;
} elsif ( $chaplace eq "108" ){
require "./$boss3cgi";exit;
} elsif ( $chaplace eq "123" ){
require "./$boss4cgi";exit;
} elsif ( $chaplace eq "114" ){
require "./$boss5cgi";exit;
} elsif ( $chaplace eq "148" ){
require "./$boss6cgi";exit;
} elsif ( $chaplace eq "149" ){
require "./$boss7cgi";exit;
} elsif ( $chaplace eq "150" ){
require "./$boss8cgi";exit;
} elsif ( $chaplace eq "500" ){
require "./$boss10cgi";exit;
} else {


require "./$fieldcgi";
&hpowari;

}
exit;
