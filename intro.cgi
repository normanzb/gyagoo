#!/usr/bin/perl

#　↑サーバーの設定に合わせて変更してください。

require "./settei.cgi";
require "./cgi-lib.pl";
&ReadParse;
require "./zone.pl";

&charadataload;
&hpsaisyo;
print <<"HTM";
<center><font size=6 color=#$mojiiro2><b><font size=7 color=#$chamoji>$chaname
</font>さんのステータス</b></font><br><br>
<b><font size=+1>ゾーン名 [ $zone[$chaplace] ]</b></font><br><br>

HTM
&pettukitable;
&itemtable;
print <<"HTM";
</center></body></html>
HTM
exit;
