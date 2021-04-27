from tkinter import Tk, ttk, constants
from services.program_service import program_service
from docx import Document


class CreateDocumentView:
    def __init__(self, root, handle_show_main_view, filename):
        self._root = root
        self._handle_show_main_view = handle_show_main_view
        self._frame = None
        self._filename = filename
        self._gui_components = []

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()
    
    def _handle_button_click(self):
        document = Document("asiakirjapohjat/" + self._filename + ".docx")
        user_input = []
        placeholder = []
        for entry in self._gui_components[2::3]:
            user_input.append(entry.get())        
        for entry in self._gui_components[1::3]:
            placeholder.append(entry.cget("text"))        
        for entry in range(0, len(user_input)):
            program_service.replace_words (document, user_input[entry], placeholder[entry])        
        print(f"Täyttö tehty ja valmis.docx asiakirja luotu.")

    def _initialize(self):
        # if filename = "Lisää täyttötietoja" ERROR!
        document_entries = program_service.find_document_entries(self._filename)
        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(master=self._frame, text="Täytä asiakirjapohja")

        for entry in range(0, len(document_entries)):
            self._gui_components.append(ttk.Label(master=self._frame, text=document_entries[entry].user_input_data))                        
            self._gui_components.append(ttk.Label(master=self._frame, text=document_entries[entry].placeholder))
            self._gui_components.append(ttk.Entry(master=self._frame))
            #gui_components.append(ttk.Label(master=self._frame, text=document_entries[entry].instruction))

        button = ttk.Button(
            master=self._frame,
            text="Täytä",
            command=self._handle_button_click
            )

        button2 = ttk.Button(
            master=self._frame,
            text="Palaa alkuvalikkoon",
            command=self._handle_show_main_view
            )

        heading_label.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)        
        for entry in range(0, len(self._gui_components)):
            self._gui_components[entry].grid(columnspan=2, sticky=constants.W, padx=5, pady=5)
        button.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)
        button2.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)