En este ejercicio se trabaja el proceso completo de **publicación de una página web estática utilizando GitHub Pages**. El objetivo principal es aprender a crear repositorios en GitHub, subir archivos HTML y CSS, y publicar el contenido en Internet de forma gratuita.

Este tipo de práctica es muy habitual en el entorno profesional, ya que permite mostrar un currículum o portafolio online de forma sencilla y accesible. Además, se refuerzan conceptos básicos de estructura HTML, diseño con CSS y control de versiones mediante Git.

---

En primer lugar, se ha creado un repositorio público en GitHub llamado **curriculum**. Este repositorio actúa como contenedor del proyecto web y permite gestionar los archivos y versiones del código.

Posteriormente, se ha creado un segundo repositorio llamado **portafolio**, destinado a futuros proyectos o ejemplos adicionales. De esta forma, se separa el currículum personal del resto de trabajos.

Una vez creado el repositorio `curriculum`, se ha añadido un archivo principal llamado `index.html`. Este archivo define la estructura básica de la página web utilizando HTML5. En él se incluyen las secciones principales de un sitio web:

- `<header>` para el encabezado y el nombre
- `<main>` para el contenido principal
- `<footer>` para la información final

El archivo HTML enlaza con una hoja de estilos externa mediante la etiqueta:

```
    <link rel="stylesheet" href="estilo.css">
```

Esto permite separar el contenido de la presentación, una buena práctica en el desarrollo web.

A continuación, se ha creado el archivo `estilo.css`, donde se definen los estilos visuales del currículum. En este archivo se utilizan propiedades como `display: grid` para organizar el contenido, márgenes automáticos para centrar los elementos y estilos básicos para imágenes y enlaces.

Una vez creados ambos archivos, se han añadido al repositorio utilizando Git, realizando un commit con el mensaje "Inicialización del proyecto" y posteriormente un `push` para subir los cambios a GitHub.

Con el repositorio ya publicado, se ha configurado GitHub Pages desde la sección de configuración del repositorio, seleccionando la rama `main` como fuente. Tras unos minutos, GitHub genera automáticamente una URL pública donde se puede acceder a la página web.

Finalmente, al acceder a la URL proporcionada por GitHub Pages, se comprueba que la página se muestra correctamente, respetando la estructura HTML y los estilos CSS definidos.

--- 

_index.html_

```
    <!doctype html>
    <html lang="es">
    <head>
        <meta charset="utf-8">
        <title>Curriculum</title>
        <link rel="stylesheet" href="estilo.css">
    </head>
    <body>
        <header>
        <h1>Jose Vicente Carratala</h1>
        </header>
        <main>
        <img src="josevicente.jpg" alt="Foto de Jose Vicente Carratala">
        <p>Bienvenido a mi portfolio. Aquí encontrarás información sobre mis habilidades y proyectos.</p>
        </main>
        <footer>
        <p>&copy; 2023 Jose Vicente Carratala</p>
        </footer>
    </body>
    </html>
```

- Se utiliza una estructura HTML semántica.
- Se enlaza una hoja de estilos externa.
- Se incluye una imagen y texto descriptivo.
- El contenido está organizado de forma clara y legible.

_estilo.css_

```
    header, main, footer {
    width: 1200px;
    margin: auto;
    padding: 20px;
    font-family: sans-serif;
    }

    main {
    display: grid;
    grid-template-columns: repeat(3, 100fr);
    gap: 20px;
    }

    img {
    width: 100%;
    }

    a {
    color: white;
    text-decoration: inherit;
    background: indigo;
    padding: 10px;
    border-radius: 5px;
    }

    header, footer {
    text-align: center;
    }
```

- Se centra el contenido principal de la página.
- Se utiliza CSS Grid para organizar el contenido.
- Las imágenes se adaptan al ancho del contenedor.
- Se definen estilos básicos para enlaces y texto.

---

Este ejercicio permite comprender el flujo completo de creación y publicación de una página web utilizando GitHub Pages. A través del uso de repositorios, commits y configuración de Pages, se consigue publicar un currículum online accesible desde cualquier lugar. Esta práctica resulta especialmente útil para mostrar proyectos personales y mejorar la presencia profesional en Internet.