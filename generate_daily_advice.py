import google.generativeai as genai
import json
import os
from datetime import datetime

# Configura tu clave de API de Gemini desde las variables de entorno de GitHub Actions
# La clave se inyecta de forma segura a través de ${{ secrets.GEMINI_API_KEY }}
genai.configure(api_key=os.environ.get('GEMINI_API_KEY'))

# Define el modelo a usar (el más eficiente para generación de texto)
# Usamos gemini-2.5-flash-lite para optimizar costo y velocidad
model = genai.GenerativeModel('gemini-2.5-flash-lite')

# Define el prompt para generar el consejo diario
# Este prompt incorpora todas tus especificaciones, Leo:
# - Tono profesional y experto en bienestar integral.
# - Temas variados (masajes, automasajes, alimentación, respiración, sueño, etc.).
# - Longitud específica (80-100 palabras).
# - Inclusión de emojis acordes al contenido.
# - Llamada a la acción para reservar un masaje.
prompt = """
Eres un masajista profesional y experto en bienestar integral de "Relax Natural Zen".
Tu objetivo es escribir un "Consejo del Día" inspirador, calmante y práctico para una página web.
El consejo debe sonar como si fuera escrito por un profesional empapado en técnicas de masajes,
automasajes, alimentación saludable (agua, frutas, verduras, productos naturales),
ejercicios sencillos, consejos de respiración, la importancia del sueño y descanso reparador,
técnicas de mindfulness o meditación, y consejos de postura/ergonomía.

El consejo debe tener entre 80 y 100 palabras.
Incluye 2 o 3 emojis relevantes y agradables que complementen el contenido del consejo.
Finaliza el consejo con una invitación sutil pero clara para reservar un masaje en "Relax Natural Zen".
Utiliza variaciones de la frase "Déjanos cuidarte, tu bienestar es nuestra prioridad. ¡Agenda tu cita!"
o "Tu bienestar es nuestra prioridad. ¡Agenda tu masaje en Relax Natural Zen hoy mismo!"
o "Permítenos ser tu oasis de bienestar. ¡Reserva tu experiencia en Relax Natural Zen!"

Ejemplos de temas a considerar:
- Un consejo sobre la importancia de la hidratación y cómo se relaciona con la flexibilidad muscular.
- Una técnica de automasaje simple para cuello y hombros al final del día.
- La relación entre una dieta rica en antioxidantes y la energía corporal.
- Un ejercicio de respiración consciente para reducir el estrés.
- La importancia de estirar suavemente por la mañana.
- Cómo un masaje profesional puede complementar tus esfuerzos de autocuidado.
- Consejos para mejorar la calidad del sueño.
- La conexión entre la postura y la tensión en la espalda.
- El poder de la aromaterapia para la relajación.

Asegúrate de que cada consejo sea único y diferente cada vez.
"""

def generate_daily_advice():
    """Genera un consejo diario usando la API de Gemini y lo guarda en un archivo JSON."""
    try:
        print("Generando consejo del día...")
        # Genera el contenido con el prompt definido
        response = model.generate_content(prompt)
        
        # Accede al texto generado
        advice_text = response.candidates[0].content.parts[0].text

        # Obtiene la fecha actual en el formato deseado
        current_date = datetime.now().strftime("%d de %B de %Y")

        # Crea el diccionario con el consejo y la fecha
        advice_data = {
            "advice": advice_text,
            "date": current_date
        }

        # Guarda el consejo en un archivo JSON
        file_path = os.path.join(os.getcwd(), 'daily_advice.json')
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(advice_data, f, ensure_ascii=False, indent=4)
        
        print(f"Consejo del día guardado en {file_path}")

    except Exception as e:
        print(f"Ocurrió un error al generar o guardar el consejo: {e}")

if __name__ == "__main__":
    generate_daily_advice()
