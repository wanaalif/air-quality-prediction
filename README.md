# Air Quality Prediction for Smart Cities 🌍

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange.svg)](https://www.tensorflow.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A machine learning project focused on predicting urban air quality, specifically Benzene (C6H6) concentrations, using Artificial Neural Networks (ANN). This project was developed as part of the Machine Learning course (SAIA 2113) at Universiti Teknologi Malaysia.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Dataset](#dataset)
- [Model Architecture](#model-architecture)
- [Results](#results)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributors](#contributors)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## 🎯 Overview

This project aims to predict urban air quality by analyzing hourly measurements of various air pollutants and meteorological data. The predictive model uses deep learning techniques to forecast Benzene concentrations, which is crucial for:

- **Smart City Development**: Real-time air quality monitoring
- **Public Health**: Early warning systems for pollution events
- **Urban Planning**: Data-driven environmental policy decisions
- **Traffic Management**: Pollution-aware traffic control

### Key Objectives

1. **Data Preprocessing**: Clean and prepare real-world sensor data
2. **Feature Engineering**: Extract temporal and environmental features
3. **Model Development**: Build and train an ANN for regression
4. **Performance Evaluation**: Achieve high accuracy with appropriate metrics
5. **Insights Generation**: Provide actionable environmental insights

## ✨ Features

- **Comprehensive Data Analysis**: Exploratory data analysis with visualization
- **Advanced Feature Engineering**: Temporal features (hour, day of week, weekend) and environmental interactions
- **Robust Outlier Treatment**: Domain-specific outlier handling for environmental data
- **Deep Learning Architecture**: Multi-layer perceptron with batch normalization and dropout
- **High Accuracy**: R² score of 0.9940, indicating 99.40% variance explained
- **Feature Importance Analysis**: Permutation importance to understand model decisions
- **Visualization Tools**: Training curves, residual plots, and prediction analysis

## 📊 Dataset

The project uses the **Air Quality UCI Dataset** from the UCI Machine Learning Repository:

- **Source**: Real-world sensor data from Rome, Italy
- **Size**: 9,357 hourly measurements
- **Duration**: Collected over significant period in a heavily polluted road environment
- **Features**: 15 variables including:
  - Pollutants: CO, NOx, NO₂, Benzene (C6H6), NMHC
  - Sensor readings: PT08.S1-S5 (metal oxide sensors)
  - Meteorological: Temperature, Relative Humidity, Absolute Humidity
  - Temporal: Date, Time

### Data Characteristics

- **No missing values**: Clean dataset with complete records
- **No duplicates**: All entries are unique
- **Real-world variability**: Captures actual pollution events and patterns

## 🏗️ Model Architecture

### Artificial Neural Network (ANN)

Our model is a **Multi-Layer Perceptron (MLP)** with the following architecture:

```
Input Layer (15 features)
    ↓
Dense Layer (128 units, ReLU) + Batch Normalization + Dropout (0.3)
    ↓
Dense Layer (64 units, ReLU) + Batch Normalization + Dropout (0.3)
    ↓
Dense Layer (32 units, ReLU) + Batch Normalization + Dropout (0.3)
    ↓
Dense Layer (16 units, ReLU) + Batch Normalization + Dropout (0.3)
    ↓
Output Layer (1 unit, Linear activation)
```

### Training Configuration

- **Optimizer**: Adam (learning rate: 0.001)
- **Loss Function**: Mean Squared Error (MSE)
- **Metrics**: Mean Absolute Error (MAE)
- **Epochs**: 200 (with early stopping)
- **Batch Size**: 32
- **Total Parameters**: 13,889 (13,409 trainable)

### Regularization Techniques

- **Batch Normalization**: Stabilizes learning and accelerates convergence
- **Dropout (0.3)**: Prevents overfitting by randomly disabling neurons
- **Early Stopping**: Monitors validation loss with patience of 20 epochs
- **Learning Rate Reduction**: Reduces LR by 50% if validation loss plateaus

## 📈 Results

### Model Performance (Test Set)

| Metric | Value | Interpretation |
|--------|-------|----------------|
| **MAE** | 0.335 μg/m³ | Average prediction error |
| **MSE** | 0.269 | Squared error measure |
| **RMSE** | 0.518 μg/m³ | Typical prediction error |
| **R² Score** | **0.9940** | **99.40% variance explained** |

### Key Findings

1. **Exceptional Accuracy**: The model explains nearly all variance in Benzene concentration
2. **Low Prediction Error**: Average deviation of only 0.34 μg/m³
3. **Feature Importance**: PT08.S2(NMHC) is the most influential predictor
4. **Stable Training**: Consistent learning curves with no overfitting

### Feature Importance Ranking

1. **PT08.S2(NMHC)** - 1.809 ± 0.055 (Dominant contributor)
2. **PT08.S4(NO₂)** - 0.0018 ± 0.0001
3. **NOx(GT)** - 0.0012 ± 0.0002
4. Other features contribute minimally

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- (Optional) Virtual environment tool (venv, conda)

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/air-quality-prediction.git
cd air-quality-prediction
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# Using venv
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Download Dataset

The dataset should be placed in the `data/` directory. You can download it from:
- [UCI Machine Learning Repository - Air Quality Data Set](https://archive.ics.uci.edu/ml/datasets/Air+Quality)

## 💻 Usage

### Quick Start - Jupyter Notebook

1. Launch Jupyter Notebook:
```bash
jupyter notebook
```

2. Open `notebooks/Air_Quality_Prediction.ipynb`

3. Run all cells to:
   - Load and explore the data
   - Train the model
   - Evaluate performance
   - Visualize results

## 📁 Project Structure

```
air-quality-prediction/
│
├── README.md                          # This file
├── LICENSE                            # MIT License
├── requirements.txt                   # Python dependencies
├── setup.py                          # Package setup file
├── .gitignore                        # Git ignore rules
│
├── data/                             # Data directory
│   ├── raw/                          # Original dataset
│   └── README.md                     # Data documentation
│
├── notebooks/                        # Jupyter notebooks
│   └── Air_Quality_Prediction.ipynb  # Main analysis notebook
│
└── docs/                             # Documentation
    └── report.pdf                    # Full project report
```

## 👥 Contributors

This project was developed by the **Smart City Group** for the Machine Learning course (SAIA 2113) at Universiti Teknologi Malaysia:

- **Wan Alif Danial Bin Wan Kamarulfarid** (A24AI0093)
- **Farin Batrisyia Binti Saipul Nizam** (A24AI0030)
- **Muhammad Danish Iqbal Bin Mohamad Hassan** (A24AI0052)

**Section**: 4  
**Lecturer**: Dr Adam Bin Mohd Khairuddin

### Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on:
- Reporting bugs
- Suggesting enhancements
- Submitting pull requests
- Code style guidelines

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Third-Party Licenses

- **Dataset**: UCI Machine Learning Repository (Citation required)
- **TensorFlow**: Apache License 2.0
- **Keras**: MIT License

## 🙏 Acknowledgments

### Academic Acknowledgment

We express our gratitude to:

- **Dr. Adam Bin Mohd Khairuddin**: For guidance and support throughout this project
- **Universiti Teknologi Malaysia**: For providing the educational environment and resources
- **Faculty of Artificial Intelligence**: For the Machine Learning course infrastructure

### Technical Acknowledgments

- **UCI Machine Learning Repository**: For providing the Air Quality dataset
- **TensorFlow/Keras Team**: For the deep learning framework
- **Open Source Community**: For the various libraries and tools used

### Research References

Key papers that influenced this work:

1. Kumar et al. (2015) - "The rise of low-cost sensing for managing air pollution in cities"
2. Baron & Saffell (2017) - "Amperometric Gas Sensors as a Low Cost Emerging Technology Platform"
3. Apostolopoulos et al. (2023) - "Field Calibration of Low-Cost Air Quality Monitoring Devices"

Full references available in [docs/report.pdf](docs/report.pdf).

## 📞 Contact

For questions, suggestions, or collaborations:

- **Project Repository**: [GitHub Issues](https://github.com/yourusername/air-quality-prediction/issues)
- **Email**: [wanalifdanial03@gmail.com](mailto:wanalifdanial03@gmail,.com)

## 🔮 Future Work

Potential enhancements for this project:

1. **Real-time Deployment**: Deploy as a web service for live predictions
2. **Time Series Models**: Explore LSTM/GRU for temporal patterns
3. **Multi-pollutant Prediction**: Extend to predict multiple pollutants simultaneously
4. **Transfer Learning**: Adapt model to different geographical locations
5. **Mobile Application**: Develop citizen-facing air quality app
6. **IoT Integration**: Connect with real sensor networks

## 📊 Citation

If you use this work in your research, please cite:

```bibtex
@misc{smartcity2024airquality,
  title={Air Quality Prediction for Smart Cities Using Artificial Neural Networks},
  author={Wan Kamarulfarid, Wan Alif Danial and Saipul Nizam, Farin Batrisyia and Mohamad Hassan, Muhammad Danish Iqbal},
  year={2024},
  institution={Universiti Teknologi Malaysia},
  howpublished={\url{https://github.com/wanaalif/air-quality-prediction}}
}
```

---

**Made with ❤️ for a cleaner, smarter future**

*Last updated: February 2026*
