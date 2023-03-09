from View import View, tk
from Model import Model

if __name__ == '__main__':
    root = tk.Tk()  # root object (pop up window)
    view = View(root)
    view.grid(column=0, row=1)
    root.mainloop()

    model = Model()
    model.sendToVehicle("Please print this", 10)



