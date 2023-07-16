#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Dustin Ober
# DATE CREATED:  July 14, 2023                                
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files.
    """
    # Get the filenames from the folder
    filename_list = listdir(image_dir)
    
    # Create the results dictionary
    results_dic = dict()

    # Process through each file in the directory, extracting only the words
    # of the file that contain the pet image label
    for filename in filename_list:

        # Skip file if starts with . (like .DS_Store of Mac OSX)
        if filename[0] != ".":

            # Creates temporary label variable to hold pet label name extracted 
            pet_label = ""

            # TODO: 2a. BELOW REPLACE pass with CODE that will process each 
            #          filename in the filename_list extracting only the words
            #          of the filename that contain the pet image label. You 
            #          will need to use the .split() method to 'split' the string 
            #          into words (splitting on the underscore character: "_"). 
            #          This split will create a 'list' of words that were in the 
            #          filename. This list of words contains the pet image label 
            #          (dog breed name) in lower case letters that could be split 
            #          by a space (creating a list of names) and/or is separated by 
            #          underscores (_). This 'list' of names is returned as item[0] 
            #          of the list that the os.path.splitext(filename) method returns.
            #
            low_pet_image = filename.lower().split("_")
            for word in low_pet_image:
                if word.isalpha():
                    pet_label += word + " "
            
            pet_label = pet_label.strip()

            # If filename doesn't already exist in dictionary add it and it's
            # pet label - otherwise print an error message because indicates 
            if filename not in results_dic:
                results_dic[filename] = [pet_label]

            else:
                print("** Warning: Duplicate files exist in directory:", 
                      filename)

    # Replace None with the results_dic dictionary that you created with this
    # function
    return results_dic
