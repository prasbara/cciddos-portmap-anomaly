# DDoS PortMap Anomaly Detection

This project implements an anomaly detection system for DDoS PortMap attacks using the Isolation Forest algorithm. It processes the CICDDoS2019 dataset to identify potential DDoS attacks based on network traffic patterns.

## Project Structure

```
cciddos-portmap-anomaly/
├─ data/              # Dataset directory
├─ notebooks/         # Jupyter notebooks for analysis
├─ src/              # Source code
├─ tests/            # Unit tests
```

## Setup and Installation

1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Place the CICDDoS2019 PortMap CSV file in the `data/` directory

## Usage

Run the main detection pipeline:
```
python -m src.main
```

## Outputs

The pipeline generates two main outputs:

1. `alerts.csv`: Contains detected anomalies with timestamps and scores
2. `anomaly_hist.png`: Visualization of anomaly score distribution

## Model Details

- Algorithm: Isolation Forest
- Configuration: 
  - contamination=0.02 (expected 2% anomaly rate)
  - random_state=42 (for reproducibility)
- Features used: Flow duration, packet counts, IAT statistics, etc.

## Dataset

This project uses the CICDDoS2019 dataset (PortMap subset):
[Canadian Institute for Cybersecurity DDoS2019](https://www.unb.ca/cic/datasets/ddos-2019.html)

## License

MIT License