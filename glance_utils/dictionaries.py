import numpy as np

l2_class_dict = {1:'Water', 
                 2:'Ice/Snow', 
                 3: 'Developed', 
                 4: 'Soil', 
                 5: 'Rock',
                 6: 'Beach/sand', 
                 7: 'Deciduous', 
                 8: 'Evergreen', 
                 9: 'Mixed', 
                 10: 'Shrub', 
                 11: 'Grassland', 
                 12:'Agriculture', 
                 13: 'Moss/lichen', 
                 0: np.nan}

l1_class_dict = {1: 'Water', 
                 2: 'Ice/Snow', 
                 3: 'Developed', 
                 4: 'Barren/Sparsely vegetated', 
                 5: 'Trees', 
                 6: 'Shrub', 
                 7: 'Herbaceous'}

continent_dict = {1: 'North America', 
                  2: 'South America', 
                  3: 'Africa',
                  4: 'Europe', 
                  5: 'Asia',
                  6: 'Oceania'}