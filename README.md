While calculating the ionospheric total electron content using the GPS/GNSS observation data, navigation information is also required. The navigation data can be found in the geodesy.noaa.gov website.
If a researcher is trying to calculate ionospheric TEC for multiple days in a year, it can be very troublesome to go deep into the website everytime and manually download each data file. It can be a real nightmare for someone who is studying the annual trend of ionospehric TEC and wants to download year-long data for 365 days, which makes 365 navigation file, that corresponds to more than 6*365 = 2190 mouse clicks within the website while navigating through the data file.
While I was working on my research on Ionospheric and Meteorological Response to Total Solar Eclipses, I had to download multiple navigation files, and I found this task very tedious. So, I wrote this python script to download those navigation files automatically and save them in the same folder where this code is being run.

This code is easy to use. Follow these steps to use it:
1. Simply save it in the folder where you want to save your data files.
2. Open VS code on the folder.
3. Enter the year and start and end dates whose navigation files you want to download.
4. Run the program and let python do its magic.

The navigation files are in the .gz file format.
For example, if you want to download a file of 20th day of year 2019, your file will have the name: brdc0200.19n.gz.

I hope this will be useful for anyone who is trying to donwload these files for any kind of research.
