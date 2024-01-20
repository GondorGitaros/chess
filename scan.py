from PIL import Image
import pyautogui

TOP_LEFT_X, TOP_LEFT_Y = 190, 83
BOX = 122
PATH = "D:\\Code\\Git\\Main\\chess\\pieces\\"



def scan():
    white = True
    fen = ""
    replace_colors = [(244, 246, 128), (187, 204, 68), (119, 153, 84), (233, 237, 204)]
    for i in range(8):
        for j in range(8):
            img = pyautogui.screenshot(region=(j * BOX + TOP_LEFT_X, i * BOX + TOP_LEFT_Y, BOX, BOX))
            pixels = img.load() 

            for y in range(img.size[1]): 
                for x in range(img.size[0]): 
                    if pixels[x, y] in replace_colors:
                        pixels[x, y] = (255, 255, 255)
            img_path = 'images/' + str(i+1) + str(j+1) + '.png'
            img.save(img_path)
            
            
            if pyautogui.locate(PATH + "bb.png", img_path, confidence=0.6):
                fen += "b"
            elif pyautogui.locate(PATH + "bp.png", img_path, confidence=0.6):
                fen += "p"
            elif pyautogui.locate(PATH + "bk.png", img_path, confidence=0.6):
                fen += "k"
            elif pyautogui.locate(PATH + "bn.png", img_path, confidence=0.6):
                fen += "n"
            elif pyautogui.locate(PATH + "bq.png", img_path, confidence=0.4):
                fen += "q"
            elif pyautogui.locate(PATH + "br.png", img_path, confidence=0.4):
                fen += "r"
            elif pyautogui.locate(PATH + "wb.png", img_path, confidence=0.4):
                fen += "B"
            elif pyautogui.locate(PATH + "wp.png", img_path, confidence=0.35):
                fen += "P"
            elif pyautogui.locate(PATH + "wk.png", img_path, confidence=0.35):
                fen += "K"
            elif pyautogui.locate(PATH + "wn.png", img_path, confidence=0.35):
                fen += "N"
            elif pyautogui.locate(PATH + "wq.png", img_path, confidence=0.35):
                fen += "Q"
            elif pyautogui.locate(PATH + "wr.png", img_path, confidence=0.35):
                fen += "R"    
            else:
                fen += "1"
        fen += "/"

    # the fen looks like this: 1K1R11N1/PPP1P11P/111111P1/111b1111/11111bB1/11b11111/b111bbbb/Bb1b1b1b/ 
    # we need to remove the 1s (with a better solution than this)
    fen = fen.replace("11111111", "8")
    fen = fen.replace("1111111", "7")
    fen = fen.replace("111111", "6")
    fen = fen.replace("11111", "5")
    fen = fen.replace("1111", "4")
    fen = fen.replace("111", "3")
    fen = fen.replace("11", "2")

    # remove the last slash
    fen = fen[:-1]
    screen = pyautogui.screenshot()
    # save the image
    screen.save("images/fullpic.png")
    img = Image.open("images/fullpic.png")
    rgb = img.getpixel((1364, 121))
    if rgb == (255, 255, 255):
        fen += " w - - 0 1"
    else:
        fen = fen[::-1]
        fen += " b - - 0 1"
        white = False

    # add the rest of the fen
    #######################
    return fen, white
