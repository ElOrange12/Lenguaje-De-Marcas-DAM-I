En este ejercicio se trabaja el lenguaje **XML (eXtensible Markup Language)**, una tecnología ampliamente utilizada para almacenar y transportar información estructurada. XML comparte ciertas similitudes con HTML, como el uso de etiquetas, pero se diferencia en que permite crear **etiquetas personalizadas**, adaptadas a la información que se desea representar.

El objetivo principal de la práctica es aprender a crear documentos XML bien formados, respetando sus reglas básicas, como la existencia de una única etiqueta raíz y la correcta anidación de los elementos.

---

Todo documento XML comienza con una declaración inicial que indica la versión del lenguaje y la codificación utilizada:

```
    <?xml version="1.0" encoding="UTF-8"?>
```

Esta línea informa a los programas que lean el archivo de que se trata de un documento XML versión 1.0 y que utiliza codificación UTF-8, lo que permite incluir caracteres especiales sin problemas.

A continuación, se define la etiqueta raíz del documento:

```
    <persona>
```

En XML es obligatorio que exista una única etiqueta raíz que contenga todo el contenido del documento. En este caso, la raíz es `<persona>`, que representa a una persona concreta.

Dentro de esta etiqueta raíz se incluyen diferentes elementos hijo, que almacenan la información asociada a la persona:

```
    <nombre>Daniel</nombre>
    <apellidos>Oliveira Vidal</apellidos>
```

Cada elemento tiene una etiqueta de apertura y una de cierre, y contiene texto en su interior. XML es sensible a la estructura, por lo que es importante que las etiquetas estén correctamente cerradas y anidadas.

Para representar varios valores del mismo tipo, como números de teléfono, se utiliza una estructura jerárquica. Primero se crea una etiqueta contenedora `<telefonos>` y dentro de ella se repiten las etiquetas `<telefono>`:

```
    <telefonos>
        <telefono>123456789</telefono>
        <telefono>987654321</telefono>
    </telefonos>
```

Este enfoque permite agrupar información relacionada y facilita su lectura y procesamiento posterior por otros programas.

Finalmente, se cierra la etiqueta raíz del documento:

```
    </persona>
```

Con esto, el documento XML queda correctamente formado y listo para ser utilizado o validado.

---

```
    <?xml version="1.0" encoding="UTF-8"?>
    <persona>
        <nombre>Daniel</nombre>
        <apellidos>Oliveira Vidal</apellidos>
        <telefonos>
            <telefono>123456789</telefono>
            <telefono>987654321</telefono>
        </telefonos>
    </persona>
```

- El documento comienza con la declaración XML.
- Existe una única etiqueta raíz (`persona`).
- Las etiquetas están correctamente anidadas.
- Se utilizan etiquetas personalizadas adaptadas al contenido.
- Se agrupan varios elementos del mismo tipo dentro de un contenedor común.

---

Este ejercicio permite comprender los fundamentos de XML y su estructura básica. Se ha practicado la creación de un documento bien formado, con una etiqueta raíz, elementos hijo y subetiquetas repetidas. XML es una tecnología clave para el intercambio de datos estructurados y sigue siendo muy utilizada en servicios web, configuraciones y almacenamiento de información. Dominar estos conceptos es fundamental para avanzar en el desarrollo y la gestión de datos.