#!/usr/bin/perl

#�@���T�[�o�[�̐ݒ�ɍ��킹�ĕύX���Ă��������B

require "./settei.cgi";
require "./cgi-lib.pl";
&ReadParse;

&cookieget;
&ipblock;
&cookieset;

print <<"HTM";
Content-type: text/html

<html><head><title>Gyagoo�d�q����</title></head>
<frameset border=0 rows="100,*">
<frame src="./form.cgi?usrid=$in{usrid}&usrpass=$in{usrpass}" name="bar" noresize scrolling=no>
<frame src="./chat.cgi?usrid=$in{usrid}&usrpass=$in{usrpass}&key=enter" name="chat" noresize>
HTM

exit;