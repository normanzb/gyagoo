&topsisetu;

#VER106 Start エンディング
	if ( $flag2 == 1 ) {
print <<"HTM";
そうか・・・お主、あやつを倒したか。<br>
そう、噂\に流れていた「ヴァグー」は<br>
「バグ」が正しい呼び方じゃ。<br>
長い間、噂\として流れている間に<br>
呼び方が変わってしまったのじゃろう。<br><br>
お主、真実をその目で確かめてみたいか？<br>
もし心の準備が出来ているのならば奥へ進むがよい。<br>
その先はこの世の果てに続いておる。<br><br>
ただし！<br>
何が起こってもとりみだしてはならんぞ。<br>
<form method="post" action="./last.cgi">
<input type=hidden value="0" name="last">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="  奥へ進む  ">
</form>
HTM
        } elsif ( $flag2 == 2 ) {
print <<"HTM";
お主もついにVagooの真意を知ってしまったか・・。<br><br>
これからわしら人間はどうすればよいのかのぅ。<br>
誰にも答えが出ないのじゃよ。<br>
以前、その重みに耐えられず、<br>
自ら命を絶った者もいたほどじゃ。<br><br>
これからどうするか。<br>
それはお主自身で答えを見つけるのじゃ・・・<br>

HTM
$flag2 = 3;
&charadatawrt;
} elsif ( $in{riyou} eq "1" ) {
#if ( $in{riyou} eq "1" ) {
#VER106 End

print <<"HTM";
ふむ。何を聞きたい？<br>
<form method="post" action="./$zonecgi">
<input type=hidden value="7" name="sisetu">
<input type=hidden value="11" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=radio value="1" name="hear" checked>種族<br>
<input type=radio value="2" name="hear">ジョブ<br>
<input type=radio value="3" name="hear">ペット<br>
<input type=radio value="4" name="hear">アイテム<br>
<input type=radio value="5" name="hear">ゾーン<br>
<input type=radio value="6" name="hear">ヴァグー<br>
<input type=radio value="7" name="hear">アルパチー<br>
<input type=radio value="8" name="hear">謎の扉<br><br>
<input type=submit value="    聞く    ">
</form>
HTM
	} elsif ( $in{riyou} eq "11" ) {
		if ( $in{hear} == 1 ) {
print <<"HTM";
この世界には４つの種族が生息している。<br>
　「人間」「精霊」「霊獣」「魔人」<br>
まーこれは人間が勝手にそう呼んでいるだけじゃがな。<br>
その他にも新種族がいるかもしれんのう。<br><br>
この種族という概念はペット合成時に<br>
大きく関係してくるのじゃ。<br>
覚えておくとよいぞ。<br>
HTM
		} elsif ( $in{hear} == 2 ) {
print <<"HTM";
ジョブ、すなわち職業のことじゃ。<br>
ある一定レベルに達すると<br>
$sisetu[6] で転職することができるぞぃ<br><br>
各ジョブにはそれぞれ特徴がある。<br>
特技、ステータスアップ率、連れて歩けるペット数、<br>
装備できる重量などがそれじゃ。<br><br>
転職は1回しかできない。<br>
だからお主のなりたいジョブを慎重に選ぶのじゃ。<br><br>
中級ジョブに転職後、さらにレベルがあがると<br>
上級ジョブに転職できるぞぃ。<br>
HTM
		} elsif ( $in{hear} == 3 ) {
print <<"HTM";
戦闘後にペットを獲得できることがあるのじゃ。<br>
$sisetu[4] から出して連れて歩くと<br>
一緒に戦闘に参加してくれるぞぃ。<br>
連れて歩けるペットの最大数は<br>
ジョブによって異なるので気をつけるように。<br>
なんと集めたペットを $sisetu[5] で<br>
合成することもできるぞぃ。<br><br>
ペットの中には戦闘後にしか獲得できないもの、<br>
合成でしか獲得できないものも存在するのじゃ。<br>
ペット捜しをお主の旅の目標にしてもよいかもな。<br>
HTM
		} elsif ( $in{hear} == 4 ) {
print <<"HTM";
アイテムは大きくわけて次の３つに分かれる。<br>
　　「道具」「武器」「防具」<br>
武器防具に関しては重量という概念が存在する。<br>
お主のジョブによっては装備できない物も<br>
あるかもしれないのう。<br>
まー装備できない物は $sisetu[10] で他の冒険者と<br>
トレードするのも一つの手かもしれん。<br>
さらに、ジョブ専用のアイテムも存在するそうじゃ。<br><br>
アイテム捜しをお主の旅の目標にしてもよいかもな。<br>
HTM
		} elsif ( $in{hear} == 5 ) {
print <<"HTM";
この世界はゾーンと呼ばれるもので区切られておる。<br>
ようするにマップってことじゃ。<br><br>
次のゾーンへ移動するには規程回数の戦闘をこなさないと<br>
移動出来ないシステムになっておる。<br>
とあるアイテムを使えば瞬間移動も可能じゃがな。<br>
HTM
		} elsif ( $in{hear} == 6 ) {
print <<"HTM";
ううぅむ、難しい質問じゃ。<br>
実のところ、わしも言葉の意味はわからないのじゃ。<br><br>
まだ見ぬ財宝か、それとも新種の種族か・・・。<br>
ぜひお主にもそれを解明して欲しいのじゃ。<br>
ひょっとすると我が種族「人間」を<br>
導く道しるべとなるかもしれん。<br>
よろしく頼むぞぃ。<br>
HTM
		} elsif ( $in{hear} == 7 ) {
print <<"HTM";
アルパチーの森で、黒い鎧を身にまとった<br>
人影がうろついておるらしいのじゃ。<br><br>
そやつは冒険者を見つけると無差別に襲い掛かってくるらしいのじゃ。<br>
盗賊かのぅ。物騒な世の中になった物じゃ。<br>
とにかく、$chanameもアルパチーの森に行く時は<br>
十\分、注意しなさい。<br>
HTM
		} elsif ( $in{hear} == 8 ) {
print <<"HTM";
あの扉について知りたいのか。<br>
教えてあげたいのじゃが、実はわしにもわからんのじゃ。<br><br>
あの扉はわしの生まれる前からあっての。<br>
わしの父が、扉について何か知っておるみたいじゃったが・・・。<br>
もう４０年前になるのかのぅ・・・。<br>結局、扉の事を誰にも明かさぬまま、父は逝きよっての。<br>
それ以来、あの部屋は開かずの扉となってしまったのじゃ。<br>
誰が何の為に作り、中に何があるのかも、今となっては誰にもわからないのじゃ。<br>
<br><br>

HTM
		}
print <<"HTM";
<form method="post" action="./$zonecgi">
<input type=hidden value="7" name="sisetu">
<input type=hidden value="1" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="   他の話を聞く  ">
</form>
HTM
	} elsif ( $in{riyou} eq "2" ) {
print <<"HTM";
ほれ、現在登録されている冒険者のリストじゃ。<br>
<form action="./$introcgi" target="bouken" method="post">
<input type=submit value="   ステータス閲覧  ">
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
これこれ、何もせずに報酬など出せるはずがないじゃろう。<br>
働かざる者、食うべからず。じゃよ。
HTM
	} else {

$chagold += $chastats[13];
print <<"HTM";
そうじゃな。お主の今までの働きからいくと・・・<br>
<font color=blue><font size=+2><b>$chastats[13]</font></font><font size=+2>G</font></b> ってとこじゃな。<br>
これからも頑張ってモンスターを退治しておくれ。
</select>
</form>
HTM
$chastats[13] = 0;
&charadatawrt;
&tyourouform;
}
	} elsif ( $in{riyou} eq "3" ) {
print <<"HTM";
たまには気分転換も必要じゃな。<br>
色を選択しておくれ。<br><br>
<form method="post" action="./$zonecgi">
<input type=hidden value="7" name="sisetu">
<input type=hidden value="31" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="   文字色変更  ">
<select name="mojisyoku">
<option value="000000" selected>黒
<option value="dd0000">赤
<option value="0000dd">青
<option value="009900">緑
<option value="ffbb00">黄
<option value="00aaaa">水
<option value="00bb00">黄緑
<option value="ff55ff">桃
<option value="a96800">茶
<option value="af00af">紫
<option value="666666">銀
<option value="888800">金
<option value="ff8500">橙
<option value="7800d3">青紫
</select></form>
HTM
	} elsif ( $in{riyou} eq "31" ) {
$chamoji = $in{mojisyoku};
&charadatawrt;
print <<"HTM";
うむ、変更しておいたぞぃ。<br>
他にはどんな用事かのう？<br><br>
HTM
&tyourouform;
	} elsif ( $in{riyou} eq "4" ) {
print <<"HTM";
では新しいURLを記入しなさい。<br>
<form action="./$zonecgi" method="post">
<input type=text value="http://" size=50 name="url" maxlength=100>
<input type=submit value="   登録変更  ">
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
ふむ。変更しておいたぞぃ。<br>
他にはどんな用事かのう？<br><br>
HTM
&tyourouform;


	} elsif ( $in{riyou} eq "8" ) {
print <<"HTM";
では新しいコメントを記入しなさい。（全角35文字・半角70文字以内）<br>
<form action="./$zonecgi" method="post">
<input type=text value="" size=50 name="comment" maxlength=70>
<input type=submit value="  内容変更  ">
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
ふむ。変更しておいたぞぃ。<br>
他にはどんな用事かのう？<br><br>
HTM
&tyourouform;



	} elsif ( $in{riyou} eq "7" ) {
	if ($flag3 ) {
print <<"HTM";
扉には暗号式の鍵が掛かっている。<br>
正しい４桁の数字を入力すると開くようだ。<br>
<form action="./$zonecgi" method="post">
<input type=text value="" size=4 name="angou" maxlength=4>
<input type=submit value="確認">
<input type=hidden value="7" name="sisetu">
<input type=hidden value="61" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
</form>
HTM

	} else {
print <<"HTM";
扉には暗号式の鍵が掛かっている。<br>
正しい４桁の数字を入力すると開くようだ。<br>
<br>
しかし、$chanameには暗号がわからなかった・・・。
HTM
}
	} elsif ( $in{riyou} eq "61" ) {
	if ( $in{angou} eq "$karistats[10]" ){
print <<"HTM";
正しく入力されました。<br>
HTM
	} else {
print <<"HTM";
何も起こらなかった。<br>
HTM
}


	} elsif ( $in{riyou} eq "5" ) {
print <<"HTM";
<b><font size=+2>【パスワード変更】</font></b><br><br>
新規登録時に自動生成された、<br>
<font color=red>パスキー</font>を入力してください。<br><br>
<b>※パスワードとは異なります。</b><br><br>
<center>
<form action="./$zonecgi" method="post">
<input type=text value="" size=5 name="angou2" maxlength=5>
<input type=submit value="認証">
<input type=hidden value="7" name="sisetu">
<input type=hidden value="51" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<font size=-2><b>(半角数字５字)</b></font>
</form>
</center>
HTM
	} elsif ( $in{riyou} eq "51" ) {
	if ( $in{angou2} eq "$passkey" ){
print <<"HTM";
<font size=+2><b>【認証に成功しました】</font></b><br><br>
次に、<font color=red>新しいパスワード</font>を入力してください。<br>
"変更"ボタンを押すと、パスワードが変更されます。<br><br>

<form action="./$zonecgi" method="post">
<input type=text value="" size=8 name="chapass" maxlength=8>
<input type=submit value="  変更  ">　<font size=-1><b>(半角英数4～8文字)</b></font>
<input type=hidden value="7" name="sisetu">
<input type=hidden value="52" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
</form>
<font color=red>
<b>変更したパスワードは絶対に忘れないようにしてください。</b><br>
次回からは、古いパスワードは使えなくなり、<br>ここで設定したパスワードでのログインとなります。</b></font><br>
HTM

	} else {
print <<"HTM";

<font size=+2><b>【認証に失敗しました】</font></b><br><br>
パスキーが間違っている恐れがあります。<br>
パスキーを確認し、再度試してみてください。<br><br>
HTM
if ( $admailyn == "1" ) {
print <<"HTM";
パスキーを忘れてしまった場合は、<br><body><A href="mailto:$admail"><b>コチラ</b></a></body>
より管理者に問い合わせてください。<br>
</span>
HTM
}
if ( $admailyn == "2" ) {
print <<"HTM";
パスキーを忘れてしまった場合は、<br><body><A href="$urlbbs"><b>掲示板</b></a></body>
より管理者に問い合わせてください。<br>
</span>
HTM
}
if ( $admailyn == "3" ) {
print <<"HTM";
パスキーを忘れてしまった場合は、<br>郵便局より <body><b>$adname</b></body>
宛てに手紙を送信してください。<br>
</span>
HTM
}
}

	} elsif ( $in{riyou} eq "52" ) {
	if(length($in{chapass}) < 4 || length($in{chapass}) > 8 ){
print <<"HTM";
パスワードは、必ず<b><font color=red>半角英数4～8文字</font></b>の間で指定してください。<br>
<br>
HTM

	} else {
$chapass = $in{chapass};
&charadatawrt;
print <<"HTM";
<font size=+2><b>【変更完了】</font></b><br><br>
パスワードは正常に変更されました。<br>
新しいパスワードは、「<font color=red><b>$chapass</b></font>」です。<br>
次回からは、このパスワードでログインしてください。<br>
<br>
HTM

}



	} else {
print <<"HTM";
よくきてくれた。<br>
どんな用事かのう？<br><br>
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
<input type=submit value="     話を聞く     ">
</form>
<form method="post" action="./$zonecgi">
<input type=hidden value="7" name="sisetu">
<input type=hidden value="6" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="   報酬をもらう   ">
</form>
<form method="post" action="./$zonecgi">
<input type=hidden value="7" name="sisetu">
<input type=hidden value="2" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="    登録者一覧    ">
</form>
<form method="post" action="./$zonecgi">
<input type=hidden value="7" name="sisetu">
<input type=hidden value="3" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="    文字色変更    ">
</form>
<form method="post" action="./$zonecgi">
<input type=hidden value="7" name="sisetu">
<input type=hidden value="4" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="    登録HP変更    ">
</form>
<form method="post" action="./$zonecgi">
<input type=hidden value="7" name="sisetu">
<input type=hidden value="5" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="   パスワード変更   ">
</form>
<form method="post" action="./$zonecgi">
<input type=hidden value="7" name="sisetu">
<input type=hidden value="8" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="   コメント変更   ">
</form>
<br>
<form method="post" action="./$zonecgi">
<input type=hidden value="7" name="sisetu">
<input type=hidden value="7" name="riyou">
<input type=hidden value="$chaid" name="usrid">
<input type=hidden value="$chapass" name="usrpass">
<input type=submit value="     謎の扉     ">
</form>
HTM

}
&townmodori;

1;