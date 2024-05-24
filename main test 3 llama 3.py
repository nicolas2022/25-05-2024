import customtkinter as ctk

class Application(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Création des onglets
        self.tab_manager = ctk.CTkTabview(self, width=800, height=600)
        self.tab_manager.pack(fill="both", expand=True)

        self.onglet1 = self.tab_manager.add("Enregistrement ADD")
        self.onglet2 = self.tab_manager.add("Sélection de dossier")
        self.onglet3 = self.tab_manager.add("Suivi de dossier")
        self.onglet4 = self.tab_manager.add("Extraction")

        # Onglet 1 : Enregistrement ADD
        self.onglet1.configure(fg_color="#333")  # Fond noir-gris

        # Ligne titre : Organisme demandeur" (onglet1ligne1)
        self.onglet1ligne1 = ctk.CTkLabel(self.onglet1, text="DEMANDEUR", font=("Arial", 14, "bold"), fg_color="#333", text_color="white")
        self.onglet1ligne1.pack(fill="x", pady=10)

        # Ligne 1 (onglet1ligne2)
        self.onglet1ligne2 = ctk.CTkFrame(self.onglet1, fg_color="#333")
        self.onglet1ligne2.pack(anchor="center", pady=5)

        # Menu deroulant CTkComboBox pour le type d'organisme demandeur en ligne 1
        self.onglet1ligne2_1 = ctk.CTkComboBox(self.onglet1ligne2, width=170, values=["Association", "Bailleur social", "CCAS", "Centre médico-social", "Département", "Maison de métropole", "Maison du Rhône", "Autre"], command=self.update_case, state="readonly")
        self.onglet1ligne2_1.pack(side="left", padx=10)
        self.onglet1ligne2_1.bind("<<ComboboxSelected>>", self.update_case)
        self.onglet1ligne2_1.bind("<Button-1>", self.open_combobox)
        self.onglet1ligne2_1.bind("<Return>", self.check_selection)

        # Texte : "Nom si association" en ligne 1
        self.onglet1ligne2_2 = ctk.CTkLabel(self.onglet1ligne2, text="Nom si association", fg_color="#333", text_color="white")
        self.onglet1ligne2_2.pack(side="left", padx=10)

        # Case CTkEntry -> nom de l'organisme demandeur en ligne 1
        self.onglet1ligne2_3 = ctk.CTkEntry(self.onglet1ligne2, width=326, fg_color="#333", text_color="white")
        self.onglet1ligne2_3.pack(side="left", padx=10)
        self.onglet1ligne2_3.bind("<Return>", self.focus_next_entry)

        # Ligne 2 (onglet1ligne3)
        self.onglet1ligne3 = ctk.CTkFrame(self.onglet1, fg_color="#333")
        self.onglet1ligne3.pack(anchor="center", pady=5)

        # Texte : "Adresse" en ligne 2
        self.onglet1ligne3_1 = ctk.CTkLabel(self.onglet1ligne3, text="Adresse", fg_color="#333", text_color="white")
        self.onglet1ligne3_1.pack(side="left", padx=10)

        # Case CTkEntry -> adresse de l'organisme demandeur en ligne 2
        self.onglet1ligne3_2 = ctk.CTkEntry(self.onglet1ligne3, width=579, fg_color="#333", text_color="white")
        self.onglet1ligne3_2.pack(side="left", padx=10)
        self.onglet1ligne3_2.bind("<Return>", self.focus_next_entry)

        # Ligne 3 (onglet1ligne4)
        self.onglet1ligne4 = ctk.CTkFrame(self.onglet1, fg_color="#333")
        self.onglet1ligne4.pack(anchor="center", pady=5)

        # Texte : "Code postal" en ligne 3
        self.onglet1ligne4_1 = ctk.CTkLabel(self.onglet1ligne4, text="Code postal", fg_color="#333", text_color="white")
        self.onglet1ligne4_1.pack(side="left", padx=10)

        # Case CTkEntry -> code postal de l'organisme demandeur en ligne 3
        self.onglet1ligne4_2 = ctk.CTkEntry(self.onglet1ligne4, width=50, fg_color="#333", text_color="white")
        self.onglet1ligne4_2.pack(side="left", padx=10)
        self.onglet1ligne4_2.bind("<KeyRelease>", self.limit_character_count)
        self.onglet1ligne4_2.bind("<Return>", self.focus_next_entry)

        # Texte : "Ville" en ligne 3
        self.onglet1ligne4_3 = ctk.CTkLabel(self.onglet1ligne4, text="Ville", fg_color="#333", text_color="white")
        self.onglet1ligne4_3.pack(side="left", padx=10)

        # Case CTkEntry -> ville de l'organisme demandeur en ligne 3
        self.onglet1ligne4_4 = ctk.CTkEntry(self.onglet1ligne4, width=192, fg_color="#333", text_color="white")
        self.onglet1ligne4_4.pack(side="left", padx=10)
        self.onglet1ligne4_4.bind("<Return>", self.focus_next_entry)

        # Case CTkLabel -> element decoratif en fin de ligne 4
        self.onglet1ligne4_5 = ctk.CTkLabel(self.onglet1ligne4, text=" ", fg_color="#333", text_color="#333", width=232)
        self.onglet1ligne4_5.pack(side="left", padx=10)

                # Ligne 4 (onglet1ligne5)
        self.onglet1ligne5 = ctk.CTkFrame(self.onglet1, fg_color="#333")
        self.onglet1ligne5.pack(anchor="center", pady=5)

        # Texte : "Referent(e) :" en ligne 4
        self.onglet1ligne5_1 = ctk.CTkLabel(self.onglet1ligne5, text="Référent(e) :", fg_color="#333", text_color="white")
        self.onglet1ligne5_1.pack(side="left", padx=10)

        # Menu deroulant CTkComboBox pour le sexe du travailleur social en ligne 4
        self.onglet1ligne5_2 = ctk.CTkComboBox(self.onglet1ligne5, width=70, values=[" ", "M.", "Mme"], state="readonly")
        self.onglet1ligne5_2.pack(side="left", padx=10)
        self.onglet1ligne5_2.bind("<Button-1>", self.open_combobox)

        # Texte : "Nom" en ligne 4
        self.onglet1ligne5_3 = ctk.CTkLabel(self.onglet1ligne5, text="Nom", fg_color="#333", text_color="white")
        self.onglet1ligne5_3.pack(side="left", padx=10)

        # Case CTkEntry -> nom du travailleur social en ligne 4
        self.onglet1ligne5_4 = ctk.CTkEntry(self.onglet1ligne5, width=165, fg_color="#333", text_color="white")
        self.onglet1ligne5_4.pack(side="left", padx=10)
        self.onglet1ligne5_4.bind("<Return>", self.focus_next_entry)

        # Texte : "Prenom" en ligne 4
        self.onglet1ligne5_5 = ctk.CTkLabel(self.onglet1ligne5, text="Prénom", fg_color="#333", text_color="white")
        self.onglet1ligne5_5.pack(side="left", padx=10)

        # Case CTkEntry -> prenom du travailleur social en ligne 4
        self.onglet1ligne5_6 = ctk.CTkEntry(self.onglet1ligne5, width=165, fg_color="#333", text_color="white")
        self.onglet1ligne5_6.pack(side="left", padx=10)
        self.onglet1ligne5_6.bind("<Return>", self.focus_next_entry)

        # Ligne 5 (onglet1ligne6)
        self.onglet1ligne6 = ctk.CTkFrame(self.onglet1, fg_color="#333")
        self.onglet1ligne6.pack(anchor="center", pady=5)

        # Texte : "Téléphone 1" en ligne 5
        self.onglet1ligne6_1 = ctk.CTkLabel(self.onglet1ligne6, text="Téléphone 1", fg_color="#333", text_color="white")
        self.onglet1ligne6_1.pack(side="left", padx=10)

        # Case CTkEntry -> téléphone 1 du travailleur social en ligne 5
        self.onglet1ligne6_2 = ctk.CTkEntry(self.onglet1ligne6, width=90, fg_color="#333", text_color="white")
        self.onglet1ligne6_2.pack(side="left", padx=10)
        self.onglet1ligne6_2.bind("<Return>", self.focus_next_entry)

        # Texte : "Téléphone 2" en ligne 5
        self.onglet1ligne6_3 = ctk.CTkLabel(self.onglet1ligne6, text="Téléphone 2", fg_color="#333", text_color="white")
        self.onglet1ligne6_3.pack(side="left", padx=10)

        # Case CTkEntry -> téléphone 2 du travailleur social en ligne 5
        self.onglet1ligne6_4 = ctk.CTkEntry(self.onglet1ligne6, width=90, fg_color="#333", text_color="white")
        self.onglet1ligne6_4.pack(side="left", padx=10)
        self.onglet1ligne6_4.bind("<Return>", self.focus_next_entry)

        # Case CTkLabel -> element decoratif en fin de ligne 5
        self.onglet1ligne6_5 = ctk.CTkLabel(self.onglet1ligne6, text=" ", fg_color="#333", text_color="#333", width=243)
        self.onglet1ligne6_5.pack(side="left", padx=10)

        # Ligne 6 (onglet1ligne7)
        self.onglet1ligne7 = ctk.CTkFrame(self.onglet1, fg_color="#333")
        self.onglet1ligne7.pack(anchor="center", pady=5)

        # Texte : "Mail" en ligne 6
        self.onglet1ligne7_1 = ctk.CTkLabel(self.onglet1ligne7, text="Mail", fg_color="#333", text_color="white")
        self.onglet1ligne7_1.pack(side="left", padx=10)

        # Case CTkEntry -> mail du travailleur social en ligne 6
        self.onglet1ligne7_2 = ctk.CTkEntry(self.onglet1ligne7, width=350, fg_color="#333", text_color="white")
        self.onglet1ligne7_2.pack(side="left", padx=10)
        self.onglet1ligne7_2.bind("<Return>", self.focus_next_entry)

        # Case CTkLabel -> element decoratif en fin de ligne 6
        self.onglet1ligne7_3 = ctk.CTkLabel(self.onglet1ligne7, text=" ", fg_color="#333", text_color="#333", width=230)
        self.onglet1ligne7_3.pack(side="left", padx=10)

        # Ligne 7 (onglet1ligne8)
        self.onglet1ligne8 = ctk.CTkFrame(self.onglet1, fg_color="#333")
        self.onglet1ligne8.pack(anchor="center", pady=5)

        # Texte : "Mail en copie" en ligne 7
        self.onglet1ligne8_1 = ctk.CTkLabel(self.onglet1ligne8, text="Mail en copie", fg_color="#333", text_color="white")
        self.onglet1ligne8_1.pack(side="left", padx=10)

        # Case CTkEntry -> mail en copie du travailleur social en ligne 7
        self.onglet1ligne8_2 = ctk.CTkEntry(self.onglet1ligne8, width=350, fg_color="#333", text_color="white")
        self.onglet1ligne8_2.pack(side="left", padx=10)
        self.onglet1ligne8_2.bind("<Return>", self.focus_next_entry)

        # Case CTkLabel -> element decoratif en fin de ligne 7
        self.onglet1ligne8_3 = ctk.CTkLabel(self.onglet1ligne8, text=" ", fg_color="#333", text_color="#333", width=180)
        self.onglet1ligne8_3.pack(side="left", padx=10)

    def update_case(self, event=None):
        if self.onglet1ligne2_1.get() == "Association":
            self.onglet1ligne2_3.configure(state="normal", fg_color="#333")
        else:
            self.onglet1ligne2_3.delete(0, 'end')
            self.onglet1ligne2_3.configure(state="disabled", fg_color="black")

    def open_combobox(self, event):
        # Fermer toutes les autres fenêtres de combobox ouvertes
        self.onglet1ligne2_1.tk_focusPrev().focus()
        event.widget.focus()
        event.widget.event_generate('<Down>')

    def check_selection(self, event):
        if self.onglet1ligne2_1.get() == "Association":
            self.onglet1ligne2_3.focus()
        else:
            self.onglet1ligne3_2.focus()

    def limit_character_count(self, event):
        widget = event.widget
        if len(widget.get()) > 5:
            widget.delete(5, 'end')

    def focus_next_entry(self, event):
        event.widget.tk_focusNext().focus()

if __name__ == "__main__":
    app = Application()
    app.mainloop()

