# GIS-Data-QC-Assessor v1.0
An automated QA/QC framework for utility tabular datasets

## What is the GIS Data QC Assessor?
The `GIS Data QC Assessor v1.0` is a **Python** QA/QC framework used to assess the quality of tabular utility datasets. By performing a series of validation checks, generating quality reports, calculating weighted quality scores, and more, the user will understand the number of errors within the dataset, where the errors are located, and how valid the data is.

### Libraries Used
The libraries used within the tool include **Pandas** for data analysis and **Matplotlib** for data visualization.

### Tool Purpose
The GIS Data QC Assessor is important because it:
- Enhances work efficiency by automating statistical and analytical error checks
- Conducts checks based on common errors found in utility datasets
- Breaks down errors within the dataset that the user may not immediately find
- Output of report and related charts that can be shared amongst diverse audiences
- Allows the user to better understand their data, visualize it, and take action towards correcting the data

### Features
- User inputs
- Field alias formatting
- Dynamic runnability based on available fields
- Null detection
- Duplicate detection
- Invalid coordinate (Lat, Lon) detection
- Invalid pipe installation year detection
- Invalid pipe status detection
- Weighted quality scoring
- Report of error counts
- Report of error location
- Report of executed and skipped checks
- Visualization of error counts & quality score
- Outputs file that includes qc report & charts

### Supported Fields
Alias standardization for any fields related to:
- Asset_ID
- Asset_Type
- Latitude
- Longitude
- Install_Year
- Diameter
- Status
- Material

### Workflow
1. Input CSV Dataset
2. Field Alias Standardization
3. Validation Checks
4. Quality Scoring
5. Report Generation
6. Chart Visualization
7. Output Folder

## Output Examples
<details>
  <summary> Click to expand</summary>

  ### Output Report
  <img width="351" height="920" alt="Screenshot 2026-08-04 115957" src="https://github.com/user-attachments/assets/7c559612-d3fd-47ee-8333-d45e7c4b374f" />

  ### Output Error Count Chart
  <img width="678" height="782" alt="image" src="https://github.com/user-attachments/assets/e95a6ecb-41c2-4002-a630-a8ad34ba9621" />

  ### Output Score Chart
  <img width="687" height="703" alt="image" src="https://github.com/user-attachments/assets/e23d289b-5618-4664-bb31-ae16fcc2a5d3" />
</details>

## Eventual Enhancements
- GeoPandas integration & functionality for Geodataframes
- Geometry validation
- Duplicate geometry detection
- Additional domain validation rules
- Logical upgrades

```python
import pandas as pd
import matplotlib.pyplot as plt
