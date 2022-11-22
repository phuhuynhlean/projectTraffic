import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('420x200')

        frm = tk.Frame(self)

        self.var = tk.StringVar()

        ent = tk.Entry(frm, textvariable=self.var, fg='black', bg='white')
        lst = tk.Listbox(frm, bd=0, bg='white')

        item_list = ('Big Dog', 'Big Cat', 'big bird', 'Small Bird', 'Small Fish', 'Little Insect', 'Long Snake')

        ent.grid(sticky=tk.EW)
        frm.grid(sticky=tk.NW)

        def get_input(*args):
            lst.delete(0, tk.END)
            string = self.var.get()

            if string:
                for item in item_list:
                    if item.startswith(string):
                        lst.insert(tk.END, item)
                        lst.itemconfigure(tk.END, foreground="black")

                for item in item_list:
                    if item.startswith(string):
                        lst.grid(sticky=tk.NSEW)
                    elif not lst.get(0):
                        lst.grid_remove()
            else:
                lst.grid_remove()

        def list_hide(e=None):
            lst.delete(0, tk.END)
            lst.grid_remove()

        def list_input(_):
            lst.focus()
            lst.select_set(0)

        def list_up(_):
            if not lst.curselection()[0]:
                ent.focus()
                list_hide()

        def get_selection(_):
            value = lst.get(lst.curselection())
            self.var.set(value)
            list_hide()
            ent.focus()
            ent.icursor(tk.END)

        self.var.trace('w', get_input)

        ent.bind('<Down>', list_input)
        ent.bind('<Return>', list_hide)

        lst.bind('<Up>', list_up)
        lst.bind('<Return>', get_selection)


def main():
    app = App()
    app.mainloop()


if __name__ == '__main__':
    main() 