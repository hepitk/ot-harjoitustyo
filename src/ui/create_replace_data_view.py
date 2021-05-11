from tkinter import Tk, ttk, constants, StringVar
from services.program_service import program_service


class CreateReplaceDataView:
    def __init__(self, root, handle_show_main_view):
        self._root = root
        self._handle_show_main_view = handle_show_main_view
        self._document_name_entry = None
        self._user_input_data_entry = None
        self._placeholder_entry = None
        self._frame = None
        self._message_variable = None
        self._message_label = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _handle_button_click(self):
        if self._document_name_entry.get() != "" and self._user_input_data_entry.get() != "" and self._placeholder_entry.get() != "" and not program_service.placeholder_duplicate_exists(self._document_name_entry.get(), self._placeholder_entry.get()):
            program_service.create_replace_data(
                self._document_name_entry.get(),
                self._user_input_data_entry.get(),
                self._placeholder_entry.get()
                )
            self._show_message("Täyttötieto luotu")
        elif program_service.placeholder_duplicate_exists(self._document_name_entry.get(), self._placeholder_entry.get()):
            self._show_message("Samaa täyttötietoa ei voi lisätä kahteen kertaan!")
        else:
            self._show_message("Mikään kenttä ei saa olla tyhjä!")

    def _show_message(self, message):
        self._message_variable.set(message)
        self._message_label.grid()

    def _hide_message(self):
        self._message_label.grid_remove()
        
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._message_variable = StringVar(self._frame)
        self._message_label = ttk.Label(master=self._frame, textvariable=self._message_variable, foreground="red")

        heading_label = ttk.Label(master=self._frame, text="Lisää täyttötietoja", font="font=TkHeadingFont 16 bold")

        document_name_label = ttk.Label(master=self._frame, text="Asiakirjapohjan nimi:")
        self._document_name_entry = ttk.Entry(master=self._frame)

        user_input_data_label = ttk.Label(master=self._frame, text="Täytettävän tiedon tyyppi:")
        self._user_input_data_entry = ttk.Entry(master=self._frame)

        placeholder_label = ttk.Label(master=self._frame, text="Paikkatietomerkintä:")
        self._placeholder_entry = ttk.Entry(master=self._frame)

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
                
        heading_label.grid(columnspan=2, padx=5, pady=5, sticky=constants.W)
        document_name_label.grid(padx=5, pady=5)
        self._document_name_entry.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        user_input_data_label.grid(padx=5, pady=5)
        self._user_input_data_entry.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        placeholder_label.grid(padx=5, pady=5)
        self._placeholder_entry.grid(row=3, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        button.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        button2.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        self._message_label.grid(columnspan= 2, padx=5, pady=5, sticky=(constants.E, constants.W))
        self._hide_message()
        self._frame.grid_columnconfigure(1, weight=1, minsize=400)




