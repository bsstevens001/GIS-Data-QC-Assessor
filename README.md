# GIS-Data-QC-Assessor v1.0
Repository for accessing &amp; understanding the GIS Data QC Assessor

## What is the GIS Data QC Assessor?
The GIS Data QC Assessor is a **Python** framework used to assess the quality of tabular utility datasets. By performing a series of validation checks, generating quality reports, calculating weighted quality scores, and more, the user will understand the number of errors within the dataset, where the errors are located, and how valid the data is.

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
- Invalid pipe age detection
- Invalid pipe status detection
- Weighted quality scoring
- Report of error counts
- Report of error location
- Report of executed and skipped checks
- Visualization of error counts & quality score

### Supported Fields
Alias standardization for fields related to:
- Asset_ID
- Asset_Type
- Latitude
- Longitude
- Install_Year
- Diameter
- Status
- Material

### Libraries Used
The libraries used within the tool include **Pandas** for data analysis and **Matplotlib** for data visualization.

## Output Examples

### Output Report
<img width="364" height="919" alt="Screenshot 2026-08-04 114247" src="https://github.com/user-attachments/assets/5b326fb7-a9e2-4a2c-96ec-bf240cb9b839" />

### Output Error Count Chart
<img width="678" height="782" alt="image" src="https://github.com/user-attachments/assets/e95a6ecb-41c2-4002-a630-a8ad34ba9621" />

### Output Score Chart
<img width="687" height="703" alt="image" src="https://github.com/user-attachments/assets/e23d289b-5618-4664-bb31-ae16fcc2a5d3" />

```python
import pandas as pd
import matplotlib.pyplot as plt
