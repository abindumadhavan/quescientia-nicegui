from nicegui import ui

@ui.page('/maths-easy')
def show():
    ui.label('Welcome to the Maths made Easy page!')
    ui.label('Here you will find resources and tutorials to get started with Learning Maths.')
    ui.button('Back to Home', on_click=lambda: ui.navigate.to('/'))