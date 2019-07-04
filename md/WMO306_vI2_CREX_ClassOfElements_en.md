**CREX TABLES RELATIVE TO SECTION 2**

**CREX Table B** *-- Classification of elements*

F X Class Comments

B 00 BUFR/CREX table entries

B 01 Identification Identifies origin and type of data

B 02 Instrumentation Defines instrument types used

B 03 Instrumentation Defines instrument types used

B 04 Location (time) Defines time and time derivatives

B 05 Location (horizontal -- 1) Defines geographical position, including horizontal

derivatives, in association with Class 06 (first dimension of

horizontal space)

B 06 Location (horizontal -- 2) Defines geographical position, including horizontal

derivatives, in association with Class 05 (second

dimension of horizontal space)

B 07 Location (vertical) Defines height, altitude, pressure level, including vertical

derivatives of position

B 08 Significance qualifiers Defines special character of data

B 09 Reserved

B 10 Non-coordinate location (vertical) Height, altitude, pressure and derivatives observed or measured,

*not* defined as a vertical location

B 11 Wind and turbulence Wind speed, direction, etc.

B 12 Temperature

B 13 Hydrographic and Humidity, rainfall, snowfall, etc.\
hydrological elements

B 14 Radiation and radiance

B 15 Physical/chemical constituents

B 19 Synoptic features

B 20 Observed phenomena Defines present/past weather, special phenomena, etc.

B 21 Radar data

B 22 Oceanographic elements

B 23 Dispersal and transport

B 24 Radiological elements

B 25 Processing information

B 26 Non-coordinate location (time) Defines time and time derivatives that are not coordinates

B 27 Non-coordinate location Defines geographical positions, in conjunction

(horizontal -- 1) with Class 28, that are not coordinates

B 28 Non-coordinate location Defines geographical positions, in conjunction

(horizontal -- 2) with Class 27, that are not coordinates

B 29 Map data

B 30 Image

B 33 Quality information

B 35 Data monitoring information

B 40 Satellite data

B 41 **Oceanographic/biogeochemical parameters**

B 42 **Oceanographic elements**

*(continued)*

*\
(CREX Table B -- continued)*

Notes:

\(1) Where a code table or flag table is appropriate, "code table" or "flag table", respectively is entered in the UNIT column.

\(2) The code tables and flag tables associated with Table B are numbered to correspond with the xx and yyy part of the table reference.

\(3) To encode values into CREX, the data (with units as specified in the UNIT column) must be multiplied by 10 to the power SCALE.

\(4) Where a UNIT is given as Character, data shall be coded as character data left justified within the field width.

\(5) Classes 48 to 63 are reserved for local use; all other classes are reserved for future development.

\(6) Entries 192 to 255 within all classes are reserved for local use.

\(7) The use of local descriptors, as defined in Notes 5 and 6, in messages intended for non-local or international exchange is strongly discouraged.

\(8) First-order statistics are included in Table B only when they are produced, as such, by the observing system.

CREX Table B entries from Classes 00 to 42 are defined in BUFR/CREX Table B in Part B, Binary codes, of the Manual.

Note: Class 31 does not exist in CREX.

\_\_\_\_\_\_\_\_\_\_\_\_
