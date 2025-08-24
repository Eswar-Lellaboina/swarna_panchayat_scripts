# Swarna Panchayat Automation Scripts

This repository contains automation scripts designed to update household information in the Swarna Panchayat application. The scripts automate the process of populating various tabs with property and tax assessment data.

## 🏗️ Repository Structure

### Core Scripts
- **`tab1.py`** - Property Details Population (First Tab)
- **`tab2.py`** - Owner Details Population (Second Tab) 
- **`tab3.py`** - Floor Details Population (Third Tab)
- **`tab4.py`** - Tax Demand Details Population (Fourth Tab)
- **`enroll_assesment_adjustment.py`** - Assessment Adjustment and Arrears Update

### Configuration
- **`constants.py`** - API configuration and constants

### Data Files
- **`TAB1.xlsx`** - Property details data for Tab 1
- **`FINAL TAB2.xlsx`** - Owner details data for Tab 2
- **`Pedapalem HT 2024-25 (1) (2).xlsx`** - Floor and tax data for Tabs 3 & 4
- **`TAB4.xlsx`** - Tax demand data for Tab 4
- **`ARREAR FILE TAB4.xlsx`** - Arrears data for tax calculations

## 🚀 Script Execution Order

The scripts should be executed in the following sequence to ensure proper data flow:

1. **Tab 1** → Property basic information and site details
2. **Tab 2** → Owner and occupant details
3. **Tab 3** → Building floor details and construction information
4. **Tab 4** → Tax assessment and demand details
5. **Assessment Adjustment** → Updates arrears and adjusts assessment data (can be run independently when needed)

## 📋 Script Details

### Tab 1 - Property Details (`tab1.py`)
- Populates basic property information
- Sets property boundaries (East, West, North, South)
- Configures property type and land use
- Sets up basic facility information

**Data Source**: `TAB1.xlsx`
**API Endpoint**: `/prtntmapi/insert-prptydetails`

### Tab 2 - Owner Details (`tab2.py`)
- Adds property owner information
- Sets up occupant details
- Configures relationship types and addresses

**Data Source**: `FINAL TAB2.xlsx`
**API Endpoint**: `/prtntmapi/insert-ownerdetails`

### Tab 3 - Floor Details (`tab3.py`)
- Populates building construction details
- Sets floor dimensions and areas
- Configures building classification and rates

**Data Source**: `Pedapalem HT 2024-25 (1) (2).xlsx`
**API Endpoint**: `/prtntmapi/insert-floordetails`

### Tab 4 - Tax Demand (`tab4.py`)
- Sets up tax assessment details
- Configures various tax components (House Tax, Water Tax, etc.)
- Sets financial year-wise tax demands

**Data Source**: `Pedapalem HT 2024-25 (1) (2).xlsx`
**API Endpoint**: `/prtntmapi/insert-demanddetails`

### Assessment Adjustment (`enroll_assesment_adjustment.py`)
- **Primary Purpose**: Updates arrears and adjusts assessment data
- Corrects and adjusts assessment data
- Handles arrear calculations for multiple financial years
- Updates tax components and demand details
- Provides data validation and error handling
- **Use Case**: This script is used to update historical arrears and correct assessment data

**Data Sources**: `TAB4.xlsx`, `ARREAR FILE TAB4.xlsx`
**API Endpoint**: `/prtntmapi/insert-demanddetails`

## ⚙️ Configuration

Before running the scripts, update `constants.py` with your specific values:

```python
headers = {"Authorization": "Bearer $TOKEN", "Content-Type": "application/json"}
user_id = "your_user_id"
panch_secretariat_id = your_panchayat_id
village_id = your_village_id
habitation = "your_habitation_name"
property_street = "your_street_name"
property_pincode = "your_pincode"
```

## 🔧 Prerequisites

- Python 3.6+
- Required packages: `requests`, `pandas`, `openpyxl`
- Valid API access token for Swarna Panchayat application
- Excel files with proper data structure

## 📦 Installation

```bash
# Clone the repository
git clone <repository-url>
cd swarna_panchayat_scripts

# Install required packages
pip install requests pandas openpyxl
```

## 🚀 Usage

1. **Configure constants**: Update `constants.py` with your API credentials
2. **Prepare data**: Ensure Excel files contain required data in correct format
3. **Execute scripts**: Run scripts in sequence from Tab 1 to Tab 4
4. **Monitor execution**: Check console output for any errors or retries
5. **Verify data**: Validate populated data in the Swarna Panchayat application

## ⚠️ Important Notes

- Scripts include retry mechanisms for API failures
- Random data generation is used for some fields (building ages, dimensions)
- Assessment numbers are filtered for specific ranges (400-500 in some scripts)
- All scripts include error handling and logging
- API rate limiting is handled with sleep intervals

## 🐛 Troubleshooting

- **API Errors**: Check authentication token and API endpoint availability
- **Data Mismatches**: Verify Excel file structure matches script expectations
- **Retry Failures**: Check network connectivity and API response codes
- **Missing Data**: Ensure all required Excel files are present and accessible

## 📊 Data Flow

```
Excel Files → Script Processing → API Calls → Swarna Panchayat App
     ↓              ↓              ↓              ↓
  TAB1.xlsx →   tab1.py   →  Property API →  Tab 1 Data
FINAL TAB2.xlsx → tab2.py →  Owner API →  Tab 2 Data
Pedapalem HT → tab3.py →  Floor API →  Tab 3 Data
Pedapalem HT → tab4.py →  Tax API →  Tab 4 Data
```

## 🤝 Contributing

When contributing to this repository:
- Maintain the existing script structure
- Update documentation for any new features
- Test scripts with sample data before committing
- Follow the established naming conventions

## 📄 License

This project is intended for internal use by Swarna Panchayat administration.

---

## ⚠️ **IMPORTANT LEGAL DISCLAIMER**

**EDUCATIONAL PURPOSE ONLY**: These automation scripts are created **solely for educational and learning purposes**. They are **NOT authorized** for use in automating the Swarna Panchayat government service web application or any other government systems.

**NO PRODUCTION USE**: These scripts should **NEVER be used** in production environments, government systems, or to automate official government services without proper authorization.

**LEGAL COMPLIANCE**: Users are responsible for ensuring compliance with all applicable laws, regulations, and government policies. Unauthorized automation of government services may violate legal requirements.

**USE AT YOUR OWN RISK**: The authors and contributors are not responsible for any legal consequences, damages, or issues arising from the use of these scripts.

**📋 For complete legal terms, see [LEGAL_DISCLAIMER.md](LEGAL_DISCLAIMER.md)**

---

**Note**: These scripts are designed for specific use cases within the Swarna Panchayat system. Ensure proper testing and validation before using in production environments.
