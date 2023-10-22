from operator import itemgetter
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.behaviors.button import ButtonBehavior
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.widget import Widget, ListProperty
from kivy.graphics import Line, Color
from random import choice
from functools import partial
from game import fields_check



class GameLayout(BoxLayout):
    rows = 3
    cols = 3
    len_win = 3

    def on_parent(self, *args):
        self.grid = self.rows * self.cols + 1
        self.player = None
        self.lines = list()
        self.result = {x: None for x in range(1, self.grid)}
        self.end_game = False
        self.ids['gameArea'].rows = self.rows
        self.ids['gameArea'].cols = self.cols

        for id_ in range(1, self.grid):
            btn_area = ButtonPlay()
            btn_area.bind(on_release=partial(self.play, id_))
            self.ids[id_] = btn_area
            try:
                self.ids['gameArea'].add_widget(btn_area)
            except Exception:
                pass

    def change_grid(self, rows, cols, len_win):
        self.rows = rows
        self.cols = cols
        self.len_win = len_win
        self.restart()
        self.ids['gameArea'].clear_widgets()
        self.on_parent()
        
    def play(self, id_, *args):
        if self.result[id_] is not None or self.end_game:
            return
        self.id_ = id_
        self.check_turn()
        self.result[id_] = self.player

        # update front-end
        Window.add_widget(self.player)
        self.check_win()
        self.check_end()
        
    def check_turn(self):
        """Valida de quem é o turno."""
        if isinstance(self.player, Player1):
            self.player = Player2(self.ids[self.id_])
        elif isinstance(self.player, Player2):
            self.player = Player1(self.ids[self.id_])
        else:
            self.player = choice([
                Player1(self.ids[self.id_]), 
                Player2(self.ids[self.id_])
            ])

    def check_win(self):
        """Valida se tem um ganhador."""
        fields = list(self.result.values())
        result = list(map(lambda x: x.__class__, fields))
        p_len = result.count(self.player.__class__)

        if p_len < self.len_win:
            return
        
        dict_fields = fields_check(self.cols, self.rows, self.len_win)
        for orientation, wins in dict_fields.items():
            for win in wins:
                res = list(itemgetter(*win)(result))
                for index in range(len(res) - self.len_win + 1):
                    if res[index: index + self.len_win].count(self.player.__class__) == self.len_win:
                        line = LineWin(orientation, fields[win[index]], fields[win[index + self.len_win - 1]])
                        self.lines.append(line)
                        Window.add_widget(line)
                        self.end_game = True        

    def check_end(self):
        """Valida se deu velha."""
        if not None in self.result.values() and not self.end_game:
            print('deu velha')
            return

    def restart(self):
        """Reinicia o jogo."""
        for player in self.result.values():
            if player is not None:
                player.canvas.clear()
                Window.unbind(
                    on_minimize=player.update,
                    on_maximize=player.update,
                    on_restore=player.update,
                    on_resize=player.update,
                )
        for line in self.lines:
            line.canvas.clear()
            Window.unbind(
                on_minimize=line.update,
                on_maximize=line.update,
                on_restore=line.update,
                on_resize=line.update,
            )
        self.player = None
        self.result = {x: None for x in range(1, self.grid)}
        self.end_game = False


class ButtonPlay(ButtonBehavior, Label):
    def __init__(self, **kwargs):
        super(ButtonPlay, self).__init__(**kwargs)


class LineWin(Widget):
    """Linha do vencedor do jogo."""
    color = ListProperty([0, 0, 0, 1])
    ini_x = None

    def __init__(self, orientation, ini, end, **kwargs):
        super(LineWin, self).__init__(**kwargs)
        self.orientation = orientation
        self.field_ini = ini.field
        self.field_end = end.field
        self.update()
        Window.bind(
            on_minimize=self.update,
            on_maximize=self.update,
            on_restore=self.update,
            on_resize=self.update,
        )

    def update(self, *args):
        self.canvas.clear()
        pos = min(self.field_ini.width, self.field_ini.height)
        if self.orientation == 0:
            # horizontal
            points = (
                self.field_ini.center_x - pos / 2,
                self.field_ini.center_y,
                self.field_end.center_x + pos / 2,
                self.field_end.center_y
            )

        elif self.orientation == 1:
            # vertical
            points = (
                self.field_ini.center_x,
                self.field_ini.center_y + pos / 2,
                self.field_end.center_x,
                self.field_end.center_y - pos / 2
            )
        elif self.orientation == 2:
            # paralelo esq - dir
            points = (
                self.field_ini.center_x - pos / 2,
                self.field_ini.center_y + pos / 2,
                self.field_end.center_x + pos / 2,
                self.field_end.center_y - pos / 2
            )

        elif self.orientation == 3:
            # paralelo dir - esq
            points = (
                self.field_ini.center_x + pos / 2,
                self.field_ini.center_y + pos / 2,
                self.field_end.center_x - pos / 2,
                self.field_end.center_y - pos / 2
            )

        with self.canvas:
            Color(rgba=self.color),
            Line(
                width=pos / 30,
                points=points,
                cap='square',
                joint='bevel'
            )


class Player1(Widget):
    """Player (⭕)."""
    color = ListProperty([.1, .1, 1, 1])

    def __init__(self, field, **kwargs):
        super(Player1, self).__init__(**kwargs)
        self.field = field
        self.update()
        Window.bind(
            on_minimize=self.update,
            on_maximize=self.update,
            on_restore=self.update,
            on_resize=self.update,
        )

    def update(self, *args):
        self.canvas.clear()
        with self.canvas:
            Color(rgba=self.color),
            Line(
                width=min(self.field.width, self.field.height) / 15,
                circle=(
                    self.field.center_x,
                    self.field.center_y,
                    min(self.field.width, self.field.height) / 3.5
                ),
            )


class Player2(Widget):
    """Player (❌)."""
    color = ListProperty([1, .1, .1, 1])
    
    def __init__(self, field, **kwargs):
        super(Player2, self).__init__(**kwargs)
        self.field = field
        self.update()
        Window.bind(
            on_minimize=self.update,
            on_maximize=self.update,
            on_restore=self.update,
            on_resize=self.update,
        )
    
    def update(self, *args):
        self.canvas.clear()
        pos = min(self.field.width, self.field.height) / 3.8
        with self.canvas:
            Color(rgba=self.color),
            Line(
                width=min(self.field.width, self.field.height) / 15,
                points=(
                    self.field.center_x - pos,
                    self.field.center_y - pos,
                    self.field.center_x + pos,
                    self.field.center_y + pos,
                    self.field.center_x,
                    self.field.center_y,
                    self.field.center_x + pos,
                    self.field.center_y - pos,
                    self.field.center_x - pos,
                    self.field.center_y + pos
                ),
                joint='round',
                cap='round'
            )


class MainApp(App):
    def build(self):
        return GameLayout()
