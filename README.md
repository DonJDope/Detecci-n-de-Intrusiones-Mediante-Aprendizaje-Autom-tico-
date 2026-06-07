🛡️ IDS Pipeline — Detección de Intrusiones con Machine Learning

Pipeline de evaluación, auditoría e impacto operativo para la detección de tráfico malicioso en redes mediante clasificación supervisada.
Proyecto Integrador · Aprendizaje Máquina · Universidad Veracruzana · 2026


📋 Descripción
Este proyecto implementa un sistema de detección de intrusiones (IDS) basado en aprendizaje automático que clasifica flujos de red como tráfico Normal (0) o Ataque (1) usando características extraídas de registros Netflow normalizados.
Se comparan dos algoritmos:

Random Forest — modelo principal, exportado para producción vía joblib
Gaussian Naive Bayes — modelo de referencia comparativa


📁 Estructura del repositorio
ids-ml-pipeline/
│
├── Proyecto_AM.py          # Script principal: entrenamiento, evaluación y comparación
├── Formateados.csv         # Dataset de tráfico de red (no incluido — ver sección Dataset)
├── requirements.txt        # Dependencias del entorno Python
├── README.md               # Este archivo

⚙️ Requisitos del entorno

Python 3.9 o superior
pip

Dependencias
pandas
numpy
matplotlib
seaborn
scikit-learn
joblib
rich
Instálalas todas de una vez con:
bashpip install -r requirements.txt
Contenido del archivo requirements.txt:
pandas>=1.5.0
numpy>=1.23.0
matplotlib>=3.6.0
seaborn>=0.12.0
scikit-learn>=1.2.0
joblib>=1.2.0
rich>=13.0.0

🗂️ Dataset
El script espera el archivo Formateados.csv en el mismo directorio de trabajo.
El dataset debe contener al menos las siguientes columnas (por índice de posición):
ÍndiceNombre de columnaDescripción0FamilyEtiqueta: Normal u otro ataque6Netflow Bytes NormalizadoVolumen de datos del flujo7Payload Size NormalizadoTamaño de la carga útil8Number of Packets NormalizadoCantidad de paquetes9Response Time NormalizadoLatencia del flujo10Data Transfer Rate NormalizadoVelocidad de transferencia

Nota: El archivo Formateados.csv no está incluido en el repositorio por su tamaño. Colócalo manualmente en la raíz del proyecto antes de ejecutar el script.


🚀 Pasos de ejecución
1. Clonar el repositorio
bashgit clone https://github.com/<usuario>/<repositorio>.git
cd <repositorio>
2. (Opcional) Crear un entorno virtual
bashpython -m venv venv

# Linux / macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
3. Instalar dependencias
bashpip install -r requirements.txt
4. Colocar el dataset
Copia el archivo Formateados.csv en la raíz del repositorio:
bash# Ejemplo si lo tienes en otra carpeta
cp /ruta/a/tu/Formateados.csv .
5. Ejecutar el pipeline
bashpython Proyecto_AM.py

📊 Salida esperada
Al ejecutar el script correctamente verás en consola:

Cantidad de registros cargados
Confirmación de entrenamiento del modelo Random Forest (ESCUDO ENTRENADO)
Tabla de métricas técnicas: Accuracy, Recall y Especificidad del RF
Precisión del modelo Naive Bayes
Generación del archivo modelo_ids_cyber.joblib

Archivos generados
ArchivoDescripciónmodelo_ids_cyber.joblibModelo Random Forest serializado, listo para inferencia

🔬 Usar el modelo en producción
Una vez generado modelo_ids_cyber.joblib, puedes cargarlo y usarlo para predecir nuevos flujos sin reentrenar:
pythonimport joblib
import pandas as pd

# Cargar el modelo entrenado
modelo = joblib.load('modelo_ids_cyber.joblib')

# Ejemplo de nuevo flujo de red (valores normalizados)
nuevo_flujo = pd.DataFrame([{
    'Netflow Bytes Normalizado': 0.42,
    'Payload Size Normalizado': 0.17,
    'Number of Packets Normalizado': 0.85,
    'Response Time Normalizado': 0.03,
    'Data Transfer Rate Normalizado': 0.61
}])

prediccion = modelo.predict(nuevo_flujo)
probabilidad = modelo.predict_proba(nuevo_flujo)

print("Clase predicha:", "Ataque" if prediccion[0] == 1 else "Normal")
print(f"Probabilidad de ataque: {probabilidad[0][1]*100:.2f}%")

👥 Integrantes del equipo
NombreMatrícula[Christopher Gomez][Ruth Avendaño][Mario Erik Flandes][Irvin Josafat Dominguez][Jesus Valentin Mora]
Docente: [Max Willian Millan Martinez ]
Materia: Aprendizaje Máquina
Período: Enero – Julio 2026

📄 Licencia
Proyecto académico desarrollado para la materia de Aprendizaje Máquina de la Ingeniería en Ciberseguridad, Universidad Veracruzana. Uso exclusivamente educativo.
