# Project Structure Documentation

## 📁 File Organization

### 🐍 Python Scripts
```
├── tab1.py                           # Property details population script
├── tab2.py                           # Owner details population script  
├── tab3.py                           # Floor details population script
├── tab4.py                           # Tax demand details population script
├── enroll_assesment_adjustment.py    # Assessment adjustment and arrears update script
├── constants.py                      # Configuration constants and API settings
└── requirements.txt                  # Python dependencies
```

### 📊 Data Files (Excel)
```
├── TAB1.xlsx                         # Property data for Tab 1
├── FINAL TAB2.xlsx                   # Owner data for Tab 2
├── Pedapalem HT 2024-25 (1) (2).xlsx # Floor and tax data for Tabs 3 & 4
├── TAB4.xlsx                         # Tax demand data for Tab 4
├── ARREAR FILE TAB4.xlsx             # Arrears data for tax calculations
├── 42 COLUMN DATA LATEST (2).xlsx    # Additional data file (unused)
├── FINAL_BOOK2.xlsx                  # Additional data file (unused)
├── FINAL_BOOK2_l.xlsx                # Additional data file (unused)
└── Book2.xlsx                        # Additional data file (unused)
```

### 📚 Documentation
```
├── README.md                         # Main project documentation
└── PROJECT_STRUCTURE.md              # This file - detailed structure
```

## ⚠️ File Naming Issues Identified

### 1. Inconsistent Excel File Naming
- **Current**: `Pedapalem HT 2024-25 (1) (2).xlsx` (contains spaces and special characters)
- **Recommended**: `pedapalem_ht_2024_25.xlsx` (use underscores, no spaces)

### 2. Unused Data Files
Several Excel files appear to be unused by the current scripts:
- `42 COLUMN DATA LATEST (2).xlsx`
- `FINAL_BOOK2.xlsx`
- `FINAL_BOOK2_l.xlsx`
- `Book2.xlsx`

### 3. Script File Naming
The script files are well-named and follow a consistent pattern:
- `tab1.py`, `tab2.py`, `tab3.py`, `tab4.py` ✅
- `enroll_assment_adjustment.py` ✅

## 🔄 Data Flow Between Files

### Tab 1 Data Flow
```
TAB1.xlsx → tab1.py → Property API
     ↓           ↓         ↓
Property → Script → Swarna Panchayat
Details   Process   Application
```

### Tab 2 Data Flow
```
FINAL TAB2.xlsx → tab2.py → Owner API
       ↓            ↓         ↓
   Owner Data → Script → Swarna Panchayat
              Process   Application
```

### Tab 3 Data Flow
```
Pedapalem HT 2024-25 (1) (2).xlsx → tab3.py → Floor API
              ↓                        ↓         ↓
         Floor Data → Script → Swarna Panchayat
                     Process   Application
```

### Tab 4 Data Flow
```
Pedapalem HT 2024-25 (1) (2).xlsx → tab4.py → Tax API
              ↓                        ↓         ↓
         Tax Data → Script → Swarna Panchayat
                    Process   Application
```

### Assessment Adjustment Data Flow
```
TAB4.xlsx + ARREAR FILE TAB4.xlsx → enroll_assesment_adjustment.py → Tax API
       ↓                ↓                        ↓                    ↓
   Current Tax + Arrears Data → Arrears Update Script → Swarna Panchayat
                               (Updates Historical Data)  Application
```

## 📋 File Dependencies

### Script Dependencies
- **tab1.py**: Depends on `TAB1.xlsx`, `constants.py`
- **tab2.py**: Depends on `FINAL TAB2.xlsx`, `constants.py`
- **tab3.py**: Depends on `Pedapalem HT 2024-25 (1) (2).xlsx`, `constants.py`
- **tab4.py**: Depends on `Pedapalem HT 2024-25 (1) (2).xlsx`, `constants.py`
- **enroll_assesment_adjustment.py**: Depends on `TAB4.xlsx`, `ARREAR FILE TAB4.xlsx`, `constants.py`

### API Dependencies
All scripts depend on the Swarna Panchayat API endpoints:
- Base URL: `https://api.swarnapanchayat.apcfss.in/prtntmapi/`
- Authentication: Bearer token in headers
- Rate limiting: Built-in retry mechanisms with sleep intervals

## 🎯 Recommendations for File Organization

### 1. Standardize Excel File Names
```
Current Name → Recommended Name
Pedapalem HT 2024-25 (1) (2).xlsx → pedapalem_ht_2024_25.xlsx
ARREAR FILE TAB4.xlsx → arrear_file_tab4.xlsx
FINAL TAB2.xlsx → final_tab2.xlsx
```

### 2. Remove Unused Files
Consider removing or archiving unused Excel files:
- `42 COLUMN DATA LATEST (2).xlsx`
- `FINAL_BOOK2.xlsx`
- `FINAL_BOOK2_l.xlsx`
- `Book2.xlsx`

### 3. Create Data Directory
Organize Excel files in a dedicated data directory:
```
data/
├── tab1_data.xlsx
├── tab2_data.xlsx
├── tab3_tab4_data.xlsx
├── tab4_tax_data.xlsx
└── arrear_data.xlsx
```

## 🔍 File Content Analysis

### Excel File Structures
- **TAB1.xlsx**: Contains property assessment numbers, door numbers, boundaries
- **FINAL TAB2.xlsx**: Contains owner names, father names, assessment numbers
- **Pedapalem HT 2024-25 (1) (2).xlsx**: Contains floor details, tax amounts, capital values
- **TAB4.xlsx**: Contains current year tax demands
- **ARREAR FILE TAB4.xlsx**: Contains historical tax arrears data

### Script Functionality
- **tab1.py**: Basic property information population
- **tab2.py**: Owner and occupant details
- **tab3.py**: Building construction and floor details
- **tab4.py**: Tax assessment and demand details
- **enroll_assesment_adjustment.py**: Data correction and historical arrears updates

## 📝 Notes
- All scripts include comprehensive error handling
- Retry mechanisms are implemented for API failures
- Random data generation is used for some fields
- Assessment number filtering is implemented (400-500 range in some scripts)
- API rate limiting is handled with sleep intervals

## ⚠️ **LEGAL DISCLAIMER**

**EDUCATIONAL PURPOSE ONLY**: These scripts are created solely for educational and learning purposes. They are NOT authorized for production use in government systems.

**NO PRODUCTION USE**: These scripts should NEVER be used to automate official government services without proper authorization.

**USE AT YOUR OWN RISK**: Users are responsible for legal compliance and any consequences of unauthorized use.
