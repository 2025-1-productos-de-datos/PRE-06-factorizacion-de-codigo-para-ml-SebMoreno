import os
import pickle


def save_model(model, save_path="models/estimator.pkl"):
    """Save the model to the specified path."""
    os.makedirs("models", exist_ok=True)
    with open(save_path, "wb") as file:
        pickle.dump(model, file)
