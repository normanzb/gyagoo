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
����ł́A������]���̋V�����n�߂܂��B<br>
�ڂ���Ă��������B<br><br>
<font color=#$chamoji><b>�_��A$chaname�ɐV���Ȑl������܂����܂��I</b></font><br><br>
�E<br>
�E<br>
�E<br>
�E<br>
�����ɓ]�����I�����܂����B<br>
�X�Ȃ鍂�݂�ڎw���A���ꂩ����C�s�ɗ�݂Ȃ����B<br>
HTM

	} else {
while($tenseigold =~ s/(.*\d)(\d\d\d)/$1,$2/){} ;
print <<"HTM";
�����͋���B<br>
���̐��E�� �X�Ȃ鍂�݂�ڎw���҂��W���ꏊ�B<br><br>
<b> Lv$tenseilv</b> �� <b><font color=blue>$tenseigold</font>G</b>�̊�t������΁A<br>
�]���̋V�����󂯂鎖���o���܂��B<br><br>
HTM
		if ( $chalvl >= $tenseilv && $chagold >= $tenseigold ){
print <<"HTM";
<b><font color=#$chamoji>$chaname</font></b> ��E�E�E�E<br>
�����ȏC����ς�ł����悤�ł��ˁB<br>
�M���ɂ� �]���̋V�����󂯂鎑�i������悤�ł��B<br>
<br>
<font color=red>�� �]��������ƁA���x�����P�ɖ߂�A<br>
�ő�HP�ASTR�AAC�AAGI�AINT�������ɂȂ�܂����A<br>
�X�e�[�^�X�̏㏸���������Ȃ�A��苭���L�����Ɉ�Ă鎖���o���܂��B<br>
�W���u�f�[�^�͂��̂܂܈����p����܂��B</font><br>
<br>
<form method="post" action="./$zonecgi">
<input type=hidden value="12" name="sisetu">
<input type=hidden value="1" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="     �]������     ">
</form><br>
HTM

		} else {
print <<"HTM";
�������A���Ȃ��͂܂��A<br>
�]���̋V�����󂯂�ɑ��������o����ς�ł��Ȃ��悤�ł��B<br>
�_��A$chaname�ɂ�������B<br><br>
HTM
		}
}
&townmodori;

1;