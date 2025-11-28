# robosys2025-2
- このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布及び使用が許可されます。
- © 2025 Rintatrou Matunaga

- 概要 -
このコマンドは標準入力から読んだ数値に対して四則演算を行うコマンドです。
四則演算に対応しております。

- 実行方法 -
seq 5 | ./calc plus

- 使用例 -
$ seq 5 | ./calc plus
15
$ seq 5 | ./calc minus
-13
$ seq 5 | ./calc times
120
$ seq 5 | ./calc div
0.008333333333333333

- 必要なソフトウェア -
Python(3.7 ~ 3.12:テスト済み)
bashコマンド(テストスクリプトにて必要)

- テスト環境 -
以下の環境にて実行
Ubuntu 22.04.5 LTS
bash

- 手動でのテストについて -
bash -xv ./test.bash　を実行
seq 5 | ./calc plus
seq 5 | ./calc minus
seq 5 | ./calc times
seq 5 | ./calc div
これらのテストを手動で行い、GitHub Actionsと同じ挙動を確認できれば成功となります。

- ライセンス -
SPDX-License-Identifier: BSD-3-Clause 
© 2025 Rintatrou Matunaga
コマンドファイル内にSPDXの記載をしてあります

- 補足事項 -
このプログラムは標準入力を使ったストリーム処理です
このプログラムは自動的に int → float にフォールバックする設計となっています
このプログラムは受けた命令が不正なら usage とともに終了します
