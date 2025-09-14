from nicegui import ui

@ui.page('/physics-fun')
def show():
    ui.label('Welcome to the Fun with Physics page!')
    ui.label('Here you will find resources and tutorials to get started with Learning Physics.')
    ui.button('Back to Home', on_click=lambda: ui.navigate.to('/'))