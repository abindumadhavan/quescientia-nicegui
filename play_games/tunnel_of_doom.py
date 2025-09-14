from nicegui import ui

@ui.page('/tunnel-of-doom', title='Tunnel of Doom')
def show():
    ui.markdown("""
    # Welcome! You're playing Tunnel of Doom.

    #### Drag the cat through the tunnel to it's home. Please be careful, and do not touch the walls.
    - **Press the green flag to start** 
    - **Press the red button to stop**
    - **Start again if you touched the wall as the timer ticks**
    """)

    ui.element('iframe').props('src="https://scratch.mit.edu/projects/1203401862/embed"').classes('w-full h-[calc(100vh-20em)] border-none')    
