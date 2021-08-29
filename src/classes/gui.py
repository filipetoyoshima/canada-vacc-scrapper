import tkinter as tk
from PIL import ImageTk, Image
import os


_dir_name = os.path.dirname(os.path.abspath(__file__))
CHECK_ICON_LOCATION = _dir_name + '/../imgs/check_icon.png'
CROSS_ICON_LOCATION = _dir_name + '/../imgs/cross_icon.png'


class Gui:
    def __init__(self, approved:list, disapproved:list, searches:list):
        self.root = tk.Tk()
        self.root.title('Canada Aproved / Not Approved Vaccines')
        self.approved = approved
        self.disapproved = disapproved
        self.searches = searches
        self.good_icon = ImageTk.PhotoImage(Image.open(CHECK_ICON_LOCATION).resize((25, 25), Image.ANTIALIAS))
        self.bad_icon = ImageTk.PhotoImage(Image.open(CROSS_ICON_LOCATION).resize((25, 25), Image.ANTIALIAS))

        for i, vacc_name in enumerate(approved):
            img_label = tk.Label(self.root, image=self.good_icon)
            img_label.grid(column=0, row=i)
            txt_label = tk.Label(text=vacc_name).grid(column=1, row=i, padx=70)

        for i, vacc_name in enumerate(disapproved):
            img_label = tk.Label(self.root, image=self.bad_icon).grid(column=2, row=i)
            txt_label = tk.Label(text=vacc_name).grid(column=3, row=i, padx=70)

        result_row = max(len(self.approved), len(self.disapproved)) + 1
        space_label = tk.Label(self.root, pady=2, padx=250, background='black', font=("Halvetica", 1)).grid(column=0, columnspan=4, row=result_row)
        result_row += 1

        for i, result in enumerate(searches):
            color = 'red'
            fg = 'white'
            if result[1]:
                color = 'green'
                fg = 'black'
            tk.Label(self.root, text=result[0], background=color, fg=fg).grid(column=0, columnspan=4, row=(result_row + i))

        result_row += len(searches)

        tk.Button(self.root, text='Thanks!', padx=50, command=self.root.quit).grid(column=0, columnspan=4, row=result_row)
        

    def mainloop(self):
        self.root.mainloop()


if __name__ == '__main__':
    approved = ['A boa', 'A melhor']
    disapproved = ['Meia boca', 'Cloroquina', 'Vermífugo']
    searches = [('vacina', True), ('anti-vax', False)]
    gui = Gui(approved, disapproved, searches)
    gui.mainloop()

# if __name__ == '__main__':
#     print('getcwd:      ', os.path.dirname(os.path.abspath(__file__)))
#     print('__file__:    ', __file__)