&topsisetu;
print <<"HTM";
いらっしゃいませ。<br>
お金さえ払えば、あなたの肉体を<br>
素早く、簡単に増強させてあげる事ができます。<br><br>
HTM
if ( $in{riyou} eq "1" ) {
$ryoukin1 = $chastats[9] * 15;
	if ( $chagold < $ryoukin1) {
print <<"HTM";
<b><font color=red>お金が足りません。</font></b><br>
HTM
		} else {
$ryoukin1 = $chastats[9] * 15;
$chagold -= $ryoukin1;
$maxhp = int( $chastats[9] / 15 );
$maxhp1 = int( $chalvl / 3 );
$maxhp += int(rand($maxhp1));
	if ($maxhp > 100){$maxhp = 100;}
$chastats[9] += $maxhp;

print <<"HTM";
<font color=#$chamoji><b>$chaname</b></font>の<b>最大HPが<font color=#$mojiiro3>$maxhp</font>上がった！<br><br>
HTM
}
&charadatawrt;
}

if ( $in{riyou} eq "2" ) {
$ryoukin2 = $chastats[2] * 250;
	if ( $chagold < $ryoukin2) {
print <<"HTM";
<b><font color=red>お金が足りません。</font></b><br>
HTM
		} else {
$ryoukin2 = $chastats[2] * 250;
$chagold -= $ryoukin2;
$chastats[2] ++;
print <<"HTM";
<font color=#$chamoji><b>$chaname</font>の<b><font color=darkorange>STR</font>が<font color=red>1</font>上がった！</b><br><br>
HTM
}
&charadatawrt;
}

if ( $in{riyou} eq "3" ) {
$ryoukin3 = $chastats[1] * 250;
	if ( $chagold < $ryoukin3) {
print <<"HTM";
<b><font color=red>お金が足りません。</font></b><br>
HTM
		} else {
$ryoukin3 = $chastats[1] * 250;
$chagold -= $ryoukin3;
$chastats[1] ++;
print <<"HTM";
<font color=#$chamoji><b>$chaname</font>の<b><font color=lightsalmon>AC</font>が<font color=red>1</font>上がった！</b><br><br>
HTM
}
&charadatawrt;
}

if ( $in{riyou} eq "4" ) {
$ryoukin4 = $chastats[3] * 250;
	if ( $chagold < $ryoukin4) {
print <<"HTM";
<b><font color=red>お金が足りません。</font></b><br>
HTM
		} else {
$ryoukin4 = $chastats[3] * 250;
$chagold -= $ryoukin4;
$chastats[3] ++;
print <<"HTM";
<font color=#$chamoji><b>$chaname</font>の<b><font color=orchid>AGI</font>が<font color=red>1</font>上がった！</b><br><br>
HTM
}
&charadatawrt;
}

if ( $in{riyou} eq "5" ) {
$ryoukin5 = $chastats[4] * 250;
	if ( $chagold < $ryoukin5) {
print <<"HTM";
<b><font color=red>お金が足りません。</font></b><br>
HTM
		} else {
$ryoukin5 = $chastats[4] * 250;
$chagold -= $ryoukin5;
$chastats[4] ++;
print <<"HTM";
<font color=#$chamoji><b>$chaname</font>の<b><font color=cornflowerblue>INT</font>が<font color=red>1</font>上がった！</b><br><br>
HTM
}
&charadatawrt;
}

$ryoukin1 = $chastats[9] * 15;
$ryoukin2 = $chastats[2] * 250;
$ryoukin3 = $chastats[1] * 250;
$ryoukin4 = $chastats[3] * 250;
$ryoukin5 = $chastats[4] * 250;

&kunrenform;
sub kunrenform {
print <<"HTM";
<font size=-1>現在の所持金</font>：<b>$chagold</b><font size=-1>G</font>
<form method="post" action="./$zonecgi">
<input type=hidden value="13" name="sisetu">
<input type=hidden value="1" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="　\H\P\を強化　" size=30 onClick="this.disabled=true; this.value='  お待ちください  '; this.form.submit();">　【<font color=blue><b>$ryoukin1</b></font><font size=-1>Ｇ</font>】
</form>
<form method="post" action="./$zonecgi">
<input type=hidden value="13" name="sisetu">
<input type=hidden value="2" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value=" STRを強化 " size=30 onClick="this.disabled=true; this.value='  お待ちください  '; this.form.submit();">　【<font color=blue><b>$ryoukin2</b></font><font size=-1>Ｇ</font>】
</form>
<form method="post" action="./$zonecgi">
<input type=hidden value="13" name="sisetu">
<input type=hidden value="3" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="　\A\C\を強化　" size=30 onClick="this.disabled=true; this.value='  お待ちください  '; this.form.submit();">　【<font color=blue><b>$ryoukin3</b></font><font size=-1>Ｇ</font>】
</form>
<form method="post" action="./$zonecgi">
<input type=hidden value="13" name="sisetu">
<input type=hidden value="4" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value=" AGIを強化  " size=30 onClick="this.disabled=true; this.value='  お待ちください  '; this.form.submit();">　【<font color=blue><b>$ryoukin4</b></font><font size=-1>Ｇ</font>】
</form>
<form method="post" action="./$zonecgi">
<input type=hidden value="13" name="sisetu">
<input type=hidden value="5" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value=" INTを強化  " size=30 onClick="this.disabled=true; this.value='  お待ちください  '; this.form.submit();">　【<font color=blue><b>$ryoukin5</b></font><font size=-1>Ｇ</font>】
</form>

HTM
}
&townmodori;
1;