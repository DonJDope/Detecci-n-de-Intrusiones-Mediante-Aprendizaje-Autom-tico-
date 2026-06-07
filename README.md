# 🛡️ IDS Pipeline — Detección de Intrusiones con Machine Learning

Pipeline de evaluación, auditoría e impacto operativo para la detección de tráfico malicioso en redes mediante clasificación supervisada.

**Proyecto Integrador · Aprendizaje Máquina · Universidad Veracruzana · 2026**

---

## 📋 Descripción

Este proyecto implementa un **Sistema de Detección de Intrusiones (IDS)** basado en aprendizaje automático que clasifica flujos de red como:

- **Normal (0)**
- **Ataque (1)**

Utilizando características extraídas de registros **Netflow** previamente normalizados.

### Algoritmos evaluados

- 🌳 **Random Forest**
  - Modelo principal.
  - Exportado para producción mediante `joblib`.

- 📈 **Gaussian Naive Bayes**
  - Modelo de referencia para comparación.

---

## 📁 Estructura del repositorio

```text
ids-ml-pipeline/
│
├── Proyecto_AM.py          # Script principal
├── Formateados.csv         # Dataset (no incluido)
├── requirements.txt        # Dependencias
└── README.md               # Documentación
```

---

## ⚙️ Requisitos del entorno

### Software

- Python 3.9 o superior
- pip

### Dependencias

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- joblib
- rich

Instalación rápida:

```bash
pip install -r requirements.txt
```

### Contenido sugerido de `requirements.txt`

```text
pandas>=1.5.0
numpy>=1.23.0
matplotlib>=3.6.0
seaborn>=0.12.0
scikit-learn>=1.2.0
joblib>=1.2.0
rich>=13.0.0
```

---

## 🗂️ Dataset

El script espera encontrar el archivo:

```text
Formateados.csv
```

en el mismo directorio del proyecto.

### Variables requeridas

| Índice | Columna | Descripción |
|---------|----------|-------------|
| 0 | Family | Etiqueta de clase (Normal o Ataque) |
| 6 | Netflow Bytes Normalizado | Volumen de datos del flujo |
| 7 | Payload Size Normalizado | Tamaño de la carga útil |
| 8 | Number of Packets Normalizado | Cantidad de paquetes |
| 9 | Response Time Normalizado | Latencia del flujo |
| 10 | Data Transfer Rate Normalizado | Velocidad de transferencia |

> **Nota:** El archivo `Formateados.csv` no se incluye en el repositorio debido a su tamaño. Debe colocarse manualmente antes de ejecutar el proyecto.

---

## 🚀 Pasos de ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/USUARIO/ids-ml-pipeline.git
cd ids-ml-pipeline
```

### 2. Crear un entorno virtual (Opcional)

#### Linux / macOS

```bash
python -m venv venv
source venv/bin/activate
```

#### Windows

```powershell
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Colocar el dataset

Copiar el archivo `Formateados.csv` a la raíz del proyecto.

Ejemplo:

```bash
cp /ruta/a/Formateados.csv .
```

### 5. Ejecutar el pipeline

```bash
python Proyecto_AM.py
```

---

## 📊 Salida esperada

Al ejecutar correctamente el script se mostrará:

- Cantidad de registros cargados.
- Confirmación de entrenamiento del modelo Random Forest.
- Métricas técnicas:
  - Accuracy
  - Recall
  - Especificidad
- Precisión del modelo Gaussian Naive Bayes.
- Generación del modelo serializado.

### Archivo generado

| Archivo | Descripción |
|----------|------------|
| `modelo_ids_cyber.joblib` | Modelo Random Forest entrenado y listo para inferencia |

---

## 🔬 Uso del modelo entrenado

Una vez generado el archivo:

```text
modelo_ids_cyber.joblib
```

puede utilizarse sin necesidad de reentrenar el modelo.

```python
import joblib
import pandas as pd

# Cargar modelo
modelo = joblib.load("modelo_ids_cyber.joblib")

# Nuevo flujo de red
nuevo_flujo = pd.DataFrame([{
    "Netflow Bytes Normalizado": 0.42,
    "Payload Size Normalizado": 0.17,
    "Number of Packets Normalizado": 0.85,
    "Response Time Normalizado": 0.03,
    "Data Transfer Rate Normalizado": 0.61
}])

prediccion = modelo.predict(nuevo_flujo)
probabilidad = modelo.predict_proba(nuevo_flujo)

print(
    "Clase predicha:",
    "Ataque" if prediccion[0] == 1 else "Normal"
)

print(
    f"Probabilidad de ataque: {probabilidad[0][1] * 100:.2f}%"
)
```

---

## 📈 Métricas evaluadas

El proyecto evalúa los modelos mediante:

- Accuracy
- Recall
- Especificidad
- Matriz de confusión

Estas métricas permiten medir la capacidad del IDS para detectar tráfico malicioso minimizando falsos positivos y falsos negativos.

---

## 👥 Integrantes del equipo

| Integrante |
|------------|
| Christopher Gomez |
| Ruth Avendaño |
| Mario Erik Flandes |
| Irvin Josafat Dominguez |
| Jesus Valentin Mora |

### Docente

**Max Willian Millán Martínez**

### Materia

**Aprendizaje Máquina**

### Período

**Enero – Julio 2026**

---

## 📄 Licencia

Proyecto académico desarrollado para la experiencia educativa **Aprendizaje Máquina** de la **Ingeniería en Ciberseguridad** de la Universidad Veracruzana.

Su uso está destinado exclusivamente a fines educativos y de investigación.
