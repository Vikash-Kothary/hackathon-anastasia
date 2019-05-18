The *.geotiff files are raster images of the daily or monthly mean irradiance (in watts per square meter) of the UK, on a regular 5km x 5km grid.  Try using the Python package 'rasterio' to load these files.  These files were processed by my Jupyter notebook script.

The *.nc files are the raw NetCDF3 files downloaded from the CM SAF SARAH website[1].  Probably ignore these.  But, if you need them, you can try using the Python package 'xarray'.


1: https://wui.cmsaf.eu/safira/action/viewDoiDetails?acronym=SARAH_V001
