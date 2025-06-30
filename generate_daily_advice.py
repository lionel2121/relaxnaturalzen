import google.generativeai as genai
import json
import os
import datetime

# Configura tu clave de API de Gemini.
# Se recomienda usar un secreto de GitHub Actions para GEMINI_API_KEY.
# Por ejemplo, en tu flujo de trabajo de GitHub, tendrías:
# env:
#   GEMINI_API_KEY: ${{ secrets.GEMINI_API_KEY }}
genai.configure(api_key=os.environ.get('GEMINI_API_KEY'))

def generate_daily_advice():
    """
    Genera un consejo diario utilizando el modelo de IA de Gemini
    y lo guarda en un archivo JSON.
    """
    try:
        # Define el modelo de IA a utilizar.
        # 'gemini-2.0-flash' es un modelo compatible para generación de contenido.
        model = genai.GenerativeModel('gemini-2.0-flash')

        # Define el prompt para generar el consejo.
        # Personaliza el prompt para que el consejo sea relevante para tu negocio
        # de masajes "Relax Natural Zen" y para Leo, un masajista no vidente.
        prompt = (
            "Eres un experto en masajes y bienestar. Genera un consejo diario "
            "corto, inspirador y útil para un masajista profesional no vidente llamado Leo, "
            "que dirige una empresa de masajes llamada 'Relax Natural Zen'. "
            "Los masajes que ofrece incluyen: relajante, descontracturante o terapéutico, "
            "drenaje linfático, reductivo y reafirmante, maderoterapia, aromaterapia, "
            "reflexología, desintoxicación iónica, masaje deportivo, yesoterapia, "
            "masaje o limpieza facial, terapia termo reductora, piedras calientes, "
            "masaje sueco, tratamiento de movimiento del colon o infección intestinal. "
            "El consejo debe ser positivo y enfocado en el bienestar, la conexión con el cliente, "
            "la importancia del tacto o la energía. "
            "Formato: 'Consejo del día: [Tu consejo aquí]'."
        )

        # Genera el contenido utilizando el modelo de IA.
        response = model.generate_content(prompt)

        # Extrae el texto del consejo.
        advice_text = response.candidates[0].content.parts[0].text

        # Obtiene la fecha actual en formato ISO 8601 (YYYY-MM-DD).
        today_date = datetime.date.today().isoformat()

        # Crea el objeto JSON.
        advice_data = {
            "date": today_date,
            "advice": advice_text
        }

        # Define la ruta del archivo JSON.
        file_path = 'daily_advice.json'

        # Guarda el consejo en el archivo JSON.
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(advice_data, f, ensure_ascii=False, indent=4)

        print(f"Consejo del día generado y guardado en {file_path}")

    except Exception as e:
        print(f"Se produjo un error al generar o guardar el consejo: {e}")

if __name__ == "__main__":
    print("Generando consejo del día...")
    generate_daily_advice()
