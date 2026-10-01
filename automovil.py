class Automovil:
    def __init__(self, marca, modelo, velocidad_max, nivel_combustible, año_fabricacion):
        self.marca = marca
        self.modelo = modelo
        self._velocidad_max = velocidad_max
        self._nivel_combustible = nivel_combustible
        self._año_fabricacion = año_fabricacion

    @property
    def año_fabricacion(self):
        return self._año_fabricacion

    @año_fabricacion.setter
    def año_fabricacion(self, valor):
        if valor < 1886 or valor > 2026:
            raise ValueError("El año debe estar entre 1886 y 2026")
        self._año_fabricacion = valor

    @property
    def nivel_combustible(self):
        return self._nivel_combustible

    @nivel_combustible.setter
    def nivel_combustible(self, valor):
        if valor < 0.0 or valor > 100.0:
            raise ValueError("El nivel de combustible debe estar entre 0.0 y 100.0")
        self._nivel_combustible = valor

    @property
    def velocidad_max(self):
        return self._velocidad_max

    @velocidad_max.setter
    def velocidad_max(self, valor):
        if valor <= 0:
            raise ValueError("La velocidad maxima debe ser mayor a 0")
        self._velocidad_max = valor

    def tiempo_llegada(self, distancia_km):
        return distancia_km / self._velocidad_max

    def __str__(self):
        return (f"{self.marca} {self.modelo} ({self._año_fabricacion}) - "
                f"Vel. max: {self._velocidad_max} km/h - "
                f"Combustible: {self._nivel_combustible}%")


if __name__ == "__main__":
    auto = Automovil("Toyota", "Corolla", 180, 75.5, 2020)
    print(auto)
    print(f"Tiempo de llegada a 360 km: {auto.tiempo_llegada(360):.2f} horas")

    try:
        auto.año_fabricacion = 1800
    except ValueError as e:
        print(f"Error capturado: {e}")