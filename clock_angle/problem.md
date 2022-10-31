Clock Angle Problem: Given time in hh:mm format in 24-hour notation, calculate the shorter angle between the hour and minute hand in an analog clock.
For example,
Input:  5:30
Output: 15°
 
 
Input:  21:00
Output: 90°
 
 
Input:  12:00
Output: 0°
 

Please note that hh:60 should be considered as (hh+1):0

Extra stuff


The hour hand of a 12–hour analog clock turns 360° in 12 hours, and the minute hand rotates through 360° in 60 minutes. So, we can calculate the angle in degrees of the hour hand minute hand separately and return their difference using the following formula:
Degree(hh) = H×(360/12) + (M×360)/(12×60)
Degree(mm) = M×(360/60) 