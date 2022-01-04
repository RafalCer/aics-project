## 2022-01-04 


Pre-trained model for generating composites

Image --> Composite

Autoencoder

picture image --> abstraction --> composite image

What layer of abstraction? Currently using the final composite pixel image.





Model 1

Dataset 2: pictures and descriptions

Dataset 2+: composites (encoded with model pre-trained model), pictures and descriptions

Task: composite, picture --> description

composite --> dense-1 512

picture --> dense-2 512

concatenate dense-1 dense-2

attention on the concatenated layer and generate caption: bonus: what information is the attention layer using to generate caption, composite or image?

use code from the image captioning tutorial




