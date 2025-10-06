#!/usr/bin/env python3
"""
LIMPIEZA FOCALIZADA PARA AWS LIGHSAIL (2GB RAM, 2 vCPU)
Conserva solo lo esencial para análisis de vorticidad cósmica
"""

import os
import shutil

# ARCHIVOS ESENCIALES A CONSERVAR
ARCHIVOS_ESENCIALES = {
    # Análisis principal
    'BISPECTRO_PYTHON_FINAL.py',
    'CALIBRACION_KAI_RUST.py', 
    'PIPELINE_CALIBRADO_CORREGIDO.py',
    
    # Datos
    'datos_planck',
    'datos_sinteticos',
    'cosmic_frontier_truth',
    'resultados',
    'resultados_reales',
    
    # Rust core
    'rust_final',
    'cosmic_vorticity.so',
    
    # Scripts de utilidad
    'visualizar_firmas_vorticidad.py',
    'separar_lente_vorticidad.py',
    
    # Documentación
    'informeDatos.md',
    'informeOperativo.md',
    'RESUMEN_EJECUTIVO_FINAL.md'
}

# ARCHIVOS DEBUG QUE PODEMOS ELIMINAR
ARCHIVOS_DEBUG = [
    'DEBUG_ALGORITMO_BISPECTRO.py',
    'DEBUG_CALIBRACION_CRITICA.py', 
    'DEBUG_PROFUNDO_RUST.py',
    'DEBUG_RUST_BISPECTRO.py',
    'DEBUG_RUST_DIRECTO.py',
    'DEBUG_ULTRA_PROFUNDO.py',
    'DIAGNOSTICO_BUG_WIGNER.py',
    'DIAGNOSTICO_CALIBRACION.py',
    'DIAGNOSTICO_CEROS_BISPECTRO.py',
    'VERIFICACION_ENLACE.py',
    'VERIFICACION_EXTREMA_RUST.py',
    'VERIFICACION_FINAL.py',
    'VERIFICACION_INMEDIATA.py',
    'VERIFICACION_KAI_RUST.py',
    'VERIFICACION_MODULO_REAL.py',
    'VERIFICAR_CORRECCIONES.py',
    'verification_complete.py',
    'TEST_INDICES_CORRECTOS.py',
    'TEST_FINAL_CORREGIDO.py',
    'VALIDACION_CALIBRACION.py',
    'PRUEBA_DATOS_SINTETICOS.py'
]

# ARCHIVOS OBSOLETOS O DUPLICADOS
ARCHIVOS_OBSOLETOS = [
    'BISPECTRO_SIMPLIFICADO.py',
    'CALIBRACIÓN_CON_DATOS_REALES.py',  # Tiene caracteres especiales
    'CALIBRACION_CON_REFERENCIA.py',
    'INTEGRADOR_RUST.py',
    'PYO3_INTEGRACION_COMPLETA.py',
    'PYO3_INTEGRACION_DIRECTA.py',
    'SOLUCION_DATOS_REALES_a_lm.py',
    'SOLUCION_DATOS_REALES.py',
    'ENERAR_DATOS_FORMATO_CORRECTO.py',  # Probable typo
    'encontrar_datos_reales.py',
    'analizar_datos_wmap_reales.py',
    'OPTIMIZACION_EXTREMA.py',
    'purga_focalizada.py',
    'purga.py',
    'analisis_python',  # Directorio
    'src_rust',  # Duplicado de rust_final
    'logs',  # Podemos regenerar
    '__pycache__',
    'reporte_calibracion_simple.json',
    'test_pipeline_rust_bispectro.csv',
    'test_pipeline_rust.json',
    'datos_estables_frontera.py'
]

def limpiar_archivos():
    """Elimina archivos no esenciales de forma segura"""
    
    print("🧹 INICIANDO LIMPIEZA FOCALIZADA")
    print("=" * 50)
    
    # Primero, hacer backup de los esenciales
    print("📦 Verificando archivos esenciales...")
    for archivo in ARCHIVOS_ESENCIALES:
        if os.path.exists(archivo):
            print(f"   ✅ Conservando: {archivo}")
        else:
            print(f"   ⚠️  No encontrado: {archivo}")
    
    # Eliminar archivos de debug
    print("\n🗑️  Eliminando archivos de debug...")
    for archivo in ARCHIVOS_DEBUG:
        if os.path.exists(archivo):
            try:
                if os.path.isdir(archivo):
                    shutil.rmtree(archivo)
                else:
                    os.remove(archivo)
                print(f"   ✅ Eliminado: {archivo}")
            except Exception as e:
                print(f"   ❌ Error eliminando {archivo}: {e}")
    
    # Eliminar archivos obsoletos
    print("\n🗑️  Eliminando archivos obsoletos...")
    for archivo in ARCHIVOS_OBSOLETOS:
        if os.path.exists(archivo):
            try:
                if os.path.isdir(archivo):
                    shutil.rmtree(archivo)
                else:
                    os.remove(archivo)
                print(f"   ✅ Eliminado: {archivo}")
            except Exception as e:
                print(f"   ❌ Error eliminando {archivo}: {e}")
    
    # Limpiar logs si existen
    if os.path.exists('logs'):
        try:
            shutil.rmtree('logs')
            print("   ✅ Eliminado: logs/")
        except Exception as e:
            print(f"   ❌ Error eliminando logs: {e}")

def verificar_espacio():
    """Verifica el espacio liberado"""
    print("\n💾 VERIFICACIÓN DE ESPACIO:")
    
    # Calcular espacio actual
    total_size = 0
    for dirpath, dirnames, filenames in os.walk('.'):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    
    print(f"   Espacio total utilizado: {total_size / (1024**3):.2f} GB")
    
    # Listar archivos restantes
    print("\n📁 ESTRUCTURA FINAL:")
    for item in sorted(os.listdir('.')):
        if item.startswith('.'):
            continue
        size = os.path.getsize(item) if os.path.isfile(item) else 0
        print(f"   {item}/" if os.path.isdir(item) else f"   {item}")

if __name__ == "__main__":
    print("🚀 OPTIMIZACIÓN PARA AWS LIGHSAIL (2GB RAM, 2 vCPU)")
    print("   Conservando solo el núcleo de análisis de vorticidad\n")
    
    # Confirmación de seguridad
    respuesta = input("¿Continuar con la limpieza? (s/N): ")
    if respuesta.lower() in ['s', 'si', 'y', 'yes']:
        limpiar_archivos()
        verificar_espacio()
        print("\n🎉 LIMPIEZA COMPLETADA")
    else:
        print("❌ Limpieza cancelada")
