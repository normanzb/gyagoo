#!/usr/bin/perl

#�@���T�[�o�[�̐ݒ�ɍ��킹�ĕύX���Ă��������B

require "./settei.cgi";
require "./cgi-lib.pl";
&ReadParse;
require "./zone.pl";

&charadataload;
&hpsaisyo;
print <<"HTM";
<center><font size=6 color=#$mojiiro2><b><font size=7 color=#$chamoji>$chaname
</font>����̃X�e�[�^�X</b></font><br><br>
<b><font size=+1>�]�[���� [ $zone[$chaplace] ]</b></font><br><br>

HTM
&pettukitable;
&itemtable;
print <<"HTM";
</center></body></html>
HTM
exit;
