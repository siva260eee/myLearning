"""
Deep Learning - Examples
=========================
Neural networks with TensorFlow/Keras
"""

# ============================================================================
# EXAMPLE 1: Simple Neural Network
# ============================================================================
def example_simple_nn():
    """Basic neural network for classification"""
    import tensorflow as tf
    from tensorflow import keras
    from sklearn.datasets import make_classification
    from sklearn.model_selection import train_test_split
    import numpy as np
    
    # Generate sample data
    X, y = make_classification(n_samples=1000, n_features=20, n_classes=2, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Build model
    model = keras.Sequential([
        keras.layers.Dense(64, activation='relu', input_shape=(20,)),
        keras.layers.Dense(32, activation='relu'),
        keras.layers.Dense(1, activation='sigmoid')
    ])
    
    # Compile
    model.compile(
        optimizer='adam',
        loss='binary_crossentropy',
        metrics=['accuracy']
    )
    
    # Train
    history = model.fit(
        X_train, y_train,
        epochs=50,
        batch_size=32,
        validation_split=0.2,
        verbose=0
    )
    
    # Evaluate
    test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)
    
    print(f"Test Accuracy: {test_acc:.4f}")
    print(f"Model Summary:")
    model.summary()


# ============================================================================
# EXAMPLE 2: Multi-Class Classification
# ============================================================================
def example_multiclass():
    """Neural network for iris classification"""
    import tensorflow as tf
    from tensorflow import keras
    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    
    # Load data
    iris = load_iris()
    X, y = iris.data, iris.target
    
    # Preprocess
    scaler = StandardScaler()
    X = scaler.fit_transform(X)
    
    # Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Build model
    model = keras.Sequential([
        keras.layers.Dense(16, activation='relu', input_shape=(4,)),
        keras.layers.Dense(8, activation='relu'),
        keras.layers.Dense(3, activation='softmax')  # 3 classes
    ])
    
    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    
    # Train
    history = model.fit(
        X_train, y_train,
        epochs=100,
        batch_size=16,
        validation_data=(X_test, y_test),
        verbose=0
    )
    
    # Evaluate
    test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)
    print(f"Test Accuracy: {test_acc:.4f}")
    
    # Predict
    predictions = model.predict(X_test[:5])
    print("\nSample predictions:")
    for i, pred in enumerate(predictions):
        print(f"Sample {i+1}: {iris.target_names[pred.argmax()]} (confidence: {pred.max():.4f})")


# ============================================================================
# EXAMPLE 3: CNN for Image Classification (MNIST)
# ============================================================================
def example_cnn_mnist():
    """Convolutional Neural Network for digit recognition"""
    import tensorflow as tf
    from tensorflow import keras
    import numpy as np
    
    # Load MNIST dataset
    (X_train, y_train), (X_test, y_test) = keras.datasets.mnist.load_data()
    
    # Preprocess
    X_train = X_train.reshape(-1, 28, 28, 1).astype('float32') / 255
    X_test = X_test.reshape(-1, 28, 28, 1).astype('float32') / 255
    
    # Build CNN
    model = keras.Sequential([
        # First conv block
        keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
        keras.layers.MaxPooling2D((2, 2)),
        
        # Second conv block
        keras.layers.Conv2D(64, (3, 3), activation='relu'),
        keras.layers.MaxPooling2D((2, 2)),
        
        # Dense layers
        keras.layers.Flatten(),
        keras.layers.Dense(64, activation='relu'),
        keras.layers.Dropout(0.5),
        keras.layers.Dense(10, activation='softmax')
    ])
    
    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    
    print("Training CNN on MNIST...")
    history = model.fit(
        X_train, y_train,
        epochs=5,
        batch_size=128,
        validation_split=0.1,
        verbose=1
    )
    
    # Evaluate
    test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)
    print(f"\nTest Accuracy: {test_acc:.4f}")


# ============================================================================
# EXAMPLE 4: CNN with Data Augmentation (CIFAR-10)
# ============================================================================
def example_cnn_cifar10():
    """CNN with data augmentation for image classification"""
    import tensorflow as tf
    from tensorflow import keras
    
    # Load CIFAR-10
    (X_train, y_train), (X_test, y_test) = keras.datasets.cifar10.load_data()
    
    # Normalize
    X_train = X_train.astype('float32') / 255
    X_test = X_test.astype('float32') / 255
    
    # Data augmentation
    data_augmentation = keras.Sequential([
        keras.layers.RandomFlip("horizontal"),
        keras.layers.RandomRotation(0.1),
        keras.layers.RandomZoom(0.1),
    ])
    
    # Build model
    model = keras.Sequential([
        data_augmentation,
        keras.layers.Conv2D(32, (3, 3), activation='relu', padding='same', input_shape=(32, 32, 3)),
        keras.layers.MaxPooling2D((2, 2)),
        keras.layers.Conv2D(64, (3, 3), activation='relu', padding='same'),
        keras.layers.MaxPooling2D((2, 2)),
        keras.layers.Conv2D(64, (3, 3), activation='relu', padding='same'),
        keras.layers.Flatten(),
        keras.layers.Dense(64, activation='relu'),
        keras.layers.Dropout(0.5),
        keras.layers.Dense(10, activation='softmax')
    ])
    
    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    
    print("Training CNN on CIFAR-10 with data augmentation...")
    history = model.fit(
        X_train, y_train,
        epochs=10,
        batch_size=64,
        validation_data=(X_test, y_test),
        verbose=1
    )
    
    test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)
    print(f"\nTest Accuracy: {test_acc:.4f}")


# ============================================================================
# EXAMPLE 5: Transfer Learning with Pre-trained Model
# ============================================================================
def example_transfer_learning():
    """Use pre-trained MobileNetV2 for image classification"""
    import tensorflow as tf
    from tensorflow import keras
    import numpy as np
    
    # Load pre-trained model (without top layer)
    base_model = keras.applications.MobileNetV2(
        input_shape=(224, 224, 3),
        include_top=False,
        weights='imagenet'
    )
    
    # Freeze base model
    base_model.trainable = False
    
    # Add custom layers
    model = keras.Sequential([
        base_model,
        keras.layers.GlobalAveragePooling2D(),
        keras.layers.Dense(128, activation='relu'),
        keras.layers.Dropout(0.5),
        keras.layers.Dense(10, activation='softmax')  # 10 classes
    ])
    
    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    
    print("Transfer Learning Model:")
    model.summary()
    
    print("\nNote: This model is ready for training with your custom dataset!")
    print("Base model is frozen, only top layers will be trained.")


# ============================================================================
# EXAMPLE 6: Simple RNN for Sequence Classification
# ============================================================================
def example_simple_rnn():
    """RNN for sentiment analysis"""
    import tensorflow as tf
    from tensorflow import keras
    import numpy as np
    
    # Generate dummy sequential data
    vocab_size = 1000
    max_length = 100
    num_samples = 1000
    
    X = np.random.randint(0, vocab_size, size=(num_samples, max_length))
    y = np.random.randint(0, 2, size=(num_samples,))
    
    # Build RNN model
    model = keras.Sequential([
        keras.layers.Embedding(vocab_size, 32, input_length=max_length),
        keras.layers.SimpleRNN(32, return_sequences=False),
        keras.layers.Dense(1, activation='sigmoid')
    ])
    
    model.compile(
        optimizer='adam',
        loss='binary_crossentropy',
        metrics=['accuracy']
    )
    
    print("Simple RNN Model:")
    model.summary()


# ============================================================================
# EXAMPLE 7: LSTM for Text Classification
# ============================================================================
def example_lstm():
    """LSTM network for sentiment classification"""
    import tensorflow as tf
    from tensorflow import keras
    
    # Load IMDB dataset
    max_features = 10000
    maxlen = 200
    
    print("Loading IMDB dataset...")
    (X_train, y_train), (X_test, y_test) = keras.datasets.imdb.load_data(num_words=max_features)
    
    # Pad sequences
    X_train = keras.preprocessing.sequence.pad_sequences(X_train, maxlen=maxlen)
    X_test = keras.preprocessing.sequence.pad_sequences(X_test, maxlen=maxlen)
    
    # Build LSTM model
    model = keras.Sequential([
        keras.layers.Embedding(max_features, 128),
        keras.layers.LSTM(64, dropout=0.2),
        keras.layers.Dense(1, activation='sigmoid')
    ])
    
    model.compile(
        optimizer='adam',
        loss='binary_crossentropy',
        metrics=['accuracy']
    )
    
    print("\nTraining LSTM on IMDB reviews...")
    history = model.fit(
        X_train, y_train,
        epochs=3,
        batch_size=128,
        validation_split=0.2,
        verbose=1
    )
    
    test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)
    print(f"\nTest Accuracy: {test_acc:.4f}")


# ============================================================================
# EXAMPLE 8: Autoencoder
# ============================================================================
def example_autoencoder():
    """Simple autoencoder for dimensionality reduction"""
    import tensorflow as tf
    from tensorflow import keras
    from sklearn.datasets import load_digits
    import matplotlib.pyplot as plt
    
    # Load digits dataset
    digits = load_digits()
    X = digits.data.astype('float32') / 16.0
    
    # Define encoding dimension
    encoding_dim = 8
    
    # Build encoder
    encoder = keras.Sequential([
        keras.layers.Dense(32, activation='relu', input_shape=(64,)),
        keras.layers.Dense(encoding_dim, activation='relu')
    ])
    
    # Build decoder
    decoder = keras.Sequential([
        keras.layers.Dense(32, activation='relu', input_shape=(encoding_dim,)),
        keras.layers.Dense(64, activation='sigmoid')
    ])
    
    # Full autoencoder
    autoencoder = keras.Sequential([encoder, decoder])
    
    autoencoder.compile(optimizer='adam', loss='mse')
    
    print("Training autoencoder...")
    history = autoencoder.fit(
        X, X,  # Input = Output for autoencoder
        epochs=50,
        batch_size=32,
        validation_split=0.2,
        verbose=0
    )
    
    # Test reconstruction
    encoded = encoder.predict(X[:5])
    decoded = decoder.predict(encoded)
    
    print(f"Original shape: {X.shape[1]}")
    print(f"Encoded shape: {encoding_dim}")
    print(f"Compression ratio: {X.shape[1] / encoding_dim:.1f}x")


# ============================================================================
# EXAMPLE 9: Callbacks and Model Checkpointing
# ============================================================================
def example_callbacks():
    """Using callbacks for better training"""
    import tensorflow as tf
    from tensorflow import keras
    from sklearn.datasets import make_classification
    from sklearn.model_selection import train_test_split
    
    # Generate data
    X, y = make_classification(n_samples=1000, n_features=20, random_state=42)
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2)
    
    # Build model
    model = keras.Sequential([
        keras.layers.Dense(64, activation='relu', input_shape=(20,)),
        keras.layers.Dense(32, activation='relu'),
        keras.layers.Dense(1, activation='sigmoid')
    ])
    
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    
    # Define callbacks
    callbacks = [
        # Save best model
        keras.callbacks.ModelCheckpoint(
            'best_model.keras',
            save_best_only=True,
            monitor='val_loss'
        ),
        
        # Early stopping
        keras.callbacks.EarlyStopping(
            monitor='val_loss',
            patience=10,
            restore_best_weights=True
        ),
        
        # Reduce learning rate
        keras.callbacks.ReduceLROnPlateau(
            monitor='val_loss',
            factor=0.5,
            patience=5
        )
    ]
    
    print("Training with callbacks...")
    history = model.fit(
        X_train, y_train,
        epochs=100,
        batch_size=32,
        validation_data=(X_val, y_val),
        callbacks=callbacks,
        verbose=0
    )
    
    print(f"Training stopped at epoch: {len(history.history['loss'])}")


# ============================================================================
# Main execution
# ============================================================================
if __name__ == "__main__":
    print("="*70)
    print("DEEP LEARNING - EXAMPLES")
    print("="*70)
    
    examples = [
        ("Simple Neural Network", example_simple_nn),
        ("Multi-Class Classification", example_multiclass),
        ("CNN on MNIST", example_cnn_mnist),
        ("CNN with Data Augmentation (CIFAR-10)", example_cnn_cifar10),
        ("Transfer Learning", example_transfer_learning),
        ("Simple RNN", example_simple_rnn),
        ("LSTM for Text", example_lstm),
        ("Autoencoder", example_autoencoder),
        ("Callbacks", example_callbacks)
    ]
    
    print("\nAvailable examples:")
    for i, (name, _) in enumerate(examples, 1):
        print(f"{i}. {name}")
    
    choice = input("\nEnter example number (or 'q' to quit): ").strip()
    
    if choice.isdigit() and 1 <= int(choice) <= len(examples):
        name, func = examples[int(choice) - 1]
        print(f"\n{'='*70}")
        print(f"Running: {name}")
        print('='*70)
        try:
            func()
        except Exception as e:
            print(f"Error: {e}")
            print("\nNote: Make sure you have TensorFlow installed:")
            print("pip install tensorflow")
    elif choice.lower() != 'q':
        print("Invalid choice!")
