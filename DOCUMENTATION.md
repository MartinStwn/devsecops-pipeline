## DevSecops Pipeline Project


This repository contains Github Actions workflows used for auotomating security in the development pipeline.


## Folder Structur
- github/workflows/: Github Actions YAML file for CI/CD
- src/: Aplication source code (optimal)
- docs/: Documentation folder (optimal) 

## Workflows Overview
The DevSecOps Pipeline Perfoms Automated Tasks Such as:
- Code scanning (e.g., with Gitleaks)
- Code Linting and Formating 
- Build verification 
- Static verification 
- Static Application Security Testing (SAST)
- Continous Integration check
- Security check
- Optimal: Deployment or artifact generation 

## Tools Used 
- Github Actions
- Gitleaks
- [...]

## Example Workflows: Gitleaks Scan

Here's an example of a Github Actions workflows that perfoms a secrets scan using Gitleaks:
"
'''yaml 
name: Gitleaks Secret Scan 
on: 
	push:
		branches:
			- main 
		
	pull_request 
	

jobs:
	scan:
	  runs-on: ubuntu-lastets
	  steps:
		- user: actions/checkout@v3
		- name: Run Gitleask 
		- uses: zricethezav/gitleaks-action@v1.6.0
		
		
## Author 
Martinus Setiawan - [GITHUB](https://github.com/MartinStwn)	
