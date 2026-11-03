# Hydrocalafquen 

**Hydrocalafquen** es una plataforma tecnológica integral para la exploración recreativa, la zonificación acuática y el registro de actividades deportivas en el Lago Calafquén. Combina una interfaz web cartográfica con una aplicación de escritorio/móvil orientada a la bitácora técnica de buceo y entrenamiento de apnea.

---

##  Arquitectura y Tecnologías

* **Módulo Web (Mapa Interactivo):** HTML5, CSS3, JavaScript (Leaflet.js), PHP y MySQL.
* **Módulo Móvil/Escritorio (Bitácora & Apnea):** Python, Framework Kivy / KivyMD.
* **Persistencia de Datos:** Arquitectura relacional SQL (SQLite local en cliente, MySQL en servidor web).
* **Control de Versiones:** Git & GitHub.

---

##  Estructura del Proyecto

```text
hidrocalafquenproyect/
├── web/                  # Plataforma web y API en PHP/MySQL
│   ├── assets/
│   ├── api/
│   └── index.php
├── app/                  # Aplicación en Python con Kivy
│   ├── database/         # Modelos relacionales de SQLite
│   ├── ui/               # Vistas y pantallas KivyMD
│   └── main.py
├── .gitignore
└── README.md
