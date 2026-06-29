---
name: notion-academic-sync
description: Sincroniza apuntes académicos en Markdown con Notion, aplicando un formato enriquecido (iconos, banners, bloques de código, colores) siguiendo los estándares de la cursada de Estructura de Datos.
---

# Notion Academic Sync

Este skill automatiza la carga de archivos Markdown (.md) a una base de datos o página de Notion, transformando el contenido plano en una estructura visualmente atractiva y didáctica.

## 🛠️ Procedimiento de Carga

1. **Identificar origen:** Localizar los archivos `.md` de la clase o tema (ej. `Clase 1/clase1.md`).
2. **Utilizar API Nativa (2026):** El skill utiliza el parámetro `markdown` nativo de la API de Notion (versión `2026-03-11`). Esto garantiza que Notion traduzca perfectamente todos los elementos (`#`, `**`, `*`, lists, etc.) sin dejar caracteres especiales visibles.
3. **Formato Automático:**
   - **Títulos y Secciones:** Se renderizan como bloques nativos de Notion según el nivel de `#`.
   - **Formato de Texto:** Las negritas, itálicas y links se aplican correctamente como estilos de texto.
   - **Código:** Los bloques de código se crean con el lenguaje correspondiente y resaltado de sintaxis.
   - **Iconos y Banners:** Se asigna un icono representativo y una imagen de portada automáticamente.

## 🐍 Script de Automatización

El skill utiliza `scripts/upload_enhanced.py`, que envía el contenido Markdown íntegro a Notion, permitiendo que la plataforma realice la conversión perfecta.

## 🎨 Estándares de Diseño (Notion)
- **Fondo:** Dark mode (por defecto del usuario).
- **Iconos:** Usar emojis representativos por clase (ej. 📚 para Intro, ⚙️ para Funciones).
- **Colores:** Usar `blue` para conceptos teóricos y `yellow` para alertas o errores comunes.
