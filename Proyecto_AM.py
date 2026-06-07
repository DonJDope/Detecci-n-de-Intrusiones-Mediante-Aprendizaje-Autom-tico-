from sklearn.metrics import precision_score, recall_score, f1_score, roc_curve, auc
import matplotlib.pyplot as plt
import seaborn as sns

# 1. OBTENER PREDICCIONES Y PROBABILIDADES DE AMBOS MODELOS
# Random Forest (ya lo tenías, pero sacamos probabilidades para el AUC/ROC)
pred_rf = modelo_rf.predict(X_test)
prob_rf = modelo_rf.predict_proba(X_test)[:, 1]

# Naive Bayes
pred_bayes = modelo_bayes.predict(X_test)
prob_bayes = modelo_bayes.predict_proba(X_test)[:, 1]

# 2. TABLA COMPARATIVA DE MÉTRICAS (Estructura para tu reporte PDF)
tabla_comparativa = Table(title="[bold purple]Comparativa de Modelos de Detección")
tabla_comparativa.add_column("Métrica", style="bold")
tabla_comparativa.add_column("Random Forest", justify="right")
tabla_comparativa.add_column("Naive Bayes", justify="right")

def calcular_metricas(y_real, y_pred, y_prob):
    return [
        accuracy_score(y_real, y_pred),
        precision_score(y_real, y_pred, zero_division=0),
        recall_score(y_real, y_pred, zero_division=0),
        f1_score(y_real, y_pred, zero_division=0),
        auc(*roc_curve(y_real, y_prob)[:2]) # Calcula AUC directamente
    ]

met_rf = calcular_metricas(y_test, pred_rf, prob_rf)
met_nb = calcular_metricas(y_test, pred_bayes, prob_bayes)
nombres_metricas = ["Accuracy (Exactitud)", "Precision (Precisión)", "Recall (Sensibilidad)", "F1-Score", "AUC (Área bajo la curva)"]

for nombre, val_rf, val_nb in zip(nombres_metricas, met_rf, met_nb):
    tabla_comparativa.add_row(nombre, f"{val_rf*100:.2f}%", f"{val_nb*100:.2f}%")

console.print(tabla_comparativa)

# 3. MATRICES DE CONFUSIÓN (Ambos modelos)
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

sns.heatmap(confusion_matrix(y_test, pred_rf), annot=True, fmt='d', cmap='Blues', 
            xticklabels=['Normal', 'Ataque'], yticklabels=['Normal', 'Ataque'], ax=axes[0])
axes[0].set_title('Matriz de Confusión: Random Forest')
axes[0].set_xlabel('Predicción')
axes[0].set_ylabel('Realidad')

sns.heatmap(confusion_matrix(y_test, pred_bayes), annot=True, fmt='d', cmap='Oranges', 
            xticklabels=['Normal', 'Ataque'], yticklabels=['Normal', 'Ataque'], ax=axes[1])
axes[1].set_title('Matriz de Confusión: Naive Bayes')
axes[1].set_xlabel('Predicción')
axes[1].set_ylabel('Realidad')

plt.tight_layout()
plt.show()

# 4. GRÁFICA DE LA CURVA ROC COMPARATIVA
fpr_rf, tpr_rf, _ = roc_curve(y_test, prob_rf)
fpr_nb, tpr_nb, _ = roc_curve(y_test, prob_bayes)

plt.figure(figsize=(8, 6))
plt.plot(fpr_rf, tpr_rf, color='blue', lw=2, label=f'Random Forest (AUC = {met_rf[4]:.3f})')
plt.plot(fpr_nb, tpr_nb, color='orange', lw=2, label=f'Naive Bayes (AUC = {met_nb[4]:.3f})')
plt.plot([0, 1], [0, 1], color='gray', linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('Tasa de Falsos Positivos (Falsas Alarmas)')
plt.ylabel('Tasa de Verdaderos Positivos (Detecciones Correctas)')
plt.title('Curva ROC: Análisis de Modelos de Intrusión')
plt.legend(loc="lower right")
plt.show()