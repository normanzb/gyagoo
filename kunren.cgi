&topsisetu;
	if ( $in{riyou} eq "1" ) {
$chastats[9] = int($chastats[9] / 2 );
$chahp = $chastats[9];
$chastats[1] = int($chastats[1] / 2 );
$chastats[2] = int($chastats[2] / 2 );
$chastats[3] = int($chastats[3] / 2 );
$chastats[4] = int($chastats[4] / 2 );
$chalvl = 1;
$chaexp = 0;
$chanextlvl = 5;
$strexp /= 20;
$acexp /= 20;
$agiexp /= 20;
$intexp /= 20;
$nowstrexp = 0;
$nowacexp = 0;
$nowagiexp = 0;
$nowintexp = 0;
$chagold -= $tenseigold;
$newtegami = 1;
$tensei ++;
&charadatawrt;
print <<"HTM";
それでは、これより転生の儀式を始めます。<br>
目を閉じてください。<br><br>
<font color=#$chamoji><b>神よ、$chanameに新たな人生を歩ませたまえ！</b></font><br><br>
・<br>
・<br>
・<br>
・<br>
無事に転生が終了しました。<br>
更なる高みを目指し、これからも修行に励みなさい。<br>
HTM

	} else {
while($tenseigold =~ s/(.*\d)(\d\d\d)/$1,$2/){} ;
print <<"HTM";
ここは教会。<br>
この世界で 更なる高みを目指す者が集う場所。<br><br>
<b> Lv$tenseilv</b> と <b><font color=blue>$tenseigold</font>G</b>の寄付があれば、<br>
転生の儀式を受ける事が出来ます。<br><br>
HTM
		if ( $chalvl >= $tenseilv && $chagold >= $tenseigold ){
print <<"HTM";
<b><font color=#$chamoji>$chaname</font></b> よ・・・・<br>
相当な修練を積んできたようですね。<br>
貴方には 転生の儀式を受ける資格があるようです。<br>
<br>
<font color=red>※ 転生をすると、レベルが１に戻り、<br>
最大HP、STR、AC、AGI、INTが半分になりますが、<br>
ステータスの上昇率が早くなり、より強いキャラに育てる事が出来ます。<br>
ジョブデータはそのまま引き継がれます。</font><br>
<br>
<form method="post" action="./$zonecgi">
<input type=hidden value="12" name="sisetu">
<input type=hidden value="1" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="     転生する     ">
</form><br>
HTM

		} else {
print <<"HTM";
しかし、あなたはまだ、<br>
転生の儀式を受けるに相応しい経験を積んでいないようです。<br>
神よ、$chanameにご加護を。<br><br>
HTM
		}
}
&townmodori;

1;