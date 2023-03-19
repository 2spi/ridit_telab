# RIDIT: Relative to an Identified Distribution

TE Lab Assignment - RIDIT Analysis, comparing two different pathways between two locations.

RIDIT (Relative to an Identified Distribution) Analysis is a simple statistical method for analyzing ordinal data i.e. qualitative ordered data.

The basic intent of RIDIT Analysis is to make comparisons across samples of relative frequency distributions of random variable measured on an ordinal scale (like a series of categories such as "minor," "moderate", "severe").

This method can be used for comparing responses such as the degree of pain, severity of disease, levels of satisfaction, preference or agreement.

## Usage
The main code file for RIDIT is data.py. This file uses the pandas library to read data from survey.txt and treatment.txt. survey.txt stores the reference group data and treatment.txt stores the treatment group data.

The code calculates "control RIDITs" for the data in treatment.txt and the "mean RIDIT" for the data in treatment.txt. This will execute the code and print the control RIDITs and mean RIDIT to the console.
