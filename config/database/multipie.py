#!/usr/bin/env python

import bob

# setup for Multi-PIE database
name = 'multipie'
db = bob.db.multipie.Database()
protocol = 'U'

img_input_dir = "/idiap/resource/database/Multi-Pie/data/"
img_input_ext = ".png"
pos_input_dir = "/idiap/user/mguenther/annotations/multipie/"
pos_input_ext = ".pos"

first_annot = 1
all_files_options = { 'expressions': 'neutral' }
world_extractor_options = { 'expressions': 'neutral' }
world_projector_options = { 'expressions': 'neutral', 'world_sampling': 3, 'world_first': True } 
world_enroler_options = { 'expressions': 'neutral' }

