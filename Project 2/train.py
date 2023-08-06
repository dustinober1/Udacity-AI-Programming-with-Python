import argparse
import torch
import torchvision.transforms as transforms
import torchvision.datasets as datasets
import torchvision.models as models
import torch.nn as nn
import torch.optim as optim

def build_model(arch, hidden_units, output_units):
    """
    Builds the model based on the specified architecture, hidden units, and output units.
    """
    if arch == 'vgg13':
        model = models.vgg13(pretrained=True)
        input_units = model.classifier[0].in_features
    elif arch == 'resnet18':
        model = models.resnet18(pretrained=True)
        input_units = model.fc.in_features
    elif arch == 'densenet121':
        model = models.densenet121(pretrained=True)
        input_units = model.classifier.in_features
    else:
        raise ValueError("Unsupported architecture")

    # Freeze parameters so we don't backprop through them
    for param in model.parameters():
        param.requires_grad = False

    # Define the custom classifier
    classifier = nn.Sequential(
        nn.Linear(input_units, hidden_units),
        nn.ReLU(),
        nn.Dropout(0.2),
        nn.Linear(hidden_units, output_units),
        nn.LogSoftmax(dim=1)
    )

    # Replace the model's classifier with the custom classifier
    if arch == 'resnet18':
        model.fc = classifier
    elif arch == 'densenet121':
        model.classifier = classifier
    else:  # arch == 'vgg13'
        model.classifier = classifier

    return model

def main():
    parser = argparse.ArgumentParser(description="Train a new network on a dataset and save the model as a checkpoint")
    parser.add_argument('data_directory', type=str, help='Data directory')
    parser.add_argument('--save_dir', type=str, default='', help='Directory to save checkpoints')
    parser.add_argument('--arch', type=str, default='vgg13', choices=['vgg13', 'resnet18', 'densenet121'], help='Architecture')
    parser.add_argument('--learning_rate', type=float, default=0.01, help='Learning rate')
    parser.add_argument('--hidden_units', type=int, default=512, help='Hidden units')
    parser.add_argument('--epochs', type=int, default=20, help='Number of epochs')
    parser.add_argument('--gpu', action='store_true', help='Use GPU for training')
    args = parser.parse_args()

    # Data loading
    train_dir = args.data_directory + '/train'
    valid_dir = args.data_directory + '/valid'
    transform = transforms.Compose([
        transforms.RandomResizedCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
    train_data = datasets.ImageFolder(train_dir, transform=transform)
    valid_data = datasets.ImageFolder(valid_dir, transform=transform)
    trainloader = torch.utils.data.DataLoader(train_data, batch_size=64, shuffle=True)
    validloader = torch.utils.data.DataLoader(valid_data, batch_size=64)

    # Model setup
    model = build_model(args.arch, args.hidden_units, len(train_data.classes))
    criterion = nn.NLLLoss()
    optimizer = optim.Adam(model.classifier.parameters(), lr=args.learning_rate)

    # GPU usage, check if user choice is GPU and cuda is available
    device = torch.device("cuda" if args.gpu and torch.cuda.is_available() else "cpu")
    model.to(device)

    # Training loop
    for epoch in range(args.epochs):
        model.train()
        running_loss = 0
        for images, labels in trainloader:
            images, labels = images.to(device), labels.to(device)
            optimizer.zero_grad()
            log_ps = model(images)
            loss = criterion(log_ps, labels)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()

        # Validation loop
        model.eval()
        valid_loss = 0
        accuracy = 0
        with torch.no_grad():
            for images, labels in validloader:
                images, labels = images.to(device), labels.to(device)
                log_ps = model(images)
                valid_loss += criterion(log_ps, labels).item()
                ps = torch.exp(log_ps)
                top_p, top_class = ps.topk(1, dim=1)
                equals = top_class == labels.view(*top_class.shape)
                accuracy += torch.mean(equals.type(torch.FloatTensor))

        print(f"Epoch {epoch+1}/{args.epochs}.. "
              f"Train loss: {running_loss/len(trainloader):.3f}.. "
              f"Validation loss: {valid_loss/len(validloader):.3f}.. "
              f"Validation accuracy: {accuracy/len(validloader):.3f}")

    # Save checkpoint
    checkpoint = {
        'arch': args.arch,
        'class_to_idx': train_data.class_to_idx,
        'state_dict': model.state_dict(),
        'hidden_units': args.hidden_units,
    }
    torch.save(checkpoint, args.save_dir + 'checkpoint.pth')

if __name__ == "__main__":
    main()
