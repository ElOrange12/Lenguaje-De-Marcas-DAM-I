En este ejercicio se practican varios conceptos clave relacionados con la manipulación del DOM en JavaScript, centrándose especialmente en la creación y eliminación dinámica de elementos HTML. A lo largo de la práctica se combinan técnicas como la creación de nodos, el uso de eventos `click`, el control del tiempo mediante temporizadores y la gestión de bucles controlados.

El resultado final es un pequeño minijuego en el que se generan elementos de forma periódica en posiciones aleatorias, se registran en una tabla y pueden eliminarse tanto visualmente como de su registro asociado. Este tipo de ejercicios ayuda a entender cómo JavaScript controla el comportamiento dinámico de una página web.

---

El documento comienza definiendo algunos estilos CSS básicos. Se utiliza una clase `.cuadrado` para los elementos del juego, dándoles un tamaño fijo, posición absoluta y una transición suave para los cambios visuales:

```
	.cuadrado{
	  width:50px;
	  height:50px;
	  position:absolute;
	  transition:all 0.5s
```

También se definen estilos para una tabla fija que servirá como registro de los elementos creados:

```
	table{
	  border:1px solid grey;
	  background:white;
	  position:fixed;
	  right:10px;
	  top:10px;
	  width:200px
	}
```

En el cuerpo del documento se incluyen dos botones (`Iniciar juego` y `Parar juego`) y un contenedor (`zona_juego`) donde se insertarán los elementos dinámicos.

Dentro del script, lo primero que se hace es declarar una variable global que almacenará el temporizador:

```
	let temporizador;
```

Esto es fundamental para poder controlar el bucle y detenerlo cuando sea necesario.

A continuación, se crea dinámicamente una tabla utilizando JavaScript y se añade al documento. Esta tabla servirá como registro de los elementos creados:

```
	let tabla = document.createElement('table');
	document.querySelector('body').appendChild(tabla);
```

Los botones de control utilizan eventos `onclick`. El botón Iniciar llama a la función `bucle()`, mientras que el botón Parar detiene el temporizador usando `clearTimeout`:

```
	document.querySelector('#iniciar').onclick = function(){
	  bucle();
	}

	document.querySelector('#parar').onclick = function(){
	  clearTimeout(temporizador);
	}
```

La función `bucle()` es el núcleo del ejercicio. Dentro de ella se crea dinámicamente un nuevo elemento `<div>` que representa una pieza del minijuego:

```
	let elemento = document.createElement('div');
	elemento.classList.add('cuadrado');
```

A este elemento se le asigna una posición aleatoria en la pantalla, utilizando valores generados con `Math.random()`:

```
	elemento.style.left = Math.random()*800+'px';
	elemento.style.top = Math.random()*600+'px';
```

También se le asigna un color aleatorio creando valores RGB dinámicos:

```
	let rojo = Math.round(Math.random()*255);
	let verde = Math.round(Math.random()*255);
	let azul = Math.round(Math.random()*255);
	elemento.style.background = 'rgb('+rojo+','+verde+','+azul+')';
```

El elemento se añade al contenedor del juego:

```
	document.querySelector('#zona_juego').appendChild(elemento);
```

Cada vez que se crea un elemento, también se registra en la tabla. Para ello se genera una fila `<tr>` con un mensaje descriptivo:

```
	let fila = document.createElement('tr');
	fila.innerHTML = '<td>Elemento creado</td>';
	tabla.appendChild(fila);
```

Se añade un evento `onclick` al elemento creado. Cuando el usuario hace clic sobre él, se elimina tanto el propio elemento visual como su fila correspondiente en la tabla:

```
	elemento.onclick = function(){
	  this.remove();
	  fila.remove();
	}
```

Finalmente, se implementa un bucle controlado mediante `setTimeout`. La función se llama a sí misma cada segundo, creando así un bucle infinito controlado que puede detenerse:

```
	clearTimeout(temporizador);
	temporizador = setTimeout('bucle()', 1000);
```

Este enfoque permite controlar el ritmo del juego sin bloquear la ejecución del navegador.

---

```
	<!doctype html>
	<html>
		<head>
			<style>
				.cuadrado{width:50px; height:50px; position:absolute; transition:all 0.5s}
				table{border:1px solid grey; background:white; position:fixed; right:10px; top:10px; width:200px}
				table tr td{border-bottom:1px solid grey; padding:5px;}
			</style>
		</head>
		<body>
			<button id='iniciar'>Iniciar juego</button>
			<button id='parar'>Parar juego</button>
			<div id='zona_juego'></div>
			<script>
				let temporizador;
				
				let tabla = document.createElement('table');
				document.querySelector('body').appendChild(tabla);

				document.querySelector('#iniciar').onclick = function(){
					bucle();
				}
				
				document.querySelector('#parar').onclick = function(){
					clearTimeout(temporizador);
				}

				function bucle(){
					let elemento = document.createElement('div');
					elemento.classList.add('cuadrado');
					
					elemento.style.left = Math.random()*800+'px';
					elemento.style.top = Math.random()*600+'px';
					
					let rojo = Math.round(Math.random()*255);
					let verde = Math.round(Math.random()*255);
					let azul = Math.round(Math.random()*255);
					elemento.style.background = 'rgb('+rojo+','+verde+','+azul+')';
					
					document.querySelector('#zona_juego').appendChild(elemento);

					let fila = document.createElement('tr');
					fila.innerHTML = '<td>Elemento creado</td>';
					tabla.appendChild(fila);

					elemento.onclick = function(){
						this.remove();
						fila.remove(); 
					}

					clearTimeout(temporizador);
					temporizador = setTimeout('bucle()', 1000);
				}
			</script>
		</body>
	</html>
```

**Notas:**

- Se crean elementos HTML dinámicamente con `createElement`.
- Se eliminan elementos usando el método `remove()`.
- Se manejan eventos `click` para interactuar con el usuario.
- Se controla la ejecución mediante temporizadores `(setTimeout)`.
- Se manipula una tabla HTML de forma dinámica.
- Se implementa un bucle infinito controlado.

---

Este ejercicio integra múltiples conceptos fundamentales de JavaScript y manipulación del DOM, como la creación y eliminación dinámica de elementos, el uso de eventos y el control del tiempo. El resultado es un minijuego sencillo pero completo que demuestra cómo JavaScript puede gestionar interfaces interactivas y dinámicas, sentando las bases para aplicaciones web más complejas.
