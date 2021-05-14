# Holds UI logic
from tkinter import Tk, ttk
from ui.main_view import MainView
from ui.create_replace_data_view import CreateReplaceDataView
from ui.create_document_view import CreateDocumentView
from ui.delete_replace_data_view import DeleteReplaceDataView
from ui.settings_view import SettingsView

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None        

    def start(self):
        self._show_main_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_main_view(self):
        self._hide_current_view()

        self._current_view = MainView(
            self._root,
            self._show_create_replace_data_view,
            self._show_create_document_view,
            self._show_delete_replace_data_view,
            self._show_settings_view,
        )

        self._current_view.pack()

    def _show_create_replace_data_view(self):
        self._hide_current_view()

        self._current_view = CreateReplaceDataView(
            self._root,
            self._show_main_view,            
        )

        self._current_view.pack()

    def _show_delete_replace_data_view(self):
        self._hide_current_view()

        self._current_view = DeleteReplaceDataView(
            self._root,
            self._show_main_view,            
        )

        self._current_view.pack()

    def _show_create_document_view(self):
        document_name_variable = self._current_view._document_name_variable.get()

        self._hide_current_view()

        self._current_view = CreateDocumentView(
            self._root,
            self._show_main_view,
            document_name_variable              
        )

    def _show_settings_view(self):
        self._hide_current_view()

        self._current_view = SettingsView(
            self._root,
            self._show_main_view,             
        )

        self._current_view.pack()
