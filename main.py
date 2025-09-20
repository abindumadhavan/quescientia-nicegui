from nicegui import ui
from python_intro import python_intro_controller
from maths_easy import maths_chap1
from physics_fun import physics_chap1
from play_games import games_controller
from periodic_table import periodic_table_controller

@ui.page('/')
def main_page():
    with ui.row().classes('w-full items-center justify-left bg-green-300 p-2'):
        ui.label('QueScientia').classes('text-black text-lg font-bold ml-4')
        #ui.space() # Pushes subsequent elements to the right
        with ui.button('Learn').classes('text-black hover:bg-green-100'):
            with ui.menu() as menu1:
                ui.menu_item('Introduction to Python', lambda: ui.navigate.to('/python-intro'))
                ui.menu_item('Maths made easy', lambda: ui.navigate.to('/maths-easy')   )
                ui.menu_item('Fun with Physics', lambda: ui.navigate.to('/physics-fun'))
                ui.menu_item('The Periodic Table', lambda: ui.navigate.to('/periodic-table'))

        with ui.button('Analyze').classes('text-black hover:bg-green-100'):
            with ui.menu() as menu2:
                ui.menu_item('Motion', lambda: ui.notify('Selected item 1'))
                ui.menu_item('Space', lambda: ui.notify('Selected item 2'))
                ui.menu_item('Energy', lambda: ui.notify('Selected item 3'))
        ui.button('Apply', on_click=lambda: ui.notify('Services clicked')).classes('text-black hover:bg-green-100')
        ui.button('Play', on_click=lambda: ui.navigate.to('/play-games')).classes('text-black hover:bg-green-100')
        ui.button('About', on_click=lambda: ui.notify('Contact clicked')).classes('text-black hover:bg-green-100 mr-4')

    ui.label('Welcome to the QueScientia Home Page!').classes('text-2xl font-bold mt-8')
    ui.label('Explore our resources and tutorials to enhance your knowledge in various subjects.').classes('mt-4')
    
@ui.page('/python-intro',title='Introduction to Python')
def python_intro_subpage():
    python_intro_controller.show()

@ui.page('/maths-easy',title='Maths made easy')
def maths_easy_subpage():
    maths_chap1.show()

@ui.page('/physics-fun',title='Fun with Physics')
def physics_fun_subpage():
    physics_chap1.show()

@ui.page('/periodic-table',title='The Periodic Table')
def periodic_table_subpage():
    periodic_table_controller.show()

@ui.page('/play-games',title='Relax and Play')
def play_games_subpage():
    games_controller.show()

ui.run(title='Welcome to QueScientia')