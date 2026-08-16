clear all 
set more off

import excel "../Data/HUD/ZIP_COUNTY_122024.xlsx", sheet("Export Worksheet") firstrow allstring clear
keep if USPS_ZIP_PREF_STATE=="CA"
duplicates tag ZIP, gen(zip_dup)
drop if zip_dup>=1
keep ZIP retailercounty
rename ZIP zip5
tempfile zip
save `zip', replace

import delimited "../Data/Cannabiz/Cannabis Market Intelligence Platform Report - Licenses - 2025-02-21.csv", clear
gen multi_owner=0
replace multi_owner=strpos(companyid,";")
gen primary_company=substr(companyid,1,multi_owner-1)
replace primary_company=companyid if primary_company==""
destring primary_company, replace
keep statelicenseid primary_company county
rename statelicenseid retailerlicensenumber
rename county cannabiz_county
duplicates drop
keep if retailerlicensenumber!=""

tempfile parent_co
save `parent_co'

local files "sales18.csv sales19.csv sales20.csv sales21.csv sales22.csv sales23v2.csv sales24.csv"

foreach file in `files' {
    import delimited "../Data/`file'", clear stringcols(_all) 
	drop meanprice v1
	tempfile processed_`=subinstr("`file'",".csv","",.)'
    save `processed_`=subinstr("`file'",".csv","",.)''
}

use `processed_sales18', clear
append using `processed_sales19'
append using `processed_sales20'
append using `processed_sales21'
append using `processed_sales22'
append using `processed_sales23v2'
append using `processed_sales24'
tempfile sales
save `sales'
tab itemcategory

// local files "salesquantity18.csv salesquantity19.csv salesquantity20.csv salesquantity21.csv salesquantity22.csv salesquantity23v2.csv salesquantity24.csv"
//
// foreach file in `files' {
//     import delimited "../Data/`file'", clear stringcols(_all) 
// 	drop meanprice v1
// 	tempfile processed_`=subinstr("`file'",".csv","",.)'
//     save `processed_`=subinstr("`file'",".csv","",.)''
// }
//
// use `processed_salesquantity18', clear
// append using `processed_salesquantity19'
// append using `processed_salesquantity20'
// append using `processed_salesquantity21'
// append using `processed_salesquantity22'
// append using `processed_salesquantity23v2'
// append using `processed_salesquantity24'
// destring totalgrams totalsales, replace
// rename totalsales totalsales_fromQ
// replace itemcategory="Flower (packaged eighth - each)" if itemcategory=="flowereighth"
// replace itemcategory="Flower (packaged quarter - each)" if itemcategory=="flowerquarter"
// replace itemcategory="" if itemcategory=="vapegram"
// replace itemcategory="" if itemcategory=="vapehalfgram"
// tempfile salesquantity
// save `salesquantity'
// tab itemcategory
//
// collapse (sum) totalgrams totalsales, by(retailerlicensenumber itemcategory date)
//
// merge 1:1 retailerlicensenumber itemcategory date using `sales'

gsort retailerlicensenumber -retailercounty retailerfacilitytype retailercity retailerzipcode   date itemcategory totalsales 

merge m:1 retailerlicensenumber using `parent_co'
drop if _merge==2
// gen retailerzipcode_full=retailerzipcode
// replace retailerzipcode=substr(retailerzipcode,1,5)
// merge m:1 retailerzipcode using `zip', gen(_merge_zip)

replace retailercounty="" if retailercounty=="NA"
replace retailercounty="" if retailercounty=="UNDEFINED"


replace retailercounty="ALAMEDA" if cannabiz_county=="Alameda County"&retailercounty==""
replace retailercounty="EL DORADO" if cannabiz_county=="El Dorado County"&retailercounty==""
replace retailercounty="HUMBOLDT" if cannabiz_county=="Humboldt County"&retailercounty==""
replace retailercounty="IMPERIAL" if cannabiz_county=="Imperial County"&retailercounty==""
replace retailercounty="INYO" if cannabiz_county=="Inyo County"&retailercounty==""
replace retailercounty="KERN" if cannabiz_county=="Kern County"&retailercounty==""
replace retailercounty="KINGS" if cannabiz_county=="Kings County"&retailercounty==""
replace retailercounty="LOS ANGELES" if cannabiz_county=="Los Angeles County"&retailercounty==""
replace retailercounty="MARIN" if cannabiz_county=="Marin County"&retailercounty==""
replace retailercounty="MENDOCINO" if cannabiz_county=="Mendocino County"&retailercounty==""
replace retailercounty="MERCED" if cannabiz_county=="Merced County"&retailercounty==""
replace retailercounty="MONTEREY" if cannabiz_county=="Monterey County"&retailercounty==""
replace retailercounty="NEVADA" if cannabiz_county=="Nevada County"&retailercounty==""
replace retailercounty="RIVERSIDE" if cannabiz_county=="Riverside County"&retailercounty==""
replace retailercounty="SACRAMENTO" if cannabiz_county=="Sacramento County"&retailercounty==""
replace retailercounty="SAN DIEGO" if cannabiz_county=="San Diego County"&retailercounty==""
replace retailercounty="SAN FRANCISCO" if cannabiz_county=="San Francisco County"&retailercounty==""
replace retailercounty="SAN LUIS OBISPO" if cannabiz_county=="San Luis Obispo County"&retailercounty==""
replace retailercounty="SAN MATEO" if cannabiz_county=="San Mateo County"&retailercounty==""
replace retailercounty="SANTA BARBARA" if cannabiz_county=="Santa Barbara County"&retailercounty==""
replace retailercounty="SANTA CRUZ" if cannabiz_county=="Santa Cruz County"&retailercounty==""
replace retailercounty="SHASTA" if cannabiz_county=="Shasta County"&retailercounty==""
replace retailercounty="SONOMA" if cannabiz_county=="Sonoma County"&retailercounty==""
replace retailercounty="STANISLAUS" if cannabiz_county=="Stanislaus County"&retailercounty==""
replace retailercounty="TULARE" if cannabiz_county=="Tulare County"&retailercounty==""
replace retailercounty="VENTURA" if cannabiz_county=="Ventura County"&retailercounty==""
replace retailercounty="CALAVERAS" if cannabiz_county=="Calaveras County"&retailercounty==""
replace retailercounty="LASSEN" if cannabiz_county=="Lassen County"&retailercounty==""
replace retailercounty="MONO" if cannabiz_county=="Mono County"&retailercounty==""
replace retailercounty="NAPA" if cannabiz_county=="Napa County"&retailercounty==""
replace retailercounty="SAN BENITO" if cannabiz_county=="San Benito County"&retailercounty==""
replace retailercounty="SAN BERNARDINO" if cannabiz_county=="San Bernardino County"&retailercounty==""
replace retailercounty="SAN JOAQUIN" if cannabiz_county=="San Joaquin County"&retailercounty==""
replace retailercounty="SANTA CLARA" if cannabiz_county=="Santa Clara County"&retailercounty==""
replace retailercounty="YUBA" if cannabiz_county=="Yuba County"&retailercounty==""

replace retailercount="RIVERSIDE" if retailerlicensenumber=="C10-0000209-LIC"
replace retailercount="SAN BERNARDINO" if retailerlicensenumber=="C12-0000370-LIC"

replace retailercounty=strupper(retailercounty)

preserve
	keep retailerlicensenumber retailercounty
	drop if retailerlicensenumber==""
	drop if retailercounty==""
	duplicates drop
	tempfile license_county
	save `license_county', replace
restore

merge m:1 retailerlicensenumber using `license_county', update gen(_merge_lic_county)

*****************
gen zip5=substr(retailerzipcode,1,5)
merge m:1 zip5 using `zip', update gen(_merge_zip)
drop if _merge_zip==2
drop _merge _merge_zip

replace retailercount="LOS ANGELES" if retailerlicensenumber=="C10-0000279-LIC"
replace retailercount="LOS ANGELES" if retailerlicensenumber=="C10-0000747-LIC"
replace retailercount="LOS ANGELES" if retailerlicensenumber=="C12-0000056-LIC"
replace retailercount="LOS ANGELES" if retailerlicensenumber=="C9-0000499-LIC"
replace retailercount="LOS ANGELES" if retailerlicensenumber=="C10-0000248-LIC"
replace retailercount="KINGS" if retailerlicensenumber=="C9-0000386-LIC"
replace retailercount="TULARE" if retailerlicensenumber=="C10-0000343-LIC"
replace retailercount="TULARE" if retailerlicensenumber=="C10-0000299-LIC"
replace retailercount="MONO" if retailerlicensenumber=="C10-0000078-LIC"
replace retailercount="SAN FRANCISCO" if retailerlicensenumber=="C10-0000265-LIC"
replace retailercount="SOLANO" if retailerlicensenumber=="C12-0000068-LIC"
replace retailercount="SAN BENITO" if retailerlicensenumber=="C9-0000396-LIC"
replace retailercount="SANTA CRUZ" if retailerlicensenumber=="C10-0000238-LIC"
replace retailercount="STANISLAUS" if retailerlicensenumber=="C10-0000576-LIC"
replace retailercount="STANISLAUS" if retailerlicensenumber=="C10-0000022-LIC"
replace retailercount="SACRAMENTO" if retailerlicensenumber=="C12-0000157-LIC"
replace retailercount="HUMBOLDT" if retailerlicensenumber=="C10-0000190-LIC"
replace retailercount="YOLO" if retailerlicensenumber=="C10-0000148-LIC"
replace retailercount="YOLO" if retailerlicensenumber=="C10-0000111-LIC"
replace retailercount="YOLO" if retailerlicensenumber=="C9-0000088-LIC"
replace retailercount="YUBA" if retailerlicensenumber=="C10-0000449-LIC"
replace retailercount="YUBA" if retailerlicensenumber=="C10-0000707-LIC"
replace retailercount="LOS ANGELES" if retailerlicensenumber=="C10-0000398-LIC"
replace retailercount="MONO" if retailerlicensenumber=="C10-0000382-LIC"
replace retailercount="SAN FRANCISCO" if retailerlicensenumber=="C10-0000200-LIC"
replace retailercount="SAN FRANCISCO" if retailerlicensenumber=="C10-0000152-LIC"
replace retailercount="SOLANO" if retailerlicensenumber=="C9-0000376-LIC"
replace retailercount="LOS ANGELES" if retailerlicensenumber=="C10-0000098-LIC"
replace retailercount="STANISLAUS" if retailerlicensenumber=="C10-0000196-LIC"
replace retailercount="YOLO" if retailerlicensenumber=="C9-0000142-LIC"
replace retailercount="NEVADA" if retailerlicensenumber=="C9-0000061-LIC"

tab retailercounty, miss

save "../Data/Working_data/sales_w_parent_co.dta", replace



