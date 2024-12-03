import os
import requests

def download_file(url, file_path, filename):
    with open(os.path.join(file_path, filename), "wb") as f:
        response = requests.get(f"{url}/{filename}")
        f.write(response.content)
    print(f"File downloaded: {filename}")

# Enter your eclipse year here
year = 2019         # modify as your requirement

# Give your start and end day
start_day = 1         # modify as your requirement
end_day = 365         # modify as your requirement

yearr = str(year)
last = yearr[-2:]
file_path = os.getcwd()

for day in range(start_day, end_day+1):
    if day <= 9:
        link = f"https://geodesy.noaa.gov/corsdata/rinex/{year}/00{day}/"
        url = link
        filename = f"brdc00{day}0.{last}n.gz"
        download_file(url, file_path, filename)
    elif day <= 99:
        link = f"https://geodesy.noaa.gov/corsdata/rinex/{year}/0{day}/"
        url = link
        filename = f"brdc0{day}0.{last}n.gz"
        download_file(url, file_path, filename)
    else:
        link = f"https://geodesy.noaa.gov/corsdata/rinex/{year}/{day}/"
        url = link
        filename = f"brdc{day}0.{last}n.gz"
        download_file(url, file_path, filename)