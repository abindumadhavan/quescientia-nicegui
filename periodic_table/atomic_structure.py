from nicegui import ui

@ui.page('/atomic_structure', title='The Atomic Structure')
def show():
    global el_info, plot_area
    ui.markdown("""
    # Here we are going to dive deeper inside atoms!

    #### Explore the atoms, their atomic structures incl. electron configuration.
    - **Learn about each atom by selecting it from the drop down**
    - **Discover electron orbital structures (bohr model)**
    """)

    ui.element('iframe').props('src="https://artsexperiments.withgoogle.com/periodic-table/"').classes('w-full h-[calc(100vh-20em)] border-none')