# Informe Comparativo: Patrones de Diseño Creacionales

**Autor:** David Victor Belizario yana  
**Curso:** Programación Orientada a Objetos  
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
