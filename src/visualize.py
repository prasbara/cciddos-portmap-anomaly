"""
Module for visualizing anomaly detection results.
"""
import logging
import matplotlib.pyplot as plt
import numpy as np
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def plot_anomaly_scores(scores, labels, output_path="anomaly_hist.png"):
    """
    Plot histogram of anomaly scores with different colors for normal/anomaly.
    
    Args:
        scores (np.array): Anomaly scores from the model
        labels (np.array): Anomaly labels (-1 for anomalies, 1 for normal)
        output_path (str): Path to save the plot
    """
    logger.info("Plotting anomaly score distribution...")
    
    plt.figure(figsize=(10, 6))
    
    # Plot normal samples
    plt.hist(scores[labels == 1], bins=50, alpha=0.7, 
             label='Normal', color='blue', density=True)
    
    # Plot anomalous samples
    plt.hist(scores[labels == -1], bins=50, alpha=0.7,
             label='Anomaly', color='red', density=True)
    
    plt.title("Distribution of Anomaly Scores")
    plt.xlabel("Anomaly Score")
    plt.ylabel("Density")
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Save plot
    plt.savefig(output_path)
    logger.info(f"Plot saved to {output_path}")
    plt.close()

def create_anomaly_summary(df, labels, scores):
    """
    Create a summary of detected anomalies.
    
    Args:
        df (pd.DataFrame): Original dataset
        labels (np.array): Anomaly labels
        scores (np.array): Anomaly scores
        
    Returns:
        pd.DataFrame: Summary of anomalies
    """
    import pandas as pd
    
    logger.info("Creating anomaly summary...")
    
    # Create summary dataframe
    summary = pd.DataFrame({
        'Timestamp': df['Timestamp'] if 'Timestamp' in df.columns else range(len(df)),
        'Anomaly_Score': scores,
        'Is_Anomaly': labels == -1
    })
    
    # Add relevant features if available
    for feature in ['Source IP', 'Destination IP', 'Flow Duration']:
        if feature in df.columns:
            summary[feature] = df[feature]
    
    return summary

if __name__ == "__main__":
    # Example usage
    from parse_logs import load_dataset
    from features import prepare_features
    from detect import detect_anomalies
    
    data_path = os.path.join("data", "CICDDoS2019_PortMap.csv")
    df = load_dataset(data_path)
    X_scaled, features = prepare_features(df)
    labels, scores = detect_anomalies(X_scaled)
    
    # Plot results
    plot_anomaly_scores(scores, labels)
    
    # Create and display summary
    summary = create_anomaly_summary(df, labels, scores)
    print("\nAnomalies Summary:")
    print(summary[summary['Is_Anomaly']].head())