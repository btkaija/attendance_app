# Will either return a nine diget ID number or 'invalid'
def parse_card_data(swipe):
	#normal swipe is formatted as ;XXXXXXXXX=XXXX?
	#faulty swipe %E?;XXXXXXXXX=XXXX? or ;E? or ;E?+E? or +E?
	try:
		if len(swipe) == 9 and int(swipe)>0:
			return swipe
		elif len(swipe) == 16:
			normal_swipe = swipe.split('=')[0].split(';')[1]
			if len(normal_swipe) != 9:
				normal_swipe = 'invalid'
			return normal_swipe
		elif len(swipe) == 19:
			errored_swipe = swipe.split(';')[1].split('=')[0]
			if len(errored_swipe) != 9:
				errored_swipe = 'invalid'
			return errored_swipe
		else:
			return 'invalid'
	except (IndexError, ValueError):
		return 'invalid'