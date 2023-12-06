
    # Module gestion OS
import os, signal
import shutil
import subprocess
import sys

    # Module requêtes
import requests

    # Module multi-task
from threading import *

    # Module affichage graphique
import tkinter as tk
import customtkinter
from PIL import Image

    # Module Temps
import datetime
from time import sleep

    # Module 7zip
import zipfile

    # Module pour modifier le titre de la fenêtre 
import ctypes

    # Module utiliser des définitions dans les commandes 
from functools import partial

    # Module réseau
import socket

    # Module Mega (download)
from mega import Mega

    # Module permettant de vérifier l'intégrité d'un fichier | Sha256
import hashlib


if getattr(sys, 'frozen', False):
    import pyi_splash

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.build_ui()

    def center(self):
        self.update_idletasks()
        width = self.winfo_width()
        frm_width = self.winfo_rootx() - self.winfo_x()
        win_width = width + 2 * frm_width
        height = self.winfo_height()
        titlebar_height = self.winfo_rooty() - self.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = self.winfo_screenwidth() // 2 - win_width // 2
        y = self.winfo_screenheight() // 2 - win_height // 2
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.deiconify()

    def build_ui(self):
        if getattr(sys, 'frozen', False):
            pyi_splash.close()
        self.geometry("1050x500")
        self.resizable(False,False)
        self.center()

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.title("EBP2023.py | Version "+version_package)

            # Mise en variable path Image 
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "assets")

        try:
            icone = tk.PhotoImage(file=os.path.dirname(os.path.realpath(__file__))+"/assets/EBP2023.png")
            self.iconphoto(True, icone)
        except Exception as e:
            print(e)

            # Set layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

            # Mise en variable LOGO "printer_logo"
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "EBP2023.png")), size=(48, 48))

            # Mise en variable LOGO "ECORIS_LOGO" b&w
        self.large_test_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "ECORIS_LOGO.png")),
                                                        dark_image=Image.open(os.path.join(image_path, "ECORIS_LOGO_3.png")),
                                                        size=(275, 125))
        
    
            # Mise en variable Image "installer" b&w
            # Icone pour : 1er Choix | home_button
        self.installer_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "installer.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "installer.png")), size=(40, 40))

            # Mise en variable Image "soutien-technique" b&w
            # Icone pour : 2nd Choix | support_button
        self.soutien_tech_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "soutien-technique.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "soutien-technique.png")), size=(40, 40))

            # Mise en variable Image "log" b&w
            # Icone pour : 3me Choix | log_button
        self.log_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "log.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "log_black.png")), size=(40, 40))

            # Mise en variable Image "recherche_maj" b&w
            # Icone pour : 4me Choix | update_button
            # Icone pour : 5me Choix | update_windows_button
        self.recherche_maj_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "maj_search.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "maj_search.png")), size=(40, 40))

            # Mise en variable Image "maj_ok" b&w
            # Icone pour : 4me Choix | update_button
            # Icone pour : 5me Choix | update_windows_button
        self.maj_ok_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "maj_ok.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "maj_ok.png")), size=(40, 40))

            # Mise en variable Image "maj_error" b&w
            # Icone pour : 4me Choix | update_button
            # Icone pour : 5me Choix | update_windows_button
        self.maj_error_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "maj_error.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "maj_error.png")), size=(40, 40))
        

            # Mise en variable Image "logiciel" b&w
        self.image_icon_logiciel = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "logiciel.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "logiciel_white.png")), size=(32, 32))

            # Mise en variable Image "soutien_informatique" b&w
        self.image_icon_assistance = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "soutien_technique.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "soutien_technique_black.png")), size=(32, 32))

            # Mise en variable Image "code_source" b&w
        self.image_icon_code_source = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "code_source.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "code_source_black.png")), size=(32, 32))

            # Mise en variable "documentation" b&w
        self.image_icon_documentation = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "documentation.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "documentation_black.png")), size=(32, 32))

            # Mise en variable Image "home" b&w
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(24, 24))
                
            # Mise en variable Image "chat" b&w
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(24, 24))

            # Mise en variable Image "acceptation" b&w
        self.acceptation_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "acceptation.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "acceptation_black.png")), size=(24, 24))

            # Mise en variable Image "refus" b&w
        self.refus_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "refus.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "refus_black.png")), size=(24, 24))

            # Mise en variable Image "trashcan" b&w
        self.trashcan_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "trashcan.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "trashcan_white.png")), size=(24, 24))

            # Mise en variable Image "download" b&w
        self.download_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "download.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "download_white.png")), size=(24, 24))

            # Creéation de la fenêtre de navigation
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(6, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text=" EBP 2023 | V "+version_package, image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Installation",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.installer_image, anchor="w", command=self.home_button_event, font=customtkinter.CTkFont(size=18))
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.support_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Support",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.soutien_tech_image, anchor="w", command=self.support_button_event, font=customtkinter.CTkFont(size=18))
        self.support_button.grid(row=2, column=0, sticky="ew")

        self.log_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Log",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.log_image, anchor="w", command=self.log_button_event, font=customtkinter.CTkFont(size=18))
        self.log_button.grid(row=3, column=0, sticky="ew")

        self.update_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Mise à jour Utilitaire",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.recherche_maj_image, anchor="w", command=self.update_button_event, font=customtkinter.CTkFont(size=18))
        self.update_button.grid(row=4, column=0, sticky="ew")

        self.update_windows_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Mise à jour Windows",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.recherche_maj_image, anchor="w", command=self.update_windows_button_event, font=customtkinter.CTkFont(size=18))
        self.update_windows_button.grid(row=5, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event, font=("",16))
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")


            # Création de la fenêtre "INSTALLATION"
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.large_test_image)
        self.home_frame_large_image_label.place(relx=0.5, rely=0.01, anchor="n")

        self.label_choice = customtkinter.CTkLabel(self.home_frame, text="Choix :", width=100, height=50, font=('Arial',24))
        self.label_choice.place(relx=0.075, rely=0.3, anchor=customtkinter.CENTER)
        
        globals()["self.checkbox_{}".format(0)] = customtkinter.CTkCheckBox(self.home_frame, text="Tout installer", font=('Arial',18), command=partial(self.checkbox_event, EBP_List_Logiciel, "self.checkbox_0"), variable=customtkinter.StringVar(value="off"), onvalue="all", offvalue="off")
        globals()["self.checkbox_{}".format(0)].place(relx=0.075, rely=0.4, anchor="w")

        y=0.47
        for elem in EBP_List_Logiciel:
            globals()["self.checkbox_{}".format(EBP_List_Logiciel.index(elem)+1)] = customtkinter.CTkCheckBox(self.home_frame, text=elem[0], font=('Arial',16), command=partial(self.checkbox_event, elem, "self.checkbox_{}".format(EBP_List_Logiciel.index(elem)+1)), variable=customtkinter.StringVar(value="off"), onvalue=elem[1], offvalue="off")
            globals()["self.checkbox_{}".format(EBP_List_Logiciel.index(elem)+1)].place(relx=0.075, rely=y, anchor="w")
            y+=0.07


        self.separator = customtkinter.CTkFrame(self.home_frame,width=5,height=275,corner_radius=0,fg_color="black")
        self.separator.place(relx=0.5, rely=0.625, anchor="w")

        y=0.45
        for elem in Event_Swtichcase:
            globals()["self.switch_{}".format(Event_Swtichcase.index(elem)+1)] = customtkinter.CTkSwitch(self.home_frame, text=elem[0], font=('Arial',14), command=partial(self.switch_event, elem[0], elem[1], "self.switch_{}".format(Event_Swtichcase.index(elem)+1)), variable=customtkinter.StringVar(value=elem[2]), onvalue="Oui", offvalue="Non", state=elem[3])
            if elem[2] =="Oui":
                 globals()["self.switch_{}".format(Event_Swtichcase.index(elem)+1)].select()
            globals()["self.switch_{}".format(Event_Swtichcase.index(elem)+1)].place(relx=0.53, rely=y, anchor="w")
            y+=0.07

    
        self.start_install_home_button_1 = customtkinter.CTkButton(self.home_frame, text="Installer", font=('Arial',20), width=250, image=self.image_icon_logiciel, compound="left", state="disabled", command=self.ebp_valid_install)
        self.start_install_home_button_1.place(relx=0.75, rely=0.8, anchor="n")


            # Création de la fenêtre "SUPPORT"
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        
        self.second_frame_large_image_label = customtkinter.CTkLabel(self.second_frame, text="", image=self.large_test_image)
        self.second_frame_large_image_label.place(relx=0.5, rely=0.01, anchor="n")
        
        self.second_frame_button_1 = customtkinter.CTkButton(self.second_frame, text="Accéder à la documentation", width=250, height=60, font=("",14), image=self.image_icon_documentation, compound="left", command=self.open_documentation)
        self.second_frame_button_1.place(relx=0.3, rely=0.4, anchor="n")
        
        self.second_frame_button_2 = customtkinter.CTkButton(self.second_frame, text="Accéder au code source", width=250, height=60, font=("",14), image=self.image_icon_code_source, compound="right", command=self.open_code_source)
        self.second_frame_button_2.place(relx=0.7, rely=0.4, anchor="n")

        self.second_frame_button_3 = customtkinter.CTkButton(self.second_frame, text="Demander de l'assistance", width=580, height=80, font=("",24), image=self.image_icon_assistance, compound="top", command=self.open_assistance)
        self.second_frame_button_3.place(relx=0.5, rely=0.625, anchor="n")


            # Création de la fenêtre "LOG"
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        self.second_frame_large_image_label = customtkinter.CTkLabel(self.third_frame, text="", image=self.large_test_image)
        self.second_frame_large_image_label.place(relx=0.5, rely=0.01, anchor="n")

        self.textbox = customtkinter.CTkTextbox(self.third_frame,width=700,height=225)
        self.textbox.place(relx=0.5, rely=0.375, anchor="n")
        self.textbox.insert("0.0", f"\n   • Démarrage de l'instance à {datetime.datetime.now().strftime('%H:%M:%S')}, le {datetime.datetime.now().strftime('%d/%m/%Y')}.\n\n")
        self.textbox.configure(state="disabled")


            # Création de la fenêtre "Mise à jour"
        self.fourth_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        self.second_frame_large_image_label = customtkinter.CTkLabel(self.fourth_frame, text="", image=self.large_test_image)
        self.second_frame_large_image_label.place(relx=0.5, rely=0.01, anchor="n")

        request = requests.get('https://github.com/greverdy/EBPInstaller2023/blob/main/v.'+version_package+'.md')
        if request.status_code == 200:
            try:
                self.update_button.configure(image=self.maj_ok_image)
            except:
                pass
            self.label = customtkinter.CTkLabel(self.fourth_frame, text="Utilitaire à jour !", font=("",40))
            self.label.place(relx=0.5, rely=0.5, anchor="n")
            self.textbox.configure(state="normal")
            self.textbox.insert(tk.END, f"   ✔ L'utilitaire est à jour !\n\n")
            self.textbox.configure(state="disabled")
        else:
            try:
                self.update_button.configure(image=self.maj_error_image)
            except:
                pass
            thread_blink_update_event=Thread(target=self.blink_update_event)
            thread_blink_update_event.start()
            self.label = customtkinter.CTkLabel(self.fourth_frame, text="L'utilitaire n'est pas à jour !", font=("",40))
            self.label.place(relx=0.5, rely=0.5, anchor="n")
            self.textbox.configure(state="normal")
            self.textbox.insert(tk.END, f"   ⚠ L'utilitaire n'est pas à jour !\n\n")
            self.textbox.configure(state="disabled")

            self.update_frame_button_1 = customtkinter.CTkButton(self.fourth_frame, text="Obtenir la dernière version", width=250, height=50, image=self.download_image, compound="left", command=self.get_update, font=("",20))
            self.update_frame_button_1.place(relx=0.5, rely=0.8, anchor="n")



            # Création de la fenêtre "Mise à jour Windows"
        self.fifth_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        self.fifth_frame_large_image_label = customtkinter.CTkLabel(self.fifth_frame, text="", image=self.large_test_image)
        self.fifth_frame_large_image_label.place(relx=0.5, rely=0.01, anchor="n")

        self.progressbar_windows_update = customtkinter.CTkProgressBar(master=self.fifth_frame, mode="indeterminate", indeterminate_speed=0.675, variable=customtkinter.IntVar(value=1))
        self.progressbar_windows_update.place(relx=0.5, rely=0.93, anchor="n")
        self.progressbar_windows_update.set(0.0)
        self.progressbar_windows_update.start()

        thread_CheckUpdateCommand=Thread(target=self.CheckWindowsUpdateCommand)
        thread_CheckUpdateCommand.start()
        self.label_fifth_frame = customtkinter.CTkLabel(self.fifth_frame, text='Recherche de mise a jour Windows ', font=("",40))
        self.label_fifth_frame.place(relx=0.5, rely=0.5, anchor="n")

        thread_AnnimText_WU_Command=Thread(target=self.WindowsUpdate_text_animation)
        thread_AnnimText_WU_Command.start()



            # Selection par défaut "HOME"
        self.select_frame_by_name("Installation")


    def select_frame_by_name(self, name):
            # Définition de la couleur du bouton en fonction du menu sélectionné
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "Installation" else "transparent")
        self.support_button.configure(fg_color=("gray75", "gray25") if name == "Support" else "transparent")
        self.log_button.configure(fg_color=("gray75", "gray25") if name == "Log" else "transparent")
        self.update_button.configure(fg_color=("gray75", "gray25") if name == "Mise à jour" else "transparent")
        self.update_windows_button.configure(fg_color=("gray75", "gray25") if name == "Mise à jour Windows" else "transparent")

            # Affiche les éléments de la fenêtre sélectionnée, ou les effaces.
        if name == "Installation":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "Support":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "Log":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()
        if name == "Mise à jour":
            self.fourth_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.fourth_frame.grid_forget()
        if name == "Mise à jour Windows":
            self.fifth_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.fifth_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("Installation")

    def support_button_event(self):
        self.select_frame_by_name("Support")

    def log_button_event(self):
        self.select_frame_by_name("Log")
            # Affiche le bas de la textbox
        try:
            self.textbox.yview(tk.END)
        except:
            pass

    def update_button_event(self):
        self.select_frame_by_name("Mise à jour")

    def update_windows_button_event(self):
        self.select_frame_by_name("Mise à jour Windows")

    
    def open_documentation(self):
        os.system("start https://github.com/greverdy/EBPInstaller2023")

    def open_code_source(self):
        os.system("start https://github.com/greverdy/EBPInstaller2023/blob/main/EBP_tkinter.py")

    def open_assistance(self):
        log_textbox = self.textbox.get("1.0","end")
        text_assistance = f"""\
Merci d'envoyer votre mail à informatique@ecoris.fr

Sujet = "Problème Installation EBP 2023"

Message =
--- MERCI DE DÉTAILLER VOTRE INCIDENT ET DE FOURNIR LES LOGS OU CAPTURE D'ÉCRANS, EN CAS CONTRAIRE VOTRE MAIL NE SERA PAS TRAITÉ ---

Log textbox :
{log_textbox}
        """
        with open(os.environ['USERPROFILE']+"\\Desktop\\Mail_Informatique_Template.txt", "w", encoding="utf-8-sig") as log_textbox_file:
            log_textbox_file.write(text_assistance)
        log_textbox_file.close()
        tk.messagebox.showinfo("Info","Un exemple de mail a été généré sur votre bureau !")

    def waitprogressbar(self):
        var = customtkinter.IntVar()
        app.after(10000, var.set, 1)
        app.wait_variable(var)
        try:
            self.textbox.yview(tk.END)
        except:
            pass

    def blink_log_event(self):
        try:
            for i in range (0,5):
                self.log_button.configure(fg_color=("#CBA261", "#F0B755"))
                sleep(0.5)
                self.log_button.configure(fg_color=("transparent"))
                sleep(0.5)
                i+=1
        except:
            pass

    def blink_update_event(self):
        try:
            for i in range (0,12):
                self.update_button.configure(fg_color=("#ED5656", "#D37978"))
                sleep(0.5)
                self.update_button.configure(fg_color=("transparent"))
                sleep(0.5)
                i+=1
        except:
            pass

    def blink_update_windows_event(self):
        try:
            for i in range (0,12):
                self.update_windows_button.configure(fg_color=("#ED5656", "#D37978"))
                sleep(0.5)
                self.update_windows_button.configure(fg_color=("transparent"))
                sleep(0.5)
                i+=1
        except:
            pass

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def get_update(self):
        os.system("start https://soft.ecoris.fr")
    
    def get__windows_update(self):
        os.system("start ms-settings:windowsupdate")

    def CheckWindowsUpdateCommand(self):
        try:
            try:
                command_verif_update = r"""powershell.exe -command "function Test-PendingReboot { if (Get-ChildItem \"HKLM:\Software\Microsoft\Windows\CurrentVersion\Component Based Servicing\RebootPending\" -EA Ignore) { return $true } if (Get-Item \"HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\Auto Update\RebootRequired\" -EA Ignore) { return $true } if (Get-ItemProperty \"HKLM:\SYSTEM\CurrentControlSet\Control\Session Manager\" -Name PendingFileRenameOperations -EA Ignore) { return $true } try { $util = [wmiclass]\"\\.\root\ccm\clientsdk:CCM_ClientUtilities\"; $status = $util.DetermineIfRebootPending(); if(($status -ne $null) -and $status.RebootPending){ return $true } } catch{} return $false }; Test-PendingReboot"""
                result_command_verif_update = os.popen(command_verif_update).read()
            except:
                result_command_verif_update = False

            print(result_command_verif_update)
            print(bool(result_command_verif_update))
            print(eval(result_command_verif_update))
            
            if eval(result_command_verif_update):
                self.update_windows_button.configure(image=self.maj_error_image)
                self.label_fifth_frame.place(relx=0.5, rely=0.45, anchor="n")
                self.label_fifth_frame.configure(text='Des mises à jour sont en attente.\nVeuillez redémarrer votre poste !')
                self.textbox.configure(state="normal")
                self.textbox.insert(tk.END, f"   ⚠ Une demande de redémarrage a été détectée !\n\n")
                self.textbox.configure(state="disabled")
                thread_blink_update_event=Thread(target=self.blink_update_windows_event)
                thread_blink_update_event.start()
                self.update_windows_frame_button_1 = customtkinter.CTkButton(self.fifth_frame, text="Ouvrir Windows Update", width=250, height=50, image=self.download_image, compound="left", command=self.get__windows_update, font=("",20))
                self.update_windows_frame_button_1.place(relx=0.5, rely=0.8, anchor="n")
            else:
                self.update_windows_button.configure(image=self.maj_ok_image)
                self.label_fifth_frame.configure(text='Aucune mise à jour ne semble en attente.')
                self.textbox.configure(state="normal")
                self.textbox.insert(tk.END, f"   ✔ Aucune demande de redémarrage n'a été détectée !\n\n")
                self.textbox.configure(state="disabled")
            self.progressbar_windows_update.destroy()
        except Exception as e:
            print(e)
            pass

    def WindowsUpdate_text_animation(self):
        try:
            while "Recherche de mise a jour Windows " in self.label_fifth_frame.cget("text"):
                for i in range (0,3):
                    if not "Recherche de mise a jour Windows " in self.label_fifth_frame.cget("text"): #permet d'éviter l'ajout de texte
                        break
                    self.label_fifth_frame.configure(text=self.label_fifth_frame.cget("text")+'.')
                    sleep(0.5)
                    i+=1
                for i in range (0,3):
                    if not "Recherche de mise a jour Windows " in self.label_fifth_frame.cget("text"): #permet d'éviter la suppression de texte
                        break
                    self.label_fifth_frame.configure(text=self.label_fifth_frame.cget("text")[:-1])
                    sleep(0.5)
                    i+=1
        except:
            pass

    def checkbox_event(self, definition, param):
        global EBP_List_Select

        if param == 'self.checkbox_0' :
            if globals()[param].get() == "all" :
                EBP_List_Select.clear()
                for i in range(1,8):
                    globals()["self.checkbox_{}".format(i)].configure(state="disable", variable=customtkinter.StringVar(value="off"))
                EBP_List_Select = EBP_List_Logiciel[:]
            else:
                for i in range(1,8):
                    globals()["self.checkbox_{}".format(i)].configure(state="normal")
                EBP_List_Select.clear()
                
        elif globals()[param].get() != 'off' :
            EBP_List_Select.append(definition)
        else:
            if EBP_List_Select:
                EBP_List_Select.remove(definition)

        if EBP_List_Select:
            self.start_install_home_button_1.configure(state='normal')
        else:
            self.start_install_home_button_1.configure(state='disabled')

    def ebp_valid_install(self):

        try:
            self.quit_button.destroy()
        except:
            pass

        for elem in Event_Swtichcase:
            globals()["self.switch_{}".format(Event_Swtichcase.index(elem)+1)].configure(state="disabled")
        for elem in EBP_List_Logiciel:
            globals()["self.checkbox_{}".format(EBP_List_Logiciel.index(elem)+1)].configure(state="disabled")
        globals()["self.checkbox_{}".format(0)].configure(state="disabled")
        self.start_install_home_button_1.configure(state="disabled")
        
        if Event_Swtichcase[3][2] == "Oui":
            self.restore_licence(None,True,None,None,None)
        else:
            self.install()

    def install(self):
        thread_blink_log_event=Thread(target=self.blink_log_event)
        thread_blink_log_event.start()

        for elem in Event_Swtichcase:
            self.wait()
            self.textbox.configure(state="normal")
            self.textbox.insert(tk.END, f"   ℹ {elem[0]} \n")
            self.textbox.configure(state="disabled")

        self.textbox.configure(state="normal")
        self.textbox.insert(tk.END, f"\n")
        self.textbox.configure(state="disabled")

        if foldername == "%LOCALAPPDATA%":
            try:
                os.mkdir(os.environ['LOCALAPPDATA']+'/EBP2023')
                self.textbox.configure(state="normal")
                self.textbox.insert(tk.END, f'   • Dossier EBP2023 cree dans le repertoire : {foldername}.\n')
                self.textbox.configure(state="disabled")
                try:
                    os.system(f"echo %date%-%time% - code 0x1001 - Dossier EBP2023 cree dans le repertoire : {foldername} >> %userprofile%/Desktop/EBPInstaller_Rapport.log")
                except:
                    pass
            except PermissionError:
                self.textbox.configure(state="normal")
                self.textbox.insert(tk.END, '   • Impossible de creer un dossier.\n     Merci de relancer le script en Administrateur, ou de selectionner un dossier auquel vous avez acces!\n')
                self.textbox.configure(state="disabled")
                try:
                    os.system(f"echo %date%-%time% - code 0x1002 - Erreur de permission : {foldername} >> %userprofile%/Desktop/EBPInstaller_Rapport.log")
                except:
                    pass
            except Exception as e:
                self.textbox.configure(state="normal")
                self.textbox.insert(tk.END, f'   • Dossier EBP2023 existant dans le repertoire : {foldername}.\n')
                self.textbox.configure(state="disabled")
                try:
                    os.system(f"echo %date%-%time% - code 0x1003 - Dossier EBP2023 deja cree : {foldername} >> %userprofile%/Desktop/EBPInstaller_Rapport.log")
                except:
                    pass
        else:
            try:
                os.mkdir(foldername+'/EBP2023')
                self.textbox.configure(state="normal")
                self.textbox.insert(tk.END, f'   • Dossier EBP2023 cree dans le repertoire : {foldername}.\n')
                self.textbox.configure(state="disabled")
                try:
                    os.system(f"echo %date%-%time% - code 0x2001 - Dossier EBP2023 cree dans le repertoire : {foldername} >> %userprofile%/Desktop/EBPInstaller_Rapport.log")
                except:
                    pass
            except PermissionError:
                self.textbox.configure(state="normal")
                self.textbox.insert(tk.END, '   • Impossible de creer un dossier.\n     Merci de relancer le script en Administrateur, ou de selectionner un dossier auquel vous avez acces!\n')
                self.textbox.configure(state="disabled")
                try:
                    os.system(f"echo %date%-%time% - code 0x2002 - Erreur de permission : {foldername} >> %userprofile%/Desktop/EBPInstaller_Rapport.log")
                except:
                    pass
            except Exception as e:
                self.textbox.configure(state="normal")
                self.textbox.insert(tk.END, f'   • Dossier EBP2023 existant dans le repertoire : {foldername}.\n')
                self.textbox.configure(state="disabled")
                try:
                    os.system(f"echo %date%-%time% - code 0x2003 - Dossier EBP2023 deja cree : {foldername} >> %userprofile%/Desktop/EBPInstaller_Rapport.log")
                except:
                    pass

        try:
            os.mkdir(os.environ['PROGRAMDATA']+'/EBP')
            self.textbox.configure(state="normal")
            self.textbox.insert(tk.END, '\n   • Dossier PROGRAMDATA\EBP cree.\n')
            self.textbox.configure(state="disabled")
            try:
                os.system(f"echo %date%-%time% - code 0x3001 - Dossier PROGRAMDATA\EBP cree >> %userprofile%/Desktop/EBPInstaller_Rapport.log")
            except:
                pass
        except PermissionError:
            self.textbox.configure(state="normal")
            self.textbox.insert(tk.END, '   • Impossible de creer le dossier PROGRAMDATA\EBP !\n     Merci de relancer le script en Administrateur.\n')
            self.textbox.configure(state="disabled")
            try:
                os.system(f"echo %date%-%time% - code 0x3002 - Impossible de creer le dossier PROGRAMDATA\EBP >> %userprofile%/Desktop/EBPInstaller_Rapport.log")
            except:
                pass
        except Exception as e:
            self.textbox.configure(state="normal")
            self.textbox.insert(tk.END, f'   • Dossier \"%PROGRAMDATA%\EBP\" existant.\n')
            self.textbox.configure(state="disabled")
            try:
                os.system(f"echo %date%-%time% - code 0x3003 - Dossier \"%PROGRAMDATA%\EBP\" existant. >> %userprofile%/Desktop/EBPInstaller_Rapport.log")
            except:
                pass


        for elem in EBP_List_Select :

            self.wait()

            self.textbox.configure(state="normal")
            self.textbox.insert(tk.END, f"\n\n")
            self.textbox.insert(tk.END, f" • {elem[0]} | [{EBP_List_Select.index(elem)+1}/{len(EBP_List_Select)}]")
            self.textbox.insert(tk.END,f"\n   • Telechargement de {elem[1]}.exe : en cours\n")
            self.textbox.configure(state="disabled") 

            self.wait()
            if not os.path.isdir(elem[3]):
                if not os.path.isfile(foldername+f"/EBP2023/{elem[1]}.exe"):
                    self.progressbar_download_ebp = customtkinter.CTkProgressBar(master=self.third_frame, mode="indeterminate", indeterminate_speed=0.675, variable=customtkinter.IntVar(value=1))
                    self.progressbar_download_ebp.place(relx=0.3, rely=0.9, anchor=customtkinter.CENTER)
                    self.progressbar_download_ebp.set(0.0)
                    self.progressbar_download_ebp.start()
                    try:
                        self.wait()

                        #"DOWNLOAD"
                        try:
                            t2=Thread(target=self.MegaDownload,kwargs={"elem" : elem[2]})
                            t2.start()

                            try:
                                os.system(f"echo %date%-%time% - code 0x4001 - EBP.MegaDownload - Start {elem[2]} >> %userprofile%/Desktop/EBPInstaller_Rapport.log")
                            except:
                                pass

                            while t2.is_alive():
                                self.waitprogressbar()
                            

                            #mega = Mega()
                            #mega.download_url(elem,foldername+'/EBP2023/')

                            if os.path.isfile(foldername+'/EBP2023/'+elem[1]+'.exe'):

                                self.textbox.configure(state="normal")
                                self.textbox.insert(tk.END, f"        • Telechargement de {elem[1]} : OK\n")
                                self.textbox.configure(state="disabled")

                                self.progressbar_download_ebp.destroy()

                                self.textbox.configure(state="normal")
                                self.textbox.insert(tk.END, f"     • Vérification de l'intégrité du fichier\n")
                                self.textbox.configure(state="disabled")

                                thread_hash_sha256=Thread(target=self.Check_Sha256,kwargs={"elem" : elem})
                                thread_hash_sha256.start()

                                while thread_hash_sha256.is_alive():
                                    self.waitprogressbar()

                                self.wait()

                                self.textbox.configure(state="normal")
                                self.textbox.insert(tk.END, f"          • Installation de {elem[1]} : en cours\n")
                                self.textbox.configure(state="disabled")

                                self.wait()

                                self.progressbar_install_ebp = customtkinter.CTkProgressBar(master=self.third_frame, mode="indeterminate", indeterminate_speed=0.675, variable=customtkinter.IntVar(value=1))
                                self.progressbar_install_ebp.place(relx=0.7, rely=0.9, anchor=customtkinter.CENTER)
                                self.progressbar_install_ebp.set(0.0)
                                self.progressbar_install_ebp.start()

                                t2=Thread(target=self.InstallProduct,kwargs={"elem" : elem})
                                t2.start()
                                
                                try:
                                    os.system(f"echo %date%-%time% - code 0x4002 - EBP.InstallProduct - Start >> %userprofile%/Desktop/EBPInstaller_Rapport.log")
                                except:
                                    pass

                                while t2.is_alive():
                                    self.waitprogressbar()

                            else:
                                
                                try:
                                    os.system(f"echo %date%-%time% - code 0xe002 - EBP.MegaDownload - Failed - {foldername+'/EBP2023/'+elem[1]+'.exe'} introuvable >> %userprofile%/Desktop/EBPInstaller_Rapport.log")
                                except:
                                    pass

                                self.textbox.configure(state="normal")
                                self.textbox.insert(tk.END, f"        • Telechargement de {elem[1]} : FAILED\n")
                                self.textbox.configure(state="disabled")

                                self.progressbar_download_ebp.destroy()

                                Failed_List.append(elem)

                                IPaddress=socket.gethostbyname(socket.gethostname())

                                if IPaddress=="127.0.0.1":
                                    self.textbox.configure(state="normal")
                                    self.textbox.insert(tk.END, f"          • Vous ne semblez pas connecté(e) à internet !\n")
                                    self.textbox.configure(state="disabled")
                        
                        except:
                            self.textbox.configure(state="normal")
                            self.textbox.insert(tk.END, f"        • Telechargement de {elem[1]} : FAILED\n")
                            self.textbox.configure(state="disabled")

                            self.progressbar_download_ebp.destroy()

                            Failed_List.append(elem)

                            IPaddress=socket.gethostbyname(socket.gethostname())

                            if IPaddress=="127.0.0.1":
                                self.textbox.configure(state="normal")
                                self.textbox.insert(tk.END, f"          • Vous ne semblez pas connecté(e) à internet !\n")
                                self.textbox.configure(state="disabled")

                            try:
                                os.system(f"echo %date%-%time% - code 0xe002 - EBP.MegaDownload - Failed >> %userprofile%/Desktop/EBPInstaller_Rapport.log")
                            except:
                                pass

                    except WindowsError as a:
                        if os.path.isfile(foldername+'/EBP2023/'+elem[1]+'.exe'):

                            self.textbox.configure(state="normal")
                            self.textbox.insert(tk.END, f"        • Telechargement de {elem[1]} : OK\n")
                            self.textbox.configure(state="disabled")

                            self.progressbar_download_ebp.destroy()

                            self.textbox.configure(state="normal")
                            self.textbox.insert(tk.END, f"     • Vérification de l'intégrité du fichier\n")
                            self.textbox.configure(state="disabled")

                            thread_hash_sha256=Thread(target=self.Check_Sha256,kwargs={"elem" : elem})
                            thread_hash_sha256.start()

                            while thread_hash_sha256.is_alive():
                                self.waitprogressbar()

                            self.wait()

                            try:
                                os.system(f"echo %date%-%time% - code 0xd001 - EBP.MegaDownload - OK >> %userprofile%/Desktop/EBPInstaller_Rapport.log")
                            except:
                                pass

                            self.textbox.configure(state="normal")
                            self.textbox.insert(tk.END, f"          • Installation de {elem[1]} : en cours\n")
                            self.textbox.configure(state="disabled")

                            self.wait()

                            t2=Thread(target=self.InstallProduct_WindowsError,kwargs={"elem" : elem})
                            t2.start()

                            try:
                                os.system(f"echo %date%-%time% - code 0x4002 - EBP.InstallProduct_WindowsError - Start >> %userprofile%/Desktop/EBPInstaller_Rapport.log")
                            except:
                                pass

                            while t2.is_alive():
                                self.waitprogressbar()
                        else:
                            self.textbox.configure(state="normal")
                            self.textbox.insert(tk.END, f"            • [WindowsError] - Fichier introuvable ! Merci de contacter informatique@ecoris.fr, avec l\'aide du fichier \'EBPInstaller_Rapport.log\' genere sur votre Bureau (ou sur la session administrateur), pour signaler cette erreur !\n")
                            self.textbox.configure(state="disabled")
                            Failed_List.append(elem)
                            try:
                                os.system(f"echo %date%-%time% - code 0x5001 - Erreur Telechargement {elem[1]} ou Fichier introuvable ! - {foldername+'/EBP2023/'+elem[1]+'.exe'} - WindowsError - {a} >> %userprofile%/Desktop/EBPInstaller_Rapport.log")
                            except:
                                pass
                    except Exception as e:
                        self.textbox.configure(state="normal")
                        self.textbox.insert(tk.END, f"            • Fichier introuvable ! Merci de contacter informatique@ecoris.fr, avec l\'aide du fichier \'EBPInstaller_Rapport.log\' genere sur votre Bureau (ou sur la session administrateur), pour signaler cette erreur !\n")
                        self.textbox.configure(state="disabled")
                        Failed_List.append(elem)
                        try:
                            os.system(f"echo %date%-%time% - code 0x5002 - Erreur Telechargement {elem[1]} - WindowsError - {e} >> %userprofile%/Desktop/EBPInstaller_Rapport.log")
                        except:
                            pass
                else:

                    self.wait()
                    self.textbox.configure(state="normal")
                    self.textbox.insert(tk.END, f"        • {elem[1]}.exe est deja telecharge dans le dossier {foldername}/EBP2023\n")
                    self.textbox.configure(state="disabled")

                    self.textbox.configure(state="normal")
                    self.textbox.insert(tk.END, f"     • Vérification de l'intégrité du fichier\n")
                    self.textbox.configure(state="disabled")

                    thread_hash_sha256=Thread(target=self.Check_Sha256,kwargs={"elem" : elem})
                    thread_hash_sha256.start()

                    while thread_hash_sha256.is_alive():
                        self.waitprogressbar()

                    try:
                        os.system(f"echo %date%-%time% - code 0xf001 - {elem[1]}.exe est deja telecharge dans le dossier {foldername}/EBP2023 >> %userprofile%/Desktop/EBPInstaller_Rapport.log")
                    except:
                        pass

                    self.wait()

                    self.textbox.configure(state="normal")
                    self.textbox.insert(tk.END, f"          • Installation de {elem[1]} : en cours\n")
                    self.textbox.configure(state="disabled")

                    self.wait()

                    self.progressbar_install_ebp = customtkinter.CTkProgressBar(master=self.third_frame, mode="indeterminate", indeterminate_speed=0.675, variable=customtkinter.IntVar(value=1))
                    self.progressbar_install_ebp.place(relx=0.7, rely=0.9, anchor=customtkinter.CENTER)
                    self.progressbar_install_ebp.set(0.0)
                    self.progressbar_install_ebp.start()

                    self.wait()

                    
                    t2=Thread(target=self.InstallProduct_dl,kwargs={"elem" : elem})
                    t2.start()
                    
                    try:
                        os.system(f"echo %date%-%time% - code 0x4002 - EBP.InstallProduct_dl - Start >> %userprofile%/Desktop/EBPInstaller_Rapport.log")
                    except:
                        pass

                    while t2.is_alive():
                        self.waitprogressbar()

            else:
                self.textbox.configure(state="normal")
                self.textbox.insert(tk.END, f"     • {elem[1]} est deja installe [Dossier d'installation present]\n")
                self.textbox.configure(state="disabled")
                Failed_List.append(elem)

                try:
                    os.system(f"echo %date%-%time% - code 0xfff0 - {elem[1]} est deja installe [Dossier d'installation present] >> %userprofile%/Desktop/EBPInstaller_Rapport.log")
                except:
                    pass

            self.wait()

        self.wait()

        self.licenseXML(EBP_List_Select,Failed_List)
    
    def MegaDownload(self, elem):
        try:
            mega = Mega()
            mega.download_url(elem,foldername+'/EBP2023/')
            try:
                os.system(f"echo %date%-%time% - code 0x7001 - EBP.MegaDownload - OK >> %userprofile%/Desktop/EBPInstaller_Rapport.log")
            except:
                pass
            raise Exception
        except Exception as e:
            if str(e).strip() != "":
                try:
                    os.system(f"echo %date%-%time% - code 0x7001 - EBP.MegaDownload - Failed - {e} >> %userprofile%/Desktop/EBPInstaller_Rapport.log")
                except:
                    pass

    def Check_Sha256(self, elem):

        file = foldername+'/EBP2023/'+elem[1]+'.exe'
        BLOCK_SIZE = 65536 

        file_hash = hashlib.sha256() 
        with open(file, 'rb') as f: 
            fb = f.read(BLOCK_SIZE) 
            while len(fb) > 0: 
                file_hash.update(fb) 
                fb = f.read(BLOCK_SIZE) 
        if file_hash.hexdigest() == elem[5]:
            self.textbox.configure(state="normal")
            self.textbox.insert(tk.END, f"        • Hash Ok ! L'installation va commencer.\n")
            self.textbox.configure(state="disabled")
            try:
                os.system(f"echo %date%-%time% - code 0x7B01 - self.Check_Sha256 - Good >> %userprofile%/Desktop/EBPInstaller_Rapport.log")
            except:
                pass
        else:
            self.textbox.configure(state="normal")
            self.textbox.insert(tk.END, f"     • Le hash ne correspond pas ! Le fichier semble être corrompu et va être supprimé.\n")
            self.textbox.configure(state="disabled")
            try:
                os.system(f"echo %date%-%time% - code 0x7B02 - self.Check_Sha256 - Failed - HASH OG {elem[5]} - HASH DL {file_hash.hexdigest()} >> %userprofile%/Desktop/EBPInstaller_Rapport.log")
            except:
                pass
            
            try:
                os.remove(file)
                try:
                    os.system(f"echo %date%-%time% - code 0x7B03 - self.Check_Sha256 - Fichier supprime >> %userprofile%/Desktop/EBPInstaller_Rapport.log")
                except:
                    pass
            except:
                try:
                    os.system(f"echo %date%-%time% - code 0x7B04 - self.Check_Sha256 - Erreur fichier non supprime >> %userprofile%/Desktop/EBPInstaller_Rapport.log")
                except:
                    pass

            self.textbox.configure(state="normal")
            self.textbox.insert(tk.END,f"\n   • Telechargement de {elem[1]}.exe : en cours\n")
            self.textbox.configure(state="disabled") 

            self.progressbar_download_ebp = customtkinter.CTkProgressBar(master=self.third_frame, mode="indeterminate", indeterminate_speed=0.675, variable=customtkinter.IntVar(value=1))
            self.progressbar_download_ebp.place(relx=0.3, rely=0.9, anchor=customtkinter.CENTER)
            self.progressbar_download_ebp.set(0.0)
            self.progressbar_download_ebp.start()
            t2=Thread(target=self.MegaDownload,kwargs={"elem" : elem[2]})
            t2.start()

            try:
                os.system(f"echo %date%-%time% - code 0x4a01 - EBP.MegaDownload - Start {elem[2]} >> %userprofile%/Desktop/EBPInstaller_Rapport.log")
            except:
                pass

            while t2.is_alive():
                self.waitprogressbar()

    
    def InstallProduct(self, elem):
        installation_process = subprocess.run([f"{foldername}/EBP2023/{elem[1]}.exe", "/s", "NETWORK=FALSE", " PERSONALIZED=TRUE", "WEBCHECKED=TRUE"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if installation_process.returncode == 0:
            self.textbox.configure(state="normal")
            self.textbox.insert(tk.END, f"            • Installation de {elem[1]} : OK\n")
            self.textbox.configure(state="disabled")
            self.progressbar_install_ebp.destroy()
            try:
                os.system(f"echo %date%-%time% - code 0x6001 - EBP.InstallProduct - OK - {foldername}\EBP2023\{elem[1]}.exe >> %userprofile%/Desktop/EBPInstaller_Rapport.log")
            except:
                pass
        else:
            self.textbox.configure(state="normal")
            self.textbox.insert(tk.END, f"            • Erreur ! L'installation de {elem[1]} a echoue !\n")
            self.textbox.configure(state="disabled")
            Failed_List.append(elem)
            self.progressbar_install_ebp.destroy()
            try:
                os.system(f"echo %date%-%time% - code 0x6001 - EBP.InstallProduct - Erreur installation - {foldername}\EBP2023\{elem[1]}.exe >> %userprofile%/Desktop/EBPInstaller_Rapport.log")
            except:
                pass

    def InstallProduct_WindowsError(self, elem):
        installation_process = subprocess.run([f"{foldername}/EBP2023/{elem[1]}.exe", "/s", "NETWORK=FALSE", " PERSONALIZED=TRUE", "WEBCHECKED=TRUE"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if installation_process.returncode == 0:
            self.textbox.configure(state="normal")
            self.textbox.insert(tk.END, f"            • Installation de {elem[1]} : OK\n")
            self.textbox.configure(state="disabled")
            self.progressbar_install_ebp.destroy()
            try:
                os.system(f"echo %date%-%time% - code 0x6002 - EBP.InstallProduct_WindowsError - OK - {foldername}\EBP2023\{elem[1]}.exe >> %userprofile%/Desktop/EBPInstaller_Rapport.log")
            except:
                pass
        else:
            self.textbox.configure(state="normal")
            self.textbox.insert(tk.END, f"            • Erreur ! L'installation de {elem[1]} a echoue !\n")
            self.textbox.configure(state="disabled")
            Failed_List.append(elem)
            self.progressbar_install_ebp.destroy()
            try:
                os.system(f"echo %date%-%time% - code 0x6003 - EBP.InstallProduct_WindowsError - Erreur installation - {foldername}\EBP2023\{elem[1]}.exe >> %userprofile%/Desktop/EBPInstaller_Rapport.log")
            except:
                pass

    def InstallProduct_dl(self, elem):
        installation_process = subprocess.run([f"{foldername}/EBP2023/{elem[1]}.exe", "/s", "NETWORK=FALSE", " PERSONALIZED=TRUE", "WEBCHECKED=TRUE"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if installation_process.returncode == 0:
            self.textbox.configure(state="normal")
            self.textbox.insert(tk.END, f"            • Installation de {elem[1]} : OK\n")
            self.textbox.configure(state="disabled")
            self.progressbar_install_ebp.destroy()
            try:
                os.system(f"echo %date%-%time% - code 0x6003 - EBP.InstallProduct_dl - Ok - {foldername}\EBP2023\{elem[1]}.exe >> %userprofile%/Desktop/EBPInstaller_Rapport.log")
            except:
                pass
        else:
            self.textbox.configure(state="normal")
            self.textbox.insert(tk.END, f"            • Erreur ! L'installation de {elem[1]} a echoue !\n")
            self.textbox.configure(state="disabled")
            Failed_List.append(elem)
            self.progressbar_install_ebp.destroy()
            try:
                os.system(f"echo %date%-%time% - code 0x6003 - EBP.InstallProduct_dl - Erreur installation - {foldername}\EBP2023\{elem[1]}.exe >> %userprofile%/Desktop/EBPInstaller_Rapport.log")
            except:
                pass
    
    def licenseXML(self, list,error):
        global no_ebp

        self.wait()

        for elem in error:
            try:
                list.remove(elem)
            except:
                pass
        
        self.textbox.configure(state="normal")
        self.textbox.insert(tk.END, f"\n\n")
        self.textbox.insert(tk.END, f"   • Configuration des licences.\n")
        self.textbox.configure(state="disabled")
        self.wait()

        if list:
            if os.path.isfile(os.environ['PROGRAMDATA']+'/EBP/license.xml'):

                self.textbox.configure(state="normal")
                self.textbox.insert(tk.END, f"     • Un fichier de licence existe.\n")
                self.textbox.configure(state="disabled")

                self.wait()
                try:
                    with open(os.environ['PROGRAMDATA']+'/EBP/license.xml', 'r') as fr:
                        lines = fr.readlines()
                        with open(os.environ['PROGRAMDATA']+'/EBP/license-new.xml', 'w') as fw:
                            for line in lines:
                                if line.strip('\n') != '</ApplicationsLicenses>':
                                    fw.write(line)
                            for elem in list:
                                fw.write(elem[4][1:] if list.index(elem)==0 else elem[4])

                            fw.write('\n</ApplicationsLicenses>')
                        fw.close()
                    fr.close()
                    with open(os.environ['PROGRAMDATA']+'/EBP/license-new.xml', 'r+') as fd:
                        lines = fd.readlines()
                        fd.seek(0)
                        fd.writelines(line for line in lines if line.strip())
                        fd.truncate()
                    fd.close()

                    path = os.replace(os.environ['PROGRAMDATA']+'/EBP/license-new.xml', os.environ['PROGRAMDATA']+'/EBP/license.xml')

                    self.textbox.configure(state="normal")
                    self.textbox.insert(tk.END, f"        • Fichier de licence modifié !\n\n")
                    self.textbox.configure(state="disabled")

                    self.wait()
                except:
                    self.textbox.configure(state="normal")
                    self.textbox.insert(tk.END, f"        • Une erreur est survenue lors de la modification du fichier de licence !\n          Merci de contacter informatique@ecoris.fr pour signaler cette erreur !\n")
                    self.textbox.configure(state="disabled")

                    self.wait()
                    
            else:

                self.textbox.configure(state="normal")
                self.textbox.insert(tk.END, f"        • Aucun fichier de licence existant.\n")
                self.textbox.configure(state="disabled")

                self.wait()
                try:
                    with open(os.environ['PROGRAMDATA']+'/EBP/license.xml', 'w') as fw:
                        fw.write('<ApplicationsLicenses>\n')
                        for elem in list:
                                fw.write(elem[4][1:] if list.index(elem)==0 else elem[4])
                        fw.write('\n</ApplicationsLicenses>')
                    fw.close()

                    with open(os.environ['PROGRAMDATA']+'/EBP/license.xml', 'r+') as fd:
                        lines = fd.readlines()
                        fd.seek(0)
                        fd.writelines(line for line in lines if line.strip())
                        fd.truncate()
                    fd.close()

                    self.textbox.configure(state="normal")
                    self.textbox.insert(tk.END, f"          • Fichier de licence cree !\n\n")
                    self.textbox.configure(state="disabled")

                    self.wait()
                    
                except:

                    self.textbox.configure(state="normal")
                    self.textbox.insert(tk.END, f"          • Une erreur est survenue lors de la creation du fichier de licence !\n            Merci de contacter informatique@ecoris.fr pour signaler cette erreur !\n")
                    self.textbox.configure(state="disabled")

                    self.wait()
        else:

            self.textbox.configure(state="normal")
            self.textbox.insert(tk.END, f"          • Aucune nouvelle application n'a ete installee. Le fichier de licence ne sera pas modifié.\n\n")
            self.textbox.configure(state="disabled")
            no_ebp=True

            self.wait()

        temp_Event_Swtichcase = Event_Swtichcase[:3]
        for elem in temp_Event_Swtichcase:
            try:
                func = getattr(self, elem[1])
                Installation=True
                func(elem[1], Installation, None, elem[2], None)
                # test != self =! elem(1)
            except Exception as e:
                try:
                    os.system(f"echo Error - licenseXML - temp_Event_Swtichcase - {e} >> %userprofile%/Desktop/EBPInstaller_Rapport.log")
                except:
                    pass
        
        self.wait()
        self.textbox.configure(state="normal")
        self.textbox.insert(tk.END, f"\n\n")
        self.textbox.insert(tk.END, f"   • Instance terminée. L'application peut-être fermée.\n")
        self.textbox.configure(state="disabled")
        self.wait()

        self.restore_switchcase_checkbox_button()

        EBP_List_Select.clear()
        
        self.quit_button = customtkinter.CTkButton(master=self.third_frame, text="Quitter", corner_radius=10, command=self.shut_app, width=250, height=30, hover=True, font=('Arial',20))
        self.quit_button.place(relx=0.5, rely=0.93, anchor=customtkinter.CENTER)


    def shut_app(self):
        try:
            os.system(f"echo. >> %userprofile%/Desktop/EBPInstaller_Rapport.log && echo %date%-%time% - Fermeture >> %userprofile%/Desktop/EBPInstaller_Rapport.log && echo. >> %userprofile%/Desktop/EBPInstaller_Rapport.log")
        except:
            pass
            
        try:
            os.system(f"exit")
        except:
            exit()
        else:
            os._exit(0)

    def restore_switchcase_checkbox_button(self):
        for elem in Event_Swtichcase:
            globals()["self.switch_{}".format(Event_Swtichcase.index(elem)+1)].configure(state="normal")
        for elem in EBP_List_Logiciel:
            globals()["self.checkbox_{}".format(EBP_List_Logiciel.index(elem)+1)].configure(state="normal")
            globals()["self.checkbox_{}".format(EBP_List_Logiciel.index(elem)+1)].deselect()
        globals()["self.checkbox_{}".format(0)].configure(state="normal")
        globals()["self.checkbox_{}".format(0)].deselect()
        

    def switch_event(self, EventText, definition,param):
        func = getattr(self, definition)
        Installation=False
        func(definition, Installation, EventText, param,globals()[param].get())

    def delete_EBP_packages(self, test, Installation, EventText, param, value):
        if not Installation:
            if value == "Non":
                globals()[param].configure(variable=customtkinter.StringVar(value="Non"), text=EventText[:-3]+"Non")
            else:
                globals()[param].configure(variable=customtkinter.StringVar(value="Oui"), text=EventText[:-3]+"Oui")

            textlist=EventText[:-3]+("Non" if value == "Oui" else "Oui")
            for elem in Event_Swtichcase:
                if textlist in elem:
                    elem[0]=EventText[:-3]+globals()[param].get()
                    elem[2]=globals()[param].get()
        else:
            if param == "Oui" and not no_ebp:
                self.nettoyage(foldername, value)
            elif param == "Oui" and no_ebp:
                self.textbox.configure(state="normal")
                self.textbox.insert(tk.END, f"\n          • Aucune nouvelle application n'a ete installee. Le dossier EBP2023 ne sera pas supprime.\n")
                self.textbox.configure(state="disabled")
            
    def restart(self, test, Installation, EventText, param, value):
        if not Installation:
            if value == "Non":
                globals()[param].configure(variable=customtkinter.StringVar(value="Non"), text=EventText[:-3]+"Non")
            else:
                globals()[param].configure(variable=customtkinter.StringVar(value="Oui"), text=EventText[:-3]+"Oui")

            textlist=EventText[:-3]+("Non" if value == "Oui" else "Oui")
            for elem in Event_Swtichcase:
                if textlist in elem:
                    elem[0]=EventText[:-3]+globals()[param].get()
                    elem[2]=globals()[param].get()
            
        else:
            if param == "Oui" and not no_ebp:
                self.wait()
                self.textbox.configure(state="normal")
                self.textbox.insert(tk.END, f"          • Le poste va redemarrer.\n")
                self.textbox.configure(state="disabled")
                self.wait()
                self.wait()
                self.wait()
                self.wait()
                self.wait()
                os.system("shutdown -r -t 2")
            elif param == "Oui" and no_ebp:
                self.wait()
                self.textbox.configure(state="normal")
                self.textbox.insert(tk.END, f"\n          • Aucune nouvelle application n'a ete installee. Le poste ne va pas redemarrer.\n")
                self.textbox.configure(state="disabled")
                self.wait()
                self.wait()

    def Change_path(self, test, Installation, EventText, param, value):
        global foldername
        if not Installation:
            if value == "Non":
                foldername = tk.filedialog.askdirectory(initialdir = os.environ['USERPROFILE'],
                                                title = "Select a Folder")
                if foldername:
                    if foldername[-7:]=="EBP2023":
                        foldername=foldername[:len(foldername)-len(foldername[-7:])-1]
                    show_foldername=foldername[:(foldername.find('/', foldername.find('/')+1,len(foldername)))+1]+"[•••]"+foldername[-(foldername[::-1].find('/'))-1:]
                    globals()[param].configure(variable=customtkinter.StringVar(value="Chemin : "+foldername), text="Chemin : "+show_foldername)
                else:
                    #foldername="%LOCALAPPDATA%"
                    foldername=os.environ["LOCALAPPDATA"]
                    globals()[param].configure(variable=customtkinter.StringVar(value="Oui"), text="Chemin par default : %LOCALAPPDATA%")
            else:
                #foldername="%LOCALAPPDATA%"
                foldername=os.environ["LOCALAPPDATA"]
                globals()[param].configure(variable=customtkinter.StringVar(value="Oui"), text="Chemin par default : %LOCALAPPDATA%")


            for elem in Event_Swtichcase:
                for celem in elem:
                    if "Chemin" in celem:
                        elem[0]=("Chemin : " if foldername != "%LOCALAPPDATA%" else "Chemin par defaut : ")+foldername
        else:
            pass
    
    def restore_licence(self, test, Installation, EventText, param, value):
        if not Installation:
            if value == "Non":
                globals()[param].configure(variable=customtkinter.StringVar(value="Non"), text=EventText[:-3]+"Non")
            else:
                globals()[param].configure(variable=customtkinter.StringVar(value="Oui"), text=EventText[:-3]+"Oui")

            textlist=EventText[:-3]+("Non" if value == "Oui" else "Oui")
            for elem in Event_Swtichcase:
                if textlist in elem:
                    elem[0]=EventText[:-3]+globals()[param].get()
                    elem[2]=globals()[param].get()
        else:
            self.textbox.configure(state="normal")
            self.textbox.insert(tk.END, f"\n       • La restauration de licence va commencer.\n")
            self.textbox.configure(state="disabled")
            self.restore_licence_event()

    def restore_licence_event(self):
        licence_xml="<ApplicationsLicenses>\n"

        for elem in EBP_List_Select:
            if os.path.isdir(elem[3]):
                #licence_xml+=(elem[4][1:] if list.index(elem)==0 else elem[4])
                licence_xml+=elem[4][1:]
                self.textbox.configure(state="normal")
                self.textbox.insert(tk.END, f"\n          • La licence de {elem[0]} a été ajouté !\n")
                self.textbox.configure(state="disabled")
            else:
                self.textbox.configure(state="normal")
                self.textbox.insert(tk.END, f"\n          • La licence de {elem[0]} ne sera pas ajouté car le logiciel ne semble pas installé.\n")
                self.textbox.configure(state="disabled")

        licence_xml+='\n</ApplicationsLicenses>'


        try:
            with open(os.environ['PROGRAMDATA']+'/EBP/license.xml', 'w') as fw:
                fw.write(licence_xml)
            fw.close()
            self.textbox.configure(state="normal")
            self.textbox.insert(tk.END, f"\n   • Le fichier de licences a bien été ajouté !\n")
            self.textbox.configure(state="disabled")
        except FileNotFoundError as e:
            self.textbox.configure(state="normal")
            self.textbox.insert(tk.END, f"\n   • Le dossier EBP dans le chemin %programdata% n'existe pas.\n")
            self.textbox.configure(state="disabled")
            
            try:
                os.mkdir(os.environ['PROGRAMDATA']+'/EBP')
                self.textbox.configure(state="normal")
                self.textbox.insert(tk.END, '\n   • Dossier PROGRAMDATA\EBP cree.\n')
                self.textbox.configure(state="disabled")
                try:
                    os.system(f"echo %date%-%time% - code 0x3001 - restore_licence_event - Dossier PROGRAMDATA\EBP cree >> %userprofile%/Desktop/EBPInstaller_Rapport.log")
                except:
                    pass
            except PermissionError:
                self.textbox.configure(state="normal")
                self.textbox.insert(tk.END, '• Impossible de creer le dossier PROGRAMDATA\EBP !\n     Merci de relancer le script en Administrateur.\n')
                self.textbox.configure(state="disabled")
                try:
                    os.system(f"echo %date%-%time% - code 0x3002 - restore_licence_event - Impossible de creer le dossier PROGRAMDATA\EBP >> %userprofile%/Desktop/EBPInstaller_Rapport.log")
                except:
                    pass
            except Exception as e:
                self.textbox.configure(state="normal")
                self.textbox.insert(tk.END, f'   • Dossier \"%PROGRAMDATA%\EBP\" existant.\n')
                self.textbox.configure(state="disabled")
                try:
                    os.system(f"echo %date%-%time% - code 0x3003 - restore_licence_event - Dossier \"%PROGRAMDATA%\EBP\" existant. >> %userprofile%/Desktop/EBPInstaller_Rapport.log")
                except:
                    pass
            
            try:        
                with open(os.environ['PROGRAMDATA']+'/EBP/license.xml', 'w') as fw:
                    fw.write(licence_xml)
                fw.close()
                self.textbox.configure(state="normal")
                self.textbox.insert(tk.END, f"\n   • Le fichier de licences a bien été ajouté !\n")
                self.textbox.configure(state="disabled")
            except Exception as e:        
                self.textbox.configure(state="normal")
                self.textbox.insert(tk.END, f"\n   • Le dossier EBP dans le chemin %programdata% n'existe pas.\n")
                self.textbox.configure(state="disabled")
                try:
                    os.system(f"echo %date%-%time% - code 0x3004 - restore_licence_event - Error n°2 - {e}. >> %userprofile%/Desktop/EBPInstaller_Rapport.log")
                except:
                    pass

        self.wait()
        self.textbox.configure(state="normal")
        self.textbox.insert(tk.END, f"\n\n")
        self.textbox.insert(tk.END, f"   • Instance terminée. L'application peut-être fermée.\n")
        self.textbox.configure(state="disabled")
        self.wait()

        self.restore_switchcase_checkbox_button()
        EBP_List_Select.clear()
        
        self.quit_button = customtkinter.CTkButton(master=self.third_frame, text="Quitter", corner_radius=10, command=self.shut_app, width=250, height=30, hover=True, font=('Arial',20))
        self.quit_button.place(relx=0.5, rely=0.93, anchor=customtkinter.CENTER)
        
    def nettoyage(self, folder):
        self.textbox.configure(state="normal")
        self.textbox.insert(tk.END, f"\n\n")
        self.textbox.insert(tk.END, f"   • Phase de nettoyage.\n")
        self.textbox.configure(state="disabled")
        self.wait()
        if os.path.isdir(folder+'/EBP2023'):
            try:
                shutil.rmtree(folder+'/EBP2023')
                self.textbox.configure(state="normal")
                self.textbox.insert(tk.END, f"     • Dossier EBP2023 supprime.\n")
                self.textbox.configure(state="disabled")
                self.wait()
            except:
                self.textbox.configure(state="normal")
                self.textbox.insert(tk.END, f"     • Impossible de supprimer le dossier EBP2023 !\n   Merci de vous rendre dans {foldername} et de supprimer le dossier EBP2023\n")
                self.textbox.configure(state="disabled")
                self.wait()
        else:
            self.wait()
            self.textbox.configure(state="normal")
            self.textbox.insert(tk.END, f"     • Aucun dossier EBP2023.\n")
            self.textbox.configure(state="disabled")
            self.wait()
    
    def wait(self):
        var = customtkinter.IntVar()
        app.after(400, var.set, 1)
        app.wait_variable(var)
        self.textbox.yview(tk.END)

    def on_closing(self):
        if tk.messagebox.askokcancel("Quitter", "Voulez-vous vraiment quitter l'application?"):
            if getattr(sys, 'frozen', False):
                pyi_splash.close()
            # Ici, vous pouvez effectuer toutes les opérations de nettoyage nécessaires
            self.destroy()  # Ferme la fenêtre principale et détruit l'instance de la classe
            try:
                self.P.kill()
            except:
                pass
            try:
                self.L.kill()
            except:
                pass
            PID = os.getpid()
            os.kill(PID, signal.SIGKILL) 
            sys.exit()
        exit()


#╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬#
#╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬#
#╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬#


#                                                            ╔═══════════════════════╗
#                                                            ║    VARIABLES FIXES    ║
#                                                            ╚═══════════════════════╝

EBP_List_Logiciel_wl =[
["EBPOL 2023 Comptabilite ELITE","EBP_2023_Comptabilite_ELITE_22_3_1_10778","https://mega.nz/file/ATsmDKQT#bNoEknOkJ4bjm3HCmnIHcuxkLpTlufyd_ZPLon1lhQE","C:\\Program Files\\EBP\\Accounting22.3FRFR40","""\n  ""","270f58088ead74ca75c44ca594a0e8c0b0b1d3700f7b88fc8aef71772f927456"],
["EBPOL 2023 Etats Financiers PRO","EBP_2023_Etats_Financiers_PRO_22_3_0_4116","https://mega.nz/file/sOFDiI4D#DQMnBrWUwa56y_PhEdEWA2GrpLXVT2qAwqduQgMzAXs","C:\\Program Files\\EBP\\FinState22.3FRFR30","""\n  ""","2203bb3baa68ed6711a8a38c276a6221a660f895704f9897a93370910b1ee4a2"],
["EBPOL 2023 Gestion ELITE","EBP_2023_Gestion_ELITE_22_2_0_7405","https://mega.nz/file/US1FjKRR#1LUjQ3PRCEDfsxFoMYujGqyTahw3VMilCLiCy_Iq_vE","C:\\Program Files\\EBP\\Invoicing22.2FRFR40","""\n  ""","77ea4f75c82480958a474f4c86896b03665bbf1057a20355bbf82f007c51cb73"],
["EBPOL 2023 Immobilisations ELITE","EBP_2023_Immobilisations_ELITE_22_0_0_3735","https://mega.nz/file/kHcSVYwa#g3AKsH8YwVTkkFpHDRJTxxSAziBHfhRksX-VKtvQhAs","C:\\Program Files\\EBP\\CapitalAsset22.0FRFR40","""\n  ""","5661edbab4a9b911f4329bcde586a1ea010e5cec6dfa628f4ad8173e7e5da12d"],
["EBP 2022 Classis BusinessPlan","EBPOL_2022_Classic_BusinessPlan_14_0_0_2005","https://mega.nz/file/QCUgiKoB#zjbGKz5-rPU1lCaJnhthq6UgCxhmUqAt6o_kkYMtIwM","C:\\Program Files\\EBP\\BusinessPlan14.0FRFR20","""\n  ""","add7ac6b9afe45b845d128459321eb174c905670abc0c5d96b01197d51129053"],
["EBP 2023 Autonome Paie","EBPOL_2023_Autonome_Paie_13_23_1_14362","https://mega.nz/file/1SdCTZzS#5ZTvIlitmXD85t3FNvslXXlyfbukFHjrTiQliA-G328","C:\\Program Files\\EBP\\Payroll13.23FRFR50","""\n  ""","daffe117f6a3e0bd32eab40ffba9a11661f97352b62e3c13363a1957dc0dcf6a"],
["EBP 2023 CRM ELITE","EBPOL_2023_CRM_ELITE_15_0_0_1305","https://mega.nz/file/oKkzgDaK#MqeWHk5O4RyXLo-NxuLlsSRkJb783R5BkaRG8qzrkaA","C:\\Program Files\\EBP\\CRM15.0FRFR40","""\n  ""","5e64625b82302a936df9930b702df161835ffdc9878cdef3912f93a81cf229b9"]
]

EBP_List_Select = []

Failed_List=[]

Event_Swtichcase=[
["Supprimer les packages apres l'installation : Non","delete_EBP_packages","Non","normal"],
["Redemarrer apres l'installation : Non","restart","Non","normal"],
["Chemin par default : %LOCALAPPDATA%", "Change_path","Oui","normal"],
["Réinstallation de licence : Non", "restore_licence","Non","normal"],
]

version_package="1.6.0"

foldername=os.environ["LOCALAPPDATA"]

no_ebp=True

#╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬#
#╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬#
#╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬#


#                                                            ╔════════════╗
#                                                            ║    CODE    ║
#                                                            ╚════════════╝


if __name__ == "__main__":
    app = App()

    app.mainloop()

#╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬#
#╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬#
#╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬#
