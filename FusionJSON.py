import json
import tkinter as tk
from tkinter import filedialog

class JSONMergerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("JSON Merger")

        self.source1_button = tk.Button(root, text="Choisir Fichier Source 1", command=self.choose_source1)
        self.source1_button.pack(pady=10)

        self.source2_button = tk.Button(root, text="Choisir Fichier Source 2", command=self.choose_source2)
        self.source2_button.pack(pady=10)

        self.final_button = tk.Button(root, text="Choisir Fichier Final", command=self.choose_final)
        self.final_button.pack(pady=10)

        self.merge_button = tk.Button(root, text="Fusionner", command=self.merge_files)
        self.merge_button.pack(pady=20)

    def choose_source1(self):
        self.source1_path = filedialog.askopenfilename(title="Choisir le premier fichier source JSON")

    def choose_source2(self):
        self.source2_path = filedialog.askopenfilename(title="Choisir le deuxième fichier source JSON")

    def choose_final(self):
        self.final_path = filedialog.asksaveasfilename(title="Enregistrer le fichier final JSON", defaultextension=".json", initialdir=".")

    def merge_files(self):
        try:
            with open(self.source1_path, 'r', encoding='utf-8') as source1_file:
                source1_data = json.load(source1_file)

            with open(self.source2_path, 'r', encoding='utf-8') as source2_file:
                source2_data = json.load(source2_file)

            fusion_data = self.fusionner_fichiers_json(source1_data, source2_data)

            with open(self.final_path, 'w', encoding='utf-8') as final_file:
                json.dump(fusion_data, final_file, indent=4)

            self.status_label.config(text="Fusion réussie dans " + self.final_path)
        except Exception as e:
            self.status_label.config(text="Erreur : " + str(e))

    def fusionner_fichiers_json(self, source1_data, source2_data):
        for key, value in source2_data.items():
            if key in source1_data:
                if source1_data[key] is False and value is True:
                    source1_data[key] = value
            else:
                source1_data[key] = value
        return source1_data

root = tk.Tk()
app = JSONMergerApp(root)
root.mainloop()

