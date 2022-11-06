#def Graded_Questions():
#    Grading = [False,False,False,False,False,False] #6 Questions total. Mark True if you wish the autograder to grade it on push.

def fix_is_store_open(current_time, opening_times):
    current_time = current_time.replace(':', '')
    opening_time_list = opening_times.replace(':', '').split('-')
    start = opening_time_list[0]
    end = opening_time_list[1]
    # you can also explictly convert to int, strings work though:
    if current_time > '2359' or start > '2359' or end > '2359':
        return 'invalid time'
    else:
        return start <= current_time <= end


def reduce_frequencies(worker_output):
    frequencies = {}
    for worker in worker_output:
        for word, count in worker.items():
            if word not in frequencies:
                frequencies[word] = count
            else:
                frequencies[word] += count
    if not frequencies:
        return 0
    else:
        return max(frequencies.values())


