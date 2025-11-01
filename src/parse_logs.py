"""
Module for loading and cleaning the CICDDoS2019 PortMap dataset.
"""
import logging
import pandas as pd
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def load_dataset(file_path):
    """
    Load the CICDDoS2019 PortMap CSV dataset.
    
    Args:
        file_path (str): Path to the CSV file
        
    Returns:
        pd.DataFrame: Cleaned dataset
    """
    logger.info(f"Loading dataset from {file_path}")
    
    try:
        df = pd.read_csv(file_path)
        logger.info(f"Loaded {len(df)} rows of data")
        return clean_dataset(df)
    except Exception as e:
        logger.error(f"Error loading dataset: {str(e)}")
        raise

def clean_dataset(df):
    """
    Clean and preprocess the dataset.
    
    Args:
        df (pd.DataFrame): Raw dataset
        
    Returns:
        pd.DataFrame: Cleaned dataset
    """
    logger.info("Cleaning dataset...")
    
    # Remove rows with missing values
    df = df.dropna()
    
    # Remove duplicate rows
    df = df.drop_duplicates()
    
    # Convert timestamp column if present
    if 'Timestamp' in df.columns:
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    
    # Convert infinity values to large numbers
    df = df.replace([float('inf'), float('-inf')], float('1e6'))
    
    logger.info(f"Dataset cleaned. Final shape: {df.shape}")
    return df

if __name__ == "__main__":
    # Example usage
    data_path = os.path.join("data", "CICDDoS2019_PortMap.csv")
    df = load_dataset(data_path)
    print(f"Dataset shape: {df.shape}")
    print("\nColumns:", df.columns.tolist())