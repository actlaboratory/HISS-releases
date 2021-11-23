# HISS: High-Speed Synthesizer For NVDA

Version: 1.0.0

[ソフトウェア詳細ページ](https://actlab.org/software/HISS)

## はじめに

HISSは、NVDA用の音声エンジンアドオンです。インストールすることで、DocumentTalkerなどで使われている「ケイコ」と「タカシ」の音声を、NVDAから直接利用できるようになります。

HISSは、株式会社アニモにより提供されている「FineSpeech Version 2」を利用しています。これより新しいバージョンもあるのですが、もっとも動作が軽い「Version 2」を採用しました。

## HISSの特徴

HISSは、SAPI経由ではなく、NVDAの音声エンジンの一つとして動作します。NVDAの読み上げに最適化した設定になっているので、キーを入力してから音声が返ってくるまでの時間が短いです。

NVDAの音声エンジンは、「高速読み上げ」に対応しているものがほとんどです。通常、「高速読み上げ」の設定はチェックボックスで切り替えるようになっていますが、HISSでは、これをスライダーにしています。これにより、細かい速度調整を可能としています。スライダーを最大まで振り切れば、人知を超えた圧倒的な速度を得られます(最大で常用することは想定していません)。

このアドオンを開発した経緯として、コンピュータープログラムを高速で読める音声エンジンがほしかったというのがあります。ということで、プログラミングでよく出てくる用語を、独自の読み辞書に登録してあります。NVDAの読み上げ辞書に入れてもいいのですが、今回はパフォーマンスを優先して、高速に処理できる音声エンジン側に入れています。「HISSならそういう用語を読める」というのを目指しています。

辞書に登録している単語数は、まだまだ少ないです。ご要望を反映して、バージョンアップするごとに単語数を増やしていきたいと考えています。

## 動作環境

HISSを動作させるには、NVDA 2019.3 以降が動作する環境が必要です。
なお、Windowsの言語が日本語以外に設定されていると、正しく動作しない可能性があります。

## シェアウェア登録について

HISSは、シェアウェアとして提供しています。ライセンス料金をお支払いいただくことで、全ての機能を無制限で使えるようになります。

## 利用開始の手順

### 体験版として起動

まだ製品版を購入していない場合、HISSの機能を30分間試せる体験版を利用できます。これは、製品の品質を評価するために使えますが、他の人のコンピューターを短時間だけ緊急で操作するときに使ってもOKです。

体験版を有効にするには、 NVDAメニュー->HISS->体験版を開始 を実行します。この際、インターネット接続が必要です。体験版の開始に成功したら、NVDAの音声設定からHISSを選択して、体験利用を開始できます。

体験版は、NVDAを終了すると、一緒に終わってしまいます。逆に、NVDAを終了させない限りは、音声エンジンを切り替えても状態が残ります。

体験版には、30分の時間制限があります。時間制限を超過すると、音声出力の最初に信号音が流れるようになります。

体験版は、直近180日間で3回まで開始できます。これを数えているのはコンピューター単位なので、違うコンピューターでは、別々にカウントされます。

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

## HISSの設定項目

HISSの設定は、NVDAに搭載されている他の音声エンジンとほとんど同じです。以下に、いくつか注意事項を記載します。

- いくつかの設定項目は、100段階のスライダーではありません。これは、 FineSpeech Version 2 の使用によるものです。
- 「大文字のピッチ変更率」や、「日本語設定」ダイアログ内の「カタカナのピッチ変更率」、「半角のピッチ変更率」には、プラスマイナス25以上の値を指定しないと音程変化が起こりません。
- 「高速読み上げ」の設定は、チェックボックスではなくスライダーです。0(ブーストなし)から、100(6倍速)のあいだで調整できます。せいぜい50ぐらいが実用の範囲だと思います。

## Q&A

### Q: パソコンが壊れたのですが、もう一度購入しなければいけませんか?

HISSのライセンス登録は、直近365日のあいだに3回まで利用できます。ですので、新しいコンピューターでライセンス登録を行っていただければ、再購入の必要はありません。

### Q: 複数のパソコンで製品登録して使ってもいいのでしょうか?

視覚に障害のある方がソフトウェアを非営利で利用し、インストールする全てのコンピュータを専ら購入者自身のみが利用する場合に限り、複数台のコンピュータでの利用を認めています。詳細については、このマニュアルの「ライセンス認証の注意事項」を参照してください。

### Q: 管理者権限がないのですが、HISSを使用できますか?

HISSを使用するに当たって、管理者権限は必要ありません。

### Q: インストールして音声エンジンを選択したのに、読み込めません。どうしたらいいですか?

体験版を開始、または製品登録をした後でないと、HISSを読み込むことはできません。

### Q: 人の名前がアルファベットで書いてあるのを全部スペル読みしてしまうんですが、なんとかなりませんか?

これは、FineSpeechが未知の英単語をスペル読みしてしまう仕様に起因しています。名前の辞書みたいなのを将来的には持たせたいなと思っています。

### Q: 高速読み上げにすると早すぎて聞き取れません。自信がなくなっちゃいます。さすがに早すぎませんか?

高速読み上げは、最もバランスが取れた値を探せるよう、広い範囲で設定できるようにしています。無理に早くする必要はありません。NVDAのsettings ring(簡単音声設定)で調整しながら使うのも有効です。ちなみに、最大にすると、中の人もまったく聞き取れません。

### Q: なんかいきなり音声だけ出なくなったんですけど?

申し訳ありません。おそらくそれはバグです。頻繁に発生する場合には、ACT Laboratoryまでお問い合わせください。なお、ラボ内でテストした限りでは、通常の利用中にこの問題は発生していません。ただ、体験版の時間制限を超過した後、稀に音声が止まることがあるようです。

## その他

このソフトウェアは、株式会社アニモの許諾を受け、同社が提供する音声合成ライブラリ「FineSpeech V.2」を使用して開発しています。なお、「FineSpeech」は富士通株式会社の登録商標です。

このソフトウェアを利用しての感想やご要望、不具合のご報告などは、以下のメールアドレスまたは掲示板へご連絡ください。

* [ACT Laboratory サポート](mailto:support@actlab.org)
* [ACT Laboratory 掲示板](https://actlab.org/bbs/)

## 著作権

JSONの解析には、 picojson 
を使用しています。

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
