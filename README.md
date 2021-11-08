# Show_do_SS
"Show do SS" is a Algorithms and Computer Programming's final project. We are from class EE 2021/1 from UnB, being tutored by Fábio Mendes. This project was a game, done with Pyxel and Random Libraries in Pycharm, using Python.

"Show do SS" é um projeto final de Algorítmos e Programação de Computadores. Nós somos da Classe EE 2021/1 da UnB, sendo lecionados por Fábio Mendes. Este projeto foi um jogo usando Python, feito a partir das bibliotecas Pyxel e Random.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Show do SS tem um nome que parodia as franquias de jogos Show do Milhão, mas acaba se assemelhando mais a jogos como Genio Quiz e derivados. Sendo um jogo de quiz, seu tema em específico é a vivência dos calouros do 1º semestre dentro da FGA, Faculdade do Gama focada em Engenharias e faz parte da Universidade de Brasília.
  
Boa parte de seu código foi feita a partir da linguagem de programação Python, principalmente da biblioteca Pyxel.

A estrutura básica da bibioteca Pyxel usa principalmente as funções draw() e update(), ambas sendo chamadas várias vezes durante a execução do código. Nesse jogo, foi utilizada somente a função draw(), mais adequada para transições de tela.

Primeiramente, subdividiu-se o arquivo em 5 telas através de funções:
~~~~python
      menu_screen()
      options_screen()
      game_screen()
      results()
      selection_screen()
~~~~

Cada função muda a posição do tilemap e troca as imagens visíveis. Da mesma forma, existem variáveis que mostram se o monitor estava em determinada tela. Essas variáveis, assim como todas as variáveis não locais se encontram no início do código.
~~~python

      # situations
      in_menu = True
      in_options = False
      in_game = False
      in_pause = False
      in_results = False
      in_selection = False
~~~
      
Essas variáveis de "estado/situação" foram criadas para que a troca de telas fosse feita a partir de condicionais (if, elif e else). Caso a tela estivesse no menu do jogo, a variável in_menu seria alterada para True e, a patir disso foram criadas essas condições na função draw():
~~~python
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
~~~

Por exemplo, quando `in_game` for `True` a função game_screen será executada. Aí quando `in_menu` for `True`, `in_game` já será `False` e somente a tela de menu agora será executada. A atualização de quadros se dá através do `pyxel.cls()`. Tendo agora as telas nas quais o jogo acontecerá, foram feitas os vários elementos que as compõe.

Todas as telas possuem "botões". Ainda que pudessem ser reduzidos a funções, escolhemos não fazer (por pura preguiça). Entretanto, todos os botões do código seguem um padrão desse tipo:

~~~python
if button_x < pyxel.mouse_x < (button_x + 56) and button_y < pyxel.mouse_y < (button_y + 24):
        pyxel.blt(button_x, button_y, 1, 16, 136, 56, 24)
        if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON):
          # algo a para acontecer feito
         else:
        pyxel.blt(button_x, button_y, 1, 16, 48, 56, 24)
    pyxel.text(button_x + 5, button_y + 3, text, pyxel.COLOR_BLACK)
~~~
Essa condição traduz-se em "caso o mouse estiver fora área da imagem do botão, a imagem do botão aparecerá. Agora se o mouse estiver na área da imagem do botão, a imagem aparecerá mais clara ou com outra cor. E se o usuário apertar com o botão direito do mouse na área do botão, alguma outra coisa vai acontecer". Ao apertar nos botões nesse quiz, muitas situações diferentes podem acontecer, desde mudanças de tela para soma de pontos, ativação de condições ou adição de novas imagens.


No Menu Principal, são usados somente botões para mudar de tela. São compostos basicamente pela estrutura padrão de botões, uma mudança de tilemaps e de variáveis de estado (exemplo: `in_game`).

Na tela de opções, como não há opções modificáveis, os recursos são os mesmos do Menu.

Na tela de jogo, além do que foi feito no menu, também aparecem outras configurações de botões. Os botões de respotas às perguntas, por exemplo, foram feitos por pergunta. Ou seja, todos os 4 botões de respostas, assim como a pergunta, foram feitos numa única função, a `question_and_answer()`

A `question_and_answer()` é uma função que engloba uma outra função, a `answers_animation()`. A estrutura de ambas é assim:

~~~python
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
~~~

~~~python
ef question_and_answer(question, a1, a1_correct, a2, a2_correct, a3, a3_correct, a4, a4_correct):
    pyxel.text(10, 10, question, 0)
    answers_animation(2, 60, a1, a1_correct)
    answers_animation(2, 90, a2, a2_correct)
    answers_animation(62, 60, a3, a3_correct)
    answers_animation(62, 90, a4, a4_correct)
~~~

Uma função utiliza-se da outra para fazerem um trabalho repetitivo ao desenvolvedo que poderia gastar muitas mais linhas de código. A função `answers_animation()` usa do código padrão dos botões, usando atributos nas partes que variam. Como esses botões de resposta executam todos a exata mesma ação, acabou sendo muito mais fácil a realização uma função que englobasse-as como um todo. Dessa forma, a `answers_animation()` desenha e salva os elementos de um dos botões de resposta, enquanto ` question_and_answer` usa da função anterior para fazer os outros 3 botões e padronizá-los numa função, com as pequenas diferenciações entre as perguntas (como a escrita e se a alternativa estava certa ou errada) sendo especificadas em seus atributos.

Auxiliando essas duas funções, foram criadas listas de respostas, armazenadas em variáveis "q _n_", cujo nome define qual questão seus elementos estão se referindo. Por exemplo, para a pergunta 1: _Qual dessas Engenharias não está na FGA?_

~~~python
q1 = [("Software", False), ("Eletrica", True), ("Aeroes-\npacial", False), ("Automo-\ntiva", False)]
shuffle(q1)
~~~
Na lista q1, cada elemento equivale a uma tupla, que carrega consigo a alternativa escrita por extenso como primeiro elemento e se esta está correta (True) ou errada (False). O shuffle() ali embaixo é uma função pertencente à biblioteca Random, cuja é embaralhar os elementos da lista. Note que o shuffle só embaralha os elementos da lista e não da tupla, logo ("Software", False) podem mular de lugar na lista, mas vão continuar com "Software" na primeira posição da tupla e "False" na segunda. Isso é essencial para entender o código contido na função da tela `game_screen()`. Veja um trecho:

~~~python
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
~~~

Com os atributos da função `question_and_answer` sendo a _questão n_, _resposta x de 4_ e _se tal resposta está certa ou errrada (True or False)_, as listas "q _n_" ditas anteriormente podem ser usadas para se identificar uma alternativa aleatória e se esta está certa ou não. `q[x][0]` é a resposta e `q[x][1]` é se ela era verdadeira ou falsa. A função `game_screen()` é somente essas condicionais até a última questão. Não tem outro segredo.

Ao clicar na resposta da pergunta, independente de estar certa ou não, você será levado para a tela de resultados, de função `result()`. 
