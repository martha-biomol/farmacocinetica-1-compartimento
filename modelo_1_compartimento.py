#!/usr/bin/env python3
"""Modelo farmacocinético de un compartimento, bolo IV (proyecto de práctica).

Después de un bolo intravenoso, en el modelo de un compartimento la
concentración plasmática cae de forma monoexponencial:

    C(t) = (Dosis / Vd) * exp(-k * t),   con k = CL / Vd

- Dosis: cantidad administrada (mg)
- Vd: volumen de distribución (L)
- CL: aclaramiento (L/h)
- k: constante de eliminación (1/h)
- t1/2 = ln(2) / k : vida media
- AUC = Dosis / CL : área bajo la curva (exposición total)

Uso:
    python3 modelo_1_compartimento.py

Genera la gráfica `concentracion_tiempo.png`.
"""

import numpy as np
import matplotlib.pyplot as plt

# Parámetros del ejemplo (fármaco hipotético)
DOSIS_MG = 100.0   # mg
VD_L = 50.0        # L
CL_L_H = 5.0       # L/h

k = CL_L_H / VD_L              # constante de eliminación, 1/h
c0 = DOSIS_MG / VD_L           # concentración inicial, mg/L
vida_media = np.log(2) / k     # horas
auc = DOSIS_MG / CL_L_H        # mg*h/L

t = np.linspace(0, 48, 200)    # 0 a 48 h
c = c0 * np.exp(-k * t)

print("Modelo de un compartimento, bolo IV")
print(f"Dosis: {DOSIS_MG:.0f} mg | Vd: {VD_L:.0f} L | CL: {CL_L_H:.0f} L/h")
print(f"k = {k:.3f} /h")
print(f"C0 = {c0:.2f} mg/L")
print(f"Vida media (t1/2) = {vida_media:.2f} h")
print(f"AUC = {auc:.1f} mg*h/L")
print()
print("Concentración en tiempos clave:")
for tiempo in [0, 6, 12, 24, 48]:
    concentracion = c0 * np.exp(-k * tiempo)
    print(f"  t = {tiempo:2d} h -> C = {concentracion:.3f} mg/L")

plt.figure()
plt.plot(t, c)
plt.axhline(0, color="gray", linewidth=0.8)
plt.xlabel("Tiempo (h)")
plt.ylabel("Concentración (mg/L)")
plt.title("Modelo de un compartimento, bolo IV\nDosis 100 mg, Vd 50 L, CL 5 L/h")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("concentracion_tiempo.png", dpi=150)
print()
print("Gráfica guardada en concentracion_tiempo.png")
