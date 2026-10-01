import math


class Planeta:
    def __init__(self, nombre, masa, radio, distancia_al_sol, tiene_vida=False):
        self.nombre = nombre
        self.masa = masa
        self.radio = radio
        self.distancia_al_sol = distancia_al_sol
        self.tiene_vida = tiene_vida

    def calcular_densidad(self):
        volumen = (4 / 3) * math.pi * (self.radio ** 3)
        return self.masa / volumen

    def es_planeta_exterior(self):
        return self.distancia_al_sol > 5.2

    def __str__(self):
        densidad = self.calcular_densidad()
        tipo = "exterior" if self.es_planeta_exterior() else "interior"
        return f"{self.nombre} - Densidad: {densidad:.2f} kg/m3 - Planeta {tipo}"


if __name__ == "__main__":
    tierra = Planeta("Tierra", 5.97e24, 6.371e6, 1.0, True)
    jupiter = Planeta("Jupiter", 1.898e27, 6.9911e7, 5.2, False)

    print(tierra)
    print(jupiter)

    # Prueba adicional de instancia
marte = Planeta("Marte", 6.39e23, 3.3895e6, 1.52, False)
print(marte)