**c. COMMON CODE TABLES TO BINARY AND ALPHANUMERIC CODES**

**COMMON CODE TABLE C--0: *GRIB, BUFR and CREX master table version number***

Octet 10 in Section 1 of GRIB Edition 2

Octet 14 in Section 1 of BUFR Edition 4

vv and bb in Group No. 1 in Section 1 of CREX Edition 2

**COMMON CODE TABLE C--1: *Identification of originating/generating centre***

F~1~F~2~ for alphanumeric codes

F~3~F~3~F~3~ for alphanumeric codes

Code table 0 in GRIB Edition 1/Code table 0 01 033 for BUFR Edition 3

Octet 5 in Section 1 of GRIB Edition 1/Octet 6 in Section 1 of BUFR Edition 3

**COMMON CODE TABLE C--2: *Radiosonde/sounding system used***

Code table 3685 -- r~a~r~a~ (Radiosonde/sounding system used) -- for alphanumeric codes

Code table 0 02 011 (Radiosonde type) in BUFR

**COMMON CODE TABLE C--3: *Instrument make and type for water temperature profile measurement with*** ***fall rate equation coefficients***

Code table 1770 -- I~X~I~X~I~X~ (Instrument type for XBT, with fall rate equation coefficients) -- for\
alphanumeric codes

Code table 0 22 067 (Instrument type for water temperature/salinity profile measurement) in BUFR

**COMMON CODE TABLE C--4: *Water temperature profile recorder types***

Code table 4770 -- X~R~X~R~ (Recorder type) -- for alphanumeric codes

Code table 0 22 068 (Water temperature profile recorder types) in BUFR

**COMMON CODE TABLE C--5: *Satellite identifier***

I~6~I~6~I~6~ for alphanumeric codes

Code table 0 01 007 in BUFR

Code used in GRIB Edition 2

**COMMON CODE TABLE C--6: *List of units for TDCFs***

(Used only in Volume I.2, Parts B and C)

**COMMON CODE TABLE C--7: *Tracking technique/status of system used***

Code table 3872 -- s~a~s~a~ for alphanumeric code

Code table 0 02 014 in BUFR

**COMMON CODE TABLE C--8: *Satellite Instruments***

Code table 0 02 019 in BUFR

**\
**

**COMMON CODE TABLE C--11: *Originating/generating centres***

BUFR 0 01 035

CREX Edition 2, ooooo in Group Poooooppp in Section 1

GRIB Edition 2, Octets 6--7 in Section 1

BUFR Edition 4, Octets 5--6 in Section 1

**COMMON CODE TABLE C--12: *Sub-centres of originating centres defined by entries in Common Code\
tables C--1 or C--11***

BUFR 0 01 034

BUFR Edition 3, Octet 5 in Section 1

BUFR Edition 4, Octets 7--8 in Section 1

GRIB Edition 1, Octet 26 in Section 1

GRIB Edition 2, Octets 8--9 in Section 1

CREX Edition 2, ppp in Group Poooooppp in Section 1

**COMMON CODE TABLE C--13: *Data sub-categories of categories defined by entries in BUFR Table A***

BUFR Edition 4, Octet 12 in Section 1 (if = 255, it means other sub-category or undefined)

CREX Edition 2, mmm in Group Annnmmm of Section 1

**COMMON CODE TABLE C--14: *Atmospheric chemical or physical constituent type***

Code Table 4.230 in GRIB 2

**COMMON CODE TABLE C--0: *GRIB, BUFR and CREX master table version number***

Octet 10 in Section 1 of GRIB Edition 2

Common Code table Octet 14 in Section 1 of BUFR Edition 4

vv and bb in Group No. 1 in Section 1 of CREX Edition 2

Version number

GRIB BUFR CREX Effective date

0 0 0 Experimental

1 1 November 1988

2 1 November 1993

3 2 November 1994

4 8 November 1995

5 6 November 1996

6 5 November 1997

7 4 November 1998

8 1 3 May 2000

9 8 November 2000

1 10 2 7 November 2001

2 11 3 5 November 2003

3 12 4 2 November 2005

4 13 5 7 November 2007

5 14 6 4 November 2009

6 15 7 15 September 2010

7 16 16 4 May 2011

8 17 17 2 November 2011

9 18 18 2 May 2012

10 19 19 7 November 2012

11 20 20 8 May 2013

12 21 21 14 November 2013

13 22 22 7 May 2014

14 23 23 5 November 2014

15 24 24 6 May 2015

16 25 25 11 November 2015

17 26 26 4 May 2016

18 27 27 2 November 2016

19 28 28 3 May 2017

20 29 29 8 November 2017

21 30 30 2 May 2018

22 31 31 7 November 2018

23 32 32 Pre-operational to be implemented by next amendment

24**--**254 33**--**254 33**--**254 Future versions

255 255 255 Missing

Notes:

\(1) Introduction of Common Code table C--0 is a legal initiative. WMO Members and other TDCF users could practically deal with the version numbers the same as before until their software becomes capable of referring to the common code table.

\(2) CREX master table version numbers 8--15 are not used.

\(3) In the case of BUFR and CREX, these version numbers apply to the master table 0.

**COMMON CODE TABLE C--1: *Identification of originating/generating centre***

F~1~F~2~ for alphanumeric codes

Common Code table F~3~F~3~F~3~ for alphanumeric codes

Code table 0 in GRIB Edition 1/Code table 0 01 033 in BUFR Edition 3

Octet 5 in Section 1 of GRIB Edition 1/Octet 6 in Section 1 of BUFR Edition 3

Octet 5 in Section 1

Code figure Code figure of GRIB Edition 1

for F~1~F~2~ for F~3~F~3~F~3~ Octet 6 in Section 1

of BUFR Edition 3

00 000 0 WMO Secretariat

**01--09: WMCs**

01 001 1 Melbourne

02 002 2 Melbourne

03 003 3 )

04 004 4 Moscow

05 005 5 Moscow

06 006 6 )

07 007 7 US National Weather Service -- National Centres

for Environmental Prediction (NCEP)

08 008 8 US National Weather Service Telecommunications Gateway\
(NWSTG)

09 009 9 US National Weather Service -- Other

**10--25: Centres in Region I**

10 010 10 Cairo (RSMC)

11 011 11 )

12 012 12 Dakar (RSMC)

13 013 13 )

14 014 14 Nairobi (RSMC)

15 015 15 )

16 016 16 Casablanca (RSMC)

17 017 17 Tunis (RSMC)

18 018 18 Tunis -- Casablanca (RSMC)

19 019 19 )

20 020 20 Las Palmas

21 021 21 Algiers (RSMC)

22 022 22 ACMAD

23 023 23 Mozambique (NMC)

24 024 24 Pretoria (RSMC)

25 025 25 La Réunion (RSMC)

**26--40: Centres in Region II**

26 026 26 Khabarovsk (RSMC)

27 027 27 )

28 028 28 New Delhi (RSMC)

29 029 29 )

30 030 30 Novosibirsk (RSMC)

31 031 31 )

32 032 32 Tashkent (RSMC)

33 033 33 Jeddah (RSMC)

34 034 34 Tokyo (RSMC), Japan Meteorological Agency

Octet 5 in Section 1

Code figure Code figure of GRIB Edition 1

for F~1~F~2~ for F~3~F~3~F~3~ Octet 6 in Section 1

of BUFR Edition 3

35 035 35 )

36 036 36 Bangkok

37 037 37 Ulaanbaatar

38 038 38 Beijing (RSMC)

39 039 39 )

40 040 40 Seoul

**41--50: Centres in Region III**

41 041 41 Buenos Aires (RSMC)

42 042 42 )

43 043 43 Brasilia (RSMC)

44 044 44 )

45 045 45 Santiago

46 046 46 Brazilian Space Agency ­ INPE

47 047 47 Colombia (NMC)

48 048 48 Ecuador (NMC)

49 049 49 Peru (NMC)

50 050 50 Venezuela (Bolivarian Republic of) (NMC)

**51--63: Centres in Region IV**

51 051 51 Miami (RSMC)

52 052 52 Miami (RSMC), National Hurricane Centre

53 053 53 MSC Monitoring

54 054 54 Montreal (RSMC)

55 055 55 San Francisco

56 056 56 ARINC Centre

57 057 57 US Air Force -- Air Force Global Weather Central

58 058 58 Fleet Numerical Meteorology and Oceanography Center,\
Monterey, CA, United States

59 059 59 The NOAA Forecast Systems Laboratory, Boulder, CO,\
United States

60 060 60 United States National Center for Atmospheric Research\
(NCAR)

61 061 61 Service ARGOS -- Landover

62 062 62 US Naval Oceanographic Office

63 063 63 International Research Institute for Climate and Society (IRI)

**64--73: Centres in Region V**

64 064 64 Honolulu (RSMC)

65 065 65 Darwin (RSMC)

66 066 66 )

67 067 67 Melbourne (RSMC)

68 068 68 Reserved

69 069 69 Wellington (RSMC)

70 070 70 )

71 071 71 Nadi (RSMC)

72 072 72 Singapore

73 073 73 Malaysia (NMC)

*\
*

Octet 5 in Section 1

Code figure Code figure of GRIB Edition 1

for F~1~F~2~ for F~3~F~3~F~3~ Octet 6 in Section 1

of BUFR Edition 3

**74--99: Centres in Region VI**

74 074 74 UK Meteorological Office ­ Exeter (RSMC)

75 075 75 )

76 076 76 Moscow (RSMC)

77 077 77 Reserved

78 078 78 Offenbach (RSMC)

79 079 79 )

80 080 80 Rome (RSMC)

81 081 81 )

82 082 82 Norrköping

83 083 83 )

84 084 84 Toulouse (RSMC)

85 085 85 Toulouse (RSMC)

86 086 86 Helsinki

87 087 87 Belgrade

88 088 88 Oslo

89 089 89 Prague

90 090 90 Episkopi

91 091 91 Ankara

92 092 92 Frankfurt/Main

93 093 93 London (WAFC)

94 094 94 Copenhagen

95 095 95 Rota

96 096 96 Athens

97 097 97 European Space Agency (ESA)

98 098 98 European Centre for Medium-Range Weather Forecasts

(ECMWF) (RSMC)

99 099 99 De Bilt

**Additional Centres**

Not applicable 100 100 Brazzaville

Not applicable 101 101 Abidjan

Not applicable 102 102 Libya (NMC)

Not applicable 103 103 Madagascar (NMC)

Not applicable 104 104 Mauritius (NMC)

Not applicable 105 105 Niger (NMC)

Not applicable 106 106 Seychelles (NMC)

Not applicable 107 107 Uganda (NMC)

Not applicable 108 108 United Republic of Tanzania (NMC)

Not applicable 109 109 Zimbabwe (NMC)

Not applicable 110 110 Hong-Kong, China

Not applicable 111 111 Afghanistan (NMC)

Not applicable 112 112 Bahrain (NMC)

Not applicable 113 113 Bangladesh (NMC)

Not applicable 114 114 Bhutan (NMC)

Not applicable 115 115 Cambodia (NMC)

Not applicable 116 116 Democratic People\'s Republic of Korea (NMC)

**\
**

Octet 5 in Section 1

Code figure Code figure of GRIB Edition 1

for F~1~F~2~ for F~3~F~3~F~3~ Octet 6 in Section 1

of BUFR Edition 3

Not applicable 117 117 Islamic Republic of Iran (NMC)

Not applicable 118 118 Iraq (NMC)

Not applicable 119 119 Kazakhstan (NMC)

Not applicable 120 120 Kuwait (NMC)

Not applicable 121 121 Kyrgyzstan (NMC)

Not applicable 122 122 Lao People\'s Democratic Republic (NMC)

Not applicable 123 123 Macao, China

Not applicable 124 124 Maldives (NMC)

Not applicable 125 125 Myanmar (NMC)

Not applicable 126 126 Nepal (NMC)

Not applicable 127 127 Oman (NMC)

Not applicable 128 128 Pakistan (NMC)

Not applicable 129 129 Qatar (NMC)

Not applicable 130 130 Yemen (NMC)

Not applicable 131 131 Sri Lanka (NMC)

Not applicable 132 132 Tajikistan (NMC)

Not applicable 133 133 Turkmenistan (NMC)

Not applicable 134 134 United Arab Emirates (NMC)

Not applicable 135 135 Uzbekistan (NMC)

Not applicable 136 136 Viet Nam (NMC)

Not applicable 137--139 137--139 Reserved for other centres

Not applicable 140 140 Bolivia (Plurinational State of) (NMC)

Not applicable 141 141 Guyana (NMC)

Not applicable 142 142 Paraguay (NMC)

Not applicable 143 143 Suriname (NMC)

Not applicable 144 144 Uruguay (NMC)

Not applicable 145 145 French Guiana

Not applicable 146 146 Brazilian Navy Hydrographic Centre

Not applicable 147 147 National Commission on Space Activities (CONAE)\
-- Argentina

Not applicable 148--149 148--149 Reserved for other centres

Not applicable 150 150 Antigua and Barbuda (NMC)

Not applicable 151 151 Bahamas (NMC)

Not applicable 152 152 Barbados (NMC)

Not applicable 153 153 Belize (NMC)

Not applicable 154 154 British Caribbean Territories Centre

Not applicable 155 155 San José

Not applicable 156 156 Cuba (NMC)

Not applicable 157 157 Dominica (NMC)

Not applicable 158 158 Dominican Republic (NMC)

Not applicable 159 159 El Salvador (NMC)

Not applicable 160 160 US NOAA/NESDIS

Not applicable 161 161 US NOAA Office of Oceanic and Atmospheric Research

Not applicable 162 162 Guatemala (NMC)

Not applicable 163 163 Haiti (NMC)

Not applicable 164 164 Honduras (NMC)

Not applicable 165 165 Jamaica (NMC)

Not applicable 166 166 Mexico City

**\
**

Octet 5 in Section 1

Code figure Code figure of GRIB Edition 1

for F~1~F~2~ for F~3~F~3~F~3~ Octet 6 in Section 1

of BUFR Edition 3

Not applicable 167 167 Curaçao and Sint Maarten (NMC)

Not applicable 168 168 Nicaragua (NMC)

Not applicable 169 169 Panama (NMC)

Not applicable 170 170 Saint Lucia (NMC)

Not applicable 171 171 Trinidad and Tobago (NMC)

Not applicable 172 172 French Departments in RA IV

Not applicable 173 173 US National Aeronautics and Space Administration (NASA)

Not applicable 174 174 Integrated Science Data Management/Marine **Environmental\
Data Service (ISDM/MEDS)** -- Canada

Not applicable 175 175 University Corporation for Atmospheric Research (UCAR)\
-- United States

Not applicable 176 176 Cooperative Institute for Meteorological Satellite Studies\
(CIMSS) -- United States

Not applicable 177 177 NOAA National Ocean Service -- United States

Not applicable 178 178 Spire Global, Inc.

Not applicable 179--189 179--189 Reserved for other centres

Not applicable 190 190 Cook Islands (NMC)

Not applicable 191 191 French Polynesia (NMC)

Not applicable 192 192 Tonga (NMC)

Not applicable 193 193 Vanuatu (NMC)

Not applicable 194 194 Brunei Darussalam (NMC)

Not applicable 195 195 Indonesia (NMC)

Not applicable 196 196 Kiribati (NMC)

Not applicable 197 197 Federated States of Micronesia (NMC)

Not applicable 198 198 New Caledonia (NMC)

Not applicable 199 199 Niue

Not applicable 200 200 Papua New Guinea (NMC)

Not applicable 201 201 Philippines (NMC)

Not applicable 202 202 Samoa (NMC)

Not applicable 203 203 Solomon Islands (NMC)

Not applicable 204 204 National Institute of Water and Atmospheric Research (NIWA -- New Zealand)

Not applicable 205--209 205--209 Reserved

Not applicable 210 210 Frascati (ESA/ESRIN)

Not applicable 211 211 Lannion

Not applicable 212 212 Lisbon

Not applicable 213 213 Reykjavik

Not applicable 214 214 Madrid

Not applicable 215 215 Zurich

Not applicable 216 216 Service ARGOS -- Toulouse

Not applicable 217 217 Bratislava

Not applicable 218 218 Budapest

Not applicable 219 219 Ljubljana

Not applicable 220 220 Warsaw

Not applicable 221 221 Zagreb

Not applicable 222 222 Albania (NMC)

Not applicable 223 223 Armenia (NMC)

Not applicable 224 224 Austria (NMC)

Octet 5 in Section 1

Code figure Code figure of GRIB Edition 1

for F~1~F~2~ for F~3~F~3~F~3~ Octet 6 in Section 1

of BUFR Edition 3

Not applicable 225 225 Azerbaijan (NMC)

Not applicable 226 226 Belarus (NMC)

Not applicable 227 227 Belgium (NMC)

Not applicable 228 228 Bosnia and Herzegovina (NMC)

Not applicable 229 229 Bulgaria (NMC)

Not applicable 230 230 Cyprus (NMC)

Not applicable 231 231 Estonia (NMC)

Not applicable 232 232 Georgia (NMC)

Not applicable 233 233 Dublin

Not applicable 234 234 Israel (NMC)

Not applicable 235 235 Jordan (NMC)

Not applicable 236 236 Latvia (NMC)

Not applicable 237 237 Lebanon (NMC)

Not applicable 238 238 Lithuania (NMC)

Not applicable 239 239 Luxembourg

Not applicable 240 240 Malta (NMC)

Not applicable 241 241 Monaco

Not applicable 242 242 Romania (NMC)

Not applicable 243 243 Syrian Arab Republic (NMC)

Not applicable 244 244 The former Yugoslav Republic of Macedonia (NMC)

Not applicable 245 245 Ukraine (NMC)

Not applicable 246 246 Republic of Moldova (NMC)

Not applicable 247 247 Operational Programme for the Exchange of weather RAdar\
information (OPERA) -- EUMETNET

Not applicable 248 248 Montenegro (NMC)

Not applicable 249 249 Barcelona Dust Forecast Center

Not applicable 250 250 COnsortium for Small scale MOdelling (COSMO)

Not applicable 251 251 Meteorological Cooperation on Operational NWP

(MetCoOp)

Not applicable 252 252 Max Planck Institute for Meteorology (MPI-M)

Not applicable 253 253 Reserved for other centres

Not applicable 254 254 EUMETSAT Operation Centre

Not applicable 255 255 Missing value

Not applicable 256--999 Not applicable Not used

Notes:

\(1) The closed bracket sign ) indicates that the corresponding code figure is reserved for the previously named centre.

\(2) With GRIB or BUFR, to indicate whether the originating/generating centre is a sub-centre or not, the following procedure should be applied:

In GRIB edition 1, use octet 26 of section 1, or in BUFR edition 3, use octet 5 of section 1, with the following meaning:

Code figure

> 0 Not a sub-centre, the originating/generating centre is the centre defined by Octet 5 in section 1 of GRIB Edition 1, or by octet 6 in section 1 of BUFR edition 3.
>
> 1 to 254 Identifier of the sub-centre which is the originating/generating centre. The identifier of the sub-\
> centre is allocated by the associated centre which is defined by octet 5 in section 1 of GRIB edition 1, or octet 6 in section 1 of BUFR edition 3. The sub-centre identifiers should be supplied to the WMO Secretariat by the associated centre(s) for publication.

\(3) For the definitions of sub-centres provided to the WMO Secretariat, see Common Code table C--12.

**COMMON CODE TABLE C--2: *Radiosonde/sounding system used***

Code table 3685 -- r~a~r~a~ (Radiosonde/sounding system used) -- for alphanumeric codes

Common Code table

Code table 0 02 011 (Radiosonde type) in BUFR

Date of Code figure for Code figure for

assignment of r~a~r~a~ BUFR

number (necessary (Code table (Code table

after 30/06/2007) 3685) 0 02 011)

Not applicable 00 0 Reserved

Before 01 1 iMet-1-BB (United States)

Not applicable 02 2 No radiosonde -- passive target (e.g. reflector)

Not applicable 03 3 No radiosonde -- active target (e.g. transponder)

Not applicable 04 4 No radiosonde -- passive temperature-humidity profiler

Not applicable 05 5 No radiosonde -- active temperature-humidity profiler

Not applicable 06 6 No radiosonde -- radio-acoustic sounder

Before 07 7 iMet-1-AB (United States)

Not applicable 08 8 No radiosonde --\... (reserved)

Not applicable 09 9 No radiosonde -- system unknown or not specified

Before 10 10 VIZ type A pressure-commutated (United States)

Before 11 11 VIZ type B time-commutated (United States)

Before 12 12 RS SDC (Space Data Corporation -- United States)

Before 13 13 Astor (no longer made -- Australia)

Before 14 14 VIZ MARK I MICROSONDE (United States)

Before 15 15 EEC Company type 23 (United States)

Before 16 16 Elin (Austria)

Before 17 17 Graw G. (Germany)

Before 18 18 Graw DFM-06 (Germany)

Before 19 19 Graw M60 (Germany)

Before 20 20 Indian Meteorological Service MK3 (India)

Before 21 21 VIZ/Jin Yang MARK I MICROSONDE (Republic of Korea)

Before 22 22 Meisei RS2-80 (Japan)

Before 23 23 Mesural FMO 1950A (France)

Before 24 24 Mesural FMO 1945A (France)

Before 25 25 Mesural MH73A (France)

Before 26 26 Meteolabor Basora (Switzerland)

Before 27 27 AVK-MRZ (Russian Federation)

Before 28 28 Meteorit MARZ2-1 (Russian Federation)

Before 29 29 Meteorit MARZ2-2 (Russian Federation)

Before 30 30 Oki RS2-80 (Japan)

Before 31 31 VIZ/Valcom type A pressure-commutated (Canada)

Before 32 32 Shanghai Radio (China)

Before 33 33 UK Met Office MK3 (UK)

Before 34 34 Vinohrady (Czechia)

Before 35 35 Vaisala RS18 (Finland)

Before 36 36 Vaisala RS21 (Finland)

Date of Code figure for Code figure for

assignment of r~a~r~a~ BUFR

number (necessary (Code table (Code table

after 30/06/2007) 3685) 0 02 011)

Before 37 37 Vaisala RS80 (Finland)

Before 38 38 VIZ LOCATE Loran-C (United States)

Before 39 39 Sprenger E076 (Germany)

Before 40 40 Sprenger E084 (Germany)

Before 41 41 Sprenger E085 (Germany)

Before 42 42 Sprenger E086 (Germany)

Before 43 43 AIR IS - 4A - 1680 (United States)

Before 44 44 AIR IS - 4A - 1680 X (United States)

Before 45 45 RS MSS (United States)

Before 46 46 AIR IS - 4A - 403 (United States)

Before 47 47 Meisei RS2-91 (Japan)

Before 48 48 VALCOM (Canada)

Before 49 49 VIZ MARK II (United States)

Before 50 50 Graw DFM-90 (Germany)

Before 51 51 VIZ-B2 (United States)

Before 52 52 Vaisala RS80-57H

Before 53 53 AVK-RF95 (Russian Federation)

Before 54 54 Graw DFM-97 (Germany)

Before 55 55 Meisei RS-01G (Japan)

Before 56 56 M2K2 (France)

Before 57 57 Modem M2K2-DC (France)

Before 58 58 AVK-BAR (Russian Federation)

Before 59 59 Modem M2K2-R 1680 MHz RDF radiosonde with pressure\
sensor chip (France)

Before 60 60 Vaisala RS80/MicroCora (Finland)

Before 61 61 Vaisala RS80/Loran/Digicora I, II or Marwin (Finland)

Before 62 62 Vaisala RS80/PCCora (Finland)

Before 63 63 Vaisala RS80/Star (Finland)

Before 64 64 Orbital Sciences Corporation, Space Data Division,\
transponder radiosonde, type 909-11-XX, where XX\
corresponds to the model of the instrument (United States)

Before 65 65 VIZ transponder radiosonde, model number 1499--520 (United\
States)

Before 66 66 Vaisala RS80 /Autosonde (Finland)

Before 67 67 Vaisala RS80/Digicora III (Finland)

Before 68 68 AVK-RZM-2 (Russian Federation)

Before 69 69 MARL-A or Vektor-M-RZM-2 (Russian Federation)

Before 70 70 Vaisala RS92/Star (Finland)

Before 71 71 Vaisala RS90/Loran/Digicora I, II or Marwin (Finland)

Before 72 72 Vaisala RS90/PC-Cora (Finland)

Before 73 73 Vaisala RS90/Autosonde (Finland)

Before 74 74 Vaisala RS90/Star (Finland)

Date of Code figure for Code figure for

assignment of r~a~r~a~ BUFR

number (necessary (Code table (Code table

after 30/06/2007) 3685) 0 02 011)

Before 75 75 AVK-MRZ-ARMA (Russian Federation)

Before 76 76 AVK-RF95-ARMA (Russian Federation)

Before 77 77 GEOLINK GPSonde GL98 (France)

Before 78 78 Vaisala RS90/Digicora III (Finland)

Before 79 79 Vaisala RS92/Digicora I, II or Marwin (Finland)

Before 80 80 Vaisala RS92/Digicora III (Finland)

Before 81 81 Vaisala RS92/Autosonde (Finland)

Before 82 82 Sippican MK2 GPS/STAR (United States) with rod thermistor,\
carbon element and derived pressure

Before 83 83 Sippican MK2 GPS/W9000 (United States) with rod thermistor,\
carbon element and derived pressure

Before 84 84 Sippican MARK II with chip thermistor, carbon element and derived\
pressure from GPS height

Before 85 85 Sippican MARK IIA with chip thermistor, carbon element and\
derived pressure from GPS height

Before 86 86 Sippican MARK II with chip thermistor, pressure and carbon\
element

Before 87 87 Sippican MARK IIA with chip thermistor, pressure and carbon\
element

Before 88 88 MARL-A or Vektor-M-MRZ (Russian Federation)

Before 89 89 MARL-A or Vektor-M-BAR (Russian Federation)

Not applicable 90 90 Radiosonde not specified or unknown

Not applicable 91 91 Pressure only radiosonde

Not applicable 92 92 Pressure only radiosonde plus transponder

Not applicable 93 93 Pressure only radiosonde plus radar reflector

Not applicable 94 94 No pressure radiosonde plus transponder

Not applicable 95 95 No pressure radiosonde plus radar reflector

Not applicable 96 96 Descending radiosonde

Before 97 97 iMet-2/iMet-1500 RDF radiosonde with pressure sensor chip\
(South Africa)

Before 98 98 iMet-2/iMet-1500 GPS radiosonde with derived pressure from\
GPS height (South Africa)

Before 99 99 iMet-2/iMet-3200 GPS radiosonde with derived pressure from\
GPS height (South Africa)

Not available 100 Reserved for BUFR only

01 101 Not vacant

Not available 102--106 Reserved for BUFR only

07 107 Not vacant

Not available 108--109 Reserved for BUFR only

01/01/2008 10 110 Sippican LMS5 w/Chip Thermistor, duct mounted capacitance\
relative humidity sensor and derived pressure from GPS height

01/01/2008 11 111 Sippican LMS6 w/Chip Thermistor, external boom mounted\
capacitance relative humidity sensor, and derived pressure\
from GPS height

06/05/2015 12 112 Jin Yang RSG-20A with derived pressure from GPS\
height/GL-5000P (Republic of Korea)

Date of Code figure for Code figure for

assignment of r~a~r~a~ BUFR

number (necessary (Code table (Code table

after 30/06/2007) 3685) 0 02 011)

15/09/2010 13 113 Vaisala RS92/MARWIN MW32 (Finland)

03/11/2011 14 114 Vaisala RS92/DigiCORA MW41 (Finland)

01/12/2011 15 115 PAZA-12M/Radiotheodolite-UL (Ukraine)

01/12/2011 16 116 PAZA-22/AVK-1 (Ukraine)

02/05/2012 17 117 Graw DFM-09 (Germany)

18 118 Not vacant

Needed 19 119 Vacant

20 120 Not vacant

06/05/2015 21 121 Jin Yang 1524LA LORAN-C/GL5000 (Republic of\
Korea)

02/05/2012 22 122 Meisei RS-11G GPS radiosonde\
w/thermistor, capacitance relative\
humidity sensor, and derived pressure\
from GPS height (Japan)

03/11/2011 23 123 Vaisala RS41/DigiCORA MW41 (Finland)

03/11/2011 24 124 Vaisala RS41/AUTOSONDE (Finland)

03/11/2011 25 125 Vaisala RS41/MARWIN MW32 (Finland)

07/05/2014 26 126 Meteolabor SRS--C34/Argus 37 (Switzerland)

27 127 Not vacant

15/09/2011 28 128 AVK - AK2-02 (Russian Federation)

15/09/2011 29 129 MARL-A or Vektor-M - AK2-02 (Russian Federation)

01/01/2010 30 130 Meisei RS-06G (Japan)

03/11/2011 31 131 Taiyuan GTS1-1/GFE(L) (China )

03/11/2011 32 132 Shanghai GTS1/GFE(L) (China)

03/11/2011 33 133 Nanjing GTS1-2/GFE(L) (China)

Needed 34 134 Vacant

07/05/2014 35 135 Meisei iMS-100 GPS radiosonde w/thermistor sensor, capacitance\
relative humidity sensor, and derived pressure from GPS height\
(Japan)

02/05/2018 36 136 Meisei iMDS-17 GPS dropsonde w/thermistor sensor, capacitance\
relative humidity sensor, and capacitance pressure sensor\
(Japan)

37 137 Not vacant

Needed 38--40 138--140 Vacant

03/11/2011 41 141 Vaisala RS41 with pressure derived from GPS height/\
DigiCORA MW41 (Finland)

03/11/2011 42 142 Vaisala RS41 with pressure derived from GPS height/\
AUTOSONDE (Finland)

07/05/2014 43 143 NanJing Daqiao XGP-3G (China)\*

07/05/2014 44 144 TianJin HuaYunTianYi GTS(U)1 (China)\*

07/05/2014 45 145 Beijing Changfeng CF-06 (China)\*

07/05/2014 46 146 Shanghai Changwang GTS3 (China)\*

\_\_\_\_\_\_\_\_\_\_\_\_

\* All GPS radiosondes are with thermistor, silicon piezoresistive pressure sensor or pressure derived from GPS height, capacitive relative humidity sensor and wind derived from GPS height.

Date of Code figure for Code figure for

assignment of r~a~r~a~ BUFR

number (necessary (Code table (Code table

after 30/06/2007) 3685) 0 02 011)

47 147 Not vacant

02/05/2012 48 148 PAZA-22M/MARL-A

49 149 Not vacant

02/11/2016 50 150 Meteolabor SRS-C50/Argus (Switzerland)

51 151 Not vacant

03/11/2011 52 152 Vaisala RS92-NGP/Intermet IMS-2000 (United States)

06/05/2015 53 153 AVK -- I-2012 (Russian Federation)

54--59 154--159 Not vacant

06/05/2015 60 160 MARL-A or Vektor-M -- I-2012 (Russian Federation)

61 161 Not vacant

06/05/2015 62 162 MARL-A or Vektor-M -- MRZ-3MK (Russian Federation)

07/11/2018 63 163 Modem M20 radiosonde w/thermistor sensor, capacitance\
relative humidity sensor, and derived pressure from GPS\
height (France)

07/11/2018 64 164 Modem PilotSonde GPS radiosonde (France)

Needed 65--66 165--166 Vacant

67--72 167--172 Not vacant

02/11/2016 73 173 МАRL-A (Russian Federation) -- ASPAN-15 (Kazakhstan)

74--76 174--176 Not vacant

15/03/2010 77 177 Modem GPSonde M10 (France)

78--81 178--181 Not vacant

07/11/2012 82 182 Lockheed Martin LMS-6 w/chip\
thermistor; external boom mounted\
polymer capacitive relative humidity sensor;\
capacitive pressure sensor and GPS wind

07/11/2012 83 183 Vaisala RS92-D/Intermet IMS 1500\
w/silicon capacitive pressure sensor,\
capacitive wire temperature sensor, twin\
thin-film heated polymer capacitive relative\
humidity sensor and RDF wind

Needed 84 184 Vacant

85-89 185-189 Not vacant

Not available 190 NCAR research dropsonde NRD94 with GPS and Vaisala\
RS92-based sensor module (United States)

Not available 191 NCAR research dropsonde NRD41 with GPS and Vaisala\
RS41-based sensor module (United States)

Not available 192 Vaisala/NCAR dropsonde RD94 with GPS and Vaisala RS92-based\
sensor module (Finland/United States)

Not available 193 Vaisala/NCAR dropsonde RD41 with GPS and Vaisala RS41-based\
sensor module (Finland/United States)

Not available 194--196 Reserved for BUFR only

97--99 197--199 Not vacant

Not available 200--254 Reserved for BUFR only

255 Missing value

Notes:

\(1) References to countries in brackets indicate the manufacturing location rather than the country using the instrument.

\(2) Some of the radiosondes listed are no longer in use but are retained for archiving purposes.

\(3) The alphanumeric code format reports only 2 digits, and the first digit for BUFR is identified from the date: the first digit is 0 if the introduction of the radiosonde for observation was before 30 June 2007, or 1 otherwise. Entries in the second part of the table (after 99), which are declared "Vacant" can be used for new radiosondes because the 2-digit number was originally attributed to sondes, which are no longer used. This system has been adopted to accommodate reporting in TEMP traditional alphanumeric code format up to the time BUFR is fully used for radiosonding reports.

**COMMON CODE TABLE C--3: *Instrument make and type for water temperature profile measurement with fall rate equation coefficients***

Code table 1770 -- I~X~I~X~I~X~ (Instrument type for XBT, with fall rate equation coefficients)

Common Code table -- for alphanumeric codes

Code table 0 22 067 (Instrument type for water temperature/salinity profile measurement)\
in BUFR

Code figure for Meaning

Code figure BUFR Instrument

for I~X~I~X~I~X~ (Code table 0 22 067) make and type Equation Coefficients

*a* *b*

001 1 Sippican T-4 6.472 --2.16

002 2 Sippican T-4 6.691 --2.25

011 11 Sippican T-5 6.828 --1.82

021 21 Sippican Fast Deep 6.346 --1.82

031 31 Sippican T-6 6.472 --2.16

032 32 Sippican T-6 6.691 --2.25

041 41 Sippican T-7 6.472 --2.16

042 42 Sippican T-7 6.691 --2.25

051 51 Sippican Deep Blue 6.472 --2.16

052 52 Sippican Deep Blue 6.691 --2.25

061 61 Sippican T-10 6.301 --2.16

071 71 Sippican T-11 1.779 --0.255

081 81 Sippican AXBT (300 m probes) 1.52 0.0

201 201 TSK T-4 6.472 --2.16

202 202 TSK T-4 6.691 --2.25

211 211 TSK T-6 6.472 --2.16

212 212 TSK T-6 6.691 --2.25

221 221 TSK T-7 6.472 --2.16

222 222 TSK T-7 6.691 --2.25

231 231 TSK T-5 6.828 --1.82

241 241 TSK T-10 6.301 --2.16

251 251 TSK Deep Blue 6.472 --2.16

252 252 TSK Deep Blue 6.691 --2.25

261 261 TSK AXBT

401 401 Sparton XBT-1 6.301 --2.16

411 411 Sparton XBT-3 5.861 --0.0904

421 421 Sparton XBT-4 6.472 --2.16

431 431 Sparton XBT-5 6.828 --1.82

441 441 Sparton XBT-5DB 6.828 --1.82

451 451 Sparton XBT-6 6.472 --2.16

461 461 Sparton XBT-7 6.472 --2.16

462 462 Sparton XBT-7 6.705 --2.28

471 471 Sparton XBT-7DB 6.472 --2.16

481 481 Sparton XBT-10 6.301 --2.16

491 491 Sparton XBT-20 6.472 --2.16

501 501 Sparton XBT-20DB 6.472 --2.16

510 510 Sparton 536 AXBT 1.524 0

700 700 Sippican XCTD Standard

710 710 Sippican XCTD Deep

720 720 Sippican AXCTD

730 730 Sippican SXCTD

Code figure for Meaning

Code figure BUFR Instrument

for I~X~I~X~I~X~ (Code table 0 22 067) make and type Equation Coefficients

*a* *b*

741 741 TSK XCTD/XCTD-1 3.42543 --0.47

742 742 TSK XCTD-2 3.43898 --0.31

743 743 TSK XCTD-2F 3.43898 --0.31

744 744 TSK XCTD-3 5.07598 --0.72

745 745 TSK XCTD-4 3.68081 --0.47

751 751 TSK AXCTD

780 780 Sea-Bird SBE21 SEACAT Not applicable\
Thermosalinograph

781 781 Sea-Bird SBE45 MicroTSG Not applicable\
Thermosalinograph

800 800 Mechanical BT Not applicable

810 810 Hydrocast Not applicable

820 820 Thermistor chain Not applicable

825 825 Temperature (sonic) and pressure Not applicable\
probes

830 830 CTD Not applicable

831 831 CTD-P-ALACE float Not applicable

835 835 PROVOR-IV Not applicable

836 836 PROVOR-III Not applicable

837 837 ARVOR\_C, SBE conductivity sensor

838 838 ARVOR\_D, SBE conductivity sensor

839 839 PROVOR--II, SBE conductivity sensor

840 840 PROVOR, no conductivity sensor Not applicable

841 841 PROVOR, Sea-Bird conductivity Not applicable

sensor

842 842 PROVOR, FSI conductivity sensor Not applicable

843 843 Polar Ocean Profiling System

(POPS), PROVOR, SBE CTD

844 844 Profiling float, ARVOR, Sea-Bird

conductivity sensor

845 845 Webb Research, no conductivity Not applicable

sensor

846 846 Webb Research, Sea-Bird Not applicable

conductivity sensor

847 847 Webb Research, FSI conductivity Not applicable

sensor

848 848 APEX--EM, SBE conductivity sensor

849 849 APEX\_D, SBE conductivity sensor

850 850 SOLO, no conductivity sensor Not applicable

851 851 SOLO, Sea-Bird conductivity Not applicable

sensor

852 852 SOLO, FSI conductivity sensor Not applicable

853 853 Profiling float, SOLO2 (SCRIPPS),

Sea-Bird conductivity sensor

854 854 S2A, SBE conductivity sensor

855 855 Profiling float, NINJA, no Not applicable

conductivity sensor

856 856 Profiling float, NINJA, SBE Not applicable

conductivity sensor

Code figure for Meaning

Code figure BUFR Instrument

for I~X~I~X~I~X~ (Code table 0 22 067) make and type Equation Coefficients

*a* *b*

857 857 Profiling float, NINJA, FSI Not applicable

conductivity sensor

858 858 Profiling float, NINJA, TSK Not applicable

conductivity sensor

859 859 Profiling float, NEMO, no Not applicable

conductivity sensor

860 860 Profiling float, NEMO, SBE Not applicable

conductivity sensor

861 861 Profiling float, NEMO, FSI Not applicable

conductivity sensor

862 862 SOLO\_D, SBE conductivity sensor

863 863 NAVIS--A, SBE conductivity sensor

864 864 NINJA\_D, SBE conductivity sensor

865 865 NOVA, SBE conductivity sensor

866 866 ALAMO, no conductivity sensor

867 867 ALAMO, RBR conductivity sensor

868 868 ALAMO, SBE conductivity sensor

869 869 Reserved

870 870 HM2000 Not applicable

871 871 COPEX Not applicable

872 872 S2X Not applicable

873 873 ALTO Not applicable

874 874 SOLO\_D\_MRV Not applicable

875--899 875--899 Reserved

900 900 Sippican LMP-5 XBT 9.727 --0.0000473

901 901 Ice-tethered Profiler (ITP),\
SBE CTD

902 902 Brooke Ocean Moving Vessel Profiler (MVP)

903 903 Sea-Bird CTD

904 904 AML Oceanographic CTD

905 905 Falmouth Scientific CTD

906 906 Ocean Sensors CTD

907 907 Valeport CTD

908 908 Oceanscience MVP

909 909 IDRONAUT CTD

910 910 Sea-Bird SBE 38

911--994 911--994 Reserved

995 995 Instrument attached to Not applicable

marine mammals

996 996 Instrument attached to animals Not applicable

other than marine mammals

997--999 997--999 Reserved

1000--1022 Reserved

1023 Missing value

Notes:

\(1) The depth is calculated from coefficients *a* and *b* and the time *t* as follows: z = *at* + 10^--3^ *bt*^2^

\(2) All unassigned numbers are reserved for future use.

\(3) The values of *a* and *b* are supplied for information only.

**COMMON CODE TABLE C--4: *Water temperature profile recorder types***

Code table 4770 -- X~R~X~R~ (Recorder type) -- for alphanumeric codes

Common Code table

Code table 0 22 068 (Water temperature profile recorder types) in BUFR

Code figure for

Code figure for BUFR

X~R~X~R~ (Code table 0 22 068) Meaning

01 1 Sippican Strip Chart Recorder

02 2 Sippican MK2A/SSQ-61

03 3 Sippican MK-9

04 4 Sippican AN/BHQ-7/MK8

05 5 Sippican MK-12

06 6 Sippican MK-21

07 7 Sippican MK-8 Linear Recorder

08 8 Sippican MK-10

10 10 Sparton SOC BT/SV Processor Model 100

11 11 Lockheed-Sanders Model OL5005

20 20 ARGOS XBT-ST

21 21 CLS-ARGOS/Protecno XBT-ST Model-1

22 22 CLS-ARGOS/Protecno XBT-ST Model-2

30 30 BATHY Systems SA-810

31 31 Scripps Metrobyte Controller

32 32 Murayama Denki Z-60-16 III

33 33 Murayama Denki Z-60-16 II

34 34 Protecno ETSM2

35 35 Nautilus Marine Service NMS-XBT

40 40 TSK MK-2A

41 41 TSK MK-2S

42 42 TSK MK-30

43 43 TSK MK-30N

45 45 TSK MK-100

46 46 TSK MK-130 Compatible recorder for both XBT and XCTD

47 47 TSK MK-130A XCTD recorder

48 48 TSK AXBT RECEIVER MK-300

49 49 TSK MK-150/MK-150N Compatible recorder for both XBT and XCTD

50 50 JMA ASTOS

60 60 ARGOS communications, sampling on up transit

61 61 ARGOS communications, sampling on down transit

62 62 Orbcomm communications, sampling on up transit

63 63 Orbcomm communications, sampling on down transit

64 64 Iridium communications, sampling on up transit

65 65 Iridium communications, sampling on down transit

70 70 CSIRO Devil-1 XBT acquisition system

71 71 CSIRO Devil-2 XBT acquisition system

72 72 TURO/CSIRO Quoll XBT acquisition system

80 80 Applied Microsystems Ltd., MICRO-SVT&P

81 81 Sea Mammal Research Unit, Univ. St. Andrews, UK,

uncorrected salinity from a sea mammal mounted instrument

82 82 Sea Mammal Research Unit, Univ. St. Andrews, UK, corrected

salinity from a sea mammal mounted instrument

99 99 Unknown

127 Missing value

Note: All unassigned numbers are reserved for future use.

**COMMON CODE TABLE C--5: *Satellite identifier***

I~6~I~6~I~6~ for alphanumeric codes

Common Code table Code table 0 01 007 in BUFR

Code used in GRIB Edition 2

*(EVEN DECILES INDICATE POLAR-ORBITING SATELLITES AND ODD DECILES INDICATE GEOSTATION-\
ARY SATELLITES.)*

Code figure for Code figure for

Code figure for BUFR GRIB

I~6~I~6~I~6~ (Code table 0 01 007) Edition 2

000 0 0 Reserved

**001--099: Numbers allocated to Europe**

001 1 1 ERS 1

002 2 2 ERS 2

003 3 3 METOP-1 (Metop-B)

004 4 4 METOP-2 (Metop-A)

005 5 5 METOP-3 (Metop-C)

020 20 20 SPOT1

021 21 21 SPOT2

022 22 22 SPOT3

023 23 23 SPOT4

040 40 40 OERSTED

041 41 41 CHAMP

042 42 42 TerraSAR-X

043 43 43 TanDEM-X

044 44 44 PAZ

046 46 46 SMOS

047 47 47 CryoSat-2

048 48 48 AEOLUS

050 50 50 METEOSAT 3

051 51 51 METEOSAT 4

052 52 52 METEOSAT 5

053 53 53 METEOSAT 6

054 54 54 METEOSAT 7

055 55 55 METEOSAT 8

056 56 56 METEOSAT 9

057 57 57 METEOSAT 10

058 58 58 METEOSAT 1

059 59 59 METEOSAT 2

060 60 60 ENVISAT

061 61 61 Sentinel 3A

062 62 62 Sentinel 1A

063 63 63 Sentinel 1B

064 64 64 Sentinel 5P

065 65 65 Sentinel 3B

070 70 70 METEOSAT 11

**100--199: Numbers allocated to Japan**

120 120 120 ADEOS

121 121 121 ADEOS II

122 122 122 GCOM-W1

Code figure for Code figure for

Code figure for BUFR GRIB

I~6~I~6~I~6~ (Code table 0 01 007) Edition 2

140 140 140 GOSAT

150 150 150 GMS 3

151 151 151 GMS 4

152 152 152 GMS 5

153 153 153 GMS

154 154 154 GMS 2

171 171 171 MTSAT-1R

172 172 172 MTSAT-2

173 173 173 Himawari-8

174 174 174 Himawari-9

**200--299: Numbers allocated to the United States**

200 200 200 NOAA 8

201 201 201 NOAA 9

202 202 202 NOAA 10

203 203 203 NOAA 11

204 204 204 NOAA 12

205 205 205 NOAA 14

206 206 206 NOAA 15

207 207 207 NOAA 16

208 208 208 NOAA 17

209 209 209 NOAA 18

220 220 220 LANDSAT 5

221 221 221 LANDSAT 4

222 222 222 LANDSAT 7

223 223 223 NOAA 19

224 224 224 NPP

225 225 225 NOAA 20

226 226 226 NOAA 21

240 240 240 DMSP 7

241 241 241 DMSP 8

242 242 242 DMSP 9

243 243 243 DMSP 10

244 244 244 DMSP 11

245 245 245 DMSP 12

246 246 246 DMSP 13

247 247 247 DMSP 14

248 248 248 DMSP 15

249 249 249 DMSP 16

250 250 250 GOES 6

251 251 251 GOES 7

252 252 252 GOES 8

253 253 253 GOES 9

254 254 254 GOES 10

Code figure for Code figure for

Code figure for BUFR GRIB

I~6~I~6~I~6~ (Code table 0 01 007) Edition 2

255 255 255 GOES 11

256 256 256 GOES 12

257 257 257 GOES 13

258 258 258 GOES 14

259 259 259 GOES 15

260 260 260 JASON 1

261 261 261 JASON 2

262 262 262 JASON 3

269 269 269 Spire Lemur 3U CubeSat

270 270 270 GOES 16

271 271 271 GOES 17

272 272 272 GOES 18

273 273 273 GOES 19

281 281 281 QUIKSCAT

282 282 282 TRMM

283 283 283 CORIOLIS

285 285 285 DMSP 17

286 286 286 DMSP 18

287 287 287 DMSP 19

288 288 288 GPM-core

289 289 289 Orbiting Carbon Observatory -- 2 

(OCO-2, NASA)

**300--399: Numbers allocated to the Russian Federation**

310 310 310 GOMS 1

311 311 311 GOMS 2

320 320 320 METEOR 2-21

321 321 321 METEOR 3-5

322 322 322 METEOR 3M-1

323 323 323 METEOR 3M-2

341 341 341 RESURS 01-4

**400--499: Numbers allocated to India**

410 410 410 KALPANA-1

421 421 421 Oceansat-2

422 422 422 **ScatSat-1**

423 423 423 Oceansat-3

430 430 430 INSAT 1B

431 431 431 INSAT 1C

432 432 432 INSAT 1D

440 440 440 Megha-Tropiques

Code figure for Code figure for

Code figure for BUFR GRIB

I~6~I~6~I~6~ (Code table 0 01 007) Edition 2

441 441 441 SARAL

450 450 450 INSAT 2A

451 451 451 INSAT 2B

452 452 452 INSAT 2E

470 470 470 INSAT 3A

471 471 471 INSAT 3D

472 472 472 INSAT 3E

473 473 473 INSAT 3DR

474 474 474 INSAT 3DS

**500--599: Numbers allocated to China**

500 500 500 FY-1C

501 501 501 FY-1D

502 502 502 Hai Yang 2A (HY-2A, SOA/NSOAS China)

503 503 503 Hai Yang 2B (HY-2B, SOA/NSOAS China)

510 510 510 FY-2

512 512 512 FY-2B

513 513 513 FY-2C

514 514 514 FY-2D

515 515 515 FY-2E

516 516 516 FY-2F

517 517 517 FY-2G

520 520 520 FY-3A

521 521 521 FY-3B

522 522 522 FY-3C

523 523 523 FY-3D

530 530 530 FY-4A

**600--699: Numbers allocated to Europe**

**700--799: Numbers allocated to the United States**

700 700 700 TIROS M (ITOS 1)

701 701 701 NOAA 1

702 702 702 NOAA 2

703 703 703 NOAA 3

704 704 704 NOAA 4

705 705 705 NOAA 5

706 706 706 NOAA 6

707 707 707 NOAA 7

708 708 708 TIROS-N

710 710 710 GOES (SMS 1)

711 711 711 GOES (SMS 2)

Code figure for Code figure for

Code figure for BUFR GRIB

I~6~I~6~I~6~ (Code table 0 01 007) Edition 2

720 720 720 TOPEX

721 721 721 GFO (GEOSAT follow on)

722 722 722 GRACE A

723 723 723 GRACE B

724 724 724 COSMIC-2 P1

725 725 725 COSMIC-2 P2

726 726 726 COSMIC-2 P3

727 727 727 COSMIC-2 P4

728 728 728 COSMIC-2 P5

729 729 729 COSMIC-2 P6

731 731 731 GOES 1

732 732 732 GOES 2

733 733 733 GOES 3

734 734 734 GOES 4

735 735 735 GOES 5

740 740 740 COSMIC-1

741 741 741 COSMIC-2

742 742 742 COSMIC-3

743 743 743 COSMIC-4

744 744 744 COSMIC-5

745 745 745 COSMIC-6

750 750 750 COSMIC-2 E1

751 751 751 COSMIC-2 E2

752 752 752 COSMIC-2 E3

753 753 753 COSMIC-2 E4

754 754 754 COSMIC-2 E5

755 755 755 COSMIC-2 E6

763 763 763 NIMBUS 3

764 764 764 NIMBUS 4

765 765 765 NIMBUS 5

766 766 766 NIMBUS 6

767 767 767 NIMBUS 7

780 780 780 ERBS

781 781 781 UARS

782 782 782 EARTH PROBE

783 783 783 TERRA

784 784 784 AQUA

785 785 785 AURA

786 786 786 C/NOFS

787 787 787 CALIPSO

788 788 788 CloudSat

**800--849 Numbers allocated to other satellite operators**

800 800 800 SUNSAT

801 801 801 International Space Station (ISS)

802 802 802 CFOSAT

Code figure for Code figure for

Code figure for BUFR GRIB

I~6~I~6~I~6~ (Code table 0 01 007) Edition 2

803 803 803 GRACE C (GRACE-FO)

804 804 804 GRACE D (GRACE-FO)

810 810 810 COMS-1

811 811 811 COMS-2

812 812 812 SCISAT-1

813 813 813 ODIN

820 820 820 SAC-C

821 821 821 SAC-D

825 825 825 KOMPSAT-5

850 850 850 Combination of TERRA and AQUA

851 851 851 Combination of NOAA 16 to NOAA 19

852 852 852 Combination of Metop-1 to Metop-3

853 853 853 Combination of METEOSAT and DMSP

854 854 854 Non-specific mixture of geostationary and low

Earth-orbiting satellites

855 855 855 Combination of INSAT 3D and INSAT 3DR

870--998 870--998 870--998 Reserved

999 Missing value 999--1022 999--65534 Reserved

1023 65535 Missing value

Note: Within the ranges 000 to 849 and 870 to 998, even deciles indicate polar orbiting satellites and odd deciles indicate geostationary satellites. The range from 850 to 869 shall be used to indicate combinations of satellites, so the aforementioned decile rule does not apply to values in this range.

**COMMON CODE TABLE C--6: *List of units for TDCFs***

+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| **Code figure** |                                                      | **Conventional abbreviation** | **Abbreviation in IA5/ASCII (5)** | **Abbreviation\ | **Definition in\         |
|                 |                                                      |                               |                                   | in ITA2 (5)**   | base units (2)**         |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
|                 | **Base SI units (1)**                                |                               |                                   |                 |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 001             | metre                                                | m                             | m                                 | M               |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 002             | kilogram                                             | kg                            | kg                                | KG              |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 003             | second                                               | s                             | s                                 | S               |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 004             | ampere                                               | A                             | A                                 | A               |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 005             | kelvin                                               | K                             | K                                 | K               |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 006             | mole                                                 | mol                           | mol                               | MOL             |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 007             | candela                                              | cd                            | cd                                | CD              |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
|                 | **Supplementary SI Units (1)**                       |                               |                                   |                 |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 021             | radian                                               | rad                           | rad                               | RAD             |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 022             | steradian                                            | sr                            | sr                                | SR              |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
|                 | **Derived SI Units with special names (1)**          |                               |                                   |                 |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 030             | hertz                                                | Hz                            | Hz                                | HZ              | s^--1^                   |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 031             | newton                                               | N                             | N                                 | N               | kg m s^--2^              |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 032             | pascal                                               | Pa                            | Pa                                | PAL             | kg m^--1^ s^--2^         |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 033             | joule                                                | J                             | J                                 | J               | kg m^2^ s^--2^           |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 034             | watt                                                 | W                             | W                                 | W               | kg m^2^ s^--3^           |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 035             | coulomb                                              | C                             | C                                 | C               | A s                      |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 036             | volt                                                 | V                             | V                                 | V               | kg m^2^ s^--3^ A^--1^    |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 037             | farad                                                | F                             | F                                 | F               | kg^--1^ m^--2^ s^4^ A^2^ |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 038             | ohm                                                  | Ω                             | Ohm                               | OHM             | kg m^2^ s^--3^ A^--2^    |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 039             | siemens                                              | S                             | S                                 | SIE             | kg^--1^ m^--2^ s^3^ A^2^ |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 040             | weber                                                | Wb                            | Wb                                | WB              | kg m^2^ s^--2^ A^--1^    |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 041             | tesla                                                | T                             | T                                 | T               | kg s^--2^ A^--1^         |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 042             | henry                                                | H                             | H                                 | H               | kg m^2^ s^--2^ A^--2^    |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 060             | degree Celsius                                       | °C                            | Cel                               | CEL             | K+273.15                 |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 070             | lumen                                                | lm                            | lm                                | LM              | cd sr                    |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 071             | lux                                                  | lx                            | lx                                | LX              | cd sr m^--2^             |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 080             | becquerel                                            | Bq                            | Bq                                | BQ              | s^--1^                   |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 081             | grey                                                 | Gy                            | Gy                                | GY              | m^2^ s^--2^              |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 082             | sievert                                              | Sv                            | Sv                                | SV              | m^2^ s^--2^              |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
|                 | **SI Unit prefixes (1) (3) (4)**                     |                               |                                   |                 |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| no              | (yotta)                                              | (Y)                           | (Y)                               | (Y)             |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| no              | (zetta)                                              | (Z)                           | (Z)                               | (Z)             |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| no              | exa                                                  | E                             | E                                 | E               |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| no              | peta                                                 | P                             | P                                 | PE              |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| no              | tera                                                 | T                             | T                                 | T               |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| no              | giga                                                 | G                             | G                                 | G               |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| no              | mega                                                 | M                             | M                                 | MA              |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| no              | kilo                                                 | k                             | k                                 | K               |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| no              | hecto                                                | h                             | h                                 | H               |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| no              | deca                                                 | da                            | da                                | DA              |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| no              | deci                                                 | d                             | d                                 | D               |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| no              | centi                                                | c                             | c                                 | C               |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| no              | milli                                                | m                             | m                                 | M               |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| no              | micro                                                | μ                             | u                                 | U               |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| **Code figure** |                                                      | **Conventional abbreviation** | **Abbreviation in IA5/ASCII (5)** | **Abbreviation\ | **Definition in\         |
|                 |                                                      |                               |                                   | in ITA2 (5)**   | base units (2)**         |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| no              | nano                                                 | n                             | n                                 | N               |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| no              | pico                                                 | p                             | p                                 | P               |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| no              | femto                                                | f                             | f                                 | F               |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| no              | atto                                                 | a                             | a                                 | A               |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| no              | (zepto)                                              | (z)                           | (z)                               |                 |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| no              | (yocto)                                              | (y)                           | (y)                               |                 |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
|                 | **Other, non-SI, units recognized by CGPM (4)**      |                               |                                   |                 |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 110             | degree (angle)                                       | °                             | deg                               | DEG             |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 111             | minute (angle)                                       | \'                            | \'                                | MNT             |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 112             | second (angle)                                       | \"                            | \"                                | SEC             |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 120             | litre                                                | l or L                        | l or L                            | L               |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 130             | minute (time)                                        | min                           | min                               | MIN             |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 131             | hour                                                 | h                             | h                                 | HR              |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 132             | day                                                  | d                             | d                                 | D               |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 150             | tonne                                                | t                             | t                                 | TNE             |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 160             | electron volt                                        | eV                            | eV                                | EV              |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 161             | atomic mass unit                                     | u                             | u                                 | U               |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 170             | astronomic unit                                      | AU                            | AU                                | ASU             |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 171             | parsec                                               | pc                            | pc                                | PRS             |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
|                 | **Non-SI Units tolerated because of widespread use** |                               |                                   |                 |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 200             | nautical mile                                        |                               |                                   |                 |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 201             | knot                                                 | kt                            | kt                                | KT              |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 210             | decibel (6)                                          | dB                            | dB                                | DB              |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 220             | hectare                                              | ha                            | ha                                | HAR             |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 230             | week                                                 |                               |                                   |                 |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 231             | year                                                 | a                             | a                                 | ANN             |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
|                 | **Other Units as used by WMO (7)**                   |                               |                                   |                 |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 300             | per cent                                             | \%                            | \%                                | PERCENT         |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 301             | parts per thousand                                   | ‰                             | 0/00                              | PERTHOU         |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 310             | eighths of cloud                                     | okta                          | okta                              | OKTA            |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 320             | degrees true                                         | °                             | deg                               | DEG             |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 321             | degrees per second                                   | degree/s                      | deg/s                             | DEG/S           |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 350             | degrees Celsius (8)                                  | °C                            | C                                 | C               |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 351             | degrees Celsius per metre                            | °C/m                          | C/m                               | C/M             |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 352             | degrees Celsius per 100 metres                       | °C/100 m                      | C/100 m                           | C/100 M         |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 360             | Dobson Unit (9)                                      | DU                            | DU                                | DU              |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 430             | month                                                | mon                           | mon                               | MON             |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 441             | per second (same as hertz)                           | s^--1^                        | /s                                | /S              |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 442             | per second squared                                   | s^--2^                        | s--2                              |                 |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 501             | knots per 1000 metres                                | kt/1000 m                     | kt/km                             | KT/KM           |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 510             | foot                                                 | ft                            | ft                                | FT              |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 511             | inch                                                 | in                            | in                                | IN              |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 520             | decipascals per second                               | dPa s^--1^                    | dPa/s                             | DPAL/S          |                          |
|                 |                                                      |                               |                                   |                 |                          |
|                 | (microbar per second)                                |                               |                                   |                 |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 521             | centibars per second                                 | cb s^--1^                     | cb/s                              | CB/S            |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 522             | centibars per 12 hours                               | cb/12 h                       | cb/12 h                           | CB/12 HR        |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 523             | dekapascal                                           | daPa                          | daPa                              | DAPAL           |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| **Code figure** |                                                      | **Conventional abbreviation** | **Abbreviation in IA5/ASCII (5)** | **Abbreviation\ | **Definition in\         |
|                 |                                                      |                               |                                   | in ITA2 (5)**   | base units (2)**         |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 530             | hectopascal                                          | hPa                           | hPa                               | HPAL            |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 531             | hectopascals per second                              | hPa s^--1^                    | hPa/s                             | HPAL/S          |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 532             | hectopascals per hour                                | hPa h^--1^                    | hPa/h                             | HPAL/HR         |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 533             | hectopascals per 3 hours                             | hPa/3 h                       | hPa/3 h                           | HPAL/3 HR       |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 535             | nanobar = hPa 10^--6^                                | nbar                          | nbar                              | NBAR            |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 620             | grams per kilogram                                   | g kg^--1^                     | g/kg                              | G/KG            |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 621             | grams per kilogram per second                        | g kg^--1^ s^--1^              | g kg--1 s--1                      |                 |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 622             | kilograms per kilogram                               | kg kg^--1^                    | kg/kg                             | KG/KG           |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 623             | kilograms per kilogram per second                    | kg kg^--1^ s^--1^             | kg kg--1 s--1                     |                 |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 624             | kilograms per square metre                           | kg m^--2^                     | kg m--2                           |                 |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 630             | acceleration due to gravity                          | g                             | g                                 |                 |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 631             | geopotential metre                                   | gpm                           | gpm                               |                 |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 710             | millimetre                                           | mm                            | mm                                | MM              |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 711             | millimetres per second                               | mm s^--1^                     | mm/s                              | MM/S            |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 712             | millimetres per hour                                 | mm h^--1^                     | mm/h                              | MM/HR           |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 713             | millimetres to the sixth power per cubic metre       | mm^6^ m^--3^                  | mm6 m--3                          |                 |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 715             | centimetre                                           | cm                            | cm                                | CM              |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 716             | centimetres per second                               | cm s^--1^                     | cm/s                              | CM/S            |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 717             | centimetres per hour                                 | cm h^--1^                     | cm/h                              | CM/HR           |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 720             | decimetre                                            | dm                            | dm                                | DM              |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 731             | metres per second                                    | m s^--1^                      | m/s                               | M/S             |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 732             | metres per second per metre                          | m s^--1^/m                    | m s--1/m                          |                 |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 733             | metres per second per 1000 metres                    | m s^--1^/1000 m               | m s--1/km                         |                 |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 734             | square metres                                        | m^2^                          | m2                                | M2              |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 735             | square metres per second                             | m^2^ s^--1^                   | m2/s                              | M2/S            |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 740             | kilometre                                            | km                            | km                                | KM              |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 741             | kilometres per hour                                  | km h^--1^                     | km/h                              | KM/HR           |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 742             | kilometres per day                                   | km/d                          | km/d                              | KM/D            |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 743             | per metre                                            | m^--1^                        | m--1                              | /M              |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 750             | becquerels per litre                                 | Bq l^--1^                     | Bq/l                              | BQ/L            |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 751             | becquerels per square metre                          | Bq m^--2^                     | Bq m--2                           | BQ/M2           |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 752             | becquerels per cubic metre                           | Bq m^--3^                     | Bq m--3                           | BQ/M3           |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 753             | millisievert                                         | mSv                           | mSv                               | MSV             |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 760             | metres per second squared                            | m s^--2^                      | m s--2                            |                 |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 761             | square metres second                                 | m^2^ s                        | m2 s                              |                 |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 762             | square metres per second squared                     | m^2^ s^--2^                   | m2 s--2                           |                 |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 763             | square metres per radian second                      | m^2^ rad^--1^ s               | m2 rad--1 s                       |                 |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 764             | square metres per hertz                              | m^2^ Hz^--1^                  | m2/Hz                             |                 |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 765             | cubic metres                                         | m^3^                          | m3                                |                 |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 766             | cubic metres per second                              | m^3^ s^--1^                   | m3/s                              |                 |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 767             | cubic metres per cubic metre                         | m^3^ m^--3^                   | m3 m--3                           |                 |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 768             | metres to the fourth power                           | m^4^                          | m4                                |                 |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 769             | metres to the two thirds power per second            | m^2/3^ s^--1^                 | m2/3 s--1                         |                 |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 772             | logarithm per metre                                  | log (m^--1^)                  | log (m--1)                        |                 |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 773             | logarithm per square metre                           | log (m^--2^)                  | log (m--2)                        |                 |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+
| 775             | kilograms per metre                                  | kg m^--1^                     | kg/m                              |                 |                          |
+-----------------+------------------------------------------------------+-------------------------------+-----------------------------------+-----------------+--------------------------+

  ----------------- ------------------------------------------------- ------------------------------- ----------------------------------- ----------------- ------------------
  **Code figure**                                                     **Conventional abbreviation**   **Abbreviation in IA5/ASCII (5)**   **Abbreviation\   **Definition in\
                                                                                                                                          in ITA2 (5)**     base units (2)**

  776               kilograms per square metre per second             kg m^--2^ s^--1^                kg m--2 s--1                                          

  777               kilograms per cubic metre                         kg m^--3^                       kg m--3                                               

  778               per square kilogram per second                    kg^--2^ s^--1^                  kg--2 s--1                                            

  779               seconds per metre                                 s m^--1^                        s/m                                                   

  785               kelvin metres per second                          K m s^--1^                      K m s--1                                              

  786               kelvins per metre                                 K m^--1^                        K/m                                                   

  787               kelvin square metres per kilogram\                K m^2^ kg^--1^ s^--1^           K m2 kg--1 s--1                                       
                    per second                                                                                                                              

  788               moles per mole                                    mol mol^--1^                    mol/mol                                               

  790               radians per metre                                 rad m^--1^                      rad/m                                                 

  795               newtons per square metre                          N m^--2^                        N m--2                                                

  800               pascals per second                                Pa s^--1^                       Pa/s                                                  

  801               kilopascal                                        kPa                             kPa                                                   

  805               joules per square metre                           J m^--2^                        J m--2                                                

  806               joules per kilogram                               J kg^--1^                       J/kg                                                  

  810               watts per metre per steradian                     W m^--1^ sr^--1^                W m--1 sr--1                                          

  811               watts per square metre                            W m^--2^                        W m--2                                                

  812               watts per square metre per steradian              W m^--2^ sr^--1^                W m--2 sr--1                                          

  813               watts per square metre per steradian centimetre   W m^--2^ sr^--1^ cm             W m--2 sr--1 cm                                       

  814               watts per square metre per steradian metre        W m^--2^ sr^--1^ m              W m--2 sr--1 m                                        

  815               watts per cubic metre per steradian               W m^--3^ sr^--1^                W m--3 sr--1                                          

  820               siemens per metre                                 S m^--1^                        S/m                                                   

  825               square degrees                                    degree^2^                       deg2                                                  

  830               becquerel seconds per cubic metre                 Bq s m^--3^                     Bq s m--3                                             

  835               decibels per metre                                dB m^--1^                       dB/m                                                  

  836               decibels per degree                               dB degree^--1^                  dB/deg                                                

  841               pH unit                                           pH unit                         pH unit                                               

  842               N units                                           N units                         N units                                               

  843               Nephelometric turbidity units                     NTU                             NTU                                                   
  ----------------- ------------------------------------------------- ------------------------------- ----------------------------------- ----------------- ------------------

Notes:

\(1) The international system of units, *Système International d\'Unités* (SI), was established by the eleventh General Conference on Weights and Measures in 1960, and extended at the 1980 Conference. There are seven base units, two dimensionless supplementary units and a set of prefixes for decimal scaling. These may be combined to give compound units. Some compound units have special names, and are called derived Units.

\(2) When documenting compound SI units, each symbol for each base unit has been separated from the others by a space. There is no space between the unit and any prefix or exponent. Any prefix establishes a new unit to which any exponent applies (e.g. km^2 ^ = (km)^2^ = m^6^ not k(m^2^) = m^5^). Prefixes must be in the case specified. The full name of the unit must not start with an upper case letter. If the solidus (/) is used, there must be only one. There is no space before or after it.

\(3) Prefixes beyond exa and atto have been proposed but not yet adopted. Use of the prefixes hecto, deca, deci and centi is discouraged.

\(4) Prefixes generally should not be used with units having non-decimal multiples and sub-multiples, such as units of time and angle, or with knots and nautical miles.

\(5) Non-WMO abbreviations with limited character sets taken from ISO 2955-1983. Other abbreviations try to be consistent with this.

\(6) The decibel is one tenth of a bel, which is the decimal logarithm of a ratio of two powers. Frequently, suffixes are supplied to indicate information about one of the quantities in the ratio, such as dB(mW), dBm, dBZ, dBW, dBmW, dB(μV/m). It is recommended that only dB is used, with the full meaning of the ratio explained, including reference levels.

\(7) This list consists of the units not mentioned previously that occur in existing WMO Manuals.

\(8) The abbreviation for degrees Celsius proposed for WMO use, C, could be confused with Coulombs. In this case, Amperes second should be used instead.

\(9) Dobson Unit = DU. One Dobson Unit corresponds to a layer of 0.01 mm of pure ozone, if the whole column of atmosphere were compressed at P = 1013 hPa and T = 0 °C.

**COMMON CODE TABLE C--7: *Tracking technique/status of system used***

Code table 3872 -- s~a~s~a~ for alphanumeric codes

Common Code table

Code table 0 02 014 in BUFR

Code figure for

Code figure for BUFR

s~a~s~a~ (Code table 0 02 014)

00 0 No wind finding

01 1 Automatic with auxiliary optical direction finding

02 2 Automatic with auxiliary radio direction finding

03 3 Automatic with auxiliary ranging

04 4 Not used

05 5 Automatic with multiple VLF-Omega signals

06 6 Automatic cross chain Loran-C

07 7 Automatic with auxiliary wind profiler

08 8 Automatic satellite navigation

09--18 9--18 Reserved

19 19 Tracking technique not specified

TRACKING TECHNIQUES/STATUS OF ASAP SYSTEM

STATUS OF SHIP SYSTEM

20 20 Vessel stopped

21 21 Vessel diverted from original destination

22 22 Vessel\'s arrival delayed

23 23 Container damaged

24 24 Power failure to container

25--28 25--28 Reserved for future use

29 29 Other problems

SOUNDING SYSTEM

30 30 Major power problems

31 31 UPS inoperative

32 32 Receiver hardware problems

33 33 Receiver software problems

34 34 Processor hardware problems

35 35 Processor software problems

36 36 NAVAID system damaged

37 37 Shortage of lifting gas

38 38 Reserved

39 39 Other problems

LAUNCH FACILITIES

40 40 Mechanical defect

41 41 Material defect (hand launcher)

42 42 Power failure

43 43 Control failure

44 44 Pneumatic/hydraulic failure

**\
**

Code figure for

Code figure for BUFR

s~a~s~a~ (Code table 0 02 014)

45 45 Other problems

46 46 Compressor problems

47 47 Balloon problems

48 48 Balloon release problems

49 49 Launcher damaged

DATA ACQUISITION SYSTEM

50 50 R/S receiver antenna defect

51 51 NAVAID antenna defect

52 52 R/S receiver cabling (antenna) defect

53 53 NAVAID antenna cabling defect

54--58 54--58 Reserved

59 59 Other problems

COMMUNICATIONS

60 60 ASAP communications defect

61 61 Communications facility rejected data

62 62 No power at transmitting antenna

63 63 Antenna cable broken

64 64 Antenna cable defect

65 65 Message transmitted power below normal

66--68 66--68 Reserved

69 69 Other problems

70 70 All systems in normal operation

71--98 71--98 Reserved

99 99 Status of system and its components not specified

Not available 100--126 Reserved

Not available 127 Missing value

**COMMON CODE TABLE C--8: *Satellite instruments***

Common Code table Code table 0 02 019 in BUFR

Code Agency Type Instrument short name Instrument long name

10 BNSC Radiometer AATSR Advanced along track scanning radiometer

11 BNSC Radiometer ATSR Along track scanning radiometer

12 BNSC Radiometer ATSR-2 Along track scanning radiometer-2

13 BNSC Radiometer MWR Microwave radiometer

30 CNES Communications ARGOS

40 CNES Lidar Laser reflectors

41 CNES Lidar DORIS Doppler orbitography and radio-positioning

integrated by satellite

42 CNES Lidar DORIS-NG Doppler orbitography and radio-positioning

integrated by satellite-NG

47 CNES Radar altimeter POSEIDON-1 Positioning ocean, solid Earth, ice dynamics

(SSALT1) orbiting navigator (single frequency solid state

radar altimeter)

48 CNES Radar altimeter POSEIDON-2 Positioning ocean, solid Earth, ice dynamics

(SSALT2) orbiting navigator (double frequency solid

state radar altimeter)

49 CNES Radar altimeter POSEIDON-3 Positioning ocean, solid Earth, ice dynamics

(SSALT3) orbiting navigator (double frequency solid

state radar altimeter)

50 CNES Imaging radiometer ATSR/M ATSR/M

51 CNES High-resolution HRG

optical imager

52 CNES Radiometer HRV High-resolution visible

53 CNES Radiometer HRVIR High-resolution visible and infrared

54 CNES Radiometer ScaRaB/MV2 Scanner for Earth\'s radiation budget

55 CNES Radiometer POLDER POLDER

56 CNES Imaging multi- IIR Imaging Infrared Radiometer\
spectral radiometer

60 CNES Spectrometer VEGETATION VEGETATION

61 CNES Spectrometer WINDII WINDII

62 CNES Altimeter AltiKa Ka band Radar Altimeter

80 CSA Communications RADARSAT DTT

81 CSA Communications RADARSAT TTC

85 CSA Radar SAR (CSA) Synthetic aperture radar (CSA)

90 CSA Radiometer MOPITT Measurements of pollution in the troposphere

91 CSA Atmospheric OSIRIS Optical spectrograph and Infrared imaging

chemistry instrument system

92 CSA Limb-scanning ACE-FTS Atmospheric Chemistry Experiment --\
sounder Fourier Transform Spectrometer

97 CSIRO Radiometer Panchromatic imager

98 CRCSS Atmospheric GPS receiver

temperature and

humidity sounder

102 DLR Radiometer CHAMP GPS sounder GPS turborogue space receiver (TRSR)

103 DLR Radiometer IGOR Integrated GPS and Occultation Receiver

Code Agency Type Instrument short name Instrument long name

104 NASA GNSS occultation Tri-G Triple-G (GPS, Galileo, GLONASS)\
sounder\
116 DLR Magnetometer CHAMP gravity package STAR accelerometer

(Accelerometer+GPS)

117 DLR Magnetometer CHAMP magnetometry Overhauser magnetometer (OVM) and\
package (1 scalar+ fluxgate magnetometer (FGM)\
2 vector magnetometer)

120 ESA Communications ENVISAT Comms Communications package on ENVISAT

121 ESA Communications ERS Comms Communication package for ERS

130 ESA Lidar ALADIN Atmospheric laser Doppler instrument

131 ESA Lidar ATLID Atmospheric lidar

140 ESA Radar AMI/SAR/image Active microwave instrumentation image

mode

141 ESA Radar AMI/SAR/wave Active microwave instrumentation wave mode

142 ESA Radar AMI/scatterometer Active microwave instrumentation wind mode

143 ESA Radar ASAR ASAR

144 ESA Imaging microwave ASAR Advanced synthetic aperture radar

(image mode)

145 ESA Imaging microwave ASAR Advanced synthetic aperture radar

(wave mode)

146 ESA Cloud profile and CPR Cloud radar

rain radar

147 ESA Radar RA-2/MWR Radar altimeter-2

148 ESA Radar RA/MWR Radar altimeter

150 ESA Scatterometer SCATTEROMETER Scatterometer

151 ESA Imaging radar SAR-C Synthetic Aperture Radar (C-band)

152 ESA Cross-nadir SW Sounder TROPOMI Tropospheric\
scanning Monitoring Instrument

161 ESA Radiometer MIPAS Michelson interferometric passive atmosphere

sounder

162 ESA Imaging multi- MWR-2 Microwave radiometer-2

spectral radiometer

(passive microwave)

163 ESA Atmospheric SOPRANO Sub-milimetre observation of processes in the

chemistry instrument absorption noteworthy for ozone

170 ESA Atmospheric GOME Global ozone monitoring experiment

chemistry instrument

172 ESA Spectrometer GOMOS Global ozone monitoring by occultation of

stars

174 ESA Spectrometer MERIS Medium resolution imaging spectrometer

175 ESA Spectrometer SCIAMACHY Scanning imaging absorption spectrometer for

atmospheric cartography

176 ESA Radiometer MIRAS Microwave imaging radiometer using aperture

synthesis

177 ESA Radar Altimeter SIRAL SAR/Interferometric Radar Altimeter

178 ESA Radar altimeter SRAL Synthetic aperture radar altimeter

179 ESA Moderate resolution OLCI Ocean and land colour imager

optical imager

180 ESA Moderate resolution SLSTR Sea and land surface temperature radiometer

optical imager

Code Agency Type Instrument short name Instrument long name

181 EUMETSAT Communications METEOSAT Comms Communications package for METEOSAT

182 EUMETSAT Communications MSG Comms Communications package for MSG

190 ESA/ Scatterometer ASCAT Advanced scatterometer

EUMETSAT

200 EUMETSAT Radiometer GERB Geostationary Earth radiation budget

202 ESA/ Radiometer GRAS GNSS receiver for atmospheric sounding

EUMETSAT

203 EUMETSAT Radiometer MHS Microwave humidity sounder

205 EUMETSAT Radiometer MVIRI METEOSAT visible and infrared imager

207 EUMETSAT Radiometer SEVIRI Spinning enhanced visible and infrared imager

208 EUMETSAT Imaging VIRI VIRI

multi-spectral

radiometer (vis/IR)

220 ESA/ Spectrometer GOME-2 Global ozone monitoring experiment-2

EUMETSAT

221 CNES/ Atmospheric IASI Infrared atmospheric sounding interferometer

EUMETSAT temperature and

humidity sounder

240 CAST Communications DCP Data-collection platform transponder

245 CAST Radiometer CCD High-resolution CCD camera

246 INPE Atmospheric HSB Humidity sounder/Brazil

temperature and

humidity sounder

248 INPE Imaging multi- OBA Observador Brasileiro da Amazonia

spectral radiometer

(vis/IR)

250 CAST Radiometer WFI Wide field imager

255 CAST Spectrometer IRMSS Infrared multispectral scanner

260 ISRO Precision orbit BSS & FSS\
transponders

261 ISRO Precision orbit DRT-S&R

262 ISRO Communications INSAT Comms Communications package for INSAT

268 ISRO High-resolution HR-PAN High-resolution panchromatic camera

optical imager

269 ISRO Imaging MSMR Multifrequency scanning

multi-spectral microwave radiometer

radiometer

(passive microwave)

270 ISRO Imaging VHRR Very high-resolution radiometer

multi-spectral

radiometer (vis/IR)

271 ISRO Imaging WiFS Wide field sensor

multi-spectral\
radiometer (vis/IR)

275 ISRO High-resolution AWiFS Advanced wide field sensor

optical imager

276 ISRO High-resolution LISS-I Linear imaging self scanner-I

optical imager

**\
**

Code Agency Type Instrument short name Instrument long name

277 ISRO High-resolution LISS-II Linear imaging self scanner-II

optical imager

278 ISRO High-resolution LISS-III Linear imaging self scanner-III

optical imager

279 ISRO High-resolution LISS-IV Linear imaging self scanner-IV

optical imager

284 ISRO High-resolution PAN Panchromatic sensor

optical imager

285 ISRO Imaging MOS Modular opto-electronic scanner

multi-spectral

radiometer (vis/IR)

286 ISRO Ocean colour OCM Ocean colour monitor

Instrument

287 ASI ROSA Radio Occultation Sounder of the Atmosphere

288 ISRO Scatterometer SCAT Scatterometer

289 ISRO Optical imager IMG Imager

290 JMA Communications MTSAT Comms Communications package for MTSAT

291 JMA Communications Himawari Comms Communications package for Himawari

294 JMA Imaging multi- JAMI Japanese Advanced Meteorological Imager

spectral radiometer

295 JMA Imaging multi- IMAGER/MTSAT-2 Imager/MTSAT-2

spectral radiometer

296 JMA Imaging multi- VISSR Visible and infrared spin scan radiometer

spectral radiometer

297 JMA Imaging multi- AHI Advanced Himawari Imager

spectral radiometer

300 NASA Lidar GLAS Geoscience laser altimeter system

301 NASA Precision orbit LRA Laser retroreflector array

302 NASA Lidar MBLA Multi-beam laser altimeter

303 NASA Lidar CALIOP Cloud-aerosol lidar with

orthogonal polarization

309 NASA Cloud profile and CPR (Cloudsat) Cloud profiling radar

rain radar

312 NASA Radar NSCAT NASA scatterometer

313 NASA Radar SeaWinds ADEOS II -- NASA scatterometer

314 NASA Radar RapidScat RapidScat scatterometer

330 NASA Earth radiation ACRIM Active cavity radiometer irradiance monitor

budget radiometer

334 NASA Total and profile BUV Backscatter ultraviolet instrument\
ozone

336 NASA High-resolution ALI Advanced land imager

optical imager

347 NASA High-resolution ASTER Advanced spaceborne thermal emission and

optical imager reflection radiometer

348 NASA Earth radiation CERES-2 Cloud and the Earth\'s radiant energy system

budget radiometer

351 NASA Atmospheric GPSDR GPS demonstration receiver

temperature and

humidity sounder

Code Agency Type Instrument short name Instrument long name

353 NASA Total and profile HiRDLS High-resolution dynamics limb sounder

ozone

354 NASA Total and profile HRDI High-resolution Doppler imager\
ozone

356 NASA Radiometer LIS Lightning imaging sensor

358 NASA Magnetic field, PEM Particle environment monitor

auroal imagery

scintillation boundary

359 NASA Ocean colour SeaWiFS Sea-viewing wide field-of-view sensor

instrument

360 NASA Earth radiation SUSIM (UARS) Solar ultraviolet irradiance monitor

budget radiometer

363 NASA Total and profile SBUV/1 Solar backscatter ultraviolet 1 instrument

ozone

365 NASA Imaging multi- TMI TRMM microwave imager

spectral radiometer

(passive microwave)

366 NASA Imaging multi- JMR JASON-1 microwave radiometer

spectral radiometer

(passive microwave)

367 NASA Imaging multi- AMR Advanced microwave radiometer

spectral radiometer\
369 NASA Total and profile LIMS Limb infrared monitor of the stratosphere

ozone

370 NASA Total and profile LRIR Limb radiance inversion radiometer instrument

ozone

371 NASA Total and profile EPIC Earth polychromatic imaging camera

ozone

372 NASA Earth radiation NISTAR NIST advanced radiometer

budget radiometer

373 NASA Magnetic field, Plasma-Mag

auroal imagery

scintillation

boundary

374 NASA Other XPS XUV photometer system

375 NASA Imaging multi- VIRS Visible infrared scanner

spectral radiometer

(vis/IR)

376 CNES Multiple direction/ POLDER II Polarization and directionality of the Earth\'s

polarization reflectance-II

radiometer

377 NASA Earth radiation TIM Total irradiance monitor

budget radiometer

379 NASA Imaging multi- WFC Wide field camera

spectral radiometer

(vis/IR)

382 NASA Spectro-radiometer CLAES Cryogenic limb array etalon spectrometer

383 NASA Spectro-radiometer HALOE Halogen occultation experiment

384 NASA Spectro-radiometer ISAMS Improved stratospheric and mesospheric

sounder

Code Agency Type Instrument short name Instrument long name

385 NASA Spectro-radiometer MISR Multi-angle imaging spectroradiometer

386 NASA Spectro-radiometer MLS Microwave limb sounder

387 NASA Spectro-radiometer MLS (EOS-Aura) Microwave limb sounder (EOS-Aura)

389 NASA Spectro-radiometer MODIS Moderate-resolution imaging

spectroradiometer

393 NASA Gravity HAIRS High accuracy inter-satellite ranging system

394 NASA Total and profile OMI Ozone measuring instrument

ozone

395 NASA Radiometer Atmospheric corrector Atmospheric corrector

396 NASA Radiometer Hyperion Hyperspectral imager

399 NASA Spectro-radiometer SAGE I Stratospheric aerosol and gas

experiment-I

400 NASA Spectro-radiometer SAGE II Stratospheric aerosol and gas

experiment-II

401 NASA Spectro-radiometer SAGE III Stratospheric aerosol and gas

experiment-III

402 NASA Spectro-radiometer SAMS Stratospheric and mesospheric sounder

403 NASA Spectro-radiometer SAM-II Stratospheric aerosol measurement-II

404 NASA Spectro-radiometer IRIS Infrared interferometer spectrometer

405 NASA Atmospheric GIFTS Geosynchronous imaging Fourier transform

temperature and spectrometer

Humidity sounder

420 NASA Spectrometer AIRS Atmospheric Infrared sounder

426 NASA Spectrometer SOLSTICE Solar stellar irradiance comparison\
experiment

430 NASA Spectrometer TES Tropospheric emission spectrometer

431 NASA Spectrometer TOMS Total ozone mapping spectrometer

432 NASA Spectrometer OCO Orbiting carbon observatory

450 JAXA Communications ADEOS Comms Communications package for ADEOS

451 JAXA Communications DCS (JAXA) Data-collection system (JAXA)

453 NASDA Communications GMS Comms Communications package on GMS

454 NASDA Communications JERS-1 Comms Communications package for JERS-1

460 NASDA Lidar RIS Retroreflector in space

461 NASDA Radar PR Precipitation radar

462 NASDA Imaging microwave SAR Synthetic aperture radar

radar

470 JAXA Imaging microwave PALSAR Phased array type L-band synthetic aperture

radar radar

478 JAXA Imaging multi- AMSR2 Advanced Microwave Scanning

spectral radiometer Radiometer 2\
(passive microwave)

479 JAXA Imaging multi- AMSR-E Advanced microwave scanning radiometer --

spectral radiometer EOS

(passive microwave)

480 JAXA High-resolution PRISM (ALOS) Panchromatic remote-sensing instrument for

optical imager stereo mapping

481 JAXA Radiometer AMSR Advanced microwave scanning radiometer

482 NASDA High-resolution AVNIR Advanced visible and near infrared radiometer

optical imager

Code Agency Type Instrument short name Instrument long name

483 JAXA High-resolution AVNIR-2 Advanced visible and near infrared radiometer

optical imager type 2

484 JAXA Imager GLI Global imager

485 NASDA Radiometer MESSR Multispectral electronic self scanning

radiometer

486 NASDA Radiometer MSR Microwave scanning radiometer

487 NASDA Radiometer OCTS Ocean colour and temperature scanner

488 NASDA Radiometer OPS Optical sensor

489 NASDA Radiometer VISSR (GMS-5) Visible and infrared spin scan radiometer

(GMS-5)

490 NASDA Radiometer VTIR Visible and thermal infrared radiometer

510 NASDA Spectrometer ILAS-I Improved limb atmospheric spectrometer

511 NASDA Spectrometer ILAS-II Improved limb atmospheric spectrometer

512 NASDA Spectrometer IMG Inferometric monitor of greenhouse gases

514 NASDA Space environment SEM Space environment monitor (NASDA)

515 JAXA Total and profile SOFIS Solar occultation Fourier transform

ozone spectrometer for inclined orbit satellite

516 JAXA Spectrometer TANSO-FTS Thermal and Near infrared Sensor for carbon

Observations (TANSO) Fourier Transform

Spectrometer (FTS)

517 JAXA Imager TANSO-CAI Thermal and Near infrared Sensor for carbon

Observations (TANSO) Cloud and Aerosol

Imager (CAI)

518 JAXA Cloud and precipi- DPR Dual-frequency precipitation radar

tation radar

519 NASA MW imaging/sound- GMI GPM microwave imager

ing radiometer,

conical scanning

530 Spire GNSS occultation SGNOS-A Spire global navigation satellite system\
sounder occultation sounder A

531 Spire GNSS occultation SGNOS-B Spire global navigation satellite system\
sounder occultation sounder B

532 Spire GNSS occultation SGNOS-C Spire global navigation satellite system\
sounder occultation sounder C

533 Spire GNSS occultation SGNOS-D Spire global navigation satellite system\
sounder occultation sounder D

540 NOAA Communications DCS (NOAA) Data-collection system (NOAA)

541 NOAA Communications GOES Comms Communications package on GOES

542 NOAA Communications LANDSAT Comms Communications package for LANDSAT

543 NOAA Communications NOAA Comms Communications package for NOAA

544 NOAA Communications S&R (GOES) Search and rescue

545 NOAA Communications S&R (NOAA) Search and rescue

546 NOAA Communications WEFAX Weather facsimile

547 NOAA Spectrometer SEM (GOES) Space environment monitor

550 NOAA Magnetic field SSM Special sensor magnetometer

551 NOAA Magnetic field SSJ/4 Special sensor precipitating

plasma monitor

Code Agency Type Instrument short name Instrument long name

552 NOAA Space environment SSIES-2 Special sensor ionospheric plasma

drift/scintillation meter

553 NOAA Space environment SSB/X-2 Special sensor gamma ray particle detector

570 NOAA Radiometer AMSU-A Advanced microwave sounding unit-A

574 NOAA Radiometer AMSU-B Advanced microwave sounding unit-B

580 NOAA Radiometer ATOVS (HIRS/3 + Advanced TIROS operational vertical sounder

AMSU + AVHRR/3)

590 NOAA Radiometer AVHRR/2 Advanced very high-resolution radiometer/2

591 NOAA Radiometer AVHRR/3 Advanced very high-resolution radiometer/3

592 NOAA Radiometer AVHRR/4 Advanced very high-resolution radiometer/4

600 NOAA Radiometer ERBE Earth\'s radiation budget experiment

601 NOAA Radiometer ETM+ Enhanced thematic mapper

605 NOAA Radiometer HIRS/2 High-resolution infrared sounder/2

606 NOAA Radiometer HIRS/3 High-resolution infrared sounder/3

607 NOAA Radiometer HIRS/4 High-resolution infrared sounder/4

615 NOAA Radiometer IMAGER Imager

616 NOAA Imaging multi- VIIRS Visible/infrared imager radiometer suite

spectral radiometer

(vis/IR)

617 NOAA Imaging ABI Advanced baseline imager\
multi-spectral\
radiometer

618 NOAA High-resolution GLM Geostationary lightning mapper\
optical imager

620 NOAA Atmospheric CrIRS/NP Cross-track infrared sounder/NPOESS

temperature and

humidity sounder

621 NOAA Atmospheric ATMS Advanced technology microwave sounder

temperature and

humidity sounder

622 NOAA Radiometer MSS Multispectral scanning system

623 NOAA Radiometer MSU Microwave sounding unit

624 NOAA Radiometer SBUV/2 Solar backscatter ultraviolet instrument/2

625 NOAA Radiometer SBUV/3 Solar backscatter ultraviolet instrument/3

626 NOAA Radiometer SOUNDER SOUNDER

627 NOAA Radiometer SSU Stratospheric sounding unit

628 NOAA Radiometer TM Thematic mapper

629 NOAA Radiometer TOVS (HIRS/2 + TIROS operational vertical sounder

MSU + SSU)

630 NOAA Radiometer VAS VISSR atmospheric sounder

631 NOAA Radiometer SSZ

645 NOAA Spectrometer SEM Space environment monitor

650 NRSCC Radiometer MVIRSR (10 channel) Multispectral visible and infrared

scan radiometer

651 NRSCC Radiometer MVIRSR (3 channel) Multispectral visible and infrared

scan radiometer

652 NRSCC Radiometer MVIRSR (5 channel) Multispectral visible and infrared

scan radiometer

Code Agency Type Instrument short name Instrument long name

670 NSAU Radar RLSBO Side looking microwave radar

680 NSAU High-resolution MSU-EU Multispectral radiometer with high resolution

optical imager

681 NSAU Imaging multi- MSU-UM Visible multispectral radiometer

spectral radio-

meter (vis/IR)

682 NSAU Radiometer RM-08 Imaging microwave radiometer

683 NSAU High-resolution SU-UMS Stereo radiometer with high resolution

optical imager

684 NSAU High-resolution SU-VR Visible radiometer with high resolution

optical imager

685 NSAU Radiometer TRASSER

686 SOA Scatterometer SCAT Scatterometer

687 SOA Radar altimeter ALT Radar altimeter

688 SOA Microwave MWI Microwave radiometer\
radiometer

700 ROSCOSMOS Communications KONDOR-2 Data-collection and transmission system\
701 ROSCOSMOS Communications BRK

710 ROSCOSMOS Lidar ALISSA Backscatter lidar

712 ROSCOSMOS Lidar Balkan-2 lidar

715 ROSCOSMOS Lidar MK-4

716 ROSCOSMOS Lidar MK-4M

730 ROSCOSMOS Radar Greben Radar altimeter

731 ROSCOSMOS Radar SAR-10 Synthetic aperture radar

732 ROSCOSMOS Radar SAR-3 Synthetic aperture radar

733 ROSCOSMOS Radar SAR-70 Synthetic aperture radar

740 ROSCOSMOS Radar SLR-3 Side looking radar

745 ROSCOSMOS Radar Travers SAR

750 ROSCOSMOS Radiometer 174-K Temperature and humidity profiler

751 ROSCOSMOS Radiometer BTVK Scanning television radiometer

752 ROSCOSMOS Radiometer Chaika Scanning infrared radiometer

753 ROSCOSMOS Radiometer DELTA-2 Multispectral microwave scanner

755 ROSCOSMOS Radiometer IKAR-D Multispectral microwave scanner

756 ROSCOSMOS Radiometer IKAR-N Multispectral microwave scanner

757 ROSCOSMOS Radiometer IKAR-P Multispectral microwave scanner

760 ROSCOSMOS Radiometer ISP

761 ROSCOSMOS Radiometer KFA-1000 Photographic camera

762 ROSCOSMOS Radiometer KFA-200 Photographic camera

763 ROSCOSMOS Radiometer KFA-3000 Photographic camera

770 ROSCOSMOS Radiometer Klimat Scanning infrared radiometer

771 ROSCOSMOS Radiometer Klimat-2 Scanning infrared radiometer

775 ROSCOSMOS Radiometer MIRAS

776 ROSCOSMOS Radiometer MIVZA

777 ROSCOSMOS Radiometer MIVZA-M Microwave scanning radiometer

780 ROSCOSMOS Radiometer MR-2000

781 ROSCOSMOS Radiometer MR-2000M

Code Agency Type Instrument short name Instrument long name

785 ROSCOSMOS Radiometer MR-900 Scanning telephotometer

786 ROSCOSMOS Radiometer MR-900B Scanning visual band telephotometer

790 ROSCOSMOS Radiometer MSU-E Multispectral high-resolution

electronic scanner

791 ROSCOSMOS Radiometer MSU-E1 Multispectral high-resolution

electronic scanner

792 ROSCOSMOS Radiometer MSU-E2 Multispectral high-resolution

electronic scanner

793 ROSCOSMOS Radiometer MSU-M

794 ROSCOSMOS Radiometer MSU-S Multispectral medium-resolution scanner

795 ROSCOSMOS Radiometer MSU-SK Multispectral medium-resolution

conical scanner

796 ROSCOSMOS Radiometer MSU-V Multispectral high-resolution

conical scanner

810 ROSCOSMOS Radiometer MTZA Scanning microwave radiometer

815 ROSCOSMOS Imaging multi- MZOAS Scanning microwave radiometer

spectral radiometer

(passive microwave)

820 ROSCOSMOS Imaging multi- R-225 Single channel microwave radiometer

spectral radiometer

(passive microwave)

821 ROSCOSMOS Radiometer R-400

822 ROSCOSMOS Radiometer R-600 Single channel microwave radiometer

830 ROSCOSMOS Radiometer RMS Radiation measurement system

835 ROSCOSMOS Radiometer TV camera

836 ROSCOSMOS Radiometer SILVA

840 ROSCOSMOS Spectro-radiometer SROSMO Spectroradiometer for ocean monitoring\
850 ROSCOSMOS Spectrometer BUFS-2 Backscatter spectrometer/2

851 ROSCOSMOS Spectrometer BUFS-4 Backscatter spectrometer/4

855 ROSCOSMOS Spectrometer ISTOK-1 Infrared spectrometer

856 ROSCOSMOS Spectrometer SFM-2 Spectrometer to measure direct

solar radiation

857 ROSCOSMOS Spectrometer DOPI

858 ROSCOSMOS Spectrometer KGI-4

859 ROSCOSMOS Spectrometer Ozon-M

860 ROSCOSMOS Spectrometer RMK-2

900 NOAA Radiometer MAXIE Magnetospheric atmospheric X-ray imaging

experiment

901 NOAA Radiometer OLS Operational linescan system

905 NOAA Radiometer SSM/I Mission sensor microwave imager

906 NOAA Radiometer SSM/T-1 Mission sensor microwave

temperature sounder

907 NOAA Radiometer SSM/T-2 Mission sensor microwave water

vapour sounder

908 NOAA Radiometer SSMIS Special sensor microwave imager sounder

910 NOAA Radiometer SXI Solar X-ray imager

Code Agency Type Instrument short name Instrument long name

930 NOAA Spectrometer EHIC Energetic heavy ion composition experiment

931 NOAA Spectrometer X-ray astronomy

payload

932 NRSCC Imaging multi- IVISSR (FY-2) Improved multispectral visible and Infrared

spectral radiometer scan radiometer (5 channels)

(vis/IR)

933 NRSCC Atmospheric IRAS Infrared atmospheric sounder

temperature and

humidity sounder

934 NRSCC Atmospheric MWAS Microwave atmospheric sounder

temperature and

humidity sounder

935 NRSCC Atmospheric IMWAS Improved Microwave atmospheric sounder

temperature and

humidity sounder

936 NRSCC Atmospheric MWHS Microwave humidity sounder

temperature and

humidity sounder

937 NRSCC Imaging multi- MVIRS Moderate resolution visible and

spectral radiometer infrared imaging spectroradiometer

(vis/IR)

938 NRSCC Imaging multi- MWRI Microwave radiation imager

spectral radiometer

(passive microwave)

940 ROSCOSMOS Atmospheric MTVZA-OK Scanning microwave radiometer

temperature and

humidity sounder

941 CNES Atmospheric SAPHIR

temperature and

humidity sounder

942 CNES Microwave imager MADRAS Microwave Analysis and Detection

of Rain and Atmospheric Structures

943 CNSA Scatterometer SCAT (on CFOSAT) Scatterometer

944 NOAA Radar altimeter ALT Altimeter

945 NOAA Earth radiation TSIS Total solar irradiance sensor

budget radiometer

946 NOAA Imaging multi- CMIS Conical-scanning microwave

spectral radiometer imager/sounder

(passive microwave)

947 NOAA Total and profile OMPS Ozone mapping and profiler suite ozone

948 NOAA Space environment GPSOS Global positioning system occultation sensor

atmospheric

temperature and

humidity sounder

Code Agency Type Instrument short name Instrument long name

949 NOAA Magnetic field, SESS Space environmental sensor suite

auroal imagery

scintillation boundary

950 NRSCC Imaging multi- VIRR Multispectral visible and infrared scan

spectral radiometer radiometer (10 channels)

(vis/IR)

951 NRSCC Total and profile TOM Total ozone mapper

ozone

952 NRSCC Total and profile OP Ozone profiler

ozone

953 CMA Microwave sound- MWHS-2 Microwave humidity sounder-2

ing radiometer,

crosstrack scanning

954 CMA Microwave sound- MWTS-2 Microwave temperature sounder-2

ing radiometer,

crosstrack scanning

955 CMA Cross-nadir scan- HIRAS Hyperspectral infrared atmospheric sounder

ning IR sounder

956 CMA Spectrometer SBUS Solar backscatter ultraviolet sounder

957 CMA Spectrometer TOU Total ozone unit

958 CMA GNSS GNOS Global navigation satellite system

occultation occultation sounder

sounder

959 SNSB Limb-scanning SMR Sub-millimetre radiometer\
sounder

960 Reserved

961 CMA Imaging multi- AGRI Advanced Geostationary Radiation\
spectral Imager\
radiometer\
962 CMA Atmospheric GIIRS Geostationary Interferometric Infrared temperature Sounder

and humidity\
sounder

963 CMA High-resolution LMI Lightning Mapping Imager\
optical imager

964 CMA Space environment SEP Space Environment Package

965--999 Reserved

1000--2046 Reserved for long-term future use

2047 Missing value

**COMMON CODE TABLE C--11: *Originating/generating centres***

BUFR 0 01 035

Common Code table CREX Edition 2, ooooo in Group Poooooppp in Section 1

GRIB Edition 2, Octets 6--7 in Section 1

BUFR Edition 4, Octets 5--6 in Section 1

CREX Edition 2 GRIB Edition 2

B 01 035 Octets 6--7 in Section 1

(5 characters) BUFR Edition 4

and Group 3 0 01 035 (16 bits)

in Section 1 and Octets 5--6 in Section 1

00000 0 WMO Secretariat

**00001--00009: WMCs**

00001 1 Melbourne

00002 2 Melbourne

00003 3 )

00004 4 Moscow

00005 5 Moscow

00006 6 )

00007 7 US National Weather Service, National Centres for

Environmental Prediction (NCEP)

00008 8 US National Weather Service Telecommunications

Gateway (NWSTG)

00009 9 US National Weather Service -- Other

**00010--00025: Centres in Region I**

00010 10 Cairo (RSMC)

00011 11 )

00012 12 Dakar (RSMC)

00013 13 )

00014 14 Nairobi (RSMC)

00015 15 )

00016 16 Casablanca (RSMC)

00017 17 Tunis (RSMC)

00018 18 Tunis--Casablanca (RSMC)

00019 19 )

00020 20 Las Palmas

00021 21 Algiers (RSMC)

00022 22 ACMAD

00023 23 Mozambique (NMC)

00024 24 Pretoria (RSMC)

00025 25 La Réunion (RSMC)

**00026--00040: Centres in Region II**

00026 26 Khabarovsk (RSMC)

00027 27 )

00028 28 New Delhi (RSMC)

00029 29 )

**\
**

CREX Edition 2 GRIB Edition 2

B 01 035 Octets 6--7 in Section 1

(5 characters) BUFR Edition 4

and Group 3 0 01 035 (16 bits)

in Section 1 and Octets 5--6 in Section 1

00030 30 Novosibirsk (RSMC)

00031 31 )

00032 32 Tashkent (RSMC)

00033 33 Jeddah (RSMC)

00034 34 Tokyo (RSMC), Japan Meteorological Agency

00035 35 )

00036 36 Bangkok

00037 37 Ulaanbaatar

00038 38 Beijing (RSMC)

00039 39 )

00040 40 Seoul

**00041--00050: Centres in Region III**

00041 41 Buenos Aires (RSMC)

00042 42 )

00043 43 Brasilia (RSMC)

00044 44 )

00045 45 Santiago

00046 46 Brazilian Space Agency ­ INPE

00047 47 Colombia (NMC)

00048 48 Ecuador (NMC)

00049 49 Peru (NMC)

00050 50 Venezuela (Bolivarian Republic of) (NMC)

**00051--00063: Centres in Region IV**

00051 51 Miami (RSMC)

00052 52 Miami RSMC, National Hurricane Centre

00053 53 MSC Monitoring

00054 54 Montreal (RSMC)

00055 55 San Francisco

00056 56 ARINC Centre

00057 57 US Air Force -- Air Force Global Weather Central

00058 58 Fleet Numerical Meteorology and Oceanography\
Center, Monterey, CA, United States

00059 59 The NOAA Forecast Systems Laboratory, Boulder, CO,\
United States

00060 60 United States National Center for Atmospheric Research\
(NCAR)

00061 61 Service ARGOS -- Landover

00062 62 US Naval Oceanographic Office

00063 63 International Research Institute for Climate and Society\
(IRI)

CREX Edition 2 GRIB Edition 2

B 01 035 Octets 6--7 in Section 1

(5 characters) BUFR Edition 4

and Group 3 0 01 035 (16 bits)

in Section 1 and Octets 5--6 in Section 1

**00064--00073: Centres in Region V**

00064 64 Honolulu (RSMC)

00065 65 Darwin (RSMC)

00066 66 )

00067 67 Melbourne (RSMC)

00068 68 Reserved

00069 69 Wellington (RSMC)

00070 70 )

00071 71 Nadi (RSMC)

00072 72 Singapore

00073 73 Malaysia (NMC)

**00074--00099: Centres in Region VI**

00074 74 UK Meteorological Office -- Exeter (RSMC)

00075 75 )

00076 76 Moscow (RSMC)

00077 77 Reserved

00078 78 Offenbach (RSMC)

00079 79 )

00080 80 Rome (RSMC)

00081 81 )

00082 82 Norrköping

00083 83 )

00084 84 Toulouse (RSMC)

00085 85 Toulouse (RSMC)

00086 86 Helsinki

00087 87 Belgrade

00088 88 Oslo

00089 89 Prague

00090 90 Episkopi

00091 91 Ankara

00092 92 Frankfurt/Main

00093 93 London (WAFC)

00094 94 Copenhagen

00095 95 Rota

00096 96 Athens

00097 97 European Space Agency (ESA)

00098 98 European Centre for Medium Range Weather Forecasts\
(ECMWF) (RSMC)

00099 99 De Bilt

CREX Edition 2 GRIB Edition 2

B 01 035 Octets 6--7 in Section 1

(5 characters) BUFR Edition 4

and Group 3 0 01 035 (16 bits)

in Section 1 and Octets 5--6 in Section 1

**Additional Centres**

00100 100 Brazzaville

00101 101 Abidjan

00102 102 Libya (NMC)

00103 103 Madagascar (NMC)

00104 104 Mauritius (NMC)

00105 105 Niger (NMC)

00106 106 Seychelles (NMC)

00107 107 Uganda (NMC)

00108 108 United Republic of Tanzania (NMC)

00109 109 Zimbabwe (NMC)

00110 110 Hong Kong, China

00111 111 Afghanistan (NMC)

00112 112 Bahrain (NMC)

00113 113 Bangladesh (NMC)

00114 114 Bhutan (NMC)

00115 115 Cambodia (NMC)

00116 116 Democratic People\'s Republic of Korea (NMC)

00117 117 Islamic Republic of Iran (NMC)

00118 118 Iraq (NMC)

00119 119 Kazakhstan (NMC)

00120 120 Kuwait (NMC)

00121 121 Kyrgyzstan (NMC)

00122 122 Lao People\'s Democratic Republic (NMC)

00123 123 Macao, China

00124 124 Maldives (NMC)

00125 125 Myanmar (NMC)

00126 126 Nepal (NMC)

00127 127 Oman (NMC)

00128 128 Pakistan (NMC)

00129 129 Qatar (NMC)

00130 130 Yemen (NMC)

00131 131 Sri Lanka (NMC)

00132 132 Tajikistan (NMC)

00133 133 Turkmenistan (NMC)

00134 134 United Arab Emirates (NMC)

00135 135 Uzbekistan (NMC)

00136 136 Viet Nam (NMC)

00137--00139 137--139 Reserved for other centres

00140 140 Bolivia (Plurinational State of) (NMC)

CREX Edition 2 GRIB Edition 2

B 01 035 Octets 6--7 in Section 1

(5 characters) BUFR Edition 4

and Group 3 0 01 035 (16 bits)

in Section 1 and Octets 5--6 in Section 1

00141 141 Guyana (NMC)

00142 142 Paraguay (NMC)

00143 143 Suriname (NMC)

00144 144 Uruguay (NMC)

00145 145 French Guiana

00146 146 Brazilian Navy Hydrographic Centre

00147 147 National Commission on Space Activities (CONAE) --

Argentina

00148--00149 148--149 Reserved for other centres

00150 150 Antigua and Barbuda (NMC)

00151 151 Bahamas (NMC)

00152 152 Barbados (NMC)

00153 153 Belize (NMC)

00154 154 British Caribbean Territories Centre

00155 155 San José

00156 156 Cuba (NMC)

00157 157 Dominica (NMC)

00158 158 Dominican Republic (NMC)

00159 159 El Salvador (NMC)

00160 160 US NOAA/NESDIS

00161 161 US NOAA Office of Oceanic and Atmospheric Research

00162 162 Guatemala (NMC)

00163 163 Haiti (NMC)

00164 164 Honduras (NMC)

00165 165 Jamaica (NMC)

00166 166 Mexico

00167 167 Curaçao and Sint Maarten (NMC)

00168 168 Nicaragua (NMC)

00169 169 Panama (NMC)

00170 170 Saint Lucia (NMC)

00171 171 Trinidad and Tobago (NMC)

00172 172 French Departments in RA IV

00173 173 US National Aeronautics and Space Administration (NASA)\
00174 174 Integrated Science Data Management/Marine

Environmental Data Service (ISDM/MEDS -- Canada)

00175 175 University Corporation for Atmospheric Research (UCAR)\
-- United States

00176 176 Cooperative Institute for Meteorological Satellite\
Studies (CIMSS) -- United States

CREX Edition 2 GRIB Edition 2

B 01 035 Octets 6--7 in Section 1

(5 characters) BUFR Edition 4

and Group 3 0 01 035 (16 bits)

in Section 1 and Octets 5--6 in Section 1

00177 177 NOAA National Ocean Service -- United States

00178 178 Spire Global, Inc.

00179--00189 179--189 Reserved for other centres

00190 190 Cook Islands (NMC)

00191 191 French Polynesia (NMC)

00192 192 Tonga (NMC)

00193 193 Vanuatu (NMC)

00194 194 Brunei Darussalam (NMC)

00195 195 Indonesia (NMC)

00196 196 Kiribati (NMC)

00197 197 Federated States of Micronesia (NMC)

00198 198 New Caledonia (NMC)

00199 199 Niue

00200 200 Papua New Guinea (NMC)

00201 201 Philippines (NMC)

00202 202 Samoa (NMC)

00203 203 Solomon Islands (NMC)

00204 204 National Institute of Water and Atmospheric Research\
(NIWA -- New Zealand)

00205--00209 205--209 Reserved for other centres

00210 210 Frascati (ESA/ESRIN)

00211 211 Lannion

00212 212 Lisboa

00213 213 Reykjavik

00214 214 Madrid

00215 215 Zurich

00216 216 Service ARGOS Toulouse

00217 217 Bratislava

00218 218 Budapest

00219 219 Ljubljana

00220 220 Warsaw

00221 221 Zagreb

00222 222 Albania (NMC)

00223 223 Armenia (NMC)

00224 224 Austria (NMC)

00225 225 Azerbaijan (NMC)

00226 226 Belarus (NMC)

00227 227 Belgium (NMC)

00228 228 Bosnia and Herzegovina (NMC)

00229 229 Bulgaria (NMC)

CREX Edition 2 GRIB Edition 2

B 01 035 Octets 6--7 in Section 1

(5 characters) BUFR Edition 4

and Group 3 0 01 035 (16 bits)

in Section 1 and Octets 5--6 in Section 1

00230 230 Cyprus (NMC)

00231 231 Estonia (NMC)

00232 232 Georgia (NMC)

00233 233 Dublin

00234 234 Israel (NMC)

00235 235 Jordan (NMC)

00236 236 Latvia (NMC)

00237 237 Lebanon (NMC)

00238 238 Lithuania (NMC)

00239 239 Luxembourg

00240 240 Malta (NMC)

00241 241 Monaco

00242 242 Romania (NMC)

00243 243 Syrian Arab Republic (NMC)

00244 244 The former Yugoslav Republic of Macedonia (NMC)

00245 245 Ukraine (NMC)

00246 246 Republic of Moldova (NMC)

00247 247 Operational Programme for the Exchange of weather\
RAdar information (OPERA) -- EUMETNET

00248 248 Montenegro (NMC)

00249 249 Barcelona Dust Forecast Center

00250 250 COnsortium for Small scale MOdelling (COSMO)

00251 251 Meteorological Cooperation on Operational NWP\
(MetCoOp)

00252 252 Max Planck Institute for Meteorology (MPI-M)

00253 253 Reserved for other centres

00254 254 EUMETSAT Operation Centre

00255 255 Not to be used

00256 256 Angola (NMC)

00257 257 Benin (NMC)

00258 258 Botswana (NMC)

00259 259 Burkina Faso (NMC)

00260 260 Burundi (NMC)

00261 261 Cameroon (NMC)

00262 262 Cabo Verde (NMC)

00263 263 Central African Republic (NMC)

00264 264 Chad (NMC)

00265 265 Comoros (NMC)

00266 266 Democratic Republic of the Congo (NMC)

00267 267 Djibouti (NMC)

CREX Edition 2 GRIB Edition 2

B 01 035 Octets 6--7 in Section 1

(5 characters) BUFR Edition 4

and Group 3 0 01 035 (16 bits)

in Section 1 and Octets 5--6 in Section 1

00268 268 Eritrea (NMC)

00269 269 Ethiopia (NMC)

00270 270 Gabon (NMC)

00271 271 Gambia (NMC)

00272 272 Ghana (NMC)

00273 273 Guinea (NMC)

00274 274 Guinea-Bissau (NMC)

00275 275 Lesotho (NMC)

00276 276 Liberia (NMC)

00277 277 Malawi (NMC)

00278 278 Mali (NMC)

00279 279 Mauritania (NMC)

00280 280 Namibia (NMC)

00281 281 Nigeria (NMC)

00282 282 Rwanda (NMC)

00283 283 Sao Tome and Principe (NMC)

00284 284 Sierra Leone (NMC)

00285 285 Somalia (NMC)

00286 286 Sudan (NMC)

00287 287 Eswatini (NMC)

00288 288 Togo (NMC)

00289 289 Zambia (NMC)

00290--65534 290--65534 Reserved for other centres

65535 65535 Missing value

65536--99999 Not applicable Not used

Notes:

\(1) The closed bracket sign \")\" indicates that the corresponding code figure is reserved for the previously named centre.

\(2) With GRIB or BUFR, to indicate whether the originating/generating centre is a sub-centre or not, the following procedure should be applied:

> In GRIB edition 2, use octets 8--9 of section 1, or in BUFR edition 4, use octets 7--8 of section 1, with the following meaning:
>
> Code figure
>
> 0 Not a sub-centre, the originating/generating centre is the centre defined by octets 6--7 in section 1 of GRIB edition 2, or by octets 5--6 in section 1 of BUFR edition 4.
>
> 1 to 254 Identifier of the sub-centre which is the originating/generating centre. The identifier of the sub-centre is allocated by the associated centre, which is defined by octets 6--7 in section 1 of GRIB edition 2 or by octets 5--6 in section 1 of BUFR edition 4. The sub-centre identifiers should be supplied to the WMO Secretariat by the associated centre(s) for publication.

\(3) For the definitions of sub-centres provided to the WMO Secretariat, see Common Code table C--12.

**COMMON CODE TABLE C--12: *Sub-centres of originating centres defined by entries in\
Common Code tables C--1 or C--11***

ORIGINATING CENTRES SUB-CENTRES

C--1, C--11 or C--12 BUFR 0 01 034

BUFR Edition 3, Octet 5 in Section 1

BUFR Edition 4, Octets 7--8 in Section 1

GRIB Edition 1, Octet 26 in Section 1

GRIB Edition 2, Octets 8--9 in Section 1

CREX Edition 2, ppp in Group Poooooppp\
in Section 1

Code figure Name Code figure Name

0 No sub-centre

**REGION II**

34 Tokyo (RSMC), Japan 207 Syowa

Meteorological Agency 240 Kiyose

241 Reanalysis project

39 Beijing (RSMC) 225 Beijing

226 Guangzhou

228 Urumuqi

40 Seoul 243 Seoul

245 Jincheon

110 Hong-Kong, China 229 Hong-Kong

**REGION III**

46 Brazilian Space Agency -- 10 Cachoeira Paulista (INPE)

INPE 11 Cuiaba (INPE)

12 Brasilia (INMET)

13 Fortaleza (FUNCEME)

14 Natal (Navy Hygrog. Centre)

15 Manaus (SIVAM)

16 Natal (INPE)

17 Boa Vista

25 São Paulo University -- USP

147 National Commission on 10 Córdoba

Space Activities (CONAE) -- 15 Ushuaia

Argentina 20 Marambio

30 Santiago de Chile

40 Punta Arenas

50 Base Presidente Frei

60 Cotopaxi

**REGION IV**

7 US National Weather Service, 1 NCEP Reanalysis Project

NCEP 2 NCEP Ensemble Products

3 NCEP Central Operations

4 Environmental Modeling Center

5 Weather Prediction Center

6 Ocean Prediction Center

7 Climate Prediction Center

8 Aviation Weather Center

9 Storm Prediction Center

10 National Hurricane Center

11 NWS Techniques Development Laboratory

12 NESDIS Office of Research and Applications

13 Federal Aviation Administration

14 NWS Meteorological Development Laboratory

ORIGINATING CENTRES SUB-CENTRES

C--1, C--11 or C--12 BUFR 0 01 034

BUFR Edition 3, Octet 5 in Section 1

BUFR Edition 4, Octets 7--8 in Section 1

GRIB Edition 1, Octet 26 in Section 1

GRIB Edition 2, Octets 8--9 in Section 1

CREX Edition 2, ppp in Group Poooooppp\
in Section 1

Code figure Name Code figure Name

**REGION IV** (*continued*)

7 US National Weather Service, 15 North American Regional Reanalysis Project\
NCEP 16 Space Weather Prediction Center\
17 ESRL Global Systems Division

160 United States NOAA/NESDIS 1 National Climatic Data Center

2 National Geophysical Data Center

3 National Oceanographic Data Center

4 Center for Satellite Applications and Research\
(STAR)

5 Joint Polar Satellite System

10 Tromso (Norway)

11 McMurdo (Antarctica)

161 United States NOAA Office of 1 Great Lakes Environmental Research Laboratory

Oceanic and Atmospheric 2 Earth System Research Laboratory

Research (NOAA/OAR) 3 Atlantic Oceanographic and Meteorological

Laboratory

4 Pacific Marine Environmental Laboratory\
5 Air Resources Laboratory\
6 Geophysical Fluid Dynamics Laboratory\
7 National Severe Storms Laboratory

173 United States National 1 Ames Research Center

Aeronautics and Space 2 Dryden Flight Research Center

Administration (NASA) 3 Glenn Research Center

4 Goddard Space Flight Center

5 Jet Propulsion Laboratory

6 Johnson Space Center

7 Kennedy Space Center

8 Langley Research Center

9 Marshall Space Flight Center

10 Stennis Space Center

11 Goddard Institute for Space Studies

12 Independent Verification and Validation Facility

13 NASA Shared Service Center

14 Wallops Flight Facility

176 Cooperative Institute for 10 Tromso (Norway)

Meteorological 11 McMurdo (Antarctica)

Satellite Studies (CIMSS) -- 12 Sodankyla (Finland)

United States 13 Fairbanks (United States)

14 Barrow (United States)

15 Rothera (Antarctica)

20 Honolulu (United States)

21 Gilmore Creek (United States)

22 Madison (United States)

23 Miami (United States)

24 Mayaguez (Puerto Rico)

25 Monterey (United States)

ORIGINATING CENTRES SUB-CENTRES

C--1, C--11 or C--12 BUFR 0 01 034

BUFR Edition 3, Octet 5 in Section 1

BUFR Edition 4, Octets 7--8 in Section 1

GRIB Edition 1, Octet 26 in Section 1

GRIB Edition 2, Octets 8--9 in Section 1

CREX Edition 2, ppp in Group Poooooppp\
in Section 1

Code figure Name Code figure Name

**REGION IV** (*continued*)

176 Cooperative Institute for 26 Guam

Meteorological 27 Corvallis (United States)

Satellite Studies (CIMSS) -- 28 Hampton (United States)

United States 29 New York City (United States)

177 NOAA National Ocean 1 Center for Operational Oceanographic Products

Service -- United States and Services

2 Coast Survey Development Laboratory

**REGION V**

2 Melbourne 201 Casey

203 Davis

210 Alice Springs

211 Melbourne Crib Point 1

214 Darwin

217 Perth

219 Townsville

232 Fiji

235 Noumea

237 Papeete

250 Vladivostock

251 Guam

252 Honolulu

69 Wellington (RSMC) 204 National Institute of Water and Atmospheric

Research (NIWA -- New Zealand)

205 Niue

206 Rarotonga (Cook Islands)

207 Apia (Samoa)

208 Tonga

209 Tuvalu

210 Kiribati

211 Tokelau

243 Kelburn

72 Singapore 249 Singapore

191 French Polynesia (NMC) 1 RARS station of Tahiti (French Polynesia)

204 National Institute of Water 101 Maupia

and Atmospheric Research 102 Lauder

(NIWA -- New Zealand)

**REGION VI**

74 UK Met Office, Exeter (RSMC) 1 Shanwick Oceanic Area Control Centre

2 Fucino

3 Gatineau

ORIGINATING CENTRES SUB-CENTRES

C--1, C--11 or C--12 BUFR 0 01 034

BUFR Edition 3, Octet 5 in Section 1

BUFR Edition 4, Octets 7--8 in Section 1

GRIB Edition 1, Octet 26 in Section 1

GRIB Edition 2, Octets 8--9 in Section 1

CREX Edition 2, ppp in Group Poooooppp\
in Section 1

Code figure Name Code figure Name

**REGION VI** (*continued*)

74 UK Met Office, Exeter (RSMC) 4 Maspalomas (Spain)

5 ESA ERS Central Facility

6 Prince Albert

7 West Freugh

13 Tromso

21 Agenzia Spaziale Italiana (Italy)

22 Centre National de la Recherche

Scientifique (France)

23 GeoForschungs Zentrum (Germany)

24 Geodetic Observatory Pecny

(Czechia)

25 Institut d\'Estudis Espacials de Catalunya (Spain)

26 Federal Office of Topography (Switzerland)

27 Nordic Commission of Geodesy (Norway)

28 Nordic Commission of Geodesy (Sweden)

29 Institute Géographique National (France) --

Service de géodésie

30 Bundesamt für Kartographie und Geodäsie

(Germany)

31 Institute of Engineering Satellite Surveying\
and Geodesy (United Kingdom)

32 Joint Operational Meteorology and

Oceanography Centre (JOMOC)

33 Koninklijk Nederlands Meteorologisch

Institut (Netherlands)

34 Nordic GPS Atmospheric Analysis centre (Sweden)

35 Instituto Geografico Nacional de España (Spain)

36 Met Éireann (Ireland)

37 Royal Observatory of Belgium (Belgium)

78 Offenbach (RSMC) 10 POLARA (Polarimetric Radar Algorithms instance)

64 Bundeswehr Geoinformation Office (BGIO)

110 NowCast mobile (Lightning data)

221 Schleswig-Holstein, Traffic Operations\
Computing Centre (TOCC)\
Kiel/Neumünster

222 Hamburg, TOCC Hamburg

223 Niedersachsen, TOCC Hannover\
224 Austria (NMC)

225 Nordrhein-Westfalen, TOCC Kamen\
Leverkusen

226 Hessen, TOCC Rüsselsheim

227 Rheinland-Pfalz, TOCC Koblenz

228 Baden-Württemberg, TOCC Ludwigsburg

229 Bayern, TOCC Freimann

230 Saarland, TOCC Rohrbach

231 Bayern, Autobahn directorate Nordbayern

232 Brandenburg, TOCC Stolpe

ORIGINATING CENTRES SUB-CENTRES

C--1, C--11 or C--12 BUFR 0 01 034

BUFR Edition 3, Octet 5 in Section 1

BUFR Edition 4, Octets 7--8 in Section 1

GRIB Edition 1, Octet 26 in Section 1

GRIB Edition 2, Octets 8--9 in Section 1

CREX Edition 2, ppp in Group Poooooppp\
in Section 1

Code figure Name Code figure Name

**REGION VI** (*continued*)

78 Offenbach (RSMC) 233 Mecklenburg-Vorpommern, TOCC Malchow

234 Sachsen, TOCC Dresden

235 Sachsen-Anhalt, TOCC Halle

236 Thüringen, TOCC Erfurt

237 EasyWay -- Meteotrans\
254 EUMETSAT

80 Rome (RSMC) 101 Albania (NMC)

102 National Research Council/Institute of

Atmospheric Sciences and Climate

(CNR-ISAC)

85 Toulouse (RSMC) 200 Institut National de l\'Environnement Industriel et

des Risques (France)

201 Rheinisches Institut für Umweltforschung an der

Universität zu Köln E.V. (Germany)

202 Institut Français de Recherche pour l\'Exploitation\
de la Mer

203 Aarhus University (Denmark)

204 Institute of Environmental Protection -- National\
Research Institute (Poland)

89 Prague (RTH) 1 Solar and Ozone Observatory Hradec Kralove

96 Athens 1 Cyprus (NMC)

227 Belgium (NMC) 1 Luxembourg (NMC)

250 COSMO (COnsortium for 76 Roshydromet (Russian Federation)

Small scale MOdelling) 78 Deutscher Wetterdienst (Germany)

80 Ufficio Generale Spazio Aereo e Meteorologia\
(Italy)

96 Hellenic National Meteorological Service (Greece)

215 MeteoSwiss (Switzerland)

220 Institute of Meteorology and Water Management\
(Poland)

242 National Meteorological Administration (Romania)

254 EUMETSAT Operation Centre 10 Tromso (Norway)

20 Maspalomas (Spain)

30 Kangerlussuaq (Greenland)

40 Edmonton (Canada)

50 Bedford (Canada)

60 Gander (Canada)

70 Monterey (United States)

80 Wallops Island (United States)

90 Gilmor Creek (United States)

100 Athens (Greece)

120 Ewa Beach, Hawaii

125 Ford Island, Hawaii

130 Miami, Florida

140 Lannion (France)

ORIGINATING CENTRES SUB-CENTRES

C--1, C--11 or C--12 BUFR 0 01 034

BUFR Edition 3, Octet 5 in Section 1

BUFR Edition 4, Octets 7--8 in Section 1

GRIB Edition 1, Octet 26 in Section 1

GRIB Edition 2, Octets 8--9 in Section 1

CREX Edition 2, ppp in Group Poooooppp\
in Section 1

Code figure Name Code figure Name

**REGION VI** (*continued*)

254 EUMETSAT Operation Centre 150 Svalbard (Norway)

170 St Denis (La Réunion)

180 Moscow

190 Muscat

200 Khabarovsk

210 Novosibirsk

**COMMON CODE TABLE C--13: *Data sub-categories of categories defined by entries in BUFR Table A***

DATA CATEGORIES INTERNATIONAL DATA SUB-CATEGORIES

BUFR Edition 4, Octet 11 in Section 1 BUFR Edition 4, Octet 12 (if = 255, it means

other sub-category or undefined)

CREX Edition 2, nnn in Group CREX Edition 2, mmm in Group Annnmmm\
Annnmmm of Section 1 of Section 1

Code figure Name Code figure Name (corresponding traditional alphanumeric\
codes are in brackets)

0 Surface data -- land 0 Hourly synoptic observations from fixed-land stations

(SYNOP)

1 Intermediate synoptic observations from fixed-land

stations (SYNOP)

2 Main synoptic observations from fixed-land stations

(SYNOP)

3 Hourly synoptic observations from mobile-land stations

(SYNOP MOBIL)

4 Intermediate synoptic observations from mobile-land

stations (SYNOP MOBIL)

5 Main synoptic observations from mobile-land stations

(SYNOP MOBIL)

6 One-hour observations from automated stations

7 n-minute observations from AWS stations

8 Radiation observations from one-hour period

9 Radiation observations from n-minute period

10 Routine aeronautical observations (METAR)

11 Special aeronautical observations (SPECI)

14 Ground-based GPS humidity observations (GPSIWV)

20 Climatological observations (CLIMAT)

21 Climatological observations (monthly reports of\
daily climate data)

30 Sferics locations

40 Hydrologic reports

50 Hourly synoptic observations with supplementary

one-hour data

51 Intermediate synoptic observations with supplementary

one-hour data

52 Main synoptic observations with supplementary one-

hour data

1 Surface data -- sea 0 Synoptic observations (SHIP)

6 One-hour observations from automated stations

7 n-minute observations from AWS stations

20 Climatological observations (CLIMAT SHIP)

25 Buoy observation (BUOY)

30 Tide gauge

31 Observed water level time series

2 Vertical soundings (other 1 Upper-wind reports from fixed-land stations (PILOT)

than satellite) 2 Upper-wind reports from ships (PILOT SHIP)

3 Upper-wind reports from mobile land stations (PILOT

MOBIL)

4 Upper-level temperature/humidity/wind reports from

fixed-land stations (TEMP)

5 Upper-level temperature/humidity/wind reports from

ships (TEMP SHIP)

DATA CATEGORIES INTERNATIONAL DATA SUB-CATEGORIES

BUFR Edition 4, Octet 11 in Section 1 BUFR Edition 4, Octet 12 (if = 255, it means

other sub-category or undefined)

CREX Edition 2, nnn in Group Annnmmm CREX Edition 2, mmm in Group Annnmmm\
of Section 1 of Section 1

Code figure Name Code figure Name (corresponding traditional\
alphanumeric codes are in brackets)

2 Vertical soundings (other 6 Upper-level temperature/humidity/wind report from

than satellite) mobile land stations (TEMP MOBIL)

(*continued*) 7 Upper-level temperature/humidity/wind reports from

dropwinsondes (TEMP DROP)

10 Wind profiler reports

11 RASS temperature profiles

14 Upper-level temperature/humidity/wind reports from\
descent radiosondes originally launched from fixed\
land stations

15 Upper-level temperature/humidity/wind reports from\
descent radiosondes originally launched from ships

16 Upper-level temperature/humidity/wind reports from\
descent radiosondes originally launched from\
mobile land stations

20 ASDAR/ACARS profiles (AMDAR)

21 Profiles of atmospheric constituents concentrations

25 Climatological observations from fixed-land stations

(CLIMAT TEMP)

26 Climatological observations from ships (CLIMAT TEMP

SHIP)

3 Vertical soundings 0 Temperature (SATEM)

(satellite) 1 TIROS (TOVS)

2 ATOVS

3 AMSU-A

4 AMSU-B

5 HIRS

6 MHS

7 IASI

8 VASS (Vertical atmospheric sounding system)

20 IR temperature/humidity sounding

30 Hyperspectral temperature/humidity sounding

40 MW temperature/humidity sounding

50 Radio occultation sounding

4 Single level upper-air data 0 ASDAR/ACARS (AMDAR)

(other than satellite) 1 Manual (AIREP, PIREP)

5 Single level upper-air data 0 Cloud wind data (SATOB)\
(satellite) 1 Cloud properties

6 Radar data 0 Reflectivity data

1 Doppler wind profiles

2 Derived products

3 Ground radar weather (RADOB)

DATA CATEGORIES INTERNATIONAL DATA SUB-CATEGORIES

BUFR Edition 4, Octet 11 in Section 1 BUFR Edition 4, Octet 12 (if = 255, it means

other sub-category or undefined)

CREX Edition 2, nnn in Group Annnmmm CREX Edition 2, mmm in Group Annnmmm\
of Section 1 of Section 1

Code figure Name Code figure Name (corresponding traditional\
alphanumeric codes are in brackets)

7 Synoptic features 0 Forecast tropical cyclone tracks from EPS

1 Squall line

8 Physical/chemical 0 Surface ozone

constituents 1 Ozone vertical sounding

2 Total ozone

3 Acid rain

9 Dispersal and transport 0 Trajectories, analysis or forecast

10 Radiological data 1 Observation (RADREP)

2 Forecast (RADOF)

12 Surface data (satellite) 0 ERS-uwa

1 ERS-uwi

2 ERS-ura

3 ERS-uat

4 SSM/I radiometer

5 Quikscat

6 Surface temp./radiation (SATOB)

7 ASCAT data

8 Soil moisture

9 Normalized differential vegetation index (NDVI)

10 Normalized radar backscatter

11 Surface emissivity

12 Sea-surface temperature

13 Precipitation

21 Radiances (satellite 0 Earth radiation budget

measured) 5 Cross-track infrared sounder

6 Advanced technology microwave sounder

7 Visible/infrared imager radiometer suite

22 Radar (satellite) but not 0 Cloud and precipitation radar

altimeter and scatterometer 1 Synthetic aperture radar

23 Lidar (satellite) 0 Lidar based missions (for wind, for cloud/aerosol,\
for water vapour, for altimetry)

24 Scatterometry (satellite) 0 Wind scatterometry

25 Altimetry (satellite) 0 Radar altimetry

26 Spectrometry (satellite) 0 Cross nadir short-wave spectrometry (for chemistry)

1 Cross nadir IR spectrometry (for chemistry)

2 Limb sounding short-wave spectrometry

3 Limb sounding IR spectrometry

4 Limb sounding sub-millimetre wave spectrometry

DATA CATEGORIES INTERNATIONAL DATA SUB-CATEGORIES

BUFR Edition 4, Octet 11 in Section 1 BUFR Edition 4, Octet 12 (if = 255, it means

other sub-category or undefined)

CREX Edition 2, nnn in Group Annnmmm CREX Edition 2, mmm in Group Annnmmm\
of Section 1 of Section 1

Code figure Name Code figure Name (corresponding traditional\
alphanumeric codes are in brackets)

30 Calibration dataset 0 Subsetted data

(satellite) 1 Collocated data

2 On-board calibration data

3 Bias monitoring

4 Near-real-time correction

5 Re-analysis correction

31 Oceanographic data 0 Surface observation

1 Surface observation along track (TRACKOB)

2 Spectral wave observation (WAVEOB)

3 Bathythermal observation (BATHY)

4 Subsurface floats (profile)

5 XBT/XCTD profiles (TESAC)

6 Waves reports

7 Tsunameter data

101 Image data (satellite) 0 Multi-purpose VIS/IR imagery

1 Conical scanning MW imagery\
(intermediate frequencies)

2 Low frequency MW imagery

3 Ocean colour imagery

4 Imagery with special viewing geometry

5 Lightning imagery

6 High-resolution short-wave imagery for land\
observation

7 SMOS data

**COMMON CODE TABLE C--14: *Atmospheric chemical or physical constituent type***

Common Code table Code table 4.230 in GRIB Edition 2

Code figure Meaning Chemical formula

0 Ozone O~3~

1 Water vapour H~2~O

2 Methane CH~4~

3 Carbon dioxide CO~2~

4 Carbon monoxide CO

5 Nitrogen dioxide NO~2~

6 Nitrous oxide N~2~O

7 Formaldehyde HCHO

8 Sulphur dioxide SO~2~

9 Ammonia NH~3~

10 Ammonium NH~4~^+^

11 Nitrogen monoxide NO

12 Atomic oxygen O

13 Nitrate radical NO~3~

14 Hydroperoxyl radical HO~2~

15 Dinitrogen pentoxide N~2~O~5~

16 Nitrous acid HONO

17 Nitric acid HNO~3~

18 Peroxynitric acid HO~2~NO~2~

19 Hydrogen peroxide H~2~O~2~

20 Molecular hydrogen H~2~

21 Atomic nitrogen N

22 Sulphate SO~4~^2--^

23 Radon Rn

24 Elemental mercury Hg(0)

25 Divalent mercury Hg^2+^

26 Atomic chlorine Cl

27 Chlorine monoxide ClO

28 Dichlorine peroxide Cl~2~O~2~

29 Hypochlorous acid HClO

30 Chlorine nitrate ClONO~2~

31 Chlorine dioxide ClO~2~

32 Atomic bromine Br

33 Bromine monoxide BrO

34 Bromine chloride BrCl

35 Hydrogen bromide HBr

36 Hypobromous acid HBrO

37 Bromine nitrate BrONO~2~

38 Oxygen O~2~

39-9999 Reserved

10000 Hydroxyl radical OH

10001 Methyl peroxy radical CH~3~O~2~

10002 Methyl hydroperoxide CH~3~O~2~H

10004 Methanol CH~3~OH

10005 Formic acid CH~3~OOH

10006 Hydrogen cyanide HCN

10007 Aceto nitrile CH~3~CN

10008 Ethane C~2~H~6~

10009 Ethene (= Ethylene) C~2~H~4~

10010 Ethyne (= Acetylene) C~2~H~2~

10011 Ethanol C~2~H~5~OH

10012 Acetic acid C~2~H~5~OOH

10013 Peroxyacetyl nitrate CH~3~C(O)OONO~2~

10014 Propane C~3~H~8~

10015 Propene C~3~H~6~

Code figure Meaning Chemical formula

10016 Butanes C~4~H~10~

10017 Isoprene C~5~H~10~

10018 Alpha pinene C~10~H~16~

10019 Beta pinene C~10~H~16~

10020 Limonene C~10~H~16~

10021 Benzene C~6~H~6~

10022 Toluene C~7~H~8~

10023 Xylene C~8~H~10~

10024--10499 Reserved for other simple organic molecules\
(e.g. higher aldehydes, alcohols, peroxides,...)

10500 Dimethyl sulphide CH~3~SCH~3~ (DMS)

10501--20000 Reserved

20001 Hydrogen chloride

20002 CFC-11

20003 CFC-12

20004 CFC-113

20005 CFC-113a

20006 CFC-114

20007 CFC-115

20008 HCFC-22

20009 HCFC-141b

20010 HCFC-142b

20011 Halon-1202

20012 Halon-1211

20013 Halon-1301

20014 Halon-2402

20015 Methyl chloride (HCC-40)

20016 Carbon tetrachloride (HCC-10)

20017 HCC-140a CH~3~CCl~3~

20018 Methyl bromide (HBC-40B1)

20019 Hexachlorocyclohexane (HCH)

20020 Alpha hexachlorocyclohexane

20021 Hexachlorobiphenyl (PCB-153)

20022--29999 Reserved

30000 Radioactive pollutant (tracer, defined by originating centre)

30001--30009 Reserved

30010 Hydrogen H-3

30011 Hydrogen organic bounded H-3o

30012 Hydrogen inorganic H-3a

30013 Beryllium 7 Be-7

30014 Beryllium 10 Be-10

30015 Carbon 14 C-14

30016 Carbon 14 CO~2~ C-14CO~2~

30017 Carbon 14 other gases C-14og

30018 Nitrogen 13 N-13

30019 Nitrogen 16 N-16

30020 Fluorine 18 F-18

30021 Sodium 22 Na-22

30022 Phosphate 32 P-32

30023 Phosphate 33 P-33

30024 Sulphur 35 S-35

30025 Chlorine 36 Cl-36

30026 Potassium 40 K-40

30027 Argon 41 Ar-41

30028 Calcium 41 Ca-41

30029 Calcium 45 Ca-45

30030 Titanium 44 Ti-44

Code figure Meaning Chemical formula

30031 Scandium 46 Sc-46

30032 Vanadium 48 V-48

30033 Vanadium 49 V-49

30034 Chrome 51 Cr-51

30035 Manganese 52 Mn-52

30036 Manganese 54 Mn-54

30037 Iron 55 Fe-55

30038 Iron 59 Fe-59

30039 Cobalt 56 Co-56

30040 Cobalt 57 Co-57

30041 Cobalt 58 Co-58

30042 Cobalt 60 Co-60

30043 Nickel 59 Ni-59

30044 Nickel 63 Ni-63

30045 Zinc 65 Zn-65

30046 Gallium 67 Ga-67

30047 Gallium 68 Ga-68

30048 Germanium 68 Ge-68

30049 Germanium 69 Ge-69

30050 Arsenic 73 As-73

30051 Selenium 75 Se-75

30052 Selenium 79 Se-79

30053 Rubidium 81 Rb-81

30054 Rubidium 83 Rb-83

30055 Rubidium 84 Rb-84

30056 Rubidium 86 Rb-86

30057 Rubidium 87 Rb-87

30058 Rubidium 88 Rb-88

30059 Krypton 85 Kr-85

30060 Krypton 85 metastable Kr-85m

30061 Krypton 87 Kr-87

30062 Krypton 88 Kr-88

30063 Krypton 89 Kr-89

30064 Strontium 85 Sr-85

30065 Strontium 89 Sr-89

30066 Strontium 89/90 Sr-8990

30067 Strontium 90 Sr-90

30068 Strontium 91 Sr-91

30069 Strontium 92 Sr-92

30070 Yttrium 87 Y-87

30071 Yttrium 88 Y-88

30072 Yttrium 90 Y-90

30073 Yttrium 91 Y-91

30074 Yttrium 91 metastable Y-91m

30075 Yttrium 92 Y-92

30076 Yttrium 93 Y-93

30077 Zirconium 89 Zr-89

30078 Zirconium 93 Zr-93

30079 Zirconium 95 Zr-95

30080 Zirconium 97 Zr-97

30081 Niobium 93 metastable Nb-93m

30082 Niobium 94 Nb-94

30083 Niobium 95 Nb-95

30084 Niobium 95 metastable Nb-95m

30085 Niobium 97 Nb-97

30086 Niobium 97 metastable Nb-97m

30087 Molybdenum 93 Mo-93

30088 Molybdenum 99 Mo-99

Code figure Meaning Chemical formula

30089 Technetium 95 metastable Tc-95m

30090 Technetium 96 Tc-96

30091 Technetium 99 Tc-99

30092 Technetium 99 metastable Tc-99m

30093 Rhodium 99 Rh-99

30094 Rhodium 101 Rh-101

30095 Rhodium 102 metastable Rh-102m

30096 Rhodium 103 metastable Rh-103m

30097 Rhodium 105 Rh-105

30098 Rhodium 106 Rh-106

30099 Palladium 100 Pd-100

30100 Palladium 103 Pd-103

30101 Palladium 107 Pd-107

30102 Ruthenium 103 Ru-103

30103 Ruthenium 105 Ru-105

30104 Ruthenium 106 Ru-106

30105 Silver 108 metastable Ag-108m

30106 Silver 110 metastable Ag-110m

30107 Cadmium 109 Cd-109

30108 Cadmium 113 metastable Cd-113m

30109 Cadmium 115 metastable Cd-115m

30110 Indium 114 metastable In-114m

30111 Tin 113 Sn-113

30112 Tin 119 metastable Sn-119m

30113 Tin 121 metastable Sn-121m

30114 Tin 122 Sn-122

30115 Tin 123 Sn-123

30116 Tin 126 Sn-126

30117 Antimony 124 Sb-124

30118 Antimony 125 Sb-125

30119 Antimony 126 Sb-126

30120 Antimony 127 Sb-127

30121 Antimony 129 Sb-129

30122 Tellurium 123 metastable Te-123m

30123 Tellurium 125 metastable Te-125m

30124 Tellurium 127 Te-127

30125 Tellurium 127 metastable Te-127m

30126 Tellurium 129 Te-129

30127 Tellurium 129 metastable Te-129m

30128 Tellurium 131 metastable Te-131m

30129 Tellurium 132 Te-132

30130 Iodine 123 I-123

30131 Iodine 124 I-124

30132 Iodine 125 I-125

30133 Iodine 126 I-126

30134 Iodine 129 I-129

30135 Iodine 129 elementary gaseous I-129g

30136 Iodine 129 organic bounded I-129o

30137 Iodine 131 I-131

30138 Iodine 131 elementary gaseous I-131g

30139 Iodine 131 organic bounded I-131o

30140 Iodine 131 gaseous elementary and organic bounded I-131go

30141 Iodine 131 aerosol I-131a

30142 Iodine 132 I-132

30143 Iodine 132 elementary gaseous I-132g

30144 Iodine 132 organic bounded I-132o

30145 Iodine 132 gaseous elementary and organic bounded I-132go

Code figure Meaning Chemical formula

30146 Iodine 132 aerosol I-132a

30147 Iodine 133 I-133

30148 Iodine 133 elementary gaseous I-133g

30149 Iodine 133 organic bounded I-133o

30150 Iodine 133 gaseous elementary and organic bounded I-133go

30151 Iodine 133 aerosol I-133a

30152 Iodine 134 I-134

30153 Iodine 134 elementary gaseous I-134g

30154 Iodine 134 organic bounded I-134o

30155 Iodine 135 I-135

30156 Iodine 135 elementary gaseous I-135g

30157 Iodine 135 organic bounded I-135o

30158 Iodine 135 gaseous elementary and organic bounded I-135go

30159 Iodine 135 aerosol I-135a

30160 Xenon 131 metastable Xe-131m

30161 Xenon 133 Xe-133

30162 Xenon 133 metastable Xe-133m

30163 Xenon 135 Xe-135

30164 Xenon 135 metastable Xe-135m

30165 Xenon 137 Xe-137

30166 Xenon 138 Xe-138

30167 Xenon sum of all Xenon isotopes Xe-sum

30168 Caesium 131 Cs-131

30169 Caesium 134 Cs-134

30170 Caesium 135 Cs-135

30171 Caesium 136 Cs-136

30172 Caesium 137 Cs-137

30173 Barium 133 Ba-133

30174 Barium 137 metastable Ba-137m

30175 Barium 140 Ba-140

30176 Cerium 139 Ce-139

30177 Cerium 141 Ce-141

30178 Cerium 143 Ce-143

30179 Cerium 144 Ce-144

30180 Lanthanum 140 La-140

30181 Lanthanum 141 La-141

30182 Praseodymium 143 Pr-143

30183 Praseodymium 144 Pr-144

30184 Praseodymium 144 metastable Pr-144m

30185 Samarium 145 Sm-145

30186 Samarium 147 Sm-147

30187 Samarium 151 Sm-151

30188 Neodymium 147 Nd-147

30189 Promethium 146 Pm-146

30190 Promethium 147 Pm-147

30191 Promethium 151 Pm-151

30192 Europium 152 Eu-152

30193 Europium 154 Eu-154

30194 Europium 155 Eu-155

30195 Gadolinium 153 Gd-153

30196 Terbium 160 Tb-160

30197 Holmium 166 metastable Ho-166m

30198 Thulium 170 Tm-170

30199 Ytterbium 169 Yb-169

30200 Hafnium 175 Hf-175

30201 Hafnium 181 Hf-181

30202 Tantalum 179 Ta-179

Code figure Meaning Chemical formula

30203 Tantalum 182 Ta-182

30204 Rhenium 184 Re-184

30205 Iridium 192 Ir-192

30206 Mercury 203 Hg-203

30207 Thallium 204 Tl-204

30208 Thallium 207 Tl-207

30209 Thallium 208 Tl-208

30210 Thallium 209 Tl-209

30211 Bismuth 205 Bi-205

30212 Bismuth 207 Bi-207

30213 Bismuth 210 Bi-210

30214 Bismuth 211 Bi-211

30215 Bismuth 212 Bi-212

30216 Bismuth 213 Bi-213

30217 Bismuth 214 Bi-214

30218 Polonium 208 Po-208

30219 Polonium 210 Po-210

30220 Polonium 212 Po-212

30221 Polonium 213 Po-213

30222 Polonium 214 Po-214

30223 Polonium 215 Po-215

30224 Polonium 216 Po-216

30225 Polonium 218 Po-218

30226 Lead 209 Pb-209

30227 Lead 210 Pb-210

30228 Lead 211 Pb-211

30229 Lead 212 Pb-212

30230 Lead 214 Pb-214

30231 Astatine 217 At-217

30232 Radon 219 Rn-219

30233 Radon 220 Rn-220

30234 Radon 222 Rn-222

30235 Francium 221 Fr-221

30236 Francium 223 Fr-223

30237 Radium 223 Ra-223

30238 Radium 224 Ra-224

30239 Radium 225 Ra-225

30240 Radium 226 Ra-226

30241 Radium 228 Ra-228

30242 Actinium 225 Ac-225

30243 Actinium 227 Ac-227

30244 Actinium 228 Ac-228

30245 Thorium 227 Th-227

30246 Thorium 228 Th-228

30247 Thorium 229 Th-229

30248 Thorium 230 Th-230

30249 Thorium 231 Th-231

30250 Thorium 232 Th-232

30251 Thorium 234 Th-234

30252 Protactinium 231 Pa-231

30253 Protactinium 233 Pa-233

30254 Protactinium 234 metastable Pa-234m

30255 Uranium 232 U-232

30256 Uranium 233 U-233

30257 Uranium 234 U-234

30258 Uranium 235 U-235

30259 Uranium 236 U-236

Code figure Meaning Chemical formula

30260 Uranium 237 U-237

30261 Uranium 238 U-238

30262 Plutonium 236 Pu-236

30263 Plutonium 238 Pu-238

30264 Plutonium 239 Pu-239

30265 Plutonium 240 Pu-240

30266 Plutonium 241 Pu-241

30267 Plutonium 242 Pu-242

30268 Plutonium 244 Pu-244

30269 Neptunium 237 Np-237

30270 Neptunium 238 Np-238

30271 Neptunium 239 Np-239

30272 Americium 241 Am-241

30273 Americium 242 Am-242

30274 Americium 242 metastable Am-242m

30275 Americium 243 Am-243

30276 Curium 242 Cm-242

30277 Curium 243 Cm-243

30278 Curium 244 Cm-244

30279 Curium 245 Cm-245

30280 Curium 246 Cm-246

30281 Curium 247 Cm-247

30282 Curium 248 Cm-248

30283 Curium 243/244 Cm-243244

30284 Plutonium 238/Americium 241 Pu-238Am-241

30285 Plutonium 239/240 Pu-239240

30286 Berkelium 249 Bk-249

30287 Californium 249 Cf-249

30288 Californium 250 Cf-250

30289 Californium 252 Cf-252

30290 Sum aerosol particulates SumAer

30291 Sum Iodine SumIod

30292 Sum noble gas SumNG

30293 Activation gas ActGas

30294 Cs-137 Equivalent EquCs137

30295--59999 Reserved

60000 HO~x~ radical (OH+HO~2~)

60001 Total inorganic and organic RO~2~\
peroxy radicals (HO~2~ + RO~2~)

60002 Passive Ozone

60003 NO~x~ expressed as nitrogen NO~x~

60004 All nitrogen oxides (NO~y~) expressed as nitrogen NO~y~

60005 Total inorganic chlorine Cl~x~

60006 Total inorganic bromine Br~x~

60007 Total inorganic chlorine except HCl, ClONO~2~: ClO~x~

60008 Total inorganic bromine except HBr, BrONO~2~: BrO~x~

60009 Lumped alkanes

60010 Lumped alkenes

60011 Lumped aromatic compounds

60012 Lumped terpenes

60013 Non-methane volatile organic compounds NMVOC

expressed as carbon

60014 Anthropogenic non-methane volatile organic aNMVOC

compounds expressed as carbon

60015 Biogenic non-methane volatile organic compounds bNMVOC

expressed as carbon

60016 Lumped oxygenated hydrocarbons OVOC

60017 NO~x~ expressed as nitrogen dioxide (NO~2~) NO~x~

60018--61999 Reserved

Code figure Meaning Chemical formula

62000 Total aerosol

62001 Dust dry

62002 Water in ambient

62003 Ammonium dry

62004 Nitrate dry

62005 Nitric acid trihydrate

62006 Sulphate dry

62007 Mercury dry

62008 Sea salt dry

62009 Black carbon dry

62010 Particulate organic matter dry

62011 Primary particulate organic matter dry

62012 Secondary particulate organic matter dry

62013 Black carbon hydrophilic dry

62014 Black carbon hydrophobic dry

62015 Particulate organic matter hydrophilic dry

62016 Particulate organic matter hydrophobic dry

62017 Nitrate hydrophilic dry

62018 Nitrate hydrophobic dry

62019 Reserved

62020 Smoke -- high absorption

62021 Smoke -- low absorption

62022 Aerosol -- high absorption

62023 Aerosol -- low absorption

62024 Reserved

62025 Volcanic ash

62026 Particulate matter (PM)

62027--62099 Reserved

62100 Alnus (alder) pollen

62101 Betula (birch) pollen

62102 Castanea (chestnut) pollen

62103 Carpinus (hornbeam) pollen

62104 Corylus (hazel) pollen

62105 Fagus (beech) pollen

62106 Fraxinus (ash) pollen

62107 Pinus (pine) pollen

62108 Platanus (plane) pollen

62109 Populus (cottonwood, poplar) pollen

62110 Quercus (oak) pollen

62111 Salix (willow) pollen

62112 Taxus (yew) pollen

62113 Tilia (lime, linden) pollen

62114 Ulmus (elm) pollen

62115--62199 Reserved

62200 Ambrosia (ragweed, burr-ragweed) pollen

62201 Artemisia (sagebrush, wormwood, mugwort) pollen

62202 Brassica (rape, broccoli, Brussels sprouts, cabbage, cauliflower, collards, kale,\
kohlrabi, mustard, rutabaga) pollen

62203 Plantago (plantain) pollen

62204 Rumex (dock, sorrel) pollen

62205 Urtica (nettle) pollen

62206--62299 Reserved

62300 Poaceae (grass family) pollen

62301--65534 Reserved

65535 Missing

\_\_\_\_\_\_\_\_\_\_\_\_
