## DevSecops Pipeline Project


This repository contains Github Actions workflows used for auotomating security in the development pipeline.


## Folder Structur
- github/workflows/: Github Actions YAML file for CI/CD
- src/: Aplication source code (optimal)
- docs/: Documentation folder (optimal) 

## Workflows Overview
- Code scanning (e.g., with Gitleaks)
- Linting / Build verification 
- Security check

## Tools Used 
- Github Actions
- Gitleaks
- [...]

## Example workflows

Here's an example of a Github Actions workflows that runs Gitleaks for scret scanning
"
'''yaml 
name: Gitleaks Scan 
on: [push]


jobs:
	scan:
	  runs-on: ubuntu-lastets
	  steps:
		- user: actions/checkout@v3
		- name: Run Gitleask 
		- uses: zricethezav/gitleaks-action@v1.6.0
		
		
## Author 
Martinus Setiawan - [GITHUB](https://github.com/MartinStwn)
