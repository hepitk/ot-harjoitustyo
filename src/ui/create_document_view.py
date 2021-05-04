from tkinter import Tk, ttk, constants, Scrollbar
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
        if program_service.document_exists(self._filename):
            document = Document("asiakirjapohjat/" + self._filename + ".docx")
            user_input = []
            placeholder = []
            replaced_words = 0
            for entry in self._gui_components[2::3]:
                user_input.append(entry.get())        
            for entry in self._gui_components[1::3]:
                placeholder.append(entry.cget("text"))        
            for entry in range(0, len(user_input)):
                replaced_words += program_service.replace_words (document, user_input[entry], placeholder[entry])        
            print("Täyttö tehty ja valmis.docx asiakirja luotu. " + str(replaced_words) + " paikkatietomerkintää korvattu.", flush=True)
        else:
            print("Asiakirjapohjaa ei löydy kansiosta. Lisää asiakirjapohja nimeltä " + self._filename + ".docx kansioon /asiakirjapohjat.", flush=True)

    def _initialize(self):
        document_entries = program_service.find_document_entries(self._filename)
        #scroll_bar = ttk.Scrollbar(master=self._frame, orient="vertical")
        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(master=self._frame, text="Täytä asiakirjapohja", font="font=TkHeadingFont 16 bold")
        
        for entry in range(0, len(document_entries)):
            self._gui_components.append(ttk.Label(master=self._frame, text=(document_entries[entry].user_input_data) + ", korvaa paikkatiedon:"))                        
            self._gui_components.append(ttk.Label(master=self._frame, text=(document_entries[entry].placeholder)))
            self._gui_components.append(ttk.Entry(master=self._frame, width=50))

        button = ttk.Button(
            master=self._frame,
            text="Täytä",
            command=self._handle_button_click,
            width=50
            )

        button2 = ttk.Button(
            master=self._frame,
            text="Palaa alkuvalikkoon",
            command=self._handle_show_main_view,
            width=50
            )

        heading_label.grid(columnspan=2, padx=5, pady=5)
        #scroll_bar.grid(row=0, column=2)
        for entry in range(0, len(self._gui_components)):
            self._gui_components[entry].grid(columnspan=2, sticky=(constants.W,constants.E), padx=5, pady=5)
        if (self._filename != "Lisää ensin täyttötietoja"):
            button.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)
        button2.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)