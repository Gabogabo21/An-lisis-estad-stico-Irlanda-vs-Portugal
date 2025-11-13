"""
Análisis Predictivo: Irlanda vs Portugal
Modelo ELO para predicción de resultados futbolísticos
Autor: [Tu Nombre]
Fecha: [Fecha]
"""

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.patches import Circle
import os

def crear_directorios():
    """Crear estructura de directorios si no existen"""
    directorios = ['visualizations', 'data', 'notebooks', 'scripts']
    for directorio in directorios:
        os.makedirs(directorio, exist_ok=True)

def guardar_datos():
    """Guardar datos crudos para referencia"""
    datos = """
    Irlanda vs Portugal - Estadísticas ELO:
    - ELO Irlanda: 87
    - ELO Portugal: 97  
    - Tilt Irlanda: -19.1%
    - Tilt Portugal: -17.9%
    - Probabilidades: Irlanda 11.4% | Empate 19.8% | Portugal 68.9%
    - Goles esperados: Irlanda 0.67 | Portugal 2.0
    """
    
    with open('data/raw_stats.txt', 'w', encoding='utf-8') as f:
        f.write(datos)

def analisis_irlanda_portugal():
    """Función principal de análisis"""
    
    print("🚀 Iniciando análisis Irlanda vs Portugal...")
    crear_directorios()
    guardar_datos()
    
    # Configuración de estilo
    plt.style.use('seaborn-v0_8')
    sns.set_palette("husl")
    
    # Crear visualizaciones principales
    crear_visualizaciones_principales()
    
    # Crear visualizaciones adicionales
    crear_visualizaciones_adicionales()
    
    print("✅ Análisis completado exitosamente!")
    print("📊 Gráficos guardados en: /visualizations/")

def crear_visualizaciones_principales():
    """Crear visualizaciones principales del análisis"""
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(20, 16))
    fig.suptitle('ANÁLISIS DE PROBABILIDADES: IRLANDA vs PORTUGAL', 
                 fontsize=20, fontweight='bold', color='#2C3E50')

    # =============================================================================
    # 1. GRÁFICO DE DONUT - PROBABILIDADES GENERALES
    # =============================================================================
    probabilidades_generales = [11.4, 19.8, 68.9]
    labels = ['Irlanda\n11.4%', 'Empate\n19.8%', 'Portugal\n68.9%']
    colors = ['#169B62', '#FFD700', '#C72C2C']

    wedges, texts, autotexts = ax1.pie(probabilidades_generales, labels=labels, colors=colors, 
                                       autopct='%1.1f%%', startangle=90)
    center_circle = Circle((0,0), 0.70, fc='white')
    ax1.add_artist(center_circle)
    ax1.set_title('PROBABILIDAD DE RESULTADO FINAL\n(Modelo ELO)', 
                  fontsize=16, fontweight='bold', pad=20)

    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
        autotext.set_fontsize(12)

    # =============================================================================
    # 2. MAPA DE CALOR DE RESULTADOS
    # =============================================================================
    resultados_matrix = [
        [6.9, 13.9, 13.9, 9.3, 4.6, 1.9, 0.6, 0.2],
        [4.6, 9.2,  9.3,  6.2, 3.1, 1.2, 0.4, 0.1],
        [1.5, 3.1,  3.1,  2.1, 1.0, 0.4, 0.1, 0.0],
        [0.3, 0.7,  0.7,  0.5, 0.2, 0.1, 0.0, 0.0],
        [0.1, 0.1,  0.1,  0.1, 0.0, 0.0, 0.0, 0.0],
    ]

    im = ax2.imshow(resultados_matrix, cmap='YlOrRd', aspect='auto')
    ax2.set_xticks(range(8))
    ax2.set_yticks(range(5))
    ax2.set_xticklabels(['0', '1', '2', '3', '4', '5', '6', '7'])
    ax2.set_yticklabels(['0', '1', '2', '3', '4'])
    ax2.set_xlabel('Goles Portugal', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Goles Irlanda', fontsize=12, fontweight='bold')
    ax2.set_title('MAPA DE CALOR - PROBABILIDADES DE RESULTADO EXACTO (%)', 
                  fontsize=16, fontweight='bold', pad=20)

    for i in range(5):
        for j in range(8):
            if resultados_matrix[i][j] >= 1.0:
                ax2.text(j, i, f'{resultados_matrix[i][j]}', 
                        ha="center", va="center", color="black", fontweight='bold')
            elif resultados_matrix[i][j] > 0:
                ax2.text(j, i, f'{resultados_matrix[i][j]}', 
                        ha="center", va="center", color="gray", fontsize=8)

    cbar = plt.colorbar(im, ax=ax2)
    cbar.set_label('Probabilidad (%)', fontsize=12)

    # =============================================================================
    # 3. TOP 10 RESULTADOS MÁS PROBABLES
    # =============================================================================
    resultados_top = {
        '0-1': 13.9, '0-2': 13.9, '1-1': 9.2, '1-2': 9.3,
        '0-3': 9.3, '0-0': 6.9, '1-3': 6.2, '1-0': 4.6,
        '0-4': 4.6, '2-2': 3.1
    }

    resultados_ordenados = dict(sorted(resultados_top.items(), 
                                     key=lambda item: item[1], reverse=True))

    bars = ax3.barh(list(resultados_ordenados.keys()), list(resultados_ordenados.values()),
                    color=['#C72C2C' if any(x in k for x in ['-0', '-1', '-2', '-3', '-4']) else 
                          '#169B62' if k.startswith(('1-', '2-')) else '#FFD700' 
                          for k in resultados_ordenados.keys()])

    ax3.set_xlabel('Probabilidad (%)', fontsize=12, fontweight='bold')
    ax3.set_title('TOP 10 RESULTADOS MÁS PROBABLES', fontsize=16, fontweight='bold', pad=20)
    ax3.invert_yaxis()

    for bar in bars:
        width = bar.get_width()
        ax3.text(width + 0.1, bar.get_y() + bar.get_height()/2, 
                 f'{width}%', ha='left', va='center', fontweight='bold')

    # =============================================================================
    # 4. COMPARATIVA DE GOLES ESPERADOS
    # =============================================================================
    equipos = ['Irlanda', 'Portugal']
    goles_esperados = [0.67, 2.0]
    colores = ['#169B62', '#C72C2C']

    bars_goles = ax4.bar(equipos, goles_esperados, color=colores, alpha=0.8)
    ax4.set_ylabel('Goles Esperados', fontsize=12, fontweight='bold')
    ax4.set_title('COMPARATIVA DE GOLES ESPERADOS (xG)', fontsize=16, fontweight='bold', pad=20)

    for bar in bars_goles:
        height = bar.get_height()
        ax4.text(bar.get_x() + bar.get_width()/2., height + 0.05,
                 f'{height}', ha='center', va='bottom', fontweight='bold', fontsize=14)

    ax4.axhline(y=1.0, color='gray', linestyle='--', alpha=0.7)
    ax4.text(1.5, 1.05, 'Línea de 1 gol', color='gray', fontsize=10)

    # Ajustes finales
    plt.tight_layout()
    plt.subplots_adjust(top=0.93)
    fig.text(0.5, 0.01, 'Análisis basado en modelo ELO | Datos previos al partido | Creado con Python', 
             ha='center', fontsize=10, style='italic')

    # Guardar figura principal
    plt.savefig('visualizations/analisis_completo.png', dpi=300, bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    plt.close()

def crear_visualizaciones_adicionales():
    """Crear visualizaciones adicionales ELO y Tilt"""
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    # Comparativa ELO
    elo_data = [87, 97]
    equipos_elo = ['Irlanda', 'Portugal']
    colors_elo = ['#169B62', '#C72C2C']

    bars_elo = ax1.bar(equipos_elo, elo_data, color=colors_elo, alpha=0.8)
    ax1.set_ylabel('Puntuación ELO', fontsize=12, fontweight='bold')
    ax1.set_title('COMPARATIVA DE RATING ELO', fontsize=16, fontweight='bold')
    ax1.set_ylim(0, 110)

    for bar in bars_elo:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + 1,
                 f'{height}', ha='center', va='bottom', fontweight='bold')

    # Gráfico de tilt
    tilt_data = [-19.1, -17.9]
    bars_tilt = ax2.bar(equipos_elo, tilt_data, color=colors_elo, alpha=0.8)
    ax2.set_ylabel('Tilt (%)', fontsize=12, fontweight='bold')
    ax2.set_title('COMPARATIVA DE TILT (Estilo de Juego)', fontsize=16, fontweight='bold')
    ax2.axhline(y=0, color='black', linewidth=0.8)

    for bar in bars_tilt:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                 f'{height}%', ha='center', va='bottom' if height < 0 else 'top', 
                 fontweight='bold')

    plt.tight_layout()
    plt.savefig('visualizations/elo_tilt_comparison.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()

if __name__ == "__main__":
    analisis_irlanda_portugal()
