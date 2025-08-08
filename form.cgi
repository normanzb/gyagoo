#!/usr/bin/perl

#　↑サーバーの設定に合わせて変更してください。

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
<font size=5><b>電子酒場</b></font>
<SCRIPT language="JavaScript">
<!--
function OpenWin(){
win=window.open("./color.html","new","width=290,height=325");
}
// -->
</SCRIPT>
<div align=right>
<body><A href="javascript:OpenWin()" onFocus="this.blur()"><b><font color=palevioletred>発言色一覧</font></b></a></body>
</div>
<table border=0><tr><td>
<input type="text" name="hatugen" size=40>
<input type="submit" value="   発言＆リロード   ">
<input type="hidden" name="key" value="hatugen">
<input type="hidden" name="usrid" value="$in{usrid}">
<input type="hidden" name="usrpass" value="$in{usrpass}">
</form></td>
<td width=100></td><td>
<form action="./chat.cgi" name="form" target="sakaba">
<input type="submit" value="   酒場を出る   ">
<input type="hidden" name="key" value="back">
<input type="hidden" name="usrid" value="$in{usrid}">
<input type="hidden" name="usrpass" value="$in{usrpass}">
</form></td>
</tr></table>
　
HTM
$value =~ tr/+/ /;
$value =~ s/%([0-9a-fA-F][0-9a-fA-F])/pack("C",hex($1))/eg;
exit;