En este ejercicio se practican conceptos básicos de JavaScript relacionados con el manejo de fechas y la definición de funciones. El objetivo principal es familiarizarse con el objeto `Date` para obtener la fecha actual y comprender cómo se pueden definir funciones con parámetros y valores de retorno.

Este tipo de ejercicios resulta fundamental para afianzar las bases del lenguaje JavaScript, ya que el trabajo con fechas y funciones es muy habitual en aplicaciones web, tanto para mostrar información dinámica como para estructurar el código de forma más clara y reutilizable.

---

El archivo comienza con un comentario de cabecera que indica el nombre del ejercicio, la versión y una breve descripción de su funcionalidad. Este comentario sirve como documentación inicial del programa.

A continuación, se define la estructura básica de un documento HTML. Dentro del cuerpo del documento (`<body>`), se incluye un bloque `<script>` donde se escribe el código JavaScript que se ejecutará en el navegador.

Dentro del script, se crea una variable llamada `hoy` que almacena la fecha y hora actuales utilizando el objeto `Date`. Para ello, se utiliza la palabra clave `new`, que permite instanciar un nuevo objeto:

```
	let hoy = new Date();
```

El objeto `Date es una clase integrada en JavaScript que proporciona métodos y propiedades para trabajar con fechas y horas. Al crear una nueva instancia sin parámetros, se obtiene automáticamente la fecha y hora del momento en el que se ejecuta el script.

Una vez creada la variable, se muestra su contenido por consola utilizando `console.log()`. Esto permite visualizar la fecha actual y comprobar que el objeto se ha creado correctamente:

```
	console.log(hoy);
```

El uso de la consola es muy habitual durante el desarrollo, ya que facilita la depuración y el seguimiento del comportamiento del código.

Aunque el enunciado también plantea la definición de una función con parámetros y retorno, en este fragmento de código el ejercicio se centra en la creación y visualización de la fecha actual, sirviendo como primer paso para trabajar posteriormente con funciones en JavaScript.

---

```
	<!--
		El dia de hoy
		v1.0 Daniel Oliveira Vidal
		Este programa te dice el día de hoy
	-->

	<!DOCTYPE html>
	<html>
		<head>
		   
		</head>
		<body>
		    <script>
		        // new quiere decir que instancio un objeto

		        let hoy = new Date();
		        console.log(hoy);
		    </script> 
		</body>
	</html>
```

**Notas:**

- Se utiliza JavaScript dentro de un documento HTML.
- Se crea una variable que almacena la fecha actual mediante el objeto `Date`.
- Se instancia un objeto usando la palabra clave `new`.
- Se muestra la información por consola con `console.log()`.
- El código se ejecuta directamente en el navegador.

---

Este ejercicio permite introducir el uso del objeto `Date` en JavaScript y comprender cómo obtener la fecha actual desde el navegador. Además, refuerza el uso de la consola como herramienta de depuración y análisis del código. Estos conceptos sirven como base para ejercicios más avanzados en los que se combinarán fechas, funciones y manipulación del contenido del documento.
