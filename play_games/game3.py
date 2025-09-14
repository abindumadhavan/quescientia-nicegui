from nicegui import ui

@ui.page('/game3', title='Game 3')
def show():
    ui.label('# Game 3 - Coming Soon!').classes('text-2xl font-bold mt-8')