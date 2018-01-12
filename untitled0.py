#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 11:28:20 2018

@author: emma
"""

#import packages
import json
import csv

#open JSON file
with open('conflict_data_full_lined.json') as file:
    data = json.load(file)
    
#create and write CSV file
with open('preprocessed_data.csv', 'w', newline='') as file:
    csvwriter = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    
    csvwriter.writerow(['ID', 'relid', 'year', 'active_year', 'code_status', 
                                              'type_of_violence', 'conflict_dset_id', 
                                              'conflict_new_id', 'conflict_name', 'dyad_dset_id', 
                                              'dyad_new_id', 'dyad_name', 'side_a_dset_id', 
                                              'side_a_new_id', 'side_a', 'side_b_dset_id', 
                                              'side_b_new_id', 'side_b', 'number_of_sources', 
                                              'source_article', 'source_office', 'source_date', 
                                              'source_headline', 'source_original', 'where_prec', 
                                              'where_coordinates', 'where_description', 'adm_1', 'adm_2', 
                                              'latitude', 'longitude', 'geom_wkt', 'priogrid_gid', 
                                              'country', 'country_id', 'region', 'event_clarity', 
                                              'date_prec', 'date_start', 'date_end', 'deaths_a', 
                                              'deaths_b', 'deaths_civilians', 'deaths_unknown', 
                                              'best', 'high', 'low'])
    
    for row in data:
        csvwriter.writerow(row.values())