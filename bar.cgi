#!/usr/bin/perl

#　↑サーバーの設定に合わせて変更してください。

require "./settei.cgi";
require "./cgi-lib.pl";
&ReadParse;

&cookieget;
&ipblock;
&cookieset;

print <<"HTM";
Content-type: text/html

<html><head><title>Gyagoo電子酒場</title></head>
<frameset border=0 rows="100,*">
<frame src="./form.cgi?usrid=$in{usrid}&usrpass=$in{usrpass}" name="bar" noresize scrolling=no>
<frame src="./chat.cgi?usrid=$in{usrid}&usrpass=$in{usrpass}&key=enter" name="chat" noresize>
HTM

exit;