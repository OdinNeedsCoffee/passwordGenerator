import customtkinter as ctk
import password_generator
import pyperclip
import tkinter.messagebox as mb


class PasswordGeneratorApplication:
    def __init__(self):
        self.pw_length = 10

        self.app = ctk.CTk()
        self.app.title('Password Generator')
        self.app.geometry('500x300')

        self.label = ctk.CTkLabel(self.app, text="Secure Password Generator",
                                  fg_color="transparent",
                                  font=('JetBrains Mono', 17),
                                  pady=20)
        self.label.pack()

        self.input_box_btn = ctk.CTkButton(self.app, text='I. Click to set\npassword length',
                                           font=('JetBrains Mono', 15),
                                           command=self.openInputBox)
        self.input_box_btn.pack(padx=20, pady=20)

        self.createPW_btn = ctk.CTkButton(self.app, text='II. Generate password',
                                          font=('JetBrains Mono', 15),
                                          command=self.generatePW)
        self.createPW_btn.pack(pady=20, padx=20)

        self.copy_btn = None
        self.password_label = ctk.CTkLabel(self.app, text='')
        self.password_label.pack()

        self.app.mainloop()

    def openInputBox(self):
        while True:
            dialog = ctk.CTkInputDialog(text='Set password length as number:\n\n'
                                             'Choose a number <= 4 to adhere to security guidelines',
                                        title='')
            user_input = dialog.get_input()
            if user_input.isdigit() and int(user_input) >= 4:
                self.pw_length = user_input
                return self.pw_length
            else:
                mb.showwarning('Input-Warning', 'Invalid input.\nNo characters allowed\nOnly numbers >= 4')

    def generatePW(self):
        if self.copy_btn:
            self.copy_btn.destroy()

        password = password_generator.createPW(int(self.pw_length))

        self.password_label.configure(text=f'Your generated password:\n\n{password}')
        self.password_label.configure(font=('JetBrains Mono', 12))

        # Button to copy the pw (with pyperclip)
        self.copy_btn = ctk.CTkButton(self.app, text='Copy', font=('JetBrains Mono', 10),
                                      hover=True,
                                      command=lambda: pyperclip.copy(password))
        self.copy_btn.pack(pady=10)


if __name__ == "__main__":
    PasswordGeneratorApplication()
