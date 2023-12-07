import subprocess

packages=['earthengine-api','folium', 'rasterio', 'rtree', 'pandas', 'geopandas', 'pyCRS', 'geemap', 'mapclassify', 'contextily', 'matplotlib_scalebar', 'opencv-python', 'natsort', 'scikit-learn']
try: 
    for package in packages:
        subprocess.run(["pip","install", package])
        print(f"{package} installed successfully")

except subprocess.CalledProcessError as e:
    print(f"Error installing the dependencies: {e}")