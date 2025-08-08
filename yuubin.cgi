&topsisetu;
($sec,$min,$hour,$mday,$mon,$year,$wday) = localtime(time);
$year = $year + 1900;$mon ++;
@youbi = ('日','月','火','水','木','金','土');
if ( length($min) == 1 ) { $min = "0$min"; }
$genzai ="$year年$mon月$mday日($youbi[$wday]) $hour:$min";

if ( $in{riyou} eq "1" ) {
	if ( $chagold < 200 ) {
print <<"HTM";
振込金額は200 G 以上です。<br>
所持金を十\分にお持ちでないようですね。<br><br>
他にもご用件はございますか？<br>
HTM
&yuubinform;
	} else {
print <<"HTM";
送り先と所持金を指定してください。<br>
<form action="./$zonecgi" method="post">
<input type=hidden value="10" name="sisetu">
<input type=hidden value="11" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<select name="chara">
HTM

open(CHA,"$maindir/$foldacha/user_id$bousi2cha$bousikts2");
$tourokunum = 1;
		while ( $chadata = <CHA> ) {
		chop($chadata);
		($id,$name) = split(/\//,$chadata);
			if ( $name ne $chaname) {
print "<option value=\"$id\">$tourokunum.$name<br>";
$tourokunum ++;
			}
		}
close(CHA);
print <<"HTM";
<SCRIPT language="JavaScript">
<!--
function Check(){
if(confirm("よろしいですか？")){

}
else{
return false; }
}
// -->
</SCRIPT>
</select>
<br><br>

<head> 
<script language="JavaScript"> 
<!-- 
document.onkeydown = KeyEvent;     
self.focus();                       
function KeyEvent(e){   
    pressKey=event.keyCode;   
     if(pressKey==13){return false;} 
} 
//--> 
</script> 
</head> 
<html> 
<body> 
<form action="b.html"  >

<input type=text size=10 value="" name="kingaku" maxlength=30>(200 G 以上)<br><br>
<input type=submit value="       振込      " onClick="this.disabled=true; this.value='  お待ちください  '; this.form.submit();">
</form></td><td width=30></td><td>

</body> 
</html> 
HTM
	}

} elsif ( $in{riyou} eq "11" ) {
#VER106 Start 正規表現
	if ( $in{kingaku} =~ /^[0-9]+$/ )
	{
#	$furikomi = int ( $in{kingaku} );
#VER106 End
$furikomi = int ( $in{kingaku} );
	if ( $furikomi < 200 || $in{kingaku} eq "" || $chagold < $furikomi ) { &fuseisyori;exit; }
open(BANK,"$maindir/$foldacha/bankg_$in{chara}$bousi2cha$bousikts");
	$bankgold = <BANK>;
close(BANK);

open(CHA,"$maindir/$foldacha/user_id$bousi2cha$bousikts2");
		while ( $chadata = <CHA> ) {
		chop($chadata);
		($id,$in{name}) = split(/\//,$chadata);
		}
close(CHA);

	$bankgold += $furikomi;
open(BANK,">$maindir/$foldacha/bankg_$in{chara}$bousi2cha$bousikts");
	print BANK "$bankgold";
close(BANK);
$chagold -= $furikomi;
&charadatawrt;


$furikomi = &put_comma($furikomi);

open(BAN,">>$maindir/$foldacha/tegami3_$in{chara}.tmp");
flock(BAN,2);


print BAN "$now\t郵便局\t$mojiiro3\t<b><font color=#$mojiiro3><font color=#$chamoji>$chaname</font> さんから <font color=#$mojiiro2>$furikomi</font> G 振込まれました。</b></font>\t$genzai\t\n";
	open(BANN,"$maindir/$foldacha/tegami_$in{chara}$bousi2cha$bousikts");
		while ( $yuubin = <BANN> ) {
		print BAN "$yuubin";
		}
	close(BANN);


open(BAN,">>$maindir/$foldacha/tegami2_$chaid.tmp");
flock(BAN,2);
print BAN "$now\t郵便局\t$mojiiro4\t<b><font color=#$mojiiro4>ID『<font color=#$chamoji>$in{chara}</font>』に <font color=#$mojiiro2>$furikomi</font> Gを振込みました。</b></font>\t$genzai\t\n";

		while ( $yuubin = <BANN> ) {
		print BAN "$yuubin";
		}


	close(BANN);


flock(BAN,8);
close(BAN);

rename("$maindir/$foldacha/tegami3_$in{chara}.tmp","$maindir/$foldacha/tegami_$in{chara}$bousi2cha$bousikts");

print <<"HTM";
確かにお振込いたしました。<br><br>
他にもご用件はございますか？<br>
HTM
&yuubinform;

#VER106 Start 正規表現
	}
	else
	{
		&fuseisyori;
	}
#VER106 End





} elsif ( $in{riyou} eq "5" ) {
	if ( $hukubiki < 1 ) {
print <<"HTM";
福引券を一枚もお持ちでないようですね。<br><br>
他にもご用件はございますか？<br>
HTM
&yuubinform;
	} else {
print <<"HTM";
送り先と枚数を指定してください。<br>
<form action="./$zonecgi" method="post">
<input type=hidden value="10" name="sisetu">
<input type=hidden value="21" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<select name="chara">
HTM

open(CHA,"$maindir/$foldacha/user_id$bousi2cha$bousikts2");
$tourokunum = 1;
		while ( $chadata = <CHA> ) {
		chop($chadata);
		($id,$name) = split(/\//,$chadata);
			if ( $name ne $chaname) {
print "<option value=\"$id\">$tourokunum.$name<br>";
$tourokunum ++;
			}
		}
close(CHA);
print <<"HTM";
<SCRIPT language="JavaScript">
<!--
function Check(){
if(confirm("よろしいですか？")){

}
else{
return false; }
}
// -->
</SCRIPT>

</select>
<br><br>

<head> 
<script language="JavaScript"> 
<!-- 
document.onkeydown = KeyEvent;     
self.focus();                       
function KeyEvent(e){   
    pressKey=event.keyCode;   
     if(pressKey==13){return false;} 
} 
//--> 
</script> 
</head> 
<html> 
<body> 
<form action="b.html"  > 
<input type=text size=3 value="" name="kingaku" maxlength=30>枚<br><br>
<input type=submit value="       確認      " onClick="this.disabled=true; this.value='  お待ちください  '; this.form.submit();">
</form></td><td width=30></td><td>
</body> 
</html>
HTM
	}

} elsif ( $in{riyou} eq "21" ) {
#VER106 Start 正規表現
	if ( $in{kingaku} =~ /^[0-9]+$/ )
	{
#	$furikomi = int ( $in{kingaku} );
#VER106 End
$furikomi = int ( $in{kingaku} );
	if ( $furikomi < 1 || $in{kingaku} eq "" || $hukubiki < $furikomi ) { &fuseisyori;exit; }
open(BANK,"$maindir/$foldacha/hukubiki_$in{chara}$bousi2cha$bousikts");
	$bankhukubiki = <BANK>;
close(BANK);

open(CHA,"$maindir/$foldacha/user_id$bousi2cha$bousikts2");
		while ( $chadata = <CHA> ) {
		chop($chadata);
		($id,$in{name}) = split(/\//,$chadata);
		}
close(CHA);

	$bankhukubiki += $furikomi;
open(BANK,">$maindir/$foldacha/hukubiki_$in{chara}$bousi2cha$bousikts");
	print BANK "$bankhukubiki";
close(BANK);
$hukubiki -= $furikomi;
&charadatawrt;

open(BAN,">>$maindir/$foldacha/tegami3_$in{chara}.tmp");
flock(BAN,2);


print BAN "$now\t郵便局\t$mojiiro3\t<b><font color=#$mojiiro3><font color=#$chamoji>$chaname</font> さんから <font color=brown>福引券 </font>が <font color=#$mojiiro2>$furikomi</font> 枚 届けられました。</b></font>\t$genzai\t\n";
	open(BANN,"$maindir/$foldacha/tegami_$in{chara}$bousi2cha$bousikts");
		while ( $yuubin = <BANN> ) {
		print BAN "$yuubin";
		}
	close(BANN);


open(BAN,">>$maindir/$foldacha/tegami2_$chaid.tmp");
flock(BAN,2);
print BAN "$now\t郵便局\t$mojiiro4\t<b><font color=#$mojiiro4>ID『<font color=#$chamoji>$in{chara}</font>』に <font color=brown>福引券</font>を <font color=#$mojiiro2>$furikomi</font> 枚を振込みました。</b></font>\t$genzai\t\n";

		while ( $yuubin = <BANN> ) {
		print BAN "$yuubin";
		}


	close(BANN);


flock(BAN,8);
close(BAN);

rename("$maindir/$foldacha/tegami3_$in{chara}.tmp","$maindir/$foldacha/tegami_$in{chara}$bousi2cha$bousikts");

print <<"HTM";
確かにお送りいたしました。<br><br>
他にもご用件はございますか？<br>
HTM
&yuubinform;

#VER106 Start 正規表現
	}
	else
	{
		&fuseisyori;
	}
#VER106 End




} elsif ( $in{riyou} eq "2" ) {
	$ccc = 1;$ccb = 0;
	while ( $ccc < 9 ) {
		if ( $chaitem[$ccc] eq "" ) {
		$ccb ++;
		}
		$ccc ++;

	}
	if ( $ccb == 8 ) {
print <<"HTM";
送るためのアイテムを<br>
何もお持ちではないようですね。<br><br>
他にもご用件はございますか？<br>
HTM
&yuubinform;
	} else {
print <<"HTM";
送り先とアイテムを指定してください。<br>
<form action="./$zonecgi" method="post">
<input type=hidden value="10" name="sisetu">
<input type=hidden value="31" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<select name="chara">
HTM

open(CHA,"$maindir/$foldacha/user_id$bousi2cha$bousikts2");
$tourokunum = 1;
		while ( $chadata = <CHA> ) {
		chop($chadata);
		($id,$name) = split(/\//,$chadata);
			if ( $name ne $chaname) {
print "<option value=\"$id\">$tourokunum.$name<br>";
$tourokunum ++;
			}
		}
close(CHA);
print <<"HTM";
</select>
<br><br><select name="itemnum">
HTM
		$ccc = 1;
		while ( $ccc < 9 ) {
			if ( $chaitem[$ccc] ne "" ) {
			print "<option value=\"$ccc\">$chaitem[$ccc] ($chasetumei[$ccc])";
			}
			$ccc ++;
		}
print <<"HTM";
<SCRIPT language="JavaScript">
<!--
function Check(){
if(confirm("よろしいですか？")){

}
else{
return false; }
}
// -->
</SCRIPT>
</select><br><br>
<input type=submit value="      送る      " onClick="this.disabled=true; this.value='  お待ちください  '; this.form.submit();">
</form></td><td width=30></td><td>
HTM
	}
} elsif ( $in{riyou} eq "31" ) {
	if ( $chaitem[$in{itemnum}] eq "" ) { &fuseisyori;exit; }

open(BANKI,"$maindir/$foldacha/bankit_$in{chara}$bousi2cha$bousikts");
  @item = <BANKI>;
close(BANKI);
  $itemsousuu = @item;
        if ( $itemsousuu >= 100 ) {
          
print <<"HTM";
送り先のバンクがいっぱいのようです。<br>
送ることができませんでした。<br><br>
HTM
        }else{

open(BANKI,">>$maindir/$foldacha/bankit_$in{chara}$bousi2cha$bousikts");
flock(BANKI,2);
	print BANKI "$chaitem[$in{itemnum}]/$chasetumei[$in{itemnum}]\n";
flock(BANKI,8);
close(BANKI);

open(BAN,">>$maindir/$foldacha/tegami4_$in{chara}.tmp");
flock(BAN,2);
print BAN "$now\t郵便局\t$mojiiro3\t<b><font color=#$mojiiro3><font color=#$chamoji>$chaname</font> さんから<font color=#$mojiiro2>「 $chaitem[$in{itemnum}] 」</font>が届けられました。</b></font>\t$genzai\t\n";
	open(BANN,"$foldacha/tegami_$in{chara}$bousi2cha$bousikts");
		while ( $yuubin = <BANN> ) {
		print BAN "$yuubin";
		}
	close(BANN);



open(BAN,">>$maindir/$foldacha/tegami2_$chaid.tmp");
flock(BAN,2);
print BAN "$now\t郵便局\t$mojiiro4\t<b><font color=#$mojiiro4>ID『<font color=#$chamoji>$in{chara}</font>』に<font color=#$mojiiro2>「 $chaitem[$in{itemnum}] 」</font>を送りました。</b></font>\t$genzai\t\n";

		while ( $yuubin = <BANN> ) {
		print BAN "$yuubin";
		}
	close(BANN);

rename("$maindir/$foldacha/tegami4_$in{chara}.tmp","$maindir/$foldacha/tegami_$in{chara}$bousi2cha$bousikts");


	if ( $chaeff[$in{itemnum}] > 1 ) {
$chaeff[$in{itemnum}] --;
	} else {
$chaitem[$in{itemnum}] = $chaeff[$in{itemnum}] = $chasetumei[$in{itemnum}] = "";
	}

&charadatawrt;

print <<"HTM";
確かにお送りいたしました。<br>
他にもご用件はございますか？<br><br>
HTM
        }
&yuubinform;

} elsif ( $in{riyou} eq "3" ) {
	$ccc = 0; $ccb = 0;
	while ( $ccb < 3 ) {
		if ( $petcode[$ccb] ne "" ) {
		$ccc = 1; last;
		}
	$ccb ++;
	}

	if ( $ccc == 0 ) {
print <<"HTM";
送るペットを連れ歩いていませんね。<br><br>
他にもご用件はございますか？<br><br>
HTM
&yuubinform;
	} else {
print <<"HTM";
送り先とペットを指定してください。<br><br>
<form action="./$zonecgi" method="post">
<input type=hidden value="10" name="sisetu">
<input type=hidden value="41" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<select name="chara">
HTM

open(CHA,"$maindir/$foldacha/user_id$bousi2cha$bousikts2");
$tourokunum = 1;
		while ( $chadata = <CHA> ) {
		chop($chadata);
		($id,$name) = split(/\//,$chadata);
			if ( $name ne $chaname) {
print "<option value=\"$id\">$tourokunum.$name<br>";
$tourokunum ++;
			}
		}
close(CHA);
print <<"HTM";
</select>
<br><br>

HTM
$waa = 0;$waw =1;
		while ( $waa < 3 ) {
			if ( $petcode[$waa] ne "" ) {
print "<input type=radio name=\"petnum\" value=\"$waa\" checked>$waw番目：<font size=4><b>$petname[$waa]</b></font> ($petcode[$waa])<br>";
			}
$waa ++;$waw ++;
		}

	}
print <<"HTM";
<SCRIPT language="JavaScript">
<!--
function Check(){
if(confirm("よろしいですか？")){

}
else{
return false; }
}
// -->
</SCRIPT>
<br><br>
<input type=submit value="      送る      "  onClick="this.disabled=true; this.value='  お待ちください  '; this.form.submit();">
</form></td><td width=30></td><td>
HTM

} elsif ( $in{riyou} eq "41" ) {
	if ( $petcode[$in{petnum}] eq "" ) { &fuseisyori;exit; }
$bub = 0;
open(PET,"$maindir/$foldacha/pet_$in{chara}$bousi2cha$bousikts");
	while ( $petti = <PET> ) {
          $petsousuu++;
		chop($petti);
		if ( $petti eq $petcode[$in{petnum}] ) {
$bub = 1;last;
		}
	}
close(PET);

	if ( $bub == 1 ) {
print <<"HTM";
送り先にすでにそのペットは存在するため<br>
送れませんでした。<br>
他にもご用件はございますか？<br><br>
HTM

	} else {
             if($petsousuu >= 200 ) {
print <<"HTM";
送り先にすでにペット小屋がいっぱいのため<br>
送れませんでした。<br>
他にもご用件はございますか？<br><br>
HTM

             }else{
open(PET,">>$maindir/$foldacha/pet_$in{chara}$bousi2cha$bousikts");
flock(PET,2);
	print PET "$petcode[$in{petnum}]\n";
flock(PET,8);
close(PET);


open(BAN,">>$maindir/$foldacha/tegami5_$in{chara}.tmp");
flock(BAN,2);
print BAN "$now\t郵便局\t$mojiiro3\t<b><font color=#$mojiiro3><font color=#$chamoji>$chaname</font> さんから<font color=#$mojiiro2>「 $petcode[$in{petnum}] 」</font>が届けられました。</b></font>\t$genzai\t\n";
	open(BANN,"$foldacha/tegami_$in{chara}$bousi2cha$bousikts");
		while ( $yuubin = <BANN> ) {
		print BAN "$yuubin";
		}
	close(BANN);

open(CHA2,"$maindir/$foldacha/user_id$bousi2cha$bousikts2");
		while ( $chadata = <CHA2> ) {
		chop($chadata);
		($id,$name) = split(/\//,$chadata);
	}
close(CHA2);


open(BAN,">>$maindir/$foldacha/tegami2_$chaid.tmp");
flock(BAN,2);
print BAN "$now\t郵便局\t$mojiiro4\t<b><font color=#$mojiiro4>ID『<font color=#$chamoji>$in{chara}</font>』に <font color=#$mojiiro2>「 $petcode[$in{petnum}] 」</font> を送りました。</b></font>\t$genzai\t\n";

		while ( $yuubin = <BANN> ) {
		print BAN "$yuubin";
		}
	close(BANN);
flock(BAN,8);
close(BAN);

rename("$maindir/$foldacha/tegami5_$in{chara}.tmp","$maindir/$foldacha/tegami_$in{chara}$bousi2cha$bousikts");


$petcode[$in{petnum}] = $petpic[$in{petnum}] = $petritu[$in{petnum}] = $petname[$in{petnum}] = $petkouka[$in{petnum}] = $petkouka2[$in{petnum}] = $petlv[$in{petnum}] = "";
$petexp[$in{petnum}] = 10;
$petnowexp[$in{petnum}] = 0;
&charadatawrt;
print <<"HTM";
確かにお送りいたしました。<br>
他にもご用件はございますか？<br><br>
HTM
               }
        }
&yuubinform;

} elsif ( $in{riyou} eq "4" ) {
print <<"HTM";
送り先と内容をお願い致します。<br>
<form action="./$zonecgi" method="post">
<input type=hidden value="10" name="sisetu">
<input type=hidden value="51" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<select name="chara">
HTM

open(CHA,"$maindir/$foldacha/user_id$bousi2cha$bousikts2");
$tourokunum = 1;
		while ( $chadata = <CHA> ) {
		chop($chadata);
		($id,$name) = split(/\//,$chadata);
			if ( $name ne $chaname) {
print "<option value=\"$id\">$tourokunum.$name<br>";
$tourokunum ++;
			}
		}
close(CHA);
print <<"HTM";
</select>
<br><br>
<input type=text size=50 value="" name="tegami">(100文字以内)<br><br>
<input type=submit value="      送る      " onClick="this.disabled=true; this.value='  お待ちください  '; this.form.submit();">
</form>
HTM


} elsif ( $in{riyou} eq "51" ) {
	if ( $in{tegami} eq "" ) {
print <<"HTM";
手紙の内容が書かれていませんね。<br>
他にもご用件はございますか？<br><br>
HTM
&yuubinform;
	} elsif( length($in{tegami}) > 200 ) {
print <<"HTM";
文字数が１００文字を越えています。<br>
他にもご用件はございますか？<br><br>
HTM
&yuubinform;

	} else {
$in{tegami} =~ s/</&lt;/g;
$in{tegami} =~ s/>/&gt;/g;
$tegaminaiyou =  "$now\t$chaname\t$chamoji\t$in{tegami}\t$genzai\t\n";

open(BAN,"$maindir/$foldacha/tegami_$in{chara}$bousi2cha$bousikts");
   @letters = <BAN>;
close(BAN);
$letter = @letter;
           if ( $letter >= 20 ) {
              $letters[0] = "";
           }
unshift(@letters,"$now\t$chaname\t$chamoji\t$in{tegami}\t$genzai\t\n");
open(BAN,">$maindir/$foldacha/tegami_$in{chara}$bousi2cha$bousikts");
flock(BAN,2);
   print BAN @letters;
flock(BAN,8);
close(BAN);

print <<"HTM";
手紙は無事届けられました。<br><br>
他にもご用件はございますか？<br><br>
HTM
&yuubinform;

     }

} else {
print <<"HTM";
いらっしゃませ。<br>
ご用件をどうぞ。<br><br>
HTM
&yuubinform;
print <<"HTM";
</td><td width=30></td><td>
HTM

}

sub yuubinform {
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="10" name="sisetu">
<input type=hidden value="1" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="所持金を振り込む" onClick="this.disabled=true; this.value='  お待ちください  '; this.form.submit();">
</form>
<form method="post" action="./$zonecgi">
<input type=hidden value="10" name="sisetu">
<input type=hidden value="2" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="   アイテムを送る   " onClick="this.disabled=true; this.value='  お待ちください  '; this.form.submit();">
</form>
<form method="post" action="./$zonecgi">
<input type=hidden value="10" name="sisetu">
<input type=hidden value="3" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="    ペットを送る    " onClick="this.disabled=true; this.value='  お待ちください  '; this.form.submit();">
</form>
<form method="post" action="./$zonecgi">
<input type=hidden value="10" name="sisetu">
<input type=hidden value="5" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="   福引券を送る   " onClick="this.disabled=true; this.value='  お待ちください  '; this.form.submit();">
</form>
<form method="post" action="./$zonecgi">
<input type=hidden value="10" name="sisetu">
<input type=hidden value="4" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="     手紙を送る     " onClick="this.disabled=true; this.value='  お待ちください  '; this.form.submit();">
</form><br></td><td width=30></td><td>
HTM
}
&townmodori;
if ( $in{riyou} eq "" ) {
print <<"HTM";
<center><font size=6 color=#$mojiiro4><b>手紙 一覧</b></font><br>
(保持期間が3日間、あるいは保持件数が30件をこえると自動消去されます)
<table border=0 width=70%><tr><td>
HTM
$tegamicount = 0;
open(BAN,">>$maindir/$foldacha/tegami2_$chaid.tmp");
flock(BAN,2);
	open(BANN,"$maindir/$foldacha/tegami_$chaid$bousi2cha$bousikts");
		while ( $yuubin = <BANN> ) {
			if ( $tegamicount > 29 ) { last; }
($kako,$chanamez,$chamojiz,$tegami,$genzai2) = split(/\t/,$yuubin);
			if ( $now < $kako + (3*24*60*60) ) {
print "<hr><font color=#$chamojiz><b>$chanamez</b></font> ： $tegami <nobr>($genzai2)</nobr>\n";
		print BAN "$yuubin";
			}
$tegamicount ++;
		}
	close(BANN);

flock(BAN,8);
close(BAN);

rename("$maindir/$foldacha/tegami2_$chaid.tmp","$maindir/$foldacha/tegami_$chaid$bousi2cha$bousikts");

print <<"HTM";
</td></tr></table><hr></center>
HTM
}
sub put_comma {
  my $num = $_[0];
  $num = reverse $num;
  $num =~ s/(\d{3})(?=\d)(?!\d*\.)/$1,/g;
  $num = reverse $num;
  return $num
}
&itemtable;

1;