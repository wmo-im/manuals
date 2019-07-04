**CREX Table C** *-- Data description operators*

+-----------+---------+-----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| REFERENCE | OPERAND | OPERATOR NAME                           | OPERATION DEFINITION                                                                                                                    |
+===========+=========+=========================================+=========================================================================================================================================+
| C 01      | YYY     | Data width replacement                  | YYY characters (from 000 to 999) replace specified Table B data width                                                                   |
+-----------+---------+-----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| C 02      | YYY     | Scale factor replacement                | YYY (from --99 to 999) replaces the specified Table B scale factor                                                                      |
+-----------+---------+-----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| C 05      | YYY     | Character insertion                     | YYY characters (from 001 to 999), including spaces, are inserted as a data field                                                        |
+-----------+---------+-----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| C 07      | YYY     | Units replacement                       | Change unit to unit defined in Common Code table C--6 by code figure equal to YYY, for example:                                         |
|           |         |                                         |                                                                                                                                         |
|           |         |                                         | YYY = 040 changes unit to Celsius                                                                                                       |
|           |         |                                         |                                                                                                                                         |
|           |         |                                         | YYY = 741 changes unit to km h^--1^                                                                                                     |
|           |         |                                         |                                                                                                                                         |
|           |         |                                         | YYY = 201 changes unit to knot                                                                                                          |
|           |         |                                         |                                                                                                                                         |
|           |         |                                         | YYY = 740 changes unit to km                                                                                                            |
+-----------+---------+-----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| C 41      | 000     | Define event                            | This operator denotes the beginning of the definition of an event                                                                       |
|           |         |                                         |                                                                                                                                         |
|           |         |                                         | (see Note 2)                                                                                                                            |
+-----------+---------+-----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| C 41      | 999     | Cancel define event                     | This operator denotes the conclusion of the event definition that was begun via the previous C 41 000 operator                          |
+-----------+---------+-----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| C 42      | 000     | Define conditioning event               | This operator denotes the beginning of the definition of a conditioning event (see Note 2)                                              |
+-----------+---------+-----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| C 42      | 999     | Cancel define\                          | This operator denotes the conclusion of the conditioning event definition that was begun via the previous C 42 000 operator             |
|           |         | conditioning event                      |                                                                                                                                         |
+-----------+---------+-----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| C 43      | 000     | Categorical forecast\                   | The values which follow are categorical forecast values (see Note 3)                                                                    |
|           |         | values follow                           |                                                                                                                                         |
+-----------+---------+-----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| C 43      | 999     | Cancel categorical\                     | This operator denotes the conclusion of the definition of categorical forecast values that was begun via the previous C 43 000 operator |
|           |         | forecast values follow                  |                                                                                                                                         |
+-----------+---------+-----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| C 60      | YYY     | National letters insertion (see Note 4) | YYY national letters including spaces are inserted as a data field                                                                      |
+-----------+---------+-----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+

Notes:

\(1) The operations specified by operator descriptors C 41 000, C 42 000 and C 43 000 remain defined until cancelled or until the end of the data subset. Regulation 95.3.4.2 shall not apply here.

\(2) An event, as defined for use with operators C 41 000 and C 42 000, is a set of one or more circumstances described using appropriate Table B descriptors along with their corresponding data values. The grouping of such descriptors together as a single \"event\" allows them to be collectively assigned as the target of a separate descriptor such as B 33 045 or B 33 046. When defining a circumstance within an event, descriptor B 33 042 may be employed preceding the appropriate Table B descriptor in order to indicate that the corresponding value is actually a bound for a range of values.

*(continued)*

*\
(CREX Table C -- continued)*

\(3) A categorical forecast value represents a \"best guess\" from among a set of related, and often mutually exclusive, data values or categories. Operator C 43 000 may be used to designate one or more values as being categorical forecast values, and descriptor B 33 042 may be employed preceding any such value in order to indicate that that value is actually a bound for a range of values.

\(4) Only the characters from the International Telegraphic Alphabet No. 2 (ITA2) are likely to be transmitted accurately to all recipients.
