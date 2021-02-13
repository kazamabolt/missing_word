import pygame
import random

pygame.init()
gameDisplay = pygame.display.set_mode([800, 600])
pygame.display.set_caption("JACKPOT")
bgimg = pygame.image.load("backframe.jpg")
bgimg = pygame.transform.scale(bgimg, (800, 600)).convert_alpha()

clock = pygame.time.Clock()
FPS = 15

white = (255, 255, 255)
black = (0, 0, 0)
red = (200, 0, 0)
green = (0, 150, 0)
blue = (40, 53, 88)
yellow = (255, 255, 0)
light_green = (0, 100, 0)
light_yellow = (200, 200, 0)
light_red = (150, 0, 0)

wordFrame = pygame.image.load("backframe.jpg")
scoreButton = pygame.image.load("score.png")
levelButton = pygame.image.load("level.png")
heart = pygame.image.load("heart.jpg")
inputText = pygame.image.load("input.png")
percent = pygame.image.load("percents.png")
icon = pygame.image.load("icon.png")

wordGuessFont = pygame.font.SysFont("CopperPlate Gothic", 50)
wordType = pygame.font.SysFont("Calibri", 50)
scoreFont = pygame.font.SysFont("Comic Sans MS", 25)
hintFont = pygame.font.SysFont("Comic Sans MS", 25)
helpFont = pygame.font.SysFont("Comic Sans MS", 25)
ratioFont = pygame.font.SysFont("CopperPlate Gothic", 25)
msgFont = pygame.font.SysFont("CopperPlate Gothic", 25)
answerFont = pygame.font.SysFont("Juice ITC", 50)

pygame.display.set_icon(icon)

lst1 = ["apple", "banana", "guava", "watermelon", "grape", "mango", "lichi", "strawberry", "pear", "kiwi"]
lst2 = ["rose", "jasmine", "lavender", "daisy", "lily", "sunflower", "lotus"]
lst3 = ["buffalo", "tiger", "giraffe", "elephant", "kangaroo", "chimpanzee", "squirrel"]
lst4 = ["bat", "cock", "eagle", "ostrich", "sparrow", "vulture", "dove", "peacock", "pigeon", "swan"]
lst5 = ["butterfly", "centipede", "grasshopper", "honeybee", "wasp", "earthworm", "spider", "leech", "locust", "mosquito" ]
lst6 = ["sanskrit", "english", "hindi", "mathematics", "chemistry", "physics", "astronomy", "economics", "history", "botany" ]
lst7 = ["cricket", "football", "hockey", "baseball", "basketball", "chess", "boxing", "wrestling", "tennis" ]
lst8 = ["paper", "pencil", "compass", "crayon", "divider", "eraser", "register", "tape", "ruler", "slate", "glue", "sheet"]
lst9 = ["cinnamon", "menthol", "saffron", "cuminseed", "pepper", "cardamon", "raisin", "cashew", "chestnut", "almond","date"]
lst10 = ["cookie", "pizza", "briyani", "puri", "mayonnaise", "pongal", "idly", "dosa", "parrota", "omelet","rice", "friedrice"]
lst11 = ["brinjal", "coriander", "cauliflower", "cucumber", "ginger", "ladyfinger", "mushroom", "pumpkin", "spinach", "turnip", "tamarind", "onion", "radish", "carrot", "cabbage", "garlic"]
lst12 = ["cheese", "biscuit", "butter", "flour", "sugar", "loaf", "bread", "cake", "cream", "yeast", "milk", "honey"]
lst13 = ["sickle", "hammer", "axe", "lance", "sword", "blade", "waterpot", "spear", "screwdriver", "spade", "chisel"]
lst14 = ["green", "yellow", "indigo", "saffron", "purple", "maroon", "golden", "blue", "pale", "white"]
lst15 = ["anklet", "bracelet", "necklace", "earring", "locket", "chain", "silver", "diamond", "aquamarine", "platinum", "pearl"]
lst16 = ["library", "university", "temple", "orphanage", "museum", "factory", "church", "theatre", "foundation", "terrace", "kitchen", "bathroom", "basement"]
lst17 = ["tamilnadu", "delhi", "bihar", "kerala", "karnataka", "goa", "rajasthan", "maharashtra", "telangana", "punjab"]
lst18 = ["mainframe", "super", "personal", "macintosh", "laptop", "tablet", "smartphone", "workstation"]
lst19 = ["hardware", "software", "liveware", "keyboard", "mouse", "monitor", "scanner", "printer", "charger","speaker"]
lst20 = ["facebook", "youtube", "wechat", "twitter", "instagram", "weibo", "qzone", "Telegram"]
lst21 = ["brinjal", "coriander", "cauliflower", "cucumber", "ginger", "ladyfinger", "mushroom", "pumpkin", "spinach", "turnip", "tamarind"]
lst22 = ["cricket", "football", "hockey", "baseball", "basketball", "chess", "boxing", "wrestling", "tennis"]
lst23 = ["cinnamon", "menthol", "saffron", "cuminseed", "pepper", "cardamon", "raisin", "cashew", "chestnut", "almond","date"]
lst24 = ["sickle", "hammer", "axe", "lance", "sword", "blade", "waterpot", "spear", "screwdriver", "spade", "chisel"]
lst25 = ["paper", "pencil", "compass", "crayon", "divider", "eraser", "register", "tape", "ruler", "slate", "glue", "sheet"]
lst26 = ["anklet", "bracelet", "necklace", "earring", "locket", "chain", "silver", "diamond", "aquamarine", "platinum", "pearl"]


global level_1_list
global level_2_list
global level_3_list
global level_4_list
global level_5_list
global level_6_list
global level_7_list
global level_8_list
global level_9_list
global level_10_list

level_1_list = lst1 + lst2
level_2_list = lst3 + lst4
level_3_list = lst5 + lst6 + lst7
level_4_list = lst8 + lst9 + lst10
level_5_list = lst11 + lst12 + lst13
level_6_list = lst14 + lst15 + lst16
level_7_list = lst17 + lst18 + lst19
level_8_list = lst20 + lst21 + lst22
level_9_list = lst23 + lst24 + lst25
level_10_list = lst26 + lst16 + lst10

def chooseWord(level, randomWords):
    while True:
        if level == 1:
            word = random.choice(level_1_list)
            if word in lst1:
                hint = "Fruit"
            elif word in lst2:
                hint = "Flower"

        elif level == 2:
            word = random.choice(level_2_list)
            if word in lst3:
                hint = "Animal"
            elif word in lst4:
                hint = "Bird"


        elif level == 3:
            word = random.choice(level_3_list)
            if word in lst5:
                hint = "Insect"
            elif word in lst6:
                hint = "Subject"
            elif word in lst7:
                hint = "Sport"


        elif level == 4:
            word = random.choice(level_4_list)
            if word in lst8:
                hint = "Stationary"
            elif word in lst9:
                hint = "Spice or Dry Fruit"
            elif word in lst10:
                hint = "Food Item"


        elif level == 5:
            word = random.choice(level_5_list)
            if word in lst11:
                hint = "Vegetable"
            elif word in lst12:
                hint = "Dairy Product"
            elif word in lst13:
                hint = "Weapon or Tool"


        elif level == 6:
            word = random.choice(level_6_list)

            if word in lst14:
                hint = "Colour"
            elif word in lst15:
                hint = "Body Accessory or a Gem"
            elif word in lst16:
                hint = "A type of a building or a part of a building"

        elif level == 7:
            word = random.choice(level_7_list)

            if word in lst17:
                hint = "states"
            elif word in lst18:
                hint = "Types of Computer"
            elif word in lst19:
                hint = "Parts of Computer"

        elif level == 8:
            word = random.choice(level_8_list)

            if word in lst20:
                hint = "Social media"
            elif word in lst21:
                hint = "vegetables"
            elif word in lst22:
                hint = "Games"

        elif level == 9:
            word = random.choice(level_9_list)

            if word in lst23:
                hint = "Spice or Dry fruit"
            elif word in lst24:
                hint = "Weapon or tool"
            elif word in lst25:
                hint = "Stationary"

        elif level == 10:
            word = random.choice(level_10_list)

            if word in lst26:
                hint = "Body Accessory or a Gem"
            elif word in lst16:
                hint = "A type of a building or a part of a building"
            elif word in lst10:
                hint = "Food Item"



        if word in randomWords:
            continue
        else:
            break

    randomWords.append(word)

    jumble_pos = list(range(len(word)))
    random.shuffle(jumble_pos)
    jumbled_word = "".join([word[pos] for pos in jumble_pos])

    return [word, hint, jumbled_word]

def displayWord(word, letters):

    wordText = wordGuessFont.render(word, True, black)
    gameDisplay.blit(wordText, [20, 200])

def displayHint(hint):
    hintText = hintFont.render("Hint: " + hint, True, blue)
    gameDisplay.blit(hintText, [50, 300])

def displayScore(score):
    scoreText = scoreFont.render("Score: " + str(score), True, black)
    gameDisplay.blit(scoreText, [25, 20])

def displayLevel(level):
    levelText = scoreFont.render("Level: " + str(level), True, black)
    gameDisplay.blit(levelText, [610, 25])

def displayRatio(correctAnswers, Total):
    ratioText = ratioFont.render(str(int(correctAnswers)) + " out of " + str(int(Total)), True, black)
    gameDisplay.blit(ratioText, [300, 110])

def typeChar(char):
    TypeChar = wordType.render(char, True, green)
    gameDisplay.blit(TypeChar, [50, 395])
    pygame.display.update()

def printAnswer(word, chances):
    if chances == 0:
        msgAnswer = answerFont.render("The correct answer is: " + word[0], True, yellow)
        pygame.draw.rect(gameDisplay, green, [0, 500, 800, 600])
        gameDisplay.blit(msgAnswer, [200, 530])
    else:
        msgAnswer = answerFont.render("Correct!", True, yellow)
        pygame.draw.rect(gameDisplay, green, [0, 500, 800, 600])
        gameDisplay.blit(msgAnswer, [300, 530])

    pygame.display.update()

    pExit = False

    while not pExit:
        for event_3 in pygame.event.get():
            if event_3.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event_3.type == pygame.KEYDOWN:
                if event_3.key == pygame.K_RETURN:
                    pExit = True
                    break

def gameComplete(score, correctAnswers, Total):
    for printRect in range(0, 610, 10):
        pygame.draw.rect(gameDisplay, yellow, [0, 600 - (printRect), 800, 50 + (printRect)])
        pygame.display.update()
        clock.tick(50)

    clock.tick(1)

    cExit = False

    msgOver = msgFont.render("YOU COMPLETED THE GAME", True, black)
    finalScore = msgFont.render("WITH SCORE: " + str(score), True, black)
    finalMarks = msgFont.render("And marks: " + str(int(correctAnswers)) + " OUT OF " + str(int(Total)), True, black)
    playAgain = helpFont.render("Play Again", True, black)
    quitGame = helpFont.render("Quit", True, black)

    gameDisplay.fill(blue)
    pygame.draw.rect(gameDisplay, yellow, [0, 100, 800, 400])
    pygame.draw.rect(gameDisplay, green, [0, 0, 800, 100])
    pygame.display.update()
    clock.tick(5)

    gameDisplay.blit(msgOver, [100, 200])
    pygame.display.update()
    clock.tick(5)

    gameDisplay.blit(finalScore, [100, 300])
    pygame.display.update()
    clock.tick(5)

    gameDisplay.blit(finalMarks, [100, 350])
    pygame.display.update()
    clock.tick(5)

    while not cExit:
        gameDisplay.fill(blue)
        pygame.draw.rect(gameDisplay, yellow, [0, 100, 800, 400])
        pygame.draw.rect(gameDisplay, green, [0, 0, 800, 100])
        gameDisplay.blit(msgOver, [100, 200])
        gameDisplay.blit(finalScore, [100, 300])
        gameDisplay.blit(finalMarks, [100, 350])

        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()


        if 100 + 175 > cur[0] > 100 and 400 + 50 > cur[1] > 400:
            pygame.draw.rect(gameDisplay, light_green, [100, 400, 175, 50])
            if click[0] == 1:
                for printRect in range(0, 610, 10):
                    pygame.draw.rect(gameDisplay, blue, [0, 600 - (printRect), 800, 50 + (printRect)])
                    pygame.display.update()
                    clock.tick(70)
                gameLoop()
        else:
            pygame.draw.rect(gameDisplay, green, [100, 400, 175, 50])

        if 500 + 100 > cur[0] > 500 and 400 + 50 > cur[1] > 400:
            pygame.draw.rect(gameDisplay, light_red, [500, 400, 100, 50])
            if click[0] == 1:
                pygame.quit()
                quit()
        else:
            pygame.draw.rect(gameDisplay, red, [500, 400, 100, 50])

        gameDisplay.blit(playAgain, [125, 405])
        gameDisplay.blit(quitGame, [525, 405])

        pygame.display.update()

        for event_2 in pygame.event.get():
            if event_2.type == pygame.QUIT:
                pygame.quit()
                quit()

def startScreen():
    clock.tick(1)

    sExit = False
    helpLine1 = helpFont.render("You need to guess the word that appears on the screen", True, yellow)
    helpLine2 = helpFont.render("You will be given 5 chances for each word", True, yellow)
    helpLine3 = helpFont.render("There is no time limit", True, yellow)
    helpLine4 = helpFont.render("If you think that the word contains certain letter", True, black)
    helpLine5 = helpFont.render("Enter that letter and press Enter", True, black)
    helpLine6 = helpFont.render("If the word contains it, it would be displayed", True, black)
    helpLine7 = helpFont.render("There are 5 levels, and 5 words per level", True, black)
    helpLine8 = helpFont.render("Plus 100 points for each correct word multiplied by the level", True, black)
    helpLine9 = helpFont.render("plus 10 for each chance left", True, black)
    helpLine0 = helpFont.render("100 points deducted if you couldn't guess the word", True, black)

    quitGame = helpFont.render("Quit the game", True, light_yellow)

    playGame = helpFont.render("Play Game!", True, light_yellow)

    button1 = helpFont.render("Play", True, black)
    button2 = helpFont.render("Help", True, black)
    button3 = helpFont.render("Quit", True, black)

    Level1Start = wordGuessFont.render("LEVEL 1", True, green)

    gameDisplay.fill((0, 0, 0))
    gameDisplay.blit(bgimg, (0, 0))
    pygame.display.update()
    clock.tick(1)

    heading = wordGuessFont.render("JACKPOT", True, yellow)
    gameDisplay.blit(heading, [200, 100])
    pygame.display.update()
    clock.tick(1)

    while not sExit:
        gameDisplay.fill((0, 0, 0))
        gameDisplay.blit(bgimg, (0, 0))
        gameDisplay.blit(heading, [200, 100])

        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if 100 + 100 > cur[0] > 100 and 200 + 50 > cur[1] > 200:
            pygame.draw.rect(gameDisplay, light_green, [100, 200, 100, 50])
            gameDisplay.blit(playGame, [300, 300])
            if click[0] == 1:
                gameDisplay.fill((0, 0, 0))
                gameDisplay.blit(bgimg, (0, 0))
                gameDisplay.blit(heading, [200, 100])
                pygame.display.update()
                break
        else:
            pygame.draw.rect(gameDisplay, green, [100, 200, 100, 50])

        if 350 + 100 > cur[0] > 350 and 200 + 50 > cur[1] > 200:
            pygame.draw.rect(gameDisplay, light_yellow, [350, 200, 100, 50])

            gameDisplay.blit(helpLine1, [50, 300])
            gameDisplay.blit(helpLine2, [50, 325])
            gameDisplay.blit(helpLine3, [50, 350])
            gameDisplay.blit(helpLine4, [50, 375])
            gameDisplay.blit(helpLine5, [50, 400])
            gameDisplay.blit(helpLine6, [50, 425])
            gameDisplay.blit(helpLine7, [50, 450])
            gameDisplay.blit(helpLine8, [50, 475])
            gameDisplay.blit(helpLine9, [50, 500])
            gameDisplay.blit(helpLine0, [50, 525])

        else:
            pygame.draw.rect(gameDisplay, yellow, [350, 200, 100, 50])

        if 600 + 100 > cur[0] > 600 and 200 + 100 > cur[1] > 200:
            pygame.draw.rect(gameDisplay, light_red, [600, 200, 100, 50])
            gameDisplay.blit(quitGame, [300, 300])
            if click[0] == 1:
                pygame.quit()
                quit()
        else:
            pygame.draw.rect(gameDisplay, red, [600, 200, 100, 50])

        gameDisplay.blit(button1, [125, 205])
        gameDisplay.blit(button2, [375, 205])
        gameDisplay.blit(button3, [625, 205])

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    for printRect in range(0, 610, 10):
        pygame.draw.rect(gameDisplay, yellow, [0, 600 - (printRect), 800, 50 + (printRect)])
        pygame.display.update()
        clock.tick(50)

    gameDisplay.blit(Level1Start, [300, 250])
    pygame.display.update()
    clock.tick(1)

    for printRect in range(0, 610, 10):
        gameDisplay.blit(Level1Start, [300, 250])
        pygame.draw.rect(gameDisplay, blue, [0, 600 - (printRect), 800, 50 + (printRect)])
        pygame.display.update()
        clock.tick(70)

def levelTransition(level):
    for printRect in range(0, 610, 10):
        pygame.draw.rect(gameDisplay, yellow, [0, 600 - (printRect), 800, 50 + (printRect)])
        pygame.display.update()
        clock.tick(50)

    textLevelStart = wordGuessFont.render("LEVEL " + str(level), True, green)
    gameDisplay.blit(textLevelStart, [300, 250])
    pygame.display.update()
    clock.tick(1)

    for printRect in range(0, 610, 10):
        gameDisplay.blit(textLevelStart, [300, 250])
        pygame.draw.rect(gameDisplay, blue, [0, 600 - (printRect), 800, 50 + (printRect)])
        pygame.display.update()
        clock.tick(70)


def gameLoop():
    startScreen()
    gameExit = False
    string = ""
    letters = []
    chances = 5
    score = 0

    correctAnswers = 0.0
    Total = 0.0

    randomWords = []
    level = 1
    level_up_check = 0
    firstWord = True

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if len(string) < 16:
                    char = (chr(event.key))
                    string += char

                if event.key == pygame.K_RETURN:
                    if len(string) == 2:
                        letters.extend(string[0])
                    string = ""
                    chances -= 1

                    if chances == 0:
                        printAnswer(word, chances)
                        string = ""
                        letters = []
                        chances = 5
                        del randomWords[-1]
                        word = chooseWord(level, randomWords)
                        Total += 1
                        score -= 100
                        if score < 0:
                            score = 0

                if event.key == pygame.K_BACKSPACE:
                    if string[-1] != chr(8):
                        string = string[:-1]
                    else:
                        string = string[:-2]

        if firstWord == True:
            word = chooseWord(1, randomWords)
            displayWord(word[2], letters)
            displayHint(word[1])
            firstWord = False

        if word[0] == string:
            typeChar(string)
            pygame.display.update()
            score += (100 * level) + (chances * 10)

            if correctAnswers != 30:
                printAnswer(word, chances)
                if level_up_check >= 3:
                    level += 1
                    level_up_check = 0
                    clock.tick(5)
                    levelTransition(level)
                word = chooseWord(level, randomWords)

                Total += 1
                correctAnswers += 1
                string = ""
                level_up_check += 1
                letters = []
                chances = 5

            else:
                printAnswer(word, chances)
                gameComplete(score, correctAnswers, Total)

        gameDisplay.fill(blue)
        gameDisplay.blit(scoreButton, [0, 0])
        gameDisplay.blit(levelButton, [550, 0])
        displayScore(score)
        displayLevel(level)

        try:
            if ((correctAnswers / Total) * 100 >= 60):
                gameDisplay.blit(percent, [0, 80], [0, 0, 800, 90])
            elif ((correctAnswers / Total) * 100 >= 40) and ((correctAnswers / Total) * 100 < 60):
                gameDisplay.blit(percent, [0, 80], [0, 90, 800, 90])
            elif ((correctAnswers / Total) * 100 < 40):
                gameDisplay.blit(percent, [0, 80], [0, 180, 800, 90])
        except:
            gameDisplay.blit(inputText, [0, 80])

        displayRatio(correctAnswers, Total)

        gameDisplay.blit(wordFrame, [0, 160])
        displayWord(word[2], letters)
        displayHint(word[1])

        for i in range(chances):
            gameDisplay.blit(heart, [20 + (i * 50), 500])

        gameDisplay.blit(inputText, [0, 375])
        typeChar(string)

        clock.tick(FPS)
        pygame.display.update()

    pygame.quit()
    quit()

gameLoop()
