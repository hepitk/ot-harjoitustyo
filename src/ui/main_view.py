from tkinter import Tk, ttk, StringVar, constants, OptionMenu
from services.program_service import program_service


class MainView:
    def __init__(self, root, handle_show_create_replace_data_view, handle_show_create_document_view, handle_show_delete_replace_data_view):
        self._root = root
        self._handle_show_create_replace_data_view = handle_show_create_replace_data_view
        self._handle_show_create_document_view = handle_show_create_document_view
        self._handle_show_delete_replace_data_view = handle_show_delete_replace_data_view
        self._frame = None
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

        program_heading_label = ttk.Label(master=self._frame, text="TÄTI – Täyttöbotti", font="TkHeadingFont 20 bold italic")
        heading_label = ttk.Label(master=self._frame, text="Lisää täyttötietoja", font="TkHeadingFont 16 bold")
        button = ttk.Button(master=self._frame, text="Lisää", command=self._handle_show_create_replace_data_view, width=50)

        heading_label2 = ttk.Label(master=self._frame, text="Poista täyttötietoja", font="TkHeadingFont 14 bold")
        button2 = ttk.Button(master=self._frame, text="Poista", command=self._handle_show_delete_replace_data_view, width=50)

        heading_label3 = ttk.Label(master=self._frame, text="Täytä asiakirjapohja", font="TkHeadingFont 14 bold")
        heading_label4 = ttk.Label(master=self._frame, text="Asiakirjapohjan nimi:")
        document_name_entry = OptionMenu(self._frame, self._document_name_variable, *document_names)
        button3 = ttk.Button(master=self._frame, text="Valitse asiakirjapohja", command=self._handle_show_create_document_view, width=50)
        
        program_heading_label.grid(columnspan=2, padx=5, pady=10)
        heading_label.grid(columnspan=2, sticky=(constants.W, constants.E), padx=5, pady=5)
        button.grid(columnspan=2, sticky=(constants.W, constants.E), padx=5, pady=5)
        heading_label2.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)
        button2.grid(columnspan=2, sticky=(constants.W, constants.E), padx=5, pady=5)
        heading_label3.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)
        heading_label4.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)       
        document_name_entry.grid(sticky=constants.W, padx=5, pady=5)
        button3.grid(columnspan=2, sticky=(constants.W, constants.E), padx=5, pady=5)
