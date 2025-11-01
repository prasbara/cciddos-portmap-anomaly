"""
Module for anomaly detection using Isolation Forest.
"""
import logging
import numpy as np
from sklearn.ensemble import IsolationForest

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class AnomalyDetector:
    """
    Anomaly detector class using Isolation Forest algorithm.
    """
    def __init__(self, contamination=0.02, random_state=42):
        """
        Initialize the anomaly detector.
        
        Args:
            contamination (float): Expected proportion of anomalies
            random_state (int): Random seed for reproducibility
        """
        self.model = IsolationForest(
            contamination=contamination,
            random_state=random_state,
            n_estimators=100,
            max_samples='auto'
        )
        
    def fit_predict(self, X):
        """
        Fit the model and predict anomalies.
        
        Args:
            X (np.array): Normalized feature matrix
            
        Returns:
            tuple: (anomaly labels, anomaly scores)
        """
        logger.info("Training Isolation Forest model...")
        
        # Fit and predict
        labels = self.model.fit_predict(X)
        scores = self.model.score_samples(X)
        
        # Convert labels: -1 for anomalies, 1 for normal
        n_anomalies = np.sum(labels == -1)
        logger.info(f"Detected {n_anomalies} anomalies in {len(X)} samples")
        
        return labels, scores
    
    def get_anomaly_indices(self, labels):
        """
        Get indices of anomalous samples.
        
        Args:
            labels (np.array): Anomaly labels (-1 for anomalies, 1 for normal)
            
        Returns:
            np.array: Indices of anomalous samples
        """
        return np.where(labels == -1)[0]

def detect_anomalies(X):
    """
    Main function to detect anomalies in the dataset.
    
    Args:
        X (np.array): Normalized feature matrix
        
    Returns:
        tuple: (anomaly labels, anomaly scores)
    """
    detector = AnomalyDetector()
    return detector.fit_predict(X)

if __name__ == "__main__":
    # Example usage
    import pandas as pd
    from parse_logs import load_dataset
    from features import prepare_features
    import os
    
    data_path = os.path.join("data", "CICDDoS2019_PortMap.csv")
    df = load_dataset(data_path)
    X_scaled, features = prepare_features(df)
    
    labels, scores = detect_anomalies(X_scaled)
    print(f"\nNumber of anomalies: {np.sum(labels == -1)}")
    print(f"Anomaly rate: {np.mean(labels == -1):.3f}")