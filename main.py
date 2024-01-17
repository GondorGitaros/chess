import chess.engine
from functs import click
from time import sleep
import clipboard



def show_next_step(FEN):
    engine = chess.engine.SimpleEngine.popen_uci("stockfish/stockfish-windows-x86-64-avx2.exe")

    # That blabla is the FEN of the starting position
    board = chess.Board(FEN)

    result = engine.play(board, chess.engine.Limit(time=2.0))
    board.push(result.move)
    return result.move

    engine.quit()


def main():
    sleep(3)
    click(1857, 94) # scan
    sleep(3)
    click(1852, 132) # copy fen
    sleep(0.1)
    fen = clipboard.paste()
    print(fen)
    move = show_next_step(fen)
    move_from = move[0] + move[1]
    move_to = move[2] + move[3]


if __name__ == "__main__":
    main()