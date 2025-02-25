import sys
from position import Position
from enums import Piece


def run():
    """簡易なコマンド処理ループ
    'd' と入力すると局面の状態を表示します。
    """
    pos = Position()

    # 動作確認のため、初期盤面にいくつかの駒を配置する例
    pos.board[6][6] = Piece.BlackPawn     # 例：先手の歩を(6,6)に配置
    pos.board[2][2] = Piece.WhitePawn     # 例：後手の歩を(2,2)に配置
    pos.hand_pieces[Piece.BlackSilver.value] = 1  # 例：先手の銀を持ち駒に1枚追加

    print("コマンドを入力してください。（'d' で局面表示、Ctrl+C で終了）")
    try:
        while True:
            line = input("> ").strip()
            if not line:
                continue

            args = line.split()
            command = args[0]

            if command == "d":
                print(pos)
            else:
                print("不明なコマンドです。")
    except KeyboardInterrupt:
        print("\n終了します。")
        sys.exit(0)


if __name__ == '__main__':
    run()
