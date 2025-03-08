#Importamos la libreria "experta"
from experta import *

#Hechos sobre el usuario y su experiencia en senderismo
class Senderismo(Fact):
    """Hechos sobre el usuario y su experiencia"""
    pass

#Determinamos las reglas, variables de entrada, intermedias
class SistemaExpertoSenderismo(KnowledgeEngine):
    
    #Determinar el nivel de experiencia en Senderismo
    #Variables de Entrada: V1, V2, V3, V4
    #Variables intermedias: V10
    #Variables de Salida: V14

    # Regla 1: Si V1 = No, entonces V10 = Principiante.
    @Rule(Senderismo(ha_realizado_senderismo=False))
    def nivel_principiante_sin_experiencia(self):
        self.declare(Senderismo(nivel_experiencia="Principiante"))
    
    # Regla 2: Si V1 = Si y V2 = Ocasionalmente, entonces V10 = Principiante.
    @Rule(Senderismo(ha_realizado_senderismo=True, frecuencia="Ocasionalmente"))
    def nivel_principiante_ocasional(self):
        self.declare(Senderismo(nivel_experiencia="Principiante"))

    # Regla 3: Si V1 = Si y V2 = Regularmente, entonces V10 = Intermedio.
    @Rule(Senderismo(ha_realizado_senderismo=True, frecuencia="Regularmente"))
    def nivel_intermedio_regular(self):
        self.declare(Senderismo(nivel_experiencia="Intermedio"))

    # Regla 4: Si V1 = Si y V2 = Frecuentemente, entonces V10 = Avanzado.
    @Rule(Senderismo(ha_realizado_senderismo=True, frecuencia="Frecuentemente"))
    def nivel_avanzado_frecuente(self):
        self.declare(Senderismo(nivel_experiencia="Avanzado"))

    # Regla 5: Si V3 = Si y V4 = Si, entonces V10 = Intermedio.
    @Rule(Senderismo(ha_recorrido_distancia=True, terrenos_accidentados=True))
    def nivel_intermedio_por_experiencia(self):
        self.declare(Senderismo(nivel_experiencia="Intermedio"))
    
    # Regla 6: Si V5 = Si y V6 = Si, entonces V13 = Medio.
    @Rule(Senderismo(conoce_orientacion=True, sabe_usar_brujula=True))
    def nivel_seguridad_por_orientacion(self):
        self.declare(Senderismo(nivel_seguridad="Medio"))
    
    # Regla 7: Si V7 = Si y V9 = Si, entonces V13 = Alto.
    @Rule(Senderismo(experiencia_clima_adverso=True, conoce_seguridad=True))
    def nivel_seguridad_por_experiencia_completa(self):
        self.declare(Senderismo(nivel_seguridad="Alto"))
    
    # Regla 8: Si V8 = No, entonces V11 = Basico.
    @Rule(Senderismo(tiene_equipo_basico=False))
    def tipo_equipo_basico(self):
        self.declare(Senderismo(tipo_equipo="Basico"))
    
    # Regla 9: Si V8 = Si y V10 = Intermedio, entonces V11 = Intermedio.
    @Rule(Senderismo(tiene_equipo_basico=True, nivel_experiencia="Intermedio"))
    def tipo_equipo_intermedio(self):
        self.declare(Senderismo(tipo_equipo="Intermedio"))
    
    # Regla 10: Si V8 = Si y V10 = Avanzado, entonces V11 = Avanzado.
    @Rule(Senderismo(tiene_equipo_basico=True, nivel_experiencia="Avanzado"))
    def tipo_equipo_avanzado(self):
        self.declare(Senderismo(tipo_equipo="Avanzado"))
    
    # Regla 11: Si V10 = Principiante, entonces V12 = Facil.
    @Rule(Senderismo(nivel_experiencia="Principiante"))
    def dificultad_facil(self):
        self.declare(Senderismo(dificultad_rutas="Facil"))
    
    # Regla 12: Si V10 = Intermedio, entonces V12 = Moderada.
    @Rule(Senderismo(nivel_experiencia="Intermedio"))
    def dificultad_moderada(self):
        self.declare(Senderismo(dificultad_rutas="Moderada"))
    
    # Regla 13: Si V10 = Avanzado, entonces V12 = Dificil.
    @Rule(Senderismo(nivel_experiencia="Avanzado"))
    def dificultad_dificil(self):
        self.declare(Senderismo(dificultad_rutas="Dificil"))
    
    # Regla 14: Si V12 = Facil, entonces V14 = "Senderos cortos y bien senalizados".
    @Rule(Senderismo(dificultad_rutas="Facil"))
    def recomendar_rutas_principiante(self):
        print("Recomendacion: Senderos cortos y bien senalizados.")
    
    # Regla 15: Si V12 = Moderada, entonces V14 = "Senderos con ascensos y terreno irregular".
    @Rule(Senderismo(dificultad_rutas="Moderada"))
    def recomendar_rutas_intermedio(self):
        print("Recomendacion: Senderos con ascensos y terreno irregular.")
    
    # Regla 16: Si V12 = Dificil, entonces V14 = "Rutas de alta montana y travesias largas".
    @Rule(Senderismo(dificultad_rutas="Dificil"))
    def recomendar_rutas_avanzado(self):
        print("Recomendacion: Rutas de alta montana y travesias largas.")
    
    # Regla 17: Si V11 = Basico, entonces V15 = "Ropa comoda, calzado basico, agua y snacks".
    @Rule(Senderismo(tipo_equipo="Basico"))
    def recomendar_equipo_basico(self):
        print("Recomendacion de equipo: Ropa comoda, calzado basico, agua y snacks.")
    
    # Regla 18: Si V11 = Intermedio, entonces V15 = "Equipo adicional como bastones y mochila con suministros".
    @Rule(Senderismo(tipo_equipo="Intermedio"))
    def recomendar_equipo_intermedio(self):
        print("Recomendacion de equipo: Equipo adicional como bastones y mochila con suministros.")
    
    # Regla 19: Si V11 = Avanzado, entonces V15 = "Equipo tecnico, brujula/GPS y planificacion avanzada".
    @Rule(Senderismo(tipo_equipo="Avanzado"))
    def recomendar_equipo_avanzado(self):
        print("Recomendacion de equipo: Equipo tecnico, brujula/GPS y planificacion avanzada.")
    
    # Regla 20: Si V13 = Bajo, entonces V16 = "Aprender normas basicas de seguridad".
    @Rule(Senderismo(nivel_seguridad="Bajo"))
    def medidas_seguridad_bajo(self):
        print("Medidas de seguridad recomendadas: Aprender normas basicas de seguridad.")
    
    # Regla 21: Si V13 = Medio, entonces V16 = "Llevar botiquin y conocer primeros auxilios".
    @Rule(Senderismo(nivel_seguridad="Medio"))
    def medidas_seguridad_medio(self):
        print("Medidas de seguridad recomendadas: Llevar botiquin y conocer primeros auxilios.")
    
    # Regla 22: Si V13 = Alto, entonces V16 = "Tener planes de emergencia y comunicacion".
    @Rule(Senderismo(nivel_seguridad="Alto"))
    def medidas_seguridad_alto(self):
        print("Medidas de seguridad recomendadas: Tener planes de emergencia y comunicacion.")
    
    # Regla por defecto para el nivel de seguridad bajo si no se cumple otra condicion
    @Rule(~Senderismo(nivel_seguridad=W()))
    def nivel_seguridad_bajo_default(self):
        self.declare(Senderismo(nivel_seguridad="Bajo"))

if __name__ == "__main__":
    
    #Inicializar el sistema experto 
    sistema = SistemaExpertoSenderismo()
    sistema.reset()

    print("\n" + "="*60)
    print(" BIENVENIDO AL SISTEMA EXPERTO DE SENDERISMO ")
    print("="*60)
    print("Este sistema te proporcionara recomendaciones personalizadas")
    print("para rutas de senderismo, equipo necesario y medidas de seguridad")
    print("basado en tu nivel de experiencia.")
    print("="*60 + "\n")

    # Validar entrada para experiencia en senderismo (V1)
    while True:
        ha_realizado = input("Has realizado senderismo anteriormente? (Si/No): ").lower()
        if ha_realizado in ["si", "s", "yes", "y"]:
            ha_realizado_senderismo = True
            break
        elif ha_realizado in ["no", "n"]:
            ha_realizado_senderismo = False
            frecuencia = None
            break
        else:
            print("Por favor, responda 'Si' o 'No'.")

    # Preguntar frecuencia solo si ha hecho senderismo antes (V2)
    frecuencia = None
    if ha_realizado_senderismo:
        while True:
            print("\nIndica con que frecuencia realizas senderismo:")
            print("1. Ocasionalmente (pocas veces al ano)")
            print("2. Regularmente (mensualmente)")
            print("3. Frecuentemente (semanalmente)")

            opcion = input("Selecciona una opcion (1-3): ")

            if opcion == "1":
                frecuencia = "Ocasionalmente"
                break
            elif opcion == "2":
                frecuencia = "Regularmente"
                break
            elif opcion == "3":
                frecuencia = "Frecuentemente"
                break
            else:
                print("Por favor, selecciona una opcion valida (1-3).")

    # Preguntar si ha realizado senderos mas de 10km (V3)
    ha_recorrido_distancia = False
    while True:
        distancia = input("\nHa realizado senderos de mas de 10km? (si/no): ").lower()
        if distancia in ["si", "s", "yes", "y"]:
            ha_recorrido_distancia = True
            break
        elif distancia in ["no", "n"]:
            ha_recorrido_distancia = False
            break
        else:
            print("Por favor, responde 'si' o 'no'.")

    # Preguntar si ha recorrido terrenos accidentados o montanosos (V4)
    terrenos_accidentados = False
    while True:
        terrenos = input("\nHa caminado en terrenos accidentados o montanosos? (si/no): ").lower()
        if terrenos in ["si", "s", "yes", "y"]:
            terrenos_accidentados = True
            break
        elif terrenos in ["no", "n"]:
            terrenos_accidentados = False
            break
        else:
            print("Por favor, responde 'si' o 'no'.")

    # Preguntar si cuenta con experiencia sobre orientacion y uso de mapas (V5)
    conoce_orientacion = False
    while True:
        experiencia = input("\nCuenta con conocimientos sobre orientacion y uso de mapas? (si/no): ").lower()
        if experiencia in ["si", "s", "yes", "y"]:
            conoce_orientacion = True
            break
        elif experiencia in ["no", "n"]:
            conoce_orientacion = False
            break
        else: 
            print("Por favor, responde 'si' o 'no'.")

    # Preguntar si sabe utilizar una brujula o GPS (V6)
    sabe_usar_brujula = False
    while True:
        uso = input("\nSabe utilizar una brujula o GPS? (si/no): ").lower()
        if uso in ["si", "s", "yes", "y"]:
            sabe_usar_brujula = True
            break
        elif uso in ["no", "n"]:
            sabe_usar_brujula = False
            break
        else:
            print("Por favor, responde 'si' o 'no'.")

    # Preguntar si ha realizado senderismo en condiciones climaticas adversas (V7)
    experiencia_clima_adverso = False
    while True:
        clima = input("\nHa realizado senderismo en condiciones climaticas adversas? (si/no): ").lower()
        if clima in ["si", "s", "yes", "y"]:
            experiencia_clima_adverso = True
            break
        elif clima in ["no", "n"]:
            experiencia_clima_adverso = False
            break
        else:
            print("Por favor, responde 'si' o 'no'.")

    # Preguntar si cuenta con equipo basico para senderismo (V8)
    tiene_equipo_basico = False
    while True:
        equipo = input("\nCuenta con el equipo basico para senderismo? (si/no): ").lower()
        if equipo in ["si", "s", "yes", "y"]:
            tiene_equipo_basico = True
            break
        elif equipo in ["no", "n"]:
            tiene_equipo_basico = False
            break
        else:
            print("Por favor, responde 'si' o 'no'.")

    # Validar conocimiento de seguridad y primeros auxilios (V9)
    conoce_seguridad = False
    while True:
        conoce = input("\nConoce las normas de seguridad y primeros auxilios en senderismo? (si/no): ").lower()
        if conoce in ["si", "s", "yes", "y"]:
            conoce_seguridad = True
            break
        elif conoce in ["no", "n"]:
            conoce_seguridad = False
            break
        else:
            print("Por favor, responde 'si' o 'no'.")
    
    print("\nAnalizando tu perfil... ")
    print("-"*60 + "\n")

    # Declarar los hechos basados en la entrada del usuario
    sistema.declare(Senderismo(
        ha_realizado_senderismo=ha_realizado_senderismo,
        frecuencia=frecuencia,
        ha_recorrido_distancia=ha_recorrido_distancia,
        terrenos_accidentados=terrenos_accidentados,
        conoce_orientacion=conoce_orientacion,
        sabe_usar_brujula=sabe_usar_brujula,
        experiencia_clima_adverso=experiencia_clima_adverso,
        tiene_equipo_basico=tiene_equipo_basico,
        conoce_seguridad=conoce_seguridad
    ))

    # Ejecutar el sistema experto
    sistema.run()

    print("\n" + "="*60)
    print("Gracias por utilizar nuestro sistema experto de senderismo!")
    print("Disfruta de tus aventuras de forma segura!")
