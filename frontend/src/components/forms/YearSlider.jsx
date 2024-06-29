import { Box, Typography, Slider } from "@mui/material";

function YearSlider({ years, handleChangeYears }) {
  return (
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
  );
}

export default YearSlider;
