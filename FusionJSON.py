import json
import tkinter as tk
from tkinter import filedialog

class JSONMergerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("JSON Merger")

        self.source1_button = tk.Button(root, text="Choose your source file 1", command=self.choose_source1)
        self.source1_button.pack(pady=5)
        self.source1_label = tk.Label(root, text="")
        self.source1_label.pack()

        self.source2_button = tk.Button(root, text="Choose your source file 2", command=self.choose_source2)
        self.source2_button.pack(pady=5)
        self.source2_label = tk.Label(root, text="")
        self.source2_label.pack()

        self.final_button = tk.Button(root, text="Choose name and directory for the final merged file", command=self.choose_final)
        self.final_button.pack(pady=5)
        self.final_label = tk.Label(root, text="")
        self.final_label.pack()

        self.merge_button = tk.Button(root, text="Merge", command=self.merge_files)
        self.merge_button.pack(pady=20)

        self.status_label = tk.Label(root, text="")
        self.status_label.pack()

    def choose_source1(self):
        self.source1_path = filedialog.askopenfilename(title="Choose the first source JSON file")
        self.source1_label.config(text="Source File 1 selected: " + self.source1_path)

    def choose_source2(self):
        self.source2_path = filedialog.askopenfilename(title="Choose the second source JSON file")
        self.source2_label.config(text="Source File 2 selected: " + self.source2_path)

    def choose_final(self):
        self.final_path = filedialog.asksaveasfilename(title="Where do we have to save the final JSON file", defaultextension=".json", initialdir=".")
        self.final_label.config(text="Final file will be saved to: " + self.final_path)

    def merge_json_files(self, source1_data, source2_data):
        for key, value in source2_data.items():
            if key in source1_data:
                for sub_key, sub_value in enumerate(value):
                    if sub_value == "0: : true" and source1_data[key][sub_key] == "0: : false":
                        source1_data[key][sub_key] = "0: : true"
            else:
                source1_data[key] = value
        return source1_data

    def merge_files(self):
        try:
            with open(self.source1_path, 'r', encoding='utf-8') as source1_file:
                source1_data = json.load(source1_file)

            with open(self.source2_path, 'r', encoding='utf-8') as source2_file:
                source2_data = json.load(source2_file)

            fusion_data = self.merge_json_files(source1_data, source2_data)

            with open(self.final_path, 'w', encoding='utf-8') as final_file:
                json.dump(fusion_data, final_file, indent=4)

            self.status_label.config(text="Merge successful. Saved to " + self.final_path)
        except Exception as e:
            self.status_label.config(text="Error: " + str(e))

root = tk.Tk()
app = JSONMergerApp(root)
root.mainloop()





