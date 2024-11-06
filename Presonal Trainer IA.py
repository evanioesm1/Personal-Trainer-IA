def montar_treino(biotipo, periodizacao, tipo):
    treino = []
    
    # Regra 2: Periodização com base na quantidade de dias informados
    if periodizacao == 1:
        treino_periodizacao = ["Full Body"]
    elif periodizacao == 3:
        treino_periodizacao = ["A", "B", "C"]
    elif periodizacao == 5:
        treino_periodizacao = ["A", "B", "C", "D", "E"]
    else:
        return "Quantidade de dias inválida!"

    # Regra 3: Seleção de exercícios com base no tipo de treino
    if tipo == "Funcional":
        exercicios = {
            "Full Body": ["Agachamento", "Flexão", "Prancha", "Afundo", "Burpee"],
            "A": ["Agachamento", "Flexão", "Prancha"],
            "B": ["Afundo", "Remada com halteres", "Burpee"],
            "C": ["Levantamento terra", "Abdominal", "Pular corda"],
            "D": ["Flexão diamante", "Elevação lateral", "Mountain climbers"],
            "E": ["Dead bug", "Superman", "Corrida no lugar"]
        }
    elif tipo == "Maquinário":
        exercicios = {
            "Full Body": ["Supino", "Leg Press", "Pull Down", "Cadeira extensora", "Puxada alta"],
            "A": ["Supino", "Leg Press", "Pull Down"],
            "B": ["Cadeira extensora", "Cadeira flexora", "Puxada alta"],
            "C": ["Smith Machine Squat", "Hack Machine", "Voador"],
            "D": ["Crossover", "Extensora", "Pullover"],
            "E": ["Rosca scott", "Tríceps pulley", "Puxada alta"]
        }
    elif tipo == "Peso livre":
        exercicios = {
            "Full Body": ["Agachamento com barra", "Supino com halteres", "Remada curvada", "Levantamento terra", "Rosca direta"],
            "A": ["Agachamento com barra", "Supino com halteres", "Remada curvada"],
            "B": ["Levantamento terra", "Desenvolvimento com halteres", "Rosca direta"],
            "C": ["Afundo com halteres", "Flexão de braço", "Elevação lateral"],
            "D": ["Levantamento terra romeno", "Remada unilateral", "Tríceps francês"],
            "E": ["Elevação frontal", "Remada alta", "Puxada alta"]
        }
    elif tipo == "Cardio":
        exercicios = {
            "Full Body": ["Corrida", "Elíptico", "Pular corda", "Bike ergométrica", "Polichinelo"],
            "A": ["Corrida", "Elíptico", "Pular corda"],
            "B": ["Bike ergométrica", "Caminhada inclinada", "Polichinelo"],
            "C": ["Corrida intervalada", "Saltos no step", "Burpees"],
            "D": ["Natação", "Spinning", "Escalada indoor"],
            "E": ["Corrida longa distância", "Rope Skipping", "HIIT"]
        }
    elif tipo == "HIIT":
        exercicios = {
            "Full Body": ["Sprint", "Burpee", "Jump Squat", "Mountain climber", "High knees"],
            "A": ["Sprint", "Burpee", "Jump Squat"],
            "B": ["Mountain climber", "High knees", "Skater jumps"],
            "C": ["Battle ropes", "Kettlebell swings", "Box jumps"],
            "D": ["Plyo push-ups", "Bicycle crunches", "Tuck jumps"],
            "E": ["Sprint", "Jump lunges", "Plank jacks"]
        }
    else:
        return "Tipo de treino inválido!"

    # Montagem do treino com base na periodização e tipo de treino
    for dia in treino_periodizacao:
        treino.append({dia: exercicios[dia]})

    return treino

# Exemplo de uso:
biotipo = input("Informe o biotipo (Ectomorfo, Mesomorfo, Endomorfo): ")
dias_treino = int(input("Informe a quantidade de dias de treino (1, 3, 5): "))
tipo = input("Informe o tipo de treino (Funcional, Maquinário, Peso livre, Cardio, HIIT): ")

treino_ideal = montar_treino(biotipo, dias_treino, tipo)
print(treino_ideal)
