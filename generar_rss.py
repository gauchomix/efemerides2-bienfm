# -*- coding: utf-8 -*-
import datetime
from datos_efemerides import EFEMERIDES_JUNIO

def generar_widget():
    hoy = datetime.date.today()
    mes_actual = hoy.strftime("%m")
    
    # Dejamos fijo el "06-21" para usar tus 10 datos reales de prueba
    clave_fecha = "06-21" 
    
    lista_efemerides = EFEMERIDES_JUNIO.get(clave_fecha, [])
    
    if not lista_efemerides:
        print("⚠️ No hay efemérides cargadas.")
        return

    # Creamos el diseño visual del Widget en HTML y CSS
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
        .efemeride-item {{
            padding: 15px 0;
            border-bottom: 1px dashed #e0e0e0;
        }}
        .efemeride-item:last-child {{
            border-bottom: none;
        }}
        .categoria {{
            display: inline-block;
            background-color: #00ca99; /* El color verde turquesa de tu sección */
            color: #ffffff;
            font-size: 11px;
            font-weight: bold;
            padding: 3px 8px;
            border-radius: 4px;
            text-transform: uppercase;
            margin-bottom: 6px;
        }}
        .titulo {{
            font-size: 16px;
            font-weight: bold;
            color: #111111;
            margin: 0 0 6px 0;
        }}
        .texto {{
            font-size: 14.5px;
            line-height: 1.5;
            color: #444444;
            margin: 0;
        }}
        .footer {{
            text-align: center;
            font-size: 12px;
            color: #999999;
            margin-top: 20px;
            padding-top: 10px;
            border-top: 1px solid #eeeeee;
        }}
    </style>
</head>
<body>
    <div class="widget-container">
"""

    # Inyectamos las 10 efemérides dentro del diseño
    for efemeride in lista_efemerides:
        html_content += f"""
        <div class="efemeride-item">
            <span class="categoria">{efemeride['categoria']}</span>
            <h3 class="titulo">{efemeride['titulo']}</h3>
            <p class="texto">{efemeride['contenido']}</p>
        </div>
        """

    html_content += f"""
        <div class="footer">
            Efemérides del {hoy.strftime('%d/%m')} • Una producción de <b>Bien FM 106.3</b>
        </div>
    </div>
</body>
</html>
"""

    # Guardamos el archivo como una página web fija que leerá el widget
    nombre_archivo = "index.html"
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write(html_content)
        
    print("✅ Widget HTML generado con éxito bajo el nombre 'index.html'.")

if __name__ == "__main__":
    generar_widget():
