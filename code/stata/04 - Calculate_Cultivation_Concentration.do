clear all 
set more off


foreach grow_type in "Indoor" "Mixed_Light" "Outdoor" {
	use "../Working_data/cultivation.dta", clear
	keep if type=="`grow_type'"

	*Statewide HHI overall
	preserve
	collapse (sum) Canopy MaxSqFt, by(businessLegalName)
	egen industry_Canopy = total(Canopy)
	egen industry_MaxSqFt = total(MaxSqFt)
	format %15.0g Canopy MaxSqFt industry_Canopy industry_MaxSqFt

	gen mkt_share_Canopy=(Canopy/industry_Canopy)*100
	gen mkt_share2_Canopy=mkt_share_Canopy^2
	gen mkt_share_MaxSqFt=(MaxSqFt/industry_MaxSqFt)*100
	gen mkt_share2_MaxSqFt=mkt_share_MaxSqFt^2
	collapse (sum) mkt_share2_Canopy Canopy mkt_share2_MaxSqFt MaxSqFt
	gen premiseCounty="CA"
	gen level="Overall"
	tempfile CA_overall_`grow_type'
	save `CA_overall_`grow_type''
	restore



	*Statewide HHI Pernt Co
	preserve
	collapse (sum) Canopy MaxSqFt (first) businessLegalName, by(primary_company)
	collapse (sum) Canopy MaxSqFt, by(businessLegalName)
	egen industry_Canopy = total(Canopy)
	egen industry_MaxSqFt = total(MaxSqFt)
	format %15.0g Canopy MaxSqFt industry_Canopy industry_MaxSqFt

	gen mkt_share_Canopy=(Canopy/industry_Canopy)*100
	gen mkt_share2_Canopy=mkt_share_Canopy^2
	gen mkt_share_MaxSqFt=(MaxSqFt/industry_MaxSqFt)*100
	gen mkt_share2_MaxSqFt=mkt_share_MaxSqFt^2
	collapse (sum) mkt_share2_Canopy Canopy mkt_share2_MaxSqFt MaxSqFt
	gen premiseCounty="CA"
	gen level="Parent Company"
	tempfile CA_parent_`grow_type'
	save `CA_parent_`grow_type''
	restore

	*County-level HHI overall
	preserve
	collapse (sum) Canopy MaxSqFt, by(businessLegalName premiseCounty)
	egen industry_Canopy = total(Canopy), by(premiseCounty)
	egen industry_MaxSqFt = total(MaxSqFt), by(premiseCounty)
	format %15.0f Canopy MaxSqFt industry_Canopy industry_MaxSqFt

	gen mkt_share_Canopy=(Canopy/industry_Canopy)*100
	gen mkt_share2_Canopy=mkt_share_Canopy^2
	gen mkt_share_MaxSqFt=(MaxSqFt/industry_MaxSqFt)*100
	gen mkt_share2_MaxSqFt=mkt_share_MaxSqFt^2
	collapse (sum) mkt_share2_Canopy Canopy mkt_share2_MaxSqFt MaxSqFt, by(premiseCounty)
	gen level="Overall"
	tempfile county_overall_`grow_type'
	save `county_overall_`grow_type''
	restore

	*County-level HHI overall
	preserve
	collapse (sum) Canopy MaxSqFt (first) businessLegalName, by(primary_company premiseCounty)
	collapse (sum) Canopy MaxSqFt, by(businessLegalName premiseCounty)
	egen industry_Canopy = total(Canopy), by(premiseCounty)
	egen industry_MaxSqFt = total(MaxSqFt), by(premiseCounty)
	format %15.0f Canopy MaxSqFt industry_Canopy industry_MaxSqFt

	gen mkt_share_Canopy=(Canopy/industry_Canopy)*100
	gen mkt_share2_Canopy=mkt_share_Canopy^2
	gen mkt_share_MaxSqFt=(MaxSqFt/industry_MaxSqFt)*100
	gen mkt_share2_MaxSqFt=mkt_share_MaxSqFt^2
	collapse (sum) mkt_share2_Canopy Canopy mkt_share2_MaxSqFt MaxSqFt, by(premiseCounty)
	gen level="Parent Company"
	tempfile county_parent_`grow_type'
	save `county_parent_`grow_type''
	restore

	use `county_overall_`grow_type'', clear
	append using `CA_overall_`grow_type''
	append using `county_parent_`grow_type''
	append using `CA_parent_`grow_type''

	export excel using "../Results/Cult_HHI__`grow_type'", firstrow(variables) replace
}

