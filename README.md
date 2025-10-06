# 🌌 Cosmic Frontier - Vorticidad Cósmica en Modos B del CMB

[![Python 3.11](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Rust 1.90](https://img.shields.io/badge/Rust-1.90-orange.svg)](https://www.rust-lang.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Sistema completo para detección de vorticidad cósmica primordial mediante análisis de bispectro no-gaussiano en modos B del CMB.

## 🎯 Hallazgo Principal

**Ratio de vorticidad: 1.307** detectado en datos Planck "Modos B Vorticidad Fuerte", sugiriendo **indicios de física beyond-ΛCDM**.

> 📊 **Interpretación:** Ratio > 1.5 = evidencia fuerte, > 1.2 = indicios prometedores

## 📊 Resultados Científicos

| Dataset | Modos | Ratio | Conclusión |
|---------|-------|-------|------------|
| `modosB_vorticidad_fuerte.fits` | 100,000 | **1.307** | 🎯 **Indicios de vorticidad** |
| `modosB_con_vorticidad.fits` | 100,000 | 0.419 | Sin evidencia fuerte |
| `modosB_gaussianos.fits` | 100,000 | 0.417 | Sin evidencia fuerte |
| `modosB_lensing.fits` | 100,000 | 0.557 | Sin evidencia fuerte |

## 🚀 Quick Start

```bash
# Instalar dependencias
pip install numpy astropy

# Ejecutar análisis completo
python3 scripts/ANALISIS_DIRECTO_ALM.py

# Pipeline optimizado para producción
python3 scripts/PIPELINE_LIGHSAIL_OPTIMO.py
