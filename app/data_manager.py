import collections

class DataManager:
	def __init__(self, filename):
		self.file = filename + '.dat'
		self.Format = collections.namedtuple('Format', 'id first_name last_name event_name attendendance')
