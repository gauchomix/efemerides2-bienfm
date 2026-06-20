# -*- coding: utf-8 -*-
import datetime
import xml.etree.ElementTree as ET
from xml.dom import minidom

from datos_efemerides import EFEMERIDES_JUNIO

def generar_feed():
    hoy = datetime.date.today()
    mes_actual = hoy.strftime("%m")
    
    # IMPORTANTE: Forzamos "06-21" para que use las 10 efemérides de prueba que cargamos
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
    ET.SubElement(channel, "description").text = "10 efemérides diarias con diseño e imágenes para Bien FM"
    ET.SubElement(channel, "language").text = "es-ar"
    
    for indice, efemeride in enumerate(lista_efemerides):
        # Diseñamos el cuerpo de la noticia usando HTML limpio
        descripcion_html = f"""<![CDATA[
        <div style="font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 600px; margin: 0 auto; padding: 10px; border: 1px solid #eee; border-radius: 8px;">
            <div style="text-align: center; margin-bottom: 15px;">
                <img src="{efemeride['imagen']}" alt="{efemeride['titulo']}" style="width: 100%; max-width: 550px; height: auto; border-radius: 6px; display: block; margin: 0 auto;" />
            </div>
            <span style="display: inline-block; background-color: #E3121A; color: #fff; font-size: 11px; font-weight: bold; padding: 3px 8px; border-radius: 3px; text-transform: uppercase; margin-bottom: 10px;">
                {efemeride['categoria']}
            </span>
            <p style="font-size: 16px; font-weight: normal; margin: 0 0 10px 0;">
                {efemeride['contenido']}
            </p>
            <hr style="border: 0; border-top: 1px dashed #ccc; margin-top: 15px;" />
            <p style="font-size: 12px; color: #777; text-align: center; margin: 0;">Es un aporte de <b>Bien FM 106.3</b> - Viví tu radio.</p>
        </div>
        ]]>"""
        
        item = ET.SubElement(channel, "item")
        # El título de la nota en el portal será el título de la efeméride
        ET.SubElement(item, "title").text = efemeride["titulo"]
        ET.SubElement(item, "description").text = descripcion_html.strip()
        ET.SubElement(item, "pubDate").text = hoy.strftime("%a, %d %b %Y 00:01:00 -0300")
        ET.SubElement(item, "guid").text = f"efemeride-{clave_fecha}-{hoy.year}-nota-{indice+1}"
    
    xml_str = ET.tostring(rss, encoding="utf-8")
    reparsed = minidom.parseString(xml_str)
    xml_bonito = reparsed.toprettyxml(indent="  ")
    
    # Reemplazo manual necesario para que Locucionar interprete el CDATA correctamente sin romper el XML
    xml_bonito = xml_bonito.replace("&lt;![CDATA[", "<![CDATA[").replace("]]&gt;", "]]>")
    
    nombre_archivo = "efemerides_bienfm.xml"
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write(xml_bonito)
        
    print(f"✅ RSS generado con {len(lista_efemerides)} notas de diseño.")

if __name__ == "__main__":
    generar_feed()
