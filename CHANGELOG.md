# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2024-02-17

### Added
- Initial release of Air Quality Prediction project
- Multi-layer Perceptron (MLP) model for Benzene prediction
- Comprehensive data preprocessing pipeline
- Feature engineering with temporal features
- Domain-specific outlier treatment
- Model training with callbacks (EarlyStopping, ReduceLROnPlateau)
- Permutation feature importance analysis
- Extensive visualization tools
- Complete documentation (README, CONTRIBUTING, etc.)
- Unit tests for core functionality
- Jupyter notebook with full analysis
- Command-line interface for training and prediction

### Model Performance
- R² Score: 0.9940 (99.40% variance explained)
- MAE: 0.335 µg/m³
- RMSE: 0.518 µg/m³

### Documentation
- Comprehensive README with installation and usage instructions
- Contributing guidelines
- MIT License
- Data documentation
- Code examples and tutorials

### Technical Details
- TensorFlow/Keras based implementation
- 4 hidden layers with Batch Normalization
- Dropout regularization (0.3)
- Adam optimizer with learning rate scheduling
- 13,889 total parameters (13,409 trainable)

## [Unreleased]

### Planned Features
- [ ] LSTM/GRU models for time series prediction
- [ ] REST API for real-time predictions
- [ ] Web dashboard for visualization
- [ ] Mobile app integration
- [ ] Multi-pollutant prediction
- [ ] Transfer learning for different cities
- [ ] Real-time model monitoring
- [ ] Docker containerization
- [ ] CI/CD pipeline

### Improvements Under Consideration
- [ ] Hyperparameter optimization with Optuna
- [ ] Ensemble methods
- [ ] Attention mechanisms
- [ ] Explainability with SHAP
- [ ] Online learning capabilities

---

## Version History

### Legend
- **Added**: New features
- **Changed**: Changes in existing functionality  
- **Deprecated**: Soon-to-be removed features
- **Removed**: Removed features
- **Fixed**: Bug fixes
- **Security**: Security vulnerabilities

---

## How to Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on:
- Reporting bugs
- Suggesting enhancements
- Submitting pull requests

## Citation

If you use this work, please cite:

```bibtex
@misc{smartcity2024airquality,
  title={Air Quality Prediction for Smart Cities Using Artificial Neural Networks},
  author={Smart City Group},
  year={2024},
  institution={Universiti Teknologi Malaysia}
}
```
