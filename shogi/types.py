class Types:
    """
    型変換などのユーティリティクラス
    """
    char_to_piece = [None] * 128
    non_promoted_to_promoted = [None] * Piece.NumPieces.value

    @classmethod
    def initialize(cls):
        # 成り駒の対応付け
        cls.non_promoted_to_promoted[Piece.BlackPawn.value] = Piece.BlackPromotedPawn
        cls.non_promoted_to_promoted[Piece.BlackLance.value] = Piece.BlackPromotedLance
        cls.non_promoted_to_promoted[Piece.BlackKnight.value] = Piece.BlackPromotedKnight
        cls.non_promoted_to_promoted[Piece.BlackSilver.value] = Piece.BlackPromotedSilver
        cls.non_promoted_to_promoted[Piece.BlackBishop.value] = Piece.BlackHorse
        cls.non_promoted_to_promoted[Piece.BlackRook.value] = Piece.BlackDragon
        cls.non_promoted_to_promoted[Piece.WhitePawn.value] = Piece.WhitePromotedPawn
        cls.non_promoted_to_promoted[Piece.WhiteLance.value] = Piece.WhitePromotedLance
        cls.non_promoted_to_promoted[Piece.WhiteKnight.value] = Piece.WhitePromotedKnight
        cls.non_promoted_to_promoted[Piece.WhiteSilver.value] = Piece.WhitePromotedSilver
        cls.non_promoted_to_promoted[Piece.WhiteBishop.value] = Piece.WhiteHorse
        cls.non_promoted_to_promoted[Piece.WhiteRook.value] = Piece.WhiteDragon

        # 文字と駒の対応付け（キーとして文字の ASCII コードを利用）
        cls.char_to_piece[ord('K')] = Piece.BlackKing
        cls.char_to_piece[ord('k')] = Piece.WhiteKing
        cls.char_to_piece[ord('R')] = Piece.BlackRook
        cls.char_to_piece[ord('r')] = Piece.WhiteRook
        cls.char_to_piece[ord('B')] = Piece.BlackBishop
        cls.char_to_piece[ord('b')] = Piece.WhiteBishop
        cls.char_to_piece[ord('G')] = Piece.BlackGold
        cls.char_to_piece[ord('g')] = Piece.WhiteGold
        cls.char_to_piece[ord('S')] = Piece.BlackSilver
        cls.char_to_piece[ord('s')] = Piece.WhiteSilver
        cls.char_to_piece[ord('N')] = Piece.BlackKnight
        cls.char_to_piece[ord('n')] = Piece.WhiteKnight
        cls.char_to_piece[ord('L')] = Piece.BlackLance
        cls.char_to_piece[ord('l')] = Piece.WhiteLance
        cls.char_to_piece[ord('P')] = Piece.BlackPawn
        cls.char_to_piece[ord('p')] = Piece.WhitePawn


def as_promoted(piece: Piece) -> Piece:
    """
    指定された駒のプロモーション済みの駒を返す関数。
    プロモーションが定義されていない場合は AssertionError を発生させる。
    """
    promoted = Types.non_promoted_to_promoted[piece.value]
    assert promoted != Piece.NoPiece, f"Piece {piece} cannot be promoted"
    return promoted
