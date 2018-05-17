#!/usr/bin/python

import webbrowser
import time

class BreakScheduler:
	def __init__(self, sleep_time, song_url):
		self.sleep_time = sleep_time
		self.song_url = song_url

	def breakSchedulerTrigger(self):
		while True:
			time.sleep(self.sleep_time)
			webbrowser.open(self.song_url, new = 0)


if __name__ == "__main__":
	breakScheduler = BreakScheduler(10, "https://www.youtube.com/watch?v=rv4_CDCtz5U")
	breakScheduler.breakSchedulerTrigger()