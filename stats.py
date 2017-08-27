import time
import spidev as SPI
import EPD_driver
import datetime
import subprocess


EPD2X9 = 0
EPD02X13 = 1
EPD1X54 = 0

bus = 0 
device = 0
 	
disp = EPD_driver.EPD_driver(spi=SPI.SpiDev(bus, device))


# stats are gathered at the top because you dont have to wait for the screen to refresh to find out your code sucks
print '---- start gathereing some stats -------'

  # Shell scripts for system monitoring from here : https://unix.stackexchange.com/questions/119126/command-to-display-memory-usage-disk-usage-and-cpu-load
cmd = "hostname -I | cut -d\' \' -f1"
IP = subprocess.check_output(cmd, shell = True )
cmd = "top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\", $(NF-2)}'"
CPU = subprocess.check_output(cmd, shell = True )
cmd = "free -m | awk 'NR==2{printf \"Mem: %s/%sMB %.2f%%\", $3,$2,$3*100/$2 }'"
MemUsage = subprocess.check_output(cmd, shell = True )
cmd = "df -h | awk '$NF==\"/\"{printf \"Disk: %d/%dGB %s\", $3,$2,$5}'"
Disk = subprocess.check_output(cmd, shell = True )
cmd = "curl -s wttr.in/sydney?0?T |tail -n5 |xargs | sed -e 's/ //g'|sed 's/[^a-zA-Z0-9]/ /g'"
Weather = subprocess.check_output(cmd, shell = True )
cmd = "date|cut -c-26"
Date = subprocess.check_output(cmd, shell = True)
    
    #weather cmd curl -s wttr.in/sydney?0 |tail -n5| awk '{ print $4$5$6 }' |xargs | sed -e 's/ / /g'
    #works curl -s wttr.in/sydney?0?T |tail -n5 |xargs | sed -e 's/ //g'|sed 's/[^a-zA-Z0-9]/ /g'
    #curl -s wttr.in/sydney?0?T |tail -n5 |xargs | sed -e 's/ //g'|sed 's/[^a-zA-Z0-9]/ /g'|awk '{print $1,$2\"-\"$3,$4,$5$6,"winds",$8$9" rainfall"}'
#test prints 

    # Write two lines of text.

    #draw.text((x, top),       "IP: " + str(IP),  font=font, fill=255)
    #draw.text((x, top+8),     str(CPU), font=font, fill=255)
    #draw.text((x, top+16),    str(MemUsage),  font=font, fill=255)
    #draw.text((x, top+25),    str(Disk),  font=font, fill=255)

    
#####dont remove BOTH clears or for some reason it just never displays.
#init and Clear full screen
print '------------init and Clear full screen------------'
disp.Dis_Clear_full()
#init and Clear part screen  
print '------------init and Clear part screen------------'
disp.Dis_Clear_part()
######dont remove the above clears!!! 

#String Font size range seems to be from 12 to 16.. for some reason
print '------------Show string------------'
disp.Dis_String(0, 0, "IP: " + str(IP),16) 
disp.Dis_String(0, 20, str(CPU),16)
disp.Dis_String(0, 36, str(MemUsage),16)
disp.Dis_String(0, 52, str(Disk),16)
disp.Dis_String(0, 68, "Weather in Sydney:",16)
disp.Dis_String(0, 84, str(Weather),12)
disp.Dis_String(0, 96, str(Date),16)

#time.sleep(DELAYTIME)

#print '------------show time------------'
#while 1 :
#	now = datetime.datetime.now()
#	now_sec = now.second%10
#	next_sec = 11  #Guaranteed next greater than 9
#	if now_sec != next_sec:
#		disp.Dis_showtime(now.hour,now.minute,now.second)
#		next_sec = now.second%10
