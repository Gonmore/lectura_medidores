from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import tarea_programada, tarea_periodica

scheduler = BackgroundScheduler()

def start():
	scheduler.add_job(tarea_programada, 'interval', minutes=15)
	scheduler.start()

def dia_de_juego(ids,inicio,fin):
    scheduler.add_job(tarea_periodica, 
                                'cron',
                                args=[ids], 
                                minute = "*/15",
                                start_date = inicio,
                                end_date = fin,
                                id="tarea_cron",
                                replace_existing=True)