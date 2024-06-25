import { useState } from "react";
import {
  Box,
  TextField,
  MenuItem,
  Slider,
  Autocomplete,
  Typography,
  IconButton,
  List,
  ListItem,
  ListItemText,
  ListItemSecondaryAction,
  Button,
  Alert,
} from "@mui/material";
import CloseIcon from "@mui/icons-material/Close";
import HappinessList from "../../utils/happiness";
import countriesList from "../../utils/country";
import disordersList from "../../utils/disorders";

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
        console.log("Success:", data);
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
        <Autocomplete
          id="countrySelect"
          sx={{ width: 300 }}
          options={countriesList}
          autoHighlight
          onChange={handleCountryChange}
          renderInput={(params) => (
            <TextField
              {...params}
              label="Select a country"
              required
              inputProps={{
                ...params.inputProps,
                autoComplete: "new-password",
              }}
            />
          )}
        />

        <TextField
          label="Select a disorder"
          select
          onChange={handleDisorderChange}
          fullWidth
          margin="normal"
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
          margin="normal"
        >
          {happinesses.map((happiness) => (
            <MenuItem key={happiness} value={happiness}>
              {happiness}
            </MenuItem>
          ))}
        </TextField>

        <Box mt={2}>
          <Typography gutterBottom>Years range</Typography>
          <Slider
            getAriaLabel={() => "Years range"}
            value={years}
            onChange={handleChangeYears}
            valueLabelDisplay="on"
            min={2005}
            max={2017}
            step={1}
            disableSwap
            marks
          />
        </Box>
        <Box mt={2}>
          <Button type="submit" variant="contained" color="primary">
            Submit
          </Button>
        </Box>
      </Box>

      {error && (
        <Box mt={2}>
          <Alert severity="error">{error}</Alert>
        </Box>
      )}

      <Box mt={2}>
        <Typography variant="h5">Selected Disorders:</Typography>
        <List>
          {selectedDisorders.map((disorder) => (
            <ListItem key={disorder}>
              <ListItemText primary={disorder} />
              <ListItemSecondaryAction>
                <IconButton
                  edge="end"
                  color="secondary"
                  onClick={() => handleRemoveDisorder(disorder)}
                >
                  <CloseIcon />
                </IconButton>
              </ListItemSecondaryAction>
            </ListItem>
          ))}
        </List>

        <Typography variant="h5">Selected Country:</Typography>
        <Typography>{selectedCountry}</Typography>

        <Typography variant="h5">Selected Happiness:</Typography>
        <List>
          {selectedHappiness.map((happiness) => (
            <ListItem key={happiness}>
              <ListItemText primary={happiness} />
              <ListItemSecondaryAction>
                <IconButton
                  edge="end"
                  color="secondary"
                  onClick={() => handleRemoveHappiness(happiness)}
                >
                  <CloseIcon />
                </IconButton>
              </ListItemSecondaryAction>
            </ListItem>
          ))}
        </List>
      </Box>
    </Box>
  );
}

export default DataForm;
