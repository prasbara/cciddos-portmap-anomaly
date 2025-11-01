"""
Unit tests for anomaly detection functionality.
"""
import unittest
import numpy as np
import pandas as pd
from src.detect import AnomalyDetector
from src.features import prepare_features

class TestAnomalyDetection(unittest.TestCase):
    def setUp(self):
        """
        Create a small dummy dataset for testing.
        """
        # Create dummy data with obvious anomalies
        np.random.seed(42)
        
        # Normal data points clustered together
        n_normal = 100
        normal_data = np.random.normal(loc=0, scale=1, size=(n_normal, 5))
        
        # Anomaly data points far from normal cluster
        n_anomalies = 2
        anomaly_data = np.random.normal(loc=10, scale=1, size=(n_anomalies, 5))
        
        # Combine data
        self.X = np.vstack([normal_data, anomaly_data])
        
        # Create dummy dataframe
        self.df = pd.DataFrame(
            self.X,
            columns=['Flow Duration', 'Total Fwd Packets', 'Flow IAT Mean', 
                    'Fwd Packets/s', 'Bwd Packets/s']
        )
    
    def test_anomaly_detection(self):
        """
        Test if anomaly detector can identify injected anomalies.
        """
        # Initialize detector with known contamination rate
        detector = AnomalyDetector(contamination=0.02)
        
        # Get predictions
        labels, scores = detector.fit_predict(self.X)
        
        # Check basic properties
        self.assertEqual(len(labels), len(self.X))
        self.assertEqual(len(scores), len(self.X))
        
        # Check if anomalies were detected
        n_anomalies = sum(labels == -1)
        self.assertTrue(0 < n_anomalies <= 3)  # Should detect 1-3 anomalies
        
        # Check if scores are normalized properly
        self.assertTrue(np.all(scores <= 0))  # Isolation Forest scores are <= 0
    
    def test_feature_preparation(self):
        """
        Test feature preparation pipeline.
        """
        # Add required columns to match feature set
        for col in ['Total Backward Packets', 'Total Length of Fwd Packets',
                   'Total Length of Bwd Packets', 'Flow IAT Std', 'Flow IAT Max',
                   'Fwd IAT Mean', 'Bwd IAT Mean']:
            self.df[col] = np.random.normal(size=len(self.df))
        
        # Prepare features
        X_scaled, features = prepare_features(self.df)
        
        # Check output properties
        self.assertEqual(X_scaled.shape[0], len(self.df))
        self.assertTrue(np.allclose(X_scaled.mean(axis=0), 0, atol=1e-10))
        self.assertTrue(np.allclose(X_scaled.std(axis=0), 1, atol=1e-10))

if __name__ == '__main__':
    unittest.main()