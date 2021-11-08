import pyxel
from random import shuffle

tm_y = 32
tm_x = 0
tile_num = 1
resolution = [210, 120]
title_color = pyxel.COLOR_BLACK

# situations
in_menu = True
in_options = False
in_game = False
in_pause = False
in_results = False
in_selection = False

# score
points = 1
result = None

# characters
white_male = True
black_male = False
white_girl = False
black_girl = False


# lists of answers
q1 = [("Software", False), ("Eletrica", True), ("Aeroes-\npacial", False), ("Automo-\ntiva", False)]
shuffle(q1)
q2 = [("Python", False), ("HTML", True), ("C", False), ("Pascal", False)]
shuffle(q2)
q3 = [("Uma especie\nde anti-\nderivada", True), ("A area abaixo\ndo grafico.", True),
      ("Variacao\nde taxa\nconstante", False), ("O limite de\numa funcao\nexponencial", False)]
shuffle(q3)
q4 = [("Arestas de\nrascunho", False), ("Arestas nao\nvisiveis", True), ("Arestas\nvisíveis", False),
      ("Arestas\nbonitas", False)]
shuffle(q4)
q5 = [("Agua que nao\nvemos numa\nproducao.", True), ("Agua\ncibernetica", False),
      ("Agua impor-\ntada", False), ("Agua total\nnuma pro-\nducao", False)]
shuffle(q5)
q6 = [("A quantidade\nde diedros", False), ("Simetria", True), ("A vista\nprincipal", False),
      ("Furos\npassantes", True)]
shuffle(q6)
q7 = [("Um numero", False), ("Codigos\nUnicode", True), ("Alfabeto", False), ("Simbolos\nquaisquer", False)]
shuffle(q7)
q8 = [("Calculo 1", False), ("Engenharia\nAmbiente", False), ("Desenho\nIndustrial", False),
      ("Introducao a\nAlgebra\nLinear", True)]
shuffle(q8)
q9 = [("Albert Eins-\ntein e Isaac\nNewton", False), ("Isaac Newton\ne Gottfried\nLeibniz", True),
      ("Albert Eins-\ntein e Gott-\nfried Leibniz", False), ("Vinicius Ris-\npoli e Ricar-\ndo Fragelli", False)]
shuffle(q9)
q10 = [("Impacto\nAmbiental", False), ("Aspecto\nAmbiental", True),
       ("Problema\nambiental", False), ("Elemento\nambiental", False)]
shuffle(q10)

def choosen_chr(x_position):
    pyxel.text(x_position, 45, "Selected", 0)


def chr_bodies_check():
    global tm_x, tm_y, tile_num
    tm_x = 5
    tile_num = 0
    if white_male:
        tm_y = 80
    if black_male:
        tm_y = 48
    if white_girl:
        tm_y = 32
    if black_girl:
        tm_y = 64


# chr_box_model
def chr_box(x_position, y_image, bm_select, wm_select, bg_select, wg_select):
    global black_male, white_male, black_girl, white_girl
    if x_position <= pyxel.mouse_x < x_position + 16 and 52 <= pyxel.mouse_y < 68:
        pyxel.blt(x_position, 52, 1, 16, y_image, 16, 16)
        if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON):
            black_male, white_male, black_girl, white_girl = bm_select, wm_select, bg_select, wg_select
    else:
        pyxel.blt(x_position, 52, 1, 16, y_image, 16, 16, pyxel.COLOR_YELLOW)


# win or lose
def results():
    global tm_x, tm_y, in_results, points, tile_num
    in_results = True

    # Scoreboard
    if points >= 1:
        pyxel.blt(176 - 16, 56, 1, 0, 120, 16, 8)
    if points >= 2:
        pyxel.blt(176 - 32, 56, 1, 0, 120, 16, 8)
    if points >= 3:
        pyxel.blt(176 - 48, 56, 1, 0, 112, 16, 8)
    if points >= 4:
        pyxel.blt(176 - 64, 56, 1, 0, 112, 16, 8)
    if points >= 5:
        pyxel.blt(176 - 80, 56, 1, 0, 104, 16, 8)
    if points >= 6:
        pyxel.blt(176 - 96, 56, 1, 0, 104, 16, 8)
    if points >= 7:
        pyxel.blt(176 - 112, 56, 1, 0, 96, 16, 8)
    if points >= 8:
        pyxel.blt(176 - 128, 56, 1, 0, 96, 16, 8)
    if points >= 9:
        pyxel.blt(176 - 144, 56, 1, 0, 88, 16, 8)
    if points == 10:
        pyxel.blt(176 - 160, 56, 1, 0, 88, 16, 8)

    if result and points != 10:
        pyxel.text(50, 10, "Congratulations!! Keep going and\n       achieve your SS!!!", pyxel.COLOR_LIME)

        # Botão continuar
        if 125 < pyxel.mouse_x < 190 and 70 < pyxel.mouse_y < 84:
            pyxel.blt(125, 70, 1, 0, 33, 64, 14, 0)
            if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON):
                points += 1
                chr_bodies_check()
                in_results = False
                game_screen()
        else:
            pyxel.blt(125, 70, 1, 0, 17, 64, 14, 0)
        pyxel.text(142, 75, "Continue", pyxel.COLOR_BLACK)
    elif not result:
        pyxel.text(90, 10, "GAME OVER", pyxel.COLOR_RED)
    elif points == 10:
        pyxel.text(80, 10, "YOU HAVE WON", pyxel.COLOR_YELLOW)
        pyxel.blt(85, 25, 0, 0, 120, 16, 16, pyxel.COLOR_PEACH)
    # Botão Recomeçar
    if 125 < pyxel.mouse_x < 190 and 85 < pyxel.mouse_y < 99:
        pyxel.blt(125, 85, 1, 0, 33, 64, 14, 0)
        if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON):
            points = 1
            chr_bodies_check()
            in_results = False
            shuffle(q1), shuffle(q2), shuffle(q3), shuffle(q4), shuffle(q5)
            game_screen()
    else:
        pyxel.blt(125, 85, 1, 0, 17, 64, 14, 0)
    pyxel.text(142, 90, "Restart", pyxel.COLOR_BLACK)

    # Botão Menu
    if 125 < pyxel.mouse_x < 190 and 100 < pyxel.mouse_y < 114:
        pyxel.blt(125, 100, 1, 0, 33, 64, 14, 0)
        if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON):
            points = 1
            tm_x, tm_y, tile_num = 0, 32, 1
            in_results = False
            menu_screen()
    else:
        pyxel.blt(125, 100, 1, 0, 17, 64, 14, 0)
    pyxel.text(152, 105, "Menu", pyxel.COLOR_BLACK)


# Buttons
def answers_animation(button_x, button_y, text: str, correct):
    global tm_x, tm_y, in_game, result, tile_num
    if button_x < pyxel.mouse_x < (button_x + 56) and button_y < pyxel.mouse_y < (button_y + 24):
        pyxel.blt(button_x, button_y, 1, 16, 136, 56, 24)
        if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON):
            tm_x, tm_y, tile_num = 36, 32, 1
            in_game = False
            result = correct
            results()
    else:
        pyxel.blt(button_x, button_y, 1, 16, 48, 56, 24)
    pyxel.text(button_x + 5, button_y + 3, text, pyxel.COLOR_BLACK)


def question_and_answer(question, a1, a1_correct, a2, a2_correct, a3, a3_correct, a4, a4_correct):
    pyxel.text(10, 10, question, 0)
    answers_animation(2, 60, a1, a1_correct)
    answers_animation(2, 90, a2, a2_correct)
    answers_animation(62, 60, a3, a3_correct)
    answers_animation(62, 90, a4, a4_correct)


# Screens
def menu_screen():
    global tm_x, tm_y, in_menu, in_options, title_color, tile_num
    pyxel.text(85, 10, "Show da SS", title_color)
    pyxel.text(10, 98, "Raphael Mendes da Silva 211039690\n"
                       "Ana Beatriz Norberto da Silva 211041080", title_color)
    in_menu = True
    if 75 < pyxel.mouse_x < 140 and 30 < pyxel.mouse_y < 44:
        pyxel.blt(75, 30, 1, 0, 33, 64, 14, 0)
        if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON):
            in_menu = False
            chr_bodies_check()
            game_screen()
    else:
        pyxel.blt(75, 30, 1, 0, 17, 64, 14, 0)
    pyxel.text(95, 34, "Start", pyxel.COLOR_BLACK)

    if 75 < pyxel.mouse_x < 140 and 50 < pyxel.mouse_y < 64:
        pyxel.blt(75, 50, 1, 0, 33, 64, 14, 0)
        if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON):
            in_menu = False
            tm_x, tm_y, tile_num = 0, 32, 1
            options_screen()
    else:
        pyxel.blt(75, 50, 1, 0, 17, 64, 14, 0)
    pyxel.text(93, 54, "Options", pyxel.COLOR_BLACK)

    if 190 < pyxel.mouse_x < 204 and 10 < pyxel.mouse_y < 24:
        pyxel.blt(190, 10, 1, 1, 129, 14, 14, 0)
        if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON):
            in_menu = False
            tm_x, tm_y, tile_num = 0, 64, 1
            selection_screen()
    else:
        pyxel.blt(190, 10, 1, 1, 145, 14, 14, 0)


def selection_screen():
    global tm_x, tm_y, in_selection, tile_num
    in_selection = True
    pyxel.text(50, 10, "Escolha seu sofredor(a)", pyxel.COLOR_WHITE)
    chr_box(22, 160, False, True, False, False)
    chr_box(66, 176, True, False, False, False)
    chr_box(110, 192, False, False, False, True)
    chr_box(158, 208, False, False, True, False)
    if white_male:
        choosen_chr(12)
    elif black_male:
        choosen_chr(56)
    elif white_girl:
        choosen_chr(100)
    elif black_girl:
        choosen_chr(148)

    if 10 < pyxel.mouse_x < 75 and 100 < pyxel.mouse_y < 113:
        pyxel.blt(10, 100, 1, 0, 33, 64, 14, 0)
        if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON):
            in_selection = False
            tm_x, tm_y, tile_num = 0, 32, 1
            menu_screen()
    else:
        pyxel.blt(10, 100, 1, 0, 17, 64, 14, 0)
    pyxel.text(13, 104, "Voltar", pyxel.COLOR_BLACK)


def game_screen():
    global in_game, points
    in_game = True
    if points == 1:
        question_and_answer("Questao 1 \nQual dessas Engenharias\nnao esta na FGA?",
                            q1[0][0], q1[0][1], q1[1][0], q1[1][1], q1[2][0], q1[2][1], q1[3][0], q1[3][1])
    if points == 2:
        question_and_answer("Questao 2 \nQual dessas nao\ne uma linguagem\nde programacao?", q2[0][0],
                            q2[0][1], q2[1][0], q2[1][1], q2[2][0],
                            q2[2][1], q2[3][0], q2[3][1])
    if points == 3:
        question_and_answer("Questao 3 \nO que e uma\nintegral?", q3[0][0],
                            q3[0][1], q3[1][0], q3[1][1], q3[2][0],
                            q3[2][1], q3[3][0], q3[3][1])
    if points == 4:
        question_and_answer("Questao 4 \nO que as linha\ntracejadas representam\nnum Desenho Tecnico?",
                            q4[0][0], q4[0][1], q4[1][0], q4[1][1], q4[2][0], q4[2][1],
                            q4[3][0], q4[3][1])
    if points == 5:
        question_and_answer("Questao 5 \nO que e agua virtual?",
                            q5[0][0], q5[0][1], q5[1][0], q5[1][1], q5[2][0], q5[2][1], q5[3][0], q5[3][1])
    if points == 6:
        question_and_answer("Questao 6 \nO que e uma\nlinha ponto-traco\nem Desenho Tecnico?", q6[0][0], q6[0][1],
                            q6[1][0], q6[1][1], q6[2][0], q6[2][1], q6[3][0], q6[3][1])
    if points == 7:
        question_and_answer("Questao 7 \nO que e uma String\nem programacao?", q7[0][0],
                            q7[0][1], q7[1][0], q7[1][1], q7[2][0], q7[2][1], q7[3][0], q7[3][1])
    if points == 8:
        question_and_answer("Questao 8 \nQual dessas nao e\numa materia do 1\nsemestre de engenharia?",
                            q8[0][0], q8[0][1], q8[1][0], q8[1][1], q8[2][0], q8[2][1], q8[3][0], q8[3][1])
    if points == 9:
        question_and_answer("Questao 9 \nQuem criou o Calculo?", q9[0][0], q9[0][1], q9[1][0],
                            q9[1][1], q9[2][0], q9[2][1], q9[3][0], q9[3][1])
    if points == 10:
        question_and_answer("Questao 10 \nEmitir gases de\nefeito estufa na at-\nmosfera e um (resposta)?",
                            q10[0][0], q10[0][1], q10[1][0], q10[1][1], q10[2][0], q10[2][1],
                            q10[3][0], q10[3][1])


def options_screen():
    global tm_x, tm_y, in_menu, in_options, tile_num
    in_options = True
    pyxel.text(5, 5, "OPTIONS", pyxel.COLOR_RED)
    pyxel.text(10, 25, "Resolucao Nao da para mudar hahahahaha", pyxel.COLOR_RED)
    pyxel.text(10, 45, "Som: Abaixe ou \naumente o volume pelo \nseu dispositivo mesmo.", pyxel.COLOR_RED)
    pyxel.text(10, 75, "Controles: E um quiz, so clicar :v", pyxel.COLOR_RED)

    if 10 < pyxel.mouse_x < 75 and 100 < pyxel.mouse_y < 113:
        pyxel.blt(10, 100, 1, 0, 33, 64, 14, 0)
        if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON):
            in_options = False
            tm_x, tm_y, tile_num = 0, 32, 1
            menu_screen()
    else:
        pyxel.blt(10, 100, 1, 0, 17, 64, 14, 0)
    pyxel.text(35, 104, "Voltar", pyxel.COLOR_BLACK)


def update():
    ...


def draw():
    pyxel.cls(0)
    pyxel.bltm(0, 0, tile_num, tm_x, tm_y, 27, 16)
    if in_menu:
        menu_screen()
    if in_options:
        options_screen()
    if in_game:
        game_screen()
    if in_results:
        results()
    if in_selection:
        selection_screen()


class App:
    def __init__(self):
        pyxel.init(resolution[0], resolution[1], caption="Show do SS - Semestre 1")
        pyxel.mouse(True)
        pyxel.load("../../../UnB/Show do SS/show.pyxres")
        pyxel.run(update, draw)


App()
