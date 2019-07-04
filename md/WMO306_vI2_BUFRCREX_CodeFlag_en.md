**CODE TABLES AND FLAG TABLES ASSOCIATED WITH BUFR/CREX TABLE B**

Note: In developing code tables associated with BUFR/CREX Table B to specify units of elements, the following principles should be applied:

\(a) Code tables specifying the units for an element which is defined, in the *Manual on Codes*, by a single symbolic letter shall be compatible with the relevant existing WMO code tables;

\(b) Code tables combining two or more existing WMO code tables to specify the units for an element which is defined, in the *Manual on Codes*, by a group of symbolic letters shall be compatible with the combined code figures of the relevant group of symbolic letters;

\(c) Code tables combining two or more existing WMO code tables to specify the units for an element which is defined, in the *Manual on Codes*, by different symbolic letters shall be compatible with the code figures of the relevant symbolic letters, with successive tens or hundreds values added, as appropriate;

\(d) Code tables and flag tables should only be used for reporting qualitative information. Quantitative information should be reported as observed using entries in Table B. "Data description operators" from Table C should be applied when a "scale change" or "data width change" is required;

\(e) Reference to existing specification(s) and code table(s) in the *Manual on Codes*, with explanation of possible deviations, shall be given in an additional table annexed to the code tables associated with BUFR/CREX Table B.

**0 01 003**

***WMO Region number/geographical area***

Code figure

0 Antarctica

1 Region I

2 Region II

3 Region III

4 Region IV

5 Region V

6 Region VI

7 Missing value

**0 01 007**

***Satellite identifier***

*(See common Code table C--5 Part C/c.)*

**0 01 024**

***Wind speed source***

Code figure

0 No wind speed data available

1 AMSR-E data

2 TMI data

3 NWP: ECMWF

4 NWP: UK Met Office

5 NWP: NCEP

6 Reference climatology

7 ERS\_scatterometer

8--30 Reserved for future use

31 Missing value

**0 01 028**

***Aerosol optical depth (AOD) source***

Code figure

0 No AOD data available

1 NESDIS

2 NAVOCEANO

3 NAAPS

4 MERIS

5 AATSR

6--30 Reserved for future use

31 Missing value

**0 01 029**

***SSI\* source***

Code figure

0 No SSI data available

1 MSG\_SEVIRI

2 GOES East

3 GOES West

4 ECMWF

5 NCEP

6 UK Met Office

7--30 Reserved for future use

31 Missing value

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\* Surface solar irradiance

**0 01 031**

***Identification of originating/generating centre***

*(See common Code table C--1 in Part C/c.)*

**0 01 033**

***Identification of originating/generating centre***

*(See common Code table C--1 in Part C/c.)*

**0 01 034**

***Identification of originating/generating sub-centre***

*(To be defined by centres themselves --\
See common Code table C--12 in Part C/c.)*

**0 01 036**

***Agency in charge of operating the observing platform***

*(The first three digits represent the ISO country code)*

Code figure

0--36000 Reserved

36001 Australia, Bureau of Meteorology (BoM)

36002 Australia, Joint Australian Facility for Ocean Observing Systems (JAFOOS)

36003 Australia, the Commonwealth Scientific and Industrial Research Organization (CSIRO)

36004--124000 Reserved

124001 Canada, Marine Environmental Data Service (MEDS)

124002 Canada, Institute of Ocean Sciences (IOS)

124003--124172 Reserved

124173 Canada, Environment Canada

124174 Canada, Department of National Defence

*(continued)*

*\
(Code table 0 01 036 -- continued)*

Code figure

124175 Canada, Nav Canada

124176--156000 Reserved

156001 China, The State Oceanic Administration

156002 China, Second Institute of Oceanography, State Oceanic Administration

156003 China, Institute of Ocean Technology

156004--250000 Reserved

250001 France, Institut de Recherche pour le Développement (IRD)

250002 France, Institut Français de Recherche pour l'Exploitation de la mer (IFREMER)

250003--276000 Reserved

276001 Germany, Bundesamt fuer Seeschiffahrt und Hydrographie (BSH)

276002 Germany, Institut fuer Meereskunde, Kiel

276003--356000 Reserved

356001 India, National Institute of Oceanography (NIO)

356002 India, National Institute for Ocean Technology (NIOT)

356003 India, National Centre for Ocean Information Service

356004--392000 Reserved

392001 Japan, Japan Meteorological Agency (JMA)

392002 Japan, Frontier Observational Research System for Global Change

392003 Japan, Japan Marine Science and Technology Centre (JAMSTEC)

392004--410000 Reserved

410001 Republic of Korea, Seoul National University

410002 Republic of Korea, Korea Ocean Research and Development Institute (KORDI)

410003 Republic of Korea, Meteorological Research Institute

410004--540000 Reserved

540001 New Caledonia, Institut de Recherche pour le Développement (IRD)

540002--554000 Reserved

554001 New Zealand, National Institute of Water and Atmospheric Research (NIWA)

554002--643000 Reserved

643001 Russian Federation, State Oceanographic Institute of Roshydromet

643002 Russian Federation, Federal Service for Hydrometeorology and Environmental\
Monitoring

643003--724000 Reserved

724001 Spain, Instituto Español de Oceanografía

724002--826000 Reserved

826001 United Kingdom, Hydrographic Office

826002 United Kingdom, Southampton Oceanography Centre (SOC)

826003--840000 Reserved

840001 USA, NOAA Atlantic Oceanographic and Meteorological Laboratories (AOML)

840002 USA, NOAA Pacific Marine Environmental Laboratories (PMEL)

840003 USA, Scripps Institution of Oceanography (SIO)

840004 USA, Woods Hole Oceanographic Institution (WHOI)

840005 USA, University of Washington

840006 USA, Naval Oceanographic Office

840007--1048574 Reserved

1048575 Missing value

**\
**

**0 01 038**

***Source of sea-ice fraction***

Code figure

0 No sea-ice set

1 NSIDC SSM/I Cavalieri et al (1992)

2 AMSR-E

3 ECMWF

4 CMS (France) cloud mask used by Medspiration

5 EUMETSAT OSI-SAF

6--30 Reserved for future use

31 Missing value

**0 01 044**

***Standard generating application***

Code figure

0 Reserved

1 Full weighted mixture of individual quality tests

2 Weighted mixture of individual tests, but excluding forecast comparison

3 Recursive filter function

4 Common quality index (QI) without forecast

5 QI without forecast

6 QI with forecast

7 Estimated error in m/s converted to a percent confidence

8--254 Reserved

255 Missing value

**0 01 052**

***Platform transmitter ID***

Code figure

0 Primary

1 Secondary

2 Reserved

3 Missing value

**\
**

**0 01 090**

***Technique for making up initial perturbations***

Code figure

0 Lagged-average forecasting (LAF)

1 Breeding

2 Singular vectors

3 Multiple analysis cycles

4--191 Reserved

192--254 Reserved for local use

255 Missing value

**0 01 092**

***Type of ensemble forecast***

Code figure

0 Unperturbed high-resolution control forecast

1 Unperturbed low-resolution control forecast

2 Negatively perturbed forecast

3 Positively perturbed forecast

4--191 Reserved

192--254 Reserved for local use

255 Missing value

**0 01 101**

***State identifier***

Code figure

0--99 Reserved

100 Algeria

101 Angola

102 Benin

103 Botswana

104 Burkina Faso

105 Burundi

106 Cameroon

107 Cabo Verde

108 Central African Republic

109 Chad

110 Comoros

111 Congo

112 Côte d'Ivoire

113 Democratic Republic of the Congo

114 Djibouti

115 Egypt

116 Eritrea

117 Ethiopia

118 France (RA I)

119 Gabon

120 Gambia

121 Ghana

122 Guinea

123 Guinea-Bissau

124 Kenya

125 Lesotho

126 Liberia

127 Libya

128 Madagascar

129 Malawi

130 Mali

131 Mauritania

132 Mauritius

133 Morocco

134 Mozambique

135 Namibia

136 Niger

137 Nigeria

138 Portugal (RA I)

139 Rwanda

140 Sao Tome and Principe

*(continued)*

*\
(Code table 0 01 101 -- continued)*

Code figure

141 Senegal

142 Seychelles

143 Sierra Leone

144 Somalia

145 South Africa

146 Spain (RA I)

147 Sudan

148 Eswatini

149 Togo

150 Tunisia

151 Uganda

152 United Kingdom of Great Britain and Northern Ireland (RA I)

153 United Republic of Tanzania

154 Zambia

155 Zimbabwe

156--199 Reserved for Region I (Africa)

200 Afghanistan

201 Bahrain

202 Bangladesh

203 Bhutan

204 Cambodia

205 China

206 Democratic People's Republic of Korea

207 Hong Kong, China

208 India

209 Iran, Islamic Republic of

210 Iraq

211 Japan

212 Kazakhstan

213 Kuwait

214 Kyrgyzstan

215 Lao People's Democratic Republic

216 Macao, China

217 Maldives

218 Mongolia

219 Myanmar

220 Nepal

221 Oman

222 Pakistan

223 Qatar

224 Republic of Korea

225 Yemen

226 Russian Federation (RA II)

227 Saudi Arabia

228 Sri Lanka

*(continued)*

*\
(Code table 0 01 101 -- continued)*

Code figure

229 Tajikistan

230 Thailand

231 Turkmenistan

232 United Arab Emirates

233 Uzbekistan

234 Viet Nam

235--299 Reserved for Region II (Asia)

300 Argentina

301 Bolivia (Plurinational State of)

302 Brazil

303 Chile

304 Colombia

305 Ecuador

306 France (RA III)

307 Guyana

308 Paraguay

309 Peru

310 Suriname

311 Uruguay

312 Venezuela (Bolivarian Republic of)

313--399 Reserved for Region III (South America)

400 Antigua and Barbuda

401 Bahamas

402 Barbados

403 Belize

404 British Caribbean Territories

405 Canada

406 Colombia

407 Costa Rica

408 Cuba

409 Dominica

410 Dominican Republic

411 El Salvador

412 France (RA IV)

413 Guatemala

414 Haiti

415 Honduras

416 Jamaica

417 Mexico

418 Curaçao and Sint Maarten

419 Nicaragua

420 Panama

421 Saint Lucia

422 Trinidad and Tobago

*(continued)*

*\
(Code table 0 01 101 -- continued)*

Code figure

423 United Kingdom of Great Britain and Northern Ireland (RA IV)

424 United States of America (RA IV)

425 Venezuela (Bolivarian Republic of)

426--499 Reserved for Region IV (North America, Central America and the Caribbean)

500 Australia

501 Brunei Darussalam

502 Cook Islands

503 Fiji

504 French Polynesia

505 Indonesia

506 Kiribati

507 Malaysia

508 Micronesia, Federated States of

509 New Caledonia

510 New Zealand

511 Niue

512 Papua New Guinea

513 Philippines

514 Samoa

515 Singapore

516 Solomon Islands

517 Tonga

518 United Kingdom of Great Britain and Northern Ireland (RA V)

519 United States of America (RA V)

520 Vanuatu

521--599 Reserved for Region V (South-West Pacific)

600 Albania

601 Armenia

602 Austria

603 Azerbaijan

604 Belarus

605 Belgium

606 Bosnia and Herzegovina

607 Bulgaria

608 Croatia

609 Cyprus

610 Czechia

611 Denmark

612 Estonia

613 Finland

614 France (RA VI)

615 Georgia

616 Germany

617 Greece

*(continued)*

*\
* *(Code table 0 01 101 -- continued)*

Code figure

618 Hungary

619 Iceland

620 Ireland

621 Israel

622 Italy

623 Jordan

624 Kazakhstan

625 Latvia

626 Lebanon

627 Lithuania

628 Luxembourg

629 Malta

630 Monaco

631 Montenegro

632 Netherlands

633 Norway

634 Poland

635 Portugal (RA VI)

636 Republic of Moldova

637 Romania

638 Russian Federation (RA VI)

639 Serbia

640 Slovakia

641 Slovenia

642 Spain (RA VI)

643 Sweden

644 Switzerland

645 Syrian Arab Republic

646 The former Yugoslav Republic of Macedonia

647 Turkey

648 Ukraine

649 United Kingdom of Great Britain and Northern Ireland (RA VI)

650--699 Reserved for Region VI (Europe)

700--999 Reserved

1000--1022 Not used

1023 Missing value

**\
**

**0 01 150**

***Coordinate reference system***

Code figure

0 WGS84, as used by ICAO since 1998

1 ETRS89, as defined by EPSG:4258

2 NAD83, as defined by EPSG:4269

3 DHDN, as defined by EPSG:4314

4 Ellipsoidal datum using the International Reference Meridian and the International Reference Pole as the prime meridian and prime pole, respectively, and the origin of the International Terrestrial Reference System (ITRS) (see Note 2). The International Reference Meridian, International Reference Pole and ITRS are maintained by the International Earth Rotation and Reference Systems Service (IERS)

5--65534 Reserved

65535 Missing value

Notes:

\(1) EPSG is a dataset of coordinate system and coordinate system transformations, originally produced and maintained by the European Petroleum Survey Group. It is now maintained by the Geodesy Subcommittee of the International Association of Oil and Gas Producers Geomatics Committee.

\(2) When Code figure 4 is used to specify a custom coordinate reference system, the ellipsoidal datum shall be an oblate ellipsoid of revolution, where the major axis is uniplanar with the equatorial plane and the minor axis traverses the prime meridian towards the prime pole. North corresponds to the direction from the Equator to the prime pole. East corresponds to the counterclockwise direction from the prime meridian as viewed from above the North Pole. In this case, the semi-major and semi-minor axes must be specified (e.g. by descriptors 0 01 152 and 0 01 153).

**0 01 151**

***Fixed mean sea-level reference datum***

Code figure

0 Earth Gravitational Model 1996

1 Baltic height system 1977

2--4094 Reserved

4095 Missing value

**0 02 001**

***Type of station***

Code figure

0 Automatic

1 Manned

2 Hybrid: both manned and automatic

3 Missing value

**0 02 002**

***Type of instrumentation for wind measurement***

Bit No. Type of Instrumentation and original units for wind measurement\
(measured in m s^--1^ unless otherwise indicated)

1 Certified instruments

2 Originally measured in knots

3 Originally measured in km h^--1^

All 4 Missing value

**0 02 003**

***Type of measuring equipment used***

Code figure

0 Pressure instrument associated with wind measuring equipment

1 Optical theodolite

2 Radio theodolite

3 Radar

4 VLF-Omega

5 Loran C

6 Wind profiler

7 Satellite navigation

8 Radio-acoustic Sounding System (RASS)

9 Sodar

10 Lidar

11--13 Reserved

14 Pressure instrument associated with wind measuring equipment but pressure element failed during ascent

15 Missing value

**0 02 004**

***Type of instrumentation for evaporation measurement or type\
of crop for which evapotranspiration is reported***

Code figure Instrumentation or crop type Type of data

0 USA open pan evaporimeter (without cover)

1 USA open pan evaporimeter (mesh covered)

2 GGI-3000 evaporimeter (sunken) Evaporation

3 20 m^2^ tank

4 Others

5 Rice

6 Wheat

7 Maize Evapotranspiration

8 Sorghum

9 Other crops

10--14 Reserved

15 Missing value

**0 02 007**

***Type of sensor for water level measuring instrument***

Code figure

0 Reserved

1 Shaft encoder float system

2 Ultrasonic

3 Radar

4 Pressure (single transducer)

5 Pressure (multiple transducer)

6 Pressure (in stilling well)

7 Bubbler pressure

8 Acoustic (with sounding tube)

9 Acoustic (in open air)

10--62 Reserved

63 Missing value

**0 02 008**

***Type of offshore platform***

Code figure

0 Fixed platform

1 Mobile offshore drill ship

2 Jack-up rig

3 Semi-submersible platform

4 Floating production storage and offloading (FPSO) unit

5 Light vessel

6--14 Reserved

15 Missing value

**0 02 011**

***Radiosonde type***

*(See common Code table C--2 in Part C/c.)*

**0 02 012**

***Radiosonde computational method***

*(To be developed)*

**0 02 013**

***Solar and infrared radiation correction***

Code figure

0 No correction

1 CIMO solar corrected and CIMO infrared corrected

2 CIMO solar corrected and infrared corrected

3 CIMO solar corrected only

4 Solar and infrared corrected automatically by radiosonde system

5 Solar corrected automatically by radiosonde system

6 Solar and infrared corrected as specified by country

7 Solar corrected as specified by country

8 Solar and infrared corrected as specified by GRUAN\*

9 Solar corrected as specified by GRUAN

10--14 Reserved

15 Missing value

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\* GRUAN = GCOS Reference Upper-Air Network

**0 02 014**

***Tracking technique/status of system used***

*(See common Code table C--7 in Part C/c.)*

**0 02 015**

***Radiosonde completeness***

Code figure

0 Reserved

1 Pressure only radiosonde

2 Pressure only radiosonde plus transponder

3 Pressure only radiosonde plus radar reflector

4 No-pressure radiosonde plus transponder

5 No-pressure radiosonde plus radar reflector

6--14 Reserved

15 Missing value

**0 02 016**

***Radiosonde configuration***

Bit No.

1 Train regulator

2 Light unit

3 Parachute

4 Rooftop release

All 5 Missing value

**0 02 017**

***Correction algorithms for humidity measurements***

Code figure

0 No corrections

1 Time lag correction provided by the manufacturer

2 Solar radiation correction provided by the manufacturer

3 Solar radiation and time lag correction provided by the manufacturer

4--6 Reserved

7 GRUAN solar radiation and time lag correction

8--30 Reserved

31 Missing value

**0 02 019**

***Satellite instruments***

*(See common Code table C--8 in Part C/c.)*

**\
**

**0 02 020**

***Satellite classification***

Code figure

0 Nimbus

1 VTPR

2 Tiros 1 (Tiros, NOAA-6 to NOAA-13)

3 Tiros 2 (NOAA-14 onwards)

10 EOS

20 GPM-core

31 DMSP

61 EUMETSAT Polar System (EPS)

91 ERS

92 Sentinel-3

121 ADEOS

122 GCOM

241 GOES

261 JASON

271 GMS

272 MTSAT

273 Himawari

281 COMS

301 INSAT

331 METEOSAT Operational Programme (MOP)

332 METEOSAT Transitional Programme (MTP)

333 METEOSAT Second Generation Programme (MSG)

351 GOMS

380 FY-1

381 FY-2

382 FY-3

383 FY-4

384--400 Reserved

401 GPS

402 GLONASS

403 GALILEO

404 BDS (BeiDou navigation satellite system)

405--510 Reserved

511 Missing value

**\
**

**0 02 021**

***Satellite instrument data used in processing***

Bit No.

1 High-resolution infrared sounder (HIRS)

2 Microwave sounding unit (MSU)

3 Stratospheric sounding unit (SSU)

4 AMI (advanced microwave instrument) wind mode

5 AMI (advanced microwave instrument) wave mode

6 AMI (advanced microwave instrument) image mode

7 Radar altimeter

8 ATSR (along-track scanning radiometer)

All 9 Missing value

**0 02 022**

***Satellite data-processing technique used***

**Bit flags denoting the elements included in processing sounding data.**

Bit No.

1 Processing technique not defined

2 Automated statistical regression

3 Clear path

4 Partly cloudy path

5 Cloudy path

6--7 Reserved

All 8 Missing value

**Notes:**

\(1) Clear path means the sounding has been generated from clear radiances derived from actual clear spot measurements. Tropospheric and stratospheric HIRS data, as well as MSU and SSU data, have been used.

\(2) Partly cloudy path means the sounding has been generated from clear radiances which have been calculated from partly cloudy spots. Tropospheric and stratospheric HIRS data, as well as MSU and SSU data, have been used.

\(3) Cloudy path means the sounding has been generated only from stratospheric HIRS data, MSU data and SSU data. Tropospheric HIRS data have not been used because of cloudy conditions.

**\
**

**0 02 023**

***Satellite-derived wind computation method***

Code figure

0 Reserved

1 Wind derived from cloud motion observed in the infrared channel

2 Wind derived from cloud motion observed in the visible channel

3 Wind derived from cloud motion observed in the water vapour channel

4 Wind derived from motion observed in a combination of spectral channels

5 Wind derived from motion observed in the water vapour channel in clear air

6 Wind derived from motion observed in the ozone channel

7 Wind derived from motion observed in water vapour channel (cloud or clear air not specified)

8--12 Reserved

13 Root-mean-square

14 Reserved

15 Missing value

**0 02 024**

***Integrated mean humidity computational method***

Code figure

0 Reserved

1 Table with full range of humidity variation in layer

2 Regression technique on 2 humidity values in layer

3--14 Reserved

15 Missing value

**0 02 025**

***Satellite channel(s) used in computation***

Bit flags denoting the instrument and/or channels used in obtaining various physical parameters. If, in any\
grouping of parameters, all bits = 0, then no retrieval was made for that parameter or set of parameters.

Bit No. Instrument (channels)

1 Reserved

*Group 1* -- Layer precipitable water for the layers: surface to 700 hPa, 700 to 500 hPa, and\
500 to 300 hPa

2 HIRS

3 MSU

4--5 Reserved

*Group 2* -- Tropopause temperature and pressure

6 HIRS

7 MSU

8--9 Reserved

*Group 3* -- Total ozone

10 HIRS (1, 2, 3, 8, 9, 16, 17)

*(continued)*

*\
* *(Flag table 0 02 025 -- continued)*

Bit No. Instrument (channels)

11 HIRS (1, 2, 3, 9, 17)

12 MSU

13--14 Reserved

*Group 4* -- Mean temperature for the layers: surface to 850 hPa, 850 to 700 hPa, 700 to\
500 hPa, 500 to 400 hPa, 400 to 300 hPa, 300 to 200 hPa, and 200 to 100 hPa

15 HIRS

16 HIRS\*

17 MSU

18 SKINTK (ocean only)

19--20 Reserved

*Group 5* -- Channel combinations used to obtain mean temperatures for the layers 100\
to 70 hPa, 70 to 50 hPa, 50 to 30 hPa, 30 to 10 hPa, 10 to 5 hPa, 5 to 2 hPa,\
2 to 1 hPa, 1 to 0.4 hPa

21 HIRS\*

22 SSU

23 MSU (3, 4)

24 Reserved

All 25 Missing value

Note: HIRS\* is equivalent to: HIRS channels 1 (669 cm^--1^)

2 (679 cm^--1^)

3 (690 cm^--1^)

4 (2358 cm^--1^)

**0 02 030**

***Method of current measurement***

Code figure

0 Reserved

1\* ADCP (Acoustic Doppler Current Profiler)

2 GEK (Geomagnetic ElectroKinetograph)

3 Ship's set and drift determined by fixes 3--6 hours apart

4 Ship's set and drift determined by fixes more than 6 hours but less than 12 hours apart

5 Drift of buoy

6 ADCP (Acoustic Doppler Current Profiler)

7 Missing value

\* Value deprecated. Code figure 6 should be used instead.

**\
**

**0 02 031**

***Duration and time of current measurement***

Code figure

0 Reserved

1 Instantaneous

2 Averaged over 3 min or less

3 Averaged over more than 3 min, but 6 min at the most

4 Averaged over more than 6 min, but 12 min at the most

5 Instantaneous

6 Averaged over 3 min or less

7 Averaged over more than 3 min, but 6 min at the most

8 Averaged over more than 6 min, but 12 min at the most

9 Vector or Doppler current profiling method not used

10 Reserved

11 1 hour or less

12 More than 1 hour but 2 hours at the most

13 More than 2 hours but 4 hours at the most

14 More than 4 hours but 8 hours at the most

15 More than 8 hours but 12 hours at the most

16 More than 12 hours but 18 hours at the most

17 More than 18 hours but 24 hours at the most

18 Reserved

19 Drift method not used

20--30 Reserved

31 Missing value

Notes:

\(1) Code figures 1--9: Duration and time of current measurement (vector or Doppler current profiling method).

\(2) Code figures 11--19: Period of current measurement (drift method).

\(3) H = Time of observation.

**0 02 032**

***Indicator for digitization***

Code figure

0 Values at selected depths (data points fixed by the instrument or selected by any other method)

1 Values at selected depths (data points taken from traces at significant depths)

2 Reserved

3 Missing value

**\
**

**0 02 033**

***Method of salinity/depth measurement***

Code figure

0 No salinity measured

1 In situ sensor, accuracy better than 0.02 ‰

2 In situ sensor, accuracy less than 0.02 ‰

3 Sample analysis

4--6 Reserved

7 Missing value

**0 02 034**

***Drogue type***

Code figure

0 Unspecified drogue

1 Holey sock

2 TRISTAR

3 Window shade

4 Parachute

5 Non-Lagrangian sea anchor

6--30 Reserved (to be developed)

31 Missing value

**0 02 036**

***Buoy type***

Code figure

0 Drifting buoy

1 Fixed buoy

2 Subsurface float (moving)

3 Missing value

**0 02 037**

***Method of tidal observation***

Code figure

0 Reserved

1 Manual reading from vertical tide staff

2 Manual reading from single automatic recorder at station

3 Manual reading from multiple automatic recorders at station

4 Automatic reading from single automatic recorder at station without level reference check

5 Automatic reading from single automatic recorder at station with level reference check, or from multiple automatic recorders

6 Reserved

7 Missing value

**0 02 038**

***Method of water temperature and/or salinity measurement***

Code figure

0 Ship intake

1 Bucket

2 Hull contact sensor

3 Reversing thermometer

4 STD/CTD sensor

5 Mechanical BT

6 Expendable BT

7 Digital BT

8 Thermistor chain

9 Infrared scanner

10 Microwave scanner

11 Infrared radiometer

12 In-line thermosalinograph

13 Towed body

14 Other

15 Missing value

**0 02 039**

***Method of wet-bulb temperature measurement***

Code figure

0 Measured wet-bulb temperature

1 Iced bulb measured wet-bulb temperature

2 Computed wet-bulb temperature

3 Iced bulb computed wet-bulb temperature

4--6 Reserved

7 Missing value

**0 02 040**

***Method of removing velocity and motion of platform from current***

Code figure

0 Ship's motion removed by averaging

1 Ship's motion removed by motion compensation Ship's velocity removed

2 Ship's motion not removed by bottom tracking

3 Ship's motion removed by averaging

4 Ship's motion removed by motion compensation Ship's velocity removed

5 Ship's motion not removed by navigation

6 Doppler current profiling method not used

7--14 Reserved

15 Missing value

**0 02 041**

***Method for estimating reports related to synoptic features***

Code figure

0 Information based on manual analysis

1 Information based on computer analysis

2 Information based on data assimilation

3 Information based on computer analysis or data assimilation manually modified

4--9 Reserved

10 Information based on the numerical weather prediction

11--62 Reserved for future use

63 Missing value

**0 02 042**

***Indicator for sea-surface current speed***

Code figure

0 Value originally reported in m/s

1 Value originally reported in knots

2 No sea-current data available

3 Missing value

**0 02 044**

***Indicator for method of calculating spectral wave data***

Code figure

0 Reserved for future use

1 Longuet-Higgins (1964)

2 Longuet-Higgins (F3 method)

3 Maximum likelihood method

4 Maximum entropy method

5--14 Reserved

15 Missing value

**0 02 045**

***Indicator for type of platform***

Code figure

0 Sea station

1 Automatic data buoy

2 Aircraft

3 Satellite

4--14 Reserved

15 Missing value

**0 02 046**

***Wave measurement instrumentation***

Code figure

0 Reserved for future use

1 Heave sensor

2 Slope sensor

3--14 Reserved

15 Missing value

**0 02 047**

***Deep-ocean tsunameter type***

Code figure

0 Reserved

1 DART II (PMEL)

2 DART ETD

3 SAIC Tsunami Buoy (STB)

4 GFZ -- Potsdam

5 INCOIS (India)

6 InaBuoy (Indonesia)

7 Envirtech

8--99 Reserved

100--126 Not used

127 Missing value

**0 02 048**

***Satellite sensor indicator***

Code figure

0 HIRS

1 MSU

2 SSU

3 AMSU-A

4 AMSU-B

5 AVHRR

6 SSMI

7 NSCAT

8 SEAWINDS

9 POSEIDON altimeter

10 JMR (JASON Microwave Radiometer)

11 MHS

12 ASCAT

13--14 Reserved

15 Missing value

**0 02 049**

***Geostationary satellite data-processing technique used***

Bit No.

1 Processing technique not defined

2 Simultaneous physical retrieval

3 Clear sounding

4 Cloudy sounding

5--7 Reserved for future use

All 8 Missing value

Notes:

\(1) Clear sounding indicates the sounding has been generated from a set of clear radiances using all available sounder radiances.

\(2) Cloudy sounding indicates that sufficient clear radiances could not be identified in the sounding area. The sounding is calculated from the cloud top (cloud pressure greater than or equal to 780 hPa) upwards.

**0 02 050**

***Geostationary sounder satellite channels used***

Bit No. Channel Central wavelength (micrometers)

1 1 14.71

2 2 14.37

3 3 14.06

4 4 13.64

5 5 13.37

6 6 12.66

7 7 12.02

8 8 11.03

9 9 9.71

10 10 7.43

11 11 7.02

12 12 6.51

13 13 4.57

14 14 4.52

15 15 4.45

16 16 4.13

17 17 3.98

18 18 3.74

19 19 0.969

All 20 Missing value

Note: Beginning with the first bit position (high order bit), if the bit position is set to one, then the channel is used. If the bit position is set to zero, then the channel is not used.

**\
**

**0 02 051**

***Indicator to specify observing method for extreme temperatures***

Code figure

0 Reserved

1 Maximum/minimum thermometers

2 Automated instruments

3 Thermograph

4--14 Reserved

15 Missing value

**0 02 052**

***Geostationary imager satellite channels used***

Bit No. Channel Central wavelength (micrometers)

1 1 0.55 -- 0.75

2 2 3.9

3 3 6.7

4 4 10.7

5 5 12.0

All 6 Missing value

Note: Beginning with the first bit position (high order bit), if the bit position is set to one, then the channel is used. If the bit position is set to zero, then the channel is not used.

**0 02 053**

***GOES-I/M brightness temperature characteristics***

Code figure

0 Observed brightness temperature

1 Brightness temperature with bias correction applied

2 Brightness temperature calculated from first guess

3 Brightness temperature calculated from sounding

4--14 Reserved

15 Missing value

**0 02 054**

***GOES-I/M soundings parameter characteristics***

Code figure

0 Parameter derived using observed sounder brightness temperatures

1 Parameter derived using observed imager brightness temperatures

2 Parameter derived using first guess information

3 Parameter derived using NMC analysis information

4 Parameter derived using radiosonde information

5--14 Reserved

15 Missing value

**0 02 055**

***Geostationary soundings statistical parameters***

Code figure

0 Statistics generated comparing retrieval versus radiosonde

1 Statistics generated comparing retrieval versus first guess

2 Statistics generated comparing radiosonde versus first guess

3 Statistics generated comparing observed versus retrieval

4 Statistics generated comparing observed versus first guess

5 Statistics generated comparing radiosonde versus imager

6 Statistics generated comparing radiosonde versus sounder

7 Statistics generated for radiosonde

8 Statistics generated for first guess

9--14 Reserved

15 Missing value

**0 02 056**

***Geostationary soundings accuracy statistics***

Code figure

0 Sums of differences

1 Sums of squared differences

2 Sample size

3 Minimum difference

4 Maximum difference

5--14 Reserved

15 Missing value

**0 02 057**

***Origin of first-guess information for GOES-I/M soundings***

Code figure

0 Nested Grid Model (NGM)

1 Aviation Model (AVN)

2 Medium Range Forecast (MRF) Model

3 Global Data Assimilation System (GDAS) Forecast Model

4 Prior soundings (within 3 hours of current time)

5 Climatology

6--14 Reserved

15 Missing value

**0 02 058**

***Valid times of first-guess information for GOES-I/M soundings***

Code figure

0 12 hour and 18 hour

1 18 hour and 24 hour

2 6 hour and 12 hour

3 Greater than 24 hours

4--14 Reserved

15 Missing value

**0 02 059**

***Origin of analysis information for GOES-I/M soundings***

Code figure

0 NCEP Nested Grid Model (NGM) Analysis

1 NCEP Aviation Model (AVN) Analysis

2 NCEP Medium Range Forecast (MRF) Model Analysis

3 NCEP Global Data Assimilation System (GDAS) Forecast Model Analysis

4--14 Reserved

15 Missing value

**0 02 060**

***Origin of surface information for GOES-I/M soundings***

Code figure

0 Current surface hourly reports

1 Current ship reports

2 Current buoy reports

3 One hour old surface hourly reports

4 One hour old ship reports

5 One hour old buoy reports

6--14 Reserved

15 Missing value

**0 02 061**

***Aircraft navigational system***

Code figure

0 Inertial navigation system

1 OMEGA

2--6 Reserved

7 Missing value

**0 02 062**

***Type of aircraft data relay system***

Code figure

0 ASDAR

1 ASDAR (ACARS also available but not operative)

2 ASDAR (ACARS also available and operative)

3 ACARS

4 ACARS (ASDAR also available but not operative)

5 ACARS (ASDAR also available and operative)

6--14 Reserved

15 Missing value

**0 02 064**

***Aircraft roll angle quality***

Code figure Meaning

0 Good

1 Bad

2 Reserved

3 Missing value

Note: Bad is currently defined as a roll angle \> 5 degrees from vertical.

**0 02 066**

***Radiosonde ground receiving system***

Code figure

0 InterMet IMS 2000

1 InterMet IMS 1500C

2 Shanghai GTC1

3 Nanjing GTC2

4 Nanjing GFE(L)1

5 MARL-A radar

6 VEKTOR-M radar

7--61 Reserved

62 Other

63 Missing value

**0 02 070**

***Original specification of latitude/longitude***

Code figure

0 Actual location in seconds

1 Actual location in minutes

2 Actual location in degrees

3 Actual location in decidegrees

4 Actual location in centidegrees

5 Referenced to checkpoint in seconds

6 Referenced to checkpoint in minutes

7 Referenced to checkpoint in degrees

8 Referenced to checkpoint in decidegrees

9 Referenced to checkpoint in centidegrees

10 Actual location in tenths of a minute

11 Referenced to checkpoint in tenths of a minute

12--14 Reserved

15 Missing value

**0 02 080**

***Balloon manufacturer***

Code figure

0 Kaysam

1 Totex

2 KKS

3 Guangzhou Shuangyi (China)

4 ChemChina Zhuzhou (China)

5--61 Reserved

62 Other

63 Missing value

**0 02 081**

***Type of balloon***

Code figure

0 GP26

1 GP28

2 GP30

3 HM26

4 HM28

5 HM30

6 SV16

7 Totex TA type balloons

8 Totex TX type balloons

9--29 Reserved

30 Other

31 Missing value

**0 02 083**

***Type of balloon shelter***

Code figure

0 High bay

1 Low bay

2 Balloon-inflated launch system (BILS)

3 Roof-top BILS

4 Automated unmanned sounding system

5--13 Reserved

14 Other

15 Missing value

**0 02 084**

***Type of gas used in balloon***

Code figure

0 Hydrogen

1 Helium

2 Natural gas

3--13 Reserved

14 Other

15 Missing value

**0 02 095**

***Type of pressure sensor***

Code figure

0 Capacitance aneroid

1 Derived from GPS

2 Resistive strain gauge

3 Silicon capacitor

4 Derived from radar height

5--29 Reserved

30 Other

31 Missing value

**0 02 096**

***Type of temperature sensor***

Code figure

0 Rod thermistor

1 Bead thermistor

2 Capacitance bead

3 Capacitance wire

4 Resistive sensor

5 Chip thermistor

6 Mercury

7 Alcohol/glycol

8--30 Reserved for future use

31 Missing value

**0 02 097**

***Type of humidity sensor***

Code figure

0 VIZ Mark II carbon hygristor

1 VIZ B2 hygristor

2 Vaisala A-Humicap

3 Vaisala H-Humicap

4 Capacitance sensor

5 Vaisala RS90

6 Sippican Mark IIA carbon hygristor

7 Twin alternatively heated Humicap capacitance sensor

8 Humicap capacitance sensor with active de-icing method

9 Carbon hygristor

10 Psychrometer

11 Capacitive (polymer)

12 Capacitive (ceramic, including metal oxide)

13 Resistive (generic)

*(continued)*

*\
* *(Code table 0 02 097 -- continued)*

Code figure

14 Resistive (salt polymer)

15 Resistive (conductive polymer)

16 Thermal conductivity

17 Gravimetric

18 Paper-metal coil

19 Ordinary human hair

20 Rolled hair (torsion)

21 Goldbeater\'s skin

22 Chilled mirror hygrometer

23 Dew cell

24 Optical absorption sensor

25--30 Reserved for future use

31 Missing value

**0 02 099**

***Polarization***

Code figure

0 HH polarization

1 VV polarization

2 HV polarization real valued component

3 HV polarization imaginary valued component

4--6 Reserved

7 Missing value

**0 02 101**

***Type of antenna***

Code figure

0 Centre front-fed paraboloid

1 Offset front-fed paraboloid

2 Centre Cassegrain paraboloid

3 Offset Cassegrain paraboloid

4 Planar array

5 Coaxial-collinear array

6 Yagi elements array

7 Microstrip

8--13 Reserved

14 Other

15 Missing value

**\
**

**0 02 103**

***Radome***

Bit No.

1 Radar antenna is protected by a radome

All 2 Missing value

**0 02 104**

***Antenna polarization***

Code figure

0 Horizontal polarization

1 Vertical polarization

2 Right circular polarization

3 Left circular polarization

4 Horizontal and vertical polarization

5 Right and left circular polarization

6 Quasi-horizontal polarization

7 Quasi-vertical polarization

8--14 Reserved

15 Missing value

**0 02 115**

***Type of surface observing equipment***

Code figure

0 PDB

1 RSOIS

2 ASOS

3 Psychrometer

4 F420

5--29 Reserved

30 Other

31 Missing value

**0 02 119**

***RA-2 instrument operations***

Code figure

0 Intermediate frequency calibration mode (IF CAL)

1 Built-in test equipment digital (BITE DGT)

2 Built-in test equipment radio frequency (BITE RF)

3 Preset tracking (PSET TRK)

4 Preset LOOP OUT

5 ACQUISITION

6 TRACKING

7 Missing value

**0 02 131**

***Sensitivity time control (STC)***

Bit No.

1 STC operational

All 2 Missing values

**0 02 137**

***Radar dual PRF ratio***

Code figure

1 3:2

2 4:3

3 5:4

4--14 Reserved

15 Missing value

**0 02 138**

***Antenna rotation direction***

Code figure

1 Clockwise rotation

2 Counterclockwise rotation

3 Missing value

**0 02 139**

***SIRAL instrument configuration***

Code figure

0 SIRAL nominal

1 SIRAL redundant

2 Missing value

**0 02 143**

***Ozone instrument type***

Code figure

0 Reserved

1 Brewer spectrophotometer

2 Caver Teichert

3 Dobson

4 Dobson (Japan)

5 Ehmet

6 Fecker telescope

7 Hoelper

8 Jodmeter

*(continued)*

*\
* *(Code table 0 02 143 -- continued)*

Code figure

9 Filter Ozonometer M-83

10 Mast

11 Oxford

12 Paetzold

13 Regener

14 Reserved for future use

15 Vassy filter ozonometer

16 Carbon iodide

17 Surface ozone bubbler

18 Filter ozonometer M-124

19 ECC sonde

20--126 Reserved

127 Missing value

**0 02 144**

***Light source type for Brewer spectrophotometer***

Code figure

0 Direct sun

1 Direct sun, attenuator \#1

2 Direct sun, attenuator \#2

3 Focused moon

4 Focused sun

5 Focused sun corrected with adjacent sky measurements

6 Zenith sky

7--14 Reserved

15 Missing value

Note: Entries 1 and 2 should not be used.

**0 02 145**

***Wavelength setting for Dobson instruments***

Code figure

0 Wavelengths AD ordinary setting

1 Wavelengths BD ordinary setting

2 Wavelengths CD ordinary setting

3 Wavelengths CC\' ordinary setting

4 Wavelengths AD focused image

5 Wavelengths BD focused image

6 Wavelengths CD focused image

7 Wavelengths CC\' focused image

8--14 Reserved

15 Missing value

**\
**

**0 02 146**

***Source conditions for Dobson instruments***

Code figure

0 On direct sun

1 On direct moon

2 On blue zenith sky

3 On zenith cloud (uniform stratified layer of small opacity)

4 On zenith cloud (uniform or moderately variable layer of medium opacity)

5 On zenith cloud (uniform or moderately variable layer of large opacity)

6 On zenith cloud (highly variable opacity, with or without precipitation)

7 On zenith cloud (fog)

8 On zenith haze

9 On direct sun through thin cloud, fog or haze

10--14 Reserved

15 Missing value

**0 02 147**

***Method of transmission to collection centre***

Code figure

0 Reserved

1 Direct leased circuit

2 Dialled up connection

3 Internet ISP

4 DCP via satellite (MTSAT, METEOSAT, etc.)

5 VSAT

6 GAN,\* BGAN\*\*

7 Thiss terminal

8 Iridium satellites

9 Mobile telephony

10--62 Reserved

63 Missing value

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\* Global Area Network.

\*\* Broadband Global Area Network

**0 02 148**

***Data collection and/or location system***

Code figure

0 Reserved

1 Argos

2 GPS

3 GOES DCP

4 METEOSAT DCP

5 ORBCOMM

*(continued)*

*(Code table 0 02 148-- continued)*

Code figure

6 INMARSAT

7 Iridium

8 Iridium and GPS

9 Argos-3

10 Argos-4

11--30 Reserved

31 Missing value

**0 02 149**

***Type of data buoy***

Code figure

0 Unspecified drifting buoy

1 Standard Lagrangian drifter (Global Drifter Programme)

2 Standard FGGE type drifting buoy\
(non-Lagrangian meteorological drifting buoy)

3 Wind measuring FGGE type drifting buoy\
(non-Lagrangian meteorological drifting buoy)

4 Ice drifter

5 SVPG Standard Lagrangian drifter with GPS

6 SVP-HR drifter with high-resolution temperature or thermistor string

7 Reserved

8 Unspecified subsurface float

9 SOFAR

10 ALACE

11 MARVOR

12 RAFOS

13 PROVOR

14 SOLO

15 APEX

16 Unspecified moored buoy

17 Nomad

18 3-metre discus

19 10-12-metre discus

20 ODAS 30 series

21 ATLAS (e.g. TAO area)

22 TRITON buoy

23 FLEX mooring (e.g. TIP area)

24 Omnidirectional waverider

25 Directional waverider

26 Subsurface ARGO float

27 PALACE

28 NEMO

29 NINJA

*(continued)*

*(Code table 0 02 149-- continued)*

Code figure

30 Ice buoy/float (POPS or ITP)

31--33 Reserved

34 Mooring oceanographic

35 Mooring meteorological

36 Mooring multidisciplinary (OceanSITES)

37 Mooring tide gauge or tsunami buoy

38 Ice beacon

39 Ice mass balance buoy

40--62 Reserved

63 Missing value

**0 02 150**

***TOVS/ATOVS/AVHRR instrumentation channel number***

Code figure

0 Reserved

1 HIRS 1

2 HIRS 2

3 HIRS 3

4 HIRS 4

5 HIRS 5

6 HIRS 6

7 HIRS 7

8 HIRS 8

9 HIRS 9

10 HIRS 10

11 HIRS 11

12 HIRS 12

13 HIRS 13

14 HIRS 14

15 HIRS 15

16 HIRS 16

17 HIRS 17

18 HIRS 18

19 HIRS 19

20 HIRS 20

21 MSU 1

22 MSU 2

23 MSU 3

24 MSU 4

25 SSU 1

26 SSU 2

27 SSU 3

*(continued)*

*(Code table 0 02 150 -- continued)*

Code figure

28 AMSU-A 1

29 AMSU-A 2

30 AMSU-A 3

31 AMSU-A 4

32 AMSU-A 5

33 AMSU-A 6

34 AMSU-A 7

35 AMSU-A 8

36 AMSU-A 9

37 AMSU-A 10

38 AMSU-A 11

39 AMSU-A 12

40 AMSU-A 13

41 AMSU-A 14

42 AMSU-A 15

43 AMSU-B 1 / MHS 1

44 AMSU-B 2 / MHS 2

45 AMSU-B 3 / MHS 3

46 AMSU-B 4 / MHS 4

47 AMSU-B 5 / MHS 5

48 AVHRR 1

49 AVHRR 2

50 AVHRR 3a

51 AVHRR 3b

52 AVHRR 4

53 AVHRR 5

54--62 Reserved

63 Missing value

**0 02 151**

***Radiometer identifier***

Code figure

0 HIRS

1 MSU

2 SSU

3 AMSU-A1-1

4 AMSU-A1-2

5 AMSU-A2

6 AMSU-B

7 AVHRR

8 Reserved

9 MHS

10--2046 Reserved

2047 Missing value**\
**

**0 02 152**

***Satellite instrument used in data processing***

Bit No.

1 High-resolution infrared sounder (HIRS)

2 Microwave sounding unit (MSU)

3 Stratospheric sounding unit (SSU)

4 AMI wind mode

5 AMI wave mode

6 AMI image mode

7 RADAR altimeter

8 ATSR

9 Geostationary imager

10 Geostationary sounder

11 Geostationary Earth radiation (GERB)

12 Multi-channel scanning radiometer

13 Polar-orbiting imager

14--30 Reserved

All 31 Missing value

**0 02 158**

***RA-2 instrument***

Bit No.

1 Mismatch in RED VEC HPA

2 Mismatch in RED VEC RFSS

3 PTR calibration band 320 MHz (Ku)

4 PTR calibration band 80 MHz (Ku)

5 PTR calibration band 20 MHz (Ku)

6 PTR calibration band 160 MHz (S)

7 Ku flight calibration parameters available

8 S flight calibration parameters available

All 9 Missing value

Note: PTR = Pulse target response

HPA = High power amplifier

RFSS = Radio frequency subsystem

RED = Redundancy

**0 02 159**

***MWR instrument***

Bit No.

1 Temperature inconsistency

2 Data is missing

3 Redundancy channel

4 Power bus protection

5 Overvoltage/Overload protection

6 Reserved

7 Reserved

All 8 Missing value

Note: MWR = Microwave radiometer

**0 02 160**

***Wave length of the radar***

Code figure

0 Reserved

1 10 to less than 20 mm

2 Reserved

3 20 to less than 40 mm

4 Reserved

5 40 to less than 60 mm

6 Reserved

7 60 to less than 90 mm

8 90 to less than 110 mm

9 110 mm and greater

10--14 Not used

15 Missing value

**0 02 161**

***Wind processing method***

Bit No.

1--10 Reserved

11 Wind height calculated from median cloud-top pressure of target

12 Target is cloudy

13 Low-level inversion

14 Cross correlation contribution (CCC) method

15 Nested tracking

All 16 Missing value

**0 02 162**

***Extended height assignment method***

Code figure

0 Auto editor

1 IRW\* height assignment

2 WV\*\* height assignment

3 H~2~O intercept height assignment

4 CO~2~ slicing height assignment

5 Low pixel max gradient

6 Higher pixel max gradient

7 Primary height assignment

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\* Infrared window

\*\* Water vapour

*(continued)*

*(Code table 0 02 162 -- continued)*

Code figure

8 Layer thickness assignment

9 Cumulative contribution function -- 10 per cent height

10 Cumulative contribution function -- 50 per cent height

11 Cumulative contribution function -- 90 per cent height

12 Cumulative contribution function -- height of maximum gradient

13 IR/two WV channel rationing method

14 Composite height assignment

15 Optimal estimation

16 Inversion correction

17 Geometric height assignment

18--62 Reserved

63 Missing value

**0 02 163**

***Height assignment method***

Code figure

0 Auto editor

1 IRW height assignment

2 WV height assignment

3 H~2~O intercept height assignment

4 CO~2~ slicing height assignment

5 Low pixel max gradient

6 Higher pixel max gradient

7 Primary height assignment

8 Layer thickness assignment

9 Cumulative contribution function -- 10 per cent height

10 Cumulative contribution function -- 50 per cent height

11 Cumulative contribution function -- 90 per cent height

12 Cumulative contribution function -- height of maximum gradient

13 IR / two WV channel ratioing method

14 Composite height assignment

15 Missing value

**0 02 164**

***Tracer correlation method***

Code figure

0 LP -- Norms least square minimum

1 EN -- Euclidean norm with radiance correlation

2 CC -- Cross correlation

3 Stereo matching

4--6 Reserved

7 Missing value

**\
**

**0 02 165**

***Radiance type flags***

Bit No.

1 Clear path

2 Partly cloudy path

3 Cloudy path

4 Apodized

5 Unapodized

6 Reconstructed

7 Cloud cleared

8--14 Reserved

All 15 Missing value

**0 02 166**

***Radiance type***

Code figure

0 Type not defined

1 Automated statistical regression

2 Clear path

3 Partly cloudy path

4 Cloudy path

5--14 Reserved

15 Missing value

**0 02 167**

***Radiance computational method***

Code figure

0 Method not defined

1 1b raw radiance

2 Processed radiance

3--14 Reserved

15 Missing value

**0 02 169**

***Anemometer type***

Code figure

0 Cup rotor

1 Propeller rotor

2 Wind Observation Through Ambient Noise (WOTAN)

3 Sonic

4--14 Reserved

15 Missing value

**0 02 170**

***Aircraft humidity sensors***

Code figure Sensor type

0 SpectraSensors WVSS-II, Version 1

1 SpectraSensors WVSS-II, Version 2

2 SpectraSensors WVSS-II, Version 3

3--61 Reserved

62 Other

63 Missing value

**0 02 172**

***Product type for retrieved atmospheric gases***

Code figure

0 Reserved

1 Retrieval from a nadir sounding

2 Retrieval from a limb sounding

3--254 Reserved

255 Missing value

**0 02 175**

***Method of precipitation measurement***

Code figure

0 Manual measurement

1 Tipping bucket method

2 Weighing method

3 Optical method

4 Pressure method

5 Float method

6 Drop counter method

7--13 Reserved

14 Others

15 Missing value

**0 02 176**

***Method of state of ground measurement***

Code figure

0 Manual observation

1 Video camera method

2 Infrared method

3 Laser method

4--13 Reserved

14 Others

15 Missing value

**0 02 177**

***Method of snow depth measurement***

Code figure

0 Manual observation

1 Ultrasonic method

2 Video camera method

3 Laser method

4--13 Reserved

14 Others

15 Missing value

**0 02 178**

***Method of liquid content measurement of precipitation***

Code figure

0 Manual observation

1 Optical method

2 Capacitive method

3--13 Reserved

14 Others

15 Missing value

**0 02 179**

***Type of sky condition algorithm***

Code figure

0 Manual observation

1 VAISALA algorithm

2 ASOS (FAA) algorithm

3 AWOS (Canada) algorithm

4--13 Reserved

14 Others

15 Missing value

**0 02 180**

***Main present weather detecting system***

Code figure

0 Manual observation

1 Optical scatter system combined with precipitation occurrence sensing system

2 Forward and/or backscatter system of visible light

3 Forward and/or backscatter system of infrared light

4 Infrared light emitting diode (IRED) system

5 Doppler radar system

6--13 Reserved

14 Others

15 Missing value

**0 02 181**

***Supplementary present weather sensor***

Bit No.

1 Rain detector

2 Freezing rain sensor

3 Ice detection sensor

4 Hail and ice pellet sensor

5--19 Reserved

20 Others

All 21 Missing value

**0 02 182**

***Visibility measurement system***

Code figure

0 Manual measurement

1 Transmissometer system (base \> 25 m)

2 Transmissometer system (base \< 25 m)

3 Forward scatter system

4 Backscatter system

5--13 Reserved

14 Others

15 Missing value

**0 02 183**

***Cloud detection system***

Code figure

0 Manual observation

1 Ceilometer system

2 Infrared camera system

3 Microwave visual camera system

4 Sky imager system

5 Video time-lapsed camera system

6 Micropulse lidar (MPL) system

7--13 Reserved

14 Others

15 Missing value

**0 02 184**

***Type of lightning detection sensor***

Code figure

0 Manual observation

1 Lightning imaging sensor

2 Electrical storm identification sensor

3 Magnetic finder sensor

4 Lightning strike sensor

5 Flash counter

6 ATDnet VLF waveform correlated sensor

7--13 Reserved

14 Others

15 Missing value

**0 02 185**

***Method of evaporation measurement***

Code figure

0 Manual measurement

1 Balanced floating method

2 Pressure method

3 Ultrasonic method

4 Hydraulic method

5--13 Reserved

14 Others

15 Missing value

**0 02 186**

***Capability to detect precipitation phenomena***

Bit No.

1 Precipitation-unknown type

2 Liquid precipitation not freezing

3 Liquid freezing precipitation

4 Drizzle

5 Rain

6 Solid precipitation

7 Snow

8 Snow grains

9 Snow pellets

10 Ice pellets

11 Ice crystals

12 Diamond dust

13 Small hail

14 Hail

*(continued)*

*\
(Flag table 0 02 186 -- continued)*

Bit No.

15 Glaze

16 Rime

17 Soft rime

18 Hard rime

19 Clear ice

20 Wet snow

21 Hoar frost

22 Dew

23 White dew

24 Convective precipitation

25--29 Reserved

All 30 Missing value

**0 02 187**

***Capability to detect other weather phenomena***

Bit No.

1 Dust/sand whirl

2 Squalls

3 Sand storm

4 Dust storm

5 Lightning -- cloud to surface

6 Lightning -- cloud to cloud

7 Lightning -- distant

8 Thunderstorm

9 Funnel cloud not touching surface

10 Funnel cloud touching surface

11 Spray

12--17 Reserved

All 18 Missing value

**0 02 188**

***Capability to detect obscuration***

Bit No.

1 Fog

2 Ice fog

3 Steam fog

4--6 Reserved

7 Mist

8 Haze

9 Smoke

10 Volcanic ash

11 Dust

12 Sand

13 Snow

14--20 Reserved

All 21 Missing value

**0 02 189**

***Capability to discriminate lightning strikes***

Bit No.

1 Manual observation

2 All lightning strikes without discrimination

3 Lightning strikes cloud to ground only

4 All lightning strikes with discrimination between cloud to ground and cloud to cloud

5--11 Reserved

All 12 Missing value

**0 02 191**

***Geopotential height calculation***

Code figure

0 Geopotential height calculated from pressure

1 Geopotential height calculated from GPS height

2 Geopotential height calculated from radar height

3--14 Reserved

15 Missing value

**0 03 001**

***Surface station type***

Code figure

0 Land station (synoptic network)

1 Shallow water station (fixed to sea/lake floor)

2 Ship

3 Rig/platform

4 Moored buoy

5 Drifting buoy (or drifter)

6 Ice buoy

7 Land station (local network)

8 Land vehicle

9 Autonomous marine vehicle

10--30 Reserved for future use

31 Missing value

**0 03 003**

***Thermometer/hygrometer housing***

Code figure

0 Screen

1 Sling/whirling

2 Unscreened

3 Radiation shield

4 Aspirated (e.g. Assmann)

5 Other shelter

6 Handheld

7--14 Reserved for future use

15 Missing value

**0 03 004**

***Type of screen/shelter/radiation shield***

Code figure

0 Stevenson screen

1 Marine Stevenson screen

2 Cylindrical section plate shield

3 Concentric tube

4 Rectangular section shield

5 Square section shield

6 Triangular section shield

7 Open covered lean-to

8 Open covered inverted V roof

9 Integrated (e.g. chilled mirror)

10--14 Reserved for future use

15 Missing value

**0 03 008**

***Artificially ventilated screen or shield***

Code figure

0 Natural ventilation in use

1 Artificial aspiration in use: constant flow at time of reading

2 Artificial aspiration in use: variable flow at time of reading

3--6 Reserved

7 Missing value

**0 03 010**

***Method of sea/water current measurement***

Code figure

0 Reserved

1\* ADCP\*\*

2 GEK (Geomagnetic ElectroKinetograph)

3 Ship\'s set and drift determined by fixes 3--6 hours apart

4 Ship\'s set and drift determined by fixes more than 6 hours but less than 12 hours apart

5 Drift of buoy

6 ADCP

7 ADCP bottom tracking mode

8 Electromagnetic sensor

9 Rotor and vane

10 Lowered ADCP

11--14 Reserved

15 Missing value

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\* Value deprecated. Code figure 6 should be used instead.

\*\* Acoustic Doppler Current Profiler

**0 03 011**

***Method of depth calculation***

Code figure

0 Depth calculated using fall rate equation

1 Depth calculated from water pressure/equation of state

2 Reserved

3 Missing value

**0 03 012**

***Instrument type/sensor for dissolved oxygen measurement***

Code figure

0 Aanderaa oxygen optode

1 Winkler bottle

2--14 Reserved

15 Missing value

**0 03 016**

***Position of road sensors***

Code figure

0 Fast lane between the wheel tracks

1 Fast lane between the wheel tracks in the opposite direction

2 Fast lane in the wheel tracks

3 Fast lane in the wheel tracks in the opposite direction

4 Slow lane between the wheel tracks

5 Slow lane between the wheel tracks in the opposite direction

6 Slow lane in the wheel tracks

7 Slow lane in the wheel tracks in the opposite direction

8--14 Reserved

15 Missing value

**0 03 017**

***Extended type of station***

Bit No.

1 Automatic

2 Manned

3 Event triggered

4 Longer time period than the standard

5 Reserved

All 6 Missing value

**0 03 018**

***Type of road***

Code figure

0 Free track without further information

1 Free track, embankment

2 Free track, flat relative to surroundings

3 Free track, water basin(s) in vicinity

4 Free track, forest

5 Free track, cleft

6 Free track, on hilltop

7 Free track, on hilltop, forest

8 Free track, in valley

9 Free track, in valley, forest

10 Free track, north inclination

11 Free track, north inclination, forest

12 Free track, south inclination

13 Free track, south inclination, forest

14--19 Reserved

20 Bridge without further information

21 Bridge across a valley in an urban area

*(continued)*

*\
(Code table 0 03 018 -- continued)*

Code figure

22 Bridge across a valley with forest/meadows/fields

23 Bridge across street/track

24 Bridge across big river/canal

25 Bridge across river/canal of medium size

26 Bridge across a small stream/loading canal

27--30 Reserved

31 Missing value

**0 03 019**

***Type of construction***

Code figure

0 Asphalt

1 Concrete

2 Concrete construction

3 Steel-girder construction

4 Box girder bridge

5 Orthotropic slab

6 Drain asphalt

7--14 Reserved

15 Missing value

**0 03 020**

***Material for thermometer/hygrometer housing***

Code figure

0 Wood

1 Metal alloy

2 Plastic/GRP\*

3 Reed/grass/leaf

4--6 Reserved for future use

7 Missing value

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\* GRP = Glass-reinforced plastic

**0 03 021**

***Hygrometer heating***

Code figure

0 Unheated

1 Heated

2 Not applicable

3 Missing value

**\
**

**0 03 022**

***Instrument owner***

Code figure

1.  National hydrometeorological/weather service

1 Other

2 Standards institute

3--6 Reserved for future use

7 Missing value

**0 03 023**

***Configuration of louvers for thermometer/hygrometer screen***

Code figure

0 Single v-section louvers

1 Overlapping louvers

2 Double v-section louvers

3 Non-overlapping louvers

4 Vented, non-louvered

5 Not applicable

6 Reserved for future use

7 Missing value

**0 03 027**

***Type of flight rig***

Code figure

0 Solo (single radiosonde)

1 Block

2 Bar

3 Cross

4 T-rig

5 Double T-rig

6 Complex

7--14 Reserved

15 Missing value

**\
**

**0 03 028**

***Method of snow water equivalent measurement***

Code figure

0 Multi-point manual snow survey

1 Single-point manual snow water equivalent measurement

2 Snow pillow or snow scale

3 Passive gamma

4 GNSS/GPS methods

5 Cosmic ray attenuation

6 Time domain reflectometry

7--62 Reserved

63 Missing value

**0 04 059**

***Times of observation used to compute the reported mean values***

Bit No.

1 0000 UTC

2 0600 UTC

3 1200 UTC

4 1800 UTC

5 Other hours

All 6 Missing value

**0 04 080**

***Averaging period for following value***

Code figure

0 Spot values

1 Less than 15 minutes

2 From 15 to 45 minutes

3 More than 45 minutes

4--8 Reserved

9 Data not available

10--14 Not used

15 Missing value

**0 05 069**

***Receiver channel***

Code figure

0 Mie

1 Rayleigh

2 Reserved

3 Missing value

**0 08 001**

***Vertical sounding significance***

Bit No.

1 Surface

2 Standard level

3 Tropopause level

4 Maximum wind level

5 Significant level, temperature and/or relative humidity

6 Significant level, wind

All 7 Missing value

**0 08 002**

***Vertical significance (surface observations)***

Code figure

0 Observing rules for base of lowest cloud and cloud types of FM 12 SYNOP and FM 13\
SHIP apply

1 First non-Cumulonimbus significant layer

2 Second non-Cumulonimbus significant layer

3 Third non-Cumulonimbus significant layer

4 Cumulonimbus layer

5 Ceiling

6 Clouds not detected below the following height(s)

7 Low cloud

8 Middle cloud

9 High cloud

10 Cloud layer with base below and top above the station

11 Cloud layer with base and top below the station level

12--19 Reserved

20 No clouds detected by the cloud detection system

21 First instrument detected cloud layer

22 Second instrument detected cloud layer

23 Third instrument detected cloud layer

24 Fourth instrument detected cloud layer

25--61 Reserved

62 Value not applicable

63 Missing value

**0 08 003**

***Vertical significance (satellite observations)***

Code figure

0 Surface

1 Base of satellite sounding

2 Cloud top

3 Tropopause

4 Precipitable water

5 Sounding radiances

6 Mean temperatures

7 Ozone

8 Low cloud

9 Med cloud

10 High cloud

11--62 Reserved

63 Missing value

**0 08 004**

***Phase of aircraft flight***

Code figure

0--1 Reserved

2 Unsteady (UNS)

3 Level flight, routine observation (LVR)

4 Level flight, highest wind encountered (LVW)

5 Ascending (ASC)

6 Descending (DES)

7 Missing value

**0 08 005**

***Meteorological attribute significance***

Code figure

0 Reserved

1 Storm centre

2 Outer limit or edge of storm

3 Location of maximum wind

4 Location of the storm in the perturbed analysis

5 Location of the storm in the analysis

6--14 Reserved

15 Missing value

**0 08 006**

***Ozone vertical sounding significance***

Bit No.

1 Surface

2 Standard level

3 Tropopause level

4 Prominent maximum level

5 Prominent minimum level

6 Minimum pressure level

7 Reserved

8 Level of undetermined significance

All 9 Missing value

**0 08 007**

***Dimensional significance***

Code figure

0 Point

1 Line

2 Area

3 Volume

4--14 Reserved

15 Missing value

Note: A consecutive sequence of 2 or more of location coordinates, such as latitude and longitude pairs, defines a line or polygon. Points shall be joined in the order given in the message. Any area described will fall left of the drawn boundary in the direction established by the order of the points given in the message. This definition is for simple non-intersecting polygons without holes.

**0 08 008**

***Radiation vertical sounding significance***

Bit No.

1 Surface

2 Standard level

3 Tropopause level

4 Level of beta radiation maximum

5 Level of gamma radiation maximum

6 Minimum pressure level

7 Reserved

8 Level of undetermined significance

All 9 Missing value

**0 08 009**

***Detailed phase of flight***

Code figure

0 Level flight, routine observation, unsteady

1 Level flight, highest wind encountered, unsteady

2 Unsteady (UNS)

3 Level flight, routine observation (LVR)

4 Level flight, highest wind encountered (LVW)

5 Ascending (ASC)

6 Descending (DES)

7 Ascending, observation intervals selected by time increments

8 Ascending, observation intervals selected by time increments, unsteady

9 Ascending, observation intervals selected by pressure increments

10 Ascending, observation intervals selected by pressure increments, unsteady

11 Descending, observation intervals selected by time increments

12 Descending, observation intervals selected by time increments, unsteady

13 Descending, observation intervals selected by pressure increments

14 Descending, observation intervals selected by pressure increments, unsteady

15 Missing value

**0 08 010**

***Surface qualifier (for temperature data)***

Code figure

0 Reserved

1 Bare soil

2 Bare rock

3 Land grass cover

4 Water (lake, sea)

5 Flood water underneath

6 Snow

7 Ice

8 Runway or road

9 Ship or platform deck in steel

10 Ship or platform deck in wood

11 Ship or platform deck partly covered with rubber mat

12 Building roof

13--30 Reserved

31 Missing value

**0 08 011**

***Meteorological feature***

Code figure

0 Quasi-stationary front at the surface

1 Quasi-stationary front above the surface

2 Warm front at the surface

3 Warm front above the surface

4 Cold front at the surface

5 Cold front above the surface

6 Occlusion

7 Instability line

8 Intertropical front

9 Convergence line

10 Jet stream

11 Cloud clear

12 Cloud

13 Turbulence

14 Storm

15 Airframe icing

16 Phenomenon

17 Volcano

18 Atmospherics

19 Reserved

20 Special clouds

21 Thunderstorm

22 Tropical cyclone

23 Mountain wave

24 Duststorm

25 Sandstorm

26--62 Reserved

63 Missing value

**0 08 012**

***Land/sea qualifier***

Code figure

0 Land

1 Sea

2 Coast

3 Missing value

**0 08 013**

***Day/night qualifier***

Code figure

0 Night

1 Day

2 Twilight

3 Missing value

**0 08 014**

***Qualifier for runway visual range***

Code figure

0 10-minute mean value -- normal value

1 10-minute mean value -- above the upper limit for assessments of RVR (P)

2 10-minute mean value -- below the lower limit for assessments of RVR (M)

3 one-minute minimum value -- normal value

4 one-minute minimum value -- above the upper limit for assessments of RVR (P)

5 one-minute minimum value -- below the lower limit for assessments of RVR (M)

6 one-minute maximum value -- normal value

7 one-minute maximum value -- above the upper limit for assessments of RVR (P)

8 one-minute maximum value -- below the lower limit for assessments of RVR (M)

9--14 Reserved

15 Missing value

**0 08 015**

***Significant qualifier for sensor***

Code figure

0 Single sensor

1 Primary sensor

2 Secondary sensor (Backup)

3--6 Reserved

7 Missing value

**0 08 016**

***Change qualifier of a trend-type forecast or an aerodrome forecast***

Code figure

0 NOSIG

1 BECMG

2 TEMPO

3 FM

4--6 Reserved

7 Missing value

**0 08 017**

***Qualifier of the time when the forecast change is expected***

Code figure

0 FM

1 TL

2 AT

3 Missing value

**0 08 018**

***SEAWINDS land/ice surface type***

Bit No.

1 Land is present

2 Surface ice map indicates ice is present

3--10 Reserved

11 Ice map data not available

12 Attenuation map data not available

13--16 Reserved

All 17 Missing value

**0 08 019**

***Qualifier for following centre identifier***

Code figure

0 Reserved

1 ATS (Air Traffic Service) unit serving FIR (Flight Information Region)

2 FIR (Flight Information Region)

3 UIR (Upper Flight Information Region)

4 CTA (Control Area)

5 VAAC (Volcanic Ash Advisory Centre)

6 MWO (Meteorological Watch Office) issuing SIGMET

7--14 Reserved

15 Missing value

**0 08 021**

***Time significance***

Code figure

0 Reserved

1 Time series

2 Time averaged (see Note 1)

3 Accumulated

4 Forecast

5 Forecast time series

6 Forecast time averaged

7 Forecast accumulated

8 Ensemble mean (see Note 2)

9 Ensemble mean time series

10 Ensemble mean time averaged

11 Ensemble mean accumulated

12 Ensemble mean forecast

13 Ensemble mean forecast time series

14 Ensemble mean forecast time averaged

15 Ensemble mean forecast accumulated

16 Analysis

17 Start of phenomenon

18 Radiosonde launch time

19 Start of orbit

20 End of orbit

21 Time of ascending node

22 Time of occurrence of wind shift

23 Monitoring period

24 Agreed time limit for report reception

25 Nominal reporting time

26 Time of last known position

27 First guess

28 Start of scan

29 End of scan or time of ending

30 Time of occurrence

31 Missing value

Notes:

\(1) "Time averaged" indicates that values are continuously averaged over a period of time.

\(2) "Ensemble mean" indicates that a number of distinct values corresponding to a set of time locations are averaged.

\(3) Time significance must be qualified by appropriate time periods being specified.

**0 08 023**

***First-order statistics\****

Code figure

0--1 Reserved

2 Maximum value

3 Minimum value

4 Mean value

5 Median value

6 Modal value

7 Mean absolute error

8 Reserved

9 Best estimate of standard deviation (N--1)

10 Standard deviation (N)

11 Harmonic mean

12 Root-mean-square vector error

13 Root-mean-square

14--31 Reserved

32 Vector mean

33--62 Reserved for local use

63 Missing value

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\* All first-order statistics are in the units defined by the original data descriptors.

**0 08 024**

***Difference statistics\****

Code figure

0--1 Reserved

2 Observed minus maximum

3 Observed minus minimum

4 Observed minus mean

5 Observed minus median

6 Observed minus mode

7--10 Reserved

11 Observed minus climatology (anomaly)

12 Observed minus analysed value

13 Observed minus initialized analysed value

14 Observed minus forecast value \*\*

15--20 Reserved

21 Observed minus interpolated value

22 Observed minus hydrostatically calculated value

23--31 Reserved

32--62 Reserved for local use

63 Missing value

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\* Difference statistics are difference values; they have dimensions the same as the corresponding reported values with respect to units, but assume a range centred on zero (e.g., the difference between reported and analysed values, the difference between reported and forecast values).

\*\* Where observed minus forecast values are represented, the period of the forecast shall be indicated by an appropriate descriptor from Class 04.

**0 08 025**

***Time difference qualifier***

Code figure

0 Universal Time Coordinated (UTC) minus Local Standard Time (LST)

1 Local Standard Time

2 Universal Time Coordinated (UTC) minus Satellite clock

3--4 Reserved

5 Time difference from edge of processing segment

6--14 Reserved

15 Missing value

**0 08 026**

***Matrix significance***

Code figure

0 Averaging kernel matrix

1 Correlation matrix (C)

2 Lower triangular correlation matrix square root (L from C=LL^T^)

3 Inverse of lower triangular correlation matrix square root (L^--1^)

4--42 Reserved

43--62 Reserved for local use

63 Missing or undefined significance

**0 08 029**

***Surface type***

Code figure

0 Open ocean or semi-enclosed sea

1 Enclosed sea or lake

2 Continental ice

3 Land

4 Low inland (below sea level)

5 Mix of land and water

6 Mix of land and low inland

7--10 Reserved

11 River

12 Lake

13 Sea

14 Glacier

15 Urban land

16 Rural land

17 Suburban land

18 Sea ice

19--254 Reserved

255 Missing value

**0 08 032**

***Status of operation***

Code figure

0 Routine operation

1 Event triggered by storm surge

2 Event triggered by tsunami

3 Event triggered manually

4 Installation testing

5 Maintenance testing

6--14 Reserved

15 Missing value

**0 08 033**

***Method of derivation of percentage confidence***

Code figure

0 Reserved

1 Percentage confidence calculated using cloud fraction

2 Percentage confidence calculated using standard deviation of temperature

3 Percentage confidence calculated using probability of cloud contamination

4 Percentage confidence calculated using normality of distribution

5--126 Reserved

127 Missing value

**0 08 034**

***Temperature/salinity measurement qualifier***

Code figure

0 Secondary sampling: averaged

1 Secondary sampling: discrete

2 Secondary sampling: mixed

3 Near-surface sampling: averaged, pumped

4 Near-surface sampling: averaged, unpumped

5 Near-surface sampling: discrete, pumped

6 Near-surface sampling: discrete, unpumped

7 Near-surface sampling: mixed, pumped

8 Near-surface sampling: mixed, unpumped

9--14 Reserved

15 Missing value

**0 08 035**

***Type of monitoring exercise***

Code figure

0 Global

1 Regional

2 National

3 Special

4 Bilateral

5 Reserved

6 Reserved

7 Missing value

**\
**

**0 08 036**

***Type of centre or station performing monitoring***

Code figure

0 WMO Secretariat

1 WMO

2 RSMC

3 NMC

4 RTH

5 Observing site

6 Other

7 Missing value

**0 08 037**

***Baseline check significance***

Code figure

0 Manufacturer's baseline check unit

1 Weather screen

2 GRUAN standard humidity chamber

3--30 Reserved

31 Missing value

**0 08 038**

***Instrument data significance***

Code figure

0 Verified instrument reading

1 Reference instrument reading

2--254 Reserved

255 Missing value

**0 08 039**

***Time significance (Aviation forecast)***

Code figure

0 Issue time of forecast

1 Time of commencement of period of the forecast

2 Time of ending of period of the forecast

3 Forecast time of maximum temperature

4 Forecast time of minimum temperature

5 Time of beginning of the forecast change

6 Time of ending of the forecast change

7--62 Reserved

63 Missing value

**0 08 040**

***Flight level significance***

Code figure

0 High-resolution data sample

1 Within 20 hPa of surface

2 Pressure less than 10 hPa (i.e., 9, 8, 7, etc.) when no other reason applies

3 Base pressure level for stability index

4 Begin doubtful temperature, height data

5 Begin missing data (all elements)

6 Begin missing relative humidity data

7 Begin missing temperature data

8 Highest level reached before balloon descent because of icing or turbulence

9 End doubtful temperature, height data

10 End missing data (all elements)

11 End missing relative humidity data

12 End missing temperature data

13 Zero degrees Celsius crossing(s) for RADAT

14 Standard pressure level

15 Operator-added level

16 Operator-deleted level

17 Balloon re-ascended beyond previous highest ascent level

18 Significant relative humidity level

19 Relative humidity level selection terminated

20 Surface level

21 Significant temperature level

22 Mandatory temperature level

23 Flight termination level

24 Tropopause(s)

25 Aircraft report

26 Interpolated (generated) level

27 Mandatory wind level

28 Significant wind level

29 Maximum wind level

30 Incremental wind level (fixed regional)

31 Incremental height level (generated)

32 Wind termination level

33 Pressure 100 to 110 hPa, when no other reason applies

34 Freezing level base

35 Freezing level top

36 Flight level base

37 Flight level top

38 Top of wind sounding

39 Bottom of wind sounding

40 Significant thermodynamic level (inversion)

41 Significant relative humidity level (according to NCDC criteria)

42 Significant temperature level (according to NCDC)

43 Begin missing wind data

44 End missing wind data

45--59 Reserved

60 Level of 80-knot isotach above jet

*(continued)*

*\
(Code table 0 08 040 -- continued)*

Code figure

61 Level of 80-knot isotach below jet

62 Other

63 Missing value

**0 08 041**

***Data significance***

Code figure

0 Parent site

1 Observation site

2 Balloon manufacture date

3 Balloon launch point

4 Surface observation

5 Surface observation displacement from launch point

6 Flight level observation

7 Flight level termination point

8 IFR ceiling and visibility

9 Mountain obscuration

10 Strong surface wind

11 Freezing level

12 Multiple freezing level

13 Instrument manufacture date

14--30 Reserved

31 Missing value

**0 08 042**

***Extended vertical sounding significance***

Bit No.

1 Surface

2 Standard level

3 Tropopause level

4 Maximum wind level

5 Significant temperature level

6 Significant humidity level

7 Significant wind level

8 Beginning of missing temperature data

9 End of missing temperature data

10 Beginning of missing humidity data

11 End of missing humidity data

12 Beginning of missing wind data

13 End of missing wind data

14 Top of wind sounding

*(continued)*

*\
(Flag table 0 08 042 -- continued)*

Bit No.

15 Level determined by regional decision

16 Freezing level

17 Pressure level originally indicated by height as the vertical coordinate

All 18 Missing value

Note:

> \(1) Freezing level is the level at which temperature first decreases to 0 °C. The criteria for the selection of freezing level in upper-air observations are:
>
> \(a) If the surface temperature is not lower than 0 °C when the radiosonde is released, then the lowest level at which the temperature first decreases to 0 °C will be selected as the freezing level.
>
> \(b) If the surface temperature is equal to 0 °C, then the surface level will be the freezing level.
>
> \(c) If during observation there is no level at which the temperature equals 0 °C, then the closest two levels between which the temperature crosses from a positive to a negative value should be used to interpolate the freezing-level temperature equal to 0 °C.
>
> \(d) The following elements will be calculated for the freezing level: time, elevation, pressure, humidity, dewpoint temperature, dewpoint depression, and deviation of longitude and latitude.

**0 08 043**

***Atmospheric chemical or physical constituent type***

Note: The last column in the table contains the associated registry number from the Chemical Abstracts Service (CAS) of the American Chemical Society.

Code figure Name Formula CAS number (if applicable)

0 Ozone O~3~ 10028-15-6

1 Water vapour H~2~O 7732-18-5

2 Methane CH~4~ 74-82-8

3 Carbon dioxide CO~2~ 124-38-9

4 Carbon monoxide CO 630-08-0

5 Nitrogen dioxide NO~2~ 10102-44-0

6 Nitrous oxide N~2~O 10024-97-2

7 Formaldehyde HCHO 50-00-0

8 Sulphur dioxide SO~2~ 7446-09-5

9--24 Reserved

25 Particulate matter \< 1.0 microns

26 Particulate matter \< 2.5 microns

27 Particulate matter \< 10 microns

28 Aerosols (generic)

29 Smoke (generic)

30 Crustal material (generic dust)

31 Volcanic ash

32--200 Reserved

201--254 Reserved for local use

255 Missing value

**0 08 050**

***Qualifier for number of missing values in calculation of statistic***

Code figure

0 Reserved

1 Pressure

2 Temperature

3 Extreme temperature

4 Vapour pressure

5 Precipitation

6 Sunshine duration

7 Maximum temperature

8 Minimum temperature

9 Wind

10--14 Reserved

15 Missing value

**0 08 051**

***Qualifier for number of missing values in calculation of statistic***

Code figure

1 Pressure

2 Temperature

3 Extreme temperature

4 Vapour pressure

5 Precipitation

6 Sunshine duration

7 Missing value

**0 08 052**

***Condition for which number of days of occurrence follows***

Code figure

0 Mean wind speed over a 10-minute period observed or recorded equal to or more than 10 m s^--1^ or 20 knots

1 Mean wind speed over a 10-minute period observed or recorded equal to or more than 20 m s^--1^ or 40 knots

2 Mean wind speed over a 10-minute period observed or recorded equal to or more than 30 m s^--1^ or 60 knots

3 Maximum temperature less than 273.15 K

4 Maximum temperature equal to or more than 298.15 K

5 Maximum temperature equal to or more than 303.15 K

6 Maximum temperature equal to or more than 308.15 K

7 Maximum temperature equal to or more than 313.15 K

8 Minimum temperature less than 273.15 K

9 Maximum temperature equal to or more than 273.15 K

10 Precipitation equal to or more than 1.0 kg m^--2^

11 Precipitation equal to or more than 5.0 kg m^--2^

12 Precipitation equal to or more than 10.0 kg m^--2^

13 Precipitation equal to or more than 50.0 kg m^--2^

14 Precipitation equal to or more than 100.0 kg m^--2^

15 Precipitation equal to or more than 150.0 kg m^--2^

16 Snow depth more than 0.00 m

17 Snow depth more than 0.01 m

18 Snow depth more than 0.10 m

19 Snow depth more than 0.50 m

20 Horizontal visibility less than 50 m

21 Horizontal visibility less than 100 m

22 Horizontal visibility less than 1000 m

23 Hail

24 Thunderstorm

25--30 Reserved

31 Missing value

**0 08 053**

***Day of occurrence qualifier***

Code figure

0 Value occurred on only one day in the month

1 Value occurred on more than one day in the month

2 Reserved

3 Missing value

**0 08 054**

***Qualifier for wind speed or wind gusts***

Code figure

0 Wind speed or gust is as reported

1 Wind speed is greater than that reported (P in METAR/TAF/SPECI)

2--6 Reserved

7 Missing value

**0 08 060**

***Sample scanning mode significance***

Code figure

0 Reserved

1 Range

2 Azimuth

3 Horizontal

4 Vertical

5 North/south

6 East/west

7--14 Reserved

15 Missing value

**0 08 065**

***Sun-glint indicator***

Code figure

0 No sun-glint

1 Sun-glint

2 Reserved

3 Missing value

**0 08 066**

***Semi-transparency indicator***

Code figure

0 Opaque

1 Semi-transparent

2 Reserved

3 Missing value

**0 08 070**

***Vertical sounding product qualifier***

Code figure

0 Reserved

1 Reserved

2 Earth located instrument counts, calibration coefficients and housekeeping (level 1b)

3 Earth located calibrated radiances (level 1c)

4 Mapped to a common footprint, Earth located calibrated radiances (level 1d)

5--14 Reserved

15 Missing value

**0 08 072**

***Pixel(s) type***

Code figure

0 Mixed

1 Clear

2 Cloudy

3 Probably clear

4 Probably cloudy

5--6 Reserved

7 Missing value

**0 08 074**

***Altimeter echo type***

Code figure

0 Open ocean or semi-enclosed sea

1 Non-ocean like

2 Reserved

3 Missing value

**0 08 075**

***Ascending/descending orbit qualifier***

Code figure

0 Ascending orbit

1 Descending orbit

2 Reserved

3 Missing value

**0 08 076**

***Type of band***

Code figure

0 Ku

1 C

2 Long-wave infrared

3 Medium-wave infrared

4 Short-wave infrared

5 M

6 I

7 Day/night

8--62 Reserved

63 Missing value

**0 08 077**

***Radiometer sensed surface type***

Code figure

0 Land

1 Sea

2 Coastal

3 Open ocean or semi-enclosed sea

4 Enclosed sea or lake

5 Continental ice

6--126 Reserved

127 Missing value

**0 08 079**

***Product status***

Code figure

0 Normal issue

1 Correction to a previously issued product (COR)

2 Amendment to a previously issued product (AMD)

3 Correction to a previously issued amended product (COR AMD)

4 Cancellation of a previously issued product (CNL)

5 No product available (NIL)

6 Special report (SPECI)

7 Corrected special report (SPECI COR)

8--14 Reserved

15 Missing or not applicable

**0 08 080**

***Qualifier for GTSPP\* quality flag***

Code figure

0 Total water pressure profile

1 Total water temperature profile

2 Total water salinity profile

3 Total water conductivity profile

4 Total water depth

5--9 Reserved

10 Water pressure at a level

11 Water temperature at a level

12 Salinity at a level

13 Water depth at a level

14 Sea/water current speed at a level

15 Sea/water current direction at a level

16 Dissolved oxygen at a level

17--19 Reserved

20 Position

21--62 Reserved

63 Missing value

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\* GTSPP = Global Temperature Salinity Profile Programme

**0 08 081**

***Type of equipment***

Code figure

0 Sensor

1 Transmitter

2 Receiver

3 Observing platform

4--62 Reserved

63 Missing value

**0 08 082**

***Modification of sensor height to another value***

Code figure

0 Sensor height is not modified

1 Sensor height is modified to standard level\*

2--6 Reserved

7 Missing value

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\* If 0 08 082 = 1, the standard level is indicated by the Class 07 descriptor, which immediately follows. It is possible to indicate the real height of the sensor by preceding the descriptor by the relevant Class 07 descriptor.

**0 08 083**

***Nominal value indicator***

Bit No.

1 Adjusted to or with respect to representative height of sensor above local ground (or deck of marine platform)

2 Adjusted to or with respect to representative height of sensor above water surface

3 Adjusted with respect to standard surface roughness

4 Adjusted with respect to wind speed

5 Adjusted with respect to temperature

6 Adjusted with respect to pressure

7 Adjusted with respect to humidity

8 Adjusted with respect to evaporation

9 Adjusted with respect to wetting losses

10--14 Reserved

All 15 Missing value

**0 08 085**

***Beam identifier***

Code figure

0 Fore beam

1 Mid beam

2 Aft beam

3--6 Reserved

7 Missing value

**0 08 086**

***Vertical significance for NWP***

Bit No.

1 Model "ground" surface

2 Standard level

3 Tropopause level

4 Maximum wind level

5 Significant temperature level

6 Significant humidity level

7 Significant wind level

8 Vertically interpolated level (This should be set to 1 for points on the vertical profile that fall between the model's native vertical levels.)

9 Virtual station height

10 Level of best fit

11 Reserved

All 12 Missing value

**0 08 087**

***Corner position of observation***

Code figure

0 Upper left

1 Upper right

2 Lower right

3 Lower left

4--6 Reserved

7 Missing value

**0 08 088**

***Map significance***

Code figure

0 Top view (geographical longitude on x-axis and latitude on y-axis)

1 North--south view (transect with geographical longitude on x-axis and vertical height on y-axis)

2 East--west view (transect with geographical latitude on x-axis and vertical height on y-axis)

3--62 Reserved

63 Missing

**0 08 091**

***Coordinates significance***

Code figure

0 Satellite coordinates

1 Observation coordinates

2 Start of observation

3 End of observation

4 Horizontal centre of gravity of the observation

5 Vertical centre of gravity of the observation

6 Top of the observation

7 Bottom of the observation

8 Projection origin

9 Coordinates of true scale

10--254 Reserved

255 Missing value

**0 08 092**

***Measurement uncertainty expression***

Code figure

0 Standard uncertainty

1--30 Reserved

31 Missing value

**0 08 093**

***Measurement uncertainty significance***

Code figure

0 Total uncertainty

1 Systematic component of uncertainty

2 Random component of uncertainty

3--30 Reserved

31 Missing value

**0 10 063**

***Characteristic of pressure tendency***

Code figure

0 Increasing, then decreasing; atmospheric pressure the same or higher than three hours ago

1 Increasing, then steady; or increasing, then increasing\
more slowly

2 Increasing (steadily or unsteadily)

3 Decreasing or steady, then increasing; or increasing,\
then increasing more rapidly

4 Steady; atmospheric pressure the same as three hours ago

5 Decreasing, then increasing; atmospheric pressure the same or lower than three hours ago

6 Decreasing, then steady; or decreasing, then\
decreasing more slowly

7 Decreasing (steadily or unsteadily)

8 Steady or increasing, then decreasing; or decreasing,\
then decreasing more rapidly

9--14 Reserved

15 Missing value

Notes:

\(1) In reports from automatic stations, code figure 2 shall be used when tendency is positive, 7 when negative, and 4 when pressure is the same as three hours before.

\(2) In reports from tropical stations reporting 24-hour pressure changes, code figure 2 shall be used when tendency is positive, 7 when negative, and 4 when pressure is the same as 24 hours before.

**0 10 064**

***SIGMET cruising level***

Code figure

0 Subsonic

1 Transonic

2 Supersonic

3--6 Reserved

7 Missing value

**0 11 030**

***Extended degree of turbulence***

Code figure

0 Nil

1 Light

2 Moderate

3 Severe

4 Nil

5 Light

6 Moderate

7 Severe

8 Nil

9 Light

10 Moderate

11 Severe

12 Extreme, in clear air

13 Extreme, in cloud

14 Extreme, cloud/clear air not specified

15 Light, isolated moderate

16 Light, occasional moderate

17 Light, frequently moderate

18 Moderate, isolated severe

19 Moderate, occasional severe

20 Moderate, frequently severe

21 Severe, isolated extreme

22 Severe, occasional extreme

23 Severe, frequently extreme

24--62 Reserved

63 Missing value

**0 11 031**

***Degree of turbulence***

Code figure

0 Nil

1 Light

2 Moderate

3 Severe

4 Nil

5 Light

6 Moderate

7 Severe

8 Nil

9 Light

10 Moderate

11 Severe

*(continued)*

*\
(Code table 0 11 031 -- continued)*

Code figure

12 Extreme, in clear air

13 Extreme, in cloud

14 Extreme, cloud/clear air not specified

15 Missing value

**0 11 037**

***Turbulence index***

Code figure Average value of eddy Peak value of eddy

dissipation rate (ave) dissipation rate

(m^2/3^ s^--1^) (peak) (m^2/3^ s^--1^)

0 ave \< 0.1 peak \< 0.1

1 ave \< 0.1 0.1 ≤ peak \< 0.2

2 0.1 ≤ ave \< 0.2 0.1 ≤ peak \< 0.2

3 ave \< 0.1 0.2 ≤ peak \< 0.3

4 0.1 ≤ ave \< 0.2 0.2 ≤ peak \< 0.3

5 0.2 ≤ ave \< 0.3 0.2 ≤ peak \< 0.3

6 ave \< 0.1 0.3 ≤ peak \< 0.4

7 0.1 ≤ ave \< 0.2 0.3 ≤ peak \< 0.4

8 0.2 ≤ ave \< 0.3 0.3 ≤ peak \< 0.4

9 0.3 ≤ ave \< 0.4 0.3 ≤ peak \< 0.4

10 ave \< 0.1 0.4 ≤ peak \< 0.5

11 0.1 ≤ ave \< 0.2 0.4 ≤ peak \< 0.5

12 0.2 ≤ ave \< 0.3 0.4 ≤ peak \< 0.5

13 0.3 ≤ ave \< 0.4 0.4 ≤ peak \< 0.5

14 0.4 ≤ ave \< 0.5 0.4 ≤ peak \< 0.5

15 ave \< 0.1 0.5 ≤ peak \< 0.8

16 0.1 ≤ ave \< 0.2 0.5 ≤ peak \< 0.8

17 0.2 ≤ ave \< 0.3 0.5 ≤ peak \< 0.8

18 0.3 ≤ ave \< 0.4 0.5 ≤ peak \< 0.8

19 0.4 ≤ ave \< 0.5 0.5 ≤ peak \< 0.8

20 0.5 ≤ ave \< 0.8 0.5 ≤ peak \< 0.8

21 ave \< 0.1 0.8 ≤ peak

22 0.1 ≤ ave \< 0.2 0.8 ≤ peak

23 0.2 ≤ ave \< 0.3 0.8 ≤ peak

24 0.3 ≤ ave \< 0.4 0.8 ≤ peak

25 0.4 ≤ ave \< 0.5 0.8 ≤ peak

26 0.5 ≤ ave \< 0.8 0.8 ≤ peak

27 0.8 ≤ ave 0.8 ≤ peak

28 Nil Nil

29--62 Reserved Reserved

63 Missing value Missing value

**0 11 038**

***Time of occurrence of peak eddy dissipation rate***

Code figure Minutes prior to\
observation time (min)

0 min \< 1

1 1 ≤ min \< 2

2 2 ≤ min \< 3

3 3 ≤ min \< 4

4 4 ≤ min \< 5

5 5 ≤ min \< 6

6 6 ≤ min \< 7

7 7 ≤ min \< 8

8 8 ≤ min \< 9

9 9 ≤ min \< 10

10 10 ≤ min \< 11

11 11 ≤ min \< 12

12 12 ≤ min \< 13

13 13 ≤ min \< 14

14 14 ≤ min \< 15

15 No timing information available

16--30 Reserved

31 Missing value

**0 11 039**

***Extended time of occurrence of peak eddy dissipation rate***

Code figure Minutes prior to\
observation time (min)

0 min \< 1

1 1 ≤ min \< 2

2 2 ≤ min \< 3

3 3 ≤ min \< 4

4 4 ≤ min \< 5

5 5 ≤ min \< 6

6 6 ≤ min \< 7

7 7 ≤ min \< 8

8 8 ≤ min \< 9

9 9 ≤ min \< 10

10 10 ≤ min \< 11

11 11 ≤ min \< 12

12 12 ≤ min \< 13

13 13 ≤ min \< 14

14 14 ≤ min \< 15

15--59 As above to 59 ≤ min \< 60

60 No timing information available

61--62 Reserved

63 Missing value

**0 13 038**

***Superadiabatic indicator***

Code figure

0 Not superadiabatic

1 Superadiabatic

2 Reserved

3 Missing value

**0 13 039**

***Terrain type (ice/snow)***

Code figure

0 Sea ice

1 Snow on land

2--6 Reserved

7 Missing value

**0 13 040**

***Surface flag***

Code figure

0 Land

1 Reserved

2 Near coast

3 Ice

4 Possible ice

5 Ocean

6 Coast

7 Inland water\*

8 Snow cover

9 Sea ice

10 Standing water

11 Snow

12--14 Reserved

15 Missing value

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\* Inland water includes rivers, lakes, wetlands and swamps.

**\
**

**0 13 041**

***Pasquill-Gifford stability category***

Code figure

1 A

2 A -- B

3 B

4 B -- C

5 C

6 D

7 E

8 F

9 G

10--14 Reserved

15 Missing value

**0 13 051**

***Frequency group, precipitation***

Code figure

0 Smaller than any value in the 30-year period

1 In the first quintile

2 In the second quintile

3 In the third quintile

4 In the fourth quintile

5 In the fifth quintile

6 Greater than any value in the 30-year period

7--14 Reserved

15 Missing value

**0 13 056**

***Character and intensity of precipitation***

Code figure

0 No precipitation

1 Light intermittent

2 Moderate intermittent

3 Heavy intermittent

4 Very heavy intermittent

5 Light continuous

6 Moderate continuous

7 Heavy continuous

8 Very heavy continuous

9 Variable -- alternatively light and heavy

10--14 Reserved

15 Missing value

**\
**

**0 13 057**

***Time of beginning or end of precipitation***

Code figure

0 No precipitation

1 Within the last hour

2 1 to 2 hours ago

3 2 to 3 hours ago

4 3 to 4 hours ago

5 4 to 5 hours ago

6 5 to 6 hours ago

7 6 to 8 hours ago

8 8 to 10 hours ago

9 More than 10 hours ago

10--14 Reserved

15 Missing value

**0 15 025**

***Type of pollutant***

Code figure

0 Ozone

1--10 Reserved

11 Fine particulate matter (diameter \< 2.5 microns)

12 Fine particulate matter (diameter \< 10 microns)

13--14 Reserved

15 Missing value

**0 19 001**

***Type of synoptic feature***

Code figure

0 Depression or low (extratroplcal)

1 Tropical depression

2 Tropical storm

3 Severe tropical storm

4 Typhoon

5--9 Reserved

10 Dust/sandstorm

11--62 Reserved

63 Missing value

Note: New local names for storm of various strengths shall be added as necessary.

**0 19 008**

***Vertical extent of circulation***

Code figure

0 Reserved

1 Shallow (top of circulation below 700-hPa level)

2 Medium (top between 700-hPa and 400-hPa level)

3 Deep (top above 400-hPa level)

4--6 Reserved

7 Missing value

**0 19 010**

***Method for tracking the centre of synoptic feature***

Code figure

1 Minimum value of sea-level pressure

2 Maximum value of 850 hPa relative vorticity

3--14 Reserved

15 Missing value

**0 19 100**

***Time interval to calculate the movement of the tropical cyclone***

Code figure

0--2 Not used

3 During the preceding 15 minutes

4 During the preceding 30 minutes

5 During the preceding 1 hour

6 During the preceding 2 hours

7 During the preceding 3 hours

8 During the preceding 6 hours

9 During a period of more than 6 hours

10 Undetermined

11--14 Not used

15 Missing value

**0 19 101**

***Accuracy of the position of the centre of the tropical cyclone***

Code figure

0 Reserved

1 Eye visible on radar scope, accuracy good (within 10 km)

2 Eye visible on radar scope, accuracy fair (within 30 km)

3 Eye visible on radar scope, accuracy poor (within 50 km)

4 Position of the centre within the area covered by the radar scope, determination\
by means of the spiral-band overlay, accuracy good (within 10 km)

5 Position of the centre within the area covered by the radar scope, determination\
by means of the spiral-band overlay, accuracy fair (within 30 km)

6 Position of the centre within the area covered by the radar scope, determination\
by means of the spiral-band overlay, accuracy poor (within 50 km)

7 Position of the centre outside the area covered by the radar scope, extrapolation\
by means of the spiral-band overlay

8--9 Reserved

10 Accuracy undetermined

11--14 Not used

15 Missing value

**0 19 102**

***Shape and definition of the eye of the tropical cyclone***

Code figure

0 Circular

1 Elliptical -- the minor axis is at least 3/4 the length\
of the major axis

2 Elliptical -- the minor axis is less than 3/4 the length\
of the major axis

3 Apparent double eye

4 Other shape

5 Ill defined

6 Undetermined

7 Missing value

**0 19 103**

***Diameter of major axis of the eye of the tropical cyclone***

Code figure

0 Less than 5 km

1 5 to less than 10 km

2 10 to less than 15 km

3 15 to less than 20 km

4 20 to less than 25 km

5 25 to less than 30 km

6 30 to less than 35 km

7 35 to less than 40 km

8 40 to less than 50 km

9 50 km and greater

10 Undetermined

11--14 Not used

15 Missing value

**0 19 104**

***Change in character of the eye during the 30 minutes***

Code figure

0 Eye has first become visible during the past 30 minutes

1 No significant change in the characteristics or size of the eye

2 Eye has become smaller with no other significant change in characteristics

3 Eye has become larger with no other significant change in characteristics

4 Eye has become less distinct with no significant change in size

5 Eye has become less distinct and decreased in size

6 Eye has become less distinct and increased in size

7 Eye has become more distinct with no significant change in size

8 Eye has become more distinct and decreased in size

9 Eye has become more distinct and increased in size

10 Change in character and size of eye cannot be determined

11--14 Not used

15 Missing value

**0 19 105**

***Distance between the end of spiral band and the centre***

Code figure

0 0 to less than 100 km

1 100 to less than 200 km

2 200 to less than 300 km

3 300 to less than 400 km

4 400 to less than 500 km

5 500 to less than 600 km

6 600 to less than 800 km

7 800 km or more

8--9 Reserved

10 Doubtful or undetermined

11--14 Not used

15 Missing value

**0 19 107**

***Time interval over which the movement of the\
tropical cyclone has been calculated***

Code figure

0 Less than 1 hour

1 1 to less than 2 hours

2 2 to less than 3 hours

3 3 to less than 6 hours

4 6 to less than 9 hours

5 9 to less than 12 hours

6 12 to less than 15 hours

7 15 to less than 18 hours

8 18 to less than 21 hours

9 21 to less than 30 hours

10--14 Not used

15 Missing value

**0 19 108**

***Accuracy of geographical position of the tropical cyclone***

Code figure

0 Cyclone centre within 10 km of the transmitted position

1 Cyclone centre within 20 km of the transmitted position

2 Cyclone centre within 50 km of the transmitted position

3 Cyclone centre within 100 km of the transmitted position

4 Cyclone centre within 200 km of the transmitted position

5 Cyclone centre within 300 km of the transmitted position

6 Cyclone centre undetermined

7 Missing value

**0 19 109**

***Mean diameter of the overcast cloud of the tropical cyclone***

Code figure

0 Less than 1° of latitude

1 1° to less than 2° of latitude

2 2° to less than 3° of latitude

3 3° to less than 4° of latitude

4 4° to less than 5° of latitude

5 5° to less than 6° of latitude

6 6° to less than 7° of latitude

7 7° to less than 8° of latitude

8 8° to less than 9° of latitude

9 9° of latitude or more

10 Undetermined

11--14 Not used

15 Missing value

**0 19 110**

***Apparent 24-hour change in intensity of the tropical cyclone***

Code figure

0 Much weakening

1 Weakening

2 No change

3 Intensification

4 Strong Intensification

5--8 Reserved

9 Not observed previously

10 Undetermined

11--14 Not used

15 Missing value

**0 19 113**

***Cloud pattern type of the DT-number***

Code figure Type

1 Curved Band

2 Shear

3 Eye

4 Banding Eye

5 Central Dense Overcast (CDO)

6 Embedded Centre

7 Centre Cold Cover (CCC)

8--14 Reserved

15 Missing value

**0 19 117**

***Cloud picture type of the PT-number***

Code figure Type

1 A (curved band)

2 B (CDO)

3 C (shear)

4--6 Reserved

7 Missing value

**0 19 119**

***Type of the final T-number***

Code figure Type

1 DT-number

2 PT-number

3 MET-number

4--6 Reserved

7 Missing value

**0 20 003**

***Present weather***

Code figure

00--49 *No precipitation at the station at the time of observation*

00--19 No precipitation, fog, ice fog (except for 11 and 12), duststorm, sandstorm, drifting or blowing\
snow at the station\* at the time of observation or, except for 09 and 17, during the preceding\
hour

00--03 No meteors except photometeors

00 Cloud development not observed or not observable

01 Clouds generally dissolving or becoming less developed

02 State of sky on the whole unchanged

03 Clouds generally forming or developing

04--09 Haze, dust, sand or smoke

04 Visibility reduced by smoke, e.g. veldt or forest fires, industrial smoke or volcanic ashes

05 Haze

06 Widespread dust in suspension in the air, not raised by wind at or near the station at the\
time of observation

07 Dust or sand raised by wind at or near the station at the time of observation, but no well-\
developed dust whirl(s) or sand whirl(s), and no duststorm or sandstorm seen; or, in the\
case of sea stations and coastal stations, blowing spray at the station

08 Well-developed dust whirl(s) or sand whirl(s) seen at or near the station during the\
preceding hour or at the same time of observation, but no duststorm or sandstorm

09 Duststorm or sandstorm within sight at the time of observation, or at the station during\
the preceding hour

10 Mist

11 Patches shallow fog or ice fog at the station, whether on land or sea,

12 More or less continuous not deeper than about 2 metres on land or 10 metres at sea

13 Lightning visible, no thunder heard

14 Precipitation within sight, not reaching the ground or the surface of the sea

15 Precipitation within sight, reaching the ground or the surface of the sea, but distant, i.e.\
estimated to be more than 5 km from the station

16 Precipitation within sight, reaching the ground or the surface of the sea, near to, but not\
at the station

17 Thunderstorm, but no precipitation at the time of observation

18 Squalls at or within sight of the station during the preceding hour or

19 Funnel cloud(s)\*\* at the time of observation

20--29 Precipitation, fog, ice fog or thunderstorm at the station during the preceding hour but\
not at the time of observation

20 Drizzle (not freezing) or snow grains

21 Rain (not freezing)

22 Snow

23 Rain and snow or ice pellets

24 Freezing drizzle or freezing rain

25 Shower(s) of rain

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\* The expression "at the station" refers to a land station or a ship.

\*\* Tornado cloud or waterspout.

*(continued)*

*\
(Code table 0 20 003 -- continued)*

Code figure

26 Shower(s) of snow, or of rain and snow

27 Shower(s) of hail\*, or of rain and hail\*

28 Fog or ice fog

29 Thunderstorm (with or without precipitation)

30--39 Duststorm, sandstorm, drifting or blowing snow

30 -- has decreased during the preceding hour

31 -- no appreciable change during the\
preceding hour

32 -- has begun or has increased during the\
preceding hour

33 -- has decreased during the preceding hour

34 -- no appreciable change during the\
preceding hour

35 -- has begun or has increased during the\
preceding hour

36 Slight or moderate drifting snow

37 Heavy drifting snow

38 Slight or moderate blowing snow

39 Heavy blowing snow

40--49 Fog or ice fog at the time of observation

40 Fog or ice fog at a distance at the time of observation, but not at the station during the\
preceding hour, the fog or ice fog extending to a level above that of the observer

41 Fog or ice fog in patches

42 Fog or ice fog, sky visible

43 Fog or ice fog, sky invisible

44 Fog or ice fog, sky visible

45 Fog or ice fog, sky invisible

46 Fog or ice fog, sky visible

47 Fog or ice fog, sky invisible

48 Fog, depositing rime, sky visible

49 Fog, depositing rime, sky invisible

50--99 *Precipitation at the station at the time of observation*

50--59 Drizzle

50 Drizzle, not freezing, intermittent

51 Drizzle, not freezing, continuous

52 Drizzle, not freezing, intermittent

53 Drizzle, not freezing, continuous

54 Drizzle, not freezing, intermittent

55 Drizzle, not freezing, continuous

56 Drizzle, freezing, slight

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\* Hail, small hail, snow pellets.

*(continued)*

*\
(Code table 0 20 003 -- continued)*

Code figure

57 Drizzle, freezing, moderate or heavy (dense)

58 Drizzle and rain, slight

59 Drizzle and rain, moderate or heavy

60--69 Rain

60 Rain, not freezing, intermittent

61 Rain, not freezing, continuous

62 Rain, not freezing, intermittent

63 Rain, not freezing, continuous

64 Rain, not freezing, intermittent

65 Rain, not freezing, continuous

66 Rain, freezing, slight

67 Rain, freezing, moderate or heavy

68 Rain or drizzle and snow, slight

69 Rain or drizzle and snow, moderate or heavy

70--79 Solid precipitation not in showers

70 Intermittent fall of snowflakes

71 Continuous fall of snowflakes

72 Intermittent fall of snowflakes

73 Continuous fall of snowflakes

74 Intermittent fall of snowflakes

75 Continuous fall of snowflakes

76 Diamond dust (with or without fog)

77 Snow grains (with or without fog)

78 Isolated star-like snow crystals (with or without fog)

79 Ice pellets

80--99 Showery precipitation, or precipitation with current or recent thunderstorm

80 Rain shower(s), slight

81 Rain shower(s), moderate or heavy

82 Rain shower(s), violent

83 Shower(s) of rain and snow mixed, slight

84 Shower(s) of rain and snow mixed, moderate or heavy

85 Snow shower(s), slight

86 Snow shower(s), moderate or heavy

87 Shower(s) of snow pellets or small hail, with or without -- slight\
rain or rain and snow mixed

88 Shower(s) of snow pellets or small hail, with or without -- moderate or heavy\
rain or rain and snow mixed

89 Shower(s) of hail, with or without rain or rain and snow -- slight\
mixed, not associated with thunder

90 Shower(s) of hail, with or without rain or rain and snow -- moderate or heavy\
mixed, not associated with thunder

91 Slight rain at time of observation

92 Moderate or heavy rain at time of observation

93 Slight snow, or rain and snow mixed or hail\* at time of observation

94 Moderate or heavy snow, or rain and snow mixed or hail\* at time\
of observation

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\* Hail, small hail, snow pellets.

*(continued)*

*\
(Code table 0 20 003 -- continued)*

Code figure

95 Thunderstorm, slight or moderate, without hail\*, but with rain\
and/or snow at time of observation

96 Thunderstorm, slight or moderate, with hail\* at time of observation

97 Thunderstorm, heavy, without hail\*, but with rain and/or snow Thunderstorm at\
at time of observation time of observation

98 Thunderstorm combined with duststorm or sandstorm at time of\
observation

99 Thunderstorm, heavy, with hail\* at time of observation

Present weather reported from an automatic weather station

100 No significant weather observed

101 Clouds generally dissolving or becoming less developed during the past hour

102 State of sky on the whole unchanged during the past hour

103 Clouds generally forming or developing during the past hour

104 Haze or smoke, or dust in suspension in the air, visibility equal to, or greater than, 1 km

105 Haze or smoke, or dust in suspension in the air, visibility less than 1 km

106--109 Reserved

110 Mist

111 Diamond dust

112 Distant lightning

113--117 Reserved

118 Squalls

119 Reserved

Code figures 120--126 are used to report precipitation, fog (or ice fog) or thunderstorm\
at the station during the preceding hour but not at the time of observation

120 Fog

121 PRECIPITATION

122 Drizzle (not freezing) or snow grains

123 Rain (not freezing)

124 Snow

125 Freezing drizzle or freezing rain

126 Thunderstorm (with or without precipitation)

127 BLOWING OR DRIFTING SNOW OR SAND

128 Blowing or drifting snow or sand, visibility equal to, or greater than, 1 km

129 Blowing or drifting snow or sand, visibility less than 1 km

130 FOG

131 Fog or ice fog in patches

132 Fog or ice fog, has become thinner during the past hour

133 Fog or ice fog, no appreciable change during the past hour

134 Fog or ice fog, has begun or become thicker during the past hour

135 Fog, depositing rime

136--139 Reserved

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\* Hail, small hail, snow pellets.

*(continued)*

*\
(Code table 0 20 003 -- continued)*

Code figure

140 PRECIPITATION

141 Precipitation, slight or moderate

142 Precipitation, heavy

143 Liquid precipitation, slight or moderate

144 Liquid precipitation, heavy

145 Solid precipitation, slight or moderate

146 Solid precipitation, heavy

147 Freezing precipitation, slight or moderate

148 Freezing precipitation, heavy

149 Reserved

150 DRIZZLE

151 Drizzle, not freezing, slight

152 Drizzle, not freezing, moderate

153 Drizzle, not freezing, heavy

154 Drizzle, freezing, slight

155 Drizzle, freezing, moderate

156 Drizzle, freezing, heavy

157 Drizzle and rain, slight

158 Drizzle and rain, moderate or heavy

159 Reserved

160 RAIN

161 Rain, not freezing, slight

162 Rain, not freezing, moderate

163 Rain, not freezing, heavy

164 Rain, freezing, slight

165 Rain, freezing, moderate

166 Rain, freezing, heavy

167 Rain (or drizzle) and snow, slight

168 Rain (or drizzle) and snow, moderate or heavy

169 Reserved

170 SNOW

171 Snow, slight

172 Snow, moderate

173 Snow, heavy

174 Ice pellets, slight

175 Ice pellets, moderate

176 Ice pellets, heavy

177 Snow grains

178 Ice crystals

179 Reserved

180 SHOWER(S) OR INTERMITTENT PRECIPITATION

181 Rain shower(s) or intermittent rain, slight

182 Rain shower(s) or intermittent rain, moderate

183 Rain shower(s) or intermittent rain, heavy

*(continued)*

*(Code table 0 20 003 -- continued)*

Code figure

184 Rain shower(s) or intermittent rain, violent

185 Snow shower(s) or intermittent snow, slight

186 Snow shower(s) or intermittent snow, moderate

187 Snow shower(s) or intermittent snow, heavy

188 Reserved

189 Hail

190 THUNDERSTORM

191 Thunderstorm, slight or moderate, with no precipitation

192 Thunderstorm, slight or moderate, with rain showers and/or snow showers

193 Thunderstorm, slight or moderate, with hail

194 Thunderstorm, heavy, with no precipitation

195 Thunderstorm, heavy, with rain showers and/or snow showers

196 Thunderstorm, heavy, with hail

197--198 Reserved

199 Tornado

Present weather (in addition to present weather report from either a manned or an\
automatic station)

Deciles 200--209

200--203 Not used

204 Volcanic ash suspended in the air aloft

205 Not used

206 Thick dust haze, visibility less than 1 km

207 Blowing spray at the station

208 Drifting dust (sand)

209 Wall of dust or sand in distance (like haboob)

Deciles 210--219

210 Snow haze

211 Whiteout

212 Not used

213 Lightning, cloud to surface

214--216 Not used

217 Dry thunderstorm

218 Not used

219 Tornado cloud (destructive) at or within sight of the station during preceding hour or\
at the time of observation

Deciles 220--229

220 Deposition of volcanic ash

221 Deposition of dust or sand

222 Deposition of dew

223 Deposition of wet snow

224 Deposition of soft rime

225 Deposition of hard rime

*(continued)*

*\
(Code table 0 20 003 -- continued)*

Code figure

226 Deposition of hoar frost

227 Deposition of glaze

228 Deposition of ice crust (ice slick)

229 Not used

Deciles 230--239

230 Duststorm or sandstorm with temperature below 0 °C

231--238 Not used

239 Blowing snow, impossible to determine whether snow is falling or not

Deciles 240--249

240 Not used

241 Fog on sea

242 Fog in valleys

243 Arctic or Antarctic sea smoke

244 Steam fog (sea, lake or river)

245 Steam log (land)

246 Fog over ice or snow cover

247 Dense fog, visibility 60--90 m

248 Dense fog, visibility 30--60 m

249 Dense fog, visibility less than 30 m

Deciles 250--259

250 less than 0.10 mm h^--1^

251 0.10--0.19 mm h^--1^

252 0.20--0.39 mm h^--1^

253 0.40--0.79 mm h^--1^

254 0.80--1.59 mm h^--1^

255 1.60--3.19 mm h^--1^

256 3.20--6.39 mm h^--1^

257 6.4 mm h^--1^ or more

258 Not used

259 Drizzle and snow

Deciles 260--269

260 less than 1.0 mm h^--1^

261 1.0--1.9 mm h^--1^

262 2.0-- 3.9 mm h^--1^

263 4.0-- 7.9 mm h^--1^

264 8.0--15.9 mm h^--1^

265 16.0--31.9 mm h^--1^

266 32.0--63.9 mm h^--1^

267 64.0 mm h^--1^ or more

268--269 Not used

*(continued)*

*\
(Code table 0 20 003 -- continued)*

Code figure

Deciles 270--279

270 less than 1.0 cm h^--1^

271 1.0--1.9 cm h^--1^

272 2.0--3.9 cm h^--1^

273 4.0--7.9 cm h^--1^

274 8.0--15.9 cm h^--1^

275 16.0--31.9 cm h^--1^

276 32.0--63.9 cm h^--1^

277 64.0 cm h^--1^ or more

278 Snow or ice crystal precipitation from a clear sky

279 Wet snow, freezing on contact

Deciles 280--299

280 Precipitation of rain

281 Precipitation of rain, freezing

282 Precipitation of rain and snow mixed

283 Precipitation of snow

284 Precipitation of snow pellets or small hall

285 Precipitation of snow pellets or small hail, with rain

286 Precipitation of snow pellets or small hail, with rain and snow mixed

287 Precipitation of snow pellets or small hail, with snow

288 Precipitation of hail

289 Precipitation of hail, with rain

290 Precipitation of hall, with rain and snow mixed

291 Precipitation of hail, with snow

292 Shower(s) or thunderstorm over sea

293 Shower(s) or thunderstorm over mountains

294--299 Not used

300--507 Reserved

508 No significant phenomenon to report, present and past weather omitted

509 No observation, data not available, present and past weather omitted

510 Present and past weather missing, but expected

511 Missing value

Notes:

\(1) The middle portion of this code table (code figures 100--199) includes terms on several levels to cover simple and increasingly complex automatic stations.

\(2) Generic terms for weather (e.g. fog, drizzle) are intended for use at automatic stations capable of determining types of weather but no other information. Generic terms are included in the code table using all capital letters.

\(3) Code figures for generic precipitation (code figures 140--148) are arranged in order of increasing complexity. For example, a very simple station that can sense only the presence or absence of precipitation would use code figure 140 (precipitation). At the next level, an automatic station capable of sensing amount but not type would use code figure 141 or 142. An automatic station capable of sensing gross type (liquid, solid, freezing) and amount would use code figures 143--148. An automatic station capable of reporting actual types of precipitation (e.g. drizzle rain), but not the amount, would use the appropriate whole decile number (e.g. 150 for generic drizzle, 160 for generic rain).

**0 20 004/0 20 005**

***Past weather (1) and (2)***

Code figure

0 Cloud covering 1/2 or less of the sky throughout the appropriate period

1 Cloud covering more than 1/2 of the sky during part of the appropriate period and\
covering 1/2 or less during part of the period

2 Cloud covering more than 1/2 of the sky throughout the appropriate period

3 Sandstorm, duststorm or blowing snow

4 Fog or ice fog or thick haze

5 Drizzle

6 Rain

7 Snow, or rain and snow mixed

8 Shower(s)

9 Thunderstorm(s) with or without precipitation

10 No significant weather observed

11 VISIBILITY REDUCED (see Note)

12 Blowing phenomena, visibility reduced

13 FOG (see Note)

14 PRECIPITATION (see Note)

15 Drizzle

16 Rain

17 Snow or ice pellets

18 Showers or intermittent precipitation

19 Thunderstorm

20--30 Reserved

31 Missing value

Note: The weather descriptions in code figures 10 to 19 are progressively complex, to accommodate the different levels of weather discrimination capability of various automatic stations. Stations having only basic sensing capability may use the lower code figures and basic generic descriptions (shown in capital letters). Stations with progressively higher discrimination capability shall use the more detailed descriptions (higher codes).

**0 20 006**

***Flight rules***

Code figure

0 Low instrument flight rules -- Ceiling \< 500 feet and/or visibility \< 1 mile

1 Instrument flight rules -- Ceiling \< 1000 feet and/or visibility \< 3 miles

2 Marginal visual flight rules -- 1000 feet ≤ Ceiling \< 3000 feet and/or 3 miles ≤ visibility\
\< 5 miles

3 Visual flight rules -- Ceiling ≥ 3000 feet and/or visibility ≥ 5 miles

4--6 Reserved

7 Missing value

**0 20 008**

***Cloud distribution for aviation***

Code figure

0 Sky clear

1 Few

2 Scattered

3 Broken

4 Overcast

5 Reserved

6 Scattered/broken (Many forecasts use scattered/broken or broken/overcast

7 Broken/overcast followed by cloud type(s))

8 Isolated (Used on aviation charts to describe the cloud type Cb)

9 Isolated embedded (Used on aviation charts to describe the cloud type Cb)

10 Occasional (Used on aviation charts to describe the cloud type Cb)

11 Occasional embedded (Used on aviation charts to describe the cloud type Cb)

12 Frequent (Used on aviation charts to describe the cloud type Cb)

13 Dense (Used on aviation charts to describe cloud that would cause\
sudden changes in visibility (less than 1 000 m))

14 Layers

15 Obscured (OBSC)

16 Embedded (EMBD)

17 Frequent embedded

18--30 Reserved

31 Missing value

**0 20 009**

***General weather indicator (TAF/METAR)***

Code figure

0 Reserved

1 NSC Nil Significant Cloud

2 CAVOK

3 SKC Sky Clear

4 NSW Nil Significant Weather

5--14 Reserved

15 Missing value

**0 20 011**

***Cloud amount***

Code figure

0 0 0

1 1 okta or less, but not zero 1/10 or less, but not zero

2 2 oktas 2/10 -- 3/10

3 3 oktas 4/10

4 4 oktas 5/10

*(continued)*

*(Code table 0 20 011 -- continued)*

Code figure

5 5 oktas 6/10

6 6 oktas 7/10 -- 8/10

7 7 oktas or more, but not 8 oktas 9/10 or more, but not 10/10

8 8 oktas 10/10

9 Sky obscured by fog and/or other meteorological phenomena

10 Sky partially obscured by fog and/or other meteorological phenomena

11 Scattered

12 Broken

13 Few

14 Reserved

15 Cloud cover is indiscernible for reasons other than fog or other meteorological phenomena, or observation is not made

Notes:

\(1) For use of code figure 15, see Regulation 12.1.4.

\(2) "Clear" and "overcast" are coded by 0 and 8, respectively.

**0 20 012**

***Cloud type***

Code figure

0 Cirrus (Ci)

1 Cirrocumulus (Cc)

2 Cirrostratus (Cs)

3 Altocumulus (Ac)

4 Altostratus (As)

5 Nimbostratus (Ns)

6 Stratocumulus (Sc)

7 Stratus (St)

8 Cumulus (Cu)

9 Cumulonimbus (Cb)

10 No C~H~ clouds

11 Cirrus fibratus, sometimes uncinus, not progressively invading the sky

12 Cirrus spissatus, in patches or entangled sheaves, which usually do not increase and sometimes seem to be the remains of the upper part of a cumulonimbus; or cirrus castellanus or floccus

13 Cirrus spissatus cumulonimbogenitus

14 Cirrus uncinus or fibratus, or both, progressively invading the sky; they generally thicken as a whole

15 Cirrus (often in bands) and cirrostratus, or cirrostratus alone, progressively invading the sky; they generally thicken as a whole, but the continuous veil does not reach 45 degrees above the horizon

16 Cirrus (often in bands) and cirrostratus, or cirrostratus alone, progressively Invading the sky; they generally thicken as a whole; the continuous veil extends more than 45 degrees above the horizon, without the sky being totally covered

17 Cirrostratus covering the whole sky

*(continued)*

*\
(Code table 0 20 012 -- continued)*

Code figure

18 Cirrostratus not progressively invading the sky and not entirely covering it

19 Cirrocumulus alone, or cirrocumulus predominant among the C~H~ clouds

20 No C~M~ clouds

21 Altostratus translucidus

22 Altostratus opacus or nimbostratus

23 Altocumulus translucidus at a single level

24 Patches (often lenticular) of altocumulus translucidus, continually changing and occurring at one or more levels

25 Altocumulus translucidus in bands, or one or more layers of altocumulus translucidus or opacus, progressively invading the sky; these altocumulus clouds generally thicken as a whole

26 Altocumulus cumulogenitus (or cumulonimbogenitus)

27 Altocumulus translucidus or opacus in two or more layers, or altocumulus opacus in a single layer, not progressively invading the sky, or altocumulus with altostratus or nimbostratus

28 Altocumulus castellanus or floccus

29 Altocumulus of a chaotic sky, generally at several levels

30 No C~L~ clouds

31 Cumulus humilis or cumulus fractus other than of bad weather,\* or both

32 Cumulus mediocris or congestus, towering cumulus (TCU), with or without cumulus of species fractus or humilis or stratocumulus, all having their bases at the same level

33 Cumulonimbus calvus, with or without cumulus, stratocumulus or stratus

34 Stratocumulus cumulogenitus

35 Stratocumulus other than stratocumulus cumulogenitus

36 Stratus nebulosus or stratus fractus other than of bad weather,\* or both

37 Stratus fractus or cumulus fractus of bad weather,\* or both (pannus), usually below altostratus or nimbostratus

38 Cumulus and stratocumulus other than stratocumulus cumulogenitus, with bases at\
different levels

39 Cumulonimbus capillatus (often with an anvil), with or without cumulonimbus calvus, cumulus, stratocumulus, stratus or pannus

40 C~H~

41 C~M~

42 C~L~

43 Clear

44 Liquid water

45 Supercooled liquid water

46 Mixed phase

47 Optically thick ice

48 Optically thin ice

49 Multilayered ice

50--58 Reserved

59 Cloud not visible owing to darkness, fog, duststorm, sandstorm, or other analogous phenomena

60 C~H~ clouds invisible owing to darkness, fog, blowing dust or sand, or other similar phenomena, or because of a continuous layer of lower clouds

*(continued)*

*\
(Code table 0 20 012 -- continued)*

Code figure

61 C~M~ clouds invisible owing to darkness, fog, blowing dust or sand, or other similar phenomena, or because of continuous layer of lower clouds

62 C~L~ clouds invisible owing to darkness, fog, blowing dust or sand, or other similar phenomena

63 Missing value

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\* "Bad weather" denotes the conditions which generally exist during precipitation and a short time before and after.

**0 20 017**

***Cloud top description***

Code figure

0 Isolated cloud fragments of clouds

1 Continuous cloud

2 Broken cloud -- small breaks flat tops

3 Broken cloud -- large breaks

4 Continuous cloud

5 Broken cloud -- small breaks undulating tops

6 Broken cloud -- large breaks

7 Continuous or almost continuous waves with towering clouds above the top of the layer

8 Groups of waves with towering clouds above the top of the layer

9 Two or more layers at different levels

10--14 Reserved

15 Missing value

**0 20 018**

***Tendency of runway visual range***

Code figure

0 Increasing (U)

1 Decreasing (D)

2 No distinct change (N)

3 Missing value

**\
**

**0 20 021**

***Type of precipitation***

Bit No.

1 Precipitation -- unknown type

2 Liquid precipitation not freezing

3 Liquid freezing precipitation

4 Drizzle

5 Rain

6 Solid precipitation

7 Snow

8 Snow grains

9 Snow pellets

10 Ice pellets

11 Ice crystals

12 Diamond dust

13 Small hail

14 Hail

15 Glaze

16 Rime

17 Soft rime

18 Hard rime

19 Clear ice

20 Wet snow

21 Hoar frost

22 Dew

23 White dew

24--29 Reserved

All 30 Missing value

Note: Mixed precipitation is indicated by setting to one the bits of all the observed single types of precipitation.

**0 20 022**

***Character of precipitation***

Code figure

0 No precipitation

1 Continuous

2 Intermittent

3 Shower

4 Not reaching ground

5 Deposition

6--14 Reserved

15 Missing value

**0 20 023**

***Other weather phenomena***

Bit No.

1 Dust/sand whirl

2 Squalls

3 Sandstorm

4 Duststorm

5 Lightning -- cloud to surface

6 Lightning -- cloud to cloud

7 Lightning -- distant

8 Thunderstorm

9 Funnel cloud not touching surface

10 Funnel cloud touching surface

11 Spray

12 Waterspout

13 Wind shear

14 Dust devils

15--17 Reserved

All 18 Missing value

**0 20 024**

***Intensity of phenomena***

Code figure

0 No phenomena

1 Light

2 Moderate

3 Heavy

4 Violent

5 Severe

6 Very severe

7 Missing value

**\
**

**0 20 025**

***Obscuration***

Bit No.

1 Fog

2 Ice fog

3 Steam fog

4--6 Reserved

7 Mist

8 Haze

9 Smoke

10 Volcanic ash

11 Dust

12 Sand

13 Snow

14 Cloud

15 Precipitation

16 Impossible to determine whether snow is falling or not

17--20 Reserved

All 21 Missing value

**0 20 026**

***Character of obscuration***

Code figure

0 No change

1 Shallow

2 Patches

3 Partial

4 Freezing

5 Low drifting

6 Blowing

7 Increasing

8 Decreasing

9 In suspension in the air

10 Wall

11 Dense

12 Whiteout

13 Drifting and blowing

14 Reserved

15 Missing value

**0 20 027**

***Phenomena\* occurrence***

Bit No.

1 At time of observation

2 In past hour

3 In time period for past weather W~1~W~2~

4 In time period specified

5 Reserved

6 Below station level

7 At the station (see Note 1)

8 In the vicinity (see Note 2)

All 9 Missing value

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\* Phenomenon in this flag table means any phenomenon, including precipitation and obscuration.

Notes:

\(1) In conjunction with the observation of waterspouts or funnel clouds, i.e., within 3 km of the station.

\(2) In conjunction with the observation of waterspouts or funnel clouds, i.e., more than 3 km from the station.

**\
**

**0 20 028**

***Expected change in intensity***

Code figure

0 No change (NC)

1 Forecast to weaken (WKN)

2 Forecast to intensify (INTSF)

3--6 Reserved

7 Missing value

**0 20 029**

***Rain flag***

Code figure

0 No rain

1 Rain

2 Reserved

3 Missing value

**0 20 032**

***Rate of ice accretion (estimated)***

Code figure

0 Ice not building up

1 Ice building up slowly

2 Ice building up rapidly

3 Ice melting or breaking up slowly

4 Ice melting or breaking up rapidly

5--6 Reserved

7 Missing value

**0 20 033**

***Cause of ice accretion***

Bit No.

1 Icing from ocean spray

2 Icing from fog

3 Icing from rain

All 4 Missing value

**0 20 034**

***Sea-ice concentration***

Code figure

0 No sea ice in sight

1 Ship in open lead more than 1.0 nautical mile wide, or ship in fast ice with boundary\
beyond limit of visibility

2 Sea ice present in concentrations\
less than 3/10 (3/8), open water or\
very open pack ice

3 4/10 to 6/10 (3/8 to less than 6/8),\
open pack ice

4 7/10 to 8/10 (6/8 to less than 7/8),\
close pack ice

5 9/10 or more, but not 10/10 (7/8 to\
less than 8/8), very close pack ice

6 Strips and patches of pack ice\
with open water between

7 Strips and patches of close or\
very close pack ice with areas\
of lesser concentration between

8 Fast ice with open water, very\
open or open pack ice to seaward\
of the ice boundary

9 Fast ice with close or very close\
pack ice to seaward of the\
boundary

10--13 Reserved

14 Unable to report, because of darkness, lack of visibility, or because ship is more than\
0.5 nautical mile away from ice edge

15--30 Reserved

31 Missing value

**0 20 035**

***Amount and type of ice***

Code figure

0 No ice of land origin

1 1--5 icebergs, no growlers or bergy bits

2 6--10 icebergs, no growlers or bergy bits

3 11--20 icebergs, no growlers or bergy bits

4 Up to and including 10 growlers and bergy bits -- no icebergs

5 More than 10 growlers and bergy bits -- no icebergs

6 1--5 icebergs, with growlers and bergy bits

7 6--10 icebergs, with growlers and bergy bits

8 11--20 icebergs, with growlers and bergy bits

9 More than 20 icebergs, with growlers and bergy bits -- a major hazard to navigation

10--13 Reserved

14 Unable to report, because of darkness, lack of visibility or because only sea ice is visible

15 Missing value

**0 20 036**

***Ice situation***

Code figure

0 Ship in open water with floating ice in sight

1 Ship in easily penetrable ice; conditions improving

2 Ship in easily penetrable ice; conditions not changing

3 Ship in easily penetrable ice; conditions worsening

4 Ship in ice difficult to penetrate; conditions improving

5 Ship in ice difficult to penetrate; conditions not changing

6 Ship in ice difficult to penetrate and conditions worsening. Ice forming and floes freezing together

7 Ship in ice difficult to penetrate and conditions worsening. Ice under slight pressure

8 Ship in ice difficult to penetrate and conditions worsening. Ice under moderate or severe pressure

9 Ship in ice difficult to penetrate and conditions worsening. Ship beset

10--29 Reserved

30 Unable to report, because of darkness or lack of visibility

31 Missing value

**0 20 037**

***Ice development***

Code figure

0 New ice only (frazil ice, grease ice, slush, shuga)

1 Nilas or ice rind, less than 10 cm thick

2 Young ice (grey ice, grey-white ice), 10--30 cm thick

3 Predominantly new and/or young ice with some first-year ice

4 Predominantly thin first-year ice with some new and/or young ice

5 All thin first-year ice (30--70 cm thick)

6 Predominantly medium first-year ice (70--120 cm thick) and thick first-year ice (\>120 cm thick) with some thinner (younger) first-year ice

7 All medium and thick first-year ice

8 Predominantly medium and thick first-year ice with some old ice (usually more than 2 metres thick)

9 Predominantly old ice

10--29 Reserved

30 Unable to report, because of darkness, lack of visibility or because only ice of land origin is visible or because ship is more than 0.5 nautical mile away from ice edge

31 Missing value

**0 20 040**

***Evolution of drift snow***

Code figure

0 Drift snow ended before the hour of observation

1 Intensity diminishing

2 No change

3 Intensity increasing

4 Continues, apart from interruption lasting less than 30 minutes

5 General drift snow has become drift snow near the ground

6 Drift snow near the ground has become general drift snow

7 Drift snow has started again after an interruption of more than 30 minutes

8--14 Reserved

15 Missing value

**0 20 041**

***Airframe icing***

Code figure

0 No icing

1 Light icing

2 Light icing in cloud

3 Light icing in precipitation

4 Moderate icing

5 Moderate icing in cloud

6 Moderate icing in precipitation

7 Severe icing

8 Severe icing in cloud

9 Severe icing in precipitation

10 Trace of icing

11 Trace of icing in cloud

12 Trace of icing in precipitation

13--14 Reserved

15 Missing value

**0 20 042**

***Airframe icing present***

Code figure

0 No icing

1 Icing present

2 Reserved

3 Missing value

**0 20 045**

***Supercooled large droplet (SLD) conditions***

Code figure

0 No SLD conditions present

1 SLD conditions present

2 Reserved

3 Missing value

**0 20 048**

***Evolution of feature***

Code figure

0 Stability

1 Diminution

2 Intensification

3 Unknown

4--14 Reserved

15 Missing value

**0 20 050**

***Cloud index***

Code figure

0 Reserved

1 1st low cloud

2 2nd low cloud

3 3rd low cloud

4 1st medium cloud

5 2nd medium cloud

6 3rd medium cloud

7 1st high cloud

8 2nd high cloud

9--254 Reserved

255 Missing value

**0 20 055**

***State of sky in the tropics***

Code figure

0 Cumulus, if any, are quite small; generally less than 2/8 coverage, except on windward slopes of elevated terrain; average width of cloud is at least as great as its vertical thickness

1 Cumulus of intermediate size with cloud cover less than 5/8; average cloud width is more than its vertical thickness; towers are vertical with little or no evidence of precipitation, except along slopes of elevated terrain; a general absence of middle and upper clouds

2 Swelling Cumulus with rapidly growing tall turrets which decrease in size with height and whose tops tend to separate from the longer cloud body and evaporate within minutes of the separation

3 Swelling Cumulus with towers having a pronounced tilt in a downwind direction; vertical cloud thickness is more than one and a half times that of its average width

4 Swelling Cumulus with towers having a pronounced tilt in an upwind direction; vertical cloud thickness is more than one and a half times that of its average width

5 Tall Cumulus congestus with vertical thickness more than twice the average width; not organized in clusters or lines; one or more layers of clouds extend out from the cloud towers, although no continuous cloud layers exist (see Note)

6 Isolated Cumulonimbus or large clusters of Cumulus turrets separated by wide areas in which clouds are absent; cloud bases are generally dark with showers observed in most cells; some scattered middle and upper clouds may be present; individual Cumulus cells are one to two times higher than they are wide

7 Numerous Cumulus extending through the middle troposphere with broken to overcast sheets of middle clouds and/or Cirrostratus; Cumulus towers do not decrease generally in size with height; ragged dark cloud bases with some showers present

8 Continuous dense middle clouds and/or Cirrostratus cloud sheets with some large isolated Cumulonimbus or Cumulus congestus clouds penetrating these sheets; light rain occasionally observed from the Altostratus; Cumulonimbus bases ragged and dark with showers visible (see Note)

9 Continuous sheets of middle clouds and/or Cirrostratus with Cumulonimbus and Cumulus congestus in organized lines or cloud bands; rain is generally observed from Altostratus sheets and heavy showers from Cumulonimbus; wind has a squally character

10 State of sky unknown or not described by any of the above

11--14 Reserved

15 Missing value

Note: In the event of obscuration of clouds due to heavy rain, the observer should use code 5 or 8. Code 5 should be used if the rain is localized or is brief in duration; Code 8 should be used if the rain is widespread or lasts for longer periods of time.

**0 20 056**

***Cloud phase***

Code figure

0 Unknown

1 Water

2 Ice

3 Mixed

4 Clear

5 Supercooled liquid water

6 Reserved

7 Missing value

**0 20 062**

***State of the ground (with or without snow)***

Code figure

0 Surface of ground dry (without cracks and no appreciable amount\
of dust or loose sand)

1 Surface of ground moist

2 Surface of ground wet (standing water in small or large pools on\
surface)

3 Flooded

4 Surface of ground frozen

5 Glaze on ground

6 Loose dry dust or sand not covering ground completely

7 Thin cover of loose dry dust or sand covering ground completely

8 Moderate or thick cover of loose dry dust or sand covering ground\
completely

9 Extremely dry with cracks

10 Ground predominantly covered by ice

11 Compact or wet snow (with or without ice) covering less than one\
half of the ground

12 Compact or wet snow (with or without ice) covering at least one\
half of the ground but ground not completely covered

13 Even layer of compact or wet snow covering ground completely

14 Uneven layer of compact or wet snow covering ground completely

15 Loose dry snow covering less than one half of the ground

16 Loose dry snow covering at least one half of the ground but ground\
not completely covered

17 Even layer of loose dry snow covering ground completely

18 Uneven layer of loose dry snow covering ground completely

19 Snow covering ground completely; deep drifts

20--30 Reserved

31 Missing value

Notes:

\(1) The definitions in code numbers 0 to 2 and 4 apply to representative bare ground and numbers 3, 5 to 9 and 10 to 19 to an open representative area.

\(2) In all instances the highest code figures applicable are to be reported.

\(3) In the above code table, whenever reference is made to ice, it also includes solid precipitation other than snow.

**\
**

**0 20 063**

***Special phenomena***

Code figure

0 Reserved

1 Highest wind speed gusts greater than 11.5 m/s

2 Highest mean wind speed greater than 17.5 m/s

3--6 Reserved

7 Visibility greater than 100 000 m

8--9 Reserved

*10--19 Mirage*

10 Mirage -- No specification

11 Mirage -- Image of distant object raised (looming)

12 Mirage -- Image of distant object raised clear above the horizon

13 Mirage -- Inverted image of distant object

14 Mirage -- Complex, multiple images of distant object (images not inverted)

15 Mirage -- Complex, multiple images of distant object (some images being inverted)

16 Mirage -- Sun or moon seen appreciably distorted

17 Mirage -- Sun visible, although astronomically below the horizon

18 Mirage -- Moon visible, although astronomically below the horizon

19 Reserved

*20--22 Day darkness, worst in direction specified*

20 Day darkness, bad, worst in direction specified

21 Day darkness, very bad, worst in direction specified

22 Day darkness, black, worst in direction specified

23--30 Reserved

*31--39 Coloration and/or convergence of clouds associated with a tropical*\
*disturbance*

31 Slight coloration of clouds at sunrise associated with a tropical disturbance

32 Deep-red coloration of clouds at sunrise associated with a tropical disturbance

33 Slight coloration of clouds at sunset associated with a tropical disturbance

34 Deep-red coloration of clouds at sunset associated with a tropical disturbance

35 Convergence of C~H~ clouds at a point below 45° forming or increasing and associated with a tropical disturbance

36 Convergence of C~H~ clouds at a point above 45° associated with a tropical

disturbance

37 Convergence of C~H~ clouds at a point below 45° dissolving or diminishing and\
associated with a tropical disturbance

38 Convergence of C~H~ clouds at a point above 45° associated with a tropical disturbance

39 Reserved

*40--43 Hoar frost or coloured precipitation*

40 Hoar frost on horizontal surfaces

41 Hoar frost on horizontal and vertical surfaces

42 Precipitation containing sand or desert dust

43 Precipitation containing volcanic ash

44--49 Reserved

*(continued)*

*\
(Code table 0 20 063 -- continued)*

Code figure

*50--59 Nature and/or type of squall*

50 Calm or light wind followed by a squall

51 Calm or light wind followed by a succession of squalls

52 Gusty weather followed by a squall

53 Gusty weather followed by a succession of squalls

54 Squall followed by gusty weather

55 General gusty weather with squall at intervals

56 Squall approaching station

57 Line squall

58 Squall with drifting or blowing dust or sand

59 Line squall with drifting or blowing dust or sand

*60--69 Variation of temperature during the period specified, associated with glaze\
or rime*

60 Temperature steady

61 Temperature falling, without going below 0 °C

62 Temperature rising, without going above 0 °C

63 Temperature falling to a value below 0 °C

64 Temperature rising to a value above 0 °C

65 Irregular variation, oscillations of temperature passing through 0 °C

66 Irregular variation, oscillations of temperature not passing through 0 °C

67 Variation of temperature not observed

68 Not allocated

69 Variation of temperature unknown owing to lack of thermograph

*70--79 Variation of visibility during the period specified*

70 Visibility has not varied (sun\* visible) towards direction specified

71 Visibility has not varied (sun\* invisible) towards direction specified

72 Visibility has increased (sun\* visible) towards direction specified

73 Visibility has increased (sun\* invisible) towards direction specified

74 Visibility has decreased (sun\* visible) towards direction specified

75 Visibility has decreased (sun\* invisible) towards direction specified

76 Fog coming from direction specified

77 Fog has lifted, without dissipating

78 Fog has dispersed without regard to direction

79 Moving patches or banks of fog

*80--89 Optical phenomena*

80 Brocken spectre

81 Rainbow

82 Solar or lunar halo

83 Parhelia or anthelia

84 Sun pillar

85 Corona

86 Twilight glow

87 Twilight glow on the mountains (Alpenglühen)

88 Mirage

89 Zodiacal light

90 St Elmo's fire

91--1022 Reserved

1023 Missing value

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\* Or sky (if sun is low), or moon or stars at night.

**0 20 071**

***Accuracy of fix and rate of atmospherics***

Code figure Accuracy of fix (estimated error) Repetition rate

0 No assessment No assessment

1 Less than 50 km Less than 1 per second

2 Between 50 and 200 km Less than 1 per second

3 More than 200 km Less than 1 per second

4 Less than 50 km 1 or more per second

5 Between 50 and 200 km 1 or more per second

6 More than 200 km 1 or more per second

7 Less than 50 km Rate so rapid number cannot be counted

8 Between 50 and 200 km Rate so rapid number cannot be counted

9 More than 200 km Rate so rapid number cannot be counted

10--14 Reserved

15 Missing value

**0 20 085**

***General condition of runway***

Code figure

0 Cleared (CLRD//)

1 All runways closed (SNOCLO)

2--14 Reserved

15 Missing value

**0 20 086**

***Runway deposits***

Code figure

0 Clear and dry

1 Damp

2 Wet with water patches

3 Rime and frost covered (depth normally less than 1 mm)

4 Dry snow

5 Wet snow

6 Slush

7 Ice

8 Compacted or rolled snow

9 Frozen ruts or ridges

10--14 Reserved

15 Missing or not reported (e.g. due to runway clearance in progress)

**0 20 087**

***Runway contamination***

Code figure

0 Reserved

1 Less than 10% of runway covered

2 11% to 25% of runway covered

3--4 Reserved

5 26% to 50% of runway covered

6--8 Reserved

9 51% to 100% of runway covered

10--14 Reserved

15 Missing or not reported (e.g. due to runway clearance in progress)

**0 20 089**

***Runway friction coefficient***

Code figure

0 0.00

1 0.01

2--88 0.02...0.88

89 0.89

90 0.90

91 Braking action poor

92 Braking action medium to poor

93 Braking action medium

94 Braking action medium to good

95 Braking action good

96--98 Reserved

99 Unreliable

100--126 Reserved

127 Missing, not reported and/or runway not operational

**0 20 090**

***Special clouds***

Code figure

0 Reserved

1 Nacreous clouds

2 Noctilucent clouds

3 Clouds from waterfalls

4 Clouds from fires

5 Clouds from volcanic eruptions

6--14 Reserved

15 Missing value

**0 20 101**

***Locust (acridian) name***

Code figure

0 Reserved

1 Schistocerca gregaria

2 Locusta migratoria

3 Nomadacris septemfasciata

4 Oedaleus senegalensis

5 Anracridium spp

6 Other locusts

7 Other grasshoppers

8 Other crickets

9 Spodoptera exempta

10--14 Reserved

15 Missing value

**0 20 102**

***Locust (maturity) colour***

Code figure

0 Green

1 Green or black

2 Black

3 Yellow and black

4 Straw/grey

5 Pink

6 Dark red/brown

7 Mixed red and yellow

8 Yellow

9 Other

10--14 Reserved

15 Missing value

**0 20 103**

***Stage of development of locusts***

Code figure

0 Hoppers (nymphs, larvae), stage 1

1 Hoppers (nymphs, larvae), stage 2 or mixed 1, 2 instars (stages)

2 Hoppers (nymphs, larvae), stage 3 or mixed 2, 3 instars

3 Hoppers (nymphs, larvae), stage 4 or mixed 3, 4 instars

4 Hoppers (nymphs, larvae), stage 5 or mixed 4, 5 instars

5 Hoppers (nymphs, larvae), stage mixed, all or many instars

6 Fledglings (wings too soft for sustained flight)

7 Immature adults

8 Mixed maturity adults

9 Mature adults

10--14 Reserved

15 Missing value

**0 20 104**

***Organization state of swarm or band of locusts***

Code figure

0 Hoppers only, mainly in bands or clusters

1 Winged adults in the vicinity more than 10 kilometres from point of observation

2 Locusts in flight, a few seen at the station

3 Locusts at the station, most of them on the ground

4 Locusts, some on ground and others in flight at a height less than 10 metres

5 Locusts, some on ground and others in flight at a height greater than 10 metres

6 Locusts, most in flight at a height less than 10 metres

7 Locusts, most in flight at a height greater than 10 metres

8 Locusts, all over inflicting severe damage to vegetation, no extermination operation

9 Locusts, all over inflicting severe damage to vegetation, extermination operation in progress

10--14 Reserved

15 Missing value

**0 20 105**

***Size of swarm or band of locusts and duration of passage of swarm***

Code figure

When 0 20 104 (organization state of swarm or band of locusts) = 0

0 Reserved

1 Area covered by isolated bands \< 10 m^2^

2 Area covered by isolated bands 10 -- 100 m^2^

3 Area covered by isolated bands 100 -- 1000 m^2^

4 Area covered by isolated bands 1 000 -- 10000 m^2^

5 Area covered by isolated bands 1 -- 10 ha

6 Area covered by isolated bands \> 10 ha

7 Area covered by dispersed bands \< 100 km^2^

8 Area covered by dispersed bands 100 -- 1000 km^2^

9 Area covered by dispersed bands \> 1000 km^2^

10--14 Reserved

15 Missing value

When 0 20 104 (organization state of swarm or band of locusts) = 1 to 9

0 Small swarm less than 1 km^2^ or adults in ground, tens or hundreds of individuals visible simultaneously, duration of passage less than 1 hour ago

1 Small swarm less than 1 km^2^ or adults in ground, tens or hundreds of individuals visible simultaneously, duration of passage 1 to 6 hours ago

2 Small swarm less than 1 km^2^ or adults in ground, tens or hundreds of individuals visible simultaneously, duration of passage over 6 hours ago

3 Medium swarm or scattered adults, several visible simultaneously, duration of passage less than 1 hour ago

4 Medium swarm or scattered adults, several visible simultaneously, duration of passage 1 to 6 hours ago

*(continued)*

*\
(Code table 0 20 105 -- continued)*

Code figure

5 Medium swarm or scattered adults, several visible simultaneously, duration of passage over 6 hours ago

6 Large swarm or isolated adults, seen singly, duration of passage less than 1 hour ago

7 Large swarm or isolated adults, seen singly, duration of passage 1 to 6 hours ago

8 Large swarm or isolated adults, seen singly, duration of passage over 6 hours ago

9 More than one swarm of locusts

10 Size of swarm and/or duration of passage not determined owing to darkness or similar phenomena

11--14 Reserved

15 Missing value

**0 20 106**

***Locust population density***

Code figure

0 Reserved

1 Thin density swarm (swarm visible only when near enough for individual locusts to be discerned)

2 Medium density swarm

3 Dense swarm (obscuring nearby features, e.g. trees)

4 Isolated hoppers seen singly

5 Scattered hoppers, several visible simultaneously

6--14 Reserved

15 Missing value

**0 20 107**

***Direction of movements of locust swarm***

Code figure

0 Reserved

1 Generally in the direction NE

2 Generally in the direction E

3 Generally in the direction SE

4 Generally in the direction S

5 Generally in the direction SW

6 Generally in the direction W

7 Generally in the direction NW

8 Generally in the direction N

9 Specific direction indeterminable

10--14 Reserved

15 Missing value

**0 20 108**

***Extent of vegetation***

Code figure

0 Bare ground

1 Dry, presence of few and isolated shrubs

2 Sparse vegetation (sprouting)

3 Dense vegetation (sprouting)

4 Sparse vegetation (growing)

5 Dense vegetation (growing)

6 Sparse vegetation in flower

7 Dense vegetation in flower

8--14 Reserved

15 Missing value

**0 20 119**

***Lightning discharge polarity***

Code figure

0 Not defined

1 Positive

2 Negative

3 Missing value

**0 20 124**

***Lightning stroke or flash***

Code figure

0 Not defined

1 Lightning stroke

2 Lightning flash, by manual observation, or if equipment insensitive to stroke resolution

3 Missing value

**0 20 136**

***Supplementary cloud type***

Code figure

*0--7 Nature of clouds of vertical development (*C~a~ *-- Code table 0531)*

0 Isolated cumulus humilis and/or cumulus mediocris

1 Numerous cumulus humilis and/or cumulus mediocris

2 Isolated cumulus congestus

3 Numerous cumulus congestus

4 Isolated cumulonimbus

5 Numerous cumulonimbus

6 Isolated cumulus and cumulonimbus

7 Numerous cumulus and cumulonimbus

*(continued)*

*\
(Code table 0 20 136 -- continued)*

Code figure

8--9 Reserved

*10--19 Orographic clouds (C~0~ -- Code table 0561)*

10 Reserved

11 Isolated orographic clouds, pileus, incus, forming

12 Isolated orographic clouds, pileus, incus, not changing

13 Isolated orographic clouds, pileus, incus, dissolving

14 Irregular banks of orographic cloud, föhn bank, etc., forming

15 Irregular banks of orographic cloud, föhn bank, etc., not changing

16 Irregular banks of orographic cloud, föhn bank, etc., dissolving

17 Compact layer of orographic cloud, föhn bank, etc., forming

18 Compact layer of orographic cloud, föhn bank, etc., not changing

19 Compact layer of orographic cloud, föhn bank, etc., dissolving

*20--29 Cloud conditions over mountains and passes (*N~m~ *-- Code table 2745)*

20 All mountains open, only small amounts of cloud present

21 Mountains partly covered with detached clouds (not more than half the peaks can be seen)

22 All mountain slopes covered, peaks and passes free

23 Mountains open on observer's side (only small amounts of cloud present), but a continuous wall of cloud on the other side

24 Clouds low above the mountains, but all slopes and mountains open (only small amounts of cloud on the slopes)

25 Clouds low above the mountains, peaks partly covered by precipitation trails or clouds

26 All peaks covered but passes open, slopes either open or covered

27 Mountains generally covered but some peaks free, slopes wholly or partially covered

28 All peaks, passes and slopes covered

29 Mountains cannot be seen owing to darkness, fog, snowstorm, precipitation, etc.

30--34 Reserved

*35--39 Condensation trails (*N~t~ *-- Code table 2752)*

35 Non-persistent condensation trails

36 Persistent condensation trails covering less than 1/8 of the sky

37 Persistent condensation trails covering 1/8 of the sky

38 Persistent condensation trails covering 2/8 of the sky

39 Persistent condensation trails covering 3/8 or more of the sky

*40--49 Cloud conditions observed from a higher level (*N~v~ *-- Code table 2754)*

40 No cloud or mist

41 Mist, clear above

42 Fog patches

43 Layer of slight fog

44 Layer of thick fog

45 Some isolated clouds

46 Isolated clouds and fog below

47 Many isolated clouds

48 Sea of clouds

49 Bad visibility obscuring the downward view

50--510 Reserved

511 Missing value

**0 20 137**

***Evolution of clouds***

Code figure

0 No change

1 Cumulification

2 Slow elevation

3 Rapid elevation

4 Elevation and stratification

5 Slow lowering

6 Rapid lowering

7 Stratification

8 Stratification and lowering

9 Rapid change

10--14 Reserved

15 Missing value

**0 20 138**

***Road surface condition***

Code figure

0 Dry

1 Moist

2 Wet

3 Rime

4 Snow

5 Ice

6 Glaze

7 Not dry

8--14 Reserved

15 Missing value

**0 21 066**

***Wave scatterometer product confidence data***

Bit No.

1 Processing equipment not working

2 Equipment failed

3 PRF code changed during image generation

4 Sampling window changed during image generation

5 Gain changed during image generation

6 Chirp replica exceeds specified value

7 Input data mean and standard deviation of in-phase and quadrature out of range

8 Doppler centroid confidence \> MMCC value

9 Doppler centroid absolute value \> PRF/2

10 Doppler ambiguity confidence \< MMCC value

11 Output data mean and standard deviation ≤ MMCC value

All 12 Missing value

Notes:

\(1) MMCC is Mission Management Control Centre.

\(2) PRF is pulse repetition frequency.

**0 21 067**

***Wind product confidence data***

Bit No.

1 No forebeam calculation

2 No midbeam calculation

3 No aftbeam calculation

4 Forebeam arcing detected

5 Midbeam arcing detected

6 Aftbeam arcing detected

7 Any beam noise content above or equal to threshold

8 Land (any land in cell footprint)

9 Autonomous ambiguity removal not used

10 Meteorological background not used

11 Minimum residual exceeded threshold

12 Frame checksum error detected

All 13 Missing value

**0 21 068**

***Radar altimeter product confidence data***

Bit No.

1 Standard deviation of wind speed outside MMCC limit

2 Standard deviation of significant wave height outside MMCC limit

3 Standard deviation of altitude outside MMCC limit

4 Mean peakiness outside MMCC limit

5 Frame checksum error detected

6 Height-time loop time constant correction not performed

7 Not enough measurements (N \< 10)

All 8 Missing value

Note: MMCC is Mission Management Control Centre.

**0 21 069**

***SST product confidence data***

Bit No.

1 12.0 µm channel present in source data

2 11.0 µm channel present in source data

3 3.7 µm channel present in source data

4 1.6 µm channel present in source data

5 Cloud identification used 1.6 µm histogram reflectance cloud test

6 1.6 µm histogram reflectance cloud test used dynamic threshold

7 Sun glint detected by 1.6 µm reflectance cloud test

8 3.7 µm channel used in sea-surface temperature retrieval

9 Sea-surface temperature derivation used daytime data (night-time if zero)

All 10 Missing value

**0 21 070**

***SST product confidence data (SADIST-2)***

Bit No.

*1--9 Nadir-only view SST retrieval used 3.7 micron channel (one bit per 10-arcmin cell)*

1 Cell 1: nadir-only view SST used 3.7 micron channel

2 Cell 2: nadir-only view SST used 3.7 micron channel

3 Cell 3: nadir-only view SST used 3.7 micron channel

4 Cell 4: nadir-only view SST used 3.7 micron channel

5 Cell 5: nadir-only view SST used 3.7 micron channel

6 Cell 6: nadir-only view SST used 3.7 micron channel

7 Cell 7: nadir-only view SST used 3.7 micron channel

8 Cell 8: nadir-only view SST used 3.7 micron channel

9 Cell 9: nadir-only view SST used 3.7 micron channel

*(continued)*

*\
(Flag table 0 21 070 -- continued)*

Bit No.

*10--18 Dual view SST retrieval used 3.7 micron channel (one bit per 10-arcmin cell)*

10 Cell 1: dual view SST used 3.7 micron channel

11 Cell 2: dual view SST used 3.7 micron channel

12 Cell 3: dual view SST used 3.7 micron channel

13 Cell 4: dual view SST used 3.7 micron channel

14 Cell 5: dual view SST used 3.7 micron channel

15 Cell 6: dual view SST used 3.7 micron channel

16 Cell 7: dual view SST used 3.7 micron channel

17 Cell 8: dual view SST used 3.7 micron channel

18 Cell 9: dual view SST used 3.7 micron channel

19 Nadir view contains day-time data (night if zero)

20 Forward view contains day-time data (night if zero)

21 Record contains contributions from instrument scans acquired when ERS platform not inyaw-steering mode

22 Record contains contributions from instrument scans for which product confidence data show quality is poor or unknown

All 23 Missing value

**0 21 072**

***Satellite altimeter calibration status***

Bit No.

1 Height error correction applied instead of open loop calibration

2 Microwave sounder used for troposphere correction

3 AGC output correction applied instead of open loop calibration

All 4 Missing value

**0 21 073**

***Satellite altimeter instrument mode***

Bit No.

1 Blank data record

2 Test

3 Calibration (closed loop)

4 BITE

5 Acquisition on ice

6 Acquisition on ocean

7 Tracking on ice

8 Tracking on ocean

All 9 Missing value

**0 21 076**

***Representation of intensities***

Code figure

0 Linear

1 Logarithmic (base e)

2 Logarithmic (base 10)

3--6 Reserved

7 Missing value

**0 21 109**

***SEAWINDS wind vector cell quality***

Bit No.

1 Not enough good sigma-0 available for wind retrieval

2 Poor azimuth diversity among sigma-0 for wind retrieval

3--7 Reserved

8 Some portion of wind vector cell is over land

9 Some portion of wind vector cell is over ice

10 Wind retrieval not performed for wind vector cell

11 Reported wind speed is greater than 30 m s^--1^

12 Reported wind speed is less than or equal to 3 m s^--1^

13--16 Reserved

All 17 Missing value

**0 21 115**

***SEAWINDS sigma-0 quality***

Bit No.

1 Sigma-0 measurement is not usable

2 Signal to noise ratio is low

3 Sigma-0 is negative

4 Sigma-0 is outside of acceptable range

5 Scatterometer pulse quality is not acceptable

6 Sigma-0 cell location algorithm does not converge

7 Frequency shift lies beyond the range of the x factor table

8 Spacecraft temperature is beyond calibration coefficient range

9 No applicable altitude records were found for this sigma-0

10 Interpolated ephemeris data are not acceptable for this sigma-0

11--16 Reserved

All 17 Missing value

**0 21 116**

***SEAWINDS sigma-0 mode***

Bit No.

1 Calibration/measurement pulse flag (1)

2 Calibration/measurement pulse flag (2)

3 Outer antenna beam

4 Sigma-0 cell is aft of spacecraft

5 Current mode (1)

6 Current mode (2)

7 Effective gate width -- slice resolution (1)

8 Effective gate width -- slice resolution (2)

9 Effective gate width -- slice resolution (3)

10 Low resolution mode -- whole pulse data

11 Scatterometer electronic subsystem B

12 Alternate spin rate -- 19.8 rpm

13 Receiver protection on

14 Slices per composite flag (1)

15 Slices per composite flag (2)

16 Slices per composite flag (3)

All 17 Missing value

**0 21 119**

***Wind scatterometer geophysical model function***

Code figure

0 Reserved

1 SASS

2 SASS2

3 NSCAT0

4 NSCAT1

5 NSCAT2

6 QSCAT0

7 QSCAT1

8--30 Reserved

31 CMOD1

32 CMOD2

33 CMOD3

34 CMOD4

35 CMOD5

36--62 Reserved

63 Missing value

**0 21 144**

***Altimeter rain flag***

Bit No.

1 Rain

All 2 Missing value

**0 21 148**

***Trailing edge variation flag***

Bit No.

1 Non short scale variation

2 Short scale variation

3--8 Reserved

All 9 Missing value

**0 21 150**

***Beam co-location***

Code figure

0 Data from single ground station (no co-location)

1 Data from multiple ground station (co-located data)

2 Reserved

3 Missing value

**0 21 155**

***Wind vector cell quality***

Bit No.

1 Not enough good sigma-0 available for wind retrieval

2 Poor azimuth diversity among sigma-0 for wind retrieval

3 Any beam noise content above threshold

4 Product monitoring not used

5 Product monitoring flag

6 KNMI quality control fails

7 Variational quality control fails

8 Some portion of wind vector cell is over land

9 Some portion of wind vector cell is over ice

10 Wind retrieval not performed for wind vector cell

11 Reported wind speed is greater than 30 m/s

12 Reported wind speed is less than or equal to 3 m/s

13 Rain flag for the wind vector cell is not usable

14 Rain flag algorithm detects rain

15 No meteorological background used

16 Data are redundant

17--23 Reserved

All 24 Missing value

**0 21 158**

***ASCAT Kp estimate quality***

Code figure

0 Acceptable

1 Not acceptable

2 Reserved

3 Missing value

**0 21 159**

***ASCAT sigma-0 usability***

Code figure

0 Good

1 Usable

2 Bad

3 Missing value

**0 21 169**

***Ice presence indicator***

Code figure

0 No ice present

1 Ice present

2 Reserved

3 Missing value

**0 22 056**

***Direction of profile***

Code figure

0 Upwards profile

1 Downwards profile

2 Horizontal

3 Missing value

**0 22 060**

***Lagrangian drifter drogue status***

Code figure

0 Drogue is detached

1 Drogue is attached

2 Drogue status unknown

3--6 Reserved

7 Missing value

**0 22 061**

***State of the sea***

Code figure Height in metres

0 Calm (glassy) 0

1 Calm (rippled) 0 -- 0.1

2 Smooth (wavelets) 0.1 -- 0.5

3 Slight 0.5 -- 1.25

4 Moderate 1.25 -- 2.5

5 Rough 2.5 -- 4

6 Very rough 4 -- 6

7 High 6 -- 9

8 Very high 9 -- 14

9 Phenomenal Over 14

10--14 Reserved

15 Missing value

Notes:

\(1) These values refer to well-developed wind waves of the open sea. While priority shall be given to the descriptive terms, these height values may be used for guidance by the observer when reporting the total state of agitation of the sea resulting from various factors such as wind, swell, currents, angle between swell and wind, etc.

\(2) The exact bounding height shall be assigned for the lower code figure; e.g., a height of 4 m is coded as 5.

**0 22 067**

***Instrument type for water temperature/salinity profile measurement***

*(See common Code table C--3)*

**0 22 068**

***Water temperature profile recorder types***

*(See common Code table C--4)*

**0 22 120**

***Tide station automated water level check***

Code figure

0 Good data

1 Maximum (high) water level limit exceeded

2 Minimum (low) water level limit exceeded

3 Rate of change limit for water level exceeded

4 Flat limit for water level exceeded

5 Observed minus predicted water level value limit exceeded

6 Observed value from primary water level sensor minus backup water level sensor

7 Value exceeded specified tolerance from expected value

8 Water level QA parameter (sigmas and/or outliers) limits exceeded

9 Sea temperature outside of expected range

10 Multiple QC checks (above) failed

11 No automated water level checks performed

12--30 Reserved

31 Missing value

**0 22 121**

***Tide station manual water level check***

Code figure

0 Operational

1 Possible clogging problem or otherwise degraded water level data

2 Possible datum shift

3 Unknown status of water level sensor

4 Suspected or known sea-temperature sensor problem

5 Multiple possible problems (above)

6 Bad data -- DO NOT DISSEMINATE!

7 No manual water level checks performed

8--30 Reserved

31 Missing value

**0 22 122**

***Tide station automated meteorological data check***

Code figure

0 Good data from all sensors

1 Wind direction outside of allowable range

2 Wind speed outside of expected range

3 Barometric pressure outside of expected range

4 Air temperature outside of expected range

5 Multiple sensors failed QC checks

6 No automated meteorological data checks performed

7--30 Reserved

31 Missing value

**0 22 123**

***Tide station manual meteorological data check***

Code figure

0 Operational

1 Suspected or known problem with wind sensor

2 Suspected or known problem with barometric pressure sensor

3 Suspected or known problem with air temperature sensor

4 Unknown status of all sensors

5 Suspected or known problems with multiple sensors

6 Bad data -- DO NOT DISSEMINATE!

7 No manual meteorological data checks performed

8--30 Reserved

31 Missing value

**0 22 178**

***XBT/XCTD launcher type***

Code figure

0 Unknown

1 LM-2A Deck-mounted

2 LM-3A Hand-Held

3 LM-4A Thru-Hull

4--9 Reserved

10 AL-12 TSK Autolauncher (up to 12 probes)

11--19 Reserved

20 SIO XBT Autolauncher (up to 6 probes)

21--29 Reserved

30 AOML XBT V6 Autolauncher (up to 6 Deep Blue probes)

31 AOML XBT V8.0 Autolauncher (up to 8 Deep Blue probes)

32 AOML XBT V8.1 Autolauncher (up to 8 Deep Blue and Fast Deep probes)

33--89 Reserved

90 CSIRO Devil Autolauncher

91--99 Reserved

100 MFSTEP Autolauncher (Mediterranean)

101--254 Reserved

255 Missing value

**0 23 001**

***Accident early notification -- article applicable***

Code figure

0 Reserved

1 Articles 1 and 2

2 Article 3

3 Article 5.2

4--6 Reserved

7 Missing value

**0 23 002**

***Activity or facility involved in incident***

Code figure

0 Reserved

1 Nuclear reactor on ground

2 Nuclear reactor at sea

3 Nuclear reactor in space

4 Nuclear fuel facility

5 Radioactive waste management facility

6 Transport of nuclear fuel or radioactive waste

7 Storage of nuclear fuel or radioactive waste

8 Manufacture of radio-isotopes

9 Use of radio-isotopes

10 Storage of radio-isotopes

11 Disposal of radio-isotopes

12 Transport of radio-isotopes

13 Use of radio-isotopes for power generation

14--29 Reserved

30 Other

31 Missing value

**0 23 003**

***Type of release***

Code figure

0 No release

1 Release to atmosphere

2 Release to water

3 Release to both atmosphere and water

4 Expected release to atmosphere

5 Expected release to water

6 Expected release to both atmosphere and water

7 Missing value

**0 23 004**

***Countermeasures taken near border***

Code figure

0 No countermeasures

1 Evacuation

2 Sheltering

3 Prophylaxis

4 Water

5--6 Reserved

7 Missing value

**0 23 005**

***Cause of incident***

Code figure

0 Incident State does not understand what happened

1 Incident State knows the cause of the incident

2 Reserved

3 Missing value

**0 23 006**

***Incident situation***

Code figure

0 No improvement

1 Unstable

2 No deterioration

3 Improving

4 Stable

5 Deteriorating

6 Reserved

7 Missing value

**0 23 007**

***Characteristics of release***

Code figure

0 No release

1 Release has stopped

2 Release

3 Release is continuing

4--6 Reserved

7 Missing value

**0 23 008/0 23 009**

***State of current or expected release***

Code figure

0 Gaseous

1 Particulate

2 Mixture of gaseous and particulate

3 Missing value

**0 23 016**

***Possibility of significant chemical toxic health effect***

Code figure

0 No significant chemical toxic health effect

1 Significant chemical toxic health effect possible

2 Reserved

3 Missing value

**0 23 018**

***Release behaviour over time***

Code figure

0 Release no longer occurring

1 Release still occurring

2 Release expected to increase in next six hours

3 Release expected to remain constant in next six hours

4 Release expected to decrease in next six hours

5--6 Reserved

7 Missing value

**0 23 031**

***Possibility that plume will encounter precipitation\
in State in which incident occurred***

Code figure

0 Plume will not encounter rain in incident State

1 Plume will encounter rain in incident State

2 Reserved

3 Missing value

**0 23 032**

***Plume will encounter change in wind direction and/or speed flag***

Code figure

0 No significant change expected within the next six hours

1 Anticipated significant change expected within the next six hours

2 Reserved

3 Missing value

**0 24 003**

***Composition of release***

Code figure

0 Noble gases

1 Iodines

2 Caesiums

3 Transuranics

4--30 Reserved

31 Missing value

**0 25 004**

***Echo processing***

Code figure

0 Incoherent

1 Coherent (Doppler)

2 Reserved

3 Missing value

**0 25 005**

***Echo integration***

Code figure

0 Logarithm -- 2.5 dB

1 Linear

2 Special

3 Missing value

**0 25 006**

***Z to R conversion***

Code figure

0 ZH to R conversion

1 (ZH, ZDR) to (NO, DO) to R

2 (Z (F1), Z (F2)) to attenuation to R

3--5 Reserved

6 Other

7 Missing value

**0 25 009**

***Calibration method***

Bit No.

1 None

2 Calibration target or signal

3 Against raingauges

4 Against other Instruments (disdrometer -- attenuation)

All 4 Missing value

Note: Descriptor 0 25 009 is deprecated. 0 25 029 should be used instead.

**0 25 010**

***Clutter treatment***

Code figure

0 None

1 Map

2 Insertion of higher elevation data and map

3 Analysis of the fluctuating logarithm signal (clutter detection)

4 Extraction of the fluctuating part of linear signal (clutter suppression)

5 Clutter suppression -- Doppler

6 Multiparameter analysis

7--14 Reserved

15 Missing value

**0 25 011**

***Ground occultation correction (screening)***

Code figure

0 None

1 Map of correction factors

2 Interpolation (azimuth or elevation)

3 Missing value

**0 25 012**

***Range attenuation correction***

Code figure

0 Hardware

1 Software

2 Hardware and software

3 Missing value

**0 25 013**

***Bright-band correction***

Bit No.

1 Bright-band correction

All 2 Missing value

**0 25 015**

***Radome attenuation correction***

Bit No.

1 Radome attenuation correction

All 2 Missing value

**0 25 017**

***Precipitation attenuation correction***

Bit No.

1 Precipitation attenuation correction

All 2 Missing value

**0 25 020**

***Mean speed estimation***

Code figure

0 FFT (fast Fourier transform)

1 PPP (pulse-pair processing)

2 VPC (vector-phase change)

3 Missing value

**0 25 021**

***Wind computation enhancement***

Bit No.

1 Simple average

2 Consensus average

3 Median check

4 Vertical consistency check

5 Other

6--7 Reserved

All 8 Missing value

**0 25 022**

***GHRSST\* rejection flag***

Bit No.

1 Unprocessed

2 Land suspected

3 Wind speed too large

4 Ice detected

5 Rain detected (Microwave retrievals only)

6 Cloudy detected (Infra-red retrievals only)

7 Cosmetic value

8 SST out of range

All 9 Missing value

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\* GHRSST = GODAE high-resolution sea-surface temperature

**0 25 023**

***GHRSST confidence flag***

Bit No.

1 Default confidence value has been used

2 Default bias and standard deviation have been used

3 Sun glint suspected

4 Sea-ice retrieval for microwave data

5 High wind speed retrieval

6 Inaccurate SST due to low SST (\< 285K) (only applies to the TMI instrument)

7 Relaxed rain contamination suspected

8 Potential side lobe contamination

All 9 Missing value

**0 25 024**

***GHRSST data quality***

Code figure

0 Unprocessed infrared retrieval

1 Cloudy retrievals

2 Bad: Data that are probably contaminated by cloud

3 Suspect data

4 Acceptable data

5 Excellent data

6 Cool skin suspected

7--9 Reserved

10 Unprocessed microwave retrieval

11 Questionable microwave retrieval that may be contaminated

12 Acceptable microwave retrieval

13 High probability of diurnal variability

14 Reserved

15 Missing value

**0 25 029**

***Calibration method***

Bit No.

1 Reserved

2 Calibration target or signal

3 Against raingauges

4 Against other instruments (disdrometer -- attenuation)

5 Reserved

All 6 Missing value

**0 25 030**

***Running mean sea-surface temperature usage***

Code figure

0 Running mean sea-surface temperature not used because usage criteria not met

1 Running mean sea-surface temperature not used because data not available

2 Running mean sea-surface temperature used as predictor

3 Missing value

**0 25 031**

***NWP-generated vertical profile thinning method***

Code figure Meaning

0 Reserved

1 No thinning applied (all native model levels are included from base to top of pseudo-\
sounding)

2 Native model levels are present only if they are significant levels as per regulations\
B/C 25 for conventional TEMP soundings

3 A predefined subset of native model levels is present

4 No native model levels are present. All profile levels are interpolated to a predefined set\
of pressure coordinate levels

5--6 Reserved

7 Missing value

Note: None of the code figures exclude the addition of interpolated levels at the discretion of the generating centre.

**0 25 032**

***Wind profiler mode information***

Code figure

0 Reserved

1 Data from low mode

2 Data from high mode

3 Missing value

**0 25 033**

***Wind profiler submode information***

Code figure

0 Wind profiler operating in submode A

1 Wind profiler operating in submode B

2 Reserved

3 Missing value

**0 25 034**

***Wind profiler quality control test results***

Bit No. Meaning (1 = true, 0 = false)

1 Test A performed and failed

2 Test B performed and failed

3 Test results inconclusive

All 4 Missing value

**0 25 035**

***Decision method for polarity***

Code figure

0 Not defined

1 Individual voltage deflection

2 Current based, above a threshold

3 Voltage based, above a threshold

4 Consensus of sensors, current above a threshold

5 Consensus of sensors, voltage above a threshold

6 Reserved

7 Missing value

**0 25 036**

***Atmospherics location method***

Code figure

0 Network of several direction-finders operating on the same individual atmospherics

1 Network of several arrival-time stations operating on the same individual atmospherics

2--5 Reserved

6 Single station range bearing technique

7--14 Reserved

15 Missing value

**0 25 040**

***CO~2~ wind product derivation***

Code figure

0 Non-specific mode

1 First guess data

2 Cloud data

3 Average vector data

4 Primary data

5 Guess data

6 Vector data

7 Tracer data; this image

8 Tracer data to next image

9--14 Reserved

15 Missing value

**0 25 041**

***Moving platform direction reporting method***

Code figure

0 Direction originally reported in true degrees

1 Direction originally reported using Code table 0700, FM 13

2 Reserved

3 Missing value

Note: Where the original reporting method is as indicated by code figure 1, the following conversion is recommended to obtain a suitable data value corresponding to descriptor 0 01 012:

> Reported value Data value
>
> 0 0
>
> 1 45
>
> 2 90
>
> 3 135
>
> 4 180
>
> 5 225
>
> 6 270
>
> 7 315
>
> 8 360
>
> 9 511

**0 25 042**

***Moving platform speed reporting method***

Code figure

0 Speed originally reported in metres per second

1 Speed originally reported using Code table 4451, FM 13

2 Reserved

3 Missing value

Note: Where the original reporting method is as indicated by code figure 1, the following conversion is recommended to obtain a suitable data value corresponding to descriptor 0 01 013:

> Reported value Data value
>
> 0 0
>
> 1 1
>
> 2 4
>
> 3 7
>
> 4 9
>
> 5 12
>
> 6 14
>
> 7 17
>
> 8 19
>
> 9 21
>
> / 1023

**\
**

**0 25 045**

***HIRS channel combination***

Bit No.

1--20 Beginning with first bit position (high order bit),\
if bit position is set to 1, then channel is present,\
if bit position is set to 0, then channel is not present

All 21 Missing value

**0 25 046**

***MSU channel combination***

Bit No.

1--4 Beginning with first bit position (high order bit),\
if bit position is set to 1, then channel is present,\
if bit position is set to 0, then channel is not present

All 5 Missing value

**0 25 047**

***SSU channel combination***

Bit No.

1--3 Beginning with first bit position (high order bit),\
if bit position is set to 1, then channel is present;\
if bit position is set to 0, then channel is not present

All 4 Missing value

**0 25 048**

***AMSU-A channel combination***

Bit No.

1--15 Beginning with first bit position (high order bit),\
if bit position is set to 1, then channel is present,\
if bit position is set to 0, then channel is not present

All 16 Missing value

**0 25 049**

***AMSU-B channel combination***

Bit No.

1--5 Beginning with first bit position (high order bit),\
if bit position is set to 1, then channel is present,\
if bit position is set to 0, then channel is not present

All 6 Missing value

**\
**

**0 25 051**

***AVHRR channel combination***

Bit No.

1--6 Beginning with first bit position (high order bit),\
if bit position is set to 1, then channel is present,\
if bit position is set to 0, then channel is not present

All 7 Missing value

**0 25 053**

***Observation quality***

Bit No.

1 Good

2 Redundant

3 Questionable

4 Bad

5 Experimental

6 Precipitating

7--11 Reserved

All 12 Missing value

**0 25 063**

***Central processor or system identifier***

Code figure

0 Not defined

1 Main processor

2 Backup processor

3--254 Reserved

255 Missing value

**0 25 069**

***Flight level pressure corrections***

Bit No.

1 Smoothed

2 Baseline adjusted

3 Normalized time interval

4 Outlier checked

5 Plausibility checked

6 Consistency checked

7 Interpolated

All 8 Missing value

**0 25 086**

***Depth correction indicator***

Code figure

0 Depths are not corrected

1 Depths are corrected

2 Reserved

3 Missing value

**0 25 090**

***Orbit state flag***

Code figure

0 Orbit computed during a manoeuvre

1 Adjusted mission operations orbit

2 Extrapolated mission operations orbit

3 Adjusted (preliminary/precise) orbit

4 (Preliminary/precise) orbit is estimated during a manoeuvre period

5 (Preliminary/precise) orbit is interpolated over a tracking data gap

6 (Preliminary/precise) orbit is extrapolated for a duration less than 1 day

7 (Preliminary/precise) orbit is extrapolated for a duration that ranges from 1 day to 2 days

8 (Preliminary/precise) orbit is extrapolated for a duration larger than 2 days, or that the orbit is extrapolated just after a manoeuvre

9 DORIS\* DIODE\*\* navigator orbit

10--14 Reserved

15 Missing value

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\* DORIS stands for "Doppler orbitography and radio-positioning integrated by Satellite".

\*\* DIODE means *détermination immédiate d'orbite par DORIS embarqué* or immediate onboard orbit determination by DORIS. It is part of the DORIS instrument, which calculates the satellite's position and velocity.

**0 25 093**

***RASS computation correction***

Bit No.

1 No correction

2 Vertical velocity correction

3--6 Reserved

7 All corrections

All 8 Missing value

**0 25 095**

***Altimeter state flag***

Bit No.

1 Altimeter operating (0 if nominal, 1 if backup)

All 2 Missing value

**\
**

**0 25 096**

***Radiometer state flag***

Bit No.

1 Mode indicator (0 if mode 2, 1 if mode 1)

2 Mode 1 calibration sequence indicator (0 if normal data taking either mode 1 or 2, 1 if mode 1 calibration sequence)

Bits 3 and 4 indicate active 23.8 GHz channel(s):

3 Channel 2 (0 if on, 1 if off)

4 Channel 3 (0 if on, 1 if off)

All 5 Missing value

**0 25 097**

***Three-dimensional error estimate of the navigator orbit***

Code figure

0 Ranges between 0 and 30 cm

1 Ranges between 30 and 60 cm

2 Ranges between 60 and 90 cm

3 Ranges between 90 and 120 cm

4 Ranges between 120 and 150 cm

5 Ranges between 150 and 180 cm

6 Ranges between 180 and 210 cm

7 Ranges between 210 and 240 cm

8 Ranges between 240 and 270 cm

9 Ranges larger than 270 cm

10--14 Reserved

15 Missing value

**0 25 098**

***Altimeter data quality flag***

Bit No. (0 is good, 1 is bad)

1 Ku band range

2 C band range

3 Ku band SWH\*

4 C band SWH\*

5 Ku band backscatter coefficient

6 C band backscatter coefficient

7 Off nadir angle from Ku band waveform parameters

8 Off nadir angle from platform

All 9 Missing value

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\* SWH = Significant wave height

**0 25 099**

***Altimeter correction quality flag***

Bit No. (0 is good, 1 is bad)

1 Ku band range instrumental correction

2 C band range instrumental correction

3 Ku band SWH\* instrumental correction

4 C band SWH\* instrumental correction

5 Ku band backscatter coefficient instrumental correction

6 C band backscatter coefficient instrumental correction

7--8 Reserved

All 9 Missing value

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\* SWH = Significant wave height

**0 25 110**

***Image processing summary***

Bit No.

1 Raw data analysis used for raw data correction. Correction done using default parameters

2 Raw data analysis used for raw data correction. Correction done using raw data analysis results

3 Antenna elevation pattern correction applied

4 Nominal chirp replica used

5 Reconstructed chirp used

6 Slant range to ground range conversion applied

7--9 Reserved

All 10 Missing value

**0 25 112**

***Band specific altimeter data quality flag***

Bit No. (0 is good, 1 is bad)

1 Band specific range

2 Band specific significant wave height

3 Band specific backscatter coefficient

4 Off nadir angle from band specific waveform parameters

5 Off nadir angle from platform

6--8 Reserved

All 9 Missing value

**0 25 113**

***Band specific altimeter correction quality flag***

Bit No. (0 is good, 1 is bad)

1 Band specific range instrumental correction

2 Band specific significant wave height instrumental correction

3 Band specific backscatter coefficient instrumental correction

4--8 Reserved

All 9 Missing value

**0 25 120**

***RA2-L2-processing flag***

Code figure

0 Percentage of DSRs\* free of processing errors during Level 2 processing is greater than the acceptable threshold

1 Percentage of DSRs free of processing errors during Level 2 processing is less than the acceptable threshold

2 Reserved

3 Missing value

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\* DSR = Data set record

**0 25 122**

***Hardware configuration for RF\****

Code figure

0 Hardware configuration for RF is A

1 Hardware configuration for RF is B

2 Reserved

3 Missing value

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\* RF = Radio frequency

**0 25 123**

***Hardware configuration for HPA\****

Code figure

0 Hardware configuration for HPA is A

1 Hardware configuration for HPA is B

2 Reserved

3 Missing value

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\* HPA = High power amplifier

**0 25 124**

***MWR\*-L2-processing flag***

Code figure

0 Percentage of DSRs\*\* free of processing errors during Level 2 processing is greater than the acceptable threshold

1 Percentage of DSRs\*\* free of processing errors during Level 2 processing is less than the acceptable threshold

2 Reserved

3 Missing value

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\* MWR = Microwave radiometer

\*\* DSR = Data set record

**0 25 150**

***Method of tropical cyclone intensity analysis using satellite data***

Code figure

1 The Dvorak's VIS (VISual imagery) intensity analysis

2 The Dvorak's EIR (Enhanced InfraRed imagery) intensity analysis

3--14 Reserved

15 Missing value

**0 25 174**

***SMOS information flag***

Bit No. Meaning

1 Pixel is affected by RFI effects

2 Pixel is located in the hexagonal alias direction centred on Sun alias

3 Pixel is close to the border delimiting the extended alias free zone

4 Pixel is inside the extended alias free zone

5 Pixel is inside the exclusive of alias free zone

6 Pixel is located in a zone where a oon alias was reconstructed

7 Pixel is located in a zone where Sun reflection has been detected

8 Pixel is located in a zone where Sun alias was reconstructed

9 Flat target transformation has been performed during image reconstruction of this pixel

10 Scene has been combined with an adjustment scene in opposite polarization during image reconstruction to account for cross-polarization leakage

11 Direct Moon correction has been performed during image reconstruction of this pixel

12 Reflected Sun correction has been performed during image reconstruction of this pixel

13 Direct Sun correction has been performed during image reconstruction of this image

All 14 Missing value

**\
**

**0 25 181**

***L2 processing flag***

Code figure Meaning

0 OK

1 Percentage of L2b records free of processing errors is less than acceptable threshold

2 Missing value

**0 25 182**

***L1 processing flag***

Code figure Meaning

0 OK

1 Percentage of L1b records free of processing errors is less than acceptable threshold

2 Missing value

**0 25 184**

***L2 product status***

Code figure Meaning

0 OK

1 Product as a duration shorter than the input product

2 Missing value

**0 25 185**

***Encryption method***

Code figure Meaning

0 AES 256

1--254 Reserved

255 Missing value

**0 25 187**

***Confidence flag***

Code figure

0 Valid

1 Invalid

2--14 Reserved

15 Missing value

**\
**

**0 25 188**

***Method for reducing pressure report to sea level***

Code figure

0 Pressure adjusted to mean sea level following WMO-No. 8\* for low level (\< 50 m) stations

1 Pressure adjusted to mean sea level following WMO-No. 8 for stations below 750 m

2 Pressure adjusted to sea level following national practice

3 Pressure adjusted to local water level following national practice

4 Pressure not corrected for height

5--14 Reserved

15 Missing value

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\* *Guide to Meteorological Instruments and Methods of Observation*

**0 25 190**

***Altimeter echo processing mode***

Code figure

0 Low resolution mode (LRM)

1 Synthetic aperture radar (SAR)

2 LRM and SAR (interleaved)

3 Reserved

4 Pseudo-LRM (PLRM)

5 SAR interferometric mode (SARin)

6--254 Reserved

255 Missing value

**0 25 191**

***Altimeter tracking mode***

Code figure

0 Open loop

1 Closed loop

2 Open loop fixed gain

3--254 Reserved

255 Missing value

**0 26 010**

***Hours included***

Bit No.

1 0100 included

2 0200 included

3 0300 included

4 0400 included

5 0500 included

6 0600 included

7 0700 included

8 0800 included

9 0900 included

10 1000 included

11 1100 included

12 1200 included

13 1300 included

14 1400 included

15 1500 included

16 1600 included

17 1700 included

18 1800 included

19 1900 included

20 2000 included

21 2100 included

22 2200 included

23 2300 included

24 2400 included

25 Unknown mixture of hours

All 26 Missing value

**0 29 001**

***Projection type***

Code figure

0 Gnomonic projection

1 Polar stereographic projection

2 Lambert's conformal conic projection

3 Mercator's projection

4 Scanning Cone (radar)\*

5 Reserved

6 No projection

7 Missing value

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\* Projection type 4 indicates a Cartesian grid placed directly on the scanning cone defined by the azimuthal sweep of the radar.

**0 29 002**

***Coordinate grid type***

Code figure

0 Cartesian

1 Polar

2 Other

3--6 Reserved

7 Missing value

**0 30 031**

***Picture type***

Code figure

0 PPI

1 Composite

2 CAPPl

3 Vertical section

4 Alphanumeric data

5 Map of subject clutter

6 Map

7 Test picture

8 Comments

9 Map of ground occultation

10 Map of radar beam height

11--13 Reserved

14 Other

15 Missing value

**0 30 032**

***Combination with other data***

Bit No.

1 Map

2 Satellite IR

3 Satellite VIS

4 Satellite WV

5 Satellite multispectral

6 Synoptic observations

7 Forecast parameters

8 Lightning data

9--14 Reserved

15 Other data

All 16 Missing value

**0 31 021**

***Associated field significance***

Code figure

0 Reserved

1 1-bit indicator of quality 0 = good

1 = suspect or bad

2 2-bit indicator of quality 0 = good

1 = slightly suspect

2 = highly suspect

3 = bad

3--5 Reserved

6 4-bit indicator of quality control class 0 = Unqualified

according to GTSPP 1 = Correct value (all checks passed)

2 = Probably good but value\
inconsistent with statistics\
(differ from climatology)

3 = Probably bad (spike, gradient, \...\
if other tests passed)

4 = Bad value, impossible value (out\
of scale, vertical instability,\
constant profile)

5 = Value modified during quality control

6--7 = Not used (reserved)

8 = Interpolated value

9 = Missing value

7 Percentage confidence

8 0 = Not suspected

1 = Suspected

2 = Reserved

3 = Information not required

9 Status of ancillary data 0 = Data present, good, collocated

1 = Data available but of degraded\
quality and not used

2 = No spatiotemporally collocated\
data available

3--14 = Not used (reserved)

15 = Missing value

10--20 Reserved

21 1-bit indicator of correction 0 = original value

(see Note 2) 1 = substituted/corrected value

22--62 Reserved for local use

63 Missing value

Notes:

\(1) Associated field significance shall be used initially in conjunction with the quality of observed data.

\(2) The code figure 21 may be used within corrected messages with the substituted/corrected values identified.

\(3) Further applications may be developed.

**0 31 031**

***Data present indicator***

Bit No. Value

1 0 Data present

1 Data not present

**0 33 002**

***Quality information***

Code figure

0 Data not suspect

1 Data suspect

2 Reserved

3 Quality information not given

**0 33 003**

***Quality information***

Code figure

0 Data not suspect

1 Data slightly suspect

2 Data highly suspect

3 Data considered unfit for use

4--6 Reserved

7 Quality information not given

**0 33 005**

***Quality information (AWS data)***

Bit No.

1 No automated meteorological data checks performed

2 Pressure data suspect

3 Wind data suspect

4 Air temperature data suspect

5 Wet-bulb temperature data suspect

6 Humidity data suspect

7 Ground temperature data suspect

8 Soil temperature (depth 1) data suspect

9 Soil temperature (depth 2) data suspect

10 Soil temperature (depth 3) data suspect

11 Soil temperature (depth 4) data suspect

12 Soil temperature (depth 5) data suspect

13 Cloud data suspect

14 Visibility data suspect

15 Present weather data suspect

16 Lightning data suspect

17 Ice deposit data suspect

18 Precipitation data suspect

19 State of ground data suspect

20 Snow data suspect

21 Water content data suspect

22 Evaporation/evapotranspiration data suspect

23 Sunshine data suspect

24--29 Reserved

All 30 Missing value

**0 33 006**

***Internal measurement status information (AWS)***

Code figure

0 Self-check OK

1 At least one warning active, no alarms

2 At least one alarm active

3 Sensor failure

4--6 Reserved

7 Missing value

**0 33 015**

***Data quality-check indicator***

Code figure

0 Passed all checks

1 Missing data check

2 Descending/reascending balloon check

3 Data plausibility check (above limits)

4 Data plausibility check (below limits)

5 Superadiabatic lapse rate check

6 Limiting angles check

7 Ascension rate check

8 Excessive change from previous flight

9 Balloon overhead check

10 Wind speed check

11 Wind direction check

12 Dependency check

13 Data valid but modified

14 Data outlier check

15--62 Reserved

63 Missing value

**0 33 020**

***Quality control indication of following value***

Code figure

0 Good

1 Inconsistent

2 Doubtful

3 Wrong

4 Not checked

5 Has been changed

6 Estimated

7 Missing value

**0 33 021**

***Quality of following value***

Code figure

0 Within limits

1 Outside limits

2 Reserved

3 Missing value

**0 33 022**

***Quality of buoy satellite transmission***

Code figure

0 Good (several identical reports have been received)

1 Dubious (no identical reports have been received)

2 Reserved

3 Missing value

**0 33 023**

***Quality of buoy location***

Code figure

0 Reliable (location was made over two satellite passes)

1 Latest known (no location over the corresponding pass)

2 Dubious (location made over one pass only; a second solution is possible in 5 per cent of the cases)

3 Missing value

**0 33 024**

***Station elevation quality mark (for mobile stations)***

Code figure

0 Reserved

1 Excellent -- within 3 metres

2 Good -- within 10 metres

3 Fair -- within 20 metres

4 Poor -- more than 20 metres

5 Excellent -- within 10 feet

6 Good -- within 30 feet

7 Fair -- within 60 feet

8 Poor -- more than 60 feet

9--14 Reserved

15 Missing value

**0 33 025**

***ACARS interpolated values indicator***

Code figure

0 Time interpolated, latitude and longitude reported

1 Time reported, latitude and longitude interpolated

2 Time, latitude, and longitude interpolated

3 Time, latitude, and longitude reported

4--6 Reserved

7 Missing value

**0 33 026**

***Moisture quality***

Code figure

0 Normal operations -- measurement mode

1 Normal operations -- non-measurement mode

2 Small RH

3 Humidity element is wet

4 Humidity element contaminated

5 Heater fail

6 Heater fail and wet/contaminated humidity element

7 At least one of the input parameters used in the calculation of mixing ratio is invalid

8 Numeric error

9 Sensor not installed

10 Calculated RH \> 100%

11 Input laser power too low

12 Probe WV temperature out of range

13 Probe WV pressure out of range

14 Spectral line out of range

15 No laser output

16--62 Reserved

63 Missing value

**0 33 027**

***Location quality class (range of radius of 66% confidence)***

Code figure

0 Radius ≥ 1500 m

1 500 m ≤ Radius \<1500 m

2 250 m ≤ Radius \< 500 m

3 Radius \< 250 m

4 ≤ 100 m

5--6 Reserved

7 Missing value

**0 33 028**

***Snapshot overall quality***

Code figure

1 Nominal

2 Degraded by SW error; any error reported by the algorithms

3 Degraded by instrument error

4 Degraded by corrupted /missing ADF

5--6 Reserved

7 Missing value

**0 33 030**

***Scan line status flags for ATOVS***

Bit No.

1 Do not use scan for product generation

2 Time sequence error detected with this scan

3 Data gap precedes this scan

4 No calibration

5 No Earth location

6 First good time following a clock update

7 Instrument status changed with this scan

8--23 Reserved

All 24 Missing value

Note: If bit is set to 1 then statement is true.

**0 33 031**

***Scan line quality flags for ATOVS***

Bit No.

1 Time field is bad but can probably be inferred from the previous good time

2 Time field is bad and cannot be inferred from the previous good time

3 This record starts a sequence that is inconsistent with previous times (i.e. there is a time discontinuity). This may or may not be associated with a spacecraft clock update (see scan line status flags for ATOVS)

4 Start of a sequence that apparently repeats scan times that have been previously accepted

5 Scan line was not calibrated because of bad time

6 Scan line was calibrated using fewer than the preferred number of scan lines because of proximity to start or end of data or to a data gap

7 Scan line was not calibrated because of bad or insufficient PRT data

8 Scan line was calibrated but with marginal PRT data

9 Some uncalibrated channels on this scan

10 Uncalibrated due to instrument mode

*(continued)*

*\
(Flag table 0 33 031 -- continued)*

Bit No.

11 Questionable calibration because of antenna position error of space view

12 Questionable calibration because of antenna position error of black body

13 Not Earth located because of bad time

14 Earth location questionable because of questionable time code (see time problem code bits)

15 Earth location questionable -- only marginal agreement with reasonableness check

16 Earth location questionable -- fails reasonableness check

17 Earth location questionable because of antenna position check

18 Scan line calibration cold black body

19 Scan line calibration warm black body

20 Scan line calibration space view

21 Earth view

22--23 Reserved

All 24 Missing value

Notes:

\(1) If bit is set to 1 then statement is true.

\(2) Bits 1--4 represent time problem code. All bits off implies the scan time is as expected.

\(3) Bits 5--10 represent calibration problem code. All bits set to zero indicated normal calibration. Where any of bits 5, 7, 10 are set, secondary calibration coefficients have been used.

\(4) Bits 11--17 represent Earth location problem code. All bits set to zero implies the Earth location was normal.

**0 33 032**

***Channel quality flags for ATOVS***

Bit No.

1 No good blackbody counts for scan line

2 No good space view counts for this line

3 No good PRTs for this line

4 Some bad blackbody view counts for this line

5 Some bad space view counts for this line

6 Some bad PRT temps on this line

7 Quality for this scan is reduced

8--23 Reserved (bits set to zero)

All 24 Missing value

Note: All bits off implies a good calibration.

**0 33 033**

***Field of view quality flags for ATOVS***

Bit No.

1 Set if secondary calibration used

2--21 Bit n set to 1 if brightness temperature in channel n -- 1 is physically unreasonable or has not been calculated due to calibration problems

22 Set if all the channels are missing

23 Suspect

All 24 Missing value

Notes:

\(1) All bits off implies a good calibration.

\(2) Bits 2--21 used for HIRS, but only bits 2--16 used for AMSU-A and only bits 2--6 used for AMSU-B.

**0 33 035**

***Manual/automatic quality control***

Code figure

0 Automatic quality control passed and not manually checked

1 Automatic quality control passed and manually checked and passed

2 Automatic quality control passed and manually checked and deleted

3 Automatic quality control failed and manually not checked

4 Automatic quality control failed and manually checked and failed

5 Automatic quality control failed and manually checked and re-inserted

6 Automatic quality control flagged data as questionable and not manually checked

7 Automatic quality control flagged data as questionable and manually checked and failed

8 Manually checked and failed

9--14 Reserved

15 Missing value

**0 33 037**

***Wind correlation error***

Bit No.

1 u departure from guess

2 v departure from guess

3 u and v departure from guess

4 u acceleration

5 v acceleration

6 u and v acceleration

7 Possible land feature

8 u acceleration and possible land feature

9 v acceleration and possible land feature

10 u and v acceleration and possible land feature

*(continued)*

*\
(Flag table 0 33 037 -- continued)*

Bit No.

11 Bad wind guess

12 Correlation failure

13 Search box off edge of area

14 Target box off edge of area

15 Pixel brightness out of bounds (noisy line)

16 Target outside of latitude/longitude box

17 Target outside of pressure minimum/maximum

18 Autoeditor flagged slow vector

19 Autoeditor flagged vectors

All 20 Missing value

**0 33 038**

***Quality flags for ground-based GNSS\* data***

Bit No.

1 Total zenith delay quality is considered poor

2 GALILEO satellites used

3 GLONASS satellites used

4 GPS satellites used

5 Meteorological data applied

6 Atmospheric loading correction applied

7 Ocean tide loading applied

8 Climate quality data processing

9 Near-real time data processing

All 10 Missing value

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\* GNSS = Global Navigation Satellite Systems

**0 33 039**

***Quality flags for radio occultation data***

Bit No.

1 Non-nominal quality

2 Offline product

3 Ascending occultation flag

4 Excess phase processing non-nominal

5 Bending angle processing non-nominal

6 Refractivity processing non-nominal

7 Meteorological processing non-nominal

8--13 Reserved

14 Background profile non-nominal

15 Background (i.e. not retrieved) profile present

All 16 Missing value

**0 33 041**

***Attribute of following value***

Code figure

0 The following value is the true value

1 The following value is higher than the true value (the measurement hit the lower limit of the instrument)

2 The following value is lower than the true value (the measurement hit the higher limit of the instrument)

3 Missing value

Note: This descriptor will be associated with visibility data or height of clouds data to specify if the value is bounded. If the reported data is the true value, the code figure is 0. However, the measurement can hit the limit of the instrument measurement capability. If the reported value is higher than the true value, the code figure is 1; if the reported value is lower than the true value, the code figure is 2.

**0 33 042**

***Type of limit represented by following value***

Code figure

0 Exclusive lower limit (\>)

1 Inclusive lower limit (≥)

2 Exclusive upper limit (\<)

3 Inclusive upper limit (≤)

4--6 Reserved

7 Missing value

**0 33 043**

***AST confidence***

Bit No.

1 Sea MDS. Nadir only SST retrieval used 3.7 micron channel. Land MDS reserved

2 Sea MDS. Dual view SST retrieval used 3.7 micron channel. Land MDS reserved

3 Nadir view contains day time data

4 Forward view contains day time data

5--7 Reserved

All 8 Missing value

**0 33 044**

***ASAR quality information***

Bit No.

1 Input data mean outside nominal range flag

2 Input data standard deviation outside nominal range flag

3 Number of input data gaps \> threshold value

4 Percentage of missing lines \> threshold value

*(continued)*

*\
(Flag table 0 33 044 -- continued)*

Bit No.

5 Doppler centroid uncertain. Confidence measure \< specific value

6 Doppler ambiguity estimate uncertain. Confidence measure \< specific value

7 Output data mean outside nominal range flag

8 Output data standard deviation outside nominal range flag

9 Chirp reconstruction failed or is of low quality flag

10 Data set missing

11 Invalid downlink parameters

12 Azimuth cut-off iteration count. The azimuth cut-off fit did not converge within a minimum number of iterations

13 Azimuth cut-off fit did not converge within a minimum number of iterations

14 Phase information confidence measure. The imaginary spectral peak is less than a minimum threshold, or the zero lag shift is greater than a minimum threshold

All 15 Missing value

**0 33 047**

***Measurement confidence data***

Bit No.

1 Error detected and attempts to recover made

2 Anomaly in on-board data handling (OBDH) value detected

3 Anomaly in ultra-stable oscillator processing (USOP) value detected

4 Errors detected by on-board computer

5 Automatic gain control (AGC) out of range

6 Reception (Rx) delay fault. Rx distance out of range

7 Wave form samples fault identifier. Error

8 S band anomaly/error detected

9--11 Reserved

12 Brightness temperature (channel 1) out of range

13 Brightness temperature (channel 2) out of range

14 Reserved

15 Ku band ocean retracking error

16 S band ocean retracking error

17 Ku band ice 1 retracking error

18 S band ice 1 retracking error

19 Ku band ice 2 retracking error

20 S band ice 2 retracking error

21 Ku band sea ice retracking error

22 Arithmetic fault error

23 Meteo data state. No map

24 Meteo data state. 1 map

25 Meteo data state. 2 maps degraded

26 Meteo data state. 2 maps nominal

27 Orbit propagator status for propagation mode, several errors

28 Orbit propagator status for propagation mode, warning detected

29 Orbit propagator status for initialization mode, several errors

30 Orbit propagator status for initialization mode, warning detected

All 31 Missing value

**0 33 048**

***Confidence measure of SAR\* inversion***

Code figure

0 Inversion successful

1 Inversion not successful

2 Reserved

3 Missing value

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\* SAR = Synthetic aperture radar

**0 33 049**

***Confidence measure of wind retrieval***

Code figure

0 External wind direction used during inversion

1 External wind direction not used during inversion

2 Reserved

3 Missing value

**0 33 050**

***Global GTSPP quality flag***

Code figure

0 Unqualified

1 Correct value (all checks passed)

2 Probably good but value inconsistent with statistics (differ from climatology)

3 Probably bad (spike, gradient, etc., if other tests passed)

4 Bad value, impossible value (out of scale, vertical instability, constant profile)

5 Value modified during quality control

6--7 Reserved

8 Interpolated value

9 Good for operational use; caution; check literature for other uses

10--14 Reserved

15 Missing value

**0 33 052**

***S band ocean retracking quality***

Bit No.

1--20 First 20 least significant bits correspond to the 20 values (one per data block containing:\
0 = valid measurement, 1 = invalid). Bit 1 applies to the 20th data block

All 21 Missing value

**0 33 053**

***Ku band ocean retracking quality***

Bit No.

1--20 First 20 least significant bits correspond to the 20 values (one per data block containing:\
0 = valid measurement, 1 = invalid). Bit 1 applies to the 20th data block

All 21 Missing value

**0 33 060**

***GqisFlagQual -- individual IASI-System quality flag***

Code figure

0 Good

1 Bad

2 Reserved

3 Missing value

**0 33 066**

***AMV\* quality flag***

Bit No.

1--21 Reserved

22 Correlation surface constraint fails

23 Reserved

All 24 Missing value

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\* Atmospheric motion vectors

**0 33 070**

***Total ozone quality***

Code figure

0 Good retrieval

1 Bad aerosol information flag or NOAA-16 radiance anomaly

2 Solar zenith angle greater than 84 degrees

3 380 nm residue greater than limit

4 Ozone inconsistency

5 Difference between profile ozone and step 3 total ozone exceeds threshold (set to 25 DU)

6 Step 1 ozone iteration did not converge

7 Any channel residue greater than 16 or bad radiance

8 Insufficient pixels -- not processed

9 First guess good -- ozone forecast data used

10 High cloud in pixel -- not processed

11 Successful ozone retrieval

12 Unsuccessful ozone retrieval

13--14 Reserved

15 Missing value

**0 33 071**

***Profile ozone quality***

Code figure

0 Good retrieval

1 Solar zenith angle greater than 84 degrees

2 Difference between step 3 and profile total ozone greater than limit (25 DU)

3 Average final residue for wavelengths used in retrieval greater than threshold

4 Final residue greater than 3 times a priori error

5 Difference between retrieved and a priori greater than 3 times a priori error

6 Non-convergent solution

7 Upper level profile anomaly or stray light anomaly

8 Initial residue greater than 18.0 N-value units

9--14 Reserved

15 Missing value

**0 33 072**

***Ozone error***

Code figure

0 Good retrieval

1 Reflectivity out of range

2 Larger pixels (Number of cross-track pixels less than 32) or backward scans error

3 Solar zenith angle greater than 88 degrees

4 Latitude/longitude out of range

5 Viewing zenith angle or solar zenith angle out of range

6 Step-one process failed in general

7 First guess ozone out of range

8 Too many iterations (exceed 8)

9 Step-one residue calculation failed

10 Step-two process failed in general

11 First guess ozone profile out of range

12 Step-two ozone value out of range

13 Step-two residue calculation failed

14 Step-three process failed in general

15 Polarization correction accuracy alert

16 Radiance or irradiance less or equal to zero

17--30 Reserved

31 Missing value

**\
**

**0 33 075**

***Scan-level quality flags***

Bit No.

1 Gap in raw data record (RDR) data detected (i.e., missing scan(s) preceding the current scan)

2 Recorded time is not in sequence (i.e., the scan start time is out of sequence)

3 Lambda monitored calculation cannot be updated (see Note 1)

4 The measured temperatures of any instrument components (e.g., beam-splitter, scan mirror, scan baffle) are outside the allowable ranges (see Note 2)

5 At least one of the monitored instrument temperatures has drifted more than\
a specified tolerance value

6--12 Reserved

All 13 Missing value

Notes:

\(1) Set to 1 if laser wavelength calculation is invalid due to laser diode bias current and/or laser diode temperature measurements being outside the predetermined allowable ranges. These ranges are tunable. In this case Lambda monitored calculation shall have 1 bit per scan.

\(2) These temperatures are used to compute the "environmental" contribution to the internal calibration target (ICT) radiances. When this bit is set to 1, the invalid temperatures shall be replaced with the validated temperature values of the ICT.

**0 33 076**

***Calibration quality flags***

Bit No.

1 Lunar intrusion on first deep space view (see Note)

2 Lunar intrusion on second deep space view (see Note)

3--8 Reserved

All 9 Missing value

Note: Set to 1 if at least one spectrum in the deep space moving average was invalidated due to a lunar intrusion.

**0 33 077**

***Field-of-view quality flags***

Bit No.

1 Degraded SDR\* quality

2 Invalid SDR\* quality (see Note 1)

3 Invalid SDR\* geolocation information

4 Degraded radiometric calibration

5 Invalid radiometric calibration (see Note 2)

6 Degraded spectral calibration

7 Invalid spectral calibration (see Note 3)

8 Fringe count error detected and corrected (see Note 4)

9 Day/night indicator (see Note 5)

10 Invalid RDR\*\* data (see Note 6)

11 Significant fringe count error detected (see Note 7)

12 Bit trim failed

13--18 Reserved

All 19 Missing value

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\* SDR = Sensor data record

\*\* RDR = Raw data record

Notes:

\(1) SDR quality is invalid if bit trim failed (see bit 12), or fringe count error detected (see bit 11), or invalid raw data record (RDR) data (see bit 10), or invalid radiometric calibration (see bit 5), or invalid spectral calibration (see bit 7).

\(2) Radiometric calibration is invalid if radiometric calibration is not performed, or if it is performed with invalid calibration data (e.g., deep space window size = 0).

\(3) Spectral calibration is invalid if fringe count error detected and corrected (see bit 8), or if neon calibration is suspect and Lambda monitored calculation cannot be updated (see "Scan-level quality flags" (0 33 075) -- bit 3).

\(4) Set to 0 if no fringe count error was detected (see bit 11), or a fringe count error was detected but it was not corrected.

\(5) Set to 0 if day (solar zenith angle \< 90°). Set to 1 if night (solar zenith angle ≥ 90°).

\(6) This flag indicates the instrument exhibited operational errors and the associated interferogram(s) is/are excluded from SDR processing.

\(7) This flag indicates that a significant number of fringes have been missed, shifting the interferogram ZPD outside of a window monitored by the instrument, and the interferogram is excluded from SDR processing.

**0 33 078**

***Geolocation quality***

Code figure

0 Nominal -- altitude and ephemeris data available

1 Missing at most a small gap of altitude and ephemeris data

2 Missing more than a small gap of altitude and ephemeris data, but no more than a\
granule boundary

3 Missing more than a granule boundary of altitude and ephemeris data

4--14 Reserved

15 Missing value

**0 33 079**

***Granule level quality flags***

Bit No.

1--5 Reserved

6 The No. 1--No.7 health checks failed

7 The No. 8--No.15 health checks failed

8 The No. 16--No.23 health checks failed

9 The No. 24--No.31 health checks failed

10 The No. 32--No.39 health checks failed

11 The No. 40--No.47 health checks failed

12 The No. 48--No.55 health checks failed

13 The No. 56--No.63 health checks failed

14 The No. 64--No.70 health checks failed

15 Quadratic correction applied to the radiometric transfer function for non-linearity\
correction

All 16 Missing value

**0 33 080**

***Scan level quality flags***

Bit No.

1--6 Reserved

7 Divide-by-zero condition or computation loop failed to converge in the K/Ka and V\
(KAV) band PRT \*

8 Divide-by-zero condition or computation loop failed to converge in the WG band PRT

9 Divide-by-zero condition or computation loop failed to converge in the K/Ka, V, W, G\
band receiver shelf PRT K temperature computation

10 Out of range condition for the K/Ka and V band PRT

11 Out of range condition for the WG band PRT

12 KAV PRT temperature inconsistency

13 WG PRT temperature inconsistency

14 Time sequence error

15 Data gap -- missing scan(s) preceding the current scan

16 KAV PRT sufficiency -- insufficient KAV PRT data are available

17 WG PRT sufficiency -- insufficient WG PRT data are available

18 Space view antenna position error

19 Blackbody antenna position error

All 20 Missing value

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\* PRT = Platinum Resistance Temperature

**0 33 081**

***Channel data quality flags***

Bit No.

1--2 Reserved

3 Moon in space view

4 Gain error -- the lowest blackbody count is smaller than or equal to the highest space\
view count in a scan

5 Calibration with fewer than preferred samples

6 Space view data sufficiency check -- insufficient space view samples are available

7 Blackbody view data sufficiency check -- insufficient blackbody view samples are available

8 Out of range condition for the space view

9 Out of range condition for the blackbody view

10 Space view inconsistency

11 Blackbody view inconsistency

All 12 Missing value

**0 33 082**

***Geolocation quality flags***

Bit No.

1--5 Reserved

6 Within South Atlantic anomaly

7 Invalid input data (indicates that any of the spacecraft ephemeris or attitude data are

invalid)

8 Bad pointing (indicates that the sensor LOS does not intersect the geoid, is near the

limb, has invalid sensor angles or other similar condition)

9 Bad terrain (indicates that the algorithm could not obtain a valid terrain value)

10 Invalid solar angles

11 Missing at most a small gap of altitude and ephemeris data

12 Missing more than a small gap of altitude and ephemeris data, but no more than a

granule boundary

13 Missing more than a granule boundary of altitude and ephemeris data

14 The number of encoder pulse values per delta time is not as expected

15 Solar eclipse during Earth view scan

All 16 Missing value

**\
**

**0 33 083**

***Radiance data quality flags***

Bit No.

1--5 Reserved

6 Pixel is affected by radio-frequency interference

7 Poor calibration quality due to bad space view offsets, OBC\* view offsets, etc. or use of a previous calibration view

8 Saturated pixel

9 Missing data --data required for calibration processing are not available for processing

10 Calibrated pixel radiance out of range

11 Calibrated pixel reflectance or EBBT out of range

12 The moon has corrupted the space view

13 Scan data is not present (no valid data)

14 Quality for this scan-line is reduced. The value is determined by the combined number of steps required to find a replacement for thermistor or calibration source data

15 Bad detector

All 16 Missing value

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\* OBC = on-board calibration

**0 33 084**

***Pixel level quality flags***

Bit No.

1--5 Reserved

6 Bulk SST outside of validation range

7 Skin SST outside of validation range

8 Sensor zenith angle \> 40 degrees (pixel is not within 40 degrees of nadir and therefore is not of high quality)

9 Degradation -- horizontal cell size (HCS) \> 1.3 km (HCS \> 1.3 km, swath width \> 1 700 km, sensor zenith angle \> 50.3 degrees)

10 Exclusion: no ocean in pixel

11 Degradation: aerosol optical thickness (AOT) \> 0.6 (AOT in horizontal cell \> 0.6 on the slant path (AOT \@550 nm))

12 Exclusion: AOT \> 1.0 (AOT in horizontal cell \> 1.0 on the slant path (AOT \@550 nm))

13 Sun glint present in pixel

14 Ice concentration threshold exceeded (SST not retrieved due to ice concentration exceeding threshold in system spec)

15 Thin cirrus detected in pixel

All 16 Missing value

**\
**

**0 33 085**

***Aerosol optical thickness quality flags***

Bit No.

1--3 Reserved

4 Angstrom exponent is outside of the system specification range

5 Excluded, Angstrom exponent for AOT\* at 550 nm \< 0.15

6 Bright surface in cell (if over land), or shallow or turbid water in cell (if over ocean)

7 Low sun, excluded, Solar Zenith Angle \> 80 degrees

8 Low sun, degraded, 65 degrees \< Solar Zenith Angle ≤ 80 degrees

9 Fire detected in cell

10 Snow/Ice in cell

11 Cloud shadow in cell

12 Sun glint in cell

13 Bad SDR\*\* data present in horizontal cell (quality of AOT/APSP\*\*\* degraded or AOT/APSP not retrieved due to bad SDR data in horizontal cell)

14 Cirrus contamination in cell

15 Cloud adjacent to cell

16 Cloud contamination in cell

17 AOT is outside of the system specification range

All 18 Missing value

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\* AOT = Aerosol optical thickness

\*\* SDR = Sensor data record

\*\*\* APSP = Aerosol particle size parameter

**0 33 086**

***Quality of pixel level retrieval***

Code figure

0 Not retrieved

1 Excluded

2 Degraded

3 High quality

4--6 Reserved

7 Missing value

**\
**

**0 33 087**

***Extent of satellite within South Atlantic anomaly (based on climatological data)***

Code figure

0 Less than or equal to 10%

1 Greater than 10% but less than or equal to 20%

2 Greater than 20% but less than or equal to 30%

3 Greater than 30% but less than or equal to 40%

4 Greater than 40% but less than or equal to 50%

5 Greater than 50% but less than or equal to 60%

6 Greater than 60% but less than or equal to 70%

7 Greater than 70% but less than or equal to 80%

8 Greater than 80%

9--14 Reserved

15 Missing value

**0 33 088**

***Ozone total column quality flag***

Bit No.

1--5 Reserved

6 Surface reflectivity out of range

7 Residual too large

8 Aerosol index limit exceeded

9 Solar eclipse present (all or part of the IFOV\* is affected by a solar eclipse, umbra or penumbra viewing)

10 Sun glint present within IFOV

11 Snow or ice surface is within the IFOV

12 Solar zenith angle in excluded (night) condition (solar zenith angle ≥ 88 degrees)

13 Solar zenith angle in degraded condition (80 degrees ≤ solar zenith angle \< 88 degrees)

14 SO~2~ index \> 6 DU (degraded condition)

15 Residues are not consistent (indicates whether the residues from the 22 wavelengths are consistent)

16 O~3~ triplet selection is not consistent within retrieval (ozone triplet consistency)

17 Input data quality is not good

All 18 Missing value

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\* IFOV = Instantaneous field of view

**0 33 092**

***Band-specific ocean quality flag***

Bit No.

1 Altimeter operating

2 Microwave radiometer (MWR) operating

3--8 Reserved

All 9 Missing value

**0 35 000**

***FM and Regional Code number***

Code figure

000--099 International FM Codes

100--199 RA I Codes

200--299 RA II Codes

300--399 RA III Codes

400--499 RA IV Codes

500--599 RA V Codes

600--699 RA VI Codes

700--799 Antarctic Codes

800--999 Reserved

1000--1022 Not used

1023 Missing value

**0 35 001**

***Time frame for monitoring***

Code figure

0 Real time

1 Near-real time

2 Non-real time

3--6 Reserved

7 Missing value

**0 35 030**

***Discrepancies in the availability of expected data***

Code figure

0 No discrepancies

1 Non-compliance with standard and recommended practices and procedures including those of monitoring

2 Catalogues of meteorological bulletins not updated in a timely manner

3 Incorrect routing directories

4 Lack of flexibility in the routing arrangements

5 Deficiencies in the operation of GTS centres and circuits

6 Loss of data or delays in relaying data on the GTS

7 Routing of data different from the routing provided in the plan

8 Various malpractices

9--14 Reserved

15 Missing value

**0 35 031**

***Qualifier on monitoring results***

Code figure

1 Sufficient and all of acceptable quality

2 Sufficient but partly of acceptable quality

3 Insufficient but all of acceptable quality

4 Insufficient and of unacceptable quality

5 Some messages not complete

6 Suspect or wrongly coded groups could not be interpreted confidently

7 Gross coding errors

8 Transmission sequential order not observed

9 Report completely garbled and thus discarded

10 Deficiencies identified and rectified

11 Deficiencies identified but not rectified

12 Deficiencies not identified

13 Measuring errors

14 Mutual inconsistency

15 Temporal inconsistency

16 Forecast error

17 Bias

18 Improve system of quality control

19 Expand training programmes

20--98 Reserved

99--126 Not used

127 Missing value

**0 35 032**

***Cause of missing data***

Code figure

1 Data groups missing due to radio fading

2 Data groups missing due to outage of centre

3 Data groups missing due to outage of circuit

4 Non-implementation or maintenance of required RBSN density

5 Shortage of qualified staff to man stations

6 Lack of consumables

7 Instrument failure

8 Non-adherence to telecommunication procedures

9 Some observing programmes ceased

10--14 Not used

15 Missing value

**0 35 033**

***Observation and collection deficiencies***

Code figure

1 No deficiency

2 Observations not made regularly

3 Observations not made at right time

4 Observations made but not disseminated

5 Observations made and sent to incorrect users

6 Collection not received

7 Collection transmitted late

8 Collection not transmitted

9 Difficulties in HF propagation and selection of suitable frequency

10 Difficulties in maintenance of communication equipment at remote stations

11 No alternative arrangement for routing meteorological observation

12--99 Reserved

100--122 Not used

123 Missing value

**0 35 034**

***Statistical trends for availability of data (during the survey period(s))***

Code figure

1 Slight improvement

2 Significant improvement

3 Most significant improvement

4 Steady

5 Decreasing

6 Efforts required to improve night-time observations

7 Missing value

**0 35 035**

***Reason for termination***

Code figure

0 Reserved

1 Balloon burst

2 Balloon forced down by icing

3 Leaking or floating balloon

*(continued)*

*\
(Code table 0 35 035 -- continued)*

Code figure

4 Weak or fading signal

5 Battery failure

6 Ground equipment failure

7 Signal interference

8 Radiosonde failure

9 Excessive missing data frames

10 Reserved

11 Excessive missing temperature

12 Excessive missing pressure

13 User terminated

14 Sudden loss of signal

15 Tracking lost

16 Increasing pressure

17 Invalid and/or missed data time limits exceeded

18--29 Reserved

30 Other

31 Missing value

**0 40 005**

***Soil moisture correction flag***

Bit No.

1 Soil moisture between --20% and 0%

2 Soil moisture between 100% and 120%

3 Correction of wet backscatter reference

4 Correction of dry backscatter reference

5 Correction of volume scattering in sand

6--7 Reserved

All 8 Missing value

Note: The nominal range for the surface soil moisture is 0% -- 100%. In extreme cases, the extrapolated backscatter at 40 degrees incidence angle may exceed the dry or the wet backscatter reference. In these cases, the value provided by the measurement process of surface soil moisture is, respectively, less than 0% or more than 100%.

**0 40 006**

***Soil moisture processing flag***

Bit No.

1 Not soil

2 Sensitivity to soil moisture below limit

3 Azimuthal noise above limit

4 Backscatter Fore-Aft beam out of range

5 Slope Mid-Fore beam out of range

6 Slope Mid-Aft beam out of range

7 Soil moisture below --20%

8 Soil moisture above 120%

9--15 Reserved

All 16 Missing value

Note: See Note under Flag table 0 40 005.

**0 40 011**

***Interpolation flag***

Bit No.

1 Mean sea-surface (MSS) interpolation flag

2 Ocean tide solution 1 interpolation flag (0 = 4 points over ocean, 1 = less than 4 points)

3 Ocean tide solution 2 interpolation flag (0 = 4 points over ocean, 1 = less than 4 points)

4 Meteorological data interpolation flag (0 = 4 points over ocean, 1 = less than 4 points)

5--7 Reserved

All 8 Missing value

**0 40 012**

***Radiometer data quality flag***

Bit No. (0 is good, 1 is bad)

1 18.7 GHz brightness temperature

2 23.8 GHz brightness temperature

3 34 GHz brightness temperature

4--7 Reserved

All 8 Missing value

**0 40 013**

***Radiometer brightness temperature interpretation flag***

Code figure

0 Interpolation with no gap between JMR\* data

1 Interpolation with gaps between JMR\* data

2 Extrapolation of JMR\* data

3 Failure of extrapolation and interpolation

4--6 Reserved

7 Missing value

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\* JMR = JASON-1 Microwave Radiometer

**0 40 020**

***GqisFlagQualDetailed -- quality flag for the system***

Bit No.

1 NZPD and complex calibration error

2 Band 3 affected by spike

3 Band 3 affected by saturation

4 Band 2 affected by spike

5 Band 1 affected by spike

6 Overflow/under flow

7 On-board processing error

8 Spectral calibration error

9 Radiometric calibration error

10 Missing AVHRR data

11 Missing IIS data

12 Missing sounder data

13 GqisFlagQual summary flag for all bands

14 On-ground processing error

15 Inter-calibration error IASI/AVHRR

16 Spare

All 17 Missing value

**0 40 023**

***Auxiliary altimeter state flags***

Bit No.

1 Band sequence (0 = 3Ku\_1C\_3Ku, 1 = 2Ku\_1C\_2Ku)

2 C band frequency (0 = 320 MHz, 1 = 100 MHz)

3 C band status (0 = On, 1 = Off)

4 Ku band status (0 = On, 1 = Off)

All 5 Missing value

**0 40 024**

***Meteorological map availability***

Code figure

0 2 maps available (6 hours apart)

1 2 maps available (\> 6 hours apart)

2 1 map available; data extrapolated

3 No maps used

4--6 Reserved

7 Missing value

**0 40 025**

***Interpolation flag for mean diurnal tide***

Code figure

0 Good

1 Bad

2 Reserved

3 Missing value

**0 40 028**

***GMI quality flag***

Code figure

0 Good data

1 Possible sun glint

2 Possible radio-frequency interference

3 Degraded geolocation data

4 Data corrected for warm load intrusion

5 Scan blanking on

6 Data is missing from file or unreadable

7 Unphysical brightness temperature

8 Error in geolocation data

9 Data missing in one channel

10 Data missing in multiple channels

*(continued)*

*\
(Code table 0 40 028 -- continued)*

Code figure

11 Lat/lon values are out of range

12 Non-normal status modes

13 Distance to corresponding low frequency pixel \> 7 km

14 Reserved

15 Missing value (no quality information available)

**0 40 036**

***Lidar L2b classification type***

Code figure

0 Clear

1 Cloud

2--14 Reserved

15 Missing value

**0 40 043**

***Satellite manoeuvre indicator***

Code figure

0 The platform is not undergoing a manoeuvre

1 The platform is undergoing a manoeuvre, nominal processing

2 The platform is undergoing a manoeuvre, no processing

3--6 Reserved

7 Missing value

**0 40 045**

***Cloud formation and height assignment***

Bit No.

1 Cloud products retrieved with the chi-squared method

2 Cloud products retrieved with the CO~2~-slicing

3 Height assignment performed with statistical first guess retrieval

4 Height assignment performed with NWP forecasts

All 5 Missing value

**\
**

**0 40 046**

***Cloudiness summary***

Code figure

0 The IASI IFOV is clear

1 Small cloud contamination possible

2 The IASI IFOV is partially covered by clouds

3 High or full cloud coverage

4--6 Reserved

7 Missing value

**0 40 047**

***Validation flag for IASI or IASI-NG level 1 product***

Code figure

0 The measurements and side information are available and of good quality for L2 processing

1 The L1c products are of degraded quality according to L1c flags, no L2 processing

2 Quality control indicates that the L1c data are of degraded quality (not indicated by the IASI L1c flags), no L2 processing

3--6 Reserved

7 Missing value

**0 40 048**

***Validation flag of AMSU-A level 1 data flow***

Code figure

0 The expected AMSU measurements are available, of good quality and collocated with IASI for processing

1 AMSU-A data are available but of degraded quality (according to AMSU L1 flags or QC tests) and not used for processing

2 No coincident (time and space) AMSU measurements available for processing

3--6 Reserved

7 Missing value

**\
**

**0 40 049**

***Cloud tests executed and results***

Bit No.

1--3 Reserved

4 IASI cloud optical thickness indicates a cloud

5 IASI cloud optical thickness computed

6 AVHRR heterogeneity test indicates a cloud

7 AVHRR heterogeneity test executed

8 IASI-AVHRR ANN cloud test indicates a cloud

9 IASI-AVHRR ANN cloud test executed

10 AVHRR integrated cloud fraction indicates a cloud

11 AVHRR integrated cloud fraction assessed

12 AMSU cloud test indicates a cloud

13 AMSU cloud test executed

14 IASI Window cloud test indicates a cloud

15 IASI Window cloud test executed

All 16 Missing value

**0 40 050**

***Retrieval initialization***

Bit No.

1--4 Reserved

5 MHS included

6 AMSU included

7 IASI included

All 8 Missing value

**0 40 051**

***Convergence of the iterative retrieval***

Code figure

0 **Optimal estimation methods** (OEM) not attempted

1 OEM aborted because first guess residuals too high

2 The minimization did not converge, sounding rejected

3 The minimization did not converge, sounding accepted

4 The minimization converged but sounding rejected

5 The minimization converged, sounding accepted

6 Reserved

7 Missing value

**\
**

**0 40 052**

***Indication of super-adiabatic and super-saturation in final retrieval***

Bit No.

1--3 Reserved

4 Supersaturation conditions in the OEM retrieval

5 Superadiabatic conditions in the OEM retrieval

6 Supersaturation conditions in the first guess

7 Superadiabatic conditions in the first guess

All 8 Missing value

**0 40 054**

***Potential processing and inputs errors***

Bit No.

1 An error has been detected

2 Message from L1

3 Message from L2

4 Message from ancillary data

5 Message from fitting procedure

6 File opening

7 File reading

8 Quality flag

9 Level 2 \"from linear regression\"(F\_Qual), report a pixel where L2 are not fully trusted

10 Empty field or data

11 Missing surface pressure value

12 Radiance filtering

All 13 Missing value

**0 40 055**

***Diagnostics on the retrieval***

Bit No.

1 Radiance filtering

2 Polar regions

3 Location in the night

4 Negative altitude surface below mean sea level

5 Cloud covered scene

6 Scene above the sea

7 Scene above desert

8 Skin temperature

9 Skin temperature differential

10 Spectral line contrast too weak

11 Maximum number of iterations exceeded

*(continued)*

*\
(Flag table 0 40 055 -- continued)*

Bit No.

12 Negative partial columns

13 Matrix ill conditioned

14 Fit diverged

15 Error in **GNU scientific library** (GSL) usage

16 Residuals "biased"

17 Residuals "sloped"

18 Residuals root mean square (RMS) error is large

19 Weird averaging kernels

20 Ice presence detected

All 21 Missing value

**0 40 056**

***General retrieval quality***

Code figure

0 Use not recommended

1 Use with caution

2 Best quality

3--6 Reserved

7 Missing value

**0 40 057**

***IASI level 2 retrieval flags***

Bit No.

1 An error has been detected

2 Message from L1

3 Message from L2

4 Message from ancillary data

5 Message from fitting procedure

6 Reserved

7 Bad L1 or L2 flag raised

8 Level 2 not fully trusted

9 Missing temperature or humidity levels in the vertical profile

10 Missing surface pressure value

11 Radiance filtering

12 Polar regions

13 Location in the night

14 Negative altitude

15 Cloud covered scene

16 Scene above the sea

17 Scene above desert

18 Missing skin temperature

*(continued)*

*\
(Flag table 0 40 057 -- continued)*

Bit No.

19 Retrieved skin temperature too different from model

20 Spectral line contrast too weak

21 Maximum number of iterations exceeds

22 Negative partial columns

23 Matrix ill conditioned

24 Fit diverged

25 Error in GSL usage

26 Residuals biased

27 Residuals sloped

28 Residuals RMS error is large

29 Weird averaging kernels

30 Ice presence detected

All 31 Missing value

**0 40 068**

***General retrieval quality flag for SO~2~***

Code figure

0 Values calculated with IASI L2

1 Pressure and temperature profiles missing in IASI L2 data; model/forecast data\
used instead

2 Best quality

3--14 Reserved

15 Missing value

**0 42 004**

***Confidence of inversion for each partition of swell wave spectra***

Code figure

0 Wave direction resolved

1 180-degree ambiguity not resolved

2*--*14 Reserved

15 Missing