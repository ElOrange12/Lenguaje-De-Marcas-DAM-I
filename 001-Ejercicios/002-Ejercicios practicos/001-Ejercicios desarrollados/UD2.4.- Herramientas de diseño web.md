En este ejercicio se trabaja la estructura y organización del contenido dentro de una página web utilizando HTML. 

A partir del archivo original, el objetivo es practicar el uso de bloques, secciones y elementos multimedia para mejorar la presentación visual y la distribución de la información. 

Para ello, se parte del ejemplo visto en clase sobre posicionamiento y contenido estructurado, aplicando estos conceptos para añadir nuevas secciones y enriquecer la página.

---

En base a la estructura del ejercicio hemos usado una etiqueta `iframe` para añadir la foto y una `p` para añadir un parrafo, esto lo hemos colocado en el `section` de Estudios:

```
    <iframe src="https://www.eedeporte.com/wp-content/uploads/MINIBLOGS-6.png"></iframe>
    <p>El futbol es uno de mis hobbies favoritos por la emoción, la confianza en un equipo y el entretenimiento que me proporciona.</p>
```

Y en la `section` de portafolio he añadido un `article` con un `h4` y un `p` y he añadido una noticia sobre videojuegos:

```
    <article>
        <h4>Juegos de marcianitos</h4>
        <p>Hoy he hecho un juego de marcianitos en scratch</p>
    </article>    
```

---

A continuación se muestra un ejemplo de código del ejercicio resuelto:

```
<!DOCTYPE html>
<html lang = "es">
    <head>
        <title>Daniel Oliveira Vidal</title>
        <meta charset = "UTF-8">
        <!-- Etiquetas de posicionamiento -->
        <meta name= "description" content= "Web de Daniel, estudiante de DAM">
        <meta name= "viewport" content= "width=device-width, initial-scale=1.0">
        <meta name= "keywords" content= "Programación, curso, diseño, IA, big data, ...">
        <meta name= "author" content= "José Vicente Carratalá Sanchis">
        <link rel= "icon" href="Mosca_Orange.png" type= "image/png">
        <meta property= "og:title" content= "Daniel Oliveira Vidal">
        <meta property= "og:description" content= "Web de Daniel, estudiante de DAM">
        <meta property= "og:image" content= "Mosca_Orange.png">
        <meta property= "og:url" content= "https://ElOrange12.com">
        <meta property= "og:type" content= "website"
    </head> 
    <body>
        <header>
            <!-- Esto es la cabecera de la página -->
            <h1>Daniel Oliveira Vidal</h1>
            <h2>Alumno, Desarrollo de Aplicaciones Multiplataforma</h2>
            <nav>
                <ul>
                    <li><a href="#inicio">Inicio</a></li>
                    <li><a href="#sobremi">Sobre mi</a></li>
                    <li><a href="#estudios">Estudios</a></li>
                    <li><a href="#portafolio">Portafolio</a></li>
                </ul>
            </nav>
        </header>
        <main>
            <!-- Esto es el contenido principal -->
            <section id = 'inicio'>
                <h3>Inicio</h3>
                <div class= "bloque">
                    <img src = "Foto perfil.jfif" alt= "Daniel Oliveira Vidal">
                    <p> La Web de un estudiante de DAM </p>
                </div>
            </section>
            <section id = 'sobremi'>
                <h3>Sobre mi</h3>  
                <div class= "bloque">
                    <p> Un chico de 18 años aficionada y dedicado a la programación, el cual realiza un grado superior en DAM </p>
                </div>              
            </section>
            <section id = 'estudios'>
                <h3>Estudios</h3>
                <iframe src="https://www.google.com/maps/embed?pb=!1m14!1m12!1m3!1d1088.442970449391!2d-0.4100256160043913!3d39.50136085114006!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e0!3m2!1ses!2ses!4v1759912144688!5m2!1ses!2ses" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
                <form>
                    <label for = "nombre">Introduce tu nombre</label>
                    <input type = "text" id = "nombre">
                    <label for = "email">Introduce tu email</label>
                    <input type = "text" id = "nombre">
                    <textarea></textarea>
                    <input type = "submit">
                </form>
                <div class= "bloque">
                    <p> ¡¡Donde estudio!! </p>
                </div>
                <iframe src="https://www.eedeporte.com/wp-content/uploads/MINIBLOGS-6.png"></iframe>
                <p>El futbol es uno de mis hobbies favoritos por la emoción, la confianza en un equipo y el entretenimiento que me proporciona.</p>
            </section>
            <section id = 'portafolio'>
                <h3>Portafolio</h3>
                <div id= "portafolio">
                    <article>
                        <h4>Elemento de portáfolio</h4>
                        <p>Hoy estoy retocando mi pagina web.</p>
                    </article>
                    <article>
                        <h4>Juegos de marcianitos</h4>
                        <p>Hoy he hecho un juego de marcianitos en scratch</p>
                    </article>
                </div>
            </section>
        </main>
        <footer>
            <!-- Esto es el pié de página -->
            <a href = 'https://instagram.com/elorange12'>Instagram</a>
            <a href = 'https://github.com/ElOrange12'>GitHub</a>
        </footer>
    </body>
</html>
```

**Notas:**

- Cerrar todas las etiquetas al acabar
- Es recomentdable descargar las fotos antes que poner una url

---

Con la modificación del archivo original, el alumno refuerza su comprensión sobre cómo integrar imágenes, texto y artículos dentro de una estructura HTML bien organizada. 

La incorporación de un bloque adicional en la sección de estudios y un nuevo artículo en el portafolio permite practicar la creación de contenido relevante y visualmente coherente.

Este ejercicio consolida habilidades esenciales para construir páginas más completas, dinámicas y centradas en los intereses personales del autor.