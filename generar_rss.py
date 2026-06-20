# -*- coding: utf-8 -*-
import datetime
from datos_efemerides import EFEMERIDES_JUNIO

def generar_widget():
    hoy = datetime.date.today()
    mes_actual = hoy.strftime("%m")
    clave_fecha = hoy.strftime("%m-%d") # Ej: "06-20"
    
    # Días de la semana en español
    dias_semana = {
        0: "Lunes", 1: "Martes", 2: "Miércoles", 3: "Jueves",
        4: "Viernes", 5: "Sábado", 6: "Domingo"
    }
    nombre_dia_semana = dias_semana.get(hoy.weekday(), "")

    meses = {
        "01": "Enero", "02": "Febrero", "03": "Marzo", "04": "Abril", 
        "05": "Mayo", "06": "Junio", "07": "Julio", "08": "Agosto", 
        "09": "Septiembre", "10": "Octubre", "11": "Noviembre", "12": "Diciembre"
    }
    nombre_mes = meses.get(mes_actual, "")

    lista_efemerides = []
    if mes_actual == "06":
        lista_efemerides = EFEMERIDES_JUNIO.get(clave_fecha, [])

    if not lista_efemerides:
        lista_efemerides = [{"ano": hoy.strftime("%Y"), "contenido": "Sintonizá la mañana de la radio para repasar los grandes hitos de la historia y disfrutar la mejor compañía musical en el aire de Bien FM."}]

    # DISEÑO RETRO DE AGENDA BASADO EN TU IMAGEN
    html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Efemérides Bien FM</title>
    <style>
        body {{
            font-family: 'Georgia', 'Times New Roman', serif;
            margin: 0;
            padding: 15px;
            background-color: #f4ebd9; /* Fondo color crema suave */
            color: #2b2b2b;
        }}
        .widget-container {{
            max-width: 100%;
            margin: 0 auto;
            background-color: #f4ebd9;
        }}
        .header-radio {{
            font-family: 'Courier New', monospace;
            font-size: 13px;
            color: #4a5e51;
            letter-spacing: 2px;
            margin-bottom: 20px;
            border-bottom: 1px solid rgba(74, 94, 81, 0.2);
            padding-bottom: 5px;
            font-weight: bold;
        }}
        .block-title-container {{
            display: flex;
            align-items: center;
            margin-bottom: 25px;
        }}
        .date-badge {{
            background-color: #e6533c; /* Recuadro rojo de fecha */
            color: #ffffff;
            padding: 10px 15px;
            border-radius: 6px;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            margin-right: 15px;
            min-width: 45px;
        }}
        .date-badge .day {{
            font-size: 28px;
            font-weight: bold;
            line-height: 1;
            font-family: Arial, sans-serif;
        }}
        .date-badge .month-year {{
            font-size: 10px;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-top: 3px;
            font-family: Arial, sans-serif;
            font-weight: bold;
        }}
        .title-text {{
            font-size: 26px;
            font-weight: bold;
            color: #1a1a1a;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            line-height: 1.1;
        }}
        .title-text span {{
            display: block;
            font-size: 14px;
            color: #70624d;
            font-style: italic;
            text-transform: none;
            margin-top: 2px;
            font-weight: normal;
        }}
        .efemeride-row {{
            display: flex;
            align-items: flex-start;
            margin-bottom: 18px;
            padding-bottom: 15px;
            border-bottom: 1px dotted rgba(112, 98, 77, 0.25);
        }}
        .efemeride-row:last-child {{
            border-bottom: none;
            margin-bottom: 0;
        }}
        .ano-box {{
            background-color: #e6dec9; /* Fondo gris/beige claro del año */
            color: #2b2b2b;
            font-family: Arial, sans-serif;
            font-weight: bold;
            font-size: 13px;
            padding: 4px 8px;
            border-radius: 4px;
            margin-right: 15px;
            min-width: 38px;
            text-align: center;
        }}
        .texto-contenido {{
            font-size: 14.5px;
            line-height: 1.5;
            color: #2b2b2b;
            margin: 0;
            text-align: left;
        }}
        .footer {{
            text-align: center;
            font-size: 11px;
            color: #70624d;
            margin-top: 25px;
            padding-top: 10px;
            border-top: 1px solid rgba(112, 98, 77, 0.15);
            font-family: Arial, sans-serif;
        }}
    </style>
</head>
<body>
    <div class="widget-container">
        <div class="header-radio">☉ BIEN FM 92.7 · TANDIL</div>
        
        <div class="block-title-container">
            <div class="date-badge">
                <div class="day">{hoy.day}</div>
                <div class="month-year">{nombre_mes[:3]}<br>{hoy.year}</div>
            </div>
            <div class="title-text">
                EFEMÉRIDES
                <span>{nombre_dia_semana}</span>
            </div>
        </div>

        """

    for item in lista_efemerides:
        html_content += f"""
        <div class="efemeride-row">
            <div class="ano-box">{item['ano']}</div>
            <p class="texto-contenido">{item['contenido']}</p>
        </div>
        """

    html_content += f"""
        <div class="footer">
            Actualizado hoy, {hoy.day} de {nombre_mes.lower()} • Fuente: Wikipedia
        </div>
    </div>
</body>
</html>
"""

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)
        
    print("✅ Widget estilo Agenda Vintage (5 efemérides por día) generado con éxito.")

if __name__ == "__main__":
    generar_widget()
