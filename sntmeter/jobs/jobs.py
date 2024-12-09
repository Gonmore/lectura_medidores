from .. import lectura

def tarea_programada():
    se_lee = bool()
    se_lee=lectura.lectura_global()
    print('Ejecutando tarea', se_lee)

def tarea_periodica(ids):
    lectura.simple_de_medidor(ids)
    print('tarea periodica')