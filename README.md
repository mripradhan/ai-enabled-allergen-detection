# AI Enabled Allergen Detection
Our preliminary submission for the Craft-N'-Code Hackathon, focusing on AI-Enabled Detection of Allergens. 

Our solution addresses the Automated Auditing Tools track. 

The specific problem statement is to ensure accurate allergen detection and labeling through AI-based systems. We aim to automatically analyze ingredient compositions and cross-reference them with allergen databases. This eliminates the need for manual checks, reducing human error and ensuring compliance with food safety standards during quality control audits.

## Requirements

To run this project, you need the following Python libraries:

- `customtkinter`
- `numpy`
- `tensorflow`
- `scikit-learn`
- `pandas`

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/mripradhan/ai-enabled-allergen-detection.git
   cd ai-enabled-allergen-detection
   ```

2. **Create a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Place the model file:**
   
   Ensure that the model file `fooda1model.h5` is located in the same directory as your script.

## Usage

1. **Run the application:**

   ```bash
   python GUIViewAllergensDraft.py
   ```

2. **Enter the nutritional values (currently only accepts allotted numbers based on priority, as seen in the Kaggle NB):**

   Fill in the fields for:
   - Food Product
   - Main Ingredient
   - Sweetener
   - Fat/Oil
   - Seasoning

3. **Click on the "Predict" button** to get the allergen prediction result in a pop-up message box.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
