from nicegui import ui
from play_games import tunnel_of_doom, tic_tac_toe, game3

game_selected = 'Tic-Tac-Toe'

control_dict = {    
    '00': {
        'game_name': 'Tic-Tac-Toe',
        'label': 'Play Tic Tac Toe against an AI agent',
        'content_file': 'tic_tac_toe.show()'
    },
    '01': {
        'game_name': 'Tunnel of Doom',
        'label': 'Play Tunnel of Doom and guide the cat through the tunnel',
        'content_file': 'tunnel_of_doom.show()'
    },
    '02': {
        'game_name': 'Game 3',
        'label': 'Game 3 to be developed',
        'content_file': 'game3.show()'
    }

}    

@ui.refreshable
def content_pane():
    """This function contains the content to be refreshed."""
    #print(game_selected)
    for key, value in control_dict.items():
        if value['game_name'] == game_selected:
            eval(control_dict[key]['content_file'])
            break


def handle_radio_change(e):
    """Callback function for the stepper's value change."""
    global game_selected
    game_selected = e.value
    content_pane.refresh()


@ui.page('/play-games')
def show():
    with ui.left_drawer(top_corner=True, bottom_corner=True).style('background-color: #d7e3f4'):
        ui.label('Lets play games and have some fun').classes('text-xl font-bold p-4')
        ui.radio(['Tic-Tac-Toe', 'Tunnel of Doom', 'Game 3'], value='Tic-Tac-Toe', on_change=handle_radio_change)
        ui.button('Home', on_click=lambda: ui.navigate.to('/')).classes('m-4')

    #print(game_selected)
    content_pane()
    
