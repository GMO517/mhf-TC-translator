# 待決專名（翻譯中標記）

> Translator 拿不定、或曾出現**半翻**時列在這裡。  
> **禁止**用「全形拉丁字母＋片假名」充數（見 docs/STYLE.md）。  
> 該 CATEGORY／子類**整段譯完後**，使用者在「決定」欄給定譯 → Fixer 回寫 CSV／batches。  
> 已定稿可移入 `terms.csv`（approved=Y）並從本表刪除或標 `decided`。

## 欄位（必填）

| 欄 | 說明 |
|---|---|
| source 關鍵 | 詞根／專名 key |
| 例 index／原文／現況 | 溯源與目前 CSV 暫譯 |
| **建議譯** | Agent **必填**一版推薦寫法（須符合禁半翻） |
| **建議理由** | **必填**：為何這樣建議（wiki／義譯／音譯／避半翻／缺字等） |
| 決定 | **僅使用者填**；空白＝尚未裁定 |
| status | pending／decided |

---

## 已決定

| source 關鍵 | 例 index | 例原文 | 現況 | 建議譯（當時） | 建議理由 | 決定 | status |
|---|---|---|---|---|---|---|---|
| Crest | 9345 | C Crest Tkt | Ｃ・紋章票 | Ｃ・紋章票 | Crest＝紋章（普通名詞義譯）；字母碼＋・＋漢字 | **紋章** → Ｃ・紋章票 | decided |

---

## items-name / tickets（待決）

> 前段含歷史半翻；後段多為音譯暫譯。請在「決定」欄批示；Fixer 再回修。

| source 關鍵 | 例 index | 例原文 | 現況（半翻／暫譯） | 建議譯 | 建議理由 | 決定（使用者填） | status |
|---|---|---|---|---|---|---|---|
| Creek | 1708 | M Creek Tkt | Ｍクリーク票 | Ｍ・溪流票 | Creek＝溪流（普通名詞）；字母碼＋・＋漢字，去掉片假名半翻 |  | pending |
| Marsh | 1709 | B Marsh Tkt | Ｂマルシュ票 | Ｂ・沼澤票 | Marsh＝沼澤；同 Crest 格式（字母・漢字） |  | pending |
| Bolt | 2974 | W Bolt Tkt | Ｗボルト票 | Ｗ・雷栓票 | Bolt 在 MH 武器脈絡多指銃／雷栓義；避免 Ｗボルト 半翻 |  | pending |
| Fang | 2975 | C Fang Tkt | Ｃファング票 | Ｃ・牙票 | Fang＝牙（漢字義譯）；Ｃ／Ｔ 為系列碼 |  | pending |
| Lever | 4017 | V Lever Tkt | Ｖレバー票 | Ｖ・槓桿票 | Lever＝槓桿；若爆框可再縮 |  | pending |
| Rose | 4021 | A Rose Tkt | Ａローズ票 | Ａ・薔薇票 | Rose＝薔薇／玫瑰；採遊戲常見「薔薇」 |  | pending |
| Derose | 4022 | A Derose Tkt | Ａデローズ票 | デローズＡ票 | 疑專名 Derose／デローズ；採「片假名＋系列碼Ａ」，禁止 Ａデローズ 半翻 |  | pending |
| Tweeter | 5655 | S Tweeter Tkt | Ｓツィータ票 | Ｓ・高音票 | Tweeter＝高音單元（音響義）；非專名時用漢字 |  | pending |
| Fanare | 5657 | S Fanare Tkt | Ｓファナレ票 | ファナレＳ票 | 疑專名音譯；採「片假名＋系列碼」避免 Ｓファナレ 半翻 |  | pending |
| Blade | 6476 | D Blade Tkt | Ｄブレイド票 | Ｄ・刃票 | Blade＝刃／劍；短 UI 用「刃」 |  | pending |
| Lance | 6478 | C Lance Tkt | Ｃランス票 | Ｃ・槍票 | Lance＝槍；與武器種「銃槍」區隔時可再調 |  | pending |
| Mortar | 6480 | S Mortar Tkt | Ｓモルタル票 | Ｓ・迫擊砲票 | Mortar＝迫擊砲；若過長可縮「迫擊票」 |  | pending |
| Cavalry | 6484 | S Cavalry Tkt | Ｓカルバリ票 | Ｓ・騎兵票 | Cavalry＝騎兵 |  | pending |
| Gear | 7164 | D Gear Tkt | Ｄギア票 | Ｄ・齒輪票 | Gear＝齒輪／裝置；道具名優先「齒輪」 |  | pending |
| Carbine | 7166 | IM Carbine Tkt | ＩＭカービン票 | ＩＭ・短步槍票 | Carbine＝卡賓槍；「卡」可能缺字故用「短步槍」 |  | pending |
| Tomen | 7272 | IM Tomen Tkt | ＩＭトメン票 | トメンＩＭ票 | 疑專名；「片假名＋ＩＭ」避免 ＩＭトメン 半翻 |  | pending |
| Regil | 7999 | GE Regil Tkt | ＧＥレギル票 | レギルＧＥ票 | 疑專名；名＋ＧＥ 後綴 |  | pending |
| Dore | 8000 | GE Dore Tkt | ＧＥドーレ票 | ドーレＧＥ票 | 疑專名；名＋ＧＥ |  | pending |
| Greed | 8190 | E Greed Tkt | Ｅグリード票 | Ｅ・貪婪票 | Greed＝貪婪（漢字）；字母碼＋・＋漢字 |  | pending |
| Vang | 8339 | E Vang Tkt | Ｅヴァング票 | ヴァングＥ票 | 疑專名音譯；名＋Ｅ |  | pending |
| Aria | 8820 | I Aria Tkt | Ｉアリア票 | アリアＩ票 | 疑專名／曲名 Aria；名＋字母碼 |  | pending |
| Bank | 8821 | I Bank Tkt | Ｉバンク票 | バンクＩ票 | Bank 作專名暫音譯；名＋字母（若指銀行可改「銀行」） |  | pending |
| Tavros | 9346 | N Tavros Tkt | Ｎタウロス票 | タウロスＮ票 | 疑專名（牛座音近）；名＋Ｎ |  | pending |
| Pact | 9696 | C Pact Tkt | Ｃパクト票 | Ｃ・契約票 | Pact＝契約；字母・漢字 |  | pending |
| Veran | 9837 | Veran Tkt Head | ヴェラン頭票 | ヴェラン頭票 | 音譯 |  | pending |
| Endore | 9847 | Endore Tkt Head | エンドア頭票 | エンドア頭票 | 音譯 |  | pending |
| Done Cat | 10357 | Done Cat Tkt Head | ドーネ猫頭票 | ドーネ猫頭票 | 音譯 |  | pending |
| Gemtail | 10379 | Neko Gemtail Tkt | 宝石尾猫票 | 宝石尾猫票 | 音譯 |  | pending |
| Harze | 10380 | Harze Ticket | ハルゼ票 | ハルゼ票 | 音譯 |  | pending |
| Stradia | 10593 | Stradia Tkt | ストラディア票 | ストラディア票 | 音譯 |  | pending |
| Riura | 10594 | Riura Tkt | リウラ票 | リウラ票 | 音譯 |  | pending |
| Larcia | 10595 | Larcia Tkt | ラルシア票 | ラルシア票 | 音譯 |  | pending |
| Shelsha | 10596 | Shelsha Tkt | シェルシャ票 | シェルシャ票 | 音譯 |  | pending |
| Lagri | 10597 | Lagri Tkt | ラグリ票 | ラグリ票 | 音譯 |  | pending |
| Zaouli | 10604 | Zaouli Tkt | ザウリ票 | ザウリ票 | 音譯 |  | pending |
| Defi | 10615 | Defi Tkt | デフィ票 | デフィ票 | 音譯 |  | pending |
| Vizov | 10616 | Vizov Tkt | ヴィゾフ票 | ヴィゾフ票 | 音譯 |  | pending |
| Lies | 10617 | Lies Tkt | リース票 | リース票 | 音譯 |  | pending |
| Via | 10618 | Via Tkt | ヴィア票 | ヴィア票 | 音譯 |  | pending |
| Ketto | 10619 | Ketto Tkt | ケット票 | ケット票 | 音譯 |  | pending |
| Poisuku | 10626 | Poisuku Tkt | ポイスク票 | ポイスク票 | 音譯 |  | pending |
| Lorelei | 10633 | Lorelei Tkt | ロレライ票 | ロレライ票 | 音譯 |  | pending |
| Mansana | 10634 | Mansana Tkt | マンサナ票 | マンサナ票 | 音譯 |  | pending |
| Fata | 10635 | Fata Tkt | ファタ票 | ファタ票 | 音譯 |  | pending |
| Fleur | 10636 | Fleur Tkt | フルール票 | フルール票 | 音譯 |  | pending |
| Risty | 10662 | Risty Tkt | リスティ票 | リスティ票 | 音譯 |  | pending |
| Del Sur | 10663 | Del Sur Tkt | デルスル票 | デルスル票 | 音譯 |  | pending |
| Trihes | 10664 | Trihes Tkt | トリヘス票 | トリヘス票 | 音譯 |  | pending |
| Lux Raw | 10665 | Lux Raw Tkt | リュクス生票 | リュクス生票 | 音譯 |  | pending |
| Zut Student | 10666 | Zut Student Tkt | ズット生徒票 | ズット生徒票 | 音譯 |  | pending |
| Madoka | 10750 | Madoka Tkt | マドカ票 | マドカ票 | 音譯 |  | pending |
| Trume | 10780 | Trume Tkt | トルメ票 | トルメ票 | 音譯 |  | pending |
| Bande | 10800 | Bande Tkt (Head) | バンデ頭票 | バンデ頭票 | 音譯 |  | pending |
| Bendi | 10810 | Bendi Tkt | ベンディ票 | ベンディ票 | 音譯 |  | pending |
| Revenants | 10811 | Revenants Tkt | レヴナント票 | レヴナント票 | 音譯 |  | pending |
| Cardia | 11174 | Cardia Tkt | カルディア票 | カルディア票 | 音譯 |  | pending |
| Munimy | 11175 | Munimy Tkt | ムニミ票 | ムニミ票 | 音譯 |  | pending |
| Pugi | 11242 | 3P Pugi Tkt | プギ３票 | プギ３票 | 音譯 |  | pending |
| Azoth | 11288 | Azoth Tkt | アゾット票 | アゾット票 | 音譯 |  | pending |
| Marinero | 11292 | Marinero Tkt | マリネロ票 | マリネロ票 | 音譯 |  | pending |
| Materoto | 11293 | Materoto Tkt | マテロト票 | マテロト票 | 音譯 |  | pending |
| Maru | 11294 | Maru Tkt | マル票 | マル票 | 音譯 |  | pending |
| Thalassa | 11295 | Thalassa Tkt | タラサ票 | タラサ票 | 音譯 |  | pending |
| Ruvuni | 11301 | Ruvuni Tkt | ルヴニ票 | ルヴニ票 | 音譯 |  | pending |
| Viri | 11303 | Viri Tkt | ヴィリ票 | ヴィリ票 | 音譯 |  | pending |
| Tupars | 11307 | Tupars Tkt | トゥパルス票 | トゥパルス票 | 音譯 |  | pending |
| Zafia | 11308 | Zafia Tkt | ザフィア票 | ザフィア票 | 音譯 |  | pending |
| Oniche | 11309 | Oniche Tkt | オニチェ票 | オニチェ票 | 音譯 |  | pending |
| Manaito | 11313 | Manaito Tkt | マナイト票 | マナイト票 | 音譯 |  | pending |
| Supirune | 11314 | Supirune Tkt | スピルネ票 | スピルネ票 | 音譯 |  | pending |
| Valier | 11330 | Valier Tkt | ヴァリエ票 | ヴァリエ票 | 音譯 |  | pending |
| Louise | 11331 | Louise Tkt | ルイーズ票 | ルイーズ票 | 音譯 |  | pending |
| Rei Alma | 11332 | Rei Alma Tkt | レイアルマ票 | レイアルマ票 | 音譯 |  | pending |
| Kanpi | 11333 | Kanpi Tkt | カンピ票 | カンピ票 | 音譯 |  | pending |
| Vinci | 11334 | Vinci Tkt | ヴィンチ票 | ヴィンチ票 | 音譯 |  | pending |
| Esse | 11378 | Esse SC Tkt | エッセＳＣ票 | エッセＳＣ票 | 音譯 |  | pending |
| Regu | 11405 | Regu Cat Tkt | レグ猫票 | レグ猫票 | 音譯 |  | pending |
| Rufflet | 11431 | Rufflet Tkt Head | ラフレット頭票 | ラフレット頭票 | 音譯 |  | pending |
| Bronte | 11436 | Bronte Tkt | ブロンテ票 | ブロンテ票 | 音譯 |  | pending |
| Solene | 11437 | Solene Tkt | ソレーヌ票 | ソレーヌ票 | 音譯 |  | pending |
| Rapinu | 11438 | Rapinu Ticket | ラピヌ票 | ラピヌ票 | 音譯 |  | pending |
| Tropio | 11442 | Tropio Tkt | トロピオ票 | トロピオ票 | 音譯 |  | pending |
| Tarneko | 11455 | Gold Tarneko Tkt | 金タルネコ票 | 金タルネコ票 | 音譯 |  | pending |
| Cilty | 11804 | Cilty Tkt | チルティ票 | チルティ票 | 音譯 |  | pending |
| Airyu | 11982 | Airyu Tkt | アイリュ票 | アイリュ票 | 音譯 |  | pending |
| Cornpopper | 11983 | Cornpopper Tkt | コーンポッパー票 | コーンポッパー票 | 音譯 |  | pending |
| Gaiasp | 11984 | Gaiasp Tkt | ガイアスプ票 | ガイアスプ票 | 音譯 |  | pending |
| Chak Chak | 11985 | Chak Chak Tkt | チャクチャク票 | チャクチャク票 | 音譯 |  | pending |
| Arca | 11986 | Arca Tkt | アルカ票 | アルカ票 | 音譯 |  | pending |
| Rashino | 11991 | Rashino Tkt | ラシノ票 | ラシノ票 | 音譯 |  | pending |
| Rosson | 11992 | Rosson Tkt | ロッソン票 | ロッソン票 | 音譯 |  | pending |
| Longinus | 11995 | Longinus Tkt | ロンギヌス票 | ロンギヌス票 | 音譯 |  | pending |
| Dist | 12027 | S Dist Tkt | ディストＳ票 | ディストＳ票 | 音譯 |  | pending |
| Troll | 12028 | S Troll Tkt | トロールＳ票 | トロールＳ票 | 音譯 |  | pending |
| Est | 12029 | S Est Tkt | エストＳ票 | エストＳ票 | 音譯 |  | pending |
| Mira | 12030 | S Mira Tkt | ミラＳ票 | ミラＳ票 | 音譯 |  | pending |
| Domino | 12031 | S Domino Tkt | ドミノＳ票 | ドミノＳ票 | 音譯 |  | pending |
| Etotra | 12023 | Etotra Tkt | エトトラ票 | エトトラ票 | 音譯 |  | pending |
| Latesia | 12024 | Latesia Tkt | ラテシア票 | ラテシア票 | 音譯 |  | pending |
| Artes | 12025 | Artes Tkt | アルテス票 | アルテス票 | 音譯 |  | pending |
| Polemika | 12026 | Polemika Tkt | ポレミカ票 | ポレミカ票 | 音譯 |  | pending |
| Pral | 12032 | Pral Tkt | プラル票 | プラル票 | 音譯 |  | pending |
| Larufi | 12033 | Larufi Tkt | ラルフィ票 | ラルフィ票 | 音譯 |  | pending |
| Yufal | 12040 | Yufal Tkt | ユファル票 | ユファル票 | 音譯 |  | pending |
| Pen Cat | 12061 | Pen Cat Tkt Head | ペン猫頭票 | ペン猫頭票 | 音譯 |  | pending |
| Gania | 12152 | Gania Tkt Head | ガニア頭票 | ガニア頭票 | 音譯 |  | pending |
| Valenti | 12393 | Valenti Tkt | ヴァレンティ票 | ヴァレンティ票 | 音譯 |  | pending |
| Begia | 12394 | Begia Tkt | ベギア票 | ベギア票 | 音譯 |  | pending |
| Aniba | 12400 | Aniba Quest Tkt | アニバ任務票 | アニバ任務票 | 音譯 |  | pending |
| Riko | 12416 | Riko No. Tkt | リコノ票 | リコノ票 | 音譯 |  | pending |
| Gio | 12423 | Gio No. Tkt | ジオノ票 | ジオノ票 | 音譯 |  | pending |
| Azul | 12430 | Azul Tkt | アズール票 | アズール票 | 音譯 |  | pending |
| Verde | 12434 | Verde Tkt | ヴェルデ票 | ヴェルデ票 | 音譯 |  | pending |
| Cassius | 12436 | Cassius Tkt | カシウス票 | カシウス票 | 音譯 |  | pending |
| Volga | 12470 | Volga Tkt | ヴォルガ票 | ヴォルガ票 | 音譯 |  | pending |
| Tallfish | 12472 | Tallfish Tkt | トールフィッシュ票 | トールフィッシュ票 | 音譯 |  | pending |
| Kaila | 12505 | Kaila Ticket | カイラ票 | カイラ票 | 音譯 |  | pending |
| Veitch | 12509 | Veitch Ticket | ヴィーチ票 | ヴィーチ票 | 音譯 |  | pending |
| Amista | 12525 | Amista Tkt Head | アミスタ頭票 | アミスタ頭票 | 音譯 |  | pending |
| Amineko | 12769 | Amineko Tkt | アミ猫票 | アミ猫票 | 音譯 |  | pending |
| Gagachu | 12853 | Gagachu Ticket | ガガチュ票 | ガガチュ票 | 音譯 |  | pending |
| Cielo | 12872 | Cielo Ticket | シエロ票 | シエロ票 | 音譯 |  | pending |
| Salta | 12873 | Salta Tkt | サルタ票 | サルタ票 | 音譯 |  | pending |
| Peri Cat | 12975 | Peri Cat Tkt | ペリ猫票 | ペリ猫票 | 音譯 |  | pending |
| Mimital | 12983 | Mimital Tkt | ミミタル票 | ミミタル票 | 音譯 |  | pending |
| Feza | 12987 | Feza Tkt | フェザ票 | フェザ票 | 音譯 |  | pending |
| Ryu | 12991 | Ryu Dragon Tkt | リュウ竜票 | リュウ竜票 | 音譯 |  | pending |
| Engetsu | 12993 | Engetsu Thndr Tkt | エンゲツ雷票 | エンゲツ雷票 | 音譯 |  | pending |
| Ranze | 13013 | Ranze B Tkt | ランゼＢ票 | ランゼＢ票 | 音譯 |  | pending |
| Perif | 13022 | Perif Tkt Head | ペリフ頭票 | ペリフ頭票 | 音譯 |  | pending |
| Kaiji | 13023 | Kaiji Tkt | カイジ票 | カイジ票 | 音譯 |  | pending |
| Souffle | 13028 | Souffle Tkt | スフレ票 | スフレ票 | 音譯 |  | pending |
| Arbden | 13177 | Arbden Ticket | アルブデン票 | アルブデン票 | 音譯 |  | pending |
| Keravuno | 13178 | Keravuno Ticket | ケラヴノ票 | ケラヴノ票 | 音譯 |  | pending |
| Waka | 13326 | Waka Ticket | ワカ票 | ワカ票 | 音譯 |  | pending |
| Flare | 13327 | S Flare Tkt Ⅰ | フレアＳ票Ⅰ | フレアＳ票Ⅰ | 音譯 |  | pending |
| Gu Neko | 13392 | Gu Neko Tkt | グ猫票 | グ猫票 | 音譯 |  | pending |
| Rufus | 13437 | Rufus Tkt | ルーファス票 | ルーファス票 | 音譯 |  | pending |
| Aura | 13449 | Aura Ticket | オーラ票 | オーラ票 | 音譯 |  | pending |
| Taruta | 13451 | Taruta Tkt | タルタ票 | タルタ票 | 音譯 |  | pending |
| Ruruta | 13452 | Ruruta Tkt | ルルタ票 | ルルタ票 | 音譯 |  | pending |
| Clofi | 13453 | Clofi Ticket | クロフィ票 | クロフィ票 | 音譯 |  | pending |
| Gudan | 13454 | Gudan Tkt Head | グダン頭票 | グダン頭票 | 音譯 |  | pending |
| Chiarim | 13508 | Chiarim Ticket | キアリム票 | キアリム票 | 音譯 |  | pending |
| Evoneko | 13624 | Evoneko Tkt | エボ猫票 | エボ猫票 | 音譯 |  | pending |
| Tio | 13626 | Tio Tkt | ティオ票 | ティオ票 | 音譯 |  | pending |
| Zio | 13627 | Zio Tkt | ジオ票 | ジオ票 | 音譯 |  | pending |
| Solitaire | 13786 | Solitaire Tkt | ソリティア票 | ソリティア票 | 音譯 |  | pending |
| Sakufi | 13790 | Sakufi Tkt | サクフィ票 | サクフィ票 | 音譯 |  | pending |
| Asumo | 13791 | Asumo Ticket | アスモ票 | アスモ票 | 音譯 |  | pending |
| Dios | 13792 | Dios Tkt | ディオス票 | ディオス票 | 音譯 |  | pending |
| Carrol | 13794 | Carrol C Tkt | キャロルＣ票 | キャロルＣ票 | 音譯 |  | pending |
| Loose | 13796 | Loose C Tkt | ルーズＣ票 | ルーズＣ票 | 音譯 |  | pending |
| Harokyu | 13797 | Harokyu D Tkt | ハロキュＤ票 | ハロキュＤ票 | 音譯 |  | pending |
| Higakure | 13798 | Higakure C Tkt | ヒガクレＣ票（或日隠Ｃ） | ヒガクレＣ票 | 音譯 |  | pending |
| Evol | 13894 | Evol D Tkt | エヴォルＤ票 | エヴォルＤ票 | 音譯 |  | pending |
| Destin | 13936 | Destin Tkt | デスタン票 | デスタン票 | 音譯 |  | pending |
| Diletto | 13940 | Diletto Tkt | ディレット票 | ディレット票 | 音譯 |  | pending |
| Solte | 13942 | D Solte Tkt | ソルテＤ票 | ソルテＤ票 | 音譯 |  | pending |
| San | 13952 | E San Tkt | サンＥ票 | サンＥ票 | 音譯 |  | pending |
| Shin | 13953 | E Shin Tkt | シンＥ票 | シンＥ票 | 音譯 |  | pending |
| Snow Miku | 13960 | Snow Miku Tkt | 雪ミク票（wiki 外装ユキネ） | 雪ミク票 | wiki／既有 |  | pending |
| Wander | 13961 | Wander Tkt | ワンダレ票 | ワンダレ票 | 音譯 |  | pending |
| Muruta | 13962 | Muruta Ticket | ムルタ票 | ムルタ票 | 音譯 |  | pending |
| Howla | 13963 | Howla Ticket | ハウラ票 | ハウラ票 | 音譯 |  | pending |
| Panse | 13964 | Panse Ticket | パンセ票 | パンセ票 | 音譯 |  | pending |
| Marriage | 13965 | Marriage Ticket | マリジュ票 | マリジュ票 | 音譯 |  | pending |
| Ice Emperor D | 13967 | Blue Ice Emperor D Tkt | 蒼氷帝Ｄ票（wiki 皇氷） | 蒼氷帝Ｄ票 | wiki／既有 |  | pending |
| Rance | 13977 | Rance C Tkt | ランセＣ票 | ランセＣ票 | 音譯 |  | pending |
| Asteli | 14008 | Asteli D Tkt | アステリＤ票 | アステリＤ票 | 音譯 |  | pending |
| Harve | 14012 | Harve D Tkt | ハーヴェストＤ票 | ハーヴェストＤ票 | 音譯 |  | pending |
| Melan | 14013 | Melan D Tkt | メランＤ票 | メランＤ票 | 音譯 |  | pending |
| Diru | 14014 | Diru D Tkt | ディールＤ票 | ディールＤ票 | 音譯 |  | pending |
| Tandre | 14015 | Tandre D Tkt | タンドレスＤ票 | タンドレスＤ票 | 音譯 |  | pending |
| Ganeto | 14017 | Ganeto D Tkt | ガネトＤ票 | ガネトＤ票 | 音譯 |  | pending |
| Chiru | 14018 | Chiru D Tkt | チールＤ票 | チールＤ票 | 音譯 |  | pending |
| Shiusu | 14019 | Shiusu D Tkt | シウスＤ票 | シウスＤ票 | 音譯 |  | pending |
| Uruki | 14020 | Uruki D Tkt | ウルキＤ票 | ウルキＤ票 | 音譯 |  | pending |
| Wans | 14021 | Wans D Tkt | ワンスＤ票 | ワンスＤ票 | 音譯 |  | pending |
| Pale Sakura | 14022 | Pale Sakura D Tkt | 薄桜Ｄ票 | 薄桜Ｄ票 | 音譯 |  | pending |
| Iris | 14023 | Iris D Tkt | アイリスＤ票 | アイリスＤ票 | 音譯 |  | pending |
| Wasou D | 14031 | Wasou D Tkt | 和装Ｄ票（wiki 和奏） | 和装Ｄ票 | wiki／既有 |  | pending |
| Obituary | 14033 | Obituary D Tkt | 訃告Ｄ票 | 訃告Ｄ票 | 音譯 |  | pending |
| Butterfly D | 14034 | Butterfly D Tkt | 蝶Ｄ票 | 蝶Ｄ票 | 音譯 |  | pending |
| V Ad | 14035 | V Ad D Tkt | アドＶＤ票 | アドＶＤ票 | 音譯 |  | pending |
| V Reje | 14036 | V Reje D Tkt | レジェＶＤ票 | レジェＶＤ票 | 音譯 |  | pending |
| Demon Lord | 14037 | Demon Lord D Tkt | 魔王Ｄ票 | 魔王Ｄ票 | 音譯 |  | pending |
| Demon Tale | 14038 | Demon Tale D Tkt | 魔譚Ｄ票 | 魔譚Ｄ票 | 音譯 |  | pending |
| Demon Rule | 14039 | Demon Rule D Tkt | 魔則Ｄ票 | 魔則Ｄ票 | 音譯 |  | pending |
| Bistro | 14040 | Bistro D Tkt | ビストロＤ票 | ビストロＤ票 | 音譯 |  | pending |
| IC Sword | 14065 | IC Sword Tkt | ＩＣ剣票 | ＩＣ剣票 | 音譯 |  | pending |
| LH Sword | 14066 | LH Sword Tkt | ＬＨ剣票 | ＬＨ剣票 | 音譯 |  | pending |
| G Reaper | 14067 | G Reaper Tkt | Ｇ・死神票 | ・Ｇ死神票 | 避半翻：名＋字母碼 |  | pending |
| Saga | 14069 | Saga Tkt | サガ票 | サガ票 | 音譯 |  | pending |
| T260G | 14070 | T260G Tkt | Ｔ２６０Ｇ票 | Ｔ２６０Ｇ票 | 音譯 |  | pending |
| Emil | 14088 | Emil D Tkt | エミルＤ票 | エミルＤ票 | 音譯 |  | pending |
| Hesham | 14089 | Hesham Ticket | ヘシュム票 | ヘシュム票 | 音譯 |  | pending |
| Kasamie | 14091 | Kasamie Ticket | カサミエ票 | カサミエ票 | 音譯 |  | pending |
| Spooky | 14094 | Spooky Tkt | 怪奇票 | 怪奇票 | 音譯 |  | pending |
| Kinosu | 14104 | Kinosu D Tkt | キノスＤ票 | キノスＤ票 | 音譯 |  | pending |
| Himeros | 14105 | Himeros D Tkt | ヒメロスＤ票 | ヒメロスＤ票 | 音譯 |  | pending |
| Charien | 14106 | Charien D Tkt | カリエンＤ票 | カリエンＤ票 | 音譯 |  | pending |
| Arie | 14107 | Arie D Tkt | アリエＤ票 | アリエＤ票 | 音譯 |  | pending |
| Craft | 14108 | Craft D Tkt | クラフトＤ票 | クラフトＤ票 | 音譯 |  | pending |
| Shieri | 14109 | Shieri D Tkt | シエリーＤ票 | シエリーＤ票 | 音譯 |  | pending |
| Pupen | 14110 | Pupen D Tkt | プペンＤ票 | プペンＤ票 | 音譯 |  | pending |
| Moss Cover | 14111 | Moss Cover D Tkt | モスカバＤ票 | モスカバＤ票 | 音譯 |  | pending |
| Excelle | 14112 | Excelle D Tkt | エクセレＤ票 | エクセレＤ票 | 音譯 |  | pending |
| Ordre | 14113 | Ordre D Tkt | オルドルＤ票 | オルドルＤ票 | 音譯 |  | pending |
| R Duo | 14114 | R Duo D Tkt | デュオＲＤ票 | デュオＲＤ票 | 音譯 |  | pending |
| Atra | 14115 | Atra D Tkt | アトラＤ票 | アトラＤ票 | 音譯 |  | pending |
| Madaru | 14116 | Madaru D Tkt | マダルＤ票 | マダルＤ票 | 音譯 |  | pending |
| Shasse | 14117 | Shasse D Tkt | シャッセＤ票 | シャッセＤ票 | 音譯 |  | pending |
| Orchesis | 14118 | Orchesis D Tkt | オルケシスＤ票 | オルケシスＤ票 | 音譯 |  | pending |
| Blize | 14119 | Blize D Tkt | ブライズＤ票 | ブライズＤ票 | 音譯 |  | pending |
| Quoiz | 14120 | Quoiz D Tkt | クォイズＤ票 | クォイズＤ票 | 音譯 |  | pending |
| Kalais | 14121 | Kalais D Tkt | カライスＤ票 | カライスＤ票 | 音譯 |  | pending |
| Lucchese | 14122 | Lucchese D Tkt | ルケッセＤ票 | ルケッセＤ票 | 音譯 |  | pending |
| Entora | 14123 | Entora D Tkt | エントラＤ票 | エントラＤ票 | 音譯 |  | pending |
| Vichi | 14126 | Vichi D Tkt | ヴィチＤ票 | ヴィチＤ票 | 音譯 |  | pending |
| Furu | 14184 | Furu B Tkt | フルＢ票 | フルＢ票 | 音譯 |  | pending |
| Arben | 14191 | Arben D Tkt | アーベンＤ票 | アーベンＤ票 | 音譯 |  | pending |
| Penre | 14195 | Penre D Tkt | ペンレＤ票 | ペンレＤ票 | 音譯 |  | pending |
| Rokka | 14197 | Rokka D Tkt | ロッカＤ票 | ロッカＤ票 | 音譯 |  | pending |
| NieR | 14201 | NieR Ticket | ニーア票 | ニーア票 | 音譯 |  | pending |
| White Execution | 14203 | White Execution Tkt | 白処刑票 | 白処刑票 | 音譯 |  | pending |
| White Sorrow | 14204 | White Sorrow Tkt | 白哀惜票 | 白哀惜票 | 音譯 |  | pending |
| 10th Anniv | 14402 | 10th Anniv C Tkt | 10周年Ｃ票（wiki 十ノ軌跡Ｃ） | 10周年Ｃ票 | wiki／既有 |  | pending |
| Zakka | 14406 | Zakka Ticket | ザッカ票 | ザッカ票 | 音譯 |  | pending |
| Rantana | 14407 | Rantana Ticket | ランタナ票 | ランタナ票 | 音譯 |  | pending |
| Eris | 14408 | Eris Tkt | エリス票 | エリス票 | 音譯 |  | pending |
| Magisa | 14417 | Magisa D Tkt | マギサＤ票 | マギサＤ票 | 音譯 |  | pending |
| Shaln | 14418 | Shaln D Tkt | シャランＤ票 | シャランＤ票 | 音譯 |  | pending |
| Chandelier | 14421 | Chandelier D Tkt | シャンディＤ票（既有シャンデ） | シャンディＤ票 | 音譯 |  | pending |
| Korinyi | 14423 | Korinyi D Tkt | コリニィＤ票 | コリニィＤ票 | 音譯 |  | pending |
| Renka | 14424 | Renka D Tkt | レンカＤ票 | レンカＤ票 | 音譯 |  | pending |
| Kukubo | 14428 | Kukubo D Tkt | ククボＤ票 | ククボＤ票 | 音譯 |  | pending |
| Kakabu | 14429 | Kakabu D Tkt | カカブＤ票 | カカブＤ票 | 音譯 |  | pending |
| Aruru | 14430 | Aruru D Tkt | アルルＤ票 | アルルＤ票 | 音譯 |  | pending |
| Scarlet Neko | 14431 | Scarlet Neko D Tkt | 緋猫Ｄ票 | 緋猫Ｄ票 | 音譯 |  | pending |
| Raios | 14432 | Raios D Tkt | ライオスＤ票 | ライオスＤ票 | 音譯 |  | pending |
| Bonito | 14433 | Bonito D Tkt | ボニトＤ票 | ボニトＤ票 | 音譯 |  | pending |
| Meirida | 14434 | Meirida D Tkt | メイリダＤ票 | メイリダＤ票 | 音譯 |  | pending |
| Miniom | 14435 | Miniom D Tkt | ミニオムＤ票 | ミニオムＤ票 | 音譯 |  | pending |
| Harimeno | 14436 | Harimeno D Tkt | ハリメノＤ票 | ハリメノＤ票 | 音譯 |  | pending |
| Deriv | 14437 | Deriv D Tkt | デリヴＤ票 | デリヴＤ票 | 音譯 |  | pending |
| Asaak | 14438 | Asaak D Tkt | アサークＤ票 | アサークＤ票 | 音譯 |  | pending |
| Desert D | 14439 | Desert D Tkt | デゾルトＤ票 | デゾルトＤ票 | 音譯 |  | pending |
| Halgan | 14440 | Halgan D Tkt | ハラガンＤ票 | ハラガンＤ票 | 音譯 |  | pending |
| Abyad | 14441 | Abyad D Tkt | アブヤドＤ票 | アブヤドＤ票 | 音譯 |  | pending |
| Demonclad | 14499 | Demonclad D Tkt | 魔装Ｄ票 | 魔装Ｄ票 | 音譯 |  | pending |
| Scharf | 14500 | Scharf Ticket | シャルフ票 | シャルフ票 | 音譯 |  | pending |
| Kamara | 14501 | Kamara Ticket | カマラ票 | カマラ票 | 音譯 |  | pending |
| Ruche | 14502 | Ruche Ticket | ルーチェ票 | ルーチェ票 | 音譯 |  | pending |
| Levin | 14503 | Levin Ticket | レビン票 | レビン票 | 音譯 |  | pending |
| Liebre | 14508 | Liebre D Tkt | リエーブレＤ票 | リエーブレＤ票 | 音譯 |  | pending |
| Tangusu | 14547 | Tangusu D Tkt | タングスＤ票 | タングスＤ票 | 音譯 |  | pending |
| FP Transmog | 14548 | FP Transmog Ticket | ＦＰ外装票 | ＦＰ外装票 | 音譯 |  | pending |
| White/Red Hiden EX D | 14549 | White Hiden EX D Tkt | 白／紅秘傳ＥＸＤ票 | 白／紅秘傳ＥＸＤ票 | 音譯 |  | pending |
| Disu | 14574 | Disu D Tkt | ディスＤ票 | ディスＤ票 | 音譯 |  | pending |
| Lils | 14575 | Lils D Tkt | リルスＤ票 | リルスＤ票 | 音譯 |  | pending |
| Dragoon SC/GD | 14576 | Dragoon SC Tkt | ドラゴンＳＣ／ＧＤ票（既有 Dragoon→惡龍） | ドラゴンＳＣ／ＧＤ票 | 音譯 |  | pending |
| Vulcan | 14578 | Vulcan D Tkt | バルカンＤ票 | バルカンＤ票 | 音譯 |  | pending |
| Gaburas Merit | 14600 | Gaburas Merit Tkt | ガブラス功票（官方多作功券） | ガブラス功票 | 音譯 |  | pending |
| Routama | 14638 | Routama D Tkt | ルータマＤ票 | ルータマＤ票 | 音譯 |  | pending |
| Burning/Crimson Cliff | 14643 | Burning Cliff D Tkt | 焔嶽／緋嶽Ｄ票 | 焔嶽／緋嶽Ｄ票 | 音譯 |  | pending |
| Furogada | 14645 | Furogada D Tkt | フロガダＤ票 | フロガダＤ票 | 音譯 |  | pending |
| Lars | 14646 | Lars D Tkt | ラースＤ票 | ラースＤ票 | 音譯 |  | pending |
| Donru | 14647 | Donru D Tkt | ドンルＤ票 | ドンルＤ票 | 音譯 |  | pending |
| Crushing Fog | 14650 | Crushing Fog D Tkt | 砕霧Ｄ票 | 砕霧Ｄ票 | 音譯 |  | pending |
| Valued Word | 14651 | Valued Word D Tkt | 金言Ｄ票 | 金言Ｄ票 | 音譯 |  | pending |
| Noon Glow | 14653 | Noon Glow D Tkt | 午光Ｄ票 | 午光Ｄ票 | 音譯 |  | pending |
| Kosho | 14654 | Kosho D Tkt | コショーＤ票 | コショーＤ票 | 音譯 |  | pending |
| True Shadow | 14655 | True Shadow D Tkt | 真影Ｄ票 | 真影Ｄ票 | 音譯 |  | pending |
| Primitive Fire | 14657 | Primitive Fire Tkt | 原火票 | 原火票 | 音譯 |  | pending |
| EXTELLA | 14659 | EXTELLA Tkt | エクステラ票 | エクステラ票 | 音譯 |  | pending |
| Rose Cat | 14661 | Rose Cat Tkt | 薔薇猫票 | 薔薇猫票 | 音譯 |  | pending |
| Shui | 14662 | Shui Ticket | シュイ票 | シュイ票 | 音譯 |  | pending |
| Ledia | 14664 | Ledia D Tkt | レディアＤ票 | レディアＤ票 | 音譯 |  | pending |
| École | 14668 | ?cole D Tkt | エコールＤ票（原文缺字） | エコールＤ票 | 音譯 |  | pending |
| Guns | 14669 | Guns D Tkt | ガンズＤ票 | ガンズＤ票 | 音譯 |  | pending |
| Agria | 14670 | Agria D Tkt | アグリアＤ票 | アグリアＤ票 | 音譯 |  | pending |
| Fauve | 14671 | Fauve D Tkt | フォーヴＤ票 | フォーヴＤ票 | 音譯 |  | pending |
| Tier | 14672 | Tier D Tkt | ティエールＤ票 | ティエールＤ票 | 音譯 |  | pending |
| Muse | 14673 | Muse D Tkt | ミューズＤ票 | ミューズＤ票 | 音譯 |  | pending |
| Dicto | 14674 | Dicto D Tkt | ディクトＤ票 | ディクトＤ票 | 音譯 |  | pending |
| Kruss | 14675 | Kruss D Tkt | クルスＤ票 | クルスＤ票 | 音譯 |  | pending |
| Starina | 14676 | Starina D Tkt | スタリナＤ票 | スタリナＤ票 | 音譯 |  | pending |
| Mirado | 14678 | Mirado D Tkt | ミラドＤ票 | ミラドＤ票 | 音譯 |  | pending |
| Deyuru | 14679 | Deyuru D Tkt | デユルＤ票 | デユルＤ票 | 音譯 |  | pending |
| Robust | 14680 | Robust D Tkt | ロバストＤ票 | ロバストＤ票 | 音譯 |  | pending |
| Falco | 14681 | Falco D Tkt | ファルコＤ票 | ファルコＤ票 | 音譯 |  | pending |
| Howx | 14682 | Howx D Tkt | ハウクスＤ票 | ハウクスＤ票 | 音譯 |  | pending |
| Pirata | 14683 | Pirata D Tkt | ピラタＤ票 | ピラタＤ票 | 音譯 |  | pending |
| Zeroi | 14684 | Zeroi D Tkt | ゼロイＤ票 | ゼロイＤ票 | 音譯 |  | pending |
| Rail | 14685 | Rail D Tkt | レイルＤ票 | レイルＤ票 | 音譯 |  | pending |
| Ridere | 14686 | Ridere D Tkt | リデーレＤ票 | リデーレＤ票 | 音譯 |  | pending |
| Riot | 14687 | Riot D Tkt | ライオットＤ票 | ライオットＤ票 | 音譯 |  | pending |
| Rutare | 14688 | Rutare D Tkt | ルターレＤ票 | ルターレＤ票 | 音譯 |  | pending |
| Rolling Flow/Sky | 14689 | Rolling Flow D Tkt | 転流／転空Ｄ票 | 転流／転空Ｄ票 | 音譯 |  | pending |
| Cubie | 14691 | Cubie D Tkt | クービーＤ票 | クービーＤ票 | 音譯 |  | pending |
| Kemor | 14692 | Kemor D Tkt | ケモールＤ票 | ケモールＤ票 | 音譯 |  | pending |
| Latria | 14693 | Latria D Tkt | ラトリアＤ票 | ラトリアＤ票 | 音譯 |  | pending |
| Kontao | 14694 | Kontao D Tkt | コンタオＤ票 | コンタオＤ票 | 音譯 |  | pending |
| Ukon | 14695 | Ukon D Tkt | ウコンＤ票 | ウコンＤ票 | 音譯 |  | pending |
| Rotto | 14696 | Rotto D Tkt | ロットＤ票 | ロットＤ票 | 音譯 |  | pending |
| Shoko | 14697 | Shoko D Tkt | ショコＤ票 | ショコＤ票 | 音譯 |  | pending |
| Nimbus | 14698 | Nimbus D Tkt | ニンバスＤ票 | ニンバスＤ票 | 音譯 |  | pending |
| Fonse | 14709 | Fonse D Tkt | フォンスＤ票 | フォンスＤ票 | 音譯 |  | pending |
| Ragri/Zauri PT | 14795 | Ragri PT Tkt | ラグリ／ザウリＰＴ票 | ラグリ／ザウリＰＴ票 | 音譯 |  | pending |
| IM Sorrow | 14797 | IM Sorrow Tkt | ＩＭ哀惜票 | ＩＭ哀惜票 | 音譯 |  | pending |
| Storm FU | 14798 | Storm FU Tkt | ストームＦＵ票 | ストームＦＵ票 | 音譯 |  | pending |
| Sun/Moon Ninja | 14805 | Sun Ninja D Tkt | 陽忍／月忍Ｄ票 | 陽忍／月忍Ｄ票 | 音譯 |  | pending |
| Pilove | 14813 | Pilove Tkt | ピロープ票 | ピロープ票 | 音譯 |  | pending |
| Iora | 14814 | Iora Tkt | イオラ票 | イオラ票 | 音譯 |  | pending |
| S Sol | 14838 | S Sol SP Red Tkt | ソルＳＰ赤票（官方Ｓ・ソル；半翻閘門略Ｓ・） | ソルＳＰ赤票 | 音譯 |  | pending |
| Alfi | 14855 | Alfi Ticket | アルフィ票 | アルフィ票 | 音譯 |  | pending |
| Kaifa | 14891 | Kaifa Ticket | カイファ票 | カイファ票 | 音譯 |  | pending |
| Chiyo | 14897 | Chiyo D Tkt | チヨＤ票 | チヨＤ票 | 音譯 |  | pending |
| Nekodan | 14899 | Nekodan D Tkt | ネコダンＤ票 | ネコダンＤ票 | 音譯 |  | pending |
| Fate AP | 14904 | Fate AP Ⅰ Tkt | フェイトＡＰⅠ票 | フェイトＡＰⅠ票 | 音譯 |  | pending |
| Saint Cat/Flag | 14908 | Saint Cat Tkt | 聖猫／聖旗票 | 聖猫／聖旗票 | 音譯 |  | pending |
| Glittering | 14909 | Glittering Tkt | 煌めき票 | 煌めき票 | 音譯 |  | pending |
| Fantasy GS | 14910 | Fantasy GS Tkt | 幻想大剣票 | 幻想大剣票 | 音譯 |  | pending |
| Twelve Heroes | 14911 | Twelve Heroes Tkt | 十二英雄票 | 十二英雄票 | 音譯 |  | pending |
| Straza | 14913 | Straza Ticket | ストラザ票 | ストラザ票 | 音譯 |  | pending |
| Bonne | 14949 | Bonne D Tkt | ボンネＤ票 | ボンネＤ票 | 音譯 |  | pending |
| WhtTigr * | 14983 | WhtTigrHolySwrdTkt | 白虎・剣聖／双龍／剣王／刀神／天槍／弓鬼票 | 白虎・剣聖／双龍／剣王／刀神／天槍／弓鬼票 | 音譯 |  | pending |
| Jagged | 15014 | Jagged SP Red Tkt | ジャギドＳＰ赤票 | ジャギドＳＰ赤票 | 音譯 |  | pending |
| Gae Bolg | 15023 | Gae Bolg Tkt | ゲイボルグ票 | ゲイボルグ票 | 音譯 |  | pending |
| Saga II | 15027 | Saga II Ticket | サガⅡ票 | サガⅡ票 | 音譯 |  | pending |
| Saine | 15030 | Saine Ticket | サイネ票 | サイネ票 | 音譯 |  | pending |
| Nerihi | 15032 | Nerihi D Tkt | ネリヒＤ票 | ネリヒＤ票 | 音譯 |  | pending |
| Wing | 15062 | Wing Ticket | ウィング票 | ウィング票 | 音譯 |  | pending |
| Pinbi | 15064 | Pinbi Ticket | ピンビ票 | ピンビ票 | 音譯 |  | pending |
| Pribu | 15066 | Pribu Ticket | プリブ票 | プリブ票 | 音譯 |  | pending |
| Melas | 15096 | Melas D Tkt | メラスＤ票 | メラスＤ票 | 音譯 |  | pending |
| Robin Neko | 15097 | Robin Neko Ticket | ロビンネコ票 | ロビンネコ票 | 音譯 |  | pending |
| Dylan | 15113 | Dylan Tkt | ディラン票 | ディラン票 | 音譯 |  | pending |
| Dibble | 15115 | Dibble Tkt | ディブル票 | ディブル票 | 音譯 |  | pending |
| Neriotori | 15117 | Neriotori D Tkt | ネリオトリＤ票 | ネリオトリＤ票 | 音譯 |  | pending |
| Sharuru | 15118 | Sharuru Tkt | シャルル票 | シャルル票 | 音譯 |  | pending |
| G Night PVSP | 15133 | G Night PVSP Tkt | Ｇ夜ＰＶＳＰ票 | Ｇ夜ＰＶＳＰ票 | 音譯 |  | pending |
| Empre | 15134 | Empre SP Red Tkt | エンプレスＳＰ赤票 | エンプレスＳＰ赤票 | 音譯 |  | pending |
| Rango | 15137 | Rango SP Yellow Tkt | ランゴＳＰ黄票 | ランゴＳＰ黄票 | 音譯 |  | pending |
| Death S. | 15140 | Death S. SP White Tkt | デススタＳＰ白票 | デススタＳＰ白票 | 音譯 |  | pending |
| Makluva | 15146 | Makluva SP Green Tkt | マクロアバＳＰ緑票 | マクロアバＳＰ緑票 | 音譯 |  | pending |
| Cure | 15155 | Cure D Tkt | キュアＤ票 | キュアＤ票 | 音譯 |  | pending |
| Jyaga | 15156 | Jyaga D Tkt | ジャガＤ票 | ジャガＤ票 | 音譯 |  | pending |
| SnowWeapn Trial | 15169 | SnowWeapn TrialTkt | 雪武器體驗票 | 雪武器體驗票 | 音譯 |  | pending |
| Mezefest | 15173 | Mezefest Tkt | メゼフェス票 | メゼフェス票 | 音譯 |  | pending |
| Algol | 15176 | Algol D Tkt | アルゴルＤ票 | アルゴルＤ票 | 音譯 |  | pending |
| Katante | 15192 | Katante D Tkt | カタンテＤ票 | カタンテＤ票 | 音譯 |  | pending |
| Ricante | 15193 | Ricante D Tkt | リカンテＤ票 | リカンテＤ票 | 音譯 |  | pending |
| Merente | 15194 | Merente D Tkt | メレンテＤ票 | メレンテＤ票 | 音譯 |  | pending |
| Utante | 15195 | Utante D Tkt | ウタンテＤ票 | ウタンテＤ票 | 音譯 |  | pending |
| Furante | 15196 | Furante D Tkt | フランテＤ票 | フランテＤ票 | 音譯 |  | pending |
| Jess | 15197 | Jess D Tkt | ジェスＤ票 | ジェスＤ票 | 音譯 |  | pending |
| Riaruo | 15198 | Riaruo D Tkt | リアルオＤ票 | リアルオＤ票 | 音譯 |  | pending |
| Reiresu | 15199 | Reiresu D Tkt | レイレスＤ票 | レイレスＤ票 | 音譯 |  | pending |
| Reuasu | 15200 | Reuasu D Tkt | レウアスＤ票 | レウアスＤ票 | 音譯 |  | pending |
| Blanc | 15201 | Blanc D Tkt | ブランＤ票 | ブランＤ票 | 音譯 |  | pending |
| H Shock | 15202 | H Shock D Tkt | Ｈ衝撃Ｄ票（擊缺字→撃） | Ｈ衝撃Ｄ票 | 音譯 |  | pending |
| Shimashima | 15203 | Shimashima D Tkt | シマシマＤ票 | シマシマＤ票 | 音譯 |  | pending |
| Charis | 15207 | Charis Tkt | カリス票 | カリス票 | 音譯 |  | pending |
| Desutora | 15209 | Desutora Tkt | デストラ票 | デストラ票 | 音譯 |  | pending |
| Kashoku | 15211 | Kashoku D Tkt | 華飾Ｄ票 | 華飾Ｄ票 | 音譯 |  | pending |
| Fins | 15220 | Fins Tkt | フィンズ票 | フィンズ票 | 音譯 |  | pending |
| Dins | 15222 | Dins Tkt | ディンズ票 | ディンズ票 | 音譯 |  | pending |
| Lenigan | 15224 | Lenigan Tkt | レニガン票 | レニガン票 | 音譯 |  | pending |
| Kiyoshi | 15229 | Kiyoshi D Tkt | キヨシＤ票 | キヨシＤ票 | 音譯 |  | pending |
| AnivaMemoryGacha | 15230 | AnivaMemoryGachaTkt | アニヴァ記憶抽選票 | アニヴァ記憶抽選票 | 音譯 |  | pending |
| Burukku | 15253 | Burukku D Tkt | ブルックＤ票 | ブルックＤ票 | 音譯 |  | pending |
| Shirukku | 15254 | Shirukku D Tkt | シルクＤ票 | シルクＤ票 | 音譯 |  | pending |
| Gorukku | 15255 | Gorukku D Tkt | ゴルクＤ票 | ゴルクＤ票 | 音譯 |  | pending |
| S Eater | 15282 | S Eater Tkt | ソウルイーター票 | ソウルイーター票 | 音譯 |  | pending |
| Strider | 15283 | Strider Tkt | ストライダー票 | ストライダー票 | 音譯 |  | pending |
| PSO2 | 15285 | PSO2 Ticket | ＰＳＯ２票 | ＰＳＯ２票 | 音譯 |  | pending |
| Ex | 15292 | Ex D Tkt | ＥＸＤ票 | ＥＸＤ票 | 音譯 |  | pending |
| Text | 15298 | Text D Tkt | 原典Ｄ票（對齊 Texto） | 原典Ｄ票 | 音譯 |  | pending |
| Suriito | 15300 | Suriito D Tkt | スリートＤ票 | スリートＤ票 | 音譯 |  | pending |
| Cayssis | 15304 | Cayssis D Tkt | ケイシスＤ票 | ケイシスＤ票 | 音譯 |  | pending |
| Zodic | 15305 | Zodic D Tkt | ゾディックＤ票 | ゾディックＤ票 | 音譯 |  | pending |
| Arge | 15306 | Arge D Tkt | アルジェＤ票 | アルジェＤ票 | 音譯 |  | pending |
| Camarera | 15307 | Camarera D Tkt | カマレラＤ票 | カマレラＤ票 | 音譯 |  | pending |
| Metenera | 15308 | Metenera D Tkt | メテネラＤ票 | メテネラＤ票 | 音譯 |  | pending |
| Abitto | 15309 | Abitto D Tkt | アビットＤ票 | アビットＤ票 | 音譯 |  | pending |
| Riburi | 15310 | Riburi D Tkt | リブリＤ票 | リブリＤ票 | 音譯 |  | pending |
| M?gos | 15311 | M?gos D Tkt | メゴスＤ票（原文缺字） | メゴスＤ票 | 音譯 |  | pending |
| Secuti | 15313 | Secuti D Tkt | セキュティＤ票 | セキュティＤ票 | 音譯 |  | pending |
| Honour | 15314 | Honour D Tkt | 榮譽Ｄ票 | 榮譽Ｄ票 | 音譯 |  | pending |
| Flight | 15315 | Flight D Tkt | 飛翔Ｄ票 | 飛翔Ｄ票 | 音譯 |  | pending |
| Amistad | 15319 | Amistad D Tkt | アミスタＤ票 | アミスタＤ票 | 音譯 |  | pending |
| Perifu | 15320 | Perifu D Tkt | ペリフＤ票 | ペリフＤ票 | 音譯 |  | pending |
| Arma | 15321 | Arma D Tkt | アルマＤ票 | アルマＤ票 | 音譯 |  | pending |
| Randa | 15328 | Randa D Tkt | ランダＤ票 | ランダＤ票 | 音譯 |  | pending |
| Maisto | 15329 | Maisto D Tkt | マイストＤ票 | マイストＤ票 | 音譯 |  | pending |
| Truss | 15330 | Truss D Tkt | トラスＤ票 | トラスＤ票 | 音譯 |  | pending |
| Cultu | 15331 | Cultu D Tkt | カルチュＤ票 | カルチュＤ票 | 音譯 |  | pending |
| Cloth | 15334 | Cloth D Tkt | クロスＤ票 | クロスＤ票 | 音譯 |  | pending |
| Tenpi | 15340 | Tenpi D Tkt | テンピＤ票 | テンピＤ票 | 音譯 |  | pending |
| Reflet | 15341 | Reflet D Tkt | ルフレＤ票 | ルフレＤ票 | 音譯 |  | pending |
| Marin | 15342 | Marin D Tkt | マリンＤ票 | マリンＤ票 | 音譯 |  | pending |
| Vakusu | 15344 | Vakusu D Tkt | ヴァクスＤ票 | ヴァクスＤ票 | 音譯 |  | pending |
| Rizuvue | 15345 | Rizuvue D Tkt | リズヴエＤ票 | リズヴエＤ票 | 音譯 |  | pending |
| Konseru | 15346 | Konseru D Tkt | コンセルＤ票 | コンセルＤ票 | 音譯 |  | pending |
| Shikari | 15347 | Shikari D Tkt | シカリＤ票 | シカリＤ票 | 音譯 |  | pending |
| Strega | 15348 | Strega D Tkt | ストレガＤ票 | ストレガＤ票 | 音譯 |  | pending |
| Eques | 15349 | Eques D Tkt | エクエスＤ票 | エクエスＤ票 | 音譯 |  | pending |
| Uida | 15350 | Uida D Tkt | ウイダＤ票 | ウイダＤ票 | 音譯 |  | pending |
| Kuraaji | 15351 | Kuraaji D Tkt | クラージＤ票 | クラージＤ票 | 音譯 |  | pending |
| Anesis | 15352 | Anesis D Tkt | アネシスＤ票 | アネシスＤ票 | 音譯 |  | pending |
| Zaakaa | 15353 | Zaakaa D Tkt | ザーカＤ票 | ザーカＤ票 | 音譯 |  | pending |
| Vinen | 15354 | Vinen D Tkt | ヴィネンＤ票 | ヴィネンＤ票 | 音譯 |  | pending |
| Rudeos | 15355 | Rudeos D Tkt | ルデオスＤ票 | ルデオスＤ票 | 音譯 |  | pending |
| Breo | 15356 | Breo D Tkt | ブレオＤ票 | ブレオＤ票 | 音譯 |  | pending |
| Rouge | 15357 | Rouge D Tkt | ルージュＤ票 | ルージュＤ票 | 音譯 |  | pending |
| Onero | 15358 | Onero D Tkt | オネロＤ票 | オネロＤ票 | 音譯 |  | pending |
| Diina | 15359 | Diina D Tkt | ディーナＤ票 | ディーナＤ票 | 音譯 |  | pending |
| Oorowa | 15360 | Oorowa D Tkt | オーロワＤ票 | オーロワＤ票 | 音譯 |  | pending |
| Perce | 15362 | Perce D Tkt | パースＤ票 | パースＤ票 | 音譯 |  | pending |
| Orykto | 15363 | Orykto D Tkt | オリクトＤ票 | オリクトＤ票 | 音譯 |  | pending |
| Yoruti | 15364 | Yoruti D Tkt | ヨルティＤ票 | ヨルティＤ票 | 音譯 |  | pending |
| Nisuru | 15365 | Nisuru D Tkt | ニスルＤ票 | ニスルＤ票 | 音譯 |  | pending |
| Maaden | 15366 | Maaden D Tkt | マーデンＤ票 | マーデンＤ票 | 音譯 |  | pending |
| Cheni | 15367 | Cheni D Tkt | チェニＤ票 | チェニＤ票 | 音譯 |  | pending |
| Eguiene | 15368 | Eguiene D Tkt | エギエネＤ票 | エギエネＤ票 | 音譯 |  | pending |
| Torboda | 15369 | Torboda D Tkt | トルボダＤ票 | トルボダＤ票 | 音譯 |  | pending |
| Cavalliba | 15370 | Cavalliba D Tkt | カバリバＤ票 | カバリバＤ票 | 音譯 |  | pending |
| Norukku | 15371 | Norukku D Tkt | ノルクＤ票 | ノルクＤ票 | 音譯 |  | pending |
| Arumyu | 15373 | Arumyu D Tkt | アルミュＤ票 | アルミュＤ票 | 音譯 |  | pending |
| Chatore | 15374 | Chatore D Tkt | チャトレＤ票 | チャトレＤ票 | 音譯 |  | pending |
| Pashio | 15375 | Pashio D Tkt | パシオＤ票 | パシオＤ票 | 音譯 |  | pending |

---

## 使用方式（Agent）

1. 翻譯中遇到無把握專名 → **新增一列** pending，**必須填建議譯＋建議理由**（可先保守暫譯，勿半翻）  
2. 子類宣告 	ranslated 前：確認本表該子類列已齊且建議欄不空  
3. 使用者填「決定」→ status=decided → Fixer 批次回修 → 入 	erms.csv  
