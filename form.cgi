#!/usr/bin/perl

#�@���T�[�o�[�̐ݒ�ɍ��킹�ĕύX���Ă��������B

###############

require "./settei.cgi";
require "./cgi-lib.pl";
&ReadParse;

&cookieget;
&ipblock;
&gaibublock;
&cookieset;
&hpsaisyo;

print <<"HTM";
<SCRIPT language="JavaScript">
<!--
function fclear() {
	self.document.kotoba.hatugen.value = "";
	self.document.kotoba.hatugen.focus();
}
// -->
</SCRIPT>
<form action="./chat.cgi" name="kotoba" target="chat" onSubmit='setTimeout(&quot;fclear()&quot;,5)'>
<font size=5><b>�d�q����</b></font>
<SCRIPT language="JavaScript">
<!--
function OpenWin(){
win=window.open("./color.html","new","width=290,height=325");
}
// -->
</SCRIPT>
<div align=right>
<body><A href="javascript:OpenWin()" onFocus="this.blur()"><b><font color=palevioletred>�����F�ꗗ</font></b></a></body>
</div>
<table border=0><tr><td>
<input type="text" name="hatugen" size=40>
<input type="submit" value="   �����������[�h   ">
<input type="hidden" name="key" value="hatugen">
<input type="hidden" name="usrid" value="$in{usrid}">
<input type="hidden" name="usrpass" value="$in{usrpass}">
</form></td>
<td width=100></td><td>
<form action="./chat.cgi" name="form" target="sakaba">
<input type="submit" value="   ������o��   ">
<input type="hidden" name="key" value="back">
<input type="hidden" name="usrid" value="$in{usrid}">
<input type="hidden" name="usrpass" value="$in{usrpass}">
</form></td>
</tr></table>
�@
HTM
$value =~ tr/+/ /;
$value =~ s/%([0-9a-fA-F][0-9a-fA-F])/pack("C",hex($1))/eg;
exit;