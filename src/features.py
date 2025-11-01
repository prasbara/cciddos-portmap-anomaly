"""
Module for feature selection and preprocessing.
"""
import logging
from sklearn.preprocessing import StandardScaler
import numpy as np

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Selected features for anomaly detection
SELECTED_FEATURES = [
    ' Flow Duration',
    ' Total Fwd Packets',
    ' Total Backward Packets',
    'Total Length of Fwd Packets',
    ' Total Length of Bwd Packets',
    ' Flow IAT Mean',
    ' Flow IAT Std',
    ' Flow IAT Max',
    ' Fwd IAT Mean',
    ' Bwd IAT Mean',
    'Fwd Packets/s',
    ' Bwd Packets/s'
]

def select_features(df):
    """
    Select relevant features for anomaly detection.
    
    Args:
        df (pd.DataFrame): Input dataset
        
    Returns:
        pd.DataFrame: Dataset with selected features
    """
    logger.info("Selecting features for anomaly detection")
    
    # Verify all features are present
    missing_features = [f for f in SELECTED_FEATURES if f not in df.columns]
    if missing_features:
        raise ValueError(f"Missing features in dataset: {missing_features}")
    
    return df[SELECTED_FEATURES]

def normalize_features(X):
    """
    Normalize features using StandardScaler.
    
    Args:
        X (pd.DataFrame): Features to normalize
        
    Returns:
        np.array: Normalized features
    """
    logger.info("Normalizing features...")
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    logger.info("Features normalized successfully")
    return X_scaled

def prepare_features(df):
    """
    Main function to prepare features for anomaly detection.
    
    Args:
        df (pd.DataFrame): Input dataset
        
    Returns:
        tuple: (normalized features array, feature names)
    """
    # Select relevant features
    X = select_features(df)
    
    # Normalize features
    X_scaled = normalize_features(X)
    
    return X_scaled, SELECTED_FEATURES

if __name__ == "__main__":
    # Example usage
    import pandas as pd
    from parse_logs import load_dataset
    import os
    
    data_path = os.path.join("data", "CICDDoS2019_PortMap.csv")
    df = load_dataset(data_path)
    X_scaled, features = prepare_features(df)
    print(f"\nFeature statistics:\n{pd.DataFrame(X_scaled, columns=features).describe()}")