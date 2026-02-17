# Data Directory

This directory contains the datasets used for air quality prediction.

## Directory Structure

```
data/
├── raw/                    # Original, immutable data
│   └── AirQualityUCI.xlsx # Main dataset
└── README.md              # This file
```

## Dataset Information

### Air Quality UCI Dataset

**Source**: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Air+Quality)

**Description**: 
- Contains hourly averaged responses from metal oxide chemical sensors
- Collected in a significantly polluted road area in an Italian city (Rome)
- Reference values from a certified air quality analyzer

**Size**: 9,357 instances × 15 attributes

**Time Period**: March 2004 - February 2005 (approximately 1 year)

**Attributes**:

1. **Date** (DD/MM/YYYY)
2. **Time** (HH:MM:SS)
3. **CO(GT)** - True hourly averaged CO concentration (mg/m³)
4. **PT08.S1(CO)** - Tin oxide sensor response (nominally CO targeted)
5. **NMHC(GT)** - True hourly averaged Non-Methane Hydrocarbons concentration (µg/m³)
6. **C6H6(GT)** - True hourly averaged Benzene concentration (µg/m³) **[TARGET VARIABLE]**
7. **PT08.S2(NMHC)** - Titania sensor response (nominally NMHC targeted)
8. **NOx(GT)** - True hourly averaged NOx concentration (ppb)
9. **PT08.S3(NOx)** - Tungsten oxide sensor response (nominally NOx targeted)
10. **NO2(GT)** - True hourly averaged NO2 concentration (µg/m³)
11. **PT08.S4(NO2)** - Tungsten oxide sensor response (nominally NO2 targeted)
12. **PT08.S5(O3)** - Indium oxide sensor response (nominally O3 targeted)
13. **T** - Temperature (°C)
14. **RH** - Relative Humidity (%)
15. **AH** - Absolute Humidity

**Missing Values**: 
- Missing values are tagged with -200 value in the original dataset
- Our preprocessing pipeline handles these appropriately

## Download Instructions

### Option 1: Manual Download

1. Visit: https://archive.ics.uci.edu/ml/datasets/Air+Quality
2. Download `AirQualityUCI.zip`
3. Extract and place `AirQualityUCI.xlsx` in `data/raw/`

### Option 2: Using Script

```bash
python scripts/download_data.py
```

## Data Processing

### Preprocessing Steps

Our data preprocessing pipeline includes:

1. **Loading**: Read Excel file with proper encoding
2. **Cleaning**: 
   - Remove missing values (tagged as -200)
   - Handle duplicates
   - Type conversion
3. **Outlier Treatment**:
   - Domain-specific outlier handling
   - Capping at 95th/99th percentile for certain features
   - Keeping pollution events (not removing all outliers)
4. **Feature Engineering**:
   - Temporal features (Hour, DayOfWeek, IsWeekend)
   - Interaction features (Temperature × Humidity)
5. **Normalization**: StandardScaler for all features
6. **Splitting**: 64% train, 16% validation, 20% test

### Usage

```python
from src.data_preprocessing import load_data, preprocess_data

# Load raw data
df = load_data('data/raw/AirQualityUCI.xlsx')

# Preprocess
df_clean = preprocess_data(df)

# The pipeline will save processed data to data/processed/
```

## Data Statistics

### Target Variable (C6H6 - Benzene)

- **Mean**: 9.78 µg/m³
- **Std**: 6.58 µg/m³
- **Min**: 0.14 µg/m³
- **Max**: 24.43 µg/m³ (after outlier treatment)
- **Range**: Varies from clean air to moderately polluted levels

### Distribution
- Right-skewed distribution
- Most values between 5-15 µg/m³
- Occasional pollution spikes

## Citation

If you use this dataset, please cite:

```bibtex
@article{devito2008field,
  title={On field calibration of an electronic nose for benzene estimation in an urban pollution monitoring scenario},
  author={De Vito, Saverio and Massera, Ettore and Piga, Maurizio and Martinotto, Luca and Di Francia, Girolamo},
  journal={Sensors and Actuators B: Chemical},
  volume={129},
  number={2},
  pages={750--757},
  year={2008},
  publisher={Elsevier}
}
```

## License

The dataset is available for research purposes. Please check the [UCI ML Repository](https://archive.ics.uci.edu/ml/datasets/Air+Quality) for specific licensing terms.

## Notes

- **Do not commit large data files** to Git (they're in .gitignore)
- Keep raw data immutable - never modify files in `raw/`
- Document any new data sources or modifications
- Processed data can be regenerated from raw data using the preprocessing pipeline

## Data Privacy

This dataset contains:
- ✅ Aggregated sensor readings (no PII)
- ✅ Environmental measurements (public information)
- ✅ No personally identifiable information
- ✅ No sensitive or confidential data

Safe for public repositories and research use.
