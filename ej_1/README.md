# Dependencies
```
pip install -r requirements.txt
```

## Labelmap
![Screenshot from 2022-07-21 15-37-21](https://user-images.githubusercontent.com/35694200/180310785-ea4514b7-7dee-4c8d-8ad6-e58298bb685c.png)

## How to use
```
python3 example.py
```

## Example
```
➜ python3 example.py                    

- loading images...
- images: (10000, 28, 28)
- labels: (10000,)

- running prediction
313/313 [==============================] - 1s 2ms/step

- confusion matrix and classification report
              precision    recall  f1-score   support

 T-shirt/top       0.10      0.09      0.09      1000
     Trouser       0.10      0.10      0.10      1000
    Pullover       0.10      0.09      0.09      1000
       Dress       0.10      0.10      0.10      1000
        coat       0.09      0.10      0.09      1000
      Sandal       0.11      0.10      0.10      1000
       Shirt       0.10      0.12      0.11      1000
     Sneaker       0.12      0.12      0.12      1000
         Bag       0.11      0.11      0.11      1000
  Ankle boot       0.09      0.08      0.08      1000

    accuracy                           0.10     10000
   macro avg       0.10      0.10      0.10     10000
weighted avg       0.10      0.10      0.10     10000
```

## Prediction
<p align="center">
  <img src="https://user-images.githubusercontent.com/35694200/180327482-830e945c-08e3-417c-ab7e-53e2628d0508.png" />
</p>

## Classification report
<p align="center">
  <img src="https://user-images.githubusercontent.com/35694200/180327491-e3abfb12-f3b4-4e7e-b92c-28e924dd83b1.png" />
</p>
