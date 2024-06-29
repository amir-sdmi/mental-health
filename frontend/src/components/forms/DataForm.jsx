import { useState } from "react";
import { Box, Typography, Button } from "@mui/material";
import HappinessList from "../../utils/happiness";
import disordersList from "../../utils/disorders";
import CountrySelector from "./CountrySelector";
import DisorderSelector from "./DisorderSelector";
import HappinessSelector from "./HappinessSelector";
import YearSlider from "./YearSlider";
import ErrorAlert from "./ErrorAlert";

function DataForm({ setResultData }) {
  const [selectedCountry, setSelectedCountry] = useState("");
  const [selectedDisorders, setSelectedDisorders] = useState([]);
  const [disorders, setDisorders] = useState(disordersList);
  const [selectedHappiness, setSelectedHappiness] = useState([]);
  const [happinesses, setHappinesses] = useState(HappinessList);
  const [years, setYears] = useState([2005, 2017]);
  const [error, setError] = useState("");

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

  const handleCountryChange = (event, newValue) => {
    setSelectedCountry(newValue);
  };

  const handleSubmit = (event) => {
    event.preventDefault();

    if (!selectedCountry) {
      setError("Country is required");
      return;
    }

    const queryParameters = new URLSearchParams();

    selectedDisorders.forEach((disorder) => {
      queryParameters.append(disorder, "true");
    });

    selectedHappiness.forEach((happiness) => {
      queryParameters.append(happiness, "true");
    });

    const url = `http://127.0.0.1:5000/data/${selectedCountry}/${years[0]}/${
      years[1]
    }?${queryParameters.toString()}`;

    fetch(url, {
      method: "GET",
    })
      .then((response) => response.json())
      .then((data) => {
        console.log("Success:", JSON.stringify(data, null, 2));
        setResultData(data);
        setError("");
      })
      .catch((error) => {
        console.error("Error:", error);
        setError("Failed to fetch data");
      });
  };

  return (
    <Box width="300px">
      <Typography variant="h2">Data Form</Typography>
      <Box component="form" onSubmit={handleSubmit} noValidate>
        <CountrySelector
          selectedCountry={selectedCountry}
          handleCountryChange={handleCountryChange}
        />
        <DisorderSelector
          disorders={disorders}
          selectedDisorders={selectedDisorders}
          handleDisorderChange={handleDisorderChange}
          handleRemoveDisorder={handleRemoveDisorder}
        />
        <HappinessSelector
          happinesses={happinesses}
          selectedHappiness={selectedHappiness}
          handleHappinessChange={handleHappinessChange}
          handleRemoveHappiness={handleRemoveHappiness}
        />
        <YearSlider years={years} handleChangeYears={handleChangeYears} />
        <Box mt={2}>
          <Button type="submit" variant="contained" color="primary">
            Submit
          </Button>
        </Box>
      </Box>
      <ErrorAlert error={error} />
    </Box>
  );
}

export default DataForm;
