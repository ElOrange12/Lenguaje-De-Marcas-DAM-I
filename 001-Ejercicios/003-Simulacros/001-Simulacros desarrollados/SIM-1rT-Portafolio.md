En este simulacro de examen se ha desarrollado un front básico para un portafolio personal utilizando únicamente HTML y CSS.

El objetivo principal es construir una estructura clara y legal que represente de forma visual varios proyectos, siguiendo las indicaciones de crear un header con información personal, un main con diferentes piezas del portafolio y un footer con el copyright correspondiente.

---

En primer lugar comenzamos poniendo la etiqueta `doctype` como cualquier `html`:

```
	<!doctype html>
```

Esto irá seguido de la etiqueta `html` esta en la página en si, al abrir esta estique especificaremos el idioma de la página, en nuestro caso será el español:

```
	<html lang="es">
	
	</html>
```

Ya puesta como en todas las páginas la etiqueta `html` abriremos dos secciones un `head` y un `body`:

```
	<head>
	
	</head>
	<body>
	
	</body>
```

En el `head` es donde marcaremos el título de la pagina, la etiqueta `meta charset` y el estilo de la pagina.

Primero añadamos el titulo y el `meta charset`:

```
	<title>Portafolio</title>
    <meta charset="utf-8">
```

Lo que pongamos en la etiqueta `title` es lo que saldrá arriba en la pestaña al entrar en la página web y la etiqueta `meta charset` en este caso es la que marca la codificación que tiene la pagina.

Ahora vayamos con el estilo, primero de todo es abrir la etiqueta `style`:

```
	<style>
		
	</style>
```

Teniendo ya la etiqueta puesta vayamos por partes, primero de todo marcaremos el fondo de la página y la tipografía de nuestra página:

```
	html,body{background:BurlyWood;font-family:sans-serif;}
```

Ahora ajustaremos el estilo del `header`, `main` y `footer`, en este ajustaremos el color de fondo, el espaciado, los margenes y demas:

```
	header,main,footer{
		background:FloralWhite;
		padding:20px;
		width:800px;
		margin:auto;
		text-align:center;
	}
```

Por ultimo ajustaremos con `grid` como se verá la información que mostremos:

```
	main{
		display:grid;
		grid-template-columns:auto auto auto;
		gap:20px;
	}
```

Ya tenemos todo lo que vamos a poner en el `head` vayamos con el `body`, en este lo primero de todo pondremos tres partes abriendo tres etiquetas, estas son `header`, `main` y `footer`:

```
	<header>

	</header>
	<main>
	
	</main>
	<footer>
	
	</footer>
```

Ahora que ya las tenemos empezaremos por el `header` , en el simplemente pondremos el título y un lugar donde consultar información adicional:

```
	<h1>Daniel Oliveira Vidal</h1>
	<h2>info@elorange.com</h2>
```

Eso sería todo en el `header` vayamos con el `body` en el pondremos una simple estructura que muestre todas las cosas de una pieza del portafolio:

```
	<article>
        <p>Categoría</p>
        <h3>Titulo</h3>
        <p>Descripción</p>
        <img src="img.png">
      </article>
```

Teniendo esta estructura clara la copiamos y pegamos unas cuantas veces para tener un esquema que de como se verán las piezas.

Por ultimo de todo el `footer` en el solamente añadiremos texto dándonos crédito de nuestra página:

```	
	(c) 2025 Daniel Oliveira Vidal
```

---

A continuación se muestra un ejemplo de código del ejercicio resuelto:

```
<!doctype html>
<html lang="es">
  <head>
    <title>Portafolio</title>
    <meta charset="utf-8">
    <style>
      html,body{background:grey;font-family:sans-serif;}
      header,main,footer{
        background:white;
        padding:20px;
        width:800px;
        margin:auto;
        text-align:center;
      }
      main{
        display:grid;
        grid-template-columns:auto auto auto;
        gap:20px;
      }
    </style>
  </head>
  <body>
    <header>
      <h1>Daniel Oliveira Vidal</h1>
      <h2>info@elorange.com</h2>
    </header>
    <main>
      <article>
        <p>Categoría</p>
        <h3>Titulo</h3>
        <p>Descripción</p>
        <img src="img.png">
      </article>
      <article>
        <p>Categoría</p>
        <h3>Titulo</h3>
        <p>Descripción</p>
        <img src="img.png">
      </article>
      <article>
        <p>Categoría</p>
        <h3>Titulo</h3>
        <p>Descripción</p>
        <img src="img.png">
      </article>
      <article>
        <p>Categoría</p>
        <h3>Titulo</h3>
        <p>Descripción</p>
        <img src="img.png">
      </article>
      <article>
        <p>Categoría</p>
        <h3>Titulo</h3>
        <p>Descripción</p>
        <img src="img.png">
      </article>
      <article>
        <p>Categoría</p>
        <h3>Titulo</h3>
        <p>Descripción</p>
        <img src="img.png">
      </article>
      <article>
        <p>Categoría</p>
        <h3>Titulo</h3>
        <p>Descripción</p>
        <img src="img.png">
      </article>
      <article>
        <p>Categoría</p>
        <h3>Titulo</h3>
        <p>Descripción</p>
        <img src="img.png">
      </article>
      <article>
        <p>Categoría</p>
        <h3>Titulo</h3>
        <p>Descripción</p>
        <img src="img.png">
      </article>
      <article>
        <p>Categoría</p>
        <h3>Titulo</h3>
        <p>Descripción</p>
        <img src="img.png">
      </article>
      <article>
        <p>Categoría</p>
        <h3>Titulo</h3>
        <p>Descripción</p>
        <img src="img.png">
      </article>
      <article>
        <p>Categoría</p>
        <h3>Titulo</h3>
        <p>Descripción</p>
        <img src="img.png">
      </article>
    </main>
    <footer>
      (c) 2025 Daniel Oliveira Vidal
    </footer>
  </body>
</html>
```

**Notas:**

- Importante cerrar todas las etiquetas que se habrán

---

El código presentado cumple con los requisitos esenciales del ejercicio: estructura HTML correcta, uso coherente de estilos CSS y organización del contenido mediante artículos que muestran distintos elementos del portafolio.

Este diseño sirve como base sólida para futuras ampliaciones y para integrar, más adelante, un panel de administración o funcionalidades dinámicas.