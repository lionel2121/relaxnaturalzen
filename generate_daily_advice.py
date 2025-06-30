import os
import json
import datetime
import google.generativeai as genai

# Configura tu API Key de Gemini
# Importante: No coloques tu API key directamente aquí.
# La leeremos de una variable de entorno segura en GitHub Actions.
# Asegúrate de que esta variable de entorno esté configurada en GitHub Secrets.
GOOGLE_API_KEY = os.getenv('GEMINI_API_KEY')

if not GOOGLE_API_KEY:
    print("Error: La variable de entorno GEMINI_API_KEY no está configurada.")
    exit(1)

genai.configure(api_key=GOOGLE_API_KEY)

def generate_advice():
    """
    Genera un consejo diario sobre bienestar, relajación o masajes utilizando Gemini.
    """
    try:
        model = genai.GenerativeModel('gemini-2.0-flash')
        # Puedes ajustar el prompt para obtener el tipo de consejo que desees
        prompt = "Genera un consejo diario breve sobre bienestar, relajación o los beneficios de los masajes, enfocado en la armonía cuerpo-mente. Utiliza un tono cálido y motivador. Debe ser conciso, idealmente una o dos oraciones. Máximo 50 palabras."
        
        response = model.generate_content(prompt)
        advice_text = response.candidates[0].content.parts[0].text
        
        # Opcional: Limpiar el texto si la IA añade asteriscos o formato no deseado
        advice_text = advice_text.replace('*', '').strip()

        return advice_text
    except Exception as e:
        print(f"Error al generar el consejo con Gemini: {e}")
        return "Tómate un momento para respirar profundamente y encontrar la calma en tu día." # Consejo de fallback

def save_advice(advice, file_path='daily_advice.json'):
    """
    Guarda el consejo y la fecha actual en un archivo JSON.
    """
    current_date = datetime.date.today().isoformat()
    data = {
        "advice": advice,
        "date": current_date
    }
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Consejo del día guardado en {file_path}")
    except Exception as e:
        print(f"Error al guardar el archivo JSON: {e}")

if __name__ == "__main__":
    print("Generando consejo del día...")
    advice = generate_advice()
    # Si daily_advice.json está en la raíz, usa 'daily_advice.json'
    # Si está en una subcarpeta como 'data/', usa 'data/daily_advice.json'
    # Asegúrate de que la ruta coincida con donde creaste el archivo JSON en el Paso 1
    save_advice(advice, file_path='daily_advice.json') # O 'data/daily_advice.json'
