# Test Pipeline Data Core v1

This test suite validates data quality and integrity for Product data loaded from an Excel file using pytest.

## Overview

The `test_pipeline_data_core_v1.py` file contains data validation tests for a Product dataset. It performs various checks including column existence, data types, null values, uniqueness, and value range validations.

## Prerequisites

- Python 3.x
- pytest
- pandas
- numpy
- openpyxl (for reading Excel files)

## Installation

Install the required dependencies:

```bash
pip install pytest pandas numpy openpyxl
```

## Data Source

The tests expect an Excel file at:
```
C:\Users\MK416SE\Downloads\Product.xlsx
```

**Note:** Update the file path in the `df()` fixture if your Excel file is located elsewhere.

## Test Cases

### 1. `test_col_exists(df)`
- **Purpose:** Validates that the `ProductKey` column exists in the dataset
- **Assertion:** Checks if `ProductKey` is present in the DataFrame columns

### 2. `test_null_check(df)`
- **Purpose:** Ensures data completeness for the `ProductKey` column
- **Assertion:** Verifies that all values in `ProductKey` are non-null

### 3. `test_unique_check(df)`
- **Purpose:** Validates uniqueness constraint on `ProductKey`
- **Assertion:** Confirms that all values in `ProductKey` are unique (no duplicates)

### 4. `test_productkey_dtype_int(df)`
- **Purpose:** Validates data type integrity for `ProductKey`
- **Assertion:** Ensures `ProductKey` is of integer type (`int` or `np.int64`)

### 5. `test_range_val(df)`
- **Purpose:** Validates value range for `SafetyStockLevel`
- **Assertion:** Checks that at least one value in `SafetyStockLevel` falls within the range [0, 1000]

### 6. `test_range_val_str(df)`
- **Purpose:** Validates allowed string values for the `Color` column
- **Assertion:** Verifies that all unique values in `Color` match the expected set:
  - `nan` (null values)
  - `'Black'`, `'Silver'`, `'Red'`, `'White'`, `'Blue'`, `'Multi'`, `'Yellow'`, `'Grey'`, `'Silver/Black'`

## Running the Tests

### Run all tests:
```bash
pytest test_pipeline_data_core_v1.py
```

### Run with verbose output:
```bash
pytest test_pipeline_data_core_v1.py -v
```

### Run a specific test:
```bash
pytest test_pipeline_data_core_v1.py::test_col_exists -v
```

### Run with detailed output:
```bash
pytest test_pipeline_data_core_v1.py -v -s
```

## Expected Output

When all tests pass, you should see:
```
========================= test session starts =========================
collected 6 items

test_pipeline_data_core_v1.py::test_col_exists PASSED
test_pipeline_data_core_v1.py::test_null_check PASSED
test_pipeline_data_core_v1.py::test_unique_check PASSED
test_pipeline_data_core_v1.py::test_productkey_dtype_int PASSED
test_pipeline_data_core_v1.py::test_range_val PASSED
test_pipeline_data_core_v1.py::test_range_val_str PASSED

========================= 6 passed in X.XXs =========================
```

## Troubleshooting

### File Not Found Error
If you encounter a file not found error:
- Ensure the Excel file exists at the specified path: `C:\Users\MK416SE\Downloads\Product.xlsx`
- Update the path in the `df()` fixture if your file is located elsewhere

### Import Errors
If you see import errors:
- Verify all dependencies are installed: `pip install pytest pandas numpy openpyxl`
- Check your Python environment is activated

### Test Failures
If tests fail:
- Review the assertion messages to identify which validation failed
- Check your Excel file data against the expected constraints
- Ensure data types match expectations (e.g., `ProductKey` should be integer)

## File Structure

```
Session one/
├── test_pipeline_data_core_v1.py  # Test file
└── README.md                      # This file
```

## Notes

- The fixture `df()` loads the Excel file once and reuses it across all tests for efficiency
- Tests are designed to validate ETL pipeline data quality
- Update the file path and expected values as needed for your specific use case
