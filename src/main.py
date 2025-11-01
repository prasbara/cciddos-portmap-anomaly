"""
Main pipeline for DDoS PortMap anomaly detection.
"""
import logging
import os
from src.parse_logs import load_dataset
from src.features import prepare_features
from src.detect import detect_anomalies
from src.visualize import plot_anomaly_scores, create_anomaly_summary

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    """
    Run the complete anomaly detection pipeline.
    """
    # Set paths
    data_path = os.path.join("data", "CICDDoS2019_PortMap.csv")
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    
    # 1. Load and clean data
    logger.info("Starting anomaly detection pipeline...")
    df = load_dataset(data_path)
    
    # 2. Prepare features
    X_scaled, features = prepare_features(df)
    
    # 3. Detect anomalies
    labels, scores = detect_anomalies(X_scaled)
    
    # 4. Visualize results
    plot_path = os.path.join(output_dir, "anomaly_hist.png")
    plot_anomaly_scores(scores, labels, plot_path)
    
    # 5. Create and save anomaly summary
    summary = create_anomaly_summary(df, labels, scores)
    alerts_path = os.path.join(output_dir, "alerts.csv")
    summary.to_csv(alerts_path, index=False)
    
    # 6. Print summary statistics
    n_anomalies = sum(labels == -1)
    logger.info(f"\nAnalysis complete:")
    logger.info(f"- Processed {len(df)} network flows")
    logger.info(f"- Detected {n_anomalies} potential DDoS PortMap attacks")
    logger.info(f"- Anomaly rate: {(n_anomalies/len(df))*100:.2f}%")
    logger.info(f"- Results saved to {output_dir}/")

if __name__ == "__main__":
    main()