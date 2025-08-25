# Inside src/main.py

import google.generativeai as genai

# --- CONFIGURATION ---
API_KEY = "AIzaSyAmaLR7D65-lOwnKveKaKxyJ80s8ll8vZA" # Make sure to put your key here

# --- DO NOT EDIT BELOW THIS LINE ---

if "PASTE_YOUR_API_KEY_HERE" in API_KEY:
    print("ERROR: Please open src/main.py and replace 'PASTE_YOUR_API_KEY_HERE' with your actual Google AI API key.")
    exit()

try:
    genai.configure(api_key=API_KEY)

    # --- ADVANCED GENERATION CONFIGURATION ---
    # Here we can control the AI's behavior.
    generation_config = {
      "temperature": 0.3,  # We set a low temperature for more predictable, correct code
     
    }

    # Initialize the model WITH our new configuration
    print("Initializing the AI model with custom configuration...")
    model = genai.GenerativeModel(
        model_name='gemini-1.5-flash',
        generation_config=generation_config
    )

    # A more advanced, code-focused prompt
    
    prompt = "genearte the ICE-61131-3 standard PLC program for the control the pipa A,control pipe B.when tank fill 70% turn on pipe A.when tank fill 80% turn on pipe B "

    print(f"Sending the prompt...")
    response = model.generate_content(prompt)

    # --- PRINT THE RESPONSE ---
    print("\n--- AI Generated Structured Text ---")
    print(response.text)
    print("------------------------------------")

    # Let's also check our token usage
    print(f"\nToken Usage: {response.usage_metadata.total_token_count} tokens")

except Exception as e:
    print(f"\nAn error occurred. Please check your API key and internet connection.")
    print(f"Error details: {e}")