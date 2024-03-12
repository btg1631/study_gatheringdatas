from apscheduler.schedulers.background import BackgroundScheduler

from sample_function import message_print, job_print
if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(message_print, trigger='interval', seconds=2, coalesce=True, max_instances=1)
    scheduler.add_job(job_print, trigger='interval', seconds=2, coalesce=True, max_instances=1)

    scheduler.start()
    pass

    # 무한 루프
    while True:
        pass
