Este proyecto consiste en la creación de una página web en HTML y CSS para representar un currículum personal. El diseño utiliza una estructura dividida en dos secciones: una columna izquierda con información personal y otra derecha con formación e idiomas. El objetivo es practicar la maquetación web, la organización semántica y el uso adecuado de estilos.

---

Empezaremos como cualquier html, poniendo el `doctype` y el `lang`:

```
    <!doctype html>
    <html lang="es">
```

A continuación empezaremos la sección `head` en la cual incluiremos el `title`, el `meta charset` y el `style`, aunque el style lo completaremos mas adelantes.

```
    <title>Curriculum</title>
            <meta charset="utf-8">
            <style>

            </style>
```

Vale como queremos hacer un curriculum haremos dos columnas, para ello empezando el `body` haremos dos `div` uno que tenga el `id` derecha y el otro izquierda:

```
    <div id="izquierda">

    </div>
    <div id="derecha">

    </div>
```

Empezemos por la izquierda, dentro habrá una foto nuestra y dos secciones una que sea un sobre nosotros y otra que sea nuestros contactos, este obviamente completaremos con nuestra información:

```
    <img src = "image.png" alt= "Daniel Oliveira Vidal">
    <div id="sobremi">
        <h3>Sobre mí</h3>
        <p>Estudiante de desarrollo de aplicaciones multiplataforma (DAM), me considero una persona aplicada, trabajadora y ordenada, busco mi primera experiencia laboral en el sector.</p>
    </div>
    <div id="contacto">
        <h3>Contacto</h3>
        <ul>
            <li>607048085</li>
            <li>danieloliveiravidal12@gmail.com</li>
            <li>València</li>
        </ul>
    </div>
```

Aquí hemos usado un `h3` para los titulos, un `p` para poner un parrafo en `sobremi` y una lista para los contactos.

Continuemos con la derecha, en esta aparecerá nuestro nombre, nuestros estudios y nuestro nivel en idiomas:

```
    <div id="encabezado">
        <h1>Daniel Oliveira Vidal</h1>
        <p>Estudiante</p>
    </div>
    <div id="educacion">
        <h3>EDUCACIÓN</h3>
        <h4>CEAC FP - Valencia</h4>
        
        <p>2025-2027</p>
        <p>Grado superior en Desarrollo de Aplicaciones Multiplataforma - En curso</p>
        <h4>Colegio Ntra. Sra. de Fátima</h4>
        <p>2023 - 2025</p>
        <p>Bachillerato Tecnologico</p>
    </div>
    <div id="idiomas">
    <h3>IDIOMAS</h3>
    <p>Inglés - Nivel medio (No certificado)</p>
    <p>Valenciano - Nivel B2</p>
    <p>Español - Nativo</p>
    </div>
```

Hagamos que todo sea bonito, empezemos con el `style`.

Primero de todo pongamos el fondo de la pagina web:

```
    html{background:antiquewhite; font-family:sans-serif}
    body{background:white; margin:auto; min-height: 600px; display:flex; width:700px}
```

A continuación empezemos con la columna izquierda, usaremos `flex` para definir las dos columnas.

Dentro de la columna izquierda ajustaremos los parrafos, titulos y listas para que aparezcan a nuestro gusto:

```
    #izquierda{
        flex:1;
        background:gainsboro;
        padding:20px 20px 20px 40px;
        display:flex;
        flex-direction:column;
        align-items: flex-start
    }
    #izquierda img{width:70%; margin-bottom:20px}
    #izquierda p {
        font-size: 13px;
        line-height: 1.6;
        margin-top: 0;
        margin-bottom: 100px;
        text-align: left;
    }
    #izquierda h3 {
        text-transform: uppercase;
        font-weight: bold;
        letter-spacing: 2px;
        font-size: 14px;
        margin-bottom: 10px;
        color: black;
    }
    #contacto ul {
        list-style: none;
        padding: 0;
        margin: 0;
    }
    #contacto li {
        display: flex;
        align-items: center;
        gap: 8px;
        font-size: 11px;
        margin-bottom: 10px;
    }
    #contacto li::before {
        font-family: "Segoe UI Symbol";
        color: #333;
        font-size: 14px;
    }

    /* Iconos según orden de las líneas */
    #contacto li:nth-child(1)::before { content: "📞"; }
    #contacto li:nth-child(2)::before { content: "✉️"; }
    #contacto li:nth-child(3)::before { content: "📍"; }
```

Esto pone iconos en los contactos, ajusta margenes, tamaño de la foto y demás.

Sigamos con la derecha que será mas de lo mismo, el flex en este caso será mas grande debido que es la importante y será mas grande

En el `style` de la derecha ajustaremos los titulos y parrafos para que queden tambien como queramos:

```
    #derecha{
        flex:4;
        background:white;
        padding:20px 20px 20px 40px;;
        margin:auto
    }
    #derecha h3 {
        text-transform: uppercase;
        font-weight: bold;
        letter-spacing: 2px;
        font-size: 14px;
        margin-bottom: 10px;
        color: black;
    }
    #derecha h4 {
        text-transform: uppercase;
        font-weight: bold;
        letter-spacing: 2px;
        font-size: 10px;
        margin-bottom: 10px;
        color: black;
    }
    #derecha p {
        font-size: 12px;
        line-height: 1.6;
        text-align: left;
    }
    #encabezado p{
        font-size: 12px;
        line-height: 1.6;
        margin-bottom: 40px;
        text-align: left;
    }
```

Y así es como tendriamos nuestro curriculum en una pagina web

---

A continuación se muestra un ejemplo de código del ejercicio resuelto:

```
    <!doctype html>
    <html lang="es">
        <head>
            <title>Curriculum</title>
            <meta charset="utf-8">
            <style>
                html{background:antiquewhite; font-family:sans-serif}
                body{background:white; margin:auto; min-height: 600px; display:flex; width:700px}
                #izquierda{
                    flex:1;
                    background:gainsboro;
                    padding:20px 20px 20px 40px;
                    display:flex;
                    flex-direction:column;
                    align-items: flex-start
                }
                #izquierda img{width:70%; margin-bottom:20px}
                #izquierda p {
                    font-size: 13px;
                    line-height: 1.6;
                    margin-top: 0;
                    margin-bottom: 100px;
                    text-align: left;
                }
                #izquierda h3 {
                    text-transform: uppercase;
                    font-weight: bold;
                    letter-spacing: 2px;
                    font-size: 14px;
                    margin-bottom: 10px;
                    color: black;
                }
                #contacto ul {
                    list-style: none;
                    padding: 0;
                    margin: 0;
                }
                #contacto li {
                    display: flex;
                    align-items: center;
                    gap: 8px;
                    font-size: 11px;
                    margin-bottom: 10px;
                }
                #contacto li::before {
                    font-family: "Segoe UI Symbol";
                    color: #333;
                    font-size: 14px;
                }

                /* Iconos según orden de las líneas */
                #contacto li:nth-child(1)::before { content: "📞"; }
                #contacto li:nth-child(2)::before { content: "✉️"; }
                #contacto li:nth-child(3)::before { content: "📍"; }
                #derecha{
                    flex:4;
                    background:white;
                    padding:20px 20px 20px 40px;;
                    margin:auto
                }
                #derecha h3 {
                    text-transform: uppercase;
                    font-weight: bold;
                    letter-spacing: 2px;
                    font-size: 14px;
                    margin-bottom: 10px;
                    color: black;
                }
                #derecha h4 {
                    text-transform: uppercase;
                    font-weight: bold;
                    letter-spacing: 2px;
                    font-size: 10px;
                    margin-bottom: 10px;
                    color: black;
                }
                #derecha p {
                    font-size: 12px;
                    line-height: 1.6;
                    text-align: left;
                }
                #encabezado p{
                    font-size: 12px;
                    line-height: 1.6;
                    margin-bottom: 40px;
                    text-align: left;
                }
            </style>
        </head>
        <body>
            <div id="izquierda">
                <img src = "image.png" alt= "Daniel Oliveira Vidal">
                <div id="sobremi">
                    <h3>Sobre mí</h3>
                    <p>Estudiante de desarrollo de aplicaciones multiplataforma (DAM), me considero una persona aplicada, trabajadora y ordenada, busco mi primera experiencia laboral en el sector.</p>
                </div>
                <div id="contacto">
                    <h3>Contacto</h3>
                    <ul>
                        <li>607048085</li>
                        <li>danieloliveiravidal12@gmail.com</li>
                        <li>València</li>
                    </ul>
                </div>
            </div>
            <div id="derecha">
                <div id="encabezado">
                    <h1>Daniel Oliveira Vidal</h1>
                    <p>Estudiante</p>
                </div>
                <div id="educacion">
                    <h3>EDUCACIÓN</h3>
                    <h4>CEAC FP - Valencia</h4>
                    
                    <p>2025-2027</p>
                    <p>Grado superior en Desarrollo de Aplicaciones Multiplataforma - En curso</p>
                    <h4>Colegio Ntra. Sra. de Fátima</h4>
                    <p>2023 - 2025</p>
                    <p>Bachillerato Tecnologico</p>
                </div>
                <div id="idiomas">
                <h3>IDIOMAS</h3>
                <p>Inglés - Nivel medio (No certificado)</p>
                <p>Valenciano - Nivel B2</p>
                <p>Español - Nativo</p>
                </div>
            </div>
        </body>
    </html>
```

**Notas:**
-
-
-

---

En conclusión el currículum en HTML y CSS permite mostrar información personal y académica de manera clara y profesional. Gracias al uso de propiedades flexbox, tipografía y márgenes, se logra una estructura visual equilibrada. Este ejercicio refuerza la comprensión del diseño web, la jerarquía del contenido y la correcta aplicación de estilos mediante hojas de estilo en cascada.