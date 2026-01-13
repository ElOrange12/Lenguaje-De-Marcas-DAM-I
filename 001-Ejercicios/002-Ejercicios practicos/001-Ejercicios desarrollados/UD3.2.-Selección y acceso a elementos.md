En este ejercicio se trabajan los conceptos básicos de manipulación de documentos web utilizando JavaScript. El objetivo es aprender a seleccionar elementos HTML, modificar su contenido y generar elementos de forma dinámica dentro de una página web.

A través de ejemplos sencillos, se practica cómo JavaScript puede interactuar con la estructura del documento (DOM), permitiendo leer información existente y escribir nuevo contenido en función de los datos disponibles. Estos conceptos son fundamentales para el desarrollo de páginas web dinámicas e interactivas.

---

El ejercicio se compone de varios ejemplos que muestran diferentes formas de manipular el contenido HTML desde JavaScript.

En primer lugar, se introduce el uso de `document.querySelector()`, un método que permite seleccionar elementos del documento HTML utilizando selectores CSS. Este método devuelve el primer elemento que coincide con el selector indicado, lo que facilita el acceso directo a nodos concretos del DOM.

En el archivo **003-escribir html.html**, se selecciona un elemento `<div>` vacío y se modifica su contenido utilizando la propiedad `innerHTML`:

```
	document.querySelector("div").innerHTML = "<h1>Hola</h1>";
```

Con esta instrucción, JavaScript inserta dinámicamente una etiqueta `<h1>` dentro del `<div>`. La propiedad `innerHTML` permite escribir código HTML directamente como texto, que el navegador interpreta y renderiza en la página.

Este tipo de técnica es muy útil para generar contenido de forma dinámica sin necesidad de que esté escrito previamente en el HTML.

En el siguiente ejemplo, correspondiente al archivo *004-microblog.html*, se trabaja con una estructura un poco más compleja. En este caso, se define una lista de artículos mediante un array de JavaScript:

```
	const articulos = [
	  "Primer artículo","Segundo artículo","Tercer artículo"
	];
```

A continuación, se selecciona el contenedor `<main>` del documento, que será el lugar donde se insertarán los artículos:

```
	const contenedor = document.querySelector("main");
```

Posteriormente, se utiliza un bucle `for` para recorrer el array de artículos. En cada iteración, se añade un nuevo encabezado `<h3>` al contenido del `<main>` utilizando `innerHTML` y concatenando el contenido anterior:

```
	for(let i = 0; i < articulos.length; i++){
	  contenedor.innerHTML += "<h3>" + articulos[i] + "</h3>";
	}
```

De esta forma, cada elemento del array se transforma en un título visible en la página, simulando el funcionamiento básico de un blog donde los artículos se generan dinámicamente a partir de una lista de datos.

---

_003-escribir html.html_

```
	<!doctype>
	<html lang="es">
	  <head>
		<title>Javascript</title>
		<meta charset="utf-8">
	  </head>
	  <body>
		<div></div>
		<script>
		  document.querySelector("div").innerHTML = "<h1>Hola</h1>";
		</script>
	  </body>
	</html>
```

_004-microblog.html_

```
	<!doctype>
	<html lang="es">
	  <head>
		<title>Javascript</title>
		<meta charset="utf-8">
	  </head>
	  <body>
		<header><h1>El blog de Jose Vicente</h1></header>
		<main></main>
		<footer>(c) 2025 Jose Vicente Carratala</footer>
		<script>
		  const articulos = [
		    "Primer artículo","Segundo artículo","Tercer artículo"
		  ];
		  const contenedor = document.querySelector("main");
		  for(let i = 0; i < articulos.length; i++){
		    contenedor.innerHTML += "<h3>" + articulos[i] + "</h3>";
		  }
		</script>
	  </body>
	</html>
```

**Notas:**

- Se seleccionan elementos HTML mediante `document.querySelector()`.
- Se modifica el contenido del DOM utilizando `innerHTML`.
- Se generan elementos HTML de forma dinámica con JavaScript.
- Se recorren listas de datos mediante bucles.
- Se simula un microblog cargando artículos desde un array.

---

Este ejercicio permite comprender cómo JavaScript puede interactuar directamente con la estructura HTML de una página web. A través de la selección y modificación de elementos del DOM, se aprende a generar contenido dinámico y a transformar datos en elementos visuales. Estos conceptos son la base para el desarrollo de aplicaciones web interactivas y para el manejo dinámico de información en el navegador.
