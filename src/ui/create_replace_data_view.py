from tkinter import Tk, ttk, constants
from services.program_service import program_service


class CreateReplaceDataView:
    def __init__(self, root, handle_show_main_view):
        self._root = root
        self._handle_show_main_view = handle_show_main_view
        self._document_name_entry = None
        self._user_input_data_entry = None
        self._placeholder_entry = None
        self._instruction_entry = None
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _handle_button_click(self):
        program_service.create_replace_data(
            self._document_name_entry.get(),
            self._user_input_data_entry.get(),
            self._placeholder_entry.get(),
            self._instruction_entry.get()
            )
        print(f"Tieto luotu.")


    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(master=self._frame, text="Lisää täyttötietoja järjestelmään")
        document_name_label = ttk.Label(master=self._frame, text="Asiakirjapohjan nimi:")
        self._document_name_entry = ttk.Entry(master=self._frame)

        user_input_data_label = ttk.Label(master=self._frame, text="Täytettävän tiedon tyyppi:")
        self._user_input_data_entry = ttk.Entry(master=self._frame)

        placeholder_label = ttk.Label(master=self._frame, text="Paikkatietomerkintä:")
        self._placeholder_entry = ttk.Entry(master=self._frame)

        instruction_label = ttk.Label(master=self._frame, text="Ohje käyttäjälle:")
        self._instruction_entry = ttk.Entry(master=self._frame)

        button = ttk.Button(
            master=self._frame,
            text="Lisää tieto",
            command=self._handle_button_click
            )
        
        button2 = ttk.Button(
            master=self._frame,
            text="Palaa alkuvalikkoon",
            command=self._handle_show_main_view
            )
                
        heading_label.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)
        document_name_label.grid(padx=5, pady=5)
        self._document_name_entry.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        user_input_data_label.grid(padx=5, pady=5)
        self._user_input_data_entry.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        placeholder_label.grid(padx=5, pady=5)
        self._placeholder_entry.grid(row=3, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        instruction_label.grid(padx=5, pady=5)
        self._instruction_entry.grid(row=4, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        button.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        button2.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)


