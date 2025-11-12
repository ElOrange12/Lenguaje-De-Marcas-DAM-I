Hoy realizaremos el examen trimestral de lenguajes de marcas, en este haremos un esquema de una página web que usaremos mas adelante junto a los examen anteriores de programación y base de datos para realizar un portafolio dinámico.

Aquí veremos como utilizar las etiquetas básicas y estructuras de `html`

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

Por ultimo ajustaremos con `grid` como se verá la información que mostremos y ajustaremos las fotos para que no se salgan de la página

```
	main{
		display:grid;
		grid-template-columns:auto auto auto;
		gap:20px;
	}
	main img{
		width: 100%; /* No quiero que la imagen se salga */ 
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

Eso sería todo en el `header` vayamos con el `body` en el pondremos una simple estructura que muestre todas las cosas de una pieza, es decir, titulo, categoría, descripción, una imagen y la fecha en la que se añadió, para esto usaremos la etiqueta `article`:

```
	<article>
		<p>Categoría</p>
		<h3>Titulo</h3>
		<p>Descripción</p>
		<p>Fecha</p>
		<img src="https://plus.unsplash.com/premium_photo-1679513691641-9aedddc94f96?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8b2JqZXRvcyUyMGFsZWF0b3Jpb3N8ZW58MHx8MHx8fDA%3D&fm=jpg&q=60&w=3000">
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
			  html,body{background:BurlyWood;font-family:sans-serif;}
			  header,main,footer{
				  background:FloralWhite;
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
			  main img{
				  width: 100%; /* No quiero que la imagen se salga */ 
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
					<p>Fecha</p>
					<img src="https://plus.unsplash.com/premium_photo-1679513691641-9aedddc94f96?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8b2JqZXRvcyUyMGFsZWF0b3Jpb3N8ZW58MHx8MHx8fDA%3D&fm=jpg&q=60&w=3000">
		  		</article>
		  		<article>
					<p>Categoría</p>
					<h3>Titulo</h3>
					<p>Descripción</p>
					<p>Fecha</p>
					<img src="https://plus.unsplash.com/premium_photo-1679513691641-9aedddc94f96?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8b2JqZXRvcyUyMGFsZWF0b3Jpb3N8ZW58MHx8MHx8fDA%3D&fm=jpg&q=60&w=3000">
		  		</article>
				<article>
					<p>Categoría</p>
					<h3>Titulo</h3>
					<p>Descripción</p>
					<p>Fecha</p>
					<img src="https://plus.unsplash.com/premium_photo-1679513691641-9aedddc94f96?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8b2JqZXRvcyUyMGFsZWF0b3Jpb3N8ZW58MHx8MHx8fDA%3D&fm=jpg&q=60&w=3000">
				</article>
			    <article>
					<p>Categoría</p>
					<h3>Titulo</h3>
					<p>Descripción</p>
					<p>Fecha</p>
					<img src="https://plus.unsplash.com/premium_photo-1679513691641-9aedddc94f96?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8b2JqZXRvcyUyMGFsZWF0b3Jpb3N8ZW58MHx8MHx8fDA%3D&fm=jpg&q=60&w=3000">
			    </article>
			    <article>
					<p>Categoría</p>
					<h3>Titulo</h3>
					<p>Descripción</p>
					<p>Fecha</p>
					<img src="https://plus.unsplash.com/premium_photo-1679513691641-9aedddc94f96?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8b2JqZXRvcyUyMGFsZWF0b3Jpb3N8ZW58MHx8MHx8fDA%3D&fm=jpg&q=60&w=3000">
			    </article>
			    <article>
					<p>Categoría</p>
					<h3>Titulo</h3>
					<p>Descripción</p>
					<p>Fecha</p>
					<img src="https://plus.unsplash.com/premium_photo-1679513691641-9aedddc94f96?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8b2JqZXRvcyUyMGFsZWF0b3Jpb3N8ZW58MHx8MHx8fDA%3D&fm=jpg&q=60&w=3000">
			    </article>
			    <article>
					<p>Categoría</p>
					<h3>Titulo</h3>
					<p>Descripción</p>
					<p>Fecha</p>
					<img src="https://plus.unsplash.com/premium_photo-1679513691641-9aedddc94f96?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8b2JqZXRvcyUyMGFsZWF0b3Jpb3N8ZW58MHx8MHx8fDA%3D&fm=jpg&q=60&w=3000">
			    </article>
			    <article>
				<p>Categoría</p>
					<h3>Titulo</h3>
					<p>Descripción</p>
					<p>Fecha</p>
					<img src="https://plus.unsplash.com/premium_photo-1679513691641-9aedddc94f96?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8b2JqZXRvcyUyMGFsZWF0b3Jpb3N8ZW58MHx8MHx8fDA%3D&fm=jpg&q=60&w=3000">
			    </article>
			    <article>
					<p>Categoría</p>
					<h3>Titulo</h3>
					<p>Descripción</p>
					<p>Fecha</p>
					<img src="https://plus.unsplash.com/premium_photo-1679513691641-9aedddc94f96?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8b2JqZXRvcyUyMGFsZWF0b3Jpb3N8ZW58MHx8MHx8fDA%3D&fm=jpg&q=60&w=3000">
			    </article>
			    <article>
					<p>Categoría</p>
					<h3>Titulo</h3>
					<p>Descripción</p>
					<p>Fecha</p>
					<img src="https://plus.unsplash.com/premium_photo-1679513691641-9aedddc94f96?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8b2JqZXRvcyUyMGFsZWF0b3Jpb3N8ZW58MHx8MHx8fDA%3D&fm=jpg&q=60&w=3000">
			    </article>
			    <article>
					<p>Categoría</p>
					<h3>Titulo</h3>
					<p>Descripción</p>
					<p>Fecha</p>
					<img src="https://plus.unsplash.com/premium_photo-1679513691641-9aedddc94f96?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8b2JqZXRvcyUyMGFsZWF0b3Jpb3N8ZW58MHx8MHx8fDA%3D&fm=jpg&q=60&w=3000">
			    </article>
			    <article>
					<p>Categoría</p>
					<h3>Titulo</h3>
					<p>Descripción</p>
					<p>Fecha</p>
					<img src="https://plus.unsplash.com/premium_photo-1679513691641-9aedddc94f96?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8b2JqZXRvcyUyMGFsZWF0b3Jpb3N8ZW58MHx8MHx8fDA%3D&fm=jpg&q=60&w=3000">
				</article>
			</main>
			<footer>
		  		(c) 2025 Daniel Oliveira Vidal
			</footer>
	    </body>
	</html>
```

**Notas:**

- Es importante cerrar cada etiqueta que se habrá sino no se leerá bien la pagina

---

En conclusión hemos visto como estructurar adecuadamente una página web debido al esquema o esqueleto base que hemos hecho, además también de como utilizar un estilo adecuado para que todo quede cuadrado y a nuestro gusto personal a la vez que organizado e intuitivo para el usuario que visite la página.
