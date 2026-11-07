# Taller de investigación: Flet

**Asignatura:** Programación Orientada a Objetos  
**Tema:** Interfaces gráficas y programación orientada a eventos  
**Aplicación:** Contador interactivo

## 1. ¿Qué es Flet y cuál es su propósito?

Flet es un framework de Python para crear interfaces y aplicaciones interactivas. Permite construir la parte visual y la lógica principalmente con Python, utilizando controles listos para usar.

## 2. ¿Qué tipo de aplicaciones permite desarrollar?

Flet permite desarrollar aplicaciones web, de escritorio y móviles. Un proyecto puede adaptarse a distintos sistemas operativos y ejecutarse en un navegador, según la configuración de publicación.

## 3. ¿Cómo se instala y qué requisitos necesita?

Se necesita Python compatible con la versión de Flet instalada y una terminal. Se recomienda utilizar un entorno virtual.

En Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
flet run main.py
```

También se puede ejecutar con `python main.py`.

## 4. ¿Cuáles son sus principales componentes gráficos?

- `Page`: página o ventana principal.
- `Text`: muestra texto.
- `Button` y `IconButton`: controles que responden a clics.
- `TextField`: entrada de texto.
- `Container`: agrupa y organiza contenido.
- `Row`: organiza controles horizontalmente.
- `Column`: organiza controles verticalmente.
- `Image`: muestra imágenes.

## 5. ¿Cómo maneja los eventos del usuario?

Los controles tienen propiedades de eventos, como `on_click`. Al hacer clic, Flet ejecuta la función o método asociado y le pasa un objeto de evento. El método puede cambiar los datos y actualizar los controles. En este ejemplo, los botones llaman a los métodos `incrementar`, `disminuir` y `reiniciar`.

## 6. Ventajas y limitaciones frente a Tkinter

### Ventajas
- Permite crear interfaces modernas.
- Puede utilizarse para aplicaciones web, de escritorio y móviles.
- Ofrece controles y herramientas de distribución de interfaces.
- Los eventos se conectan directamente con funciones y métodos de Python.

### Limitaciones
- Debe instalarse por separado; Tkinter suele venir incluido con Python.
- El empaquetado y publicación para algunas plataformas requiere pasos adicionales.
- Puede consumir más recursos que una interfaz de escritorio muy sencilla.
- Tkinter puede ser más directo para programas pequeños que solo necesitan una ventana local.

## 7. Desarrollo del ejemplo

La aplicación es un contador que comienza en cero. El botón **Incrementar** suma uno, **Disminuir** resta uno y **Reiniciar** devuelve el valor a cero. El nuevo número aparece inmediatamente en la ventana.

## 8. Explicación del funcionamiento

1. Flet crea la página y la entrega a la función `main(page)`.
2. Se crea un objeto de la clase `ContadorApp`.
3. El método `construir()` configura la ventana y agrega los controles.
4. Cada botón registra un método mediante `on_click`.
5. Al hacer clic, se ejecuta el método correspondiente.
6. El método modifica el atributo `valor` y llama a `actualizar()`.
7. `actualizar()` cambia el texto del contador y ejecuta `page.update()`.

## 9. Reto adicional: programación orientada a objetos

Flet permite organizar la aplicación mediante clases y objetos. La clase `ContadorApp` concentra el estado y el comportamiento de la interfaz.

- `page`: referencia a la ventana principal.
- `valor`: almacena el contador.
- `numero`: control visual que muestra el valor.
- `construir()`: crea y organiza los componentes.
- `incrementar(e)`: suma uno al valor.
- `disminuir(e)`: resta uno.
- `reiniciar(e)`: establece el valor en cero.
- `actualizar()`: sincroniza el valor con el texto de la interfaz.

La función `main(page)` instancia la clase y llama a `construir()`. Así, los datos y las acciones relacionadas quedan agrupados en un objeto.

## 10. Evidencia

Ejecuta la aplicación, pulsa **Incrementar** y toma una captura real donde se vea el contador funcionando. Guarda la imagen en la carpeta `evidencias/` con el nombre `captura_aplicacion.png`. La captura no se genera automáticamente: debe tomarse en el equipo donde se ejecute el programa.

## 11. Fuentes consultadas

1. Documentación oficial de Flet: https://flet.dev/docs/
2. Crear una aplicación Flet: https://flet.dev/docs/getting-started/create-flet-app/
3. Controles de Flet: https://flet.dev/docs/controls/
4. Sitio oficial de Python: https://www.python.org/

