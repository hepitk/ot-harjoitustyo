from tkinter import *
from tkinter import Tk, ttk, constants
from services.program_service import program_service
from docx import Document


class CreateDocumentView:
    def __init__(self, root, handle_show_main_view, filename):
        self._root = root
        self._handle_show_main_view = handle_show_main_view
        self._frame = None
        self._frame2 = None
        self._canvas = None
        self._scrollbar = None
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
            print("Asiakirja valmis.docx luotu kansioon /valmiit asiakirjat. " + str(replaced_words) + " paikkatietomerkintää korvattu.", flush=True)
        else:
            print("Asiakirjapohjaa ei löydy kansiosta. Lisää asiakirjapohja nimeltä " + self._filename + ".docx kansioon /asiakirjapohjat.", flush=True)

    def _mouse_scroll(self, event):
        self._canvas.yview_scroll(-1 * int((event.delta / 110)), "units")

    def _initialize(self):
        document_entries = program_service.find_document_entries(self._filename)

        self._frame = ttk.Frame(master=self._root)
        self._frame.pack(fill=BOTH, expand = 1)

        self._canvas = Canvas(self._frame, height=660)
        self._canvas.pack(side=LEFT, fill=BOTH, expand=1)

        self._scroll_bar = ttk.Scrollbar(self._frame, orient=VERTICAL, command=self._canvas.yview)
        self._scroll_bar.pack(side=RIGHT, fill=Y)

        self._canvas.configure(yscrollcommand=self._scroll_bar.set)
        self._canvas.bind("<Configure>", lambda e: self._canvas.configure(scrollregion= self._canvas.bbox("all")))
        self._canvas.bind_all("<MouseWheel>", self._mouse_scroll)

        self._frame2 = ttk.Frame(self._canvas)

        self._canvas.create_window((0,0), window=self._frame2, anchor="nw")

        heading_label = ttk.Label(self._frame2, text="Täytä asiakirjapohja", font="font=TkHeadingFont 16 bold")
        
        for entry in range(0, len(document_entries)):
            self._gui_components.append(ttk.Label(self._frame2, text=(document_entries[entry].user_input_data) + ", korvaa paikkatiedon:"))                        
            self._gui_components.append(ttk.Label(self._frame2, text=(document_entries[entry].placeholder)))
            self._gui_components.append(ttk.Entry(self._frame2, width=60))

        button = ttk.Button(
            self._frame2,
            text="Täytä",
            command=self._handle_button_click,
            width=60
            )

        button2 = ttk.Button(
            self._frame2,
            text="Palaa alkuvalikkoon",
            command=self._handle_show_main_view,
            width=60
            )
        
        heading_label.grid(columnspan=2, padx=5, pady=5)
        for entry in range(0, len(self._gui_components)):
            self._gui_components[entry].grid(columnspan=2, sticky=(constants.W,constants.E), padx=5, pady=5)
        if (self._filename != "Lisää ensin täyttötietoja"):
            button.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)
        button2.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)
