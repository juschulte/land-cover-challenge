import geopandas as gpd
import xarray as xr
from .dictionaries import l2_class_dict, l1_class_dict, continent_dict

def import_prep_glance_bolivia(glance_path='../data/bu_glance_training_dataV1.parquet', 
                               wrs_path='../data/landsat_wrs2_bolivia.gpkg'):
    """ Handy wrapper around importing and preparing the GLanCE data"""
    # read the files
    gdf = gpd.read_parquet(glance_path)
    wrs_bolivia = gpd.read_file(wrs_path)
    
    # replace with the dicts
    gdf['Continent_Code'] = gdf['Continent_Code'].replace(continent_dict)
    gdf['Glance_Class_ID_level1'] = gdf['Glance_Class_ID_level1'].replace(l1_class_dict)
    gdf['Glance_Class_ID_level2'] = gdf['Glance_Class_ID_level2'].replace(l2_class_dict)
    
    return gdf.clip(wrs_bolivia)


def get_class_timeseries(dataset, glance_gdf, landcover_class):
    """
    Given a dataset with point IDs and the glance file, finds the time series for a specific class
    """
    gdf_class = glance_gdf[glance_gdf.Glance_Class_ID_level1 == landcover_class]
    
    ids = xr.DataArray(gdf_class.ID)
    point_ids = dataset.point_id[dataset.point_id.isin(ids)].values
    point_ids = xr.DataArray(point_ids, dims=['pid'], coords={'pid':point_ids ,})
    
    return dataset.sel(point_id = point_ids)

def normalized_difference(ds, band1, band2, epsilon=1e-5):
    return (ds[band1] - ds[band2]) /  (ds[band1] + ds[band2]+epsilon)
    
    
def normalized_difference(ds, band1, band2, epsilon=1e-5):
    return (ds[band1] - ds[band2]) /  (ds[band1] + ds[band2]+epsilon)