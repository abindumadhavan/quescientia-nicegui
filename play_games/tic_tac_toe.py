from nicegui import ui

@ui.page('/tic-tac-toe', title='Tic-Tac-Toe')
def show():
    ui.label("Tic Tac Toe game will be here soon!").classes('text-2xl font-bold mt-8')