# Deep Learning

## Overview
Deep Learning is a subset of Machine Learning based on artificial neural networks with multiple layers that can learn hierarchical representations of data.

## Core Concepts

### 1. Neural Networks Fundamentals

#### Artificial Neuron (Perceptron)
```
output = activation(Σ(weight_i × input_i) + bias)
```
- **Inputs**: Features from data
- **Weights**: Learnable parameters
- **Bias**: Offset term
- **Activation**: Non-linear function

#### Multi-Layer Perceptron (MLP)
- **Input Layer**: Receives data
- **Hidden Layers**: Extract features
- **Output Layer**: Makes predictions

### 2. Activation Functions

#### ReLU (Rectified Linear Unit)
```
f(x) = max(0, x)
```
- Most popular
- Solves vanishing gradient
- Fast computation

#### Sigmoid
```
f(x) = 1 / (1 + e^(-x))
```
- Output: (0, 1)
- Used in binary classification
- Can cause vanishing gradient

#### Tanh
```
f(x) = (e^x - e^(-x)) / (e^x + e^(-x))
```
- Output: (-1, 1)
- Zero-centered
- Better than sigmoid

#### Softmax
```
f(x_i) = e^(x_i) / Σ(e^(x_j))
```
- Multi-class classification
- Outputs probabilities
- Sum equals 1

### 3. Training Neural Networks

#### Forward Propagation
1. Input passes through layers
2. Apply weights and biases
3. Apply activation functions
4. Get output prediction

#### Backpropagation
1. Calculate loss/error
2. Compute gradients
3. Update weights
4. Repeat

#### Loss Functions

**Mean Squared Error (Regression)**
```
MSE = (1/n) × Σ(y_true - y_pred)²
```

**Binary Cross-Entropy (Binary Classification)**
```
BCE = -1/n × Σ(y × log(ŷ) + (1-y) × log(1-ŷ))
```

**Categorical Cross-Entropy (Multi-class)**
```
CCE = -Σ(y_true × log(y_pred))
```

#### Optimizers

**Stochastic Gradient Descent (SGD)**
- Simple and effective
- Can be slow
- May get stuck

**Adam (Adaptive Moment Estimation)**
- Most popular
- Adaptive learning rates
- Fast convergence

**RMSprop**
- Good for RNNs
- Adaptive learning

### 4. Convolutional Neural Networks (CNNs)

#### Why CNNs for Images?
- Spatial hierarchies
- Parameter sharing
- Translation invariance

#### Key Components

**Convolutional Layer**
- Apply filters/kernels
- Extract features (edges, shapes, patterns)
- Preserve spatial structure

**Pooling Layer**
- Reduce dimensions
- Max pooling: take maximum
- Average pooling: take average

**Fully Connected Layer**
- Final classification
- Connect all neurons

#### Popular CNN Architectures
- **LeNet**: Early CNN (digit recognition)
- **AlexNet**: ImageNet winner 2012
- **VGG**: Very deep networks
- **ResNet**: Skip connections (residual learning)
- **Inception**: Multi-scale features
- **EfficientNet**: Optimal scaling

### 5. Recurrent Neural Networks (RNNs)

#### Sequential Data
- Text, time series, audio
- Order matters
- Variable length inputs

#### RNN Architecture
- Hidden state carries information
- Processes one step at a time
- Shares weights across time

#### Problems with Basic RNNs
- Vanishing gradients
- Can't learn long-term dependencies
- Limited memory

#### LSTM (Long Short-Term Memory)
- Solves vanishing gradient
- Has memory cells
- Gates control information flow:
  - **Forget gate**: What to forget
  - **Input gate**: What to remember
  - **Output gate**: What to output

#### GRU (Gated Recurrent Unit)
- Simpler than LSTM
- Fewer parameters
- Often similar performance

### 6. Advanced Architectures

#### Autoencoders
- Unsupervised learning
- Encode → Compress → Decode
- Dimensionality reduction
- Anomaly detection

#### GANs (Generative Adversarial Networks)
- **Generator**: Creates fake data
- **Discriminator**: Detects fakes
- Compete against each other
- Generate realistic images, text, audio

#### Transformers
- Attention mechanism
- Parallel processing
- State-of-the-art for NLP
- Foundation for LLMs (GPT, BERT)

### 7. Training Techniques

#### Regularization

**Dropout**
- Randomly drop neurons during training
- Prevents overfitting
- Acts like ensemble

**L1/L2 Regularization**
- Add penalty to loss
- Discourage large weights

**Early Stopping**
- Stop when validation loss increases
- Prevent overfitting

**Data Augmentation**
- Create variations of training data
- Rotation, flipping, cropping
- Increase dataset size

#### Batch Normalization
- Normalize layer inputs
- Faster training
- Better generalization

#### Learning Rate Scheduling
- Reduce learning rate over time
- Start high, end low
- Better convergence

### 8. Transfer Learning

#### Concept
- Use pre-trained models
- Adapt to new tasks
- Less data needed

#### Approaches

**Feature Extraction**
- Freeze early layers
- Train only final layers
- Fast and effective

**Fine-Tuning**
- Unfreeze some layers
- Train with low learning rate
- Better accuracy

### 9. Common Frameworks

#### TensorFlow/Keras
- Google's framework
- Production-ready
- Large ecosystem

#### PyTorch
- Facebook's framework
- Research-friendly
- Dynamic graphs
- Most popular in research

#### JAX
- Google's new framework
- Fast and flexible
- Functional programming

### 10. Best Practices

#### Model Development
1. Start simple (baseline)
2. Increase complexity gradually
3. Monitor train/val loss
4. Use callbacks
5. Save best models

#### Debugging
- Check data shape
- Verify loss decreases
- Use small dataset first
- Visualize activations
- Check gradients

#### Hyperparameters to Tune
- Learning rate (most important)
- Batch size
- Number of layers
- Layer sizes
- Dropout rate
- Optimizer choice

## Hardware Considerations

### GPU vs CPU
- GPUs: 10-100x faster for deep learning
- Parallel processing
- Essential for large models

### Cloud Options
- Google Colab (free GPU)
- Kaggle Kernels (free GPU)
- AWS, Azure, GCP
- Lambda Labs

## Common Applications

### Computer Vision
- Image classification
- Object detection
- Segmentation
- Face recognition

### Natural Language Processing
- Text classification
- Sentiment analysis
- Machine translation
- Question answering

### Time Series
- Stock prediction
- Weather forecasting
- Anomaly detection

### Generative AI
- Image generation
- Text generation
- Music generation
- Video synthesis

## Next Steps

1. Install TensorFlow or PyTorch
2. Work through examples
3. Complete exercises
4. Build CNN for image classification
5. Experiment with transfer learning
6. Move to NLP and LLMs

## Resources

- Deep Learning Book (Goodfellow, Bengio, Courville)
- Fast.ai Course
- Stanford CS231n (CNNs)
- Stanford CS224n (NLP)
- PyTorch Tutorials
- TensorFlow Tutorials
