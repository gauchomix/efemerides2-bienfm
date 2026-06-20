import datetime
import xml.etree.ElementTree as ET
from xml.dom import minidom

# Importamos las efemérides actualizadas
from datos_efemerides import EFEMERIDES_JUNIO

def generar_feed():
    hoy = datetime.date.today()
    mes_actual = hoy.strftime("%m")
    clave_fecha = hoy.strftime("%m-%d") # Ej: "06-21"
    
    # Obtenemos la lista de efemérides del día (si no hay, creamos una lista vacía)
    lista_efemerides = []
    if mes_actual == "06":
        lista_efemerides = EFEMERIDES_JUNIO.get(clave_fecha, [])
        
    # Si la lista está vacía por cualquier motivo, metemos contenido de respaldo
    if not lista_efemerides:
        lista_efemerides = [
            {"titulo": f"Efemérides del {hoy.strftime('%d/%m')} - Nota {i+1}", 
             "contenido": "Sumate a la sintonía de Bien FM para compartir la mejor información y música de nuestra región durante toda la jornada."}
            for i in range(5)
        ]

    # Armamos la estructura del RSS
    rss = ET.Element("rss", version="2.0")
    channel = ET.SubElement(rss, "channel")
    
    ET.SubElement(channel, "title").text = "Efemérides Diarias Bien FM"
    ET.SubElement(channel, "link").text = "https://bienfm.com.ar"
    ET.SubElement(channel, "description").text = "5 efemérides diarias automatizadas para el portal"
    ET.SubElement(channel, "language").text = "es-ar"
    
    # Recorremos las 5 efemérides del día y creamos un item para cada una
    for indice, efemeride in enumerate(lista_efemerides):
        item = ET.SubElement(channel, "item")
        ET.SubElement(item, "title").text = efemeride["titulo"]
        ET.SubElement(item, "description").text = efemeride["contenido"]
        ET.SubElement(item, "pubDate").text = hoy.strftime("%a, %d %b %Y 00:01:00 -0300")
        # El guid tiene que ser único para cada una de las 5 notas para que Locucionar lea las 5 por separado
        ET.SubElement(item, "guid").text = f"efemeride-{clave_fecha}-{hoy.year}-nota-{indice+1}"
    
    # Formatear el XML de manera limpia
    xml_str = ET.tostring(rss, encoding="utf-8")
    reparsed = minidom.parseString(xml_str)
    xml_bonito = reparsed.toprettyxml(indent="  ")
    
    # Guardamos el archivo listo para que lo lea el servidor de la radio
    nombre_archivo = "efemerides_bienfm.xml"
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write(xml_bonito)
        
    print(f"✅ RSS generado con éxito. Se crearon {len(lista_efemerides)} noticias para el día {clave_fecha}.")

if __name__ == "__main__":
    generar_feed()