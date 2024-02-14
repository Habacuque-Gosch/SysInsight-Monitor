from tkinter import *
import tkinter  as ttk
import customtkinter as ctk
import psutil
import os


tela = ctk.CTk()



class Application():
    # CLASSE RESPONSÁVEL POR TODA A APLICAÇÃO
    def __init__(self):
        self.tela = tela
        self.tema()
        self.layout()
        self.funcoes_da_aplicacao()
        self.tela.mainloop()

    @staticmethod
    def tema():
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

    def layout(self):
        self.tela.geometry("180x200")
        self.tela.title("HBS")
        self.tela.iconbitmap("medias/cpu.ico")
        self.tela.resizable(width=False, height=False)
        self.tela.config(bg="#0F0D0D")

    @staticmethod
    def funcoes_da_aplicacao():
        alf_img = PhotoImage(file="medias/alf.png")

        def fixar():
            tela.attributes('-alpha', 0.6)
            alf_img_label.place(x=500)
            alf_img_label1.place(x=145, y=10)

        alf_img_label = ctk.CTkButton(master=tela, image=alf_img, text="", fg_color="#0F0D0D", bg_color="#0F0D0D", hover=None, command=fixar, width=15, height=15)
        alf_img_label.place(x=145, y=10)

        def desfixar():
            tela.attributes('-alpha', 1.0)
            alf_img_label1.place(x=500)
            alf_img_label.place(x=145, y=10)
            
        alf_img_label1 = ctk.CTkButton(master=tela, image=alf_img, text="", fg_color="#0F0D0D", bg_color="#0F0D0D", hover=None, command=desfixar, width=15, height=15)


        cpu_img = PhotoImage(file="medias/cpu.png")
        cpu_img_label = ctk.CTkLabel(master=tela, image=cpu_img, text="",fg_color="#0F0D0D")
        cpu_img_label.place(x=18, y=10)

        cpu_use_label = ctk.CTkLabel(master=tela, text="", font=('krona_one', 14, 'bold'), fg_color="#0F0D0D", width=0, height=0)
        cpu_use_label.place(x=80, y=25)
    
        def cpu_usage():
            cpu = psutil.cpu_percent(1)
            tela.update()
            cpu_use_label.configure(text=f"{cpu}%")
            cpu_use_label.after(60, cpu_usage)
        cpu_usage()

        ram_img = PhotoImage(file="medias/ram.png")
        ram_img_label = ctk.CTkLabel(master=tela, image=ram_img, text="",fg_color="#0F0D0D")
        ram_img_label.place(x=22, y=80)

        ram_use_label = ctk.CTkLabel(master=tela, text="", font=('krona_one', 14, 'bold'), fg_color="#0F0D0D", width=0, height=0)
        ram_use_label.place(x=80, y=95)

        def ram_usage():
            ram = psutil.virtual_memory()[2]
            ram_use_label.configure(text=f"{ram}%")
            ram_use_label.after(60, ram_usage)
        ram_usage()

        gpu_img = PhotoImage(file="medias/gpu.png")
        gpu_img_label = ctk.CTkLabel(master=tela, image=gpu_img, text="",fg_color="#0F0D0D")
        gpu_img_label.place(x=18, y=145)

        # def gpu_usage():

        #     gpu_img = PhotoImage(file="medias/cpu.png")
        #     gpu_img_label = ctk.CTkLabel(master=tela, image=gpu_img, text="",fg_color="#0F0D0D")
        #     gpu_img_label.place(x=18, y=10)

        #     gpu = psutil.cpu_percent(4)
        
        #     gpu_use_label = ctk.CTkLabel(master=tela, text=f"{gpu}%", font=('krona_one', 14, 'bold'), fg_color="#0F0D0D", width=0, height=0)
        #     gpu_use_label.place(x=80, y=25)
        #     gpu_use_label.after(250, gpu_usage)

Application()