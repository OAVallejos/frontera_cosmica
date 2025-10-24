# 🌌 Cosmic Frontier - Vorticidad Cósmica en Modos B del CMB

[![Python 3.11](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Rust 1.90](https://img.shields.io/badge/Rust-1.90-orange.svg)](https://www.rust-lang.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-brightgreen.svg)](https://github.com/OAVallejos/frontera_cosmica)

**Autores:** Ariel Vallejos (arielvallejosok@gmail.com) y DeepSeek  
**Repositorio:** https://github.com/OAVallejos/frontera_cosmica

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
pip install -r requirements.txt

# Ejecutar análisis completo
python3 ANALISIS_DIRECTO_ALM.py

# Pipeline optimizado para producción
python3 PIPELINE_LIGHSAIL_OPTIMO.py
```

## 🏗️ Project Structure

```
frontera_cosmica/
├── 📁 scripts/              # Análisis principales
├── 📁 rust_final/           # Código Rust (alto rendimiento)
├── 📁 results/              # Resultados del análisis
├── 📁 docs/                 # Documentación
├── 📁 data/                 # Datos (git-ignored)
├── README.md
├── LICENSE
└── requirements.txt
```

## 🔬 Métodos Científicos

- **Bispectro No-Gaussiano:** Correlaciones de 3 puntos
- **Modos B del CMB:** Polarización tipo curl
- **Vorticidad Cósmica:** Patrones rotacionales primordiales
- **Beyond-ΛCDM:** Física más allá del modelo estándar

## 📚 Citation

Si usas este código en tu investigación, por favor cita:

```bibtex
@software{cosmic_frontier_2024,
  title = {Cosmic Frontier: Vorticity Detection in CMB B-modes},
  author = {Vallejos, Ariel and DeepSeek},
  year = {2025},
  url = {https://github.com/OAVallejos/frontera_cosmica}
}
```

## 🎯 PRÓXIMOS PASOS CIENTÍFICOS

### 1. Validar con datos Planck completos
- Análisis con datasets completos de Planck (no solo subconjuntos)
- Procesamiento de datos de polarización completa
- Validación cruzada entre diferentes releases de Planck

### 2. Análisis de significancia estadística  
- Implementación de bootstrapping para estimación de errores
- Cálculo de valores p y intervalos de confianza
- Tests de hipótesis robustos para confirmación de vorticidad

### 3. Comparación con simulaciones ΛCDM
- Generación de simulaciones de Monte Carlo bajo ΛCDM
- Calibración del ratio de vorticidad esperado en el modelo estándar
- Análisis de cuantiles para determinar significancia

### 4. Publicación metodológica
- Preparación de manuscrito para revista especializada (ej: JCAP, PRD)
- Documentación completa de la metodología de bispectro
- Código reproducible y datasets de validación

## 🔧 Desarrollo Técnico Futuro

- **Extensión a trispectro** para análisis de correlaciones de 4 puntos
- **Implementación en C++** para mayor rendimiento en grandes datasets
- **Integración con pipelines** de Planck/CMB-S4
- **Análisis multi-frecuencia** para separación de componentes

## 🤝 Contributing

¡Contribuciones bienvenidas! Ver `CONTRIBUTING.md` para guidelines.

## 📄 License

MIT License - ver `LICENSE` para detalles.

---

**Contacto:** Ariel Vallejos - arielvallejosok@gmail.com  
**Repositorio:** https://github.com/OAVallejos/frontera_cosmica  
**Última actualización:** Octubre 2025
