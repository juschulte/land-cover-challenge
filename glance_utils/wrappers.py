import geopandas as gpd

from .dictionaries import l2_class_dict, l1_class_dict, continent_dict

def import_prep_glance_bolivia(glance_path='../data/bu_glance_training_dataV1.parquet', 
                               wrs_path='../data/landsat_wrs2_bolivia.gpkg'):
    # read the files
    gdf = gpd.read_parquet(glance_path)
    wrs_bolivia = gpd.read_file(wrs_path)
    
    # replace with the dicts
    gdf['Continent_Code'] = gdf['Continent_Code'].replace(continent_dict)
    gdf['Glance_Class_ID_level1'] = gdf['Glance_Class_ID_level1'].replace(l1_class_dict)
    gdf['Glance_Class_ID_level2'] = gdf['Glance_Class_ID_level2'].replace(l2_class_dict)
    
    return gdf.clip(wrs_bolivia)