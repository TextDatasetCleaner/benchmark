import psutil

print (psutil.cpu_times())
print (psutil.virtual_memory())
print (psutil.virtual_memory().percent)

for proc in psutil.process_iter(['pid', 'name', 'username']):
    print(proc.info)
