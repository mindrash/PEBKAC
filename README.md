# PEBKAC
The PEBKAC series (pebkac.fyi) is dynamically generated with location and solar wind telemetry data from the Voyager 1 spacecraft. Each is a random view from a celestial body in our solar system. The signal strength of voyager degrades over the series and is highlighted when close to one of the bodies. Major solar storms and other worldly events are highlighted along the way. More project details and variation information can be found at pebkac.fyi.

This one is meant to be seen in larger views and should be good for print.

## Overview
In this series I wanted to continue to explore interesting data sets and incorporate their influence in to the dynamic generation. While many look simple, I think there are some fun things to find along the way in the whole series. Seeing one next to another and knowing the variations between as well as from the start to the end of voyager's journey make the collection meaningful to me. The telemetry has been sourced from public domain data in the [NASA Space Science Data Coordinated Archive](https://nssdc.gsfc.nasa.gov/nmc/spacecraft/displayDataset.action?spacecraftId=1977-084A).

The series progresses for each day from Voyager 1 launch (September 9, 1977) through the end of location telemetry data available in the data set (January 1, 2005). Included are two data sets for location telemetry and solar wind experiment metrics. More detail on these can be found below.

Contract: 0xAD0202597F9A14cF32c64515aA96a4c53134cc37

## Technologies
- SVG: Scalable Vector Graphics - I wanted to use SVG for this servies to move closer to an on chain solution. I decide to use IPFS because of the data set size in use, but maybe next time
- Python
- Solidity - implemented more on the contract in this one:
```
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Burnable.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Royalty.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/security/PullPayment.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "./ContextMixin.sol";
import "./@rarible/royalties/contracts/impl/RoyaltiesV2Impl.sol";
import "./@rarible/royalties/contracts/LibPart.sol";
import "./@rarible/royalties/contracts/LibRoyaltiesV2.sol";
```


## Variations

| variation                      | description  |
|--------------------------------|--------------|
| celestial_body | One of the celestial bodies in the solar system |
| voyager_date | The series covers 9997 days from September 9, 1977 through January 1, 2005 |
| palette | 3 sets of color palettes |
| night_sky | Each celestial body will have a night sky with approximate other viewable celestial bodies randomly placed |
| solar_wind | The solar wind experiment data is on the top label (more detail below) |
| location | Voyager 1 location telemetry is on the bottom label (more detail below) |
| landscape | The colors are randomly pulled from the 3 sets of palettes (celestial body specific). The number of layers/bands and general locations of each are randomly picked |
| voyager_signal | Should flow across the landscape if the origin is below the horizon (hopefully) |
| signal_strength1 | The signal strength should be stronger if the space craft was in close proximity of the celestial body |
| signal_strength2 | The circles will start to part into dashes and further distance after voyager has "left the solar system" |
| signal_animation | Random signal animation |
| solar storms | The Voyager 1 signal will be noticably highlighted during some of the major solar storms of the period |
| memorials | The Challenger and Columbia dates are memorialized |
| women | Sally Rides achievement date is marked |
| annuals | Martin Luther King day, random signal pride color in June, Halloween |

## Datasets
[NASA Space Science Data Coordinated Archive](https://nssdc.gsfc.nasa.gov/nmc/spacecraft/displayDataset.action?spacecraftId=1977-084A)

### Telemetry
```
PDS_VERSION_ID                = PDS3                                          
DATA_SET_ID                   = "VG1-SS-POS-6-1DAY-V1.0"                      
PRODUCT_ID                    = "VG1TRAJ_1DAY_1977_2005"                      
PRODUCT_TYPE                  = DATA                                          
PRODUCT_VERSION_ID            = "1.0"                                         
PRODUCT_CREATION_TIME         = 2009-02-16T08:45                              
                                                                              
RECORD_TYPE                   = FIXED_LENGTH                                  
RECORD_BYTES                  = 62                                            
FILE_RECORDS                  = 10000                                         
                                                                              
START_TIME                    = 1977-09-09                                    
STOP_TIME                     = 2005-01-24                                    
SPACECRAFT_CLOCK_START_COUNT  = "N/A"                                         
SPACECRAFT_CLOCK_STOP_COUNT   = "N/A"                                         
                                                                              
INSTRUMENT_HOST_NAME          = "VOYAGER 1"                                   
INSTRUMENT_HOST_ID            = "VG1"                                         
MISSION_PHASE_NAME            = "CRUISE"                                      
TARGET_NAME                   = "SOLAR SYSTEM"                                
INSTRUMENT_NAME               = "N/A"                                         
INSTRUMENT_ID                 = "POS"                                         
DESCRIPTION                   = "                                             
      Voyager 1 daily position (trajectory) data in Solar Ecliptic and        
      Heliographic (HG) coordinates. The data begin in 1977 and go through    
      the beginning of 2005."                                                 
                                                                              
^TABLE                        = "VG1TRAJ_1DAY_1977_2005.TAB"                  
OBJECT                        = TABLE                                         
  INTERCHANGE_FORMAT          = ASCII                                         
  ROWS                        = 10000                                         
  COLUMNS                     = 7                                             
  ROW_BYTES                   = 62                                            
  OBJECT                      = COLUMN                                        
    NAME                      = "DATE"                                        
    COLUMN_NUMBER             = 1                                             
    UNIT                      = "N/A"                                         
    DATA_TYPE                 = CHARACTER                                     
    START_BYTE                = 2                                             
    BYTES                     = 11                                            
    DESCRIPTION               = "                                             
      Sample date (UTC) in the format YYYY DDD.DD where YYYY=year,            
      and DDD.DD=decimal day (e.g. 1977 252.00)."                             
  END_OBJECT                  = COLUMN                                        
                                                                              
  OBJECT                      = COLUMN                                        
    NAME                      = "Range"                                       
    COLUMN_NUMBER             = 2                                             
    UNIT                      = "AU"                                          
    DATA_TYPE                 = ASCII_REAL                                    
    START_BYTE                = 14                                            
    BYTES                     = 8                                             
    MISSING_CONSTANT          = 0.000                                         
    DESCRIPTION               = "                                             
      Heliocentric range in AU"                                               
  END_OBJECT                  = COLUMN                                        
                                                                              
  OBJECT                      = COLUMN                                        
    NAME                      = "SE_LAT"                                      
    COLUMN_NUMBER             = 3                                             
    UNIT                      = "DEGREE"                                      
    DATA_TYPE                 = ASCII_REAL                                    
    START_BYTE                = 23                                            
    BYTES                     = 9                                             
    MISSING_CONSTANT          = 00.0000                                       
    DESCRIPTION               = "                                             
      Solar Ecliptic (SE) latitude in degrees"                                
  END_OBJECT                  = COLUMN                                        
                                                                              
  OBJECT                      = COLUMN                                        
    NAME                      = "SE_LON"                                      
    COLUMN_NUMBER             = 4                                             
    UNIT                      = "DEGREE"                                      
    DATA_TYPE                 = ASCII_REAL                                    
    START_BYTE                = 33                                            
    BYTES                     = 6                                             
    MISSING_CONSTANT          = 000.00                                        
    DESCRIPTION               = "                                             
      Solar Ecliptic (SE) longitude in degrees"                               
  END_OBJECT                  = COLUMN                                        
                                                                              
  OBJECT                      = COLUMN                                        
    NAME                      = "HG_LAT"                                      
    COLUMN_NUMBER             = 5                                             
    UNIT                      = "DEGREE"                                      
    DATA_TYPE                 = ASCII_REAL                                    
    START_BYTE                = 40                                            
    BYTES                     = 8                                             
    MISSING_CONSTANT          = 0.0000                                        
    DESCRIPTION               = "                                             
       Solar Heliographic (HG) latitude in degrees"                           
  END_OBJECT                  = COLUMN                                        
                                                                              
  OBJECT                      = COLUMN                                        
    NAME                      = "HG_LON"                                      
    COLUMN_NUMBER             = 6                                             
    UNIT                      = "DEGREE"                                      
    DATA_TYPE                 = ASCII_REAL                                    
    START_BYTE                = 49                                            
    BYTES                     = 6                                             
    MISSING_CONSTANT          = 0.00                                          
    DESCRIPTION               = "                                             
       Solar Heliographic (HG) longitude in degrees"                          
  END_OBJECT                  = COLUMN                                        
                                                                              
  OBJECT                      = COLUMN                                        
    NAME                      = "IHG_LON"                                     
    COLUMN_NUMBER             = 7                                             
    UNIT                      = "DEGREE"                                      
    DATA_TYPE                 = ASCII_REAL                                    
    START_BYTE                = 56                                            
    BYTES                     = 6                                             
    MISSING_CONSTANT          = 0.000                                         
    DESCRIPTION               = "                                             
       Inertial Solar Heliographic longitude in degrees with respect to       
       the ascending node of the solar equator in the ecliptic."              
  END_OBJECT                  = COLUMN                                        
                                                                              
END_OBJECT                    = TABLE                                         
END                                                                           
```

### Solar Wind
Solar wind comes from two datasets

1977-1989
```
PDS_VERSION_ID                = PDS3                                          
DATA_SET_ID                   = "VG1-SW-MAG-4-SUMM-HGCOORDS-1HR-V1.0"         
PRODUCT_ID                    = "VG1MAG_1HR_1977_1989"                        
PRODUCT_TYPE                  = DATA                                          
PRODUCT_VERSION_ID            = "1.0"                                         
PRODUCT_CREATION_TIME         = 2009-02-16T08:45                              
                                                                              
RECORD_TYPE                   = FIXED_LENGTH                                  
RECORD_BYTES                  = 79                                            
FILE_RECORDS                  = 75729                                         
                                                                              
START_TIME                    = 1977-09-05T17:00                              
STOP_TIME                     = 1989-12-31T22:00                              
SPACECRAFT_CLOCK_START_COUNT  = "NULL"                                        
SPACECRAFT_CLOCK_STOP_COUNT   = "NULL"                                        
                                                                              
INSTRUMENT_HOST_NAME          = "VOYAGER 1"                                   
INSTRUMENT_HOST_ID            = "VG1"                                         
MISSION_PHASE_NAME            = "CRUISE"                                      
TARGET_NAME                   = "SOLAR WIND"                                  
INSTRUMENT_NAME               = "TRIAXIAL FLUXGATE MAGNETOMETER"              
INSTRUMENT_ID                 = "MAG"                                         
DESCRIPTION                   = "                                             
      Voyager 1 MAG 1 hour averaged data from in Heliographic (HG)            
      coordinates. The data begin in 1977 and go through the end of 1989."    
                                                                              
^TABLE                        = "VG1MAG_1HR_1977_1989.TAB"                    
OBJECT                        = TABLE                                         
  INTERCHANGE_FORMAT          = ASCII                                         
  ROWS                        = 75729                                         
  COLUMNS                     = 10                                            
  ROW_BYTES                   = 79                                            
  OBJECT                      = COLUMN                                        
    NAME                      = "Spacecraft"                                  
    COLUMN_NUMBER             = 1                                             
    UNIT                      = "N/A"                                         
    DATA_TYPE                 = CHARACTER                                     
    START_BYTE                = 1                                             
    BYTES                     = 1                                             
    DESCRIPTION               = "                                             
        S/C identification (Voyager 1 = 1, Voyager 2 = 2)"                    
  END_OBJECT                  = COLUMN                                        
                                                                              
  OBJECT                      = COLUMN                                        
    NAME                      = "UTC"                                         
    COLUMN_NUMBER             = 2                                             
    UNIT                      = "N/A"                                         
    DATA_TYPE                 = CHARACTER                                     
    START_BYTE                = 3                                             
    BYTES                     = 11                                            
    DESCRIPTION               = "                                             
      Sample time (UTC) in the format YY DDD HH where YY=year, DDD=day        
      and HH =hour (e.g. 77 248 17)."                                         
  END_OBJECT                  = COLUMN                                        
                                                                              
  OBJECT                      = COLUMN                                        
    NAME                      = "X_IHG"                                       
    COLUMN_NUMBER             = 3                                             
    UNIT                      = "AU"                                          
    DATA_TYPE                 = ASCII_REAL                                    
    START_BYTE                = 13                                            
    BYTES                     = 9                                             
    MISSING_CONSTANT          = 0.000                                         
    DESCRIPTION               = "                                             
      X IHG position component (A.U. - IHG coordinates)"                      
  END_OBJECT                  = COLUMN                                        
                                                                              
  OBJECT                      = COLUMN                                        
    NAME                      = "Y_IHG"                                       
    COLUMN_NUMBER             = 4                                             
    UNIT                      = "AU"                                          
    DATA_TYPE                 = ASCII_REAL                                    
    START_BYTE                = 23                                            
    BYTES                     = 9                                             
    MISSING_CONSTANT          = 0.000                                         
    DESCRIPTION               = "                                             
      Y IHG position component (A.U. - IHG coordinates)"                      
  END_OBJECT                  = COLUMN                                        
                                                                              
  OBJECT                      = COLUMN                                        
    NAME                      = "Z_IHG"                                       
    COLUMN_NUMBER             = 5                                             
    UNIT                      = "AU"                                          
    DATA_TYPE                 = ASCII_REAL                                    
    START_BYTE                = 33                                            
    BYTES                     = 9                                             
    MISSING_CONSTANT          = 0.000                                         
    DESCRIPTION               = "                                             
      Z IHG position component (A.U. - IHG coordinates)"                      
  END_OBJECT                  = COLUMN                                        
                                                                              
  OBJECT                      = COLUMN                                        
    NAME                      = "RANGE"                                       
    COLUMN_NUMBER             = 6                                             
    UNIT                      = "AU"                                          
    DATA_TYPE                 = ASCII_REAL                                    
    START_BYTE                = 43                                            
    BYTES                     = 8                                             
    MISSING_CONSTANT          = 0.000                                         
    DESCRIPTION               = "                                             
       Heliocentric range = sqrt(X*X+Y*Y+Z*Z)"                                
  END_OBJECT                  = COLUMN                                        
                                                                              
  OBJECT                      = COLUMN                                        
    NAME                      = "F1"                                          
    COLUMN_NUMBER             = 7                                             
    UNIT                      = "nT"                                          
    DATA_TYPE                 = ASCII_REAL                                    
    START_BYTE                = 52                                            
    BYTES                     = 7                                             
    MISSING_CONSTANT          = 0.000                                         
    DESCRIPTION               = "                                             
       Field magnitude (nT)  ( avg(F2(48sec))"                                
  END_OBJECT                  = COLUMN                                        
                                                                              
  OBJECT                      = COLUMN                                        
    NAME                      = "F2"                                          
    COLUMN_NUMBER             = 8                                             
    UNIT                      = "nT"                                          
    DATA_TYPE                 = ASCII_REAL                                    
    START_BYTE                = 60                                            
    BYTES                     = 7                                             
    MISSING_CONSTANT          = 0.000                                         
    DESCRIPTION               = "                                             
       Field modulus (nT)  ( norm (B1,B2,B3) )"                               
  END_OBJECT                  = COLUMN                                        
                                                                              
  OBJECT                      = COLUMN                                        
    NAME                      = "DELTA"                                       
    COLUMN_NUMBER             = 9                                             
    UNIT                      = "DEGREE"                                      
    DATA_TYPE                 = ASCII_REAL                                    
    START_BYTE                = 68                                            
    BYTES                     = 5                                             
    MISSING_CONSTANT          = 0.0                                           
    DESCRIPTION               = "                                             
       Latitudinal angle (degrees - HG coordinates)"                          
  END_OBJECT                  = COLUMN                                        
                                                                              
  OBJECT                      = COLUMN                                        
    NAME                      = "LAMBDA"                                      
    COLUMN_NUMBER             = 10                                            
    UNIT                      = "DEGREE"                                      
    DATA_TYPE                 = ASCII_REAL                                    
    START_BYTE                = 74                                            
    BYTES                     = 5                                             
    MISSING_CONSTANT          = 0.0                                           
    DESCRIPTION               = "                                             
       Longitudinal angle (degrees - HG coordinates)"                         
  END_OBJECT                  = COLUMN                                        
END_OBJECT                    = TABLE                                         
END                                                                           
```
1990-2004 - so the last in the serie will not have this expirement data
```
PDS_VERSION_ID                = PDS3                                          
DATA_SET_ID                   = "VG1-SS-POS-6-1DAY-V1.0"                      
PRODUCT_ID                    = "VG1TRAJ_1DAY_1977_2005"                      
PRODUCT_TYPE                  = DATA                                          
PRODUCT_VERSION_ID            = "1.0"                                         
PRODUCT_CREATION_TIME         = 2009-02-16T08:45                              
                                                                              
RECORD_TYPE                   = FIXED_LENGTH                                  
RECORD_BYTES                  = 62                                            
FILE_RECORDS                  = 10000                                         
                                                                              
START_TIME                    = 1977-09-09                                    
STOP_TIME                     = 2005-01-24                                    
SPACECRAFT_CLOCK_START_COUNT  = "N/A"                                         
SPACECRAFT_CLOCK_STOP_COUNT   = "N/A"                                         
                                                                              
INSTRUMENT_HOST_NAME          = "VOYAGER 1"                                   
INSTRUMENT_HOST_ID            = "VG1"                                         
MISSION_PHASE_NAME            = "CRUISE"                                      
TARGET_NAME                   = "SOLAR SYSTEM"                                
INSTRUMENT_NAME               = "N/A"                                         
INSTRUMENT_ID                 = "POS"                                         
DESCRIPTION                   = "                                             
      Voyager 1 daily position (trajectory) data in Solar Ecliptic and        
      Heliographic (HG) coordinates. The data begin in 1977 and go through    
      the beginning of 2005."                                                 
                                                                              
^TABLE                        = "VG1TRAJ_1DAY_1977_2005.TAB"                  
OBJECT                        = TABLE                                         
  INTERCHANGE_FORMAT          = ASCII                                         
  ROWS                        = 10000                                         
  COLUMNS                     = 7                                             
  ROW_BYTES                   = 62                                            
  OBJECT                      = COLUMN                                        
    NAME                      = "DATE"                                        
    COLUMN_NUMBER             = 1                                             
    UNIT                      = "N/A"                                         
    DATA_TYPE                 = CHARACTER                                     
    START_BYTE                = 2                                             
    BYTES                     = 11                                            
    DESCRIPTION               = "                                             
      Sample date (UTC) in the format YYYY DDD.DD where YYYY=year,            
      and DDD.DD=decimal day (e.g. 1977 252.00)."                             
  END_OBJECT                  = COLUMN                                        
                                                                              
  OBJECT                      = COLUMN                                        
    NAME                      = "Range"                                       
    COLUMN_NUMBER             = 2                                             
    UNIT                      = "AU"                                          
    DATA_TYPE                 = ASCII_REAL                                    
    START_BYTE                = 14                                            
    BYTES                     = 8                                             
    MISSING_CONSTANT          = 0.000                                         
    DESCRIPTION               = "                                             
      Heliocentric range in AU"                                               
  END_OBJECT                  = COLUMN                                        
                                                                              
  OBJECT                      = COLUMN                                        
    NAME                      = "SE_LAT"                                      
    COLUMN_NUMBER             = 3                                             
    UNIT                      = "DEGREE"                                      
    DATA_TYPE                 = ASCII_REAL                                    
    START_BYTE                = 23                                            
    BYTES                     = 9                                             
    MISSING_CONSTANT          = 00.0000                                       
    DESCRIPTION               = "                                             
      Solar Ecliptic (SE) latitude in degrees"                                
  END_OBJECT                  = COLUMN                                        
                                                                              
  OBJECT                      = COLUMN                                        
    NAME                      = "SE_LON"                                      
    COLUMN_NUMBER             = 4                                             
    UNIT                      = "DEGREE"                                      
    DATA_TYPE                 = ASCII_REAL                                    
    START_BYTE                = 33                                            
    BYTES                     = 6                                             
    MISSING_CONSTANT          = 000.00                                        
    DESCRIPTION               = "                                             
      Solar Ecliptic (SE) longitude in degrees"                               
  END_OBJECT                  = COLUMN                                        
                                                                              
  OBJECT                      = COLUMN                                        
    NAME                      = "HG_LAT"                                      
    COLUMN_NUMBER             = 5                                             
    UNIT                      = "DEGREE"                                      
    DATA_TYPE                 = ASCII_REAL                                    
    START_BYTE                = 40                                            
    BYTES                     = 8                                             
    MISSING_CONSTANT          = 0.0000                                        
    DESCRIPTION               = "                                             
       Solar Heliographic (HG) latitude in degrees"                           
  END_OBJECT                  = COLUMN                                        
                                                                              
  OBJECT                      = COLUMN                                        
    NAME                      = "HG_LON"                                      
    COLUMN_NUMBER             = 6                                             
    UNIT                      = "DEGREE"                                      
    DATA_TYPE                 = ASCII_REAL                                    
    START_BYTE                = 49                                            
    BYTES                     = 6                                             
    MISSING_CONSTANT          = 0.00                                          
    DESCRIPTION               = "                                             
       Solar Heliographic (HG) longitude in degrees"                          
  END_OBJECT                  = COLUMN                                        
                                                                              
  OBJECT                      = COLUMN                                        
    NAME                      = "IHG_LON"                                     
    COLUMN_NUMBER             = 7                                             
    UNIT                      = "DEGREE"                                      
    DATA_TYPE                 = ASCII_REAL                                    
    START_BYTE                = 56                                            
    BYTES                     = 6                                             
    MISSING_CONSTANT          = 0.000                                         
    DESCRIPTION               = "                                             
       Inertial Solar Heliographic longitude in degrees with respect to       
       the ascending node of the solar equator in the ecliptic."              
  END_OBJECT                  = COLUMN                                        
                                                                              
END_OBJECT                    = TABLE                                         
END                                                                           

```

## Analysis
Will provide examples and some analysis after mint.