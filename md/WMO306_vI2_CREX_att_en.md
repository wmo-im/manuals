ATTACHMENT

**CREX TEMPLATE EXAMPLES**

PROPOSED BLOEMHOF FLOOD MONITORING CREX CODE (HYDROLOGY)

***Indicator section and data description section***

CREX++

T000101 A000 D05004++

***Station identification***

Sequence: D 01 030 consisting of

> B 01 018 WMO station identifier
>
> B 02 001 Type of station
>
> D 01 011 Date
>
> D 01 024 Latitude and longitude and height

***Hourly environmental data***

Sequence: D 05 002 consisting of

> D 01 012 Time (hour, minute)
>
> B 12 001 Air temperature
>
> B 13 003 Relative humidity
>
> B 14 051 Direct solar radiation during the last hour
>
> B 13 060 Total accumulated precipitation (modulo 10 000 kg m^--2^)
>
> B 13 072 Downstream water level
>
> B 13 080 pH
>
> B 13 081 Conductivity
>
> B 13 082 Water temperature
>
> B 13 083 Dissolved oxygen
>
> B 13 084 Turbidity

***Multiple measurement array definition***

Sequence: D 05 003 consisting of

> D 01 012 Time of first measurement (hour, minute) minus increment
>
> B 04 065 Short time increment -- time interval between measurements in the array (12 minutes)
>
> R 01 000 Delayed replication of one next descriptor (D 05 001) -- Number of measurements in the array (5)
>
> D 05 001 Single measurement

***\
***

***Single measurement***

Sequence: D 05 001 consisting of

> B 11 001 Wind direction
>
> B 11 002 Wind speed
>
> B 13 060 Total accumulated precipitation (modulo 10 000 kg m^--2^)
>
> B 13 071 Upstream water level

***End of message***

\...++

7777

Thus the format of the message D 05 004 for the BLOEMHOF Flood Monitoring System will be:

> Indicator section and data description section then:
>
> D 01 030 Identification
>
> D 05 002 Hourly instantaneous values
>
> D 05 003 Array definition
>
> n x D 05 001 Multiple measurements
>
> ++ 7777 End of message

***Example***

A CREX message transmitted at 1046 UTC would be the following:

> CREX++
>
> T000101 A000 D05004++
>
> 12345 2 1998 02 03 --2600 02800 01570
>
> 10 00 285 065 0326 03842 0683 075 2600 2805 ///// 0156
>
> 09 00 12 0005
>
> 290 0102 00012 1226
>
> 250 0250 00025 1230
>
> 245 0175 00028 1235
>
> 230 0105 00004 1241
>
> 220 0025 00001 1249++
>
> 7777

Note that the + at end of lines are not needed, only at the end of the whole report (in that case after 1249 -- last line) and only if a whole message was to be repeated one or more times. The whole message from 12345 to 1249 is called a "subset" (See Regulation 95.4.1). The space before --2 600 is required for transmission purposes, but optional for display (to keep alignment). Fifth line, last group = delayed replication -- 4 digits only = 0005.

Line 1: Message identification

Line 3:

> Station number: 12345
>
> Station type: 2
>
> Date of main measurement: 3 February 1998
>
> Position of station: 26 degrees South, 28 degrees East, 1 570 m high

***\
***

Line 4:

> Time of hourly measurement: 1000 UTC
>
> Air temperature at 1000 UTC: 28.5 °C
>
> Relative humidity at 1000 UTC: 65%
>
> Direct solar radiation integrated over the period 0900 to 1000 UTC: 326 000 J m^--2^
>
> Total accumulated precipitation at 1000 UTC: 384.2 kg m^--2^
>
> Downstream water level at 1000 UTC: 6.83 m
>
> Water pH: 7.5
>
> Conductivity at 1000 UTC: 2.6 Siemens m^--1^ = 26 mS cm^--1^
>
> Water temperature at 1000 UTC: 280.5 K
>
> Dissolved oxygen at 1000 UTC: Not available
>
> Turbidity at 1000 UTC: 156 Lumen

Line 5: Measurement array definition

> First measurement minus 12 minutes at 0900 UTC
>
> Interval between measurements is 12 minutes
>
> Number of measurements is 5

Line 6: First set of measurements at 0912 UTC

> Instantaneous wind direction at 0912 UTC: 290
>
> Instantaneous wind speed at 0912 UTC: 10.2 m s^--1^
>
> Total precipitation between 0900 and 0912 UTC: 1.2 kg m^--2^
>
> Upstream water level at 0912 UTC: 12.26 m

Line 7: Second set of measurements at 0924 UTC

> Instantaneous wind direction at 0924 UTC: 250
>
> Instantaneous wind speed at 0924 UTC: 25.0 m s^--1^
>
> Total precipitation between 0912 and 0924 UTC: 2.5 kg m^--2^
>
> Upstream water level at 0924 UTC: 12.30 m

Line 8: Third set of measurements at 0936 UTC

> Instantaneous wind direction at 0936 UTC: 245
>
> Instantaneous wind speed at 0936 UTC: 17.5 m s^--1^
>
> Total precipitation between 0912 and 0936 UTC: 2.8 kg m^--2^
>
> Upstream water level at 0936 UTC: 12.35 m

Line 9: Fourth set of measurements at 0948 UTC

> Instantaneous wind direction at 0948 UTC: 230
>
> Instantaneous wind speed at 0948 UTC: 10.5 m s^--1^
>
> Total precipitation between 0912 and 0948 UTC: 0.4 kg m^--2^
>
> Upstream water level at 0948 UTC: 12.41 m

***\
***

Line 10: Fifth set of measurements at 1000 UTC

> Instantaneous wind direction at 1000 UTC: 220
>
> Instantaneous wind speed at 1000 UTC: 2.5 m s^--1^
>
> Total precipitation between 0912 and 1000 UTC: 0.1 kg m^--2^
>
> Upstream water level at 1000 UTC: 12.49 m

Line 11: End of message identifier

TIDE GAUGE DATA EXAMPLE

CREX++

T000101 A001 D06025++

RI010 1998 01 23 15 00 2761 00 00 30 --30

01407 1225 01384 1217 01382 1221 01395 1220 01473 1262 01502 1227+

CT010 1998 01 23 15 00 2781 01 00 30 --30

02024 1757 02043 1717 02124 1728 02177 1716 ///// //// 02259 1670++

7777

Interpretation of the example:

*Line Group Meaning*

1 CREX Indicator of a CREX message

2 T000101 CREX Master Table Number 00, Edition 01, Version 01

A0001 Data type 001: Surface data -- sea

D 06 025 Tide elevation series

3 RI010 Tide station RI010

1998 Year: 1998

01 Month: January

23 Day: 23

15 Hour: 1500 UTC

00 Minute: 00

2761 Sea/water temperature: 276.1 K

00 Tide station automated water level check: Good data

00 Tide station manual water level check: Operational

30 Time increment: Time is now hour 1500, minute 30

--30 Short time increment: Increment is applied prior to each replication of two descrip-\
tors indicated by the group R 02 006, thus the time is now hour 1500, minute 00

4 01407 Tide elevation of 1 407 mm at hour 1500, minute 00

1225 Meteorological residual tidal elevation of 1 225 mm at hour 1500, minute 00

01384 Tide elevation of 1 384 mm at hour 1400, minute 30

***\
***

1217 Meteorological residual tidal elevation of 1 217 mm at hour 1400, minute 30

01382 Tide elevation of 1 382 mm at hour 1400, minute 00

1221 Meteorological residual tidal elevation of 1 221 mm at hour 1400, minute 00

01395 Tide elevation of 1 395 mm at hour 1300, minute 30

1220 Meteorological residual tidal elevation of 1 220 mm at hour 1300, minute 30

01473 Tide elevation of 1 473 mm at hour 1300, minute 30

1262 Meteorological residual tidal elevation of 1 262 mm at hour 1300, minute 00

01502 Tide elevation of 1 502 mm at hour 1200, minute 30

1227 Meteorological residual tidal elevation of 1 227 mm at hour 1200, minute 30

\+ End of report for station RI010

5 CT010 Tide station CT010

1998 Year: 1998

01 Month: January

23 Day: 23

15 Hour: 1500 UTC

00 Minute: 00

2761 Sea/water temperature: 276.1 K

00 Tide station automated water level check: Good data

00 Tide station manual water level check: Operational

30 Time increment: Time is now hour 1500, minute 30

--30 Short time increment: Increment is applied prior to each replication of two\
descriptors indicated by the group R 02 006, thus the time is now hour 1500,\
minute 00

6 02024 Tide elevation of 2 024 mm at hour 1500, minute 00

1715 Meteorological residual tidal elevation of 1 715 mm at hour 1500, minute 00

02043 Tide elevation of 2 043 mm at hour 1400, minute 30

1717 Meteorological residual tidal elevation of 1 717 mm at hour 1400, minute 30

02124 Tide elevation of 2 124 mm at hour 1400, minute 00

1728 Meteorological residual tidal elevation of 1 728 mm at hour 1400, minute 00

02177 Tide elevation of 2 177 mm at hour 1300, minute 30

1716 Meteorological residual tidal elevation of 1 716 mm at hour 1300, minute 30

///// Tide elevation missing at hour 1300, minute 30

//// Meteorological residual tidal elevation missing at hour 1300, minute 00

02259 Tide elevation of 2 259 mm at hour 1200, minute 30

1670 Meteorological residual tidal elevation of 1 670 mm at hour 1200, minute 30

++ End of report for station CT010; also, end of Data section

7 7777 End of CREX message

***\
***

**TOTAL OZONE MEASUREMENT FROM A BREWER GROUND-BASED SPECTROPHOTOMETER OBTAINED FROM AVERAGED OBSERVATIONS**

KULD40 OKOH 041643

CREX++

T0002071500 A008002 P00089001 U00 S001 Y20110504 H0748 D07042++

11 649 Hradec Kralove 5018 01583 00285 2011 05 04 07

48 08 0526 001 98 00 00022 04 0383 09 0012 11 157++

7777

**CREX**

**T0002071500 CREX master table** 00

**CREX edition number** 02

**CREX table version number** 07

**BUFR Master table version number used** 15

**Version number of local table** 00

**A008002** Data category 008

International data subcategory 002

**P00089001** Originating centre (Common Code table C--11) 00089

Originating sub-centre (Common Code table C--12) 001

**U00** Update sequence number (00 for original and delayed 00

messages; incremented for corrected messages)

**S001** Number of subsets included in the report 001

**Y20110504** Year 2011

Month 05

Day 04

**H0748** Hour 07

Minute 48

**D07042** D01001

B01001 WMO block number 11

B01002 WMO station number 649

B01015 Station or site name **^(1)^** Hradec Kralove\^\^\^\^\^\^

D01024

B05002 Latitude **^(2)\ (3)^** 50.18 deg N 5018

B06002 Longitude **^(2)\ (3)^** 15.83 deg E 01583

B07001 Height of station 00285

D01011

B04001 Year (of ozone measurement) 2011

B04002 Month (of ozone measurement) 05

B04003 Day (of ozone measurement) 04

D01012

B04004 Hour (of ozone measurement) **^(4)^** 07

B04005 Minute (of ozone measurement) **^(4)^** 48

B08021 Time significance = 8 = ensemble mean**^(5)^** 08

B04025 Time period (in minutes) 0526

D01070

B02143 Ozone instrument type 001

B02142 Ozone instrument serial number **^(1)^** 98\^\^

B02144 Light source type for Brewer spectrophotometer **^(6)^** 00

D07031

B08022 Number of measurements 00022

B08023 First order statistic = 4 = mean value 04

B15001 Value (average) of ozone measurement 0383

B08023 First order statistic = 9 = best estimate of std deviation 09

B15001 Best estimate of std deviation of the ozone 0012

measurement

B08023 First order statistic = 11 = harmonic mean 11

B15002 Harmonic mean of the air mass 157

**7777**

Notes:

\(1) Characters "\^\^\^\^\^\^" are used for visualization of the corresponding number of space characters.

\(2) Latitude and longitude shall be reported in degrees with precision in hundredths of a degree.

\(3) South latitude and west longitude shall be assigned negative values.

\(4) Hour and minute specify the time of the first measurement of the series.

\(5) "Ensemble mean" indicates that a number of distinct values corresponding to a set of time locations are averaged.

\(6) Ozone measurements of only one light source shall be selected, i.e. the best light source of the day.

EXAMPLE OF AN OZONE SOUNDING COUPLED TO A BREWER SPECTROPHOTOMETER

Note: \^ means space in the definitions below

> CREX++
>
> T000101
>
> A008
>
> D 01 001 WMO block number 71
>
> WMO station 913
>
> B 01 015 Station or site name Churchill\^\^\^\^\^\^\^\^\^\^\^
>
> D 01 024 Latitude 5875
>
> Longitude --09400
>
> Elevation 00029
>
> D 01 011 Year 1998
>
> Month 04
>
> Day 29
>
> D 01 012 Hours 13
>
> Minutes 46
>
> B 08 021 Time significance = 8 = ensemble mean 08
>
> B 04 025 Time period (minutes) 0550
>
> D 01 070 Ozone instrument type 001
>
> Ozone instrument serial number (Brewer) 26\^\^
>
> Light source type for Brewer (direct sun) 00
>
> B 08 022 Number of measurements 00010
>
> B 08 023 First order statistics = 4 = mean value 04
>
> B 15 001 Value of ozone measurement 0399
>
> B 08 023 First order statistics = 9 = best estimate of standard deviation 09
>
> B 15 001 Best estimate of standard deviation 0010
>
> B 08 023 First order statistics = harmonic mean 11
>
> B 15 002 Harmonic mean of the air mass 202
>
> D 01 001 WMO block and station number 71
>
> 913
>
> B 01 015 Station or site name Churchill\^\^\^\^\^\^\^\^\^\^\^
>
> D 01 024 Latitude 5875
>
> Longitude --09400
>
> Elevation 00029
>
> B 08 021 18 = launch time follows 18
>
> D 01 011 Year 1998
>
> Month 04
>
> Day 29
>
> D 01 012 Hours 11
>
> Minutes 22
>
> B 02 011 Radiosonde type 061
>
> B 02 143 Ozone instrument type 019
>
> B 02 142 Ozone sonde serial number ////
>
> D 15 004 Ozone sounding correction factor 0893
>
> D 15 005 Ozone p 373
>
> R 04 000 Delayed replication factor = number of levels 0093
>
> The next four descriptors are repeated 93 times
>
> B 04 025 Time displacement since launch time (minutes) See below
>
> B 08 006 Ozone VSS See below
>
> B 07 004 Pressure See below
>
> B 15 003 Measured ozone partial pressure See below
>
> ++
>
> 7777 End of message

KULA01 CWAO 051800

CREX++

T000101 A008 D09047++

71 913 CHURCHILL 5875 --09400 00029 1998 04 29 13 46

> 08 0550 001 26 00 00010 04 0399 09 0010 11 202
>
> 71 913 CHURCHILL 5875 --09400 00029 18 1998 04 29 11 22
>
> 061 019 //// 0893 373 0093
>
> 0000 400 10041 029 0000 200 10000 029 0000 002 09915 031
>
> 0001 002 09735 036 0001 002 09678 038 0002 002 09273 038
>
> 0003 002 09111 039 0004 200 08500 039 0009 200 07000 037
>
> 0011 002 06450 037 0012 002 06279 036 0012 002 06159 031
>
> 0014 002 05847 034 0016 002 05347 030 0016 002 05269 029
>
> 0017 002 05100 040 0018 200 05000 034 0019 002 04821 030
>
> 0023 200 04000 030 0027 002 03400 026 0029 002 03000 028
>
> 0031 002 02857 029 0031 002 02818 024 0032 002 02743 017
>
> 0034 200 02500 015 0036 002 02225 014 0038 002 02078 029
>
> 0038 002 02049 036 0039 200 02000 066 0039 002 01992 066
>
> 0039 002 01952 093 0040 002 01909 105 0040 002 01866 105
>
> 0041 002 01800 115 0042 002 01765 103 0042 002 01741 100
>
> 0043 002 01693 112 0043 002 01656 112 0044 002 01612 109
>
> 0044 002 01590 092 0044 002 01580 066 0045 002 01559 052
>
> 0045 002 01517 049 0046 002 01500 059 0046 002 01488 070
>
> 0046 002 01469 098 0047 002 01440 107 0047 002 01391 107
>
> 0048 002 01335 117 0049 002 01291 162 0050 002 01257 153
>
> 0051 002 01206 155 0051 002 01190 141 0051 002 01182 141
>
> 0052 002 01142 156 0053 002 01103 154 0054 002 01059 177
>
> 0055 002 01005 170 0056 200 01000 178 0056 002 00978 197
>
> 0057 002 00951 187 0058 002 00914 183 0058 002 00889 171
>
> 0059 002 00866 182 0059 002 00855 195 0060 002 00837 198
>
> 0061 002 00808 175 0061 002 00797 172 0064 200 00700 160
>
> 0065 002 00671 157 0067 002 00630 142 0068 002 00592 153
>
> 0068 002 00583 162 0070 002 00531 157 0072 002 00501 164
>
> 0072 200 00500 161 0073 002 00479 162 0073 002 00462 151
>
> 0075 002 00435 156 0076 002 00418 153 0078 002 00378 161
>
> 0081 002 00319 132 0082 002 00311 136 0083 200 00300 130
>
> 0086 002 00258 111 0091 200 00200 095 0097 002 00143 079
>
> 0099 002 00126 078 0103 200 00100 071 0110 200 00070 058
>
> 0115 002 00054 044 0116 200 00050 039 0120 002 00043 032++

7777

EXAMPLE OF AN OZONE SOUNDING NOT COUPLED TO A BREWER SPECTROPHOTOMETER

CREX++

T000101

A008

D 01 001 WMO station and block number 71

917

B 01 015 Station or site name Eureka\^\^\^\^\^\^\^\^\^\^\^\^\^\^

D 01 024 Latitude 7598

Longitude --08593

Elevation 00010

B 08 021 18 = launch time follows 18

D 01 011 Year 1998

Month 04

Day 29

D 01 012 Hours 23

Minutes 18

B 02 011 Radiosonde type 061

B 02 143 Ozone instrument type 019

B 02 142 Ozone sonde serial number ////

D 15 004 Ozone sounding correction factor ////

D 15 005 Ozone p 375

R 04 000 Delayed replication factor = number of levels 0082

The next four descriptors are repeated 82 times

B 04 025 Time displacement since launch time (minutes) See below

B 08 006 Ozone VSS See below

B 07 004 Pressure See below

B 15 003 Measured ozone partial pressure See below

++

7777 End of message

KULA01 CWAO 051800

CREX++

T000101 A008 D09045++

71 917 EUREKA 7598 --08593 00010 18 1998 04 29 23 18

> 061 019 //// //// 375 0082
>
> 0000 400 10137 030 0000 200 10000 030 0001 002 09687 037
>
> 0002 002 09366 033 0004 002 08831 037 0005 200 08500 036
>
> 0007 002 08013 043 0007 002 07881 047 0008 002 07646 037
>
> 0009 002 07442 042 0011 200 07000 031 0012 002 06849 027
>
> 0013 002 06710 036 0015 002 06291 029 0022 200 05000 028
>
> 0025 002 04557 027 0029 002 04065 024 0029 200 04000 020
>
> 0032 002 03626 025 0038 002 03000 020 0040 002 02890 021
>
> 0040 002 02829 065 0041 002 02726 105 0043 002 02576 118
>
> 0044 200 02500 135 0048 002 02218 165 0049 002 02147 161
>
> 0050 002 02104 171 0051 002 02031 153 0051 002 02010 159
>
> 0051 200 02000 171 0052 002 01941 188 0054 002 01854 198
>
> 0056 002 01744 187 0056 002 01717 194 0057 002 01683 191
>
> 0058 002 01640 161 0058 002 01623 159 0059 002 01585 168
>
> 0059 002 01576 185 0060 002 01545 197 0061 002 01500 202
>
> 0063 002 01414 221 0064 002 01370 220 0065 002 01335 230
>
> 0066 002 01269 219 0067 002 01232 227 0067 002 01226 235
>
> 0068 002 01208 241 0072 002 01055 242 0074 200 01000 236
>
> 0075 002 00960 228 0076 002 00936 192 0077 002 00912 180
>
> 0078 002 00897 187 0078 002 00883 210 0079 002 00868 221
>
> 0079 002 00850 202 0080 002 00841 199 0081 002 00815 208
>
> 0081 002 00807 189 0081 002 00803 171 0082 002 00790 152
>
> 0082 002 00777 157 0083 002 00764 172 0084 002 00741 156
>
> 0084 002 00722 156 0085 002 00715 162 0085 200 00700 188
>
> 0085 200 00700 193 0086 002 00682 203 0088 002 00639 212
>
> 0090 002 00608 206 0091 002 00588 190 0091 002 00582 192
>
> 0092 002 00570 209 0092 002 00557 215 0096 200 00500 197
>
> 0099 002 00437 171 0108 002 00316 139 0110 200 00300 128
>
> 0115 002 00242 108++

7777

SAMPLE DATA WITH CREX SEQUENCE FOR EXCHANGE OF FORECAST RESULT ON

TROPICAL CYCLONES

Descriptor Order Sample Corresponding meaning Unit Scale Data

No. data width

B 01 033 1 034 Originating Centre = RSMC Tokyo Code table 0 3

B 01 025 2 21W Storm identifier Character 0 3

B 01 027 3 ZANE WMO storm name Character 0 10

D 01 011 (sequence descriptor)

B 04 001 4 1996 Year Year 0 4

B 04 002 5 10 October Month 0 2

B 04 003 6 01 1st Day 0 2

D 01 012 (sequence descriptor)

B 04 004 7 06 6 o\'clock (UTC) Hour 0 2

B 04 005 8 00 0 minute (UTC) Minute 0 2

B 01 032 9 XXX (to be defined)

Identification of NWP model Code table 0 3

B 02 041 0 01 Based on computer analysis Code table 0 2

B 19 001 1 02 Tropical storm Code table 0 2

B 19 010 2 01 Minimum value of sea-level pressure Code table 0 2

R 18 000 3 0003 (\*\*\*delayed replication descriptor\*\*) Numeric 0 4

Data for 3 forecast times of 18

descriptors follow

B 08 021 4 04 Forecast data follow Code table 0 2

B 04 014 5 0012 12 hour forecast data follow Hour 0 4

B 08 005 6 01 Data of storm centre follow Code table 0 2

D 01 023 (sequence descriptor)

B 05 002 7 3010 Latitude of the storm centre is 30.1N Degree 2 4

B 06 002 8 14200 Longitude of the storm centre is 142.0E Degree 2 5

B 19 005 9 270 Direction of motion of storm is 270 Degree true 0 3

B 19 006 0 00500 Speed of motion of storm is 5 m s^--1^ m s^--1^ 2 5

B 10 004 1 09750 Pressure of storm centre is 975 hPa Pa --1 5

B 11 041 2 0576 Gust wind speed is 57.6 m s^--1^ m s^--1^ 1 4

B 08 021 3 06 Forecast time averaged follow Code table 0 2

B 04 075 4 10 10 minutes mean value follow Minute 0 2

B 11 040 5 0360 Maximum wind speed is 36.0 m s^--1^ m s^--1^ 1 4

B 19 008 6 2 Storm depth is medium Code table 0 1

R 05 004 \*\*\*(replication descriptor)

4 times replication of following

5 descriptors

B 05 021 7 31500 Sector 1 (from 315 degrees Degree true 2 5

B 05 021 8 04500 to 45 degrees) Degree true 2 5

R 02 002 \*\*\*(replication descriptor)

2 times replication of following

2 descriptors

B 19 003 9 025 Wind speed threshold is 25 m s^--1^ m s^--1^ 0 3

B 19 004 0 1950 Effective radius is 195 km m --2 4

Descriptor Order Sample Corresponding meaning

No. data

1 015 Wind speed threshold is 15 m s^--1^

2 4000 Effective radius is 400 km

3 04500 Sector 2 (from 45 degrees

to 135 degrees)

4 13500

5 025 Wind speed threshold is 25 m s^--1^

6 1950 Effective radius is 195 km

7 015 Wind speed threshold is 15 m s^--1^

8 4300 Effective radius is 430 km

9 13500 Sector 3 (from 135 degrees

to 225 degrees)

0 22500

1 025 Wind speed threshold is 25 m s^--1^

2 1950 Effective radius is 195 km

3 015 Wind speed threshold is 15 m s^--1^

4 6090 Effective radius is 609 km

5 22500 Sector 4 (from 225 degrees

to 315 degrees)

6 31500

7 025 Wind speed threshold is 25 m s^--1^

8 1950 Effective radius is 195 km

9 015 Wind speed threshold is 15 m s^--1^

0 4700 Effective radius is 470 km

1 04 (24- and 36-hour forecast data follow as same as

\...\...\.... the second fourth order above) \...\...\....

***CREX MESSAGE COMPOSED OF ABOVE DATA ELEMENTS:***

CREX++

T000101 A007 B01033 B01025 B01027 D01011 D01012 B01032 B02041 B19001 B19010 R18000 B08021

B04014 B08005 D01023 B19005 B19006 B10004 B11041 B08021 B04075 B11040 B19008 R05004 B05021

B05021 R02002 B19003 B19004E++

0034 121W 2ZANE 31996 410 501 606 700 8XXX 901 002 101 20003 304 40012 501 63010 714200 8270

900500 009750 10576 206 310 40360 52 631500 704500 8025 91950 0015 14000 204500 313500 4025 51950

6015 74300 813500 922500 0025 11950 2015 36090 422500 531500 6025 71950 8015 94700 004 \...\...\...\...++

7777

or (with big common sequence definition)

CREX++

T000101 A007 D16027E++

0034 121W 2ZANE 31996 410 501 606 700 8XXX 901 002 101 20003 304 40012 501 63010 714200 8270

900500 009750 10576 206 310 40360 52 631500 704500 8025 91950 0015 14000 204500 313500 4025 51950

6015 74300 813500 922500 0025 11950 2015 36090 422500 531500 6025 71950 8015 94700 004 \...\...\...\...++

7777

or without check digit:

CREX++

T000101 A007 D16027++

034 21W ZANE 1996 10 01 06 00 XXX 01 02 01 0003 04 0012 01 3010 14200 270 00500 09750 0576 06 10

0360 2 31500 04500 025 1950 015 4000 04500 13500 025 1950 015 4300 13500 22500 025 1950 015 6090

22500 31500 025 1950 015 4700 04 \...\...\...\...++

7777

**\
**

**MONITORING INFORMATION SAMPLE MESSAGE**

CREX++ (indicator section)

T000101 A020 D35010++ (description section)

1 2 4 014 23 1996 10 01 00 15 24 06 25 00 012 63 0003 740 0360 894 0353

792 0125++ (data section)

7777 (end section)

1 Regional exercise

2 Non-real time

4 RTH

014 Nairobi

23 Monitoring period follows

1996 YYYY

10 MM

01 DD

00 HH

15 Days duration

24 Data cut-off follows

06 Hours

25 Report time follows

00 Hours

012 SYNOP

63 Block number

0003 Stations

740 Nairobi

0360 Well done

894 Dar es Salaam

0353 Very good

792 A station

0125 Must do better!

++

7777

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
