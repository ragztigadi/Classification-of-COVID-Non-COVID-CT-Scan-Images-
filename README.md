# Classification of COVID & Non-COVID CT Scan Images

This project aims to classify CT scan images as either COVID or Non-COVID using machine learning models. It leverages transfer learning with pretrained models to enhance classification accuracy.

## Project Structure

- **covid19_dataset.ipynb**: Handles data loading, visualization, and preprocessing of CT scan images.
- **covid19_training_etc.ipynb**: Main notebook for training the model on COVID and Non-COVID images.
- **covid19_inference_with_pretrained.ipynb**: Inference notebook to test the trained model on new images.
- **run.py**: Script for batch predictions using the trained model.
- **README.md**: Project overview and setup instructions.

## Dataset

The dataset comprises labeled CT scan images stored in folders named `COVID` and `Non-COVID`. Organize it as follows:
```

dataset/
├── COVID/
│ ├── image1.png
│ ├── image2.png
│ └── ...
└── Non-COVID/
├── image1.png
├── image2.png
└── ...

````

## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ragztigadi/Classification-of-COVID-Non-COVID-CT-Scan-Images-.git
   cd Classification-of-COVID-Non-COVID-CT-Scan-Images-
````

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run training and inference**:
   Use Jupyter Notebook to open and execute `covid19_training_etc.ipynb` (for training) or `covid19_inference_with_pretrained.ipynb` (for testing).

4. **Run batch predictions**:
   ```bash
   python run.py --input_folder path/to/ct_images
   ```

## Results

The trained model is evaluated on accuracy and loss metrics. Key results are visualized in the training notebook.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

```

This README provides an overview, setup steps, and instructions for using your code. Let me know if you need further customization!
```
