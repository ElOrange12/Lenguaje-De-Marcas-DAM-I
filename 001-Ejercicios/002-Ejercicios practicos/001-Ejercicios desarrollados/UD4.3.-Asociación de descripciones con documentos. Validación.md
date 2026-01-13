En este ejercicio se trabaja el concepto de **validación de documentos XML mediante esquemas XSD**, utilizando Python como herramienta de comprobación. La validación permite asegurar que un documento XML cumple una estructura concreta previamente definida, evitando errores de formato o incoherencias en los datos.

Este proceso es fundamental en aplicaciones web y sistemas que intercambian información estructurada, ya que garantiza la integridad y consistencia de los datos antes de ser procesados por otros programas.

---

El script comienza indicando la necesidad de instalar la librería `lxml`, que proporciona herramientas avanzadas para trabajar con XML y XSD en Python:

```
    # pip3 install lxml
```

A continuación, se importa el módulo `etree`, que permite parsear documentos XML y definir esquemas:

```
    from lxml import etree
```

El siguiente paso consiste en cargar tanto el documento XML como el esquema XSD. Para ello, se utiliza el método `etree.parse()`, que convierte los archivos en objetos de tipo `ElementTree`:

```
    documento = etree.parse("001-documento de referencia.xml")
    esquema_doc = etree.parse("002-esquema.xsd")
```

Estos objetos representan la estructura interna de los archivos y permiten trabajar con ellos desde Python.

Una vez cargado el esquema XSD, se crea una instancia de `XMLSchema`, pasándole como parámetro el árbol del esquema:

```
    esquema = etree.XMLSchema(esquema_doc)
```

Esta instancia contiene todas las reglas de validación definidas en el XSD, como los tipos de datos, la obligatoriedad de elementos y su estructura jerárquica.

Con el esquema ya definido, se procede a validar el documento XML utilizando el método `validate()`:

```
    resultado = esquema.validate(documento)
```

Este método devuelve un valor booleano:

- `True` si el documento XML cumple todas las reglas del esquema.

- `False` si existe algún error estructural o de tipo de dato.

Finalmente, se imprime el resultado de la validación por consola:

```
    print(resultado)
```

De esta forma, el programa indica claramente si el documento XML es válido o no según el esquema XSD proporcionado.

---

```
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
```

**Notas:**

- Se utiliza la librería `lxml` para trabajar con XML.
- Se cargan el documento XML y el esquema XSD.
- Se crea un objeto `XMLSchema`.
- Se valida el documento contra el esquema.
- El resultado se muestra por consola.

---

Este ejercicio demuestra cómo validar documentos XML utilizando esquemas XSD desde Python. La validación es un paso clave para asegurar que los datos cumplen una estructura definida y evitar errores en sistemas que dependen de información estructurada. El uso de esquemas junto con herramientas como `lxml` facilita la detección de problemas y mejora la fiabilidad de las aplicaciones que trabajan con lenguajes de marcas.