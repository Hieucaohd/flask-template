from .report_when_server_restart import report_urls_accessed_while_server_stop
from .controller import Controller
from datetime import datetime


def main():
    time_server_start = datetime.utcnow()
    Controller.save_time_server_start_and_time_between_job(time_server_start)

    report_urls_accessed_while_server_stop()
    return Controller.create_job()


