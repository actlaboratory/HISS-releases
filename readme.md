# HISS: High-Speed Synthesizer For NVDA

[ソフトウェア詳細ページ](https://actlab.org/software/HISS)

## はじめに

HISSは、NVDA用の音声エンジンアドオンです。インストールすることで、DocumentTalkerなどで使われている「ケイコ」と「タカシ」の音声を、NVDAから直接利用できるようになります。

HISSは、株式会社アニモにより提供されている「FineSpeech Version 2」を利用しています。これより新しいバージョンもあるのですが、もっとも動作が軽い「Version 2」を採用しました。

## HISSの特徴

HISSは、SAPI経由ではなく、NVDAの音声エンジンの一つとして動作します。NVDAの読み上げに最適化した設定になっているので、キーを入力してから音声が返ってくるまでの時間が短いです。ver1.1.0から、拡張機能として、SAPI5のインターフェイス経由でHISSを利用できるようになりました。

HISSは、ASIOデバイスを直接サポートしています。ASIOプロトコルに対応したオーディオインターフェイスをお持ちの場合は、そのデバイスに直接音声を出力することにより、音声が返ってくるまでの時間をさらに短縮することができます。

NVDAの音声エンジンは、「高速読み上げ」に対応しているものがほとんどです。通常、「高速読み上げ」の設定はチェックボックスで切り替えるようになっていますが、HISSでは、これをスライダーにしています。これにより、細かい速度調整を可能としています。スライダーを最大まで振り切れば、人知を超えた圧倒的な速度を得られます(最大で常用することは想定していません)。

このアドオンを開発した経緯として、コンピュータープログラムを高速で読める音声エンジンがほしかったというのがあります。ということで、プログラミングでよく出てくる用語を、独自の読み辞書に登録してあります。NVDAの読み上げ辞書に入れてもいいのですが、今回はパフォーマンスを優先して、高速に処理できる音声エンジン側に入れています。「HISSならそういう用語を読める」というのを目指しています。

辞書に登録している単語数は、まだまだ少ないです。ご要望を反映して、バージョンアップするごとに単語数を増やしていきたいと考えています。

## 動作環境

HISSを動作させるには、NVDA 2019.3 以降が動作する環境が必要です。
なお、Windowsの言語が日本語以外に設定されていると、正しく動作しない可能性があります。

## シェアウェア登録について

HISSは、シェアウェアとして提供しています。ライセンス料金をお支払いいただくことで、全ての機能を無制限で使えるようになります。

## 利用開始の手順

### インストール

ダウンロードしたファイルを展開すると、拡張子が「nvda-addon」のファイルがあります。
HISSをインストールするには、NVDAが起動している状態でこのファイルを実行します。

また、 NVDAメニュー->ツール->アドオン マネージャー を使ってインストールすることもできます。
詳細については、NVDAのユーザーガイドを参照してください。

### 体験版として起動

まだ製品版を購入していない場合、HISSの機能を30分間試せる体験版を利用できます。これは、製品の品質を評価するために使えますが、他の人のコンピューターを短時間だけ緊急で操作するときに使ってもOKです。

体験版を有効にするには、 NVDAメニュー->HISS->体験版を開始 を実行します。この際、インターネット接続が必要です。体験版の開始に成功したら、NVDAの音声設定からHISSを選択して、体験利用を開始できます。

体験版は、NVDAを終了すると、一緒に終わってしまいます。逆に、NVDAを終了させない限りは、音声エンジンを切り替えても状態が残ります。

体験版には、30分の時間制限があります。時間制限を超過すると、音声出力の最初に信号音が流れるようになります。

体験版は、直近180日間で3回まで開始できます。これを数えているのはコンピューター単位なので、違うコンピューターでは、別々にカウントされます。

ASIO出力機能を体験版でテストする場合は、ASIOの設定をしてから体験版を開始することをお勧めします。NVDAの再起動によって体験版の使用回数を減らさないようにするためです。もし、順番を逆にしてしまった場合は、別の音声エンジンに切り替えた後にHISSに戻すことで、ASIO出力の状態でHISSを利用できます。

### 製品版を登録

製品版ライセンスを購入した場合は、ライセンス登録を行うことで、利用を開始できます。

2種類の方法で製品登録を行えます。詳細は、次の章を参照してください。

製品登録が完了したら、NVDAの音声設定から、HISSを選択して利用できるようになります。

## 製品登録

製品登録を行うコンピューターがインターネットにつながっている場合は、オンライン登録が便利です。

製品登録を行うコンピューターがインターネットに接続できない場合は、オフライン登録を利用して、他のコンピューターから登録を実行可能です。

### オンライン登録

NVDAメニュー->HISS->オンライン登録 を実行します。購入時に発行されたシリアル番号を入力して、OKボタンを押します。これで完了です。

### オフライン登録

インターネットにつながっている他のコンピューターで、代わりにライセンス登録を行い、必要なファイルを取得できます。これにはいくつかステップがあります。

1. HISSを使いたいコンピューターで、 NVDAメニュー->HISS->オフライン登録->登録情報を取得 を実行します。
2. 必要な情報がクリップボードにコピーされるので、これをUSBメモリーなどに保存します。
3. インターネットに接続されている別のコンピューターやスマートフォンで、 [https://actlab.org/store/manual_authorization](https://actlab.org/store/manual_authorization) にアクセスします。
4. 購入時に発行されたシリアルキーと、先ほど取得したオフライン登録コードを入力して、認証ボタンを押します。
5. ライセンスファイルがダウンロードされるので、HISSを使いたいコンピューターにそのファイルを転送します。
6. HISSを使いたいコンピューターで、 NVDAメニュー->HISS->オフライン登録->ライセンスファイルを登録 を実行します。
7. 転送したライセンスファイルを選択して読み込みます。これで完了です。

### ライセンス認証の注意事項

ライセンス認証の条件や制限事項については、以下の公式ページを参照してください。

[https://actlab.org/disclose/store_info](https://actlab.org/disclose/store_info)

## 自動更新について

HISSは、プログラムの更新があるかどうかを自動で確認して、更新可能なときにメッセージを表示します。画面の指示に従って操作すれば、そのままアップデートが可能です。

自動的なアップデート確認を無効にしたい場合は、「NVDAメニュー->HISS->起動時のアップデートチェックを無効化」を実行してください。これを実行した後は、「起動時のアップデートチェックを無効化」の項目は「起動時のアップデートチェックを有効化」という名前に変わり、実行することで、再び自動的なアップデート確認を再開させることができます。

任意のタイミングで更新を確認したい場合は、「NVDAメニュー->HISS->アップデートを確認」を実行してください。

## HISSの設定項目

### 他の音声エンジンと共通の設定項目

HISSの設定は、NVDAに搭載されている他の音声エンジンとほとんど同じです。以下に、いくつか注意事項を記載します。

- いくつかの設定項目は、100段階のスライダーではありません。これは、 FineSpeech Version 2 の使用によるものです。
- 「大文字のピッチ変更率」や、「日本語設定」ダイアログ内の「カタカナのピッチ変更率」、「半角のピッチ変更率」には、プラスマイナス25以上の値を指定しないと音程変化が起こりません。
- 「高速読み上げ」の設定は、チェックボックスではなくスライダーです。0(ブーストなし)から、100(6倍速)のあいだで調整できます。せいぜい50ぐらいが実用の範囲だと思います。

### 独自の設定項目

HISSには、独自の設定項目がいくつかあります。以下にその詳細を記載します。

- 単語の間で息継ぎをする: スペース区切りの単語があるとき、繋げて読むか、空白を空けながら読むかを切り替えられます。
- 息継ぎの長さ: 息継ぎをするとき、どれぐらい長い空白を空けるかを指定できます。
- 不明な単語に推測読みを適用: オンにすると、推測読みを有効にします。HISSとしては読み方を知らないが、明らかに日本語の発音に治せそうな単語を見つけると、独自の推測読みエンジンで読み方を推測します。たとえば、"tanaka"という単語は、推測読みを有効にしていれば「タナカ」と読まれますが、有効にしていなければ"ティーエーエヌエーケーエー"と読まれます。逆にへんな読み方になってしまう場合もあるので、切り替えられるようにしています。
- 高域を強調: 音声の広域成分を強調して、より刺さる感じの音声になります。スピーカーの性質によって標準の音声が聞き取りにくい場合には、使ってみてください。通常はオンにしなくてもよいと思います。

## ASIO出力の利用

ASIOプロトコルに対応したオーディオインターフェイスがあれば、HISSの音声を直接ASIOで出力することができます。これにより、Windowsのシステムミキサーを経由しなくなるので、超低遅延の音声出力が可能になります。

ASIO出力を設定するには、「NVDAメニュー -> HISS -> ASIOの設定」を実行します。この画面で、利用可能なASIOデバイスを選択してOKボタンを押すと、ASIO出力に切り替えることができます。この設定は保存され、次回以降の起動でも、設定したASIOデバイスに音声出力します。

ASIOの設定を適用するには、NVDAを再起動するか、HISSの音声エンジンを読み込み直す必要があります。

ASIO出力機能を体験版でテストする場合は、ASIOの設定をしてから体験版を開始することをお勧めします。NVDAの再起動によって体験版の使用回数を減らさないようにするためです。もし、順番を逆にしてしまった場合は、別の音声エンジンに切り替えた後にHISSに戻すことで、ASIO出力の状態でHISSを利用できます。

ASIO出力に切り替えると、音声読み上げの音質が若干変化します。これは、HISSが元々出力している音声フォーマットをそのままASIOに流すことができず、変換を挟んでいるからです。そして、その変換アルゴリズムは、速度優先で、最も簡易的な方法を使っています。

ASIO対応デバイスは、1つのアプリケーションからしか同時に利用できないという制限があります。そのため、HISSをASIO出力にしているときに、音楽作成ソフトのようなASIO対応アプリケーションを起動すると、エラーが発生することがあります。逆の順番でも同様です。

ASIO出力中にASIOの設定画面を開くと、現在使っているデバイスは一覧に表示されません。これも、ASIOの排他制御による仕様です。

今のところ、作者の手元にある Yamaha AG06 というインターフェイスでしかテストできていません。たぶん、ほかのデバイスでも動くとは思います。

ASIO出力機能は、HISSがNVDAの上で動作しているときのみ利用できます。SAPI拡張機能では利用できません。

## SAPI拡張機能の利用

HISSの音声エンジンを、SAPI5経由で利用することができます。これにより、SAPI5音声出力に対応した外部アプリケーションから、HISSを利用できるようになります。なお、SAPI拡張機能をインストールする際に、管理者権限が必要となります。

SAPI拡張機能を利用するには、「NVDAメニュー->HISS->SAPI拡張機能を実行」を開きます。SAPI拡張機能は、アドオン本体のファイルサイズを削減するために、必要に応じてインターネット上からダウンロードされます。

SAPI拡張機能は、それ自体が単体のプログラムとして実行されます。詳細な設定方法・利用方法については、SAPI拡張機能が起動した画面で「ヘルプ」ボタンを押すと確認できます。

SAPI拡張機能のインストールプログラムが、Windows Defenderなどのウィルス対策ソフトによってマルウェアと判定されてしまう場合があります。その場合、初回の実行でダウンロードしようとした時点で全力で消しに来るような挙動をします。検疫されたファイルの復元・実行許可を与える必要があるかもしれません。

## 更新履歴

### 2024/01/08 Version 1.3.2

1. NVDA 2024.1 に対応しました。
2. ユーザー提供を含む辞書データを追加しました。現在、2319単語。
3. SAPI拡張機能の PyInstaller バージョンを 6.3.0 に更新しました。

### 2023/10/09 Version 1.3.1

1. オンライン登録を実行しようとするとエラーになってしまう不具合を修正しました。

### 2023/10/09 Version 1.3.0

1. ASIOデバイスへの出力機能を搭載しました。
2. ユーザー提供を含む辞書データを追加しました。現在、2311単語。

### 2023/06/01 Version 1.2.5

1. ユーザー提供を含む辞書データを追加しました。現在、2307単語。

### 2023/02/16 Version 1.2.4

1. 推測読みエンジンで、 zya / zyu / zye / zyo を正しく読めるようにしました。
2. 「単語の間で息継ぎをする」の機能が半角スペースだけに対して機能していましたが、全角スペースでも息継ぎが行われるように変更しました。
3. ユーザー提供を含む辞書データを追加しました。現在、2266単語。
4. NVDA jpalpha_230211u (2023.1.0.1969) で動作確認ができたため、試験的に LastTestedNVDAVersion の値を 2023.1 に変更しました。音声エンジン回りのbreaking changeがここから出てくることはないと思いますので、先に上げてしまいます。

### 2022/11/18 Version 1.2.3

1. 推測読みエンジンをすこし調整しました。
2. ユーザー提供を含む辞書データを追加しました。現在、2210単語。

### 2022/10/11 Version 1.2.2

1. 特定の長さのBreakCommandを受け取った時、ノイズが発生することがあった不具合を修正しました。これまで確実に起きていたのは、MathPlayerで「2の3乗」のような数式を読んだときです。

### 2022/09/26 Version 1.2.1

1. 推測読みで読める単語を増やしました。
2. ユーザー提供を含む辞書データを追加しました。現在、2154単語。
3. SAPI拡張を上書きインストールするとき、以前までの設定が消えてしまっていた不具合を修正しました。

### 2022/08/04 Version 1.2.0

1. NVDA 2022.3 で導入予定の BreakCommand に対応しました。音声発声の間に待ち時間を入れるコマンドだそうです。
2. ユーザー提供を含む辞書データを追加しました。現在、2015単語。

### 2022/07/31 Version 1.1.5

1. 内部的な不具合を修正しました。音声発声終了時のイベント(synthDoneSpeaking)が正しく通知できていなかったため、一部のアドオンと組み合わせる際に問題を引き起こしていました。
2. 「initializes」を「イニシャライザーズ」と読んでいたのを修正しました。
3. 「yamada」と「yamashita」を推測読みできていなかったので、英単語リストを調整しました。
4. [HISSの辞書データがオープンソースになりました](https://github.com/actlaboratory/HISS-dictionary) 。
5. ユーザー提供を含む辞書データを追加しました。現在、1980単語。

### 2022/06/21 Version 1.1.4

1. 音声エンジンの読み込み失敗時、および起動時のアップデートチェックの設定変更時、ダイアログボックスによる通知が行われていなかった不具合を修正しました。
2. ユーザー提供を含む辞書データを追加しました。現在、1910単語。

### 2022/05/15 Version 1.1.3

1. 推測読みの精度を改善しました。前バージョンの変更で「ohayou」をへんに読むようになってしまったりしたので、その辺りを修正しました。
2. ユーザー提供を含む辞書データを追加しました。現在、1726単語。

### 2022/04/18 Version 1.1.2

1. 推測読みの精度を改善しました。具体的には、 ohta さんをオータさんと読めるようになったり、 qubo をクーボと読めるようになったりです。
2. アドオンをインストールした直後のNVDA再起動の途中で、NVDAがフリーズすることがあった(らしい)不具合を修正しました。
3. ダイアログボックスの表示方法として、NVDAのAPI的に非推奨の方法を使っていたので、推奨される方法に変えました。ユーザー的には、なにも変化はありません。
4. 推測読みで使っているワードリストが、一部大文字で始まっているものがあったために誤動作していたのを修正しました。人名を推測読みから外してほしいのに、へんに推測読みされたりしていました。
5. ユーザー提供を含む辞書データを追加しました。現在、1481単語。

### 2022/03/26 Version 1.1.1

1. NVDAControllerClient の日本語版拡張に存在する NVDAController_isSpeaking に正しい状態を返せるようにしました。これで、NVDAの音声発声終了を判定しているアプリケーションでの動作が改善するはずです。
2. 推測読みするかどうかの条件判定時、m を含む単語の処理がバグっていたのを修正しました。具体的には、 summarize とかを推測読みしないようにしていたはずが、バグが原因で推測読みされてスンマリゼになっていました。
3. 全角アルファベットにも推測読みが働くようにしました。
4. SAPIの設定で、SSMLで指定された設定値を合算した結果、SAPIとして対応している最大値/最長値を超えた場合に、値を丸め込むようにしました。JAWSで使うときに読み上げ速度が変になるのが改善されるはずです。
5. PC-TalkerでSAPI拡張を使っているときに絵文字だけがある行を読ませると、クラッシュしてPC-Talkerごとお亡くなりになってしまう不具合を修正しました。
6. ユーザー提供を含む辞書データを追加しました。現在、1137単語。

### 2022/02/23 Version 1.1.0

1. SAPI拡張機能に対応しました。
2. 推測読みするかどうかの設定を、簡単音声設定(settings ring)から切り替えられるようにしました。
3. 推測読みで、"tz"を"ツ"、"di"を"ディ"と読めるようにしました。
4. HISSのプログラムの更新を自動で確認していましたが、そのオンオフを設定で変えられるようにしました。
5. 手動で更新をチェックするメニューを追加しました。
6. 更新確認のコードをちょっとリファクタしました。
7. ユーザー提供を含む辞書データを追加しました。現在、814単語。

### 2022/01/16 Version 1.0.2

1. 広域強調の設定を切り替えられるようにしました。
2. 辞書データを更新しました。現在、513単語。
3. LastTestedNVDAVersionの値を2022.4にしました。
4. hiss.dllのコンパイラオプションで C++ 17 を有効にしました。たぶん大丈夫ですが、ランタイム関連で動かなくなるかもしれないので、そうなったら考えます。ランタイムのリンクを配るぐらいですが。

### 2022/01/10 Version 1.0.1

1. プラグインの再読み込みを実行すると、HISSのメニューが無限に増殖する不具合を修正しました。
2. HISSを読み込むときに、NVDAのログビューワーにdeprecation warningが出ていたのを修正しました。
3. アップデートチェックのレスポンスをNVDAのログビューワーに出力していた不具合を修正しました。
4. "123 456" を読ませると "123456" として読まれていた不具合を修正しました。
5. 英単語の間にポーズを入れるかどうかを制御できるオプションを追加しました。
6. ポーズの長さを調整できるオプションを追加しました。
7. 推測読み機能を追加しました。
8. HISSの音声エンジンを読み込めなかったときに、メッセージボックスを出して理由を表示するようにしました。
9. このファイルにインストール方法の説明を追記しました。
10. 文字コード変換の際にデフォルトコードページを参照していたのを、CP932に決め打ちするように変更しました。確認していませんが、これでsystem localeが違う環境でも動くんじゃないかな...
11. 独自辞書を更新しました。現在、500単語。

## Q&A

### Q: パソコンが壊れたのですが、もう一度購入しなければいけませんか?

HISSのライセンス登録は、直近365日のあいだに3回まで利用できます。ですので、新しいコンピューターでライセンス登録を行っていただければ、再購入の必要はありません。

### Q: 複数のパソコンで製品登録して使ってもいいのでしょうか?

視覚に障害のある方がソフトウェアを非営利で利用し、インストールする全てのコンピュータを専ら購入者自身のみが利用する場合に限り、複数台のコンピュータでの利用を認めています。詳細については、このマニュアルの「ライセンス認証の注意事項」を参照してください。

### Q: 管理者権限がないのですが、HISSを使用できますか?

HISSを使用するに当たって、管理者権限は必要ありません。正し、SAPI拡張機能を利用する場合に限り、特別に管理者権限を必要とします。

### Q: インストールして音声エンジンを選択したのに、読み込めません。どうしたらいいですか?

体験版を開始、または製品登録をした後でないと、HISSを読み込むことはできません。

### Q: 人の名前がアルファベットで書いてあるのを全部スペル読みしてしまうんですが、なんとかなりませんか?

設定で、「不明な単語に推測読みを適用」をオンにしてみてください。

### Q: 推測読みが適用される条件を教えてください。

最初に、HISSは、文章中に含まれる英単語を全て抽出します。これは、アルファベット([a-zA-Z])が3つ以上連続していることを条件にしています。

次に、抽出した各単語に対して、推測読みを適用するかどうかを判断します。これには、英単語セットというものを使っています。英単語セットは、HISSのアドオンがインストールされているディレクトリの中の"dictionary\english.dic"が実態です。この中に入っている単語は推測読みを適用しません。複合語も判定しているので、たとえば"timeline"は"time"と"line"が英単語セットに入っているので推測読みされません。また、actlabの独自読み上げ辞書に登録されている英単語も、推測読みの対象になりません(english.dicにはありませんが、HISS起動時に英単語セットの一部として読み込まれています)。

ここまでのチェックで推測読みをするという判定になると、実際に読み方を推測し始めます。最後まで推測できれば、その英単語の読み方を上書きします。途中でカタカナに治せないアルファベットの並びが出てきたら、その時点で推測を中断して、推測読みを適用しないままFineSpeechに任せます。FineSpeechのほうがうまく読めるという場合もあるので、推測読みでは、あまり無理なカタカナ変換はしないように設計してあります。

### Q: 高速読み上げにすると早すぎて聞き取れません。自信がなくなっちゃいます。さすがに早すぎませんか?

高速読み上げは、最もバランスが取れた値を探せるよう、広い範囲で設定できるようにしています。無理に早くする必要はありません。NVDAのsettings ring(簡単音声設定)で調整しながら使うのも有効です。ちなみに、最大にすると、中の人もまったく聞き取れません。

### Q: なんかいきなり音声だけ出なくなったんですけど?

申し訳ありません。おそらくそれはバグです。頻繁に発生する場合には、ACT Laboratoryまでお問い合わせください。なお、ラボ内でテストした限りでは、通常の利用中にこの問題は発生していません。ただ、体験版の時間制限を超過した後、稀に音声が止まることがあるようです。

### Q: SAPI拡張機能を実行したら、なんかウィルスが見つかりましたとか言われたんですけど、なにかされたんですか？オタクのソフトは本当に大丈夫なんですか？

お手数をおかけします。SAPI拡張機能のプログラム自体は、お使いのコンピュータに対して悪意のある動作をすることはありません。

マルウェアと判定されてしまうのは、設定プログラムを作るためにPyInstallerを使っているせいです。別のツールでexeにすることを試してみたのですが、なかなかPyInstaller以外でうまく動かせず、今のようになっています。ACT Laboratoryのソフトは共通してこの問題を抱えており、なんとかできるならしたいとは思っています。

## その他

このソフトウェアは、[株式会社アニモ](https://www.animo.co.jp/)の許諾を受け、同社が提供する音声合成ライブラリ「FineSpeech V.2」を使用して開発しています。なお、「FineSpeech」は富士通株式会社の登録商標です。

このソフトウェアを利用しての感想やご要望、不具合のご報告などは、以下のメールアドレスまたは掲示板へご連絡ください。

* [ACT Laboratory サポート](mailto:support@actlab.org)
* [ACT Laboratory 掲示板](https://actlab.org/bbs/)

## 著作権

英単語セットの元データには、以下の辞書を使わせていただきました。

[https://kujirahand.com/web-tools/EJDictFreeDL.php](https://kujirahand.com/web-tools/EJDictFreeDL.php)

JSONの解析には、 picojson を使用しています。

Copyright 2009-2010 Cybozu Labs, Inc.

Copyright 2011-2014 Kazuho Oku

All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice,
   this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.

ASIO出力部分には、 [PyAudio](https://people.csail.mit.edu/hubert/pyaudio/) を使用しています。

Copyright (c) 2006 Hubert Pham

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

- The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
- THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
