from django_cron import CronJobBase, Schedule
from django.core.mail import send_mail

class MyCronJob(CronJobBase):
	RUN_EVERY_MINS = 5 # every 2 hours

	schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
	code = 'articles.my_cron_job' #a unique code

	def do(self):
		print ("mail is sending...")
		send_mail(
		    'Subject',
		    '<b>Message.</b>Checking the functionality of the cron',
		    '03akash97@gmail.com',
		    ['03akash97@gmail.com', '28rancho14@gmail.com'],
		)

