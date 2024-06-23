import { useState } from "react";
import { Box, TextField, MenuItem, Slider, Autocomplete } from "@mui/material";
const countriesList = [
  "Afghanistan",
  "Albania",
  "Algeria",
  "Andorra",
  "Angola",
  "Antigua and Barbuda",
  "Argentina",
  "Armenia",
  "Australia",
  "Austria",
  "Azerbaijan",
  "Bahamas",
  "Bahrain",
  "Bangladesh",
  "Barbados",
  "Belarus",
  "Belgium",
  "Belize",
  "Benin",
  "Bhutan",
  "Bolivia",
  "Bosnia and Herzegovina",
  "Botswana",
  "Brazil",
  "Brunei",
  "Bulgaria",
  "Burkina Faso",
  "Burundi",
  "Cabo Verde",
  "Cambodia",
  "Cameroon",
  "Canada",
  "Central African Republic",
  "Chad",
  "Chile",
  "China",
  "Colombia",
  "Comoros",
  "Congo",
  "Costa Rica",
  "Croatia",
  "Cuba",
  "Cyprus",
  "Czech Republic",
  "Denmark",
  "Djibouti",
  "Dominica",
  "Dominican Republic",
  "East Timor",
  "Ecuador",
  "Egypt",
  "El Salvador",
  "Equatorial Guinea",
  "Eritrea",
  "Estonia",
  "Eswatini",
  "Ethiopia",
  "Fiji",
  "Finland",
  "France",
  "Gabon",
  "Gambia",
  "Georgia",
  "Germany",
  "Ghana",
  "Greece",
  "Grenada",
  "Guatemala",
  "Guinea",
  "Guinea-Bissau",
  "Guyana",
  "Haiti",
  "Honduras",
  "Hungary",
  "Iceland",
  "India",
  "Indonesia",
  "Iran",
  "Iraq",
  "Ireland",
  "Israel",
  "Italy",
  "Jamaica",
  "Japan",
  "Jordan",
  "Kazakhstan",
  "Kenya",
  "Kiribati",
  "Korea, North",
  "Korea, South",
  "Kosovo",
  "Kuwait",
  "Kyrgyzstan",
  "Laos",
  "Latvia",
  "Lebanon",
  "Lesotho",
  "Liberia",
  "Libya",
  "Liechtenstein",
  "Lithuania",
  "Luxembourg",
  "Madagascar",
  "Malawi",
  "Malaysia",
  "Maldives",
  "Mali",
  "Malta",
  "Marshall Islands",
  "Mauritania",
  "Mauritius",
  "Mexico",
  "Micronesia",
  "Moldova",
  "Monaco",
  "Mongolia",
  "Montenegro",
  "Morocco",
  "Mozambique",
  "Myanmar",
  "Namibia",
  "Nauru",
  "Nepal",
  "Netherlands",
  "New Zealand",
  "Nicaragua",
  "Niger",
  "Nigeria",
  "North Macedonia",
  "Norway",
  "Oman",
  "Pakistan",
  "Palau",
  "Panama",
  "Papua New Guinea",
  "Paraguay",
  "Peru",
  "Philippines",
  "Poland",
  "Portugal",
  "Qatar",
  "Romania",
  "Russia",
  "Rwanda",
  "Saint Kitts and Nevis",
  "Saint Lucia",
  "Saint Vincent and the Grenadines",
  "Samoa",
  "San Marino",
  "Sao Tome and Principe",
  "Saudi Arabia",
  "Senegal",
  "Serbia",
  "Seychelles",
  "Sierra Leone",
  "Singapore",
  "Slovakia",
  "Slovenia",
  "Solomon Islands",
  "Somalia",
  "South Africa",
  "South Sudan",
  "Spain",
  "Sri Lanka",
  "Sudan",
  "Suriname",
  "Sweden",
  "Switzerland",
  "Syria",
  "Taiwan",
  "Tajikistan",
  "Tanzania",
  "Thailand",
  "Togo",
  "Tonga",
  "Trinidad and Tobago",
  "Tunisia",
  "Turkey",
  "Turkmenistan",
  "Tuvalu",
  "Uganda",
  "Ukraine",
  "United Arab Emirates",
  "United Kingdom",
  "United States",
  "Uruguay",
  "Uzbekistan",
  "Vanuatu",
  "Vatican City",
  "Venezuela",
  "Vietnam",
  "Yemen",
  "Zambia",
  "Zimbabwe",
];
const disordersList = [
  "Schizophrenia",
  "Bipolar Disorders",
  "Eating Disorders",
  "Anxiety Disorders",
  "Depression",
  "Alcohol Disorders",
];
const HappinessList = [
  "life Ladder",
  "GDP",
  "Social Support",
  "Healthy Life Expectancy",
  "Freedom to make life choices",
  "Generosity",
  "Perceptions of corruption",
  "Positive affect",
  "Negative affect",
  "Confidence in national government",
];
function DataFrom() {
  const [selectedCountry, setSelectedCountry] = useState("");
  const [selectedDisorders, setSelectedDisorders] = useState([]);
  const [disorders, setDisorders] = useState(disordersList);
  const [selectedHappiness, setSelectedHappiness] = useState([]);
  const [happinesses, setHappinesses] = useState(HappinessList);
  const [years, setYears] = useState([2005, 2017]);

  const handleCountryChange = (e) => {
    setSelectedCountry(e.target.value);
  };
  const handleDisorderChange = (e) => {
    const selectedOption = e.target.value;
    if (selectedOption && !selectedDisorders.includes(selectedOption)) {
      setSelectedDisorders([...selectedDisorders, selectedOption]);
      setDisorders(disorders.filter((disorder) => disorder !== selectedOption));
    }
  };

  const handleRemoveDisorder = (disorder) => {
    setSelectedDisorders(selectedDisorders.filter((item) => item !== disorder));
    setDisorders([...disorders, disorder]);
  };

  const handleHappinessChange = (e) => {
    const selectedOption = e.target.value;
    if (selectedOption && !selectedHappiness.includes(selectedOption)) {
      setSelectedHappiness([...selectedHappiness, selectedOption]);
      setHappinesses(
        happinesses.filter((happiness) => happiness !== selectedOption)
      );
    }
  };
  const handleRemoveHappiness = (happiness) => {
    setSelectedHappiness(
      selectedHappiness.filter((item) => item !== happiness)
    );
    setHappinesses([...happinesses, happiness]);
  };

  const handleChangeYears = (e, newValue, activeThumb) => {
    if (!Array.isArray(newValue)) {
      return;
    }
    const minDistance = 1;
    if (activeThumb === 0) {
      setYears([Math.min(newValue[0], years[1] - minDistance), years[1]]);
    } else {
      setYears([years[0], Math.max(newValue[1], years[0] + minDistance)]);
    }
  };
  return (
    <Box width="300px">
      <h1>Data Form</h1>
      <form>
        <Autocomplete
          disablePortal
          id="countrySelect"
          options={countriesList}
          sx={{ width: 300 }}
          renderInput={(params) => (
            <TextField
              {...params}
              label="Select a country"
              onChange={handleCountryChange}
            />
          )}
        />

        <TextField
          label="Select a disorder"
          select
          onChange={handleDisorderChange}
          fullWidth
          placeholder="Select a disorder"
        >
          {disorders.map((disorder) => (
            <MenuItem key={disorder} value={disorder}>
              {disorder}
            </MenuItem>
          ))}
        </TextField>
        <TextField
          label="Select a happiness"
          select
          onChange={handleHappinessChange}
          fullWidth
        >
          {happinesses.map((happiness) => (
            <MenuItem key={happiness} value={happiness}>
              {happiness}
            </MenuItem>
          ))}
        </TextField>

        <Slider
          getAriaLabel={() => "Years range"}
          value={years}
          onChange={handleChangeYears}
          valueLabelDisplay="on"
          min={2005}
          max={2017}
          step={1}
          defaultValue={[2005, 2017]}
          disableSwap
          marks
        />
      </form>

      <div>
        <h2>Selected Disorders:</h2>
        <ul>
          {selectedDisorders.map((disorder) => (
            <li key={disorder}>
              <span
                style={{ cursor: "pointer", color: "red", marginRight: "10px" }}
                onClick={() => handleRemoveDisorder(disorder)}
              >
                &#x2716;
              </span>
              {disorder}
            </li>
          ))}
        </ul>
        <h2>Selected Country:</h2>
        <p>{selectedCountry}</p>
        <h2>Selected Happiness:</h2>
        <ul>
          {selectedHappiness.map((happiness) => (
            <li key={happiness}>
              <span
                style={{ cursor: "pointer", color: "red", marginRight: "10px" }}
                onClick={() => handleRemoveHappiness(happiness)}
              >
                &#x2716;
              </span>
              {happiness}
            </li>
          ))}
        </ul>
      </div>
    </Box>
  );
}

export default DataFrom;
