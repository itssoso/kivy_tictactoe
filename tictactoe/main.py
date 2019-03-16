from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.properties import NumericProperty, StringProperty, ObjectProperty


class Cell(Button):
    id = NumericProperty()


class Board(GridLayout):
    cols = NumericProperty(0)
    def _reset_board(self, playturn):
        self.clear_widgets()
        for i in range(self.cols**2):
            self.add_widget(Cell(id=i, on_press=playturn))

    def _status(self):
        return [x.text for x in self.children]


class Game(Widget):
    currentPlayer = StringProperty('X')
    menu = ObjectProperty()
    board = ObjectProperty()

    def _play_turn(self, button):
        button.text = self.currentPlayer
        button.disabled = True
        self._check_game_status()

    def _reset(self):
        self.menu.dismiss()
        self.board._reset_board(self._play_turn)

    def _check_game_status(self):
        status = self.board._status()
        if(
            len([x for x in status[:3] if x == self.currentPlayer ]) == 3 or
            len([x for x in status[3:6] if x == self.currentPlayer ]) == 3 or
            len([x for x in status[6:9] if x == self.currentPlayer ]) == 3 or
            len([x for x in status[::3] if x == self.currentPlayer ]) == 3 or
            len([x for x in status[1::3] if x == self.currentPlayer ]) == 3 or
            len([x for x in status[2::3] if x == self.currentPlayer ]) == 3 or
            len([x for x in status[::4] if x == self.currentPlayer]) == 3 or 
            len([x for x in status[2:7:2] if x == self.currentPlayer]) == 3 
            ):
            self.menu.title.text = f'Player "{self.currentPlayer}" Wins'
            self.menu.open()
        if(len([x for x in status if x == '']) == 0):
            self.menu.title.text = 'DRAW'
            self.menu.open()
        else:
            self.currentPlayer = 'X' if self.currentPlayer != 'X' else 'O'


class TicTacToeApp(App):
    def build(self):
        return Game()


if __name__ == '__main__':
    TicTacToeApp().run()
