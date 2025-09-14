from nicegui import ui

control_dict = {    
    '00': {
        'chap_name': 'Chapter 0: Introduction',
        'label': 'Brief overview of the Python programming language',
        'content_file': 'python_intro/chap_00.md'
    },
    '01': {
        'chap_name': 'Chapter 1: Getting Started',
        'label': 'Install Python and set up your environment',
        'content_file': 'python_intro/chap_01.md'
    },
    '02': {
        'chap_name': 'Chapter 2: Variables and Data Types',
        'label': 'Learn about variables, strings, integers, and lists',
        'content_file': 'python_intro/chap_02.md'
    },
    '03': {
        'chap_name': 'Chapter 3: Control Structures',
        'label': 'Understand: if statements, loops, and functions',
        'content_file': 'python_intro/chap_03.md'
    }
}    

@ui.refreshable
def content_pane():
    """This function contains the content to be refreshed."""
    # print(current_step)

    for key, value in control_dict.items():
        if value['chap_name'] == current_step:
            with open(control_dict[key]['content_file']) as file:
                code_content = file.read()
                ui.markdown(code_content)
            break


def update_content(e):
    """Callback function for the stepper's value change."""
    global current_step
    current_step = e.value
    content_pane.refresh()


@ui.page('/python-intro')
def show():
    with ui.left_drawer(top_corner=True, bottom_corner=True).style('background-color: #d7e3f4'):
        ui.label('Introduction to Python').classes('text-xl font-bold p-4')

        with ui.stepper(on_value_change=update_content).props('vertical').classes('w-full') as stepper:
            for items in control_dict.values():
                with ui.step(items['chap_name']):
                    ui.label(items['label']).classes('text-sm mb-4 ml-4')
                    with ui.stepper_navigation().classes('mb-4 ml-4'):
                        ui.button('Next', on_click=stepper.next)
                        ui.button('Back', on_click=stepper.previous).props('flat')

        stepper.value = 'Chapter 0: Introduction'  # Set initial step
        ui.button('Home', on_click=lambda: ui.navigate.to('/')).classes('m-4')

    content_pane()

