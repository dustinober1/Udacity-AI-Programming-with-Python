#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/check_images.py
#
# PROGRAMMER: Dustin Ober
# DATE CREATED: July 14, 2023
# REVISED DATE: 
# PURPOSE: Classifies pet images using a pretrained CNN model, compares these
#          classifications to the true identity of the pets in the images, and
#          summarizes how well the CNN performed on the image classification task. 

# Imports python modules
from time import time, sleep

# Imports print functions that check the lab
from print_functions_for_lab_checks import *

# Imports functions created for this program
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results

# Main program function defined below
def main():
    # TODO 0: Measures total program runtime by collecting start time
    start_time = time()
    
    # TODO 1: Define get_input_args function within the file get_input_args.py
    in_arg = get_input_args()
    check_command_line_arguments(in_arg)

    # TODO 2: Define get_pet_labels function within the file get_pet_labels.py
    results = get_pet_labels(in_arg.dir)
    check_creating_pet_image_labels(results)

    # TODO 3: Define classify_images function within the file classiy_images.py
    classify_images(in_arg.dir, results, in_arg.arch)
    check_classifying_images(results) 

    # TODO 4: Define adjust_results4_isadog function within the file adjust_results4_isadog.py
    adjust_results4_isadog(results, in_arg.dogfile)
    check_classifying_labels_as_dogs(results)

    # TODO 5: Define calculates_results_stats function within the file calculates_results_stats.py
    results_stats = calculates_results_stats(results)
    check_calculating_results(results, results_stats)

    # TODO 6: Define print_results function within the file print_results.py
    print_results(results, results_stats, in_arg.arch, True, True)
    
    # TODO 0: Measure total program runtime by collecting end time
    end_time = time()
    
    # TODO 0: Computes overall runtime in seconds & prints it in hh:mm:ss format
    tot_time = end_time - start_time #calculate difference between end time and start time
    print("\n** Total Elapsed Runtime:",
          str(int((tot_time/3600)))+":"+str(int((tot_time%3600)/60))+":"
          +str(int((tot_time%3600)%60)))

# Call to main function to run the program
if __name__ == "__main__":
    main()
