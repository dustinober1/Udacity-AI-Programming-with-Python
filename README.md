# Udacity AI Programming with Python

![AI Programming with Python](Al%20Programming%20with%20Python.png)

This repository contains projects and exercises from the Udacity AI Programming with Python Nanodegree program. The projects focus on foundational AI concepts using Python, and cover topics such as data manipulation, machine learning, and neural networks.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Installation](#installation)
3. [Projects](#projects)
   - [Project 1: Dog Breed Classifier](#project-1-dog-breed-classifier)
   - [Project 2: Create Your Own Image Classifier](#project-2-create-your-own-image-classifier)
4. [Key Features](#key-features)
5. [Technologies Used](#technologies-used)
6. [Contributing](#contributing)
7. [License](#license)

## Project Overview

This repository includes two major projects and several exercises designed to help you learn and apply Python in AI programming:

- **Project 1**: Use a pre-trained image classifier to identify dog breeds.
- **Project 2**: Develop a custom image classifier to categorize images based on user-defined classes.

## Installation

To run the projects in this repository, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/dustinober1/Udacity-AI-Programming-with-Python.git
   cd Udacity-AI-Programming-with-Python
## Set Up a Virtual Environment (Recommended)

```bash
python3 -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
```
## Install the Required Dependencies

```bash
pip install -r requirements.txt
```
## Projects

### Project 1: Dog Breed Classifier

**Objective**: Develop a pipeline to process real-world, user-supplied images. If a dog is detected in the image, the algorithm will identify its breed; if a human is detected, it will find a resembling dog breed.

**Key Steps**:

- Image classification using a pre-trained CNN model (e.g., ResNet, VGG, or AlexNet).
- Evaluation of model performance using different metrics.
- Deployment of the model for real-time predictions.

**Files**:

- `Project 1`: [Link to Project Directory](Project%201)

### Project 2: Create Your Own Image Classifier

**Objective**: Create a deep learning model that can classify images into categories defined by the user.

**Key Steps**:

- Implementation of a custom CNN using PyTorch or TensorFlow.
- Training the network on a large image dataset (e.g., CIFAR-10 or ImageNet).
- Saving and loading models, and handling model inference.

**Files**:

- `Project 2`: [Link to Project Directory](Project%202)

## Key Features

- **Advanced AI Projects**: Each project is designed to build core AI and machine learning skills.
- **Hands-on Learning**: Implement AI models, train classifiers, and experiment with deep learning frameworks.
- **Comprehensive Documentation**: Each project comes with clear instructions, code comments, and explanations.

## Technologies Used

- **Programming Language**: Python 3
- **Libraries and Frameworks**:
  - NumPy
  - Pandas
  - Matplotlib
  - PyTorch or TensorFlow
  - OpenCV (for image processing)
- **Tools**:
  - Jupyter Notebooks
  - Virtual Environments (venv)

## Contributing

Contributions are welcome! If you have any suggestions or improvements, please fork the repository and submit a pull request. Make sure to follow the contribution guidelines if available.

## License

This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
