# Quick Start Guide

Get started with Air Quality Prediction in 5 minutes!

## Prerequisites

- Python 3.8 or higher
- pip package manager
- 2GB free disk space

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/air-quality-prediction.git
cd air-quality-prediction
```

### 2. Set Up Virtual Environment

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Quick Usage

### Jupyter Notebook 

1. **Start Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Open the notebook:**
   - Navigate to `notebooks/Air_Quality_Prediction.ipynb`
   - Run all cells (Cell → Run All)

3. **Explore the results:**
   - Data visualizations
   - Model training progress
   - Performance metrics

## Understanding the Output

### Training Output

```
Epoch 1/200
180/180 [==============================] - 2s 8ms/step - loss: 1.2345 - mae: 0.8912
Epoch 2/200
180/180 [==============================] - 1s 7ms/step - loss: 0.9876 - mae: 0.7654
...
```

**What this means:**
- `loss`: How far predictions are from actual values (lower is better)
- `mae`: Mean Absolute Error in µg/m³ (lower is better)

### Final Results

```
Test Set Metrics:
RMSE: 0.518269
MAE: 0.335010
R²: 0.993955
```

**Interpretation:**
- **RMSE (0.52)**: Typical prediction error is ~0.5 µg/m³
- **MAE (0.34)**: Average error is ~0.3 µg/m³
- **R² (0.99)**: Model explains 99% of variance - excellent!

## Next Steps

### Learn More

1. **Read the full README**: [README.md](README.md)
2. **Understand the methodology**: [docs/methodology.md](docs/methodology.md)
3. **Check the report**: [docs/report.pdf](docs/report.pdf)

### Improve Performance

- **More data**: Add more training data
- **Feature engineering**: Create new features
- **Hyperparameter tuning**: Optimize parameters
- **Ensemble methods**: Combine multiple models

### Deploy Your Model

- **Web API**: Create Flask/FastAPI endpoint
- **Mobile app**: Build with Flutter/React Native
- **Cloud deployment**: Deploy to AWS/GCP/Azure
- **Docker**: Containerize for easy deployment

## Getting Help

- **Documentation**: See [README.md](README.md)
- **Issues**: [GitHub Issues](https://github.com/yourusername/air-quality-prediction/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/air-quality-prediction/discussions)
- **Email**: your.email@example.com

## Tips for Best Results

1. **Data Quality**: Ensure your data is clean and complete
2. **Feature Selection**: Use domain knowledge to select relevant features
3. **Regular Evaluation**: Check performance on validation set regularly
4. **Experiment**: Try different architectures and hyperparameters
5. **Document**: Keep notes on what works and what doesn't

## Congratulations! 🎉

You're now ready to predict air quality with machine learning!

For more advanced usage, see:
- [Full Documentation](README.md)
- [Contributing Guidelines](CONTRIBUTING.md)
- [API Reference](docs/api.md)

---

**Happy Coding!** 💻🌍
