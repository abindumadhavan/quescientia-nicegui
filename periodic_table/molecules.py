from nicegui import ui

@ui.page('/molecules', title='The World of Molecules')
def show():
    ui.markdown("""
    # Welcome to the World of Molecules!

    #### Use the atoms and combine them to form molecules.
    - **Drag and drop each atom on the area above** 
    - **When you bring another atom closer to an existing one, a bond forms where possible**
    - **If the molecule is recognized, its name appears automatically**
    - **Click on the bonded area, a scissor appears and you can break the bond**
    """)

    ui.element('iframe').props('src="https://phet.colorado.edu/sims/html/build-a-molecule/latest/build-a-molecule_en.html"').classes('w-full h-[calc(100vh-20em)] border-none')
