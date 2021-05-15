#from tkinter import *
from tkinter import Tk, ttk, constants, StringVar
from services.program_service import program_service
from services.document_handler import document_handler


class SettingsView:
    def __init__(self, root, handle_show_main_view):
        self._root = root
        self._handle_show_main_view = handle_show_main_view
        self._font_name_variable = None        
        self._font_name_label = None
        self._font_size_variable = None
        self._font_size_label = None
        self._change_font_name_entry = None
        self._change_font_size_entry = None
        self._frame = None
        self._message_variable = None
        self._message_label = None
        
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()
    
    def _is_integer(self):
        try:
            int(self._change_font_size_entry.get())
            return True
        except ValueError:
            self._show_message("Fontin koon on oltava numero!")
            return False

    def _handle_button_click(self):
        if self._change_font_name_entry.get() != "" and self._change_font_size_entry.get() != "":
            try:
                int(self._change_font_size_entry.get())
                if document_handler.set_font(self._change_font_name_entry.get(), int(self._change_font_size_entry.get())) and self._change_font_name_entry.get() != "":
                    self._font_name_variable.set("Asetettu fontti: " + self._change_font_name_entry.get())
                    self._font_size_variable.set("Asetettu fonttikoko: " + str(self._change_font_size_entry.get()))
                    self._show_message("Uusi fontti asetettu")
            except ValueError:
                self._show_message("Fontin koon on oltava numero!")
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

        heading_label = ttk.Label(master=self._frame, text="Asetukset", font="font=TkHeadingFont 16 bold")
        
        self._font_name_variable = StringVar(self._frame)
        self._font_name_variable.set("Asetettu fontti: " + document_handler.font_name)
        self._font_name_label = ttk.Label(master=self._frame, textvariable=self._font_name_variable, font="font=TkHeadingFont 10 bold")
        self._font_size_variable = StringVar(self._frame)
        self._font_size_variable.set("Asetettu fonttikoko: " + str(document_handler.font_size))
        self._font_size_label = ttk.Label(master=self._frame, textvariable=self._font_size_variable, font="font=TkHeadingFont 10 bold")

        change_font_name_label = ttk.Label(master=self._frame, text="Vaihda fontti: ")
        self._change_font_name_entry = ttk.Entry(master=self._frame)
        change_font_size_label = ttk.Label(master=self._frame, text="Vaihda fonttikoko: ")
        self._change_font_size_entry = ttk.Entry(master=self._frame)

        button = ttk.Button(
            master=self._frame,
            text="Vaihda fontti ja fonttikoko",
            command=self._handle_button_click
            )
        
        button2 = ttk.Button(
            master=self._frame,
            text="Palaa alkuvalikkoon",
            command=self._handle_show_main_view
            )
                
        heading_label.grid(columnspan=2, padx=5, pady=5, sticky=constants.W)
        self._font_name_label.grid(padx=5, pady=5)
        self._font_size_label.grid(padx=5, pady=5)
        change_font_name_label.grid(padx=5, pady=5)        
        self._change_font_name_entry.grid(row=3, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        change_font_size_label.grid(padx=5, pady=5)
        self._change_font_size_entry.grid(row=4, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        button.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        button2.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        self._message_label.grid(columnspan= 2, padx=5, pady=5, sticky=(constants.E, constants.W))
        self._hide_message()
        self._frame.grid_columnconfigure(1, weight=1, minsize=400)




