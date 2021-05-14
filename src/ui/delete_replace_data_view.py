from tkinter import *
from tkinter import Tk, ttk, constants
from services.program_service import program_service


class DeleteReplaceDataView:
    def __init__(self, root, handle_show_main_view):
        self._root = root
        self._handle_show_main_view = handle_show_main_view
        self._frame = None
        self._frame2 = None
        self._canvas = None
        self._scrollbar = None
        self._message_variable = None
        self._message_label = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _show_message(self, message):
        self._message_variable.set(message)
        self._message_label.grid()

    def _hide_message(self):
        self._message_label.grid_remove()
    
    def _handle_delete_replace_data(self, filename, placeholder):
        if program_service.delete_replace_data(filename, placeholder):
            self.destroy()
            self._initialize()

    def _mouse_scroll(self, event):
        self._canvas.yview_scroll(-1 * int((event.delta / 110)), "units")
        
    def _initialize(self):
        replace_data_entries = program_service.find_all_replace_data_entries()

        self._frame = ttk.Frame(master=self._root)
        self._frame.pack(fill=BOTH, expand = 1)

        self._canvas = Canvas(self._frame, height=660, width= 700)
        self._canvas.pack(side=LEFT, fill=BOTH, expand=1)

        self._scroll_bar = ttk.Scrollbar(self._frame, orient=VERTICAL, command=self._canvas.yview)
        self._scroll_bar.pack(side=RIGHT, fill=Y)

        self._canvas.configure(yscrollcommand=self._scroll_bar.set)
        self._canvas.bind("<Configure>", lambda e: self._canvas.configure(scrollregion= self._canvas.bbox("all")))
        self._canvas.bind_all("<MouseWheel>", self._mouse_scroll)

        self._frame2 = ttk.Frame(self._canvas)

        self._canvas.create_window((0,0), window=self._frame2, anchor="nw")

        self._message_variable = StringVar(self._frame2)
        self._message_label = ttk.Label(master=self._frame2, textvariable=self._message_variable, foreground="red")

        heading_label = ttk.Label(self._frame2, text="Poista täyttötietoja", font="font=TkHeadingFont 16 bold")

        button = ttk.Button(
            self._frame2,
            text="Palaa alkuvalikkoon",
            command=self._handle_show_main_view,
            width=60
            )

        heading_label.grid(columnspan=2, column=0, padx=5, pady=5, sticky=constants.W)
        for entry in range(0, len(replace_data_entries)):
            ttk.Label(self._frame2, text=(replace_data_entries[entry].filename) + "  |  " + (replace_data_entries[entry].user_input_data) + "  |  " + (replace_data_entries[entry].placeholder)).grid(row=entry+1, column=0, sticky=(constants.E, constants.W), padx=5, pady=5)
            Button(self._frame2, text=f"Poista", command=lambda entry=entry: self._handle_delete_replace_data(replace_data_entries[entry].filename, replace_data_entries[entry].placeholder)).grid(row=entry+1, column= 1, sticky=(constants.E, constants.W), padx=5, pady=5)
        button.grid(columnspan=2, column=0, sticky=(constants.E, constants.W), padx=5, pady=5)
        self._message_label.grid(columnspan= 2, column=0, padx=5, pady=5, sticky=(constants.E, constants.W))
        self._hide_message()
