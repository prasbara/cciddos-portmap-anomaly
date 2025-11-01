readme: |
  <h1 align="center" id="title">🛰️ DDoS PortMap Anomaly Detection</h1>

  <p align="center">
    <img src="https://socialify.git.ci/prasbara/cciddos-portmap-anomaly/image?description=1&language=1&owner=1&stargazers=1&theme=Light" alt="project-banner">
  </p>

  <p align="center" id="description">
    Anomaly Detection System for DDoS PortMap Attacks using Isolation Forest — <b>because sometimes, packets lie.</b>
  </p>

  <p align="center">
    <img src="https://img.shields.io/badge/Made%20with-Python-blue?logo=python" alt="Python Badge">
    <img src="https://img.shields.io/badge/License-MIT-green" alt="License Badge">
    <img src="https://img.shields.io/badge/Status-Testing%20Iseng-orange" alt="Status Badge">
    <img src="https://img.shields.io/badge/Dataset-CICDDoS2019%20PortMap-yellow" alt="Dataset Badge">
    <img src="https://img.shields.io/badge/Model-Isolation%20Forest-purple" alt="Model Badge">
  </p>

  ---

  ## 📁 Project Structure
cciddos-portmap-anomaly/
├─ data/ # Dataset directory (put your CSVs here)
├─ notebooks/ # Jupyter notebooks for exploration
├─ src/ # Source code (the magic happens here)
├─ tests/ # Unit tests (because bugs are not anomalies)

---

## ⚙️ Setup & Installation
1. **Clone this repo:**
   ```bash
   git clone https://github.com/prasbara/cciddos-portmap-anomaly.git
   cd cciddos-portmap-anomaly
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Add your dataset:**
   Place the **CICDDoS2019 PortMap CSV file** inside the `data/` directory.  
   _(If you forget this step, expect errors more than anomalies.)_

---

## 🚀 Usage
Run the main anomaly detection pipeline:

python -m src.main
FileDescriptionalerts.csvDetected anomalies with timestamps and scoresanomaly_hist.pngHistogram showing anomaly score distribution

Model Details
ParameterValueAlgorithmIsolation ForestContamination0.02Random State42Features UsedFlow duration, packet counts, IAT statistics, etc.

Dataset
This project uses the CICDDoS2019 (PortMap subset) dataset from
Canadian Institute for Cybersecurity

Notes
This repository is for testing and educational purposes only.
Not recommended for production use.

License
MIT License © 2025
You are free to use and modify this project.

Credits
  <p align="center">
    <img src="https://img.shields.io/badge/love_you-from_apart-blue" alt="shields">
  </p>
  <p align="center">made by <b>@prasbara</b></p>
```
