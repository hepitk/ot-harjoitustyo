# Class that takes care of replacing placeholders in the documents
import re
from docx import Document

class DocumentHandler:
        
    def docx_replace_regex(self, doc_obj, regex , replace):

        for p in doc_obj.paragraphs:
            if regex.search(p.text):
                inline = p.runs
                # Loop added to work with runs (strings with same style)
                for i in range(len(inline)):
                    if regex.search(inline[i].text):
                        text = regex.sub(replace, inline[i].text)
                        inline[i].text = text

        for table in doc_obj.tables:
            for row in table.rows:
                for cell in row.cells:
                    docx_replace_regex(cell, regex , replace)
