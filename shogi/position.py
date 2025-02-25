from enums import Color, Piece, to_human_readable_string


class Position:
    BoardSize = 9  # 盤面の一辺のマス数

    def __init__(self):
        # 手番（先手: Black, 後手: White）
        self.side_to_move: Color = Color.Black

        # 盤面：9x9の2次元リスト。全てのマスを Piece.NoPiece で初期化
        self.board = [[Piece.NoPiece for _ in range(Position.BoardSize)]
                      for _ in range(Position.BoardSize)]

        # 持ち駒：各駒の枚数。Piece.NumPiecesは含めず、実際の駒の種類のみ管理
        # Enumは0から始まるのでリストのサイズは len(Piece) - 1 としています。
        self.hand_pieces = [0] * (len(Piece) - 1)

        # 手数
        self.play: int = 0

    def __str__(self) -> str:
        """局面を文字列に変換（独自フォーマット）"""
        lines = []
        horizontal_line = "+----" * Position.BoardSize + "+"

        lines.append(horizontal_line)
        # 盤面の表示：右端から左端に向かって各行を出力
        for rank in range(Position.BoardSize):
            row = "|"
            for file in reversed(range(Position.BoardSize)):
                piece = self.board[file][rank]
                row += to_human_readable_string(piece) + "|"
            lines.append(row)
            lines.append(horizontal_line)

        # 先手の持ち駒（Piece.BlackPawn から WhitePawn 手前まで）
        hand_black = ""
        for piece in list(Piece):
            if piece.value < Piece.WhitePawn.value and piece not in (Piece.NoPiece, Piece.NumPieces):
                hand_black += to_human_readable_string(
                    piece).strip()[0] * self.hand_pieces[piece.value]

        # 後手の持ち駒（Piece.WhitePawn～）
        hand_white = ""
        for piece in list(Piece):
            if Piece.WhitePawn.value <= piece.value < Piece.NumPieces.value:
                hand_white += to_human_readable_string(
                    piece).strip()[0] * self.hand_pieces[piece.value]

        lines.append("先手 持ち駒: " + hand_black + " , 後手 持ち駒: " + hand_white)
        lines.append(
            f"手番 = {'先手' if self.side_to_move.name == 'Black' else '後手'}")
        return "\n".join(lines)
