# Deep Learning - Exercises

## Setup First! 🔧

```bash
pip install tensorflow numpy matplotlib scikit-learn
```

---

## Exercise 1: Build Your First Neural Network ⭐
**Goal**: Create a simple feedforward neural network

Build a neural network to classify the Wine dataset.

**Tasks**:
1. Load wine dataset from sklearn
2. Create a 3-layer neural network
3. Use ReLU activation in hidden layers
4. Use softmax for output
5. Train for 50 epochs
6. Achieve >90% accuracy

**Hints**:
- Input: 13 features
- Output: 3 classes
- Try: [13] → [16] → [8] → [3]

---

## Exercise 2: Hyperparameter Tuning ⭐⭐
**Goal**: Find the best model configuration

Using the same Wine dataset, experiment with:

**Tasks**:
1. Try different architectures:
   - Shallow: 1 hidden layer
   - Medium: 2-3 hidden layers
   - Deep: 4+ hidden layers
2. Try different activations (relu, tanh)
3. Try different optimizers (adam, sgd, rmsprop)
4. Try different batch sizes (16, 32, 64, 128)
5. Plot learning curves for each
6. Report best configuration

---

## Exercise 3: Regularization Techniques ⭐⭐
**Goal**: Prevent overfitting

Create an overfitting scenario and fix it.

**Tasks**:
1. Create a complex network (5+ layers, 256+ neurons)
2. Train on small dataset (use 20% of data)
3. Observe overfitting (train acc >> val acc)
4. Apply fixes one by one:
   - Dropout (try 0.2, 0.3, 0.5)
   - L2 regularization
   - Early stopping
   - Data augmentation
5. Compare results

---

## Exercise 4: CNN for Fashion MNIST ⭐⭐
**Goal**: Build a convolutional neural network

Classify clothing items from Fashion MNIST.

**Tasks**:
1. Load Fashion MNIST dataset
2. Build CNN with:
   - 2-3 Conv2D layers
   - MaxPooling after each Conv layer
   - Flatten
   - Dense layers
   - Dropout
3. Use data augmentation
4. Achieve >88% test accuracy
5. Visualize some predictions
6. Show confusion matrix

**Architecture Example**:
```
Conv2D(32) → MaxPool → Conv2D(64) → MaxPool → 
Flatten → Dense(128) → Dropout → Dense(10)
```

---

## Exercise 5: Transfer Learning ⭐⭐⭐
**Goal**: Use pre-trained models

Use a pre-trained model for custom classification.

**Tasks**:
1. Choose a pre-trained model (MobileNetV2, ResNet50, or VGG16)
2. Download Cats vs Dogs dataset or use your own images
3. Freeze base model layers
4. Add custom top layers
5. Train only top layers
6. Fine-tune: unfreeze some layers, train with low LR
7. Compare frozen vs fine-tuned performance

**Expected Results**:
- Frozen: ~85-90% accuracy
- Fine-tuned: ~90-95% accuracy

---

## Exercise 6: Image Classification from Scratch ⭐⭐⭐
**Goal**: Build a complete image classifier

Create a CNN for CIFAR-10 dataset.

**Tasks**:
1. Load and explore CIFAR-10
2. Implement data augmentation:
   - Random flips
   - Random rotations
   - Random crops
   - Color jittering
3. Build CNN architecture
4. Use batch normalization
5. Implement learning rate scheduling
6. Use callbacks (early stopping, model checkpoint)
7. Achieve >75% test accuracy
8. Visualize:
   - Training history
   - Sample predictions
   - Misclassified examples

---

## Exercise 7: RNN for Text Generation ⭐⭐⭐
**Goal**: Generate text character-by-character

Build a character-level RNN.

**Tasks**:
1. Use a text corpus (Shakespeare, your favorite book)
2. Preprocess: create character mappings
3. Create sequences of length 100
4. Build LSTM model:
   - Embedding layer
   - LSTM layers (1-2)
   - Dense output
5. Train the model
6. Generate new text with different temperatures (0.5, 1.0, 1.5)
7. Compare creativity vs coherence

---

## Exercise 8: Sentiment Analysis ⭐⭐⭐
**Goal**: Classify movie reviews

Build LSTM for IMDB sentiment classification.

**Tasks**:
1. Load IMDB dataset
2. Pad sequences to same length
3. Try different architectures:
   - Simple RNN
   - LSTM
   - Bidirectional LSTM
   - GRU
4. Compare performance
5. Add attention mechanism (bonus)
6. Achieve >85% accuracy
7. Test on custom reviews

---

## Exercise 9: Autoencoder for Anomaly Detection ⭐⭐⭐⭐
**Goal**: Detect anomalies using reconstruction error

**Tasks**:
1. Use MNIST dataset
2. Train autoencoder on normal digits (0-8)
3. Test reconstruction error on:
   - Normal digits (0-8)
   - Anomaly digits (9)
4. Set threshold for anomaly detection
5. Calculate precision, recall, F1-score
6. Visualize:
   - Original vs reconstructed images
   - Reconstruction error distribution
7. Try variations:
   - Convolutional autoencoder
   - Variational autoencoder (VAE)

---

## Exercise 10: Multi-Task Learning ⭐⭐⭐⭐
**Goal**: One model, multiple tasks

Build a model that performs multiple tasks simultaneously.

**Example**: Age + Gender prediction from faces

**Tasks**:
1. Find or create dataset with multiple labels
2. Build model with:
   - Shared layers (feature extraction)
   - Task-specific heads
3. Use appropriate loss for each task
4. Combine losses (weighted sum)
5. Compare with separate models
6. Analyze if tasks help each other

---

## Exercise 11: GAN for Image Generation ⭐⭐⭐⭐⭐
**Goal**: Generate new images

Build a simple GAN.

**Tasks**:
1. Use MNIST or Fashion MNIST
2. Build Generator:
   - Input: random noise
   - Output: 28x28 image
3. Build Discriminator:
   - Input: 28x28 image
   - Output: real/fake probability
4. Implement training loop:
   - Train discriminator on real + fake
   - Train generator to fool discriminator
5. Generate images every epoch
6. Monitor convergence
7. Generate 16 sample images

**Challenge**: Try DCGAN (Deep Convolutional GAN)

---

## Exercise 12: Attention Mechanism ⭐⭐⭐⭐⭐
**Goal**: Implement attention from scratch

Build a sequence-to-sequence model with attention.

**Tasks**:
1. Create a simple translation task
2. Build encoder (LSTM)
3. Implement attention mechanism:
   - Calculate attention weights
   - Compute context vector
4. Build decoder with attention
5. Train and evaluate
6. Visualize attention weights
7. See what the model focuses on

---

## Challenge Projects 🚀

### Project 1: Image Captioning
- CNN for image features
- RNN for caption generation
- Combine both
- Generate captions for new images

### Project 2: Object Detection
- Use YOLO or Faster R-CNN
- Detect multiple objects
- Draw bounding boxes
- Calculate mAP metric

### Project 3: Style Transfer
- Load VGG19
- Extract style and content
- Optimize target image
- Transfer artistic style

### Project 4: Face Recognition
- Face detection
- Face embedding
- Similarity comparison
- Build face database

---

## Solutions Template

Create `my_solutions.py`:

```python
"""
Deep Learning - My Solutions
==============================
"""

import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

# Exercise 1
def exercise_1():
    """Build first neural network"""
    pass

# Exercise 2
def exercise_2():
    """Hyperparameter tuning"""
    pass

# ... continue for all exercises

if __name__ == "__main__":
    # Test your solutions
    pass
```

---

## Tips for Success 💡

1. **Start Small**: Test on small data first
2. **Monitor Training**: Watch loss curves
3. **Use Callbacks**: Early stopping, checkpoints
4. **Save Models**: Don't lose your trained models
5. **Visualize**: Plot everything
6. **GPU**: Use Colab if you don't have GPU
7. **Batch Size**: Larger = faster but needs more memory
8. **Learning Rate**: Most important hyperparameter

## Common Issues & Solutions

### Issue: Loss is NaN
- Lower learning rate
- Check data preprocessing
- Check for extreme values

### Issue: Model not learning
- Increase model capacity
- Check learning rate (too low?)
- Verify data is properly normalized

### Issue: Overfitting
- Add dropout
- Use regularization
- Get more data
- Data augmentation

### Issue: Training too slow
- Use GPU
- Increase batch size
- Reduce model size
- Use mixed precision

---

## Next Steps

After completing:
1. Move to `03_NLP_LLMs`
2. Work on Kaggle competitions
3. Read research papers
4. Implement papers from scratch
5. Build portfolio projects

## Resources

- TensorFlow Documentation
- PyTorch Tutorials
- Papers with Code
- Kaggle Datasets
- Google Colab
