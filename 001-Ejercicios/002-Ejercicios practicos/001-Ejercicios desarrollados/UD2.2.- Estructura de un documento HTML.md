En este ejercicio se practica la creación de una página web básica utilizando HTML. Se construye la estructura mínima de un documento HTML, incluyendo la declaración del tipo de documento, las etiquetas `<html>`, `<head>` y `<body>`. 

Además, se define un título para la página y se muestra un encabezado `<h1>` en el cuerpo del documento, lo que permite familiarizarse con la sintaxis y la jerarquía de elementos en HTML.

---

Primero de todo es poner el `doctype` de la página:

```
    <!doctype html>
```

A continuación la pagina irá dentro de la etiqueta `html`, en esta se identifica el idioma de la página:

```
    <html lang="es">
    
    </html>
```

Dentro de la web esta dividido en dos partes que son el `head` y el `body`:

```
    <head>

    </head>
    <body>

    </body>
```

Ahora podemos poner cosas en cada parte, pondremos un titulo en el `head` con la etiqueta `title` y el `body` un texto que sea un encabezado, esto lo haremos con la etiqueta `h1` y ya tendríamos la web:

```
    <head>
        <title>Daniel Oliveira Vidal</title>
    </head>
    <body>
        <h1>Bienbenido a mi sitio web</h1>
    </body>
```

---

A continuación se muestra un ejemplo de código del ejercicio resuelto:

```
<!doctype html>
<html lang="es">
    <head>
        <title>Daniel Oliveira Vidal</title>
    </head>
    <body>
        <h1>Bienbenido a mi sitio web</h1>
    </body>
</html>
```

**Notas:**

- Importante cerrar todas las etiquetas que se habran
- Es recomendado usar el modelo de `sandwich` a la hora de tabular el contenido

---

Este ejemplo demuestra cómo crear la estructura básica de una página web y cómo incluir contenido visible para el usuario mediante etiquetas de encabezado. 

Dominar estos conceptos es esencial para desarrollar sitios web más complejos, donde se podrá añadir texto, imágenes, enlaces y estilos, construyendo así páginas interactivas y completas.