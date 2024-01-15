import chess.engine

def main():
    engine = chess.engine.SimpleEngine.popen_uci("stockfish/stockfish-windows-x86-64-avx2.exe")

    # That blabla is the FEN of the starting position
    board = chess.Board("3kr3/R7/2R5/8/P2P2P1/2P4P/2r5/6K1 b - - 0 1")

    try:
        result = engine.play(board, chess.engine.Limit(time=2.0))
        board.push(result.move)
        print("The next move is:", result.move)
    except chess.engine.EngineError as e:
        print("EngineError:", e)

    engine.quit()

if __name__ == "__main__":
    main()