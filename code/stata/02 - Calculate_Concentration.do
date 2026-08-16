clear all 
set more off

use "../Data/Working_data/sales_w_parent_co.dta", clear


gen year=substr(date,4,4)
destring totalsales year, replace

*Statewide HHI overall
preserve
collapse (sum) totalsales (first) retailerzipcode primary_company, by(retailerlicensenumber year)
egen industry_sales = total(totalsales), by(year)
format %15.0g totalsales industry_sales

gen mkt_share=(totalsales/industry_sales)*100
gen mkt_share2=mkt_share^2
collapse (sum) mkt_share2 totalsales, by(year)
gen retailercounty="CA"
tempfile CA_overall
save `CA_overall'
restore

*Statewide HHI by parent company
preserve
replace primary_company=retailerlicensenumber if primary_company==""
collapse (sum) totalsales (first) retailerzipcode , by(primary_company year)
egen industry_sales = total(totalsales), by(year)
format %15.0g totalsales industry_sales
gen mkt_share=(totalsales/industry_sales)*100
gen mkt_share2=mkt_share^2
collapse (sum) mkt_share2 totalsales, by(year)
rename mkt_share2 mkt_share2_parent
rename totalsales totalsales_parent
gen retailercounty="CA"
tempfile CA_parent
save `CA_parent'
restore

*County-level HHI overall
preserve
collapse (sum) totalsales (first) retailerzipcode primary_company, by(retailerlicensenumber retailercounty year)
egen industry_sales = total(totalsales), by(retailercounty year)
format %15.0g totalsales industry_sales

gen mkt_share=(totalsales/industry_sales)*100
gen mkt_share2=mkt_share^2
collapse (sum) mkt_share2 totalsales, by(retailercounty year)
tempfile county_overall
save `county_overall'
restore

*Statewide HHI by parent company
preserve
replace primary_company=retailerlicensenumber if primary_company==""
collapse (sum) totalsales (first) retailerzipcode , by(primary_company retailercounty year)
egen industry_sales = total(totalsales), by(retailercounty year)
format %15.0g totalsales industry_sales
gen mkt_share=(totalsales/industry_sales)*100
gen mkt_share2=mkt_share^2
collapse (sum) mkt_share2 totalsales, by(retailercounty year)
rename mkt_share2 mkt_share2_parent
rename totalsales totalsales_parent
tempfile county_parent
save `county_parent'
restore

use `county_overall', clear
append using `CA_overall'
merge 1:1 year retailercounty using `county_parent', nogen
merge 1:1 year retailercounty using `CA_parent', nogen update
sort retailercounty year

egen max_sales=sum(totalsales) if retailercounty=="CA"
egen max_sales2=max(max_sales)
bysort retailercounty: egen county_sales=sum(totalsales)
bysort retailercounty: egen county_sales_parent=sum(totalsales_parent)

gen opacity = (county_sales / max_sales2 )
replace opacity = round(opacity * 100)  // Convert to percentage (0 to 100)
gen opacity_parent = (county_sales_parent / max_sales2 )
replace opacity_parent = round(opacity_parent * 100)  // Convert to percentage (0 to 100)


twoway ///
    (line mkt_share2 year if retailercounty == "ALAMEDA", lcolor(navy)) ///
    (line mkt_share2 year if retailercounty == "BUTTE", lcolor(navy)) ///
	(line mkt_share2 year if retailercounty == "CA", lcolor(black) lwidth(thick)) ///
    (line mkt_share2 year if retailercounty == "CALAVERAS", lcolor(navy)) ///
    (line mkt_share2 year if retailercounty == "COLUSA", lcolor(navy)) ///
    (line mkt_share2 year if retailercounty == "CONTRA COSTA", lcolor(navy)) ///
    (line mkt_share2 year if retailercounty == "DEL NORTE", lcolor(navy)) ///
    (line mkt_share2 year if retailercounty == "EL DORADO", lcolor(navy)) ///
    (line mkt_share2 year if retailercounty == "FRESNO", lcolor(navy)) ///
    (line mkt_share2 year if retailercounty == "HUMBOLDT", lcolor(navy)) ///
    (line mkt_share2 year if retailercounty == "IMPERIAL", lcolor(navy)) ///
    (line mkt_share2 year if retailercounty == "INYO", lcolor(navy)) ///
    (line mkt_share2 year if retailercounty == "KERN", lcolor(navy)) ///
    (line mkt_share2 year if retailercounty == "KINGS", lcolor(navy)) ///
    (line mkt_share2 year if retailercounty == "LAKE", lcolor(navy)) ///
    (line mkt_share2 year if retailercounty == "LASSEN", lcolor(navy)) ///
    (line mkt_share2 year if retailercounty == "LOS ANGELES", lcolor(navy)) ///
    (line mkt_share2 year if retailercounty == "MADERA", lcolor(navy)) ///
    (line mkt_share2 year if retailercounty == "MARIN", lcolor(navy)) ///
    (line mkt_share2 year if retailercounty == "MENDOCINO", lcolor(navy)) ///
    (line mkt_share2 year if retailercounty == "MERCED", lcolor(navy)) ///
    (line mkt_share2 year if retailercounty == "MONO", lcolor(navy)) ///
    (line mkt_share2 year if retailercounty == "MONTEREY", lcolor(navy)) ///
    (line mkt_share2 year if retailercounty == "NAPA", lcolor(navy)) ///
    (line mkt_share2 year if retailercounty == "NEVADA", lcolor(navy)) ///
    (line mkt_share2 year if retailercounty == "ORANGE", lcolor(navy)) ///
    (line mkt_share2 year if retailercounty == "PLACER", lcolor(navy)) ///
    (line mkt_share2 year if retailercounty == "RIVERSIDE", lcolor(navy)) ///
    (line mkt_share2 year if retailercounty == "SACRAMENTO", lcolor(navy)) ///
    (line mkt_share2 year if retailercounty == "SAN BENITO", lcolor(navy)) ///
    (line mkt_share2 year if retailercounty == "SAN BERNARDINO", lcolor(navy)) ///
    (line mkt_share2 year if retailercounty == "SAN DIEGO", lcolor(navy)) ///
    (line mkt_share2 year if retailercounty == "SAN FRANCISCO", lcolor(navy)) ///
    (line mkt_share2 year if retailercounty == "SAN JOAQUIN", lcolor(navy)) ///
    (line mkt_share2 year if retailercounty == "SAN LUIS OBISPO", lcolor(navy)) ///
    (line mkt_share2 year if retailercounty == "SAN MATEO", lcolor(navy)) ///
    (line mkt_share2 year if retailercounty == "SANTA BARBARA", lcolor(navy)) ///
    (line mkt_share2 year if retailercounty == "SANTA CLARA", lcolor(navy)) ///
    (line mkt_share2 year if retailercounty == "SANTA CRUZ", lcolor(navy)) ///
    (line mkt_share2 year if retailercounty == "SHASTA", lcolor(navy)) ///
    (line mkt_share2 year if retailercounty == "SISKIYOU", lcolor(navy)) ///
    (line mkt_share2 year if retailercounty == "SOLANO", lcolor(navy)) ///
    (line mkt_share2 year if retailercounty == "SONOMA", lcolor(navy)) ///
    (line mkt_share2 year if retailercounty == "STANISLAUS", lcolor(navy)) ///
    (line mkt_share2 year if retailercounty == "TEHAMA", lcolor(navy)) ///
    (line mkt_share2 year if retailercounty == "TRINITY", lcolor(navy)) ///
    (line mkt_share2 year if retailercounty == "TULARE", lcolor(navy)) ///
    (line mkt_share2 year if retailercounty == "TUOLUMNE", lcolor(navy)) ///
    (line mkt_share2 year if retailercounty == "VENTURA", lcolor(navy)) ///
    (line mkt_share2 year if retailercounty == "YOLO", lcolor(navy)) ///
    (line mkt_share2 year if retailercounty == "YUBA", lcolor(navy)), ///
    xlabel(2018(1)2024) ylabel(, angle(horizontal)) ///
    title("HHI Over Time by County") ///
    xtitle("Year") ytitle("HHI") legend(off)


twoway ///
    (line mkt_share2_parent year if retailercounty == "ALAMEDA", lcolor(navy)) ///
    (line mkt_share2_parent year if retailercounty == "BUTTE", lcolor(navy)) ///
	(line mkt_share2_parent year if retailercounty == "CA", lcolor(black) lwidth(thick)) ///
    (line mkt_share2_parent year if retailercounty == "CALAVERAS", lcolor(navy)) ///
    (line mkt_share2_parent year if retailercounty == "COLUSA", lcolor(navy)) ///
    (line mkt_share2_parent year if retailercounty == "CONTRA COSTA", lcolor(navy)) ///
    (line mkt_share2_parent year if retailercounty == "DEL NORTE", lcolor(navy)) ///
    (line mkt_share2_parent year if retailercounty == "EL DORADO", lcolor(navy)) ///
    (line mkt_share2_parent year if retailercounty == "FRESNO", lcolor(navy)) ///
    (line mkt_share2_parent year if retailercounty == "HUMBOLDT", lcolor(navy)) ///
    (line mkt_share2_parent year if retailercounty == "IMPERIAL", lcolor(navy)) ///
    (line mkt_share2_parent year if retailercounty == "INYO", lcolor(navy)) ///
    (line mkt_share2_parent year if retailercounty == "KERN", lcolor(navy)) ///
    (line mkt_share2_parent year if retailercounty == "KINGS", lcolor(navy)) ///
    (line mkt_share2_parent year if retailercounty == "LAKE", lcolor(navy)) ///
    (line mkt_share2_parent year if retailercounty == "LASSEN", lcolor(navy)) ///
    (line mkt_share2_parent year if retailercounty == "LOS ANGELES", lcolor(navy)) ///
    (line mkt_share2_parent year if retailercounty == "MADERA", lcolor(navy)) ///
    (line mkt_share2_parent year if retailercounty == "MARIN", lcolor(navy)) ///
    (line mkt_share2_parent year if retailercounty == "MENDOCINO", lcolor(navy)) ///
    (line mkt_share2_parent year if retailercounty == "MERCED", lcolor(navy)) ///
    (line mkt_share2_parent year if retailercounty == "MONO", lcolor(navy)) ///
    (line mkt_share2_parent year if retailercounty == "MONTEREY", lcolor(navy)) ///
    (line mkt_share2_parent year if retailercounty == "NAPA", lcolor(navy)) ///
    (line mkt_share2_parent year if retailercounty == "NEVADA", lcolor(navy)) ///
    (line mkt_share2_parent year if retailercounty == "ORANGE", lcolor(navy)) ///
    (line mkt_share2_parent year if retailercounty == "PLACER", lcolor(navy)) ///
    (line mkt_share2_parent year if retailercounty == "RIVERSIDE", lcolor(navy)) ///
    (line mkt_share2_parent year if retailercounty == "SACRAMENTO", lcolor(navy)) ///
    (line mkt_share2_parent year if retailercounty == "SAN BENITO", lcolor(navy)) ///
    (line mkt_share2_parent year if retailercounty == "SAN BERNARDINO", lcolor(navy)) ///
    (line mkt_share2_parent year if retailercounty == "SAN DIEGO", lcolor(navy)) ///
    (line mkt_share2_parent year if retailercounty == "SAN FRANCISCO", lcolor(navy)) ///
    (line mkt_share2_parent year if retailercounty == "SAN JOAQUIN", lcolor(navy)) ///
    (line mkt_share2_parent year if retailercounty == "SAN LUIS OBISPO", lcolor(navy)) ///
    (line mkt_share2_parent year if retailercounty == "SAN MATEO", lcolor(navy)) ///
    (line mkt_share2_parent year if retailercounty == "SANTA BARBARA", lcolor(navy)) ///
    (line mkt_share2_parent year if retailercounty == "SANTA CLARA", lcolor(navy)) ///
    (line mkt_share2_parent year if retailercounty == "SANTA CRUZ", lcolor(navy)) ///
    (line mkt_share2_parent year if retailercounty == "SHASTA", lcolor(navy)) ///
    (line mkt_share2_parent year if retailercounty == "SISKIYOU", lcolor(navy)) ///
    (line mkt_share2_parent year if retailercounty == "SOLANO", lcolor(navy)) ///
    (line mkt_share2_parent year if retailercounty == "SONOMA", lcolor(navy)) ///
    (line mkt_share2_parent year if retailercounty == "STANISLAUS", lcolor(navy)) ///
    (line mkt_share2_parent year if retailercounty == "TEHAMA", lcolor(navy)) ///
    (line mkt_share2_parent year if retailercounty == "TRINITY", lcolor(navy)) ///
    (line mkt_share2_parent year if retailercounty == "TULARE", lcolor(navy)) ///
    (line mkt_share2_parent year if retailercounty == "TUOLUMNE", lcolor(navy)) ///
    (line mkt_share2_parent year if retailercounty == "VENTURA", lcolor(navy)) ///
    (line mkt_share2_parent year if retailercounty == "YOLO", lcolor(navy)) ///
    (line mkt_share2_parent year if retailercounty == "YUBA", lcolor(navy)), ///
    xlabel(2018(1)2024) ylabel(, angle(horizontal)) ///
    title("HHI Over Time by County") ///
    xtitle("Year") ytitle("HHI") legend(off)
	
	rename mkt_share2 HHI
	rename mkt_share2_parent HHI_parent_level
	keep retailercounty year HHI HHI_parent_level

	export excel using "../Results/HHI_by_county.xlsx", firstrow(variables) replace
