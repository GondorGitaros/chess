import chess.engine
from functs import click
from time import sleep
import clipboard



def show_next_step(fen):
    engine = chess.engine.SimpleEngine.popen_uci("stockfish/stockfish-windows-x86-64-avx2.exe")

    white = False
    # That blabla is the FEN of the starting position
    board = chess.Board(fen)
    for i in range(len(fen)):
        if fen[i] == " ":
            if fen[i+1] == "w":
                white = True
                break                

    result = engine.play(board, chess.engine.Limit(time=2.0))
    board.push(result.move)
    return result.move, white

    engine.quit()


def main():
    sleep(3)
    click(1857, 94) # scan
    sleep(3)
    click(1852, 132) # copy fen
    sleep(0.1)
    fen = clipboard.paste()
    print(fen)
    move, white = show_next_step(fen)
    print(move, white)
    # r2q1rk1/ppp2ppp/5n2/4p3/1b2P3/1P4N1/PP3PPP/R1BQ1K1R b - - 0 1


if __name__ == "__main__":
    main()