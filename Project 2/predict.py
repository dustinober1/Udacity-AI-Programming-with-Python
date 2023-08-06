import argparse
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import json
from torchvision import models
from PIL import Image

def load_checkpoint(filepath):
    """
    Loads the model from the checkpoint file and returns the model.
    """
    checkpoint = torch.load(filepath)
    model = getattr(models, checkpoint['arch'])(pretrained=True)
    
    # Checking the architecture to define the classifier accordingly
    if checkpoint['arch'] == 'resnet18':
        input_units = model.fc.in_features
    elif checkpoint['arch'] == 'densenet121':
        input_units = model.classifier.in_features
    else: # Assuming 'vgg13'
        input_units = model.classifier[0].in_features

    # Define the custom classifier
    classifier = nn.Sequential(
        nn.Linear(input_units, checkpoint['hidden_units']),
        nn.ReLU(),
        nn.Dropout(0.2),
        nn.Linear(checkpoint['hidden_units'], len(checkpoint['class_to_idx'])),
        nn.LogSoftmax(dim=1)
    )

    if checkpoint['arch'] == 'resnet18':
        model.fc = classifier
    elif checkpoint['arch'] == 'densenet121':
        model.classifier = classifier
    else:
        model.classifier = classifier

    model.load_state_dict(checkpoint['state_dict'])
    model.class_to_idx = checkpoint['class_to_idx']
    return model

# Rest of the functions remain the same

def main():
    parser = argparse.ArgumentParser(description='Predict flower name from an image along with the probability of that name')
    parser.add_argument('input', type=str, help='Image to predict')
    parser.add_argument('checkpoint', type=str, help='Model checkpoint')
    parser.add_argument('--top_k', type=int, default=5, help='Return top K most likely classes')
    parser.add_argument('--category_names', type=str, default='', help='Path to JSON file for mapping of categories to real names')
    parser.add_argument('--gpu', action='store_true', help='Use GPU for prediction')

    args = parser.parse_args()

    cat_to_name = {}
    if args.category_names:
        with open(args.category_names, 'r') as f:
            cat_to_name = json.load(f)

    model = load_checkpoint(args.checkpoint)
    top_probs, top_classes = predict(args.input, model, topk=args.top_k)
    labels = [cat_to_name.get(str(index), str(index)) for index in top_classes]

    print('Top classes and probabilities')
    for i in range(len(labels)):
        print(f"{labels[i]}: {top_probs[i]}")

if __name__ == "__main__":
    main()
