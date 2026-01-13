# pip3 install lxml

from lxml import etree

# Cargamos el documento XML y el esquema XSD
documento = etree.parse("001-documento de referencia.xml")
esquema_doc = etree.parse("002-esquema.xsd")

# Definición del esquema
esquema = etree.XMLSchema(esquema_doc)

# Validación del documento
resultado = esquema.validate(documento)

# Interpretación del resultado
print(resultado)