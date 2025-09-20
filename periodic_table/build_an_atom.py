from nicegui import ui

@ui.page('/build_an_atom', title='The Atomic Playground')
def show():

    ui.markdown("""
    # Here we are going to dive deeper inside atoms!

    #### Learn atomic structures incl. electron configuration.
    - **Build atoms by dragging and dropping protons and electrons**
    - **Discover electron orbital structures (bohr model) or (cloud model)**
    """)

    ui.element('iframe').props('src="https://phet.colorado.edu/sims/html/build-an-atom/latest/build-an-atom_all.html"').classes('w-full h-[calc(100vh-20em)] border-none')