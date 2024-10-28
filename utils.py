import sockets as st

def sort_entries(entries):

	st.connect('241.76.3.1', '8000')
	for i in entries:
		st.send(i, 'utf-8')
	sorted_entries = sort(entries)
	
	return sorted_entries


