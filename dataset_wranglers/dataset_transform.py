import os
from pathlib import Path
import pickle
import tqdm

class dataset_transformer():

    def __init__(self, original_folder):
        assert os.path.exists(original_folder), "Could not find: {}".format(original_folder)
        self.original_folder = original_folder
        
    def transform_to(self, 
                     transform,
                     new_folder, 
                     file_saver = None,
                     output_file_type = ".pkl",
                     input_file_type = None,
                     data_paths = None):
        """
        Applies the provided transform onto all of the files within `self.original folder`
        and copies the result into `new_folder`. The new folder will be a mirror of the original, 
        although the data will be transformed. The parameter `data_paths`, if not None, is passed 
        if there is a subset of data you wish to transform.
        
        If you don't pass a subset of data to transform, this script will attempt to 
        transform everything within the `self.original_folder`. All files that fail to 
        be converted due to improper filetype or what have you will be appended to the 
        `failed_files` list (which will be saved to file in the `new_folder` for future reference)
        
        The `transform` function must take a path as an input but it can output whatever, the 
        output is just saved as a pkl file unless you input your own `file_saver`. The file saver is 
        a user-defined function that takes data and saves it to the provided file. 
        """
        failed_files = []
        
        original_folder_head = str(self.original_folder).split("/")[-1]
        
        if data_paths == None:
            data_paths = [str(x) for x in Path(self.original_folder).glob("**/*")]
          
        if input_file_type != None:
            data_paths = [x for x in data_paths if input_file_type.lower() in str(x).lower()]
            
        #make sure data_paths are files and not directories:
        data_paths = [x for x in data_paths if not(os.path.isdir(x))]
        
        try:
            os.mkdir(new_folder)
        except FileExistsError:
            pass
        
        for d_path in tqdm.tqdm(data_paths):
            try:
                #if there is an error transforming the data -- append the path to `failed_files`
                transformed_data = transform(d_path)
            except:
                failed_files.append(d_path)
                continue
            
            new_data_path = new_folder + d_path.split(original_folder_head)[-1]
            new_data_path = ("/").join(new_data_path.split(".")[:-1])
            
            if file_saver == None:#default file_saver is just pickling
                try:
                    with open(new_data_path + output_file_type, 'wb') as f:
                        pickle.dump(transformed_data, f)
                except:
                    os.mkdir( ("/").join(new_data_path.split("/")[:-1]))
                    with open(new_data_path, 'wb') as f:
                        pickle.dump(transformed_data, f)
            else:
                try:
                    file_saver(transformed_data, new_data_path)
                except:
                    os.mkdir( ("/").join(new_data_path.split("/")[:-1]))
                    file_saver(transformed_data, new_data_path)
           
        
        #save failed_files for future reference:
        with open("{}/failed_files_from_transform.txt".format(new_folder), 'wb') as f:
            pickle.dump(failed_files, f)    
            
    
        
                
"""
#Example Usage:
    
from PIL import Image
import numpy as np
from skimage.transform import resize
import librosa
import matplotlib.pyplot as plt

def numpy_to_img_saver(np_array, save_path):
        img = Image.fromarray(np_array)
        if img.mode != 'RGB':
            img = img.convert('RGB')
        
        img.save(save_path+".png")
        
def get_cqt(path, 
            final_transform = lambda x: x,
            hop_length = 1024,
            n_bins = 90, 
            fmin = "C5"):
    
    x, rate = librosa.load(path, 
                           mono = True,
                           sr = None,
                           dtype = np.float32)

    spec = librosa.cqt(x,
                       sr = rate, 
                       fmin = librosa.note_to_hz(fmin),
                       hop_length=hop_length,
                       n_bins = n_bins)
    
    
    spec = librosa.amplitude_to_db(np.abs(spec), ref = np.max)
    spec = resize(spec, (225, 225))
    
    #spec = (spec - np.max(spec))*255
    spec = 255*(spec - np.min(spec))/(np.max(spec) - np.min(spec))
    
    spec = final_transform(spec)
    return spec.astype(np.uint8)

dst = dataset_transformer("/home/oliver/Desktop/efb_test_dataset")
dst.transform_to(get_cqt, 
                 "/home/oliver/Desktop/transformed_efb_test_dataset",
                 file_saver = numpy_to_img_saver)
"""
