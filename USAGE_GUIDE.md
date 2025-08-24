# Usage Guide for Swarna Panchayat Automation Scripts

## 🚀 Quick Start

### 1. Setup Environment
```bash
# Install required packages
pip install -r requirements.txt

# Update configuration
# Edit constants.py with your API credentials
```

### 2. Prepare Data Files
Ensure all Excel files are in the correct format and location:
- `TAB1.xlsx` - Property details
- `FINAL TAB2.xlsx` - Owner details  
- `Pedapalem HT 2024-25 (1) (2).xlsx` - Floor and tax data
- `TAB4.xlsx` - Tax demands
- `ARREAR FILE TAB4.xlsx` - Arrears data

### 3. Execute Scripts in Sequence
```bash
# Step 1: Populate Property Details
python tab1.py

# Step 2: Populate Owner Details
python tab2.py

# Step 3: Populate Floor Details
python tab3.py

# Step 4: Populate Tax Demands
python tab4.py

# Step 5: Update Arrears and Adjust Assessments (Optional - run when needed)
python enroll_assesment_adjustment.py
```

## 📋 Detailed Script Usage

### Tab 1 - Property Details (`tab1.py`)

**Purpose**: Populates basic property information in the first tab

**Data Requirements**:
- Assessment numbers
- Door numbers
- Property boundaries (East, West, North, South)
- Habitation names

**Execution**:
```bash
python tab1.py
```

**Expected Output**:
- API responses for each property
- Retry attempts if API fails
- Success/error messages for each record

**Troubleshooting**:
- Check `TAB1.xlsx` file structure
- Verify API authentication in `constants.py`
- Monitor console for error messages

### Tab 2 - Owner Details (`tab2.py`)

**Purpose**: Adds owner and occupant information

**Data Requirements**:
- Assessment numbers (400-500 range)
- Owner names
- Father names/guardian information

**Execution**:
```bash
python tab2.py
```

**Expected Output**:
- Owner details insertion confirmations
- API response messages
- Retry attempts for failed requests

**Troubleshooting**:
- Ensure `FINAL TAB2.xlsx` contains required columns
- Check assessment number range filtering
- Verify API endpoint availability

### Tab 3 - Floor Details (`tab3.py`)

**Purpose**: Populates building construction and floor information

**Data Requirements**:
- Assessment numbers (400-500 range)
- Building dimensions
- Construction types
- Capital values

**Execution**:
```bash
python tab3.py
```

**Expected Output**:
- Floor details insertion confirmations
- Building information updates
- API response status

**Troubleshooting**:
- Verify `Pedapalem HT 2024-25 (1) (2).xlsx` structure
- Check building age and dimension calculations
- Monitor API rate limiting

### Tab 4 - Tax Demands (`tab4.py`)

**Purpose**: Sets up tax assessment and demand details

**Data Requirements**:
- Assessment numbers (400-500 range)
- Tax amounts for current year
- Water, lighting, drainage taxes
- Library, sports, fire cess

**Execution**:
```bash
python tab4.py
```

**Expected Output**:
- Tax demand insertion confirmations
- Financial year tax setup
- API response messages

**Troubleshooting**:
- Check tax calculation formulas
- Verify financial year data
- Monitor API response codes

### Assessment Adjustment (`enroll_assesment_adjustment.py`)

**Purpose**: Updates arrears and adjusts assessment data

**Data Requirements**:
- Current tax data from `TAB4.xlsx`
- Historical arrears from `ARREAR FILE TAB4.xlsx`
- Assessment numbers

**Execution**:
```bash
python enroll_assment_adjustment.py
```

**Expected Output**:
- Arrears updates for multiple financial years
- Assessment corrections
- Historical tax data updates
- Multi-year tax calculations
- API response confirmations

**Troubleshooting**:
- Verify both Excel files contain required data
- Check arrear calculation formulas
- Monitor retry mechanisms

## ⚙️ Configuration

### Update Constants (`constants.py`)
```python
# API Configuration
headers = {
    "Authorization": "Bearer YOUR_ACTUAL_TOKEN",
    "Content-Type": "application/json"
}

# User and Location Details
user_id = "your_actual_user_id"
panch_secretariat_id = your_actual_panchayat_id
village_id = your_actual_village_id
habitation = "your_habitation_name"
property_street = "your_street_name"
property_pincode = "your_pincode"
```

### Environment Variables (Optional)
```bash
export SWARNA_API_TOKEN="your_token"
export SWARNA_USER_ID="your_user_id"
export SWARNA_PANCHAYAT_ID="your_panchayat_id"
```

## 📊 Monitoring and Logging

### Console Output
All scripts provide detailed console output:
- Processing progress
- API responses
- Error messages
- Retry attempts
- Success confirmations

### Error Handling
- Automatic retry mechanisms (up to 10 attempts)
- Sleep intervals between retries (3 seconds)
- Detailed error logging
- Graceful failure handling

### Success Indicators
- API response success codes
- Data insertion confirmations
- No error messages in responses
- Completed processing messages

## 🔧 Advanced Usage

### Batch Processing
Scripts process data in batches:
- `tab1.py`: Processes from record 30 onwards
- `tab2.py`: Filters assessment numbers 400-500
- `tab3.py`: Filters assessment numbers 400-500
- `tab4.py`: Filters assessment numbers 400-500

### Custom Ranges
Modify assessment number ranges in scripts:
```python
# Example: Change range in tab2.py
if (300 <= int(record["old_assessment_number"]) <= 600):
    # Process records in 300-600 range
```

### Data Validation
Scripts include built-in validation:
- Assessment number filtering
- Data type conversions
- Required field checks
- API response validation

## ⚠️ Important Considerations

### When to Use the Arrears Script
The `enroll_assesment_adjustment.py` script is designed to:
- Update historical arrears data for multiple financial years
- Correct assessment data when discrepancies are found
- Process arrear files to update tax demands
- **Note**: This script can be run independently of the main tab population process when you need to update arrears or correct assessment data

### API Rate Limiting
- Scripts include sleep intervals
- Retry mechanisms handle temporary failures
- Monitor API response times

### Data Consistency
- Ensure Excel files are not modified during execution
- Verify data formats match script expectations
- Check for duplicate assessment numbers

### Backup and Recovery
- Keep original Excel files as backups
- Monitor script execution progress
- Have rollback procedures ready

## 🐛 Common Issues and Solutions

### Issue: API Authentication Errors
**Solution**: Update token in `constants.py`

### Issue: File Not Found Errors
**Solution**: Verify Excel file names and locations

### Issue: Data Type Errors
**Solution**: Check Excel file column formats

### Issue: API Timeout Errors
**Solution**: Increase sleep intervals in scripts

### Issue: Missing Required Fields
**Solution**: Verify Excel file structure and data completeness

## ⚠️ **LEGAL DISCLAIMER**

**EDUCATIONAL PURPOSE ONLY**: This usage guide and the associated scripts are created solely for educational and learning purposes. They are **NOT authorized** for use in automating government services.

**NO PRODUCTION USE**: These scripts should **NEVER be used** in production environments, government systems, or to automate official government services without proper authorization.

**LEGAL COMPLIANCE**: Users are responsible for ensuring compliance with all applicable laws, regulations, and government policies.

**USE AT YOUR OWN RISK**: The authors and contributors are not responsible for any legal consequences arising from unauthorized use.

---

## 📞 Support

For technical support:
1. Check console error messages
2. Verify Excel file structures
3. Test API connectivity
4. Review configuration settings
5. Check data completeness

## 🔄 Maintenance

### Regular Tasks
- Update API tokens when expired
- Verify Excel data accuracy
- Monitor API response patterns
- Clean up temporary files
- Archive processed data

### Performance Optimization
- Adjust batch sizes if needed
- Optimize sleep intervals
- Monitor API response times
- Review error patterns
