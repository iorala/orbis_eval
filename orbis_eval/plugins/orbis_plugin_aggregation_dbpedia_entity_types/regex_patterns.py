# -*- coding: utf-8 -*-

base_pattern = "https?:\/\/(www\.)?(wikidata|dbpedia|schema|umbel|xmlns)\.(org|com)\/?(foaf\/0\.1|class(\/yago)?|entity|ontology|umbel\/rc)?\/"

organization_pattern = [
    "(Social)?Group",
    "Agency",
    "Bank",
    "Business",
    "CentralBank",
    "Company",
    "DrugCompany",
    "Enterprise",
    "FinancialInstitution",
    "Foundation",
    "Institution",
    "Organi(s|z)ation",
    "Q11032",
    "Q327333",
    "Q43229",
    "Q737498",
    "Wikicat.*Companies",
    "Wikicat.*Institutions",
    "Wikicat.*Organizations",
    "WikicatCompaniesBasedIn.*",
    "WikicatCompaniesEstablishedIn.*",
    "WikicatCompaniesListedOn.*",
    "WikicatDefunctCompaniesBasedIn.*",
    "WikicatMultinationalCompanies",
    "WikicatPowerCompaniesOf.*",
    "WorldOrganization",
]

person_pattern = [
    "Capitalist",
    "FictionalCharacter",
    "Governor",
    "Intellectual",
    "Investor",
    "Leader",
    "Person",
    "Politician",
    "Q215627",
    "Q5",
    "Senator",
    "SpiritualBeing",
    "Surname",
    "WikicatLivingPeople",
    "WikicatPeopleFrom.*",
]

location_pattern = [
    "AdministrativeArea",
    "AdministrativeDistrict",
    "City",
    "Country",
    "District",
    "GeographicalArea",
    "Land",
    "Location",
    "Municipality",
    "Place",
    "PopulatedPlace",
    "Q15617994",
    "Q15617994",
    "Q3455524",
    "Q6256",
    "Region",
    "Settlement",
    "State",
    "UrbanArea",
    "Village",
    "Wikicat.*Countries",
    "WikicatCountries",
    "WikicatIsIsland.*",
    "WikicatMemberStatesOf.",
    "WikicatProvincesOf.*",
    "WikicatStatesAndTerritoriesEstablished.*",
    "WikicatStatesOf.*",
    "YagoGeoEntity",
]
