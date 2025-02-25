from enum import Enum, auto


class Color(Enum):
    Black = auto()  # 先手
    White = auto()  # 後手


class Piece(Enum):
    NoPiece = 0                # 駒なし

    # 先手の駒
    BlackPawn = auto()         # 歩
    BlackLance = auto()        # 香
    BlackKnight = auto()       # 桂
    BlackSilver = auto()       # 銀
    BlackGold = auto()         # 金
    BlackBishop = auto()       # 角
    BlackRook = auto()         # 飛
    BlackKing = auto()         # 王

    BlackPromotedPawn = auto()     # と
    BlackPromotedLance = auto()    # 杏
    BlackPromotedKnight = auto()   # 圭
    BlackPromotedSilver = auto()   # 全
    BlackHorse = auto()            # 馬 (角の成り)
    BlackDragon = auto()           # 龍 (飛の成り)

    # 後手の駒
    WhitePawn = auto()         # 歩↓
    WhiteLance = auto()        # 香↓
    WhiteKnight = auto()       # 桂↓
    WhiteSilver = auto()       # 銀↓
    WhiteGold = auto()         # 金↓
    WhiteBishop = auto()       # 角↓
    WhiteRook = auto()         # 飛↓
    WhiteKing = auto()         # 王↓

    WhitePromotedPawn = auto()     # と↓
    WhitePromotedLance = auto()    # 杏↓
    WhitePromotedKnight = auto()   # 圭↓
    WhitePromotedSilver = auto()   # 全↓
    WhiteHorse = auto()            # 馬↓
    WhiteDragon = auto()           # 龍↓

    NumPieces = auto()  # 駒の種類数（末尾に配置）


# 駒を人間が読める文字列に変換するための辞書
PIECE_TO_STRING = {
    Piece.NoPiece:    "　　",
    Piece.BlackPawn:  " 歩 ",
    Piece.BlackLance: " 香 ",
    Piece.BlackKnight: " 桂 ",
    Piece.BlackSilver: " 銀 ",
    Piece.BlackGold:  " 金 ",
    Piece.BlackBishop: " 角 ",
    Piece.BlackRook:  " 飛 ",
    Piece.BlackKing:  " 王 ",
    Piece.BlackPromotedPawn:   " と ",
    Piece.BlackPromotedLance:  " 杏 ",
    Piece.BlackPromotedKnight: " 圭 ",
    Piece.BlackPromotedSilver: " 全 ",
    Piece.BlackHorse:          " 馬 ",
    Piece.BlackDragon:         " 龍 ",
    Piece.WhitePawn:  "歩↓",
    Piece.WhiteLance: "香↓",
    Piece.WhiteKnight: "桂↓",
    Piece.WhiteSilver: "銀↓",
    Piece.WhiteGold:  "金↓",
    Piece.WhiteBishop: "角↓",
    Piece.WhiteRook:  "飛↓",
    Piece.WhiteKing:  "王↓",
    Piece.WhitePromotedPawn:   "と↓",
    Piece.WhitePromotedLance:  "杏↓",
    Piece.WhitePromotedKnight: "圭↓",
    Piece.WhitePromotedSilver: "全↓",
    Piece.WhiteHorse:          "馬↓",
    Piece.WhiteDragon:         "龍↓",
}


def to_human_readable_string(piece: Piece) -> str:
    """駒を人間が読める文字列に変換するヘルパー関数"""
    return PIECE_TO_STRING.get(piece, "??")
