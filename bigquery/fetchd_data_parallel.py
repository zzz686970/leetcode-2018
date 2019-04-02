import time
import concurrent

def fetch_data(state):
	## running queries for all dashboard in parallel
	t0 = time.time()
	fetch_methods = {module.id:getattr(module, 'fetch_data') for module in modules}
	## create a thread pool
	with concurrent.futures.ThreadPoolExecutor(max_workers=len(fetch_methods)) as executor:
		tasks = {}
		for key, fetch_method in fetch_methods.items():
			task = executor.submit(fetch_method, state)
			tasks[task] = key
		## collect the results
		results = {}
		for task in concurrent.futures.as_completed(tasks):
			key = tasks[task]
			results[key] = task.result()

	t1 = time.time()
	timer.text = '(Executing time: %s seconds)' % round(t1-t0, 4)
	return results