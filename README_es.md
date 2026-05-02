<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=24,30,2&height=160&section=header&text=learn--python--with--ai&fontSize=38&fontColor=ffffff&fontAlignY=38&desc=The+only+Python+course+you+need+in+the+AI+era&descAlignY=58&descSize=14" alt="Header"/>

[![Stars](https://img.shields.io/github/stars/unrealandychan/learn-python-with-ai?style=for-the-badge&logo=github&color=f78166&logoColor=white&labelColor=0d1117)](https://github.com/unrealandychan/learn-python-with-ai/stargazers)
[![Forks](https://img.shields.io/github/forks/unrealandychan/learn-python-with-ai?style=for-the-badge&logo=github&color=79c0ff&logoColor=white&labelColor=0d1117)](https://github.com/unrealandychan/learn-python-with-ai/network/members)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&style=for-the-badge&logoColor=white&labelColor=0d1117)](https://python.org)
[![60 Lecciones](https://img.shields.io/badge/60_Lecciones-AI--First-blueviolet?style=for-the-badge&labelColor=0d1117)](.)
[![License](https://img.shields.io/github/license/unrealandychan/learn-python-with-ai?style=for-the-badge&labelColor=0d1117)](LICENSE)

</div>

---

# 🤖 El Único Curso de Python que Necesitas en la Era de la IA

[English](README.md) | [中文版](README_zh.md) | [Inicio Rápido](#-inicio-rápido) | [Plan de Estudios](#-plan-de-estudios) | [Tecnologías](#-tecnologías)

![Banner](public/banner.png)

> **60 lecciones. Sin requisitos previos. Un solo objetivo: convertirte en un desarrollador Python que construye aplicaciones de IA reales.**

---

## 🎯 Filosofía del Curso

La mayoría de los cursos de Python te enseñan a imprimir "Hello, World!" y ya. Este curso es diferente.

**Cada concepto se enseña a través de una perspectiva de IA:**

- En lugar de "aprende variables" → **"analiza la respuesta de una API de LLM en variables"**
- En lugar de "aprende listas" → **"procesa un lote de resultados generados por IA"**
- En lugar de "aprende archivos E/S" → **"guarda y carga historiales de conversación"**
- En lugar de "aprende clases" → **"crea componentes de pipeline de IA reutilizables"**

Al final, no solo sabrás Python — podrás construir aplicaciones de IA que realmente funcionen.

---

## ✨ Características Destacadas

| Característica | Descripción |
|---|---|
| 🎓 **60 Lecciones** | Desde "Hola Mundo" hasta aplicaciones de IA en producción |
| 🤖 **IA como eje central** | Cada ejercicio usa contexto de IA y patrones del mundo real |
| 🔨 **Basado en proyectos** | Crea cosas reales: chatbots, agentes, APIs, pipelines de datos |
| 📦 **Stack moderno** | OpenAI SDK, LangChain, FastAPI, Pandas, NumPy |
| 🆓 **Sin API Key necesaria** | Todos los ejercicios usan clientes simulados — conecta la API real cuando estés listo |
| 🔰 **Sin requisitos previos** | Verdaderamente amigable para principiantes — no se requiere experiencia previa en programación |

---

## 🚀 Inicio Rápido

### 1. Obtén el Código

```bash
git clone https://github.com/unrealandychan/learn-python-with-ai.git
cd learn-python-with-ai
```

### 2. Configura Python (3.11+)

```bash
# Verifica tu versión
python --version   # Debe ser 3.11 o superior

# Si no está instalado: https://www.python.org/downloads/
```

### 3. Crea un Entorno Virtual

```bash
# Usando uv (recomendado — el más rápido)
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv && source .venv/bin/activate

# O usando pip estándar
python -m venv .venv && source .venv/bin/activate  # macOS/Linux
python -m venv .venv && .venv\Scripts\activate      # Windows
```

### 4. Instala las Dependencias

```bash
pip install -r requirements.txt
```

### 5. ¡Empieza a Aprender!

```bash
# Comienza con la lección 1
cd lesson_01_intro_to_python
python exercise.py
```

### 6. (Opcional) Agrega tu API Key de OpenAI

```bash
# Crea un archivo .env
echo "OPENAI_API_KEY=sk-tu-clave-aquí" > .env
```

> **Nota**: Todas las lecciones funcionan con clientes de IA simulados — no necesitas una API key para aprender. Agrégala cuando estés listo para usar las APIs reales.

---

## 📚 Plan de Estudios

### 🟢 Módulo 1: Fundamentos de Python (Lecciones 1–20)
*Python esencial con contexto de IA — comprende cada concepto en términos de cómo se usa en el desarrollo de IA.*

| Lección | Tema | Aplicación de IA |
|---------|------|------------------|
| 01 | Introducción a Python | Por qué Python domina la IA |
| 02 | Variables y Tipos de Datos | Almacenar respuestas de LLM en variables |
| 03 | Operadores Básicos | Procesar puntuaciones de respuestas de API |
| 04 | Entrada de Usuario y Conversión de Tipos | Crear herramientas de IA interactivas |
| 05 | Sentencias Condicionales | Enrutamiento basado en resultados de clasificación de IA |
| 06 | Listas | Almacenar múltiples elementos generados por IA |
| 07 | Métodos de Listas | Gestionar arreglos de mensajes de conversación |
| 08 | Bucles For | Iterar sobre resultados de IA en lote |
| 09 | Bucles While | Lógica de reintento para llamadas a APIs |
| 10 | Diccionarios | Analizar respuestas JSON de APIs |
| 11 | Tuplas y Conjuntos | Deduplicar resultados de IA |
| 12 | Definir Funciones | Funciones auxiliares de IA reutilizables |
| 13 | Argumentos y Retornos de Funciones | Crear envoltorios de API flexibles |
| 14 | Ámbito de Variables | Gestionar claves de API y configuración |
| 15 | Módulos e Importaciones | Usar el ecosistema de bibliotecas de IA |
| 16 | E/S de Archivos: Lectura | Cargar prompts y bases de conocimiento |
| 17 | E/S de Archivos: Escritura | Guardar resultados de IA en disco |
| 18 | Manejo de Errores | Manejo robusto de errores en llamadas a APIs |
| 19 | Introducción a POO | Modelar conversaciones de IA como objetos |
| 20 | Próximos Pasos | Mini proyecto: asistente de IA en línea de comandos |

### 🟡 Módulo 2: Python Avanzado (Lecciones 21–40)
*Patrones avanzados que todo ingeniero de IA usa a diario.*

| Lección | Tema | Aplicación de IA |
|---------|------|------------------|
| 21 | Herencia en POO | Clientes especializados de modelos de IA |
| 22 | Polimorfismo en POO | Proveedores de IA intercambiables |
| 23 | Encapsulamiento en POO | Proteger claves de API en clases |
| 24 | Métodos Dunder en POO | Objetos de respuesta de IA personalizados |
| 25 | Métodos Estáticos y de Clase | Configuración compartida entre clientes de IA |
| 26 | Comprensión de Listas | Transformar lotes de resultados de IA |
| 27 | Comprensión de Diccionarios y Conjuntos | Agregar métricas de resultados de IA |
| 28 | Funciones Lambda | Transformación en línea de datos de IA |
| 29 | Map, Filter, Reduce | Pipelines funcionales para datos de IA |
| 30 | Generadores | Transmisión eficiente en memoria de respuestas de IA |
| 31 | Decoradores | Límite de velocidad, registro, caché de llamadas a IA |
| 32 | Módulo Collections | Conteo de tokens, análisis de frecuencia |
| 33 | Fechas y Horas | Registrar marcas de tiempo en interacciones de IA |
| 34 | Datos JSON | Analizar resultados JSON de LLMs |
| 35 | Módulos OS y Sys | Operaciones del sistema de archivos para pipelines de IA |
| 36 | Multihilo | Llamadas paralelas a APIs de IA |
| 37 | Multiprocesamiento | Preprocesamiento de IA vinculado a CPU |
| 38 | Introducción a Asyncio | Comprender flujos de trabajo asíncronos de IA |
| 39 | Async/Await | Llamadas asíncronas a LLM con transmisión |
| 40 | Proyecto Avanzado | Construir un pipeline de IA asíncrono |

### 🔵 Módulo 3: Bibliotecas Esenciales (Lecciones 41–53)
*Las bibliotecas que impulsan las aplicaciones Python y de IA del mundo real.*

| Lección | Tema | Aplicación de IA |
|---------|------|------------------|
| 41 | Requests | Llamar a APIs REST y endpoints de LLM |
| 42 | BeautifulSoup4 | Extraer datos de entrenamiento de la web |
| 43 | Pandas | Preparación de datos para modelos de ML |
| 44 | Matplotlib | Visualizar métricas de modelos de IA |
| 45 | Seaborn | Visualización estadística para análisis de modelos |
| 46 | FastAPI | Servir modelos de IA como APIs REST |
| 47 | Git y GitHub | Control de versiones para proyectos de IA |
| 48 | Pytest | Probar componentes de aplicaciones de IA |
| 49 | Ruff | Calidad de código para código de IA en producción |
| 50 | Gestión de Dependencias con UV | Gestionar dependencias de proyectos de IA |
| 51 | Bases de Datos | Almacenar historial de conversaciones de IA |
| 52 | Gestión de Configuración | Gestión segura de claves de API con .env |
| 53 | Python para MCP y Skills | Construir infraestructura de llamadas a herramientas |

### 🔴 Módulo 4: Integración de IA y LLM (Lecciones 54–60)
*La vanguardia — llamar, diseñar prompts y construir con LLMs.*

| Lección | Tema | Aplicación de IA |
|---------|------|------------------|
| 54 | **OpenAI SDK** | Completaciones de chat, transmisión, llamadas a funciones, modo JSON |
| 55 | **Ingeniería de Prompts** | Few-shot prompting, CoT, formato de salida, plantillas |
| 56 | **Conceptos Básicos de LangChain** | Cadenas LCEL, memoria, analizadores de salida, patrón RAG |
| 57 | **NumPy para IA** | Matemáticas vectoriales, similitud coseno, softmax, embeddings |
| 58 | **Agentes de IA** | Patrón ReAct, registros de herramientas, el bucle del agente |
| 59 | **Embeddings Vectoriales** | Búsqueda semántica, base de datos vectorial simple, fragmentación |
| 60 | **Proyecto Final** | Construir una aplicación de IA completa desde cero |

---

## 🛠 Tecnologías

Este curso usa el ecosistema moderno de Python para IA:

| Categoría | Bibliotecas |
|-----------|-------------|
| **APIs de LLM** | `openai`, `langchain`, `langchain-openai` |
| **Ciencia de Datos** | `numpy`, `pandas`, `matplotlib`, `seaborn` |
| **Web / APIs** | `fastapi`, `httpx`, `requests`, `uvicorn` |
| **Configuración** | `python-dotenv` |
| **Herramientas de Desarrollo** | `pytest`, `ruff`, `uv` |
| **Bases de Datos** | `sqlalchemy` |
| **Web Scraping** | `beautifulsoup4` |

---

## 📋 Requisitos Previos

**Ninguno.** Este curso empieza desde cero absoluto.

Necesitas:
- Una computadora (Windows, macOS o Linux)
- Conexión a internet
- Curiosidad y ganas de aprender

NO necesitas:
- Experiencia previa en programación
- Conocimientos de matemáticas
- Una API key de OpenAI (todos los ejercicios funcionan con clientes simulados)

---

## 📁 Estructura de las Lecciones

Cada lección sigue la misma estructura:

```
lesson_XX_nombre_del_tema/
├── instructions.md    ← Lee esto primero: teoría, ejemplos, conceptos
├── exercise.py        ← Tu campo de práctica: completa los ejercicios TODO
└── solution.py        ← Verifica tu trabajo después de intentarlo por tu cuenta
```

**Cómo usar cada lección:**
1. 📖 Lee `instructions.md` de principio a fin
2. ✏️ Abre `exercise.py` y completa las secciones `# YOUR CODE HERE`
3. 🚀 Ejecuta tu archivo: `python exercise.py`
4. 🔍 Compara con `solution.py` si te atascas

---

## 💡 Consejos de Aprendizaje

- **Escribe el código** — no copies y pegues. Escribir desarrolla la memoria muscular.
- **Rompe cosas** — modifica los ejemplos y observa qué sucede.
- **Usa la IA como tutor** — pregúntale a ChatGPT o Copilot que te explique los conceptos que encuentres confusos.
- **No te saltes lecciones** — cada lección se basa en las anteriores.
- **Construye algo** — después de cada módulo, intenta construir un pequeño proyecto con lo que has aprendido.

---

## 🗺 Ruta de Aprendizaje

```
Semanas 1-4:   Lecciones 01-20  → Fundamentos de Python
Semanas 5-8:   Lecciones 21-40  → Python Avanzado
Semanas 9-12:  Lecciones 41-53  → Bibliotecas Esenciales
Semanas 13-15: Lecciones 54-60  → Integración de IA y LLM
```

> A ~4 lecciones/semana, completarás el curso en ~15 semanas. Tómate tu tiempo — la profundidad es más importante que la velocidad.

---

## 🤝 Contribuir

¿Encontraste un error? ¿Tienes una mejora? ¡Los pull requests son bienvenidos!

1. Haz un fork del repositorio
2. Crea una rama: `git checkout -b fix/leccion-42-typo`
3. Realiza tus cambios
4. Sube los cambios y abre un PR

---

## 📄 Licencia

[Licencia MIT](LICENSE) — libre para usar, compartir y modificar.

---

<div align="center">

**¡Feliz aprendizaje! Construye algo increíble. 🚀**

*Si este curso te ayudó, por favor ⭐ dale una estrella al repositorio — ¡ayuda a que otros lo encuentren!*

</div>
