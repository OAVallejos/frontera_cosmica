#!/usr/bin/env python3
import numpy as np
from astropy.io import fits

print("🎯 SEPARANDO LENTE GRAVITACIONAL DE SEÑAL VORTICIAL")
print("=" * 55)

def separar_componentes():
    # Cargar datos
    B_observado = fits.open('datos_planck/vorticidad/modosB_con_vorticidad.fits')[1].data
    E_modes = fits.open('datos_planck/reales/cmb_smica.fits')[1].data  # Asumiendo que existe
    
    print(f"📊 Datos cargados: B_observado {B_observado.shape}, E_modes {E_modes.shape}")
    
    # 1. ESTIMAR COMPONENTE DE LENTE (Gaussiano)
    # Usar estimador cuadrático estándar: B_lente ≈ L[E_modes]
    B_lente_estimado = estimar_lente_desde_E(E_modes)
    
    # 2. EXTRACTAR SEÑAL PRIMORDIAL
    B_primordial = B_observado - B_lente_estimado
    
    # 3. BUSCAR BISPECTRO NO-GAUSSIANO EN SEÑAL PRIMORDIAL
    f_NL_vorticial = calcular_bispectro_triangular(B_primordial)
    
    print(f"🎯 RESULTADOS SEPARACIÓN:")
    print(f"   B_lente estimado: {np.std(B_lente_estimado):.2e}")
    print(f"   B_primordial residual: {np.std(B_primordial):.2e}")
    print(f"   f_NL vorticial: {f_NL_vorticial:.1f}")
    
    return B_primordial, f_NL_vorticial

def estimar_lente_desde_E(E_modes):
    """Estimación simplificada del componente de lente"""
    # En la práctica esto usaría un estimador cuadrático óptimo
    return 0.1 * E_modes  # Aproximación simple

def calcular_bispectro_triangular(B_map):
    """Cálculo simplificado de bispectro para triángulos irregulares"""
    # Buscar configuraciones triangulares específicas
    n_pix = len(B_map)
    indices = np.random.choice(n_pix, 1000, replace=False)  # Muestra para velocidad
    
    # Calcular productos triple para configuración irregular
    bispectrum_vals = []
    for i in range(0, len(indices)-2, 3):
        triple_product = B_map[indices[i]] * B_map[indices[i+1]] * B_map[indices[i+2]]
        bispectrum_vals.append(triple_product)
    
    f_NL = np.mean(bispectrum_vals) / (np.std(B_map)**3) if np.std(B_map) > 0 else 0
    return f_NL

if __name__ == "__main__":
    B_primordial, f_NL = separar_componentes()
    
    if abs(f_NL) > 5:
        print(f"🚨 ¡POSIBLE DETECCIÓN! f_NL = {f_NL:.1f}")
    else:
        print(f"📊 Señal primordial compatible con ruido: f_NL = {f_NL:.1f}")
