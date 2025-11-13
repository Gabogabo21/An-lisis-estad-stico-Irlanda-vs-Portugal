"""
Análisis Predictivo: Moldavia vs Italia
Modelo ELO para predicción de resultados futbolísticos
"""

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.patches import Circle
import os

def crear_directorios():
    """Crear estructura de directorios si no existen"""
    os.makedirs('visualizations', exist_ok=True)
    os.makedirs('data', exist_ok=True)

def analisis_moldavia_italia():
    """Función principal de análisis"""
    
    crear_directorios()
    
    # Configuración de estilo
    plt.style.use('seaborn-v0_8')
    sns.set_palette("husl")
    
    # Crear visualizaciones
    crear_visualizaciones()
    
    print("✅ Análisis completado. Gráficos guardados en /visualizations/")

def crear_visualizaciones():
    """Crear todas las visualizaciones del proyecto"""
    
    # 1. Gráfico principal de probabilidades
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(20, 16))
    fig.suptitle('ANÁLISIS DE PROBABILIDADES: MOLDAVIA vs ITALIA', fontsize=20, fontweight='bold')
    
    # ... (aquí va todo el código de visualización que te proporcioné anteriormente)
    
    # Guardar figura principal
    plt.savefig('visualizations/analisis_completo.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # Guardar figura ELO y Tilt
    # ... (código para la segunda figura)
    plt.savefig('visualizations/elo_tilt_comparison.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    analisis_moldavia_italia()
