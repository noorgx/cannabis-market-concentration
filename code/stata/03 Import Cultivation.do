clear all 
set more off


import delimited "../../Cal Poly/Cannabis Market Intelligence Platform Report - Licenses - 2025-07-03.csv", clear
gen multi_owner=0
replace multi_owner=strpos(companyid,";")
gen primary_company=substr(companyid,1,multi_owner-1)
replace primary_company=companyid if primary_company==""
destring primary_company, replace
keep statelicenseid primary_company 
rename statelicenseid licenseNumber
duplicates drop
keep if licenseNumber!=""

tempfile parent_co
save `parent_co'



import excel "../../Cal Poly/Working Cultivation Canopy June 2025.xlsx", sheet("License data canopy") firstrow clear

keep if licenseStatus=="Active"
keep if LargeDate==.

gen type=""
replace type="Indoor" if licenseType=="Large Indoor"
replace type="Mixed_Light" if licenseType=="Large Mixed-Light Tier 1"
replace type="Mixed_Light" if licenseType=="Large Mixed-Light Tier 2"
replace type="Outdoor" if licenseType=="Large Outdoor"
replace type="Indoor" if licenseType=="Medium Indoor"
replace type="Mixed_Light" if licenseType=="Medium Mixed-Light Tier 1"
replace type="Mixed_Light" if licenseType=="Medium Mixed-Light Tier 2"
replace type="Outdoor" if licenseType=="Medium Outdoor"
replace type="Indoor" if licenseType=="Small Indoor"
replace type="Mixed_Light" if licenseType=="Small Mixed-Light Tier 1"
replace type="Mixed_Light" if licenseType=="Small Mixed-Light Tier 2"
replace type="Outdoor" if licenseType=="Small Outdoor"
replace type="Indoor" if licenseType=="Specialty Cottage Indoor"
replace type="Mixed_Light" if licenseType=="Specialty Cottage Mixed-Light Tier 1"
replace type="Mixed_Light" if licenseType=="Specialty Cottage Mixed-Light Tier 2"
replace type="Outdoor" if licenseType=="Specialty Cottage Outdoor"
replace type="Indoor" if licenseType=="Specialty Indoor"
replace type="Mixed_Light" if licenseType=="Specialty Mixed-Light Tier 1"
replace type="Mixed_Light" if licenseType=="Specialty Mixed-Light Tier 2"
replace type="Outdoor" if licenseType=="Specialty Outdoor"

gen micro_cult=0
gen micro_indoor=0
replace micro_cult=strpos(activity,"Cultivator")
replace micro_indoor=strpos(activity,"Indoor")
drop if licenseType=="Microbusiness"&micro_cult==0

replace type="Outdoor" if licenseType=="Microbusiness"&micro_indoor==0
replace type="Indoor" if licenseType=="Microbusiness"&micro_indoor==1


merge m:1 licenseNumber using `parent_co', keep(master match) nogen



save "../Working_data/cultivation.dta", replace



