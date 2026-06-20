# -*- coding: utf-8 -*-
import datetime
import xml.etree.ElementTree as ET
from xml.dom import minidom

from datos_efemerides import EFEMERIDES_JUNIO

def generar_feed():
    hoy = datetime.date.today()
    mes_actual = hoy.strftime("%m")
    
    # Dejamos fijo el "06-21" para usar tus datos reales de prueba
    clave_fecha = "06-21" 
    
    lista_efemerides = []
    if mes_actual == "06":
        lista_efemerides = EFEMERIDES_JUNIO.get(clave_fecha, [])
        
    if not lista_efemerides:
        print("⚠️ No hay efemérides cargadas para esta fecha.")
        return

    rss = ET.Element("rss", version="2.0")
    channel = ET.SubElement(rss, "channel")
    
    ET.SubElement(channel, "title").text = "Efemérides Diarias Bien FM"
    ET.SubElement(channel, "link").text = "https://bienfm.com.ar"
    ET.SubElement(channel, "description").text = "La nota única del día con las 10 efemérides juntas"
    ET.SubElement(channel, "language").text = "es-ar"
    
    # 1. Armamos el cuerpo de la nota única juntando las 10 efemérides en texto HTML limpio
    cuerpo_nota = '<div style="font-family: Arial, sans-serif; font-size: 16px; line-height: 1.6; color: #333;">'
    cuerpo_nota += '<p>Repasamos los hechos más importantes de un día como hoy en la historia, la música y el deporte:</p><br>'
    
    for efemeride in lista_efemerides:
        cuerpo_nota += f"<b>📌 [{efemeride['categoria']}] - {efemeride['titulo']}</b><br>"
        cuerpo_nota += f"{efemeride['contenido']}<br><br>"
        cuerpo_nota += '<hr style="border:0; border-top: 1px dashed #eee; margin: 15px 0;"><br>'
        
    cuerpo_nota += '<p style="font-size: 13px; color: #777; text-align: center;">Una producción exclusiva de <b>Bien FM 106.3</b></p>'
    cuerpo_nota += '</div>'
    
    # 2. Creamos UN SOLO ITEM para todo el día
    item = ET.SubElement(channel, "item")
    
    # Título general de la única noticia que saldrá en portada
    ET.SubElement(item, "title").text = f"Efemérides del {hoy.strftime('%d/%m')}: Diez historias de un día como hoy"
    
    # Metemos todo el choclo de las 10 efemérides juntas en la descripción
    ET.SubElement(item, "description").text = f"<![CDATA[{cuerpo_nota}]]>"
    ET.SubElement(item, "pubDate").text = hoy.strftime("%a, %d %b %Y 00:01:00 -0300")
    ET.SubElement(item, "guid").text = f"efemerides-completas-{clave_fecha}-{hoy.year}"
    
    # Imagen de portada genérica para la nota del día (podés cambiarla por el logo de tu radio si preferís)
    imagen_portada = "https://images.unsplash.com/photo-1506784983877-45594efa4cbe?w=800&auto=format&fit=crop"
    ET.SubElement(item, "enclosure", url=imagen_portada, length="123456", type="image/jpeg")
    
    # Guardar archivo XML
    xml_str = ET.tostring(rss, encoding="utf-8")
    reparsed = minidom.parseString(xml_str)
    xml_bonito = reparsed.toprettyxml(indent="  ")
    xml_bonito = xml_bonito.replace("&lt;![CDATA[", "<![CDATA[").replace("]]&gt;", "]]>")
    
    nombre_archivo = "efemerides_bienfm.xml"
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write(xml_bonito)
        
    print(f"✅ RSS generado con éxito como nota única agrupada.")

if __name__ == "__main__":
    generar_feed()
