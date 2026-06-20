# -*- coding: utf-8 -*-
import datetime
import xml.etree.ElementTree as ET
from xml.dom import minidom

from datos_efemerides import EFEMERIDES_JUNIO

def generar_feed():
    hoy = datetime.date.today()
    mes_actual = hoy.strftime("%m")
    
    # Dejamos fijo el "06-21" para la prueba
    clave_fecha = "06-21" 
    
    lista_efemerides = []
    if mes_actual == "06":
        lista_efemerides = EFEMERIDES_JUNIO.get(clave_fecha, [])
        
    if not lista_efemerides:
        print("⚠️ No hay efemérides cargadas.")
        return

    rss = ET.Element("rss", version="2.0")
    channel = ET.SubElement(rss, "channel")
    
    ET.SubElement(channel, "title").text = "Efemérides Diarias Bien FM"
    ET.SubElement(channel, "link").text = "https://bienfm.com.ar"
    ET.SubElement(channel, "description").text = "Efemérides del día para Bien FM"
    ET.SubElement(channel, "language").text = "es-ar"
    
    # 1. Armamos el texto plano usando saltos de línea estándar (\n) en vez de HTML
    cuerpo_texto = "Repasamos los hechos más importantes de un día como hoy en la historia, la música y el deporte:\n\n"
    
    for efemeride in lista_efemerides:
        cuerpo_texto += f"📌 [{efemeride['categoria']}] - {efemeride['titulo']}\n"
        cuerpo_texto += f"{efemeride['contenido']}\n"
        cuerpo_texto += "-----------------------------------------\n\n"
        
    cuerpo_texto += "Una producción exclusiva de Bien FM 106.3"
    
    # 2. Creamos el ITEM único para la sección
    item = ET.SubElement(channel, "item")
    
    # Título de la noticia
    ET.SubElement(item, "title").text = f"Efemérides del {hoy.strftime('%d/%m')}: Diez historias de un día como hoy"
    
    # Mandamos el texto limpio de forma directa
    ET.SubElement(item, "description").text = cuerpo_texto
    ET.SubElement(item, "pubDate").text = hoy.strftime("%a, %d %b %Y 00:01:00 -0300")
    ET.SubElement(item, "guid").text = f"efemerides-texto-{clave_fecha}-{hoy.year}"
    
    # Categoría para que calce bajo tu barra turquesa
    ET.SubElement(item, "category").text = "Efemérides"
    
    # Imagen de portada de la nota
    imagen_portada = "https://images.unsplash.com/photo-1506784983877-45594efa4cbe?w=800&auto=format&fit=crop"
    ET.SubElement(item, "enclosure", url=imagen_portada, length="123456", type="image/jpeg")
    
    # Guardar archivo XML
    xml_str = ET.tostring(rss, encoding="utf-8")
    reparsed = minidom.parseString(xml_str)
    xml_bonito = reparsed.toprettyxml(indent="  ")
    
    nombre_archivo = "efemerides_bienfm.xml"
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write(xml_bonito)
        
    print(f"✅ RSS de texto plano generado con éxito.")

if __name__ == "__main__":
    generar_feed()
