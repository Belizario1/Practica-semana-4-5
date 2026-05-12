# Informe Comparativo: Patrones de Diseño Creacionales
**Docente** Ing. Zanabria Galvez Aldo Hernan  
**Nombre:** David Victor Belizario yana  
**Curso:** Programación Orientada a Objetos II  
**Fecha:** 11/05/2026

---

## Índice

1. Introducción
2. Patrón Singleton
3. Patrón Factory
4. Patrón Builder
5. Investigación: Django ORM y Factory
6. Investigación: Spring Boot y Singleton
7. Investigación: Builder en Tkinter vs Qt
8. Conclusión
9. Referencias

---

## 1. Introducción

Los patrones de diseño creacionales son soluciones ya probadas para problemas comunes relacionados con la creación de objetos. En lugar de crear objetos directamente con `new` o llamando a constructores, estos patrones nos dan formas más flexibles y reutilizables de crear instancias.

En este informe se explican tres patrones creacionales importantes: Singleton, Factory y Builder. Para cada uno se incluye un ejemplo de código, diagrama UML, y una investigación sobre cómo se usan en frameworks reales como Django, Spring Boot, Tkinter y Qt.

---

## 2. Patrón Singleton

### ¿Qué es?

El patrón Singleton garantiza que una clase tenga solo **una única instancia** en toda la aplicación, y proporciona un punto de acceso global a ella.

### ¿Cuándo se usa?

- Configuraciones globales del sistema
- Conexiones a bases de datos
- Loggers (sistemas de registro)
- Manejo de recursos compartidos (impresoras, archivos)

### Ejemplo en C++

```cpp
#include <iostream>
using namespace std;

class Config {
private:
    static Config* instance;
    Config() {} // Constructor privado
public:
    static Config* getInstance() {
        if (!instance) instance = new Config();
        return instance;
    }
    void showMessage() { cout << "Configuración global cargada.\n"; }
};
Config* Config::instance = nullptr;

int main() {
    Config* obj1 = Config::getInstance();
    Config* obj2 = Config::getInstance();
    obj1->showMessage();
    cout << "¿Son iguales? " << (obj1 == obj2) << endl;
    return 0;
}
```
### Salida del programa
```text
Configuración global cargada.
¿Son iguales? 1
```
## 3. Patrón Factory

### ¿Qué es?
El patrón Factory proporciona una interfaz para crear objetos, pero permite que las subclases decidan qué clase instanciar. Centraliza la creación de objetos en un solo lugar.

### ¿Cuándo se usa?
- Cuando no sabes de antemano qué tipo de objeto vas a necesitar
- Cuando la creación del objeto es compleja
- Para desacoplar el código que usa los objetos del código que los crea

### Ejemplo en Python

```python
class Transporte:
    def entregar(self):
        pass

class Camion(Transporte):
    def entregar(self):
        return "Entrega por carretera"

class Barco(Transporte):
    def entregar(self):
        return "Entrega por mar"

class Avion(Transporte):
    def entregar(self):
        return "Entrega por aire"

class Factory:
    @staticmethod
    def get_transporte(tipo):
        if tipo == "camion": return Camion()
        elif tipo == "barco": return Barco()
        elif tipo == "avion": return Avion()

t = Factory.get_transporte("avion")
print(t.entregar())
```
### Salida del programa
```text
Entrega por aire
```
## 4. Patrón Builder

### ¿Qué es?

El patrón Builder construye objetos complejos paso a paso. Permite crear diferentes representaciones del mismo tipo de objeto usando el mismo proceso de construcción.

### ¿Cuándo se usa?

- Cuando un objeto tiene muchas partes o atributos opcionales
- Cuando necesitas diferentes formas de construir el mismo objeto
- Para evitar tener constructores con muchos parámetros

### Ejemplo en Python (Combo de fast food)

```python
class Combo:
    def __init__(self):
        self.hamburguesa = None
        self.bebida = None
        self.papas = None

class Builder:
    def __init__(self):
        self.combo = Combo()
    
    def add_hamburguesa(self, tipo):
        self.combo.hamburguesa = tipo
        return self
    
    def add_bebida(self, bebida):
        self.combo.bebida = bebida
        return self
    
    def add_papas(self, papas):
        self.combo.papas = papas
        return self
    
    def build(self):
        return self.combo

combo = Builder().add_hamburguesa("Doble").add_bebida("Coca Cola").add_papas("Grandes").build()
print(vars(combo))
```
### Salida Del Programa
```text
{'hamburguesa': 'Doble', 'bebida': 'Coca Cola', 'papas': 'Grandes'}
```
## 5. Investigación: Django ORM y el patrón Factory

### ¿Qué es Django ORM?
Django es un framework para hacer páginas web con Python. El ORM (Mapeo Objeto-Relacional) es la parte que permite trabajar con bases de datos usando objetos de Python en lugar de escribir consultas SQL.

### ¿Dónde aparece el patrón Factory?
El "manager" de Django, que por defecto se llama **objects**, actúa como una fábrica. Se encarga de crear instancias de los modelos y guardarlas en la base de datos.

### Ejemplo básico

```python
# Defines un modelo (una tabla en la base de datos)
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

# La fábrica 'objects' crea y guarda productos
producto = Producto.objects.create(nombre="Camiseta", precio=19.99)
```
### ¿Qué hace el método `create()`?
1. Crea un objeto `Producto` en memoria
2. Genera la consulta SQL de inserción
3. Ejecuta la consulta en la base de datos
4. Asigna automáticamente el ID al objeto

### ¿Por qué es útil?
Sin el patrón Factory, tendrías que hacer todo eso manualmente. Con la fábrica `objects`, la creación y el guardado están unificados en un solo paso. Además, puedes crear tus propias fábricas personalizadas:

```python
class ProductoManager(models.Manager):
    def producto_en_oferta(self, nombre, precio):
        return self.create(nombre=nombre, precio=precio * 0.7)

# Uso
Producto.objects.producto_en_oferta("Oferta especial", 100)
```
### Conclusión
Django usa Factory para abstraer la creación de objetos de base de datos. El programador no necesita saber cómo se guarda el objeto, solo que la fábrica lo hace por él.
## 6. Investigación: Spring Boot y el patrón Singleton

### ¿Qué es Spring Boot?
Spring Boot es un framework para Java muy usado en aplicaciones empresariales. Una de sus características principales es la "Inyección de Dependencias", que permite que el framework administre los objetos (llamados Beans) por ti.

### ¿Cómo usa Singleton?
Por defecto, Spring Boot maneja todos sus Beans como Singleton. Esto significa que solo existe una instancia de cada Bean en toda la aplicación.

### Ejemplo básico

```java
@Component  // Con esta anotación, Spring administra esta clase
public class ConexionBaseDatos {
    private String url = "localhost:5432/miapp";
    
    public void conectar() {
        System.out.println("Conectando a: " + url);
    }
}
```
Cuando la aplicación arranca, Spring crea UNA SOLA instancia de ConexionBaseDatos. Luego, donde sea que necesites usarla, Spring te inyecta la misma instancia:
```java
@Component
public class UsuarioService {
    @Autowired  // Spring inyecta el Singleton aquí
    private ConexionBaseDatos db;
    
    public void guardarUsuario() {
        db.conectar();  // Usa la misma conexión que en otros lugares
    }
}
```
### ¿Por qué Singleton?

**Ventajas:**
- Ahorra memoria (solo un objeto en lugar de muchos)
- Mejora el rendimiento
- Es ideal para objetos que no tienen estado (stateless)
- Facilita el acceso a recursos compartidos como conexiones a bases de datos o servicios de logging

### ¿Y si necesitas múltiples instancias?
Spring permite cambiar el comportamiento con la anotación `@Scope`:

```java
@Component
@Scope("prototype")  // Ahora crea una nueva instancia cada vez
public class CarritoDeCompras {
    // Cada usuario tendrá su propio carrito
}
```
### Conclusión
Spring Boot usa Singleton por defecto porque es la opción más eficiente para la mayoría de los casos. Solo cuando un objeto necesita guardar información específica de cada usuario se cambia a otro tipo de alcance.
## 7. Investigación: Builder en Tkinter vs Qt

### Contexto
Tkinter y Qt son dos bibliotecas para crear interfaces gráficas (ventanas, botones, formularios). Tkinter viene incluido con Python; Qt es más potente pero necesita instalación aparte.

### Tkinter
Tkinter **no** tiene un Builder explícito. La construcción de la interfaz se hace creando widgets y luego mostrándolos uno por uno.

### Ejemplo con Tkinter:

```python
import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi programa")

# Crear un botón
boton = tk.Button(ventana, text="Clic")
boton.pack()  # Mostrar el botón

# Crear una etiqueta
etiqueta = tk.Label(ventana, text="Hola")
etiqueta.pack()  # Mostrar la etiqueta

ventana.mainloop()
```
**Características de Tkinter:**
- No hay un "plan de construcción" claro
- Cada widget se configura por separado
- El código se vuelve desordenado si la interfaz es grande
- Bueno para programas pequeños o para aprender
### Qt
Qt **sí** implementa el patrón Builder a través de los **Layouts**. Los Layouts son organizadores que permiten agregar widgets paso a paso y luego construir la ventana final.

### Ejemplo con Qt:

```python
from PyQt5.QtWidgets import *

app = QApplication([])

# El Layout actúa como Builder
layout = QVBoxLayout()  # Organización vertical

# Agregamos widgets paso a paso
layout.addWidget(QLabel("Bienvenido"))
layout.addWidget(QPushButton("Aceptar"))
layout.addWidget(QPushButton("Cancelar"))

# Construimos la ventana final
ventana = QWidget()
ventana.setLayout(layout)
ventana.show()

app.exec_()
```
### Características de Qt:
- Separación clara entre "qué" widgets y "cómo" se organizan
- Se puede cambiar la estructura sin modificar los widgets
- Los Layouts se pueden anidar (vertical dentro de horizontal, etc.)
- Perfecto para aplicaciones grandes y complejas

### Comparación directa

| Aspecto | Tkinter | Qt |
|---------|---------|-----|
| Implementa Builder | No | Sí |
| Organización del código | Manual | Estructurada |
| Reutilización de estructuras | Difícil | Fácil |
| Aprendizaje | Muy fácil | Media dificultad |
| Para proyectos grandes | No recomendado | Recomendado |
### ¿Por qué Qt usa Builder y Tkinter no?

- **Tkinter** fue diseñado para ser simple. Es como tener una caja de herramientas básica: puedes hacer cosas, pero no hay un sistema organizado.
- **Qt** fue diseñado para aplicaciones profesionales. El patrón Builder permite construir interfaces complejas de manera ordenada, como seguir un plano de construcción paso a paso.

---

## 8. Conclusión

Los tres patrones creacionales cumplen funciones diferentes y cada uno es útil en situaciones específicas:

| Patrón | Problema que resuelve | Mejor usado cuando... |
|--------|----------------------|----------------------|
| Singleton | Tener una sola instancia | Necesitas un recurso compartido (configuración, conexión DB) |
| Factory | No saber qué tipo crear | La creación es compleja o varía según condiciones |
| Builder | Construir objetos complejos | Un objeto tiene muchas partes y se puede construir de varias formas |

### En el mundo real
Estos patrones aparecen constantemente:
- **Django** usa Factory en su ORM para crear modelos
- **Spring Boot** usa Singleton para manejar sus Beans de forma eficiente
- **Qt** usa Builder para construir interfaces gráficas complejas mientras que Tkinter no

### Aprendizaje
Aprender estos patrones ayuda a escribir código más ordenado, reutilizable y fácil de mantener. No son reglas obligatorias, sino herramientas que se usan cuando el problema lo amerita.
## 9. Referencias

- Gamma, E., Helm, R., Johnson, R., & Vlissides, J. (1994). *Design Patterns: Elements of Reusable Object-Oriented Software*. Addison-Wesley.

- Django Documentation. (2024). Models and databases. https://docs.djangoproject.com/

- Spring Framework Documentation. (2024). The IoC Container. https://docs.spring.io/

- Python Software Foundation. (2024). tkinter documentation. https://docs.python.org/3/library/tkinter.html

- Qt Project. (2024). Qt Documentation. https://doc.qt.io/
