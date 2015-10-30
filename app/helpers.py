import operator

def get_next_element(current_item, li, direction):
    index = li.index(current_item)
    try:
        new_index = direction(index, 1)
        return li[new_index]
    except:
        return li[0]

def entries_to_remove(entries, the_dict):
    for key in entries:
        if key in the_dict:
            del the_dict[key]

def get_state(light_property, target_value):
	try:
		for attr, value in light_property.__dict__.iteritems():
			if value == target_value:
				return attr
		else:
  			raise NoMatch
	except:
		print "nomatch"
		entries = ('OFF','__doc__', '__module__')
		entries_to_remove(entries, light_property.__dict__)
		return min(light_property.__dict__, key=lambda y:abs(light_property.__dict__[y]-target_value))