&topsisetu;

#VER106 Start �G���f�B���O
	if ( $flag2 == 1 ) {
print <<"HTM";
�������E�E�E����A�����|�������B<br>
�����A�\\�ɗ���Ă����u���@�O�[�v��<br>
�u�o�O�v���������Ăѕ�����B<br>
�����ԁA�\\�Ƃ��ė���Ă���Ԃ�<br>
�Ăѕ����ς���Ă��܂����̂���낤�B<br><br>
����A�^�������̖ڂŊm���߂Ă݂������H<br>
�����S�̏������o���Ă���̂Ȃ�Ή��֐i�ނ��悢�B<br>
���̐�͂��̐��̉ʂĂɑ����Ă���B<br><br>
�������I<br>
�����N�����Ă��Ƃ�݂����Ă͂Ȃ�񂼁B<br>
<form method="post" action="./last.cgi">
<input type=hidden value="0" name="last">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="  ���֐i��  ">
</form>
HTM
        } elsif ( $flag2 == 2 ) {
print <<"HTM";
���������Vagoo�̐^�ӂ�m���Ă��܂������E�E�B<br><br>
���ꂩ��킵��l�Ԃ͂ǂ�����΂悢�̂��̂��B<br>
�N�ɂ��������o�Ȃ��̂����B<br>
�ȑO�A���̏d�݂ɑς���ꂸ�A<br>
���疽�������҂������قǂ���B<br><br>
���ꂩ��ǂ����邩�B<br>
����͂��厩�g�œ�����������̂���E�E�E<br>

HTM
$flag2 = 3;
&charadatawrt;
} elsif ( $in{riyou} eq "1" ) {
#if ( $in{riyou} eq "1" ) {
#VER106 End

print <<"HTM";
�ӂށB���𕷂������H<br>
<form method="post" action="./$zonecgi">
<input type=hidden value="7" name="sisetu">
<input type=hidden value="11" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=radio value="1" name="hear" checked>�푰<br>
<input type=radio value="2" name="hear">�W���u<br>
<input type=radio value="3" name="hear">�y�b�g<br>
<input type=radio value="4" name="hear">�A�C�e��<br>
<input type=radio value="5" name="hear">�]�[��<br>
<input type=radio value="6" name="hear">���@�O�[<br>
<input type=radio value="7" name="hear">�A���p�`�[<br>
<input type=radio value="8" name="hear">��̔�<br><br>
<input type=submit value="    ����    ">
</form>
HTM
	} elsif ( $in{riyou} eq "11" ) {
		if ( $in{hear} == 1 ) {
print <<"HTM";
���̐��E�ɂ͂S�̎푰���������Ă���B<br>
�@�u�l�ԁv�u����v�u��b�v�u���l�v<br>
�܁[����͐l�Ԃ�����ɂ����Ă�ł��邾�����Ⴊ�ȁB<br>
���̑��ɂ��V�푰�����邩�������̂��B<br><br>
���̎푰�Ƃ����T�O�̓y�b�g��������<br>
�傫���֌W���Ă���̂���B<br>
�o���Ă����Ƃ悢���B<br>
HTM
		} elsif ( $in{hear} == 2 ) {
print <<"HTM";
�W���u�A���Ȃ킿�E�Ƃ̂��Ƃ���B<br>
�����背�x���ɒB�����<br>
$sisetu[6] �œ]�E���邱�Ƃ��ł��邼��<br><br>
�e�W���u�ɂ͂��ꂼ�����������B<br>
���Z�A�X�e�[�^�X�A�b�v���A�A��ĕ�����y�b�g���A<br>
�����ł���d�ʂȂǂ����ꂶ��B<br><br>
�]�E��1�񂵂��ł��Ȃ��B<br>
�����炨��̂Ȃ肽���W���u��T�d�ɑI�Ԃ̂���B<br><br>
�����W���u�ɓ]�E��A����Ƀ��x�����������<br>
�㋉�W���u�ɓ]�E�ł��邼���B<br>
HTM
		} elsif ( $in{hear} == 3 ) {
print <<"HTM";
�퓬��Ƀy�b�g���l���ł��邱�Ƃ�����̂���B<br>
$sisetu[4] ����o���ĘA��ĕ�����<br>
�ꏏ�ɐ퓬�ɎQ�����Ă���邼���B<br>
�A��ĕ�����y�b�g�̍ő吔��<br>
�W���u�ɂ���ĈقȂ�̂ŋC������悤�ɁB<br>
�Ȃ�ƏW�߂��y�b�g�� $sisetu[5] ��<br>
�������邱�Ƃ��ł��邼���B<br><br>
�y�b�g�̒��ɂ͐퓬��ɂ����l���ł��Ȃ����́A<br>
�����ł����l���ł��Ȃ����̂����݂���̂���B<br>
�y�b�g�{��������̗��̖ڕW�ɂ��Ă��悢�����ȁB<br>
HTM
		} elsif ( $in{hear} == 4 ) {
print <<"HTM";
�A�C�e���͑傫���킯�Ď��̂R�ɕ������B<br>
�@�@�u����v�u����v�u�h��v<br>
����h��Ɋւ��Ă͏d�ʂƂ����T�O�����݂���B<br>
����̃W���u�ɂ���Ă͑����ł��Ȃ�����<br>
���邩������Ȃ��̂��B<br>
�܁[�����ł��Ȃ����� $sisetu[10] �ő��̖`���҂�<br>
�g���[�h����̂���̎肩�������B<br>
����ɁA�W���u��p�̃A�C�e�������݂��邻������B<br><br>
�A�C�e���{��������̗��̖ڕW�ɂ��Ă��悢�����ȁB<br>
HTM
		} elsif ( $in{hear} == 5 ) {
print <<"HTM";
���̐��E�̓]�[���ƌĂ΂����̂ŋ�؂��Ă���B<br>
�悤����Ƀ}�b�v���Ă��Ƃ���B<br><br>
���̃]�[���ֈړ�����ɂ͋K���񐔂̐퓬�����Ȃ��Ȃ���<br>
�ړ��o���Ȃ��V�X�e���ɂȂ��Ă���B<br>
�Ƃ���A�C�e�����g���Ώu�Ԉړ����\���Ⴊ�ȁB<br>
HTM
		} elsif ( $in{hear} == 6 ) {
print <<"HTM";
�������ށA������₶��B<br>
���̂Ƃ���A�킵�����t�̈Ӗ��͂킩��Ȃ��̂���B<br><br>
�܂����ʍ��󂩁A����Ƃ��V��̎푰���E�E�E�B<br>
���Ђ���ɂ�������𖾂��ė~�����̂���B<br>
�Ђ���Ƃ���Ɖ䂪�푰�u�l�ԁv��<br>
����������ׂƂȂ邩�������B<br>
��낵�����ނ����B<br>
HTM
		} elsif ( $in{hear} == 7 ) {
print <<"HTM";
�A���p�`�[�̐X�ŁA�����Z��g�ɂ܂Ƃ���<br>
�l�e��������Ă���炵���̂���B<br><br>
����͖`���҂�������Ɩ����ʂɏP���|�����Ă���炵���̂���B<br>
�������̂��B�����Ȑ��̒��ɂȂ���������B<br>
�Ƃɂ����A$chaname���A���p�`�[�̐X�ɍs������<br>
�\\���A���ӂ��Ȃ����B<br>
HTM
		} elsif ( $in{hear} == 8 ) {
print <<"HTM";
���̔��ɂ��Ēm�肽���̂��B<br>
�����Ă��������̂��Ⴊ�A���͂킵�ɂ��킩���̂���B<br><br>
���̔��͂킵�̐��܂��O���炠���ẮB<br>
�킵�̕����A���ɂ��ĉ����m���Ă���݂�������������E�E�E�B<br>
�����S�O�N�O�ɂȂ�̂��̂��E�E�E�B<br>���ǁA���̎���N�ɂ��������ʂ܂܁A���͐�������ẮB<br>
����ȗ��A���̕����͊J�����̔��ƂȂ��Ă��܂����̂���B<br>
�N�����ׂ̈ɍ��A���ɉ�������̂����A���ƂȂ��Ă͒N�ɂ��킩��Ȃ��̂���B<br>
<br><br>

HTM
		}
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="7" name="sisetu">
<input type=hidden value="1" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="   ���̘b�𕷂�  ">
</form>
HTM
	} elsif ( $in{riyou} eq "2" ) {
print <<"HTM";
�ق�A���ݓo�^����Ă���`���҂̃��X�g����B<br>
<form action="./$introcgi" target="bouken" method="post">
<input type=submit value="   �X�e�[�^�X�{��  ">
<select name="usrid">
HTM


open(CHA,"$maindir/$foldacha/user_id$bousi2cha$bousikts2");
$tourokunum = 1;
		while ( $chadata = <CHA> ) {
		chop($chadata);
		($id,$name) = split(/\//,$chadata);
print "<option value=\"$id\">$tourokunum.$name<br>";
$tourokunum ++;
		}
close(CHA);




print <<"HTM";
</select>
</form>
HTM

	} elsif ( $in{riyou} eq "6" ) {

	if ( $chastats[13] == 0 ) {
print <<"HTM";
���ꂱ��A���������ɕ�V�ȂǏo����͂����Ȃ�����낤�B<br>
��������ҁA�H���ׂ��炸�B�����B
HTM
	} else {

$chagold += $chastats[13];
print <<"HTM";
��������ȁB����̍��܂ł̓������炢���ƁE�E�E<br>
<font color=blue><font size=+2><b>$chastats[13]</font></font><font size=+2>G</font></b> ���ĂƂ�����ȁB<br>
���ꂩ����撣���ă����X�^�[��ގ����Ă�����B
</select>
</form>
HTM
$chastats[13] = 0;
&charadatawrt;
&tyourouform;
}
	} elsif ( $in{riyou} eq "3" ) {
print <<"HTM";
���܂ɂ͋C���]�����K�v����ȁB<br>
�F��I�����Ă�����B<br><br>
<form method="post" action="./$zonecgi">
<input type=hidden value="7" name="sisetu">
<input type=hidden value="31" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="   �����F�ύX  ">
<select name="mojisyoku">
<option value="000000" selected>��
<option value="dd0000">��
<option value="0000dd">��
<option value="009900">��
<option value="ffbb00">��
<option value="00aaaa">��
<option value="00bb00">����
<option value="ff55ff">��
<option value="a96800">��
<option value="af00af">��
<option value="666666">��
<option value="888800">��
<option value="ff8500">��
<option value="7800d3">��
</select></form>
HTM
	} elsif ( $in{riyou} eq "31" ) {
$chamoji = $in{mojisyoku};
&charadatawrt;
print <<"HTM";
���ށA�ύX���Ă����������B<br>
���ɂ͂ǂ�ȗp�����̂��H<br><br>
HTM
&tyourouform;
	} elsif ( $in{riyou} eq "4" ) {
print <<"HTM";
�ł͐V����URL���L�����Ȃ����B<br>
<form action="./$zonecgi" method="post">
<input type=text value="http://" size=50 name="url" maxlength=100>
<input type=submit value="   �o�^�ύX  ">
<input type=hidden value="7" name="sisetu">
<input type=hidden value="41" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
</form>
HTM
	} elsif ( $in{riyou} eq "41" ) {
$in{url} =~ s/,//g;
$chaurl = $in{url};
&charadatawrt;
print <<"HTM";
�ӂށB�ύX���Ă����������B<br>
���ɂ͂ǂ�ȗp�����̂��H<br><br>
HTM
&tyourouform;


	} elsif ( $in{riyou} eq "8" ) {
print <<"HTM";
�ł͐V�����R�����g���L�����Ȃ����B�i�S�p35�����E���p70�����ȓ��j<br>
<form action="./$zonecgi" method="post">
<input type=text value="" size=50 name="comment" maxlength=70>
<input type=submit value="  ���e�ύX  ">
<input type=hidden value="7" name="sisetu">
<input type=hidden value="81" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
</form>
HTM
	} elsif ( $in{riyou} eq "81" ) {
$in{comment} =~ s/,//g;
$maxcombo = $in{comment};
&charadatawrt;
print <<"HTM";
�ӂށB�ύX���Ă����������B<br>
���ɂ͂ǂ�ȗp�����̂��H<br><br>
HTM
&tyourouform;



	} elsif ( $in{riyou} eq "7" ) {
	if ($flag3 ) {
print <<"HTM";
���ɂ͈Í����̌����|�����Ă���B<br>
�������S���̐�������͂���ƊJ���悤���B<br>
<form action="./$zonecgi" method="post">
<input type=text value="" size=4 name="angou" maxlength=4>
<input type=submit value="�m�F">
<input type=hidden value="7" name="sisetu">
<input type=hidden value="61" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
</form>
HTM

	} else {
print <<"HTM";
���ɂ͈Í����̌����|�����Ă���B<br>
�������S���̐�������͂���ƊJ���悤���B<br>
<br>
�������A$chaname�ɂ͈Í����킩��Ȃ������E�E�E�B
HTM
}
	} elsif ( $in{riyou} eq "61" ) {
	if ( $in{angou} eq "$karistats[10]" ){
print <<"HTM";
���������͂���܂����B<br>
HTM
	} else {
print <<"HTM";
�����N����Ȃ������B<br>
HTM
}


	} elsif ( $in{riyou} eq "5" ) {
print <<"HTM";
<b><font size=+2>�y�p�X���[�h�ύX�z</font></b><br><br>
�V�K�o�^���Ɏ����������ꂽ�A<br>
<font color=red>�p�X�L�[</font>����͂��Ă��������B<br><br>
<b>���p�X���[�h�Ƃ͈قȂ�܂��B</b><br><br>
<center>
<form action="./$zonecgi" method="post">
<input type=text value="" size=5 name="angou2" maxlength=5>
<input type=submit value="�F��">
<input type=hidden value="7" name="sisetu">
<input type=hidden value="51" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<font size=-2><b>(���p�����T��)</b></font>
</form>
</center>
HTM
	} elsif ( $in{riyou} eq "51" ) {
	if ( $in{angou2} eq "$passkey" ){
print <<"HTM";
<font size=+2><b>�y�F�؂ɐ������܂����z</font></b><br><br>
���ɁA<font color=red>�V�����p�X���[�h</font>����͂��Ă��������B<br>
"�ύX"�{�^���������ƁA�p�X���[�h���ύX����܂��B<br><br>

<form action="./$zonecgi" method="post">
<input type=text value="" size=8 name="chapass" maxlength=8>
<input type=submit value="  �ύX  ">�@<font size=-1><b>(���p�p��4�`8����)</b></font>
<input type=hidden value="7" name="sisetu">
<input type=hidden value="52" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
</form>
<font color=red>
<b>�ύX�����p�X���[�h�͐�΂ɖY��Ȃ��悤�ɂ��Ă��������B</b><br>
���񂩂�́A�Â��p�X���[�h�͎g���Ȃ��Ȃ�A<br>�����Őݒ肵���p�X���[�h�ł̃��O�C���ƂȂ�܂��B</b></font><br>
HTM

	} else {
print <<"HTM";

<font size=+2><b>�y�F�؂Ɏ��s���܂����z</font></b><br><br>
�p�X�L�[���Ԉ���Ă��鋰�ꂪ����܂��B<br>
�p�X�L�[���m�F���A�ēx�����Ă݂Ă��������B<br><br>
HTM
if ( $admailyn == "1" ) {
print <<"HTM";
�p�X�L�[��Y��Ă��܂����ꍇ�́A<br><body><A href="mailto:$admail"><b>�R�`��</b></a></body>
���Ǘ��҂ɖ₢���킹�Ă��������B<br>
</span>
HTM
}
if ( $admailyn == "2" ) {
print <<"HTM";
�p�X�L�[��Y��Ă��܂����ꍇ�́A<br><body><A href="$urlbbs"><b>�f����</b></a></body>
���Ǘ��҂ɖ₢���킹�Ă��������B<br>
</span>
HTM
}
if ( $admailyn == "3" ) {
print <<"HTM";
�p�X�L�[��Y��Ă��܂����ꍇ�́A<br>�X�֋ǂ�� <body><b>$adname</b></body>
���ĂɎ莆�𑗐M���Ă��������B<br>
</span>
HTM
}
}

	} elsif ( $in{riyou} eq "52" ) {
	if(length($in{chapass}) < 4 || length($in{chapass}) > 8 ){
print <<"HTM";
�p�X���[�h�́A�K��<b><font color=red>���p�p��4�`8����</font></b>�̊ԂŎw�肵�Ă��������B<br>
<br>
HTM

	} else {
$chapass = $in{chapass};
&charadatawrt;
print <<"HTM";
<font size=+2><b>�y�ύX�����z</font></b><br><br>
�p�X���[�h�͐���ɕύX����܂����B<br>
�V�����p�X���[�h�́A�u<font color=red><b>$chapass</b></font>�v�ł��B<br>
���񂩂�́A���̃p�X���[�h�Ń��O�C�����Ă��������B<br>
<br>
HTM

}



	} else {
print <<"HTM";
�悭���Ă��ꂽ�B<br>
�ǂ�ȗp�����̂��H<br><br>
HTM
&tyourouform;
	}

sub tyourouform {
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="7" name="sisetu">
<input type=hidden value="1" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="     �b�𕷂�     ">
</form>
<form method="post" action="./$zonecgi">
<input type=hidden value="7" name="sisetu">
<input type=hidden value="6" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="   ��V�����炤   ">
</form>
<form method="post" action="./$zonecgi">
<input type=hidden value="7" name="sisetu">
<input type=hidden value="2" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="    �o�^�҈ꗗ    ">
</form>
<form method="post" action="./$zonecgi">
<input type=hidden value="7" name="sisetu">
<input type=hidden value="3" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="    �����F�ύX    ">
</form>
<form method="post" action="./$zonecgi">
<input type=hidden value="7" name="sisetu">
<input type=hidden value="4" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="    �o�^HP�ύX    ">
</form>
<form method="post" action="./$zonecgi">
<input type=hidden value="7" name="sisetu">
<input type=hidden value="5" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="   �p�X���[�h�ύX   ">
</form>
<form method="post" action="./$zonecgi">
<input type=hidden value="7" name="sisetu">
<input type=hidden value="8" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="   �R�����g�ύX   ">
</form>
<br>
<form method="post" action="./$zonecgi">
<input type=hidden value="7" name="sisetu">
<input type=hidden value="7" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="     ��̔�     ">
</form>
HTM

}
&townmodori;

1;