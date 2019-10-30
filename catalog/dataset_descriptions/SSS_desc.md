The Sea Surface Salinity dataset in CMAP is the
**SMAP\_RSS\_L3\_SSS\_SMI\_8DAY-RUNNINGMEAN\_V3\_70KM\_1** NASA dataset.
This 8-day running mean sea surface salinity product has near-global
spatial coverage gridded to \~ 70km x 70km grid cells. While a 40km x
40km product exists, the 70km product has a much higher SNR. The SSS
data is derived from an L-band radiometer atop of the *Soil Moisture
Active Pass* (SMAP) satellite mission. SMAP operates in a near-polar
orbit with a beam swath of 1000km. Exact repeat overpasses happen every
eight days, with near-global coverage every three days.

SSS data was referenced against the HYCOM reference salinity field.
Multiple QA flags are described on page 38 of the [Technical
Documentation](https://podaac-tools.jpl.nasa.gov/drive/files/allData/smap/docs/V4/RSS_SMAP-SSS_V4.0_TechnicalDocumentation.pdf).

**NOTE** Two known issues identified by that dataset distributor are:

  - Satellite retrieval performance was degraded between Apr. 2015 -
    Aug. 2015, possibly due to instrument calibration issues.
  - Eight of the total observations days were missing a sea-ice mask. To
    minimize contamination of salinity samples, these data were excluded
    from the Level-2 product, therefore some of the level-3 gridded
    products around these dates may have less total observations. The
    dates are: 12-03-2015, 12-03-2015, 04-15-2016, 04-16-2016,
    09-27-2017, 09-28-2017, 11-25-2017 and 12-16-2018.
