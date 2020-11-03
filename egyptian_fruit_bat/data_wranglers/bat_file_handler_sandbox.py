"""
A quick script that organizes the Egyptian fruit bat data into a 
more accessible format. Going to grab the subsection of the data
that is labeled, so that we can focus on training on just the labeled
data for now. 
"""

"""
The file Annotations.csv obviously contains the annotations, however, the
annotations point to file IDs rather than to actual filenames, and so 
we have to crossreference the file IDs with filenames using the FileInfo.csv
"""

import pandas as pd
orig_path = "/media/oliver/My Passport/egyptian_fruit_bat/"
"""making the annotations better, so that they contain file name and file location:"""
# annotations = pd.read_csv(path + "Annotations.csv")
# file_info = pd.read_csv(path + "FileInfo.csv")

# def get_file_name_from_id(file_id):
#     return file_info[file_info['FileID'] == file_id]['File name'].values[0]

# def get_file_folder_from_id(file_id):
#     return file_info[file_info['FileID'] == file_id]['File folder'].values[0]

# annotations["File name"] = [get_file_name_from_id(file_id) for file_id in annotations["FileID"]]
# annotations["File folder"] = [get_file_folder_from_id(file_id) for file_id in annotations["FileID"]]

# annotations.to_csv(path + "better_annotations.csv")

"""creating a folder full of all of the annotated data"""

import shutil
import os
from progressbar import ProgressBar
import numpy as np
annotations = pd.read_csv(orig_path + "better_annotations.csv")

#for random sampling:
#annotations = annotations.sample(frac = 0.1)


dest_path = "/media/oliver/My Passport/egyptian_fruit_bat_annotated_tiny/"
unzipped_path = "/media/oliver/My Passport/egyptian_fruit_bat_unzipped/"


context_dict = {0:"unknown", 1:"separation", 2:"biting", 
                3:"feeding", 4:"fighting", 5:"grooming", 
                6:"isolation", 7:"kissing", 8:"landing", 
                9:"mating protest", 10:"threat-like", 
                11:"general", 12:"sleeping"}

annotations = annotations[["File name", "File folder", "Context"]]
annotations["Context desc."] = [context_dict[x] for x in annotations["Context"]]


max_count = 800
annotation_counts = annotations["Context desc."].value_counts()

sampled_annotations = pd.DataFrame()

for context_desc in annotation_counts.index:
    if annotation_counts[context_desc] >= max_count:
        temp_df = annotations[annotations["Context desc."] == context_desc].sample(n = max_count)
        sampled_annotations = sampled_annotations.append(temp_df, 
                                                         ignore_index = True)
    else:
        sampled_annotations = sampled_annotations.append(annotations[annotations["Context desc."] == context_desc], 
                                                         ignore_index = True)
        
sampled_annotations['Context desc.'].value_counts().plot(kind = 'bar', 
                                                         title = "Sampled Class Label Distribution", 
                                                         ylabel = "count")


sampled_annotations['File path'] = unzipped_path + sampled_annotations['File folder'] + "/" + sampled_annotations['File name']

# print("Checking that the files exist...")
# n_samples = int(len(sampled_annotations['File path'])/2)
# n_goofs = 0

# for i,j in enumerate(np.random.randint(0, len(sampled_annotations['File path'])-1, n_samples)):
#     if not(os.path.exists(sampled_annotations['File path'] [i])):
#         n_goofs += 1# for temp_path in sampled_annotations['File path']:
    
#     progress.current += 1
#     progress.__call__()
    
#     temp_dest_dir = dest_path + temp_path.split("/")[-2]
    
#     try:
#         os.mkdir(temp_dest_dir)
#     except FileExistsError:
#         pass

#     shutil.copy(temp_path, 
#                 temp_dest_dir)
# print("Only goofed up {} times!".format(n_goofs))
        

# print("\nCopying files from: \n{} \n to: \n{}".format(unzipped_path, dest_path))
# progress = ProgressBar(len(sampled_annotations['File path']), 
#                         fmt = ProgressBar.FULL)

# for temp_path in sampled_annotations['File path']:
    
#     progress.current += 1
#     progress.__call__()
    
#     temp_dest_dir = dest_path + temp_path.split("/")[-2]
    
#     try:
#         os.mkdir(temp_dest_dir)
#     except FileExistsError:
#         pass

#     shutil.copy(temp_path, 
#                 temp_dest_dir)
    
    
"""doing it without bins"""
# try:
#     mkdir(dest_path + "annotated_data")
# except FileExistsError:
#     pass

# for i in range(len(annotated_paths)):
#     shutil.copy(annotated_paths[i], 
#                 dest_path + "annotated_data")
    
    
    
    
