import google.generativeai as genai
import json
import os
import datetime

genai.configure(api_key=os.environ.get('GEMINI_API_KEY'))

def generate_daily_advice():
    """
    Genera un consejo diario utilizando el modelo de IA de Gemini
    y lo guarda en un archivo JSON.
    """
    try:
        model = genai.GenerativeModel('gemini-2.0-flash')

        prompt = (
            "Eres un experto profesional en masoterapia, salud integral y bienestar, con experiencia en tratar a pacientes de todas las edades y condiciones. "
            "Genera un consejo diario, profesional, claro y útil, redactado en nombre de la empresa 'Relax Natural Zen', que atiende a pacientes —no clientes— con enfoque humano, ético y personalizado. "
            "El mensaje debe reflejar un compromiso genuino con el bienestar físico y emocional de las personas, transmitiendo confianza, curiosidad y conexión. "
            "Debe estar redactado en un lenguaje profesional pero accesible, evitando tecnicismos complejos, sin sonar informal o comercial. "
            "El consejo debe combinar temas como: "
            "1. Beneficios reales de los masajes que ofrecemos (relajante, deportivo, descontracturante, drenaje linfático, reflexología podal y manual, masaje reductivo, reafirmante, piedras calientes, copas suecas, maderoterapia, aromaterapia, desintoxicación iónica, entre otros). "
            "2. Sugerencias prácticas de alimentación saludable y bienestar diario, como cantidad adecuada de agua, tiempo de caminata según peso, etc. "
            "3. Consejos sobre postura o ejercicios simples para aliviar tensiones. "
            "4. Recomendaciones de infusiones naturales, hábitos sanos o curiosidades educativas sobre salud y bienestar. "
            "Incluye que Relax Natural Zen ofrece servicio a domicilio en toda la zona metropolitana de forma sutil y natural, sin que parezca publicidad directa. "
            "El consejo debe tener entre 80 y 100 palabras, incluir 1 o 2 emojis ubicados de forma estratégica para hacerlo más atractivo visualmente. "
            "Permite una mención breve y sutil de los servicios o acompañamiento que ofrecemos, sin sobrepasar el límite de palabras. "
            "Finaliza con una frase distinta cada vez que invite al lector a volver por más consejos, que sea cálida, profesional y genuina, transmitiendo continuidad en el cuidado del bienestar. "
            "Evita repetir exactamente las mismas palabras todos los días. "
            "Formato final: 'Consejo del día: [Tu consejo aquí] [Emojis] [Frase final de invitación].'"
        )

        response = model.generate_content(prompt)
        advice_text = response.candidates[0].content.parts[0].text
        today_date = datetime.date.today().isoformat()

        advice_data = {
            "date": today_date,
            "advice": advice_text
        }

        file_path = 'daily_advice.json'

        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(advice_data, f, ensure_ascii=False, indent=4)

        print(f"Consejo del día generado y guardado en {file_path}")

    except Exception as e:
        print(f"Se produjo un error al generar o guardar el consejo: {e}")

if __name__ == "__main__":
    print("Generando consejo del día...")
    generate_daily_advice()
