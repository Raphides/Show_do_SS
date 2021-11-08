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

Uma função utiliza-se da outra para fazerem um trabalho repetitivo que poderia gastar muitas mais linhas de código. A função `answers_animation()` usa do código 
