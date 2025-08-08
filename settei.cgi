###############
#
# 「Vagoo(ver1.03)」　2001年10月26日配布開始
#　　　スクリプト製作者　スカイ（game@sky-wing.com）
#
#　ダウンロード規定を同意した方のみ、「Vagoo」スクリプト類の使用を許可します。
#
#　配布元HP「うぇぶなげぇむ」http://www.sky-wing.com/~game/
#
###########


# ゲームの全体的な設定項目です

#　管理用パスワードの設定（必ず変更してください）
$adminp = '123456';

#　キャラデータ保持期限設定
#　設定した日数間アクセスのないデータを削除します。
$datadelete = "20"; #　日数を記入してください

#　ゲームタイトル名
$title = "Gyagoo";

#　掲示板までのフルアドレス
$urlbbs = "掲示板のアドレス";

#　チャットを別窓表示するか
#　するなら1、しないなら0
$chatwin = "1";

$bad_host = '1';

$mente = '0';
#　背景画像ＵＲＬ（背景に画像は使用しないことをオススメします）
$bgurl = "";

#　背景色（背景に画像を使用しない場合）
#　背景色を変更する場合はキャラ画像の体部分であるbody.gifの背景色も
#　同時に変更する必要があります
$bgclr = "C8C8C8";

$mojiiro = "000000"; #　全体的な文字色
$mojiiro2 = "ff0000"; #　強調色
$mojiiro3 = "ff00ff"; #　強調色２
$mojiiro4 = "0000ff"; #　強調色３
$linkiro = "0000ff"; #　リンクする文字色
$vlinkiro = "0000ff"; #　リンク済の文字色
$wakuiro = "000000"; #　テーブル枠の色
$tableiro = "BDB76B"; #　バトルシーンのターン数表示欄背景色

#　CGIや拡張子名
#　覗き見防止のためにも変更しておいたほうがよいと思われます。
#　変更した場合は既存のフォルダ名も同じフォルダ名に変更してください。

#　画像フォルダ名
$imgfile = "pics"; 

#　モンスターデータフォルダ名
$monsfile = "mons"; 

#　キャラクターデータ保存フォルダ名
$foldacha = "players";

#　図鑑データ保存フォルダへ名
$foldazukan = "zukan";

#　戦闘データフォルダへのパス
$foldabattle = "./btl";

#　リサイクルボックスデータフォルダへのパス
$foldamarket = "market";

#　戦闘データフォルダへのパス
$foldarank = "rank";

#　戦闘データフォルダへのパス
$foldacold = "cold";

#　各キャラステータスデータ盗み見防止用文字（必ず変更してください）
#　２～４文字程度でよいと思います
$bousicha = "1111";
#　各キャラス画像データ盗み見防止用文字（必ず変更してください）
#　２～４文字程度でよいと思います
$bousi2cha = "2222";
#　各キャラス画像データ盗み見防止用文字（必ず変更してください）
#　２～４文字程度でよいと思います
$bousi3cha = "mark";

#　データ盗み見防止用ファイル拡張子（なるべく変更してください）
#　変更することをオススメします。
#　変更をした場合は既存のファイル名の拡張子をすべて同名に変更してください。
$bousikts =".log";
$bousikts2 =".dat";

#　各CGI名
$sinki = "sinki.cgi"; #　キャラ作成時に使用するCGI
$charapic = "charapic.cgi"; #　キャラ画像を表示させるCGI
$zonecgi = "zone.cgi"; #　ゾーン処理をするCGI
$towncgi = "town.cgi"; #　旅立ちの街の基本処理をするCGI
$shopcgi = "shop.cgi"; #　街のショップの処理をするCGI
$shop2cgi = "shop2.cgi"; #　街のショップの処理をするCGI
$bankcgi = "bank.cgi"; #　街の銀行の処理をするCGI
$battlecgi = "battle.cgi"; #　戦闘処理をするCGI
$rankcgi = "rank.cgi"; #　戦闘処理をするCGI
$fieldcgi = "field.cgi"; #フィールド処理をするCGI
$koyacgi = "koya.cgi"; #　街のペット小屋の処理をするCGI
$kenkyucgi = "kenkyu.cgi"; #　街の研究所の処理をするCGI
$introcgi = "intro.cgi"; #　冒険中プレーヤーのステータス表示用CGI
$tyouroucgi = "tyourou.cgi"; #　街の長老の家の処理をするCGI
$yuubincgi = "yuubin.cgi"; #　街の郵便局の処理をするCGI
$jiincgi = "jiin.cgi"; #　街の寺院の処理をするCGI
$admincgi = "master.cgi"; #　管理モードの処理をするCGI
$bosscgi = "boss.cgi"; #　ボス戦の処理をするCGI
$kunrencgi = "kunren.cgi"; #　ボス戦の処理をするCGI
$town4cgi = "town4.cgi"; #　旅立ちの街の基本処理をするCGI
$sitiyacgi = "sitiya.cgi"; #　旅立ちの街の基本処理をするCGI
$boss4cgi = "boss4.cgi"; #　ボス戦の処理をするCGI
$seikeicgi = "seikei.cgi"; #　整形の基本処理をするCGI
$hukubikicgi = "hukubiki.cgi"; #　ボス戦の処理をするCGI
$coldcgi = "cold.cgi"; #　ボス戦の処理をするCGI


#　ジョブ名
$job[0] = "旅人"; #　初期ジョブ
$job[1] = "戦士";     #　中級ジョブ↓
$job[2] = "モンク";
$job[3] = "騎士";
$job[4] = "魔法剣士";
$job[5] = "魔術師";
$job[6] = "僧侶";
$job[7] = "吟遊詩人"; #　中級ジョブ↑
$job[11] = "侍";      #　上級ジョブ↓
$job[12] = "狂戦士";
$job[21] = "レンジャー";
$job[22] = "忍者";
$job[31] = "聖騎士";
$job[32] = "暗黒騎士";
$job[41] = "竜騎士";
$job[42] = "ロード";
$job[51] = "魔導師";
$job[52] = "幻獣師";
$job[61] = "司祭";
$job[62] = "呪術師";
$job[71] = "魔獣師";
$job[72] = "ダンサー"; #  上級ジョブ↑

$job[8] = "拳王"; #  上級ジョブ↑
$job[9] = "賢者"; #  上級ジョブ↑
$job[10] = "時空師"; #  上級ジョブ↑
$job[79] = "鬼武者"; #  上級ジョブ↑
$job[80] = "スター"; #  上級ジョブ↑
$job[81] = "猛獣使い"; #  上級ジョブ↑
$job[82] = "竜戦士"; #  上級ジョブ↑
$job[83] = "パラディン"; #  上級ジョブ↑
$job[84] = "闇の詩人"; #  上級ジョブ↑
$job[85] = "デスナイト"; #  上級ジョブ↑
$job[86] = "盗賊"; #  上級ジョブ↑

$job[87] = "勇者"; #  上級ジョブ↑
$job[88] = "覇者"; #  上級ジョブ↑
$job[89] = "界王神"; #  上級ジョブ↑
$job[90] = "？？？"; #  上級ジョブ↑
$job[91] = "？？？"; #  上級ジョブ↑
$job[92] = "？？？"; #  上級ジョブ↑
$job[93] = "？？？"; #  上級ジョブ↑
$job[94] = "？？？"; #  上級ジョブ↑
$job[95] = "？？？"; #  上級ジョブ↑


##################　ゲーム設定　##################
###　フィールド設定
$nexttime = "0"; #　次の行動までの時間（サーバー負担を考慮して変更）
$kiteisentou = "5"; #　ゾーン移動可能になる戦闘回数


###　ステータスの最大値設定
#　フィールド画面で適用
$maxmhp = "9999999"; #　最大HP
$maxdmg = "9999999"; #　DMGの最大値
$maxstr = "9999999"; #　STRの最大値
$maxdef = "9999999"; #　AC の最大値
$maxagi = "9999999"; #　AGIの最大値
$maxint = "9999999"; #　INTの最大値


###　戦闘の設定
#　経験値と金銭獲得の倍率。
#　通常は "1"。"2" にすると2倍、"3" にすると3倍
#　小数点も使用可能（"1.5" にすると1.5倍、"1.8" にすると1.8倍）
$expmode = "1"; #　取得経験値の倍率
$goldmode = "1"; #　取得金銭の倍率

$maxturn = "100"; # 戦闘の最大ターン数


###　教会設定
#　転生に必要なレベルとゴールドの設定
$tenseilv = "100"; #　転生が可能になるレベル
$tenseigold = "800000"; #　転生時に必要なゴールド


###　長老の家の設定
#　長老の家にてパスキーの入力に失敗した際どうするか
#　0 = 何も表示しない
#　1 = 管理者のメールアドレスを表示
#　2 = 掲示板のアドレスを表示
#　3 = 管理者のキャラ名を表示
$admailyn = "1"; #　表示方法

$admail = 'xxxx@xx.xx'; #　表示するメールアドレスを入力
$adname = '名前'; #　管理者のキャラ名を入力


##################################################

#　セキュリティ関連
#　外部アクセス拒否&多重窓プレー拒否セキュリティ設定
#　
#　設置するフォルダまでのアドレスを記入してください
#　例（　http://www.****.co.jp/~***/gyagoo/　以下に置く場合は
#　　$cgidomain = "www.****.co.jp"
#　　$cgidomain = "/~***/gyagoo/"　　）
$cgidomain = "aaa.ne.jp"; #　ドメイン入力（最後に/はつけないでください）
$cgidomain2 = "/gyagoo/"; #　パス入力

#　IPブロック用
@block = ('000.000.000.000','111.111.111.111','222.222.222.222','333.333.333.333','444.444.444.444','555.555.555.555'); #　ブロックしたいIPを入力

#########　設定はここまで　##########



$now = time; #　現在時刻取得
$urlbase = "http://$cgidomain$cgidomain2"; # CGI設置URL結合
$maindir = ".";
#　キャラクター画像アップ処理
sub charaga {
print <<HTM;
<iframe name="charaga" src="./$charapic?atama=$chahead&hada=$chaskin&eye=$chaeye&hana=$chanose&kuti=$chamouth&kami=$chahair&leg=$chabougue[5]&arm=$chabougue[6]&hlm=$chabougue[3]&che=$chabougue[4]&wp=$chabougue[1]&sld=$chabougue[2]" frameborder=0 scrolling=no width=100 height=125></iframe>
HTM
}


#　キャラデータ保存処理
sub charadatawrt {
open(DAT,">$maindir/$foldacha/$bousicha$chaid$bousikts");
flock(DAT,2);
print DAT "$chaid,$chapass,$chaname,$chaurl,$chamoji,$ENV{'REMOTE_ADDR'},$now,$chaplace,$chacount,$chasex,$chaage,$chaclass,$chaexp,$chanextlvl,$chagold,$chalvl,$chastats[9],$chahp,$chastats[0],$chastats[1],$chastats[2],$chastats[3],$chastats[4],$chastats[5],$chastats[6],$chastats[7],$chastats[8],$chastats[10],$chastats[11],$chastats[12],$chastats[13],$chastats[14],$chastats[15],$chastats[16],$karistats[0],$karistats[1],$karistats[2],$karistats[3],$karistats[4],$karistats[5],$karistats[6],$karistats[7],$karistats[8],$karistats[9],$karistats[10],$hukubiki,$strexp,$acexp,$agiexp,$intexp,$nowstrexp,$nowacexp,$nowagiexp,$nowintexp,$champ,$petcode[0],$petname[0],$petritu[0],$peteff[0],$petpic[0],$petkouka[0],$petkouka2[0],$petlv[0],$petexp[0],$petnowexp[0],$petcode[1],$petname[1],$petritu[1],$peteff[1],$petpic[1],$petkouka[1],$petkouka2[1],$petlv[1],$petexp[1],$petnowexp[1],$petcode[2],$petname[2],$petritu[2],$peteff[2],$petpic[2],$petkouka[2],$petkouka2[2],$petlv[2],$petexp[2],$petnowexp[2],$chaitem[1],$chaeff[1],$chasetumei[1],$chaitem[2],$chaeff[2],$chasetumei[2],$chaitem[3],$chaeff[3],$chasetumei[3],$chaitem[4],$chaeff[4],$chasetumei[4],$chaitem[5],$chaeff[5],$chasetumei[5],$chaitem[6],$chaeff[6],$chasetumei[6],$chaitem[7],$chaeff[7],$chasetumei[7],$chaitem[8],$chaeff[8],$chasetumei[8],$chasoubi[1],$chabun[1],$chabougue[1],$chasoubi[2],$chabun[2],$chabougue[2],$chasoubi[3],$chabun[3],$chabougue[3],$chasoubi[4],$chabun[4],$chabougue[4],$chasoubi[5],$chabun[5],$chabougue[5],$chasoubi[6],$chabun[6],$chabougue[6],$chasoubi[7],$chabun[7],$chasoubi[8],$chabun[8],$chaskin,$chahead,$chaeye,$chanose,$chamouth,$chahair,$flag1,$flag2,$flag3,$flag4,$flag5,$flag6,$flag7,$flag8,$flag9,$flag10,$flag11,$flag12,$flag13,$flag14,$flag15,$flag16,$flag17,$flag18,$flag19,$flag20,$flag21,$flag22,$flag23,$flag24,$flag25,$flag26,$flag27,$flag28,$flag29,$flag30,$morai,$balance,$kougeki,$mamori,$houou,$ribaibu,$kougekit,$mamorit,$jobexp[0],$jobexp[1],$jobexp[2],$jobexp[3],$jobexp[4],$jobexp[5],$jobexp[6],$jobexp[7],$jobexp[8],$jobexp[9],$jobexp[10],$jobexp[11],$jobexp[12],$jobexp[21],$jobexp[22],$jobexp[31],$jobexp[32],$jobexp[41],$jobexp[42],$jobexp[51],$jobexp[52],$jobexp[61],$jobexp[62],$jobexp[71],$jobexp[72],$jobexp[79],$jobexp[80],$jobexp[81],$jobexp[82],$jobexp[83],$jobexp[84],$jobexp[85],$jobexp[86],$jobexp[87],$jobexp[88],$jobexp[89],$jobexp[90],$jobexp[91],$jobexpnow[0],$jobexpnow[1],$jobexpnow[2],$jobexpnow[3],$jobexpnow[4],$jobexpnow[5],$jobexpnow[6],$jobexpnow[7],$jobexpnow[8],$jobexpnow[9],$jobexpnow[10],$jobexpnow[11],$jobexpnow[12],$jobexpnow[21],$jobexpnow[22],$jobexpnow[31],$jobexpnow[32],$jobexpnow[41],$jobexpnow[42],$jobexpnow[51],$jobexpnow[52],$jobexpnow[61],$jobexpnow[62],$jobexpnow[71],$jobexpnow[72],$jobexpnow[79],$jobexpnow[80],$jobexpnow[81],$jobexpnow[82],$jobexpnow[83],$jobexpnow[84],$jobexpnow[85],$jobexpnow[86],$jobexpnow[87],$jobexpnow[88],$jobexpnow[89],$jobexpnow[90],$jobexpnow[91],$master[0],$master[1],$master[2],$master[3],$master[4],$master[5],$master[6],$master[7],$master[8],$master[9],$master[10],$master[11],$master[12],$master[21],$master[22],$master[31],$master[32],$master[41],$master[42],$master[51],$master[52],$master[61],$master[62],$master[71],$master[72],$master[79],$master[80],$master[81],$master[82],$master[83],$master[84],$master[85],$master[86],$master[87],$master[88],$master[89],$master[90],$master[91],$masterjob,$lvlpoint,$passkey,$tp,$maxcombo,$maxdmg,$autop,$potion,$bpo,$newtegami,$tensei";
flock(DAT,8);
close(DAT);

}

#　キャラデータ読み込み処理
sub charadataload {
  if($in{usrid} ne "" ){
    open(CDAT,"$maindir/$foldacha/$bousicha$in{usrid}$bousikts");
      @charadataa = split(/,/,<CDAT>);
				($chaid,$chapass,$chaname,$chaurl,$chamoji,$chaip,$chajikan,$chaplace,$chacount,$chasex,$chaage,$chaclass,$chaexp,$chanextlvl,$chagold,$chalvl,$chastats[9],$chahp,$chastats[0],$chastats[1],$chastats[2],$chastats[3],$chastats[4],$chastats[5],$chastats[6],$chastats[7],$chastats[8],$chastats[10],$chastats[11],$chastats[12],$chastats[13],$chastats[14],$chastats[15],$chastats[16],$karistats[0],$karistats[1],$karistats[2],$karistats[3],$karistats[4],$karistats[5],$karistats[6],$karistats[7],$karistats[8],$karistats[9],$karistats[10],$hukubiki,$strexp,$acexp,$agiexp,$intexp,$nowstrexp,$nowacexp,$nowagiexp,$nowintexp,$champ,$petcode[0],$petname[0],$petritu[0],$peteff[0],$petpic[0],$petkouka[0],$petkouka2[0],$petlv[0],$petexp[0],$petnowexp[0],$petcode[1],$petname[1],$petritu[1],$peteff[1],$petpic[1],$petkouka[1],$petkouka2[1],$petlv[1],$petexp[1],$petnowexp[1],$petcode[2],$petname[2],$petritu[2],$peteff[2],$petpic[2],$petkouka[2],$petkouka2[2],$petlv[2],$petexp[2],$petnowexp[2],$chaitem[1],$chaeff[1],$chasetumei[1],$chaitem[2],$chaeff[2],$chasetumei[2],$chaitem[3],$chaeff[3],$chasetumei[3],$chaitem[4],$chaeff[4],$chasetumei[4],$chaitem[5],$chaeff[5],$chasetumei[5],$chaitem[6],$chaeff[6],$chasetumei[6],$chaitem[7],$chaeff[7],$chasetumei[7],$chaitem[8],$chaeff[8],$chasetumei[8],$chasoubi[1],$chabun[1],$chabougue[1],$chasoubi[2],$chabun[2],$chabougue[2],$chasoubi[3],$chabun[3],$chabougue[3],$chasoubi[4],$chabun[4],$chabougue[4],$chasoubi[5],$chabun[5],$chabougue[5],$chasoubi[6],$chabun[6],$chabougue[6],$chasoubi[7],$chabun[7],$chasoubi[8],$chabun[8],$chaskin,$chahead,$chaeye,$chanose,$chamouth,$chahair,$flag1,$flag2,$flag3,$flag4,$flag5,$flag6,$flag7,$flag8,$flag9,$flag10,$flag11,$flag12,$flag13,$flag14,$flag15,$flag16,$flag17,$flag18,$flag19,$flag20,$flag21,$flag22,$flag23,$flag24,$flag25,$flag26,$flag27,$flag28,$flag29,$flag30,$morai,$balance,$kougeki,$mamori,$houou,$ribaibu,$kougekit,$mamorit,$jobexp[0],$jobexp[1],$jobexp[2],$jobexp[3],$jobexp[4],$jobexp[5],$jobexp[6],$jobexp[7],$jobexp[8],$jobexp[9],$jobexp[10],$jobexp[11],$jobexp[12],$jobexp[21],$jobexp[22],$jobexp[31],$jobexp[32],$jobexp[41],$jobexp[42],$jobexp[51],$jobexp[52],$jobexp[61],$jobexp[62],$jobexp[71],$jobexp[72],$jobexp[79],$jobexp[80],$jobexp[81],$jobexp[82],$jobexp[83],$jobexp[84],$jobexp[85],$jobexp[86],$jobexp[87],$jobexp[88],$jobexp[89],$jobexp[90],$jobexp[91],$jobexpnow[0],$jobexpnow[1],$jobexpnow[2],$jobexpnow[3],$jobexpnow[4],$jobexpnow[5],$jobexpnow[6],$jobexpnow[7],$jobexpnow[8],$jobexpnow[9],$jobexpnow[10],$jobexpnow[11],$jobexpnow[12],$jobexpnow[21],$jobexpnow[22],$jobexpnow[31],$jobexpnow[32],$jobexpnow[41],$jobexpnow[42],$jobexpnow[51],$jobexpnow[52],$jobexpnow[61],$jobexpnow[62],$jobexpnow[71],$jobexpnow[72],$jobexpnow[79],$jobexpnow[80],$jobexpnow[81],$jobexpnow[82],$jobexpnow[83],$jobexpnow[84],$jobexpnow[85],$jobexpnow[86],$jobexpnow[87],$jobexpnow[88],$jobexpnow[89],$jobexpnow[90],$jobexpnow[91],$master[0],$master[1],$master[2],$master[3],$master[4],$master[5],$master[6],$master[7],$master[8],$master[9],$master[10],$master[11],$master[12],$master[21],$master[22],$master[31],$master[32],$master[41],$master[42],$master[51],$master[52],$master[61],$master[62],$master[71],$master[72],$master[79],$master[80],$master[81],$master[82],$master[83],$master[84],$master[85],$master[86],$master[87],$master[88],$master[89],$master[90],$master[91],$masterjob,$lvlpoint,$passkey,$tp,$maxcombo,$maxdmg,$autop,$potion,$bpo,$newtegami,$tensei) = @charadataa;
    close(CDAT);
  } else {
    &fuseisyori;
  }
}

#　キャラステータス表示処理
sub pettukitable {
while($chagold =~ s/(.*\d)(\d\d\d)/$1,$2/){} ;
if($chaurl ne "") {
$homeurl = "<a href=\"$chaurl\" target=\"_blank\"><font color=#$chamoji><b>HOME PAGE</b></font></a>";
}
if($petcode[0] ne ""){$pet1 = "<img src=\"$maindir/$imgfile/$petpic[0].gif\" alt=\"$petcode[0]（Lv.$petlv[0]）\">";}
if($petcode[1] ne ""){$pet2 = "<img src=\"$maindir/$imgfile/$petpic[1].gif\" alt=\"$petcode[1]（Lv.$petlv[1]）\">";}
if($petcode[2] ne ""){$pet3 = "<img src=\"$maindir/$imgfile/$petpic[2].gif\" alt=\"$petcode[2]（Lv.$petlv[2]）\">";}
print <<HTM;
<table bordercolor=#$wakuiro border=1><tr>
<td rowspan=12>
<table border=0 cellspacing=0><tr>
<td valign="baseline">$pet2</td><td>
HTM
&charaga;
$exp1haba = int($chaexp / $chanextlvl * 100) - 1;

if ( $exp1haba < 0 ) { $exp1haba = 0; }
if ( $exp1haba > 95 ) { $exp1haba = 95; }
$exp2haba = 95 - $exp1haba;

$hpbarcha1 = int( ( $chahp / $chastats[9] ) * 230 );
if ( $hpbarcha1 != 230 ) {
$hpbarcha2 = 230 - $hpbarcha1;
$hpbardmg2 = "<img src=\"$maindir/$imgfile/hpbar2.gif\" width=$hpbarcha2 height=\"8\">";
}

$mpbarcha1 = int( ( $champ / $chastats[16] ) * 230 );
if ( $mpbarcha1 != 230 ) {
$mpbarcha2 = 230 - $mpbarcha1;
$mpbardmg2 = "<img src=\"$maindir/$imgfile/hpbar2.gif\" width=$mpbarcha2 height=\"8\">";
}

$strbarcha1 = int( ( $nowstrexp / $strexp ) * 230 );
$strritu = int($strbarcha1 / 2.3); 
if ( $strbarcha1 != 230 ) {
$strbarcha2 = 230 - $strbarcha1;
$strbardmg2 = "<img src=\"$maindir/$imgfile/hpbar2.gif\" width=$strbarcha2 height=\"8\" alt=$strritu％>";
}
$acbarcha1 = int( ( $nowacexp / $acexp ) * 230 );
$acritu = int($acbarcha1 / 2.3); 
if ( $acbarcha1 != 230 ) {
$acbarcha2 = 230 - $acbarcha1;
$acbardmg2 = "<img src=\"$maindir/$imgfile/hpbar2.gif\" width=$acbarcha2 height=\"8\" alt=$acritu％>";
}
$agibarcha1 = int( ( $nowagiexp / $agiexp ) * 230 );
$agiritu = int($agibarcha1 / 2.3); 
if ( $agibarcha1 != 230 ) {
$agibarcha2 = 230 - $agibarcha1;
$agibardmg2 = "<img src=\"$maindir/$imgfile/hpbar2.gif\" width=$agibarcha2 height=\"8\" alt=$agiritu％>";
}
$intbarcha1 = int( ( $nowintexp / $intexp ) * 230 );
$intritu = int($intbarcha1 / 2.3); 
if ( $intbarcha1 != 230 ) {
$intbarcha2 = 230 - $intbarcha1;
$intbardmg2 = "<img src=\"$maindir/$imgfile/hpbar2.gif\" width=$intbarcha2 height=\"8\" alt=$intritu％>";
}

$petbarcha1 = int( ( $petnowexp[0] / $petexp[0] ) * 180 );
if ( $petbarcha1 != 180 ) {
$petbarcha2 = 180 - $petbarcha1;
$petbardmg2 = "<img src=\"$maindir/$imgfile/hpbar2.gif\" width=$petbarcha2 height=\"8\">";
}
$petbarcha11 = int( ( $petnowexp[1] / $petexp[1] ) * 180 );
if ( $petbarcha11 != 180 ) {
$petbarcha22 = 180 - $petbarcha11;
$petbardmg22 = "<img src=\"$maindir/$imgfile/hpbar2.gif\" width=$petbarcha22 height=\"8\">";
}
$petbarcha111 = int( ( $petnowexp[2] / $petexp[2] ) * 180 );
if ( $petbarcha111 != 180 ) {
$petbarcha222 = 180 - $petbarcha111;
$petbardmg222 = "<img src=\"$maindir/$imgfile/hpbar2.gif\" width=$petbarcha222 height=\"8\">";
}


		if ( $champ < 0) {
$champ = 0;
$mpbarcha1 = int( ( $champ / $chastats[16] ) * 0 );
if ( $mpbarcha1 != 230 ) {
$mpbarcha2 = 230 - $mpbarcha1;
$mpbardmg2 = "<img src=\"$maindir/$imgfile/hpbar2.gif\" width=$mpbarcha2 height=\"8\">";
}
}
$heikin = $chastats[0] + $chastats[1] + $chastats[2] + $chastats[3] + $chastats[4] + $chastats[5] + $chastats[6] + $chastats[7] + $chastats[8];
$heikin2 = int($heikin / 9);

if ($petkouka[0] == 16){$petkouka[0] = "物理攻撃";}
if ($petkouka[0] == 1){$petkouka[0] = "火属性攻撃";}
if ($petkouka[0] == 2){$petkouka[0] = "水属性攻撃";}
if ($petkouka[0] == 3){$petkouka[0] = "魔属性攻撃";}
if ($petkouka[0] == 4){$petkouka[0] = "無属性攻撃";}
if ($petkouka[0] == 5){$petkouka[0] = "？属性攻撃";}
if ($petkouka[0] == 6){$petkouka[0] = "お金を奪う";}
if ($petkouka[0] == 8){$petkouka[0] = "HP回復";}
if ($petkouka[0] == 9){$petkouka[0] = "ACアップ";}
if ($petkouka[0] == 10){$petkouka[0] = "STRアップ";}
if ($petkouka[0] == 11){$petkouka[0] = "AGIアップ";}
if ($petkouka[0] == 12){$petkouka[0] = "INTアップ";}
if ($petkouka[0] == 13){$petkouka[0] = "CHAアップ";}
if ($petkouka[0] == 14){$petkouka[0] = "ALL耐性アップ";}
if ($petkouka[0] == 15){$petkouka[0] = "特殊行動";}
if ($petkouka[1] == 16){$petkouka[1] = "物理攻撃";}
if ($petkouka[1] == 1){$petkouka[1] = "火属性攻撃";}
if ($petkouka[1] == 2){$petkouka[1] = "水属性攻撃";}
if ($petkouka[1] == 3){$petkouka[1] = "魔属性攻撃";}
if ($petkouka[1] == 4){$petkouka[1] = "無属性攻撃";}
if ($petkouka[1] == 5){$petkouka[1] = "？属性攻撃";}
if ($petkouka[1] == 6){$petkouka[1] = "お金を奪う";}
if ($petkouka[1] == 8){$petkouka[1] = "HP回復";}
if ($petkouka[1] == 9){$petkouka[1] = "ACアップ";}
if ($petkouka[1] == 10){$petkouka[1] = "STRアップ";}
if ($petkouka[1] == 11){$petkouka[1] = "AGIアップ";}
if ($petkouka[1] == 12){$petkouka[1] = "INTアップ";}
if ($petkouka[1] == 13){$petkouka[1] = "CHAアップ";}
if ($petkouka[1] == 14){$petkouka[1] = "ALL耐性アップ";}
if ($petkouka[1] == 15){$petkouka[1] = "特殊行動";}
if ($petkouka[2] == 16){$petkouka[2] = "物理攻撃";}
if ($petkouka[2] == 1){$petkouka[2] = "火属性攻撃";}
if ($petkouka[2] == 2){$petkouka[2] = "水属性攻撃";}
if ($petkouka[2] == 3){$petkouka[2] = "魔属性攻撃";}
if ($petkouka[2] == 4){$petkouka[2] = "無属性攻撃";}
if ($petkouka[2] == 5){$petkouka[2] = "？属性攻撃";}
if ($petkouka[2] == 6){$petkouka[2] = "お金を奪う";}
if ($petkouka[2] == 8){$petkouka[2] = "HP回復";}
if ($petkouka[2] == 9){$petkouka[2] = "ACアップ";}
if ($petkouka[2] == 10){$petkouka[2] = "STRアップ";}
if ($petkouka[2] == 11){$petkouka[2] = "AGIアップ";}
if ($petkouka[2] == 12){$petkouka[2] = "INTアップ";}
if ($petkouka[2] == 13){$petkouka[2] = "CHAアップ";}
if ($petkouka[2] == 14){$petkouka[2] = "ALL耐性アップ";}
if ($petkouka[2] == 15){$petkouka[2] = "特殊行動";}

if ($jobexpnow[$chaclass] == $jobexp[$chaclass]){ $job[$chaclass] ="<font color=red>☆ </font>$job[$chaclass]<font color=red> ☆</font>"; }
print <<HTM;

</td><td valign="baseline">$pet1</td><td valign="baseline">$pet3</td></tr></table></td>
<td colspan="4" width=250 align=center><font color=#$chamoji><b>   $chaname ($job[$chaclass])</font></font></b></font></center></td></tr>
<tr><td width=30 align=center><b>Lv</b></td><td width=95 align=right><font color=#$chamoji><b>$chalvl</b></font></td><td width=30 align=center><b>SEX</b></td><td width=95 align=right><font color=#$chamoji><b>$chasex</b></font></td></tr>
<tr><td width=30 align=center><b>HP</b></td><td colspan="3"><font color=#$chamoji><b><nobr><img src="$maindir/$imgfile/exp.gif" height="10"><img src="$maindir/$imgfile/hpbar1.gif" width=$hpbarcha1 height="8">$hpbardmg2<img src="$maindir/$imgfile/exp.gif" height="8"><font size=-1><center><b>$chahp / $chastats[9]</center></font></b></nobr></font></td></tr>
<tr><td width=30 align=center><b>TP</b></td><td colspan="3"><font color=#$chamoji><b><nobr><img src="$maindir/$imgfile/exp.gif" height="10"><img src="$maindir/$imgfile/tpbar1.gif" width=$mpbarcha1 height="8">$mpbardmg2<img src="$maindir/$imgfile/exp.gif" height="8"><font size=-1><center><b>$champ / $chastats[16]</center></font></b></nobr></font></td></tr>

<tr><td width=30 align=center><b>CP</b></td><td width=95 align=right><font color=#$chamoji><b><nobr>$chastats[14]</nobr></font><font size=-1>P</font></b></td><td width=30 align=center><b>Gold</b></td><td width=95 align=right><font color=#$chamoji><b>$chagold</font><font size=-1>G</font></b></td></tr>
<tr><td width=30 align=center><b>DMG</b></td><td width=95 align=right><font color=#$chamoji><b>$chastats[0]</b></font> + <font color=green><b>$karistats[0]</b></font></td><td width=30 align=center><b>AGE</b></td><td width=95 align=right><font color=#$chamoji><b>$chaage</b></font></td></tr>
<tr><td width=30 align=center><b>STR</b></td><td colspan="4" align=center><font color=#$chamoji><nobr><img src="$maindir/$imgfile/exp.gif" height="8"><img src="$maindir/$imgfile/mpbar1.gif" width=$strbarcha1 height="8" alt="$strritu％">$strbardmg2<img src="$maindir/$imgfile/exp.gif" height="8"><br><font size=-1><b>$chastats[2]</b></font>  + <b><nobr><font color=green><font size=-1>$karistats[2]</font></td></tr>
<tr><td width=30 align=center><b>AC</b></td><td colspan="4" align=center><font color=#$chamoji><nobr><img src="$maindir/$imgfile/exp.gif" height="8"><img src="$maindir/$imgfile/mpbar1.gif" width=$acbarcha1 height="8" alt="$acritu％">$acbardmg2<img src="$maindir/$imgfile/exp.gif" height="8"><br><font size=-1><b>$chastats[1]</b></font>  + <b><nobr><font color=green><font size=-1>$karistats[1]</font></td></tr>
<tr><td width=30 align=center><b>AGI</b></td><td colspan="4" align=center><font color=#$chamoji><nobr><img src="$maindir/$imgfile/exp.gif" height="8"><img src="$maindir/$imgfile/mpbar1.gif" width=$agibarcha1 height="8" alt="$agiritu％">$agibardmg2<img src="$maindir/$imgfile/exp.gif" height="8"><br><font size=-1><b>$chastats[3]</b></font>  + <b><nobr><font color=green><font size=-1>$karistats[3]</font></td></tr>
<tr><td width=30 align=center><b>INT</b></td><td colspan="4" align=center><font color=#$chamoji><nobr><img src="$maindir/$imgfile/exp.gif" height="8"><img src="$maindir/$imgfile/mpbar1.gif" width=$intbarcha1 height="8" alt="$intritu％">$intbardmg2<img src="$maindir/$imgfile/exp.gif" height="8"><br><font size=-1><b>$chastats[4]</b></font>  + <b><nobr><font color=green><font size=-1>$karistats[4]</font></td></tr>

<tr><td width=30 align=center><b>EXP</b></td><td colspan="3"><img src="$maindir/$imgfile/exp.gif"><img src="$maindir/$imgfile/expbar1.gif" width=$exp1haba\% height=16 alt="$exp1haba％"><img src="$maindir/$imgfile/expbar2.gif" width=$exp2haba\% height=16 alt="$exp1haba％"><img src="$maindir/$imgfile/exp2.gif" alt="$exp1haba"><center><font size=-1><b>$chaexp</b> / <b>$chanextlvl</b></font>
<br><font size=-2><font color=gray><b>Total：</b>$chastats[15]</font></font></center></td></tr>
</table><center>
<br><center>
<table border=1 bordercolor=#$wakuiro>
<font color=darkbrown><b>$maxcombo</b></font>
</table></center>
-$homeurl-
<br><br>
<center>
<tr><td>
<table border=1 bordercolor=#$wakuiro width=600><tr>
<td align=center colspan=2><b>PET NAME</b></td><td><center><b>LV</td><td><center><b>PP</td><td><center><b>TYPE</td><td><center><b>EF</td><td><center><b>EXP</td></tr>
<tr><td width=25 align=center><b>1</b></td><td width=180><font color=#$chamoji><b>$petname[0]</b></font></td><td width=30 align=center><b>$petlv[0]</td><td width=40 align=center><b>$petritu[0]</td><td width=140 align=center><b>$petkouka[0]</td><td width=30 align=center><b>$petkouka2[0]</td><td width=190 align=center><img src="$maindir/$imgfile/exp.gif" height="10"><img src="$maindir/$imgfile/jobbar1.gif" width=$petbarcha1 height="8">$petbardmg2<img src="$maindir/$imgfile/exp.gif" height="8"></td></tr>
<tr><td width=25 align=center><b>2</b></td><td width=180><font color=#$chamoji><b>$petname[1]</b></font></td><td width=30 align=center><b>$petlv[1]</td><td width=40 align=center><b>$petritu[1]</td><td width=140 align=center><b>$petkouka[1]</td><td width=30 align=center><b>$petkouka2[1]</td><td width=190 align=center><img src="$maindir/$imgfile/exp.gif" height="10"><img src="$maindir/$imgfile/jobbar1.gif" width=$petbarcha11 height="8">$petbardmg22<img src="$maindir/$imgfile/exp.gif" height="8"></td></tr>
<tr><td width=25 align=center><b>3</b></td><td width=180><font color=#$chamoji><b>$petname[2]</b></font></td><td width=30 align=center><b>$petlv[2]</td><td width=40 align=center><b>$petritu[2]</td><td width=140 align=center><b>$petkouka[2]</td><td width=30 align=center><b>$petkouka2[2]</td><td width=190 align=center><img src="$maindir/$imgfile/exp.gif" height="10"><img src="$maindir/$imgfile/jobbar1.gif" width=$petbarcha111 height="8">$petbardmg222<img src="$maindir/$imgfile/exp.gif" height="8"></td></tr>
</table>
</td></tr></table>
<br>
<font color=green>戦闘能\力</font>：<b>$heikin2</b></font>　　<font color=darkblue>マスタージョブ</font>：<b>$masterjob</b></font>　
<font color=#$mojiiro3>戦闘勝利</font>：<b>$chastats[10]</b></font>回　
<font color=#$mojiiro4>戦闘敗北</font>：<b>$chastats[12]</b></font>回　
<font color=brown>転生回数</font>：<b>$tensei</b></font>回<br>

HTM
}



#　アイテム欄表示処理
sub itemtable {
print <<HTM;
<center>
<table border=0 width=520><tr><td>
<table border=1 bordercolor=#$wakuiro width=250><tr>
<td colspan=3 align=center><b>アイテム</b></td></tr>
<tr><td width=25 align=center><b>1</b></td><td width=200><font color=#$chamoji><b>$chaitem[1]</b></font></td><td width=15 align=right><font color=#$chamoji><b>$chaeff[1]</b></font></td></tr>
<tr><td width=25 align=center><b>2</b></td><td width=200><font color=#$chamoji><b>$chaitem[2]</b></font></td><td width=15 align=right><font color=#$chamoji><b>$chaeff[2]</b></font></td></tr>
<tr><td width=25 align=center><b>3</b></td><td width=200><font color=#$chamoji><b>$chaitem[3]</b></font></td><td width=15 align=right><font color=#$chamoji><b>$chaeff[3]</b></font></td></tr>
<tr><td width=25 align=center><b>4</b></td><td width=200><font color=#$chamoji><b>$chaitem[4]</b></font></td><td width=15 align=right><font color=#$chamoji><b>$chaeff[4]</b></font></td></tr>
<tr><td width=25 align=center><b>5</b></td><td width=200><font color=#$chamoji><b>$chaitem[5]</b></font></td><td width=15 align=right><font color=#$chamoji><b>$chaeff[5]</b></font></td></tr>
<tr><td width=25 align=center><b>6</b></td><td width=200><font color=#$chamoji><b>$chaitem[6]</b></font></td><td width=15 align=right><font color=#$chamoji><b>$chaeff[6]</b></font></td></tr>
<tr><td width=25 align=center><b>7</b></td><td width=200><font color=#$chamoji><b>$chaitem[7]</b></font></td><td width=15 align=right><font color=#$chamoji><b>$chaeff[7]</b></font></td></tr>
<tr><td width=25 align=center><b>8</b></td><td width=200><font color=#$chamoji><b>$chaitem[8]</b></font></td><td width=15 align=right><font color=#$chamoji><b>$chaeff[8]</b></font></td></tr>

</table>
</td><td rowspan=2>
<table border=1 bordercolor=#$wakuiro width=250><tr>
<td colspan=2 align=center><b>装備</b></td></tr>
<tr><td width=25 align=center><nobr><b>右手</b></nobr></td><td width=220><font color=#$chamoji><b>$chasoubi[1]</b></font></td></tr>
<tr><td width=25 align=center><nobr><b>左手</b></nobr></td><td width=220><font color=#$chamoji><b>$chasoubi[2]</b></font></td></tr>
<tr><td width=25 align=center><b>頭</b></td><td width=220><font color=#$chamoji><b>$chasoubi[3]</b></font></td></tr>
<tr><td width=25 align=center><b>胸</b></td><td width=220><font color=#$chamoji><b>$chasoubi[4]</b></font></td></tr>
<tr><td width=25 align=center><b>脚</b></td><td width=220><font color=#$chamoji><b>$chasoubi[5]</b></font></td></tr>
<tr><td width=25 align=center><b>腕</b></td><td width=220><font color=#$chamoji><b>$chasoubi[6]</b></font></td></tr>
<tr><td width=25 align=center><b>指</b></td><td width=220><font color=#$chamoji><b>$chasoubi[7]</b></font></td></tr>
<tr><td width=25 align=center><b>首</b></td><td width=220><font color=#$chamoji><b>$chasoubi[8]</b></font></td></tr>
</table>
</td></tr></table>

HTM
}





sub hpsaisyo {


if ( $bgurl ne "" ){
	$bgmode = "background=\"$bgurl\"";
} else {
	$bgmode = "bgcolor=\#$bgclr";
}

print <<HTML;
Content-type: text/html

<html><head><title>$title - ($chaname)</title>
<STYLE type="text/css">
A { text-decoration: none }
</STYLE>

</head>
<body $bgmode link=#$linkiro vlink=#$vlinkiro>
<basefont size=2 color=#$mojiiro><br>

HTML

}

sub hpowari {
#　著作権表記は削除または見にくくしないように。
print <<HTM;
<br><hr>
<div align=right>オンラインRPG「Vagoo」　配布元：「<a href="http://www.sky-wing.com/~game/" target="_blank">うぇぶなげぇむ</a>」</div>
<div align=right>オンラインRPG「Gyagoo」　配布元：「<a href="http://blog.livedoor.jp/nonsense777/archives/50170214.html" target="_blank">Gyagoo配布所</a>」</div><br>

</font></center>
</body></html>
<noscript>
<META HTTP-EQUIV="Refresh" CONTENT="0;URL=java.html">
</noscript>
HTM
$cnt
}

sub jobdataload {
open(JOBD,"$maindir/job$bousikts");
	while ( $datajob = <JOBD> ) {
	($jobcode,$jobweight,$jobpet) = split(/,/,$datajob);
		if ( $jobcode == $chaclass ) {
		last;
		}
	}
close(JOBD);
}

sub proxychk {
if ($bad_host) {
local($badproxy,$badmode) = ();
while(($badproxy,$badmode) = each(%ENV)){
if($badproxy =~ /kfw001/i || $badmode =~ /kfw001/i){
&hpsaisyo;
print <<"HTM";
<font size=5 color=#$mojiiro2><b>プロクシ経由からのアクセスはできません。</b></font><br><br>

HTM
&hpowari;
exit;
  }
 }
}
}


sub fuseisyori {
print <<"HTML01";
<b><font size=6 color=#$mojiiro2>★　エラー　★</font></b><br><br>
・カウントダウン終了前に行動をした<br>
・転送データの改変<br>
・ペットやアイテムデータの未実装<br>
・外部スクリプトからのアクセス<br>
・スクリプトのバグ<br><br>

いずれかの原因が考えられます。<br>
これらの中にはブラウザの「戻る」→「更新」で解決するものもあります。<br><br>
それでもエラーが出る場合はログイン画面からやり直してください。<br><br>
<font size=4><b>[<a href="./index.html"> ログイン画面に戻る </a></font></b>]<br>
HTML01
&hpowari;
exit;
}



sub mente {
print <<"HTML01";
<b><font size=6 color=#$mojiiro2>★　メンテナンス中　★</font></b><br><br>
現在メンテナンスを行っております。<br>
ご迷惑をお掛けしますが、時間を置いてから、再度接続を試みてください。<br><br>
HTML01
&hpowari;
exit;
}


sub ipblock {
	foreach $blocking ( @block ) {
		if ( $ENV{REMOTE_ADDR} =~ /$blocking/i ) {
&hpsaisyo;
print <<"HTM";
<font size=5 color=#$mojiiro2><b>あなたのIPはブロックされています</b></font><br><br>

HTM
&hpowari;
exit;
		}
	}
}




sub gaibublock {
$gaibu = 0;
	if ( $ENV{HTTP_REFERER} =~ /$urlbase/i ) { $gaibu ++; }
	if ( $ENV{HTTP_REFERER} =~ /$urlbase2/i ) { $gaibu ++; }
	if ( $gaibu == 0 ) { &hpsaisyo;&fuseisyori;exit; }
}

sub cookieset {
($secg,$ming,$hourg,$mdayg,$mong,$yearg,$wdayg,$ydayg,$isdstg ) = gmtime(time + (0*0*0));
@youbi = ("Sun","Mon","Tue","Wed","Thu","Fri","Sat");
@monthg = ("Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec");
$date_gmt = sprintf("%s\, %02d\-%s\-%04d %02d:%02d:%02d GMT",$youbi[$wdayg],$mdayg,$monthg[$mong],$yearg +1900,$hourg,$ming,$secg);
print "Set-Cookie: FUKUIDCHK=$in{usrid}; expires=$date_gmt; domain=$cgidomain; path=$cgidomain2\n";
}

sub cookieget {

($cookies,$a) = split(/; /,$ENV{HTTP_COOKIE});
($key,$value) = split(/=/,$cookies);
$usridchk{$key} = $value;

}
srand;
1;