En este ejercicio se trabaja el concepto de evento `click` y la manipulación dinámica de elementos HTML utilizando JavaScript. A lo largo de la práctica se construye una interfaz web compuesta por un menú lateral y una zona principal de contenido, donde los elementos se generan automáticamente a partir de datos obtenidos en formato JSON.

El objetivo principal es comprender cómo JavaScript puede consumir datos desde un servidor, crear elementos HTML de forma dinámica y mostrar información estructurada como tablas. Este tipo de ejercicio es muy representativo de aplicaciones web reales, donde la interfaz se adapta en función de los datos disponibles.

---

El documento comienza definiendo la estructura HTML básica junto con estilos CSS que establecen un diseño dividido en dos zonas principales: un menú lateral (`nav`) y una zona de contenido (`main`):

```
	html, body{height:100%; padding:0px; margin:0px; display:flex; width:100%}
	nav{background:darkorange; flex:1; color:white; padding:20px}
	main{flex:4; background:AntiqueWhite; padding:20px}
```

Este diseño permite crear una interfaz tipo panel, muy utilizada en aplicaciones administrativas.

A continuación, se añaden estilos específicos para los botones del menú lateral, configurándolos en forma de columna y aplicando un diseño visual coherente con el resto de la página:

```
	nav{display:flex; flex-direction:column; gap:20px;}
	nav button{border:none; background:AntiqueWhite; color:darkorange; padding:20px; text-transform:uppercase;}
```

El primer bloque de JavaScript se encarga de consumir un JSON desde un servidor Flask. Mediante la función `fetch()`, se realiza una petición HTTP a una ruta que devuelve una lista de nombres de tablas:

```
	fetch('http://127.0.0.1:5000/tablas')
```

La respuesta se convierte a formato JSON y se procesa para crear dinámicamente los botones del menú. Para cada elemento recibido, se crea un botón nuevo y se inserta dentro del elemento `<nav>`:

```
	datos.forEach(function(texto_boton){
		let boton = document.createElement("button")
		boton.textContent = texto_boton;
		contenedor.appendChild(boton);
	})
```

De esta forma, el menú lateral se construye automáticamente en función de los datos recibidos del servidor, sin necesidad de escribir los botones manualmente en el HTML.

En el segundo bloque de JavaScript, se vuelve a utilizar `fetch()` para obtener datos en formato JSON, en este caso correspondientes a una tabla de clientes:

```
	fetch('http://127.0.0.1:5000/clientes')
```

Una vez recibidos los datos, se crea dinámicamente una tabla HTML. Primero se genera el elemento `<table>` y se añade al contenedor principal `(main)`:

```
	let tabla = document.createElement('table');
	contenedor.appendChild(tabla);
```

Posteriormente, se recorre cada línea del JSON. Cada línea representa una fila de la tabla y se transforma en un elemento `<tr>`. A su vez, cada valor de la fila se inserta en una celda `<td>`:

```
	datos.forEach(function(linea){
		let fila = document.createElement('tr');
		linea.forEach(function(celda){
		    let data = document.createElement('td');
		    data.textContent = celda
		    fila.appendChild(data);
		})
		tabla.appendChild(fila)
	})
```

Gracias a este proceso, la tabla se genera completamente de forma dinámica a partir de los datos recibidos, mostrando la información estructurada sin necesidad de escribir HTML estático.

---

```
	<!--
		Datos de un json
		v1.0 Daniel Oliveira Vidal
		Este programa crea botenes en base la información de un json
	-->
	<!Doctype html>
	<html>
		<head>
			<style>
				html, body{height:100%; padding:0px; margin:0px; display:flex; width:100%}
				nav{background:darkorange; flex:1; color:white; padding:20px}
				main{flex:4; background:AntiqueWhite; padding:20px}
			</style>
		</head>
		<body>
			<nav>Orange | Panel</nav>
			<style>
				nav{display:flex; flex-direction:column; gap:20px;}
				nav button{border:none; background:AntiqueWhite; color:darkorange; padding:20px; text-transform:uppercase;}
			</style>
			<script>
				// Ves y busca
				fetch('http://127.0.0.1:5000/tablas')
				.then(function(respuesta){
					return respuesta.json();	// La resp viene en JSON
				})
				.then(function(datos){
					// Y luego creamos botones a partir de lo que hay en el json
					let contenedor = document.querySelector('nav')
					datos.forEach(function(texto_boton){
						let boton = document.createElement("button")
						boton.textContent = texto_boton;
						contenedor.appendChild(boton);
					})
				})
			</script>
			<main>Orange | Tablas</main>
			<style>
				table{border:3px solid darkorange;border-collapse:collapse;background:Antiquewhite;}
				table tr:first-child{background:darkorange;color:Antiquewhite;}
				table tr td{padding:10px;border-right:1px solid darkorange;}
			</style>
			<script>
				// En primer lugar cargamos datos de un json
				fetch('http://127.0.0.1:5000/clientes')
				.then(function(respuesta){
					return respuesta.json();	// La resp viene en JSON
				})
				.then(function(datos){
					let contenedor = document.querySelector('main');
					let tabla = document.createElement('table');
					contenedor.appendChild(tabla);
					datos.forEach(function(linea){
						let fila = document.createElement('tr');
						linea.forEach(function(celda){
							let data = document.createElement('td');
							data.textContent = celda
							fila.appendChild(data);
						})
						tabla.appendChild(fila)
					})
				})
			</script>
		</body>
	</html>
```

**Notas:**

- Se consume información desde un servidor mediante fetch().
- Se crean botones de forma dinámica a partir de datos JSON.
- Se generan tablas HTML automáticamente desde estructuras de datos.
- Se manipula el DOM utilizando createElement() y appendChild().
- Se construye una interfaz web completa basada en datos externos.

---

Este ejercicio permite comprender cómo JavaScript puede crear interfaces dinámicas a partir de datos obtenidos desde un servidor. A través del uso de eventos, consumo de JSON y creación de elementos HTML, se simula el funcionamiento de una aplicación web real. Estos conceptos son fundamentales para el desarrollo de paneles interactivos y aplicaciones modernas basadas en datos.
