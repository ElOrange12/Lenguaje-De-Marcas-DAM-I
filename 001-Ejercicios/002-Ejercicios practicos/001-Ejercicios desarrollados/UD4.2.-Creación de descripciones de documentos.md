En este ejercicio se profundiza en el uso de **XML Schema Definition (XSD)**, una tecnología que permite definir de forma precisa la estructura y los tipos de datos que debe cumplir un documento XML. A diferencia de un XML simple, un esquema XSD actúa como una norma o contrato que garantiza que los datos almacenados cumplen una estructura concreta.

Este tipo de validación es fundamental en entornos profesionales, donde los documentos XML son intercambiados entre aplicaciones y es necesario asegurar la coherencia y fiabilidad de la información.

---

El punto de partida del ejercicio es un **documento XML de referencia**, que representa la información de una persona. Este documento contiene una etiqueta raíz `<persona>` y varios elementos hijo como `<nombre>`, `<apellidos>` y `<telefonos>`.

Para asociar el documento XML con un esquema XSD, se utilizan los atributos `xmlns:xsi` y `xsi:noNamespaceSchemaLocation` en la etiqueta raíz:

```
    <persona xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="002-esquema.xsd">
```

Estos atributos indican que el documento debe validarse utilizando el esquema definido en el archivo `002-esquema.xsd`.

Dentro del documento XML se definen los elementos según la estructura esperada por el esquema. Por ejemplo, el nombre y los apellidos se representan como texto:

```
    <nombre>Juan</nombre>
    <apellidos>Garcia Lopez</apellidos>
```

Para los números de teléfono se utiliza una estructura jerárquica, donde una etiqueta contenedora `<telefonos>` agrupa uno o varios elementos `<telefono>`:

```
    <telefonos>
        <telefono>987654321</telefono>
    </telefonos>
```

El esquema XSD correspondiente define qué elementos son obligatorios, qué tipos de datos deben contener (por ejemplo `string` o `integer`) y cuántas veces pueden repetirse. De esta forma, si el documento XML no cumple estas reglas, podrá ser detectado como inválido por un validador XML.

Finalmente, se cierra la etiqueta raíz `<persona>`, dejando el documento correctamente formado y validable según el esquema.

---

```
    <?xml version="1.0" encoding="UTF-8"?>
    <persona xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="002-esquema.xsd">
    <nombre>Juan</nombre>
    <apellidos>Garcia Lopez</apellidos>
    <telefonos>
        <telefono>987654321</telefono>
    </telefonos>
    </persona>
```

**Notas:**

- El documento comienza con la declaración XML.
- Se vincula el XML con un esquema XSD externo.
- Existe una única etiqueta raíz.
- Los elementos respetan la estructura definida en el esquema.
- Los datos cumplen los tipos establecidos por el XSD.

---

Este ejercicio permite comprender la importancia de los esquemas XSD en el uso de XML. Definir un esquema aporta una estructura clara y consistente, facilita la validación de documentos y reduce errores en el intercambio de información entre sistemas. El uso de XSD es una práctica habitual en aplicaciones profesionales, ya que garantiza que los datos XML cumplen unas reglas comunes y pueden ser procesados de forma segura y eficiente.