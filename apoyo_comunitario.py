# PRO-12 — Fundación Apoyo Comunitario
# Archivo inicial de prueba para validar el entorno y la lógica base FIFO.

from collections import deque
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Voluntario:
    nombre: str
    habilidad: str
    acreditado: bool = True


class GestorEmergenciaFIFO:
    """Gestiona cupos de una emergencia respetando el orden de llegada (FIFO)."""

    def __init__(self, nombre_emergencia: str, cupos_disponibles: int):
        self.nombre_emergencia = nombre_emergencia
        self.cupos_disponibles = cupos_disponibles
        self.asignados: list[Voluntario] = []
        self.lista_espera: deque[Voluntario] = deque()

    def postular(self, voluntario: Voluntario) -> str:
        if not voluntario.acreditado:
            return f"[RECHAZADO] {voluntario.nombre} no está acreditado."

        if len(self.asignados) < self.cupos_disponibles:
            self.asignados.append(voluntario)
            return f"[ASIGNADO] {voluntario.nombre} tomó un cupo en '{self.nombre_emergencia}'."

        self.lista_espera.append(voluntario)
        return f"[EN ESPERA FIFO] {voluntario.nombre} quedó en fila (posición {len(self.lista_espera)})."

    def mostrar_estado(self) -> None:
        print(f"\n=== Emergencia: {self.nombre_emergencia} ===")
        print(f"Cupos: {len(self.asignados)}/{self.cupos_disponibles}")
        print("Asignados:", [v.nombre for v in self.asignados])
        print("Lista de espera (FIFO):", [v.nombre for v in self.lista_espera])


def main() -> None:
    fecha_inicio = datetime.now().strftime("%Y-%m-%d %H:%M")
    print(f"Sistema PRO-12 — Fundación Apoyo Comunitario | Inicio: {fecha_inicio}")

    operativo = GestorEmergenciaFIFO(
        nombre_emergencia="Apoyo logístico y albergue temporal",
        cupos_disponibles=2,
    )

    voluntarios = [
        Voluntario("Camila Rojas", "Primeros auxilios", acreditado=True),
        Voluntario("Diego Soto", "Logística", acreditado=True),
        Voluntario("Valentina Paz", "Apoyo psicosocial", acreditado=True),
        Voluntario("Matías Vera", "Transporte", acreditado=False),
    ]

    for v in voluntarios:
        print(operativo.postular(v))

    operativo.mostrar_estado()


if __name__ == "__main__":
    main()
