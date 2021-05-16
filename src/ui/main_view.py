from tkinter import ttk, StringVar, constants, OptionMenu
from services.program_service import program_service


class MainView:
    def __init__(self,root, handle_show_create_replace_data_view, handle_show_create_document_view,
        handle_show_delete_replace_data_view, handle_show_settings_view):

        self._root = root
        self._handle_show_create_replace_data_view = handle_show_create_replace_data_view
        self._handle_show_create_document_view = handle_show_create_document_view
        self._handle_show_delete_replace_data_view = handle_show_delete_replace_data_view
        self._handle_show_settings_view = handle_show_settings_view
        self._frame = None
        self._document_name_variable = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        document_names = program_service.find_all_document_names()

        if not document_names:
            document_names.append("Lisää ensin täyttötietoja")
        if len(document_names) > 1 and "Lisää ensin täyttötietoja" in document_names:
            document_names.remove("Lisää ensin täyttötietoja")

        self._frame = ttk.Frame(master=self._root)
        self._document_name_variable = StringVar(self._frame)
        self._document_name_variable.set(document_names[0])

        program_heading_label = ttk.Label(
            master=self._frame,
            text="TÄTI – Täyttöbotti",
            font="TkHeadingFont 20 bold italic"
        )

        add_remove_heading_label = ttk.Label(
            master=self._frame,
            text="Lisää / Poista täyttötietoja",
            font="TkHeadingFont 16 bold"
        )

        add_button = ttk.Button(
            master=self._frame,
            text="Lisää",
            command=self._handle_show_create_replace_data_view, width=50
        )

        remove_button = ttk.Button(
            master=self._frame,
            text="Poista",
            command=self._handle_show_delete_replace_data_view,
            width=50
        )

        fill_heading_label = ttk.Label(
            master=self._frame,
            text="Täytä asiakirjapohja",
            font="TkHeadingFont 14 bold"
        )

        document_name_heading_label = ttk.Label(
            master=self._frame,
            text="Asiakirjapohjan nimi:"
        )

        document_name_entry = OptionMenu(
            self._frame,
            self._document_name_variable,
            *document_names
        )

        choose_document_button = ttk.Button(master=self._frame,
            text="Valitse asiakirjapohja",
            command=self._handle_show_create_document_view,
            width=50
        )

        settings_heading_label = ttk.Label(
            master=self._frame,
            text="Asetukset",
            font="TkHeadingFont 12 bold"
        )

        settings_button = ttk.Button(
            master=self._frame,
            text="Asetukset",
            command=self._handle_show_settings_view,
            width=50
        )


        program_heading_label.grid(columnspan=2, padx=5, pady=10)

        add_remove_heading_label.grid(
            columnspan=2,
            sticky=(constants.W, constants.E),
            padx=5,
            pady=5
        )

        add_button.grid(
            columnspan=2,
            sticky=(constants.W, constants.E),
            padx=5,
            pady=5
        )

        remove_button.grid(
            columnspan=2,
            sticky=(constants.W, constants.E),
            padx=5,
            pady=5
        )

        fill_heading_label.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)

        document_name_heading_label.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)

        document_name_entry.grid(sticky=constants.W, padx=5, pady=5)

        choose_document_button.grid(
            columnspan=2,
            sticky=(constants.W, constants.E),
            padx=5,
            pady=5
        )

        settings_heading_label.grid(columnspan=2, sticky=constants.W, padx=5, pady=10)

        settings_button.grid(
            columnspan=2,
            sticky=(constants.W, constants.E),
            padx=5,
            pady=5
        )
