import chess.engine
from time import sleep, perf_counter
from pyautogui import click
from scan2 import scan
import pyautogui

boardhm = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8}

def show_next_step(fen):
    engine = chess.engine.SimpleEngine.popen_uci("stockfish/stockfish-windows-x86-64-avx2.exe")

    board = chess.Board(fen)
    for i in range(len(fen)):
        if fen[i] == " ":
            if fen[i+1] == "w":
                break                

    result = engine.play(board, chess.engine.Limit(depth=21))
    board.push(result.move)
    return result.move

    engine.quit()

def main():
    sleep(5)
    while True:
        start = perf_counter()
        screen = pyautogui.screenshot()
        screen.save("cb.png")
        fen, white = scan("cb.png")
        print(fen)
        move = show_next_step(fen)
        print(move)
        move = str(move)

        if white == False:
            scolumn = 8 - boardhm[move[0]] + 1
            srow = int(move[1])
            ecolumn = 8 - boardhm[move[2]] + 1
            erow = int(move[3])
        else:
            srow = 8 - int(move[1]) + 1
            scolumn = boardhm[move[0]]
            erow = 8 - int(move[3]) + 1
            ecolumn = boardhm[move[2]]

        sleep(0.1)
        click(190 + ((scolumn)*121) - 60, 82 + ((srow)*121) - 60)
        sleep(0.1)
        click(190 + ((ecolumn)*121) - 60, 82 + ((erow)*121) - 60)
        sleep(1)
        stop = perf_counter()
        with open("time.txt", "a") as f:
            f.write(str(stop - start) + "\n")

if __name__ == "__main__":
    main()