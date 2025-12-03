En estos ejemplos se aplican estilos internos en HTML para modificar aspectos visuales como colores de fondo, tipografías y tamaños de texto.

Estos fragmentos permiten practicar cómo el CSS interno afecta directamente a los elementos de una página, ayudando a comprender mejor la personalización visual sin necesidad de archivos externos.

---

Primero empezemos con `002-estilo-interno.html` y añadamos dentro del `style` lo que nos sugirio el ejercicio:

```
    h1 {
        color: green;
    }

    body {
        background-color: lightblue;
    }
```

Ahora añadamos lo que nos pide aparte el ejercicio que es el cambio de fuente y de tamaño:

```
    p {
        font-family: "Arial", sans-serif;
        font-size: 18px;
    }
```

Ahora hagamoslo pero en el otro documento:

```
    body {
        background: lightgreen;
    }

    h1, h2, h3 {
        background-color: yellow;
    }

    p {
        font-family: "Times New Roman", serif;
        font-size: 22px;
    }
```

---

A continuación se muestran los ejemplos de código del añadido a ejercicios anteriores:

_002-estilo-interno.html_
```
    <style>
        h1 {
            color: green;
        }

        body {
            background-color: lightblue;
        }

        p {
            font-family: "Arial", sans-serif;
            font-size: 18px;
        }
    </style>
```

_008-color-de-fondo.html_
```
<style>
    body {
        background: lightgreen;
    }

    h1, h2, h3 {
        background-color: yellow;
    }

    p {
        font-family: "Times New Roman", serif;
        font-size: 22px;
    }
</style>
```

**Notas:**

- Importante el cerrar las llaves que abrimos a la hora del style

---

La práctica con estilos internos y colores de fondo demuestra lo útil que es el CSS para transformar por completo la apariencia de una web.

Experimentar con estas propiedades permite mejorar cualquier proyecto real, ajustando colores, fuentes y estructuras para obtener un diseño más atractivo y coherente con la identidad que se quiera transmitir.