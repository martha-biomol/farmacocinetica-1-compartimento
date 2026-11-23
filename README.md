# Farmacocinética: modelo de un compartimento

Modelo farmacocinético de un compartimento para un bolo intravenoso,
en Python (NumPy + Matplotlib). Proyecto de práctica para mi portafolio,
camino al modelado PopPK/PD.

## El modelo

Después de un bolo IV, la concentración cae de forma monoexponencial:

```
C(t) = (Dosis / Vd) * exp(-k * t),  con k = CL / Vd
```

- **Dosis:** cantidad administrada (mg)
- **Vd:** volumen de distribución (L)
- **CL:** aclaramiento (L/h)
- **t1/2 = ln(2)/k:** vida media
- **AUC = Dosis/CL:** exposición total

## Cómo correrlo

```bash
python3 modelo_1_compartimento.py
```

Genera la gráfica `concentracion_tiempo.png` y muestra en consola la
vida media, el AUC y la concentración a 0, 6, 12, 24 y 48 horas.

## Ejemplo (fármaco hipotético: 100 mg, Vd 50 L, CL 5 L/h)

- k = 0.100 /h
- C0 = 2.00 mg/L
- Vida media ≈ 6.93 h
- AUC = 20.0 mg·h/L

## Qué sigue

- Modelo de dos compartimentos
- Administración oral con absorción de primer orden
- Simular varios pacientes con variabilidad (primer paso a PopPK)
