# -*- coding: utf-8 -*-
import datetime
import xml.etree.ElementTree as ET

from datos_efemerides import EFEMERIDES_JUNIO

def generar_feed():
    # Forzamos la fecha en texto limpio e inglés estándar para evitar que Locucionar se maree
    # Hoy es Sábado 20 de Junio de 2026
    fecha_rfc = "Sat, 20 Jun 2026 00:01:00 -0300"
    clave_fecha = "06-21" # Mantenemos tus 10 datos reales de prueba del 21
    
    lista_efemerides = EFEMERIDES_JUNIO.get(clave_fecha, [])
    
    if not lista_efemerides:
        print("⚠️ No hay efemérides cargadas.")
        return

    # Creamos el cuerpo juntando las 10 historias
    cuerpo_texto = "Historias y efemérides de un día como hoy:\n\n"
    for efemeride in lista_efemerides:
        cuerpo_texto += f"- [{efemeride['categoria']}] {efemeride['titulo']}: {efemeride['contenido']}\n\n"
    
    cuerpo_texto += "Una producción de Bien FM 106.3"

    # Construcción del XML sin caracteres ni funciones raras de formato
    rss = ET.Element("rss", version="2.0")
    channel = ET.SubElement(rss, "channel")
    
    ET.SubElement(channel, "title").text = "Efemerides Bien FM"
    ET.SubElement(channel, "link").text = "https://bienfm.com.ar"
    ET.SubElement(channel, "description").text = "Efemerides diarias"
    ET.SubElement(channel, "language").text = "es-ar"
    
    item = ET.SubElement(channel, "item")
    ET.SubElement(item, "title").text = "Efemerides Especiales de un dia como hoy"
    ET.SubElement(item, "description").text = cuerpo_texto
    ET.SubElement(item, "pubDate").text = fecha_rfc
    # Cambiamos radicalmente el GUID para que el sistema lo tome como algo totalmente nuevo
    ET.SubElement(item, "guid").text = "efemerides-sistema-nuevo-2026"
    ET.SubElement(item, "category").text = "Efemérides"
    ET.SubElement(item, "author").text = "contacto@bienfm.com.ar"
    
    # Imagen de portada estándar
    imagen_portada = "https://images.unsplash.com/photo-1506784983877-45594efa4cbe?w=800&auto=format&fit=crop"
    ET.SubElement(item, "enclosure", url=imagen_portada, length="123456", type="image/jpeg")
    
    # Guardar plano sin minidom (algunos formateadores meten saltos invisibles que rompen a Locucionar)
    tree = ET.ElementTree(rss)
    nombre_archivo = "efemerides_bienfm.xml"
    tree.write(nombre_archivo, encoding="utf-8", xml_declaration=True)
        
    print("✅ RSS estándar e internacional generado.")

if __name__ == "__main__":
    generar_feed()
