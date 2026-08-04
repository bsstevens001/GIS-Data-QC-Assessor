# GIS-Data-QC-Assessor v1.0
Repository for accessing &amp; understanding the GIS Data QC Assessor

## What is the GIS Data QC Assessor?
The GIS Data QC Assessor is a python framework used to assess the quality of tabular utility datasets. By performing a series of validation checks, generating quality reports, calculating weighted quality scores, and more, the user will understand the number of errors within the dataset, where the errors are located, and how valid the data is.

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
Asset_ID
Asset_Type
Latitude
Longitude
Install_Year
Diameter
Status
Material

## Libraries Used
The libraries used within the tool include **Pandas** for data analysis and **Matplotlib** for data visualization.

```python
import pandas as pd
import matplotlib.pyplot as plt
