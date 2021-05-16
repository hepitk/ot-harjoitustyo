from tkinter import Tk
from initialize_database import initialize_database
from ui.ui import UI


def main():
    initialize_database()
    window = Tk()
    window.title("TÄTI")

    u_int = UI(window)
    u_int.start()

    window.mainloop()


if __name__ == "__main__":
    main()
