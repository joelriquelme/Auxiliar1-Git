class Usuario:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.tareas = []

    def agregarTarea(self, tarea):
        self.tareas.append(tarea)
    def listarTareas(self):
        for tarea in self.tareas:
            if tarea.estaLista():
<<<<<<< HEAD
                print(f"La tarea {tarea.obtenerNombre()} está lista")
                print(f"La tarea {tarea.obtenerNombre()} no está lista")
=======
                print(f"[X] {tarea.obtenerNombre()}" )
>>>>>>> 49a2dae75becf423b0bb054c4326f50e48f95ead
