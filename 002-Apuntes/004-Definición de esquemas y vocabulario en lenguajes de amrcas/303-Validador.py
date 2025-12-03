# pip3 install lxml --break-system-packages

from lxml import etree

xml_doc = etree.parse("201-Documento de referencia.xml")
xsd_doc = etree.parse("202-Esquema.xsd")

schema = etree.XMLSchema(xsd_doc)

print(schema.validate(xml_doc))
