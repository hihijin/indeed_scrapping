def save_to_file(file_name, jobs) :
  file = open(f"{file_name}.csv", "w")
  file.write("Postion, Company, Location, URL\n")
  
  for job in jobs:
    file.write(f"{job['position']}, {job['company']}, {job['region']}, {job['link']}\n")
    
  file.close()
def save_to_file(file_name, jobs) :
  file = open(f"{file_name}.csv","w", encoding="UTF-8")
  file.write("company, region, position, url\n")

  for job in jobs :
      file.write(f"{job['company']}, {job['region']}, {job['position']}, {job['link']}\n")


  file.close()
