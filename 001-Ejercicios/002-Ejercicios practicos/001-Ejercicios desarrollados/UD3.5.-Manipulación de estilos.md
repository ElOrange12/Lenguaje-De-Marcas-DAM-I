En este ejercicio se trabaja el concepto de **estilo condicional** en documentos web utilizando JavaScript y CSS. El objetivo principal es aprender a modificar dinámicamente la apariencia de un elemento HTML en función de la interacción del usuario.

Para ello, se utiliza una caja de texto donde el usuario introduce información y, dependiendo de la longitud del texto introducido, se cambia el estilo visual de un párrafo. Este tipo de comportamiento es muy habitual en formularios reales, por ejemplo para validar DNI, números de teléfono o contraseñas.

---

El documento comienza definiendo los estilos CSS que se aplicarán de forma condicional. Se crean dos clases, `.rojo` y `.verde`, que cambian el color de fondo del párrafo:

```
	.rojo {
		background: rgb(255, 200, 200);
	}

	.verde {
		background: rgb(200, 255, 200);
	}
```

Estas clases no se aplican directamente con JavaScript al cargar la página, sino que se alternan dinámicamente según la lógica del programa.

En el cuerpo del documento HTML se incluyen dos elementos clave:

```
	<input type="text" id="entrada">
	<p class="rojo">Este es un párrafo o parágrafo</p>
```

El `<input>` sirve para que el usuario introduzca texto.

El `<p>` comienza con la clase `rojo`, indicando que inicialmente no se cumple la condición deseada.

A continuación, se utiliza JavaScript para escuchar un evento `keyup`. Este evento se dispara cada vez que el usuario suelta una tecla, lo que permite reaccionar en tiempo real a los cambios del texto:

```
	document.getElementById('entrada').addEventListener('keyup', function() {
```

Dentro del evento, se obtiene el valor actual del input utilizando `this.value`, y posteriormente se calcula su longitud:

```
	let valor = this.value;
	let longitud = valor.length;
```

Este paso es clave, ya que toda la lógica del ejercicio se basa en comprobar cuántos caracteres ha introducido el usuario.

Se utiliza una estructura condicional `if` para evaluar si la longitud es exactamente igual a 9:

```
	if (longitud == 9) {
```

Cuando la condición se cumple, se modifica la clase del párrafo. Se añade la clase `verde` y se elimina la clase `rojo`:

```
	document.querySelector("p").classList.add("verde");
	document.querySelector("p").classList.remove("rojo");
```

Esto provoca que el fondo del párrafo cambie a verde, indicando visualmente que la condición es correcta.

Si la longitud no es 9, se ejecuta el bloque `else`, que realiza la operación contraria:

```
	document.querySelector("p").classList.remove("verde");
	document.querySelector("p").classList.add("rojo");
```

De esta forma, el párrafo vuelve a mostrarse en rojo cada vez que la condición deja de cumplirse. Este comportamiento garantiza que el estilo sea coherente en todo momento con el estado del input.

---

```
	<!doctype html>
	<html>
		<head>
			<style>
				.rojo {
					background: rgb(255, 200, 200);
				}

				.verde {
					background: rgb(200, 255, 200);
				}
			</style>
		</head>
		<body>
			<input type="text" id="entrada">
			<p class="rojo">Este es un párrafo o parágrafo</p>
			<script>
				document.getElementById('entrada').addEventListener('keyup', function() {
					let valor = this.value;
					let longitud = valor.length;

					if (longitud == 9) {
					    document.querySelector("p").classList.add("verde");
					    document.querySelector("p").classList.remove("rojo");
					} else {
					    document.querySelector("p").classList.remove("verde");
					    document.querySelector("p").classList.add("rojo");
					}
				});
			</script>
		</body>
	</html>
```

- Se utiliza el evento `keyup` para detectar cambios en tiempo real.
- Se accede al valor del input mediante `this.value`.
- Se evalúa la longitud del texto con `.length`.
- Se manipulan clases CSS usando `classList.add()` y `classList.remove()`.
- El estilo visual cambia dinámicamente según la condición.

---

Este ejercicio muestra cómo combinar JavaScript y CSS para crear comportamientos interactivos basados en condiciones. El uso de eventos junto con la manipulación de clases permite ofrecer una respuesta visual inmediata al usuario, mejorando la experiencia de uso y facilitando la validación de datos en formularios. Es una base fundamental para el desarrollo de interfaces web dinámicas y reactivas.

