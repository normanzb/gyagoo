&topsisetu;
print <<"HTM";
��������Ⴂ�܂��B<br>
�������������΁A���Ȃ��̓��̂�<br>
�f�����A�ȒP�ɑ��������Ă����鎖���ł��܂��B<br><br>
HTM
if ( $in{riyou} eq "1" ) {
$ryoukin1 = $chastats[9] * 15;
	if ( $chagold < $ryoukin1) {
print <<"HTM";
<b><font color=red>����������܂���B</font></b><br>
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
<font color=#$chamoji><b>$chaname</b></font>��<b>�ő�HP��<font color=#$mojiiro3>$maxhp</font>�オ�����I<br><br>
HTM
}
&charadatawrt;
}

if ( $in{riyou} eq "2" ) {
$ryoukin2 = $chastats[2] * 250;
	if ( $chagold < $ryoukin2) {
print <<"HTM";
<b><font color=red>����������܂���B</font></b><br>
HTM
		} else {
$ryoukin2 = $chastats[2] * 250;
$chagold -= $ryoukin2;
$chastats[2] ++;
print <<"HTM";
<font color=#$chamoji><b>$chaname</font>��<b><font color=darkorange>STR</font>��<font color=red>1</font>�オ�����I</b><br><br>
HTM
}
&charadatawrt;
}

if ( $in{riyou} eq "3" ) {
$ryoukin3 = $chastats[1] * 250;
	if ( $chagold < $ryoukin3) {
print <<"HTM";
<b><font color=red>����������܂���B</font></b><br>
HTM
		} else {
$ryoukin3 = $chastats[1] * 250;
$chagold -= $ryoukin3;
$chastats[1] ++;
print <<"HTM";
<font color=#$chamoji><b>$chaname</font>��<b><font color=lightsalmon>AC</font>��<font color=red>1</font>�オ�����I</b><br><br>
HTM
}
&charadatawrt;
}

if ( $in{riyou} eq "4" ) {
$ryoukin4 = $chastats[3] * 250;
	if ( $chagold < $ryoukin4) {
print <<"HTM";
<b><font color=red>����������܂���B</font></b><br>
HTM
		} else {
$ryoukin4 = $chastats[3] * 250;
$chagold -= $ryoukin4;
$chastats[3] ++;
print <<"HTM";
<font color=#$chamoji><b>$chaname</font>��<b><font color=orchid>AGI</font>��<font color=red>1</font>�オ�����I</b><br><br>
HTM
}
&charadatawrt;
}

if ( $in{riyou} eq "5" ) {
$ryoukin5 = $chastats[4] * 250;
	if ( $chagold < $ryoukin5) {
print <<"HTM";
<b><font color=red>����������܂���B</font></b><br>
HTM
		} else {
$ryoukin5 = $chastats[4] * 250;
$chagold -= $ryoukin5;
$chastats[4] ++;
print <<"HTM";
<font color=#$chamoji><b>$chaname</font>��<b><font color=cornflowerblue>INT</font>��<font color=red>1</font>�オ�����I</b><br><br>
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
<font size=-1>���݂̏�����</font>�F<b>$chagold</b><font size=-1>G</font>
<form method="post" action="./$zonecgi">
<input type=hidden value="13" name="sisetu">
<input type=hidden value="1" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="�@\H\P\�������@" size=30 onClick="this.disabled=true; this.value='  ���҂���������  '; this.form.submit();">�@�y<font color=blue><b>$ryoukin1</b></font><font size=-1>�f</font>�z
</form>
<form method="post" action="./$zonecgi">
<input type=hidden value="13" name="sisetu">
<input type=hidden value="2" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value=" STR������ " size=30 onClick="this.disabled=true; this.value='  ���҂���������  '; this.form.submit();">�@�y<font color=blue><b>$ryoukin2</b></font><font size=-1>�f</font>�z
</form>
<form method="post" action="./$zonecgi">
<input type=hidden value="13" name="sisetu">
<input type=hidden value="3" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="�@\A\C\�������@" size=30 onClick="this.disabled=true; this.value='  ���҂���������  '; this.form.submit();">�@�y<font color=blue><b>$ryoukin3</b></font><font size=-1>�f</font>�z
</form>
<form method="post" action="./$zonecgi">
<input type=hidden value="13" name="sisetu">
<input type=hidden value="4" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value=" AGI������  " size=30 onClick="this.disabled=true; this.value='  ���҂���������  '; this.form.submit();">�@�y<font color=blue><b>$ryoukin4</b></font><font size=-1>�f</font>�z
</form>
<form method="post" action="./$zonecgi">
<input type=hidden value="13" name="sisetu">
<input type=hidden value="5" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value=" INT������  " size=30 onClick="this.disabled=true; this.value='  ���҂���������  '; this.form.submit();">�@�y<font color=blue><b>$ryoukin5</b></font><font size=-1>�f</font>�z
</form>

HTM
}
&townmodori;
1;