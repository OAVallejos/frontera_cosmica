#!/usr/bin/env python3
"""
PIPELINE OPTIMIZADO PARA AWS LIGHSAIL (2GB RAM, 2 vCPU)
"""

import numpy as np
import time
import psutil
import gc

class OptimizadorMemoria:
    @staticmethod
    def estado_memoria():
        mem = psutil.virtual_memory()
        return {
            'total_GB': mem.total / (1024**3),
            'disponible_GB': mem.available / (1024**3),
            'porcentaje_usado': mem.percent
        }
    
    @staticmethod
    def liberar_memoria():
        gc.collect()

def generar_datos_eficiente(l_max=15):
    """Genera datos optimizados para baja memoria"""
    mem_ini = OptimizadorMemoria.estado_memoria()
    
    total_modos = sum(2*l + 1 for l in range(l_max + 1))
    modos_b = np.zeros(total_modos, dtype=np.float32)
    
    idx = 0
    for l in range(l_max + 1):
        for m in range(-l, l + 1):
            if l >= 2:
                if l % 3 == 0 and m == 0:
                    modos_b[idx] = 0.7
                elif l % 3 == 1 and abs(m) == 1:
                    modos_b[idx] = 0.5
                else:
                    modos_b[idx] = np.float32(np.random.normal(0, 0.1))  # CORREGIDO
            idx += 1
    
    mem_fin = OptimizadorMemoria.estado_memoria()
    print(f"📊 Datos generados: {len(modos_b)} modos, Memoria: {mem_fin['disponible_GB']:.1f}GB libre")
    
    return modos_b.tolist()

def analisis_vorticidad_eficiente():
    """Análisis principal optimizado"""
    
    print("🌌 ANÁLISIS DE VORTICIDAD - MODO EFICIENTE")
    print("=" * 50)
    print(f"💻 Recursos: 2 vCPU, 2GB RAM")
    print(f"📊 Estado memoria: {OptimizadorMemoria.estado_memoria()}")
    
    l_max = 12
    batch_size = 5

    configs_prioritarias = [
        (2, 3, 4), (3, 4, 5), (4, 5, 6),
        (2, 4, 5), (3, 5, 6), (4, 6, 7),
        (2, 2, 2), (3, 3, 3), (4, 4, 4)
    ]
    
    print(f"🔺 Analizando {len(configs_prioritarias)} configuraciones...")
    
    try:
        from cosmic_vorticity import calcular_bispectro_triangular
        
        modos_b = generar_datos_eficiente(l_max)
        OptimizadorMemoria.liberar_memoria()
        
        resultados_totales = []
        
        for i in range(0, len(configs_prioritarias), batch_size):
            batch = configs_prioritarias[i:i + batch_size]
            
            print(f"🔄 Procesando lote {i//batch_size + 1}/{(len(configs_prioritarias)-1)//batch_size + 1}")
            
            start_time = time.time()
            resultados_batch = calcular_bispectro_triangular(modos_b, l_max, batch)
            elapsed = time.time() - start_time
            
            resultados_totales.extend(resultados_batch)
            
            print(f"   ⏱️  Tiempo lote: {elapsed:.2f}s")
            print(f"   🧠 Memoria libre: {OptimizadorMemoria.estado_memoria()['disponible_GB']:.1f}GB")
            
            OptimizadorMemoria.liberar_memoria()
        
        print("\n📊 RESULTADOS OPTIMIZADOS:")
        print("-" * 40)
        
        for (l1, l2, l3), b in zip(configs_prioritarias, resultados_totales):
            tipo = "ESCALENO" if l1 != l2 and l2 != l3 and l1 != l3 else "EQUILATERO"
            print(f"B({l1},{l2},{l3}) = {b:10.6f}  [{tipo}]")
        
        escalenos = [b for (l1,l2,l3), b in zip(configs_prioritarias, resultados_totales) 
                    if l1 != l2 and l2 != l3 and l1 != l3]
        equilateros = [b for (l1,l2,l3), b in zip(configs_prioritarias, resultados_totales) 
                      if l1 == l2 == l3]
        
        if escalenos and equilateros:
            ratio = np.mean(np.abs(escalenos)) / np.mean(np.abs(equilateros))
            print(f"\n📈 Ratio escaleno/equilátero: {ratio:.3f}")
            
            if ratio > 1.2:
                print("🎯 INDICIO DE VORTICIDAD: Patrón escaleno dominante")
            else:
                print("📉 Sin evidencia fuerte de vorticidad")
        
        return resultados_totales
        
    except ImportError:
        print("❌ Módulo Rust no encontrado. Compila primero:")
        print("   cd rust_final && cargo build --release")
        return None

if __name__ == "__main__":
    resultados = analisis_vorticidad_eficiente()
    
    if resultados:
        print(f"\n✅ Análisis completado. Memoria final: {OptimizadorMemoria.estado_memoria()['disponible_GB']:.1f}GB libre")
