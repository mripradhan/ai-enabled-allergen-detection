import customtkinter as ctk  # Import CustomTkinter
from tkinter import messagebox
import numpy as np
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler
import pandas as pd

# Load the model
model = load_model('fooda1model.h5')

# Dummy data to fit scaler (use the actual training data or saved scaler object)
X_train = pd.DataFrame([[0]*5])  # Adjust the shape based on your features
scaler = StandardScaler().fit(X_train)

# Function to make a prediction
def predict_allergen():
    try:
        # Get values from entry fields
        Food_Product = float(fat_entry.get())
        Main_Ingredient = float(sugar_entry.get())
        Sweetener = float(carbs_entry.get())
        Fat_Oil = float(protein_entry.get())
        Seasoning = float(fiber_entry.get())
        
        # Create an array from inputs
        input_data = np.array([[Food_Product, Main_Ingredient, Sweetener, Fat_Oil, Seasoning]])
        
        # Scale input data
        input_data_scaled = scaler.transform(input_data)
        
        # Make prediction
        prediction = model.predict(input_data_scaled)
        
        # Convert prediction to label
        if prediction[0] > 0.5:
            result = "Contains allergens"
        else:
            result = "Does not contain allergens"
        
        # Display result in a messagebox
        messagebox.showinfo("Prediction Result", result)
    
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

# Create the GUI window
ctk.set_appearance_mode("dark")  # Set dark mode
ctk.set_default_color_theme("blue")  # Set the default color theme
window = ctk.CTk()  # Use CustomTkinter window
window.title("Allergen Predictor")

# Set up custom font
ctk.CTkFont(family="Times New Roman", size=60)  # Heading font
custom_font = ctk.CTkFont(family="Times New Roman", size=50)  # Entry and button font
title_font = ctk.CTkFont(family="Times New Roman", size=70)  # Entry and button font


# Create a frame to hold the widgets and center them
frame = ctk.CTkFrame(window)
frame.pack(expand=True)

# Add a heading
heading_label = ctk.CTkLabel(frame, text="AI-Enabled Allergen Detection", text_color='cyan', font=title_font)
heading_label.grid(row=0, columnspan=2, pady=40)  # Increased spacing for heading

# Input labels and fields with cyan text
label_color = 'lightblue'
entry_color = 'black'

ctk.CTkLabel(frame, text="Food Product", text_color=label_color, font=custom_font).grid(row=1, pady=(20, 10))  # Increased spacing
fat_entry = ctk.CTkEntry(frame, text_color='lightblue', font=custom_font)
fat_entry.grid(row=1, column=1, pady=(10, 20))  # Increased spacing

ctk.CTkLabel(frame, text="Main Ingredient", text_color=label_color, font=custom_font).grid(row=2, pady=(20, 10))  # Increased spacing
sugar_entry = ctk.CTkEntry(frame, text_color='lightblue', font=custom_font)
sugar_entry.grid(row=2, column=1, pady=(10, 20))  # Increased spacing

ctk.CTkLabel(frame, text="Sweetener", text_color=label_color, font=custom_font).grid(row=3, pady=(20, 10))  # Increased spacing
carbs_entry = ctk.CTkEntry(frame, text_color='lightblue', font=custom_font)
carbs_entry.grid(row=3, column=1, pady=(10, 20))  # Increased spacing

ctk.CTkLabel(frame, text="Fat/Oil", text_color=label_color, font=custom_font).grid(row=4, pady=(20, 10))  # Increased spacing
protein_entry = ctk.CTkEntry(frame, text_color='lightblue', font=custom_font)
protein_entry.grid(row=4, column=1, pady=(10, 20))  # Increased spacing

ctk.CTkLabel(frame, text="Seasoning", text_color=label_color, font=custom_font).grid(row=5, pady=(20, 10))  # Increased spacing
fiber_entry = ctk.CTkEntry(frame, text_color='lightblue', font=custom_font)
fiber_entry.grid(row=5, column=1, pady=(10, 20))  # Increased spacing

# Predict button with light blue background and black text
predict_button = ctk.CTkButton(frame, text="Predict", command=predict_allergen, fg_color='lightblue', text_color='black', font=custom_font)
predict_button.grid(row=6, column=1, pady=(40, 20))  # Increased spacing

# Start the GUI loop
window.mainloop()