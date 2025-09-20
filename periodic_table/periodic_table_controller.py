from nicegui import ui
from periodic_table import molecules, periodic_table, atomic_structure, build_an_atom

item_selected = 'The Periodic Table'

control_dict = {    
    '00': {
        'item_name': 'The Periodic Table',
        'label': 'Hover over elements to see details',
        'content_file': 'periodic_table.show()'
    },
    '01': {
        'item_name': 'Atomic Structure',
        'label': 'Select an atom and explore its structure',
        'content_file': 'atomic_structure.show()'
    },
    '02': {
        'item_name': 'Build an Atom',
        'label': 'Play around and build basic atom',
        'content_file': 'build_an_atom.show()'
    },
    '03': {
        'item_name': 'Molecules',
        'label': 'Explore molecular formations',
        'content_file': 'molecules.show()'
    }

}    


@ui.refreshable
def content_pane():
    """This function contains the content to be refreshed."""
    #print(game_selected)
    for key, value in control_dict.items():
        if value['item_name'] == item_selected:
            eval(control_dict[key]['content_file'])
            break


def handle_radio_change(e):
    """Callback function for the stepper's value change."""
    global item_selected
    item_selected = e.value
    content_pane.refresh()


@ui.page('/periodic-table')
def show():
    with ui.left_drawer(top_corner=True, bottom_corner=True).style('background-color: #d7e3f4'):
        ui.label('Let\'s explore the atoms, elements and molecules').classes('text-xl font-bold p-4')
        ui.radio(['The Periodic Table', 'Atomic Structure', 'Build an Atom', 'Molecules'], value='The Periodic Table', on_change=handle_radio_change)
        ui.button('Home', on_click=lambda: ui.navigate.to('/')).classes('m-4')

    #print(game_selected)
    content_pane()

