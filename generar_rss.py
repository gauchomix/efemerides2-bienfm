# -*- coding: utf-8 -*-
import datetime

# Importamos las efemérides del archivo de datos
from datos_efemerides import EFEMERIDES_JUNIO

def generar_widget():
    # 1. Obtener la fecha real de hoy de forma automática
    hoy = datetime.date.today()
    mes_actual = hoy.strftime("%m")
    clave_fecha = hoy.strftime("%m-%d") # Ej: "06-20"
    
    # Formatear la fecha en castellano para el título del widget
    meses = {
        "01": "Enero", "02": "Febrero", "03": "Marzo", "04": "Abril", 
        "05": "Mayo", "06": "Junio", "07": "Julio", "08": "Agosto", 
        "09": "Septiembre", "10": "Octubre", "11": "Noviembre", "12": "Diciembre"
    }
    nombre_mes = meses.get(mes_actual, "")
    texto_fecha_hoy = f"{hoy.day} de {nombre_mes}"

    # 2. Buscar las efemérides del día real en la base de datos
    lista_efemerides = []
    if mes_actual == "06":
        lista_efemerides = EFEMERIDES_JUNIO.get(clave_fecha, [])

    # Si por alguna razón la lista está vacía (ej: un día que falte cargar), 
    # le metemos un texto elegante de respaldo para que no quede en blanco
    if not lista_efemerides:
        lista_efemerides = [
            {
                "categoria": "MÚSICA Y CULTURA",
                "titulo": f"Efemérides especiales del {texto_fecha_hoy}",
                "contenido": "Una jornada ideal para repasar los grandes hitos de nuestra historia popular y disfrutar la mejor compañía musical en el aire de la radio."
            }
        ]

    # 3. Diseño visual del Widget (HTML + CSS)
    html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Widget Efemérides Bien FM</title>
    <style>
        body {{
            font-family: 'Segoe UI', Arial, sans-serif;
            margin: 0;
            padding: 10px;
            background-color: #ffffff;
            color: #333333;
        }}
        .widget-container {{
            max-width: 100%;
            margin: 0 auto;
        }}
        .encabezado-widget {{
            font-size: 18px;
            font-weight: bold;
            color: #111111;
            border-bottom: 2px solid #00ca99;
            padding-bottom: 8px;
            margin-bottom: 15px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}
        .efemeride-item {{
            padding: 12px 0;
            border-bottom: 1px dashed #e0e0e0;
        }}
        .efemeride-item:last-child {{
            border-bottom: none;
        }}
        .categoria {{
            display: inline-block;
            background-color: #00ca99; /* Verde turquesa de tu portal */
            color: #ffffff;
            font-size: 10px;
            font-weight: bold;
            padding: 2px 6px;
            border-radius: 3px;
            text-transform: uppercase;
            margin-bottom: 5px;
        }}
        .titulo {{
            font-size: 15px;
            font-weight: bold;
            color: #111111;
            margin: 0 0 5px 0;
        }}
        .texto {{
            font-size: 13.5px;
            line-height: 1.45;
            color: #444444;
            margin: 0;
        }}
        .footer {{
            text-align: center;
            font-size: 11px;
            color: #888888;
            margin-top: 15px;
            padding-top: 8px;
            border-top: 1px solid #eeeeee;
        }}
    </style>
</head>
<body>
    <div class="widget-container">
        <div class="encabezado-widget">📅 Efemérides de Hoy {texto_fecha_hoy}</div>
"""

    # Inyectar las efemérides del día
    for efemeride in lista_efemerides:
        html_content += f"""
        <div class="efemeride-item">
            <span class="categoria">{efemeride['categoria']}</span>
            <h3 class="titulo">{efemeride['titulo']}</h3>
            <p class="texto">{efemeride['contenido']}</p>
        </div>
        """

    # PIE DE PÁGINA CORREGIDO CON LA FRECUENCIA 92.7
    html_content += f"""
        <div class="footer">
            Una producción exclusiva de <b>Bien FM 92.7</b> • Viví tu radio
        </div>
    </div>
</body>
</html>
"""

    # Guardar el archivo index.html para la web
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)
        
    print(f"✅ Widget actualizado con fecha dinámica ({texto_fecha_hoy}) y frecuencia 92.7.")

if __name__ == "__main__":
    generar_widget()
