import { Autocomplete, TextField } from "@mui/material";
import countriesList from "../../utils/country";

function CountrySelector({ handleCountryChange }) {
  return (
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
  );
}

export default CountrySelector;
