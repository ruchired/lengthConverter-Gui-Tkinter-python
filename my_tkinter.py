import tkinter as tk
from tkinter import ttk

def length_converter(value, from_unit, to_unit):
    # Conversion factors
    factors = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1,
        "km": 1000,
        "in": 0.0254,
        "ft": 0.3048,
        "yd": 0.9144,
        "mi": 1609.34
    }
    
    # Convert to meters first
    meters = value * factors[from_unit]
    
    # Then convert to the target unit
    result = meters / factors[to_unit]
    return result

class LengthConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Length Converter")
        self.root.geometry("450x350")
        self.root.configure(bg="#f5f5f5") 
        # Title Label
        title_label = tk.Label(root, text="Length Converter", font=("Helvetica", 16, "bold"), bg="#4CAF50", fg="white", pady=10)
        title_label.pack(fill=tk.X)

        # Input Frame
        input_frame = tk.Frame(root, bg="#f5f5f5", padx=20, pady=20)
        input_frame.pack(pady=10)

        # Value Entry
        ttk.Label(input_frame, text="Enter Value:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.value_entry = ttk.Entry(input_frame, width=20, font=("Arial", 12))
        self.value_entry.grid(row=0, column=1, padx=10, pady=5)

        # From Unit Dropdown
        ttk.Label(input_frame, text="From Unit:", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.from_unit = ttk.Combobox(input_frame, values=["mm", "cm", "m", "km", "in", "ft", "yd", "mi"], state="readonly", font=("Arial", 12))
        self.from_unit.grid(row=1, column=1, padx=10, pady=5)
        self.from_unit.current(0)

        # To Unit Dropdown
        ttk.Label(input_frame, text="To Unit:", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        self.to_unit = ttk.Combobox(input_frame, values=["mm", "cm", "m", "km", "in", "ft", "yd", "mi"], state="readonly", font=("Arial", 12))
        self.to_unit.grid(row=2, column=1, padx=10, pady=5)
        self.to_unit.current(0)

        # Convert Button
        self.convert_button = ttk.Button(root, text="Convert", command=self.convert, style="TButton")
        self.convert_button.pack(pady=20)

        # Result Label
        self.result_label = tk.Label(root, text="", font=("Arial", 14), bg="#f5f5f5", fg="#333")
        self.result_label.pack(pady=10)

        # Styling
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Arial", 12), padding=10)

    def convert(self):
        try:
            value = float(self.value_entry.get())
            from_unit = self.from_unit.get()
            to_unit = self.to_unit.get()
            result = length_converter(value, from_unit, to_unit)
            self.result_label.config(text=f"{value} {from_unit} = {result:.4f} {to_unit}")
        except ValueError:
            self.result_label.config(text="Invalid input. Please enter a valid number.", fg="red")
        except KeyError:
            self.result_label.config(text="Please select valid units.", fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    app = LengthConverterApp(root)
    root.mainloop()
