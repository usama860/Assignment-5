class process:
	p_no = 0
	arrival_time = 0
	burst_time = 0
	priority = 0
	start_time = 0
	end_time = 0
	

processes = []
waiting_time = 0
turnaround_time = 0

count = input("Enter Number of Processes: ")

for index in range(int(count)):
	temp = process()
	temp.arrival_time = 0
	print '\nprocess no: ',(index+1)
	temp.priority = input("Enter priority : ")
	temp.burst_time = input("Enter Burst Time for Process no : ")
	temp.p_no = index
	processes.append(temp)



for i  in range(0,int(count)-1):
	for j  in range(i+1,int(count)):
		if processes[j].priority>processes[i].priority:
			processes[j], processes[i] = processes[i], processes[j]




processes[0].start_time = processes[0].arrival_time
processes[0].end_time =  processes[0].burst_time + processes[0].arrival_time

for index in range(1,int(count)):
	processes[index].start_time = processes[index-1].start_time + processes[index-1].burst_time
	processes[index].end_time = processes[index].start_time + processes[index].burst_time


print('\nArrival time is constant for all i.e=0')
for index in range(count):
	print '\nProcess', (processes[index].p_no+1)
	print 'Priority:', processes[index].priority
	print 'Started at:', processes[index].start_time
	print 'Ended at:', processes[index].end_time
	print 'Weighting time:', (processes[index].start_time-processes[index].arrival_time)
	print 'Turnaround time:', (processes[index].end_time-processes[index].arrival_time)
	waiting_time = waiting_time + (processes[index].start_time - processes[index].arrival_time)
	turnaround_time = turnaround_time + (processes[index].end_time - processes[index].arrival_time)

waiting_time = float(float(waiting_time) / float(count))	
turnaround_time = float(float(turnaround_time) / float(count))	


print '\n\nAverage waiting time: ', waiting_time
print 'Average turnaround time: ', turnaround_time
	
	

