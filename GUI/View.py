import customtkinter as CTk
from Controller import Controller
import tkinter as Tk
# import pickle


# inherits from CTK's frame class and calls that constructor
class View(CTk.CTkFrame):
    def __init__(self, root, master, **kwargs):
        super().__init__(master, **kwargs)
        CTk.set_appearance_mode("dark")

        # labels for each widget
        left_servo_label = CTk.CTkLabel(master=root, text="Left Thruster Angle", anchor="w")
        left_thruster_label = CTk.CTkLabel(master=root, text="Left Thruster Power", anchor="w")
        right_servo_label = CTk.CTkLabel(master=root, text="Right Thruster Angle", anchor="w")
        right_thruster_label = CTk.CTkLabel(master=root, text="Right Thruster", anchor="w")
        tail_servo_label = CTk.CTkLabel(master=root, text="Tail Thruster Angle", anchor="w")
        tail_thruster_label = CTk.CTkLabel(master=root, text="Tail Thruster", anchor="w")
        motor_status_label = CTk.CTkLabel(master=root, text="Motor Status", anchor="w")
        flight_mode_label = CTk.CTkLabel(master=root, text="Flight Mode", anchor="w")

        # slider widgets
        self.left_servo_slider = CTk.CTkSlider(master=root, from_=0, to=1, orientation="vertical")
        self.left_servo_slider.bind("<ButtonRelease-1>", self.get_left_servo)
        self.left_thruster_slider = CTk.CTkSlider(master=root, from_=0, to=1, orientation="vertical")
        self.left_thruster_slider.bind("<ButtonRelease-1>", self.get_left_thruster)
        self.right_servo_slider = CTk.CTkSlider(master=root, from_=0, to=1, orientation="vertical")
        self.right_servo_slider.bind("<ButtonRelease-1>", self.get_right_servo)
        self.right_thruster_slider = CTk.CTkSlider(master=root, from_=0, to=1, orientation="vertical")
        self.right_thruster_slider.bind("<ButtonRelease-1>", self.get_right_thruster)
        self.tail_servo_slider = CTk.CTkSlider(master=root, from_=-0, to=1, orientation="vertical")
        self.tail_servo_slider.bind("<ButtonRelease-1>", self.get_tail_servo)
        self.tail_thruster_slider = CTk.CTkSlider(master=root, from_=0, to=1, orientation="vertical")
        self.tail_thruster_slider.bind("<ButtonRelease-1>", self.get_tail_thruster)

        # combo box widgets
        motor_status = CTk.CTkOptionMenu(master=root, values=["Disarmed", "Armed"])
        flight_mode = CTk.CTkOptionMenu(master=root,
                                        values=["Manual", "Stabilize", "Acro", "Altitude Hold", "Auto", "Guided",
                                                "Circle", "Surface", "Position Hold"])
        # switch widget variables
        self.left_gripper_state = CTk.StringVar(value="open")
        self.right_gripper_state = CTk.StringVar(value="open")

        # switch widgets
        self.left_gripper_switch = CTk.CTkSwitch(master=root, text="Open Left Gripper", command=self.get_left_gripper,
                                                 variable=self.left_gripper_state, onvalue="open", offvalue="closed",
                                                 switch_width=75)
        self.right_gripper_switch = CTk.CTkSwitch(master=root, text="Open Right Gripper",
                                                  command=self.get_right_gripper,
                                                  variable=self.right_gripper_state, onvalue="open", offvalue="closed",
                                                  switch_width=75)

        # button widgets
        self.reset_state = CTk.CTkButton(master=root, text="Reset State", command=self.set_state_default)
        self.previous_state = CTk.CTkButton(master=root, text="Previous State", command=self.set_state_previous)

        # widget and label placements within frame
        motor_status_label.grid(column=0, row=0, pady=15)
        motor_status.grid(column=0, row=1, sticky="N", padx=15)

        flight_mode_label.grid(column=1, row=0, pady=15)
        flight_mode.grid(column=1, row=1, sticky="N", padx=15)

        self.reset_state.grid(column=2, row=0)
        self.previous_state.grid(column=3, row=0)

        self.left_gripper_switch.grid(column=2, row=1, padx=15)
        self.right_gripper_switch.grid(column=3, row=1, padx=15)

        left_servo_label.grid(column=2, row=2)
        self.left_servo_slider.grid(column=2, row=3, rowspan=3)

        left_thruster_label.grid(column=3, row=2, padx=10)
        self.left_thruster_slider.grid(column=3, row=3, rowspan=3, padx=10)

        right_servo_label.grid(column=2, row=6)
        self.right_servo_slider.grid(column=2, row=7, rowspan=3)

        right_thruster_label.grid(column=3, row=6, padx=10)
        self.right_thruster_slider.grid(column=3, row=7, rowspan=3, padx=10)

        tail_servo_label.grid(column=2, row=10)
        self.tail_servo_slider.grid(column=2, row=11, rowspan=3)

        tail_thruster_label.grid(column=3, row=10, padx=10)
        self.tail_thruster_slider.grid(column=3, row=11, rowspan=3, padx=10)

        self.controller = Controller()
        self.controller.start_gcs_connection()

    def get_left_servo(self, event):
        print(self.left_servo_slider.get())
        command = self.controller.createCommand("a1", self.left_servo_slider.get())
        self.controller.sendToModel(command)

    def get_right_servo(self, event):
        print(self.right_servo_slider.get())
        command = self.controller.createCommand("a2", self.right_servo_slider.get())
        self.controller.sendToModel(command)

    def get_tail_servo(self, event):
        print(self.tail_servo_slider.get())
        command = self.controller.createCommand("a3", self.tail_servo_slider.get())
        self.controller.sendToModel(command)

    def get_left_thruster(self, event):
        print(self.left_thruster_slider.get())

    def get_right_thruster(self, event):
        print(self.right_thruster_slider.get())

    def get_tail_thruster(self, event):
        print(self.tail_thruster_slider.get())

    def get_left_gripper(self):
        print(self.left_gripper_state.get())
        command = self.controller.createCommand("g1", self.left_gripper_state.get())
        self.controller.sendToModel(command)

    def get_right_gripper(self):
        print(self.right_gripper_state.get())
        command = self.controller.createCommand("g2", self.right_gripper_state.get())
        self.controller.sendToModel(command)

    def set_state_default(self):
        self.left_servo_slider.set(0.5)
        self.right_servo_slider.set(0.5)
        self.tail_servo_slider.set(0.5)
        self.left_thruster_slider.set(0.5)
        self.right_thruster_slider.set(0.5)
        self.tail_thruster_slider.set(0.5)
        self.left_gripper_state.set("closed")
        self.right_gripper_state.set("closed")
        commands = self.controller.create_commands("a1", self.left_servo_slider.get(), "a2",
                                                   self.right_servo_slider.get(), "a3", self.tail_servo_slider.get(),
                                                   "g1", self.left_gripper_state.get(),
                                                   "g2", self.left_gripper_state.get())
        self.controller.sendToModel(commands)

    def set_state_previous(self):
        self.left_gripper_state.set("closed")
        self.right_gripper_state.set("closed")
        self.left_servo_slider.set(0)
        self.right_servo_slider.set(0)
        self.tail_servo_slider.set(0)
        self.left_thruster_slider.set(0.5)
        self.right_thruster_slider.set(0.5)
        self.tail_thruster_slider.set(0.5)
