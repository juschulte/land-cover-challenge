import xarray as xr

def mask_clouds(landsat_da):
    mask_bitfields = [1, 2, 3, 4]  # dilated cloud, cirrus, cloud, cloud shadow
    bitmask = 0
    for field in mask_bitfields:
        bitmask |= 1 << field
    
    t_bands = ['lwir11']
    r_bands = ['red','blue','green', 'nir08','swir16','swir22']

    bands = r_bands #+ t_bands # don't use temperature band
    
    landsat_da = landsat_da.sel(band=bands+['qa_pixel'])
    
    qa = landsat_da.sel(band='qa_pixel').astype('uint16')
    cloudy_bitmask = qa & bitmask  # This is the subset of the qa_pixel pixels that we definitely don't want
    # Mask the images with their respective cloud mask, choosing only pixels where "cloud" isn't
    landsat_da = landsat_da.sel(band=bands).where(cloudy_bitmask == 0)
    return landsat_da