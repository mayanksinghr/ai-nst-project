import urllib.request
import os

model_path = "vgg_normalised.pth"
if not os.path.exists(model_path):
    print("Downloading VGG model...")
    urllib.request.urlretrieve(
        "https://download.pytorch.org/models/vgg19-dcbb9e9d.pth",
        model_path
    )
    print("Done!")
else:
    print("Model already exists.")