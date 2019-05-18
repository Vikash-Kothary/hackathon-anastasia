#https://gist.github.com/cspanring/5680334
sudo apt-get install gdal-bin
sudo apt-get install libgdal-dev libgdal1h
pip install GDAL==$(gdal-config --version) --global-option=build_ext --global-option="-I/usr/include/gdal" 
