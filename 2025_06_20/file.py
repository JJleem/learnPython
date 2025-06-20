# flask

def save_to_file(filename, jobs):
  file = open(f"{filename}.csv", "w")
  file.write("Position,Company,Link,Reward\n")
  for job in jobs:
    file.write(f"{job['title']},{job['company_name']},{job['link']},{job['reward']}\n")
  file.close()
