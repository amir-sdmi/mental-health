import { Box, Alert } from "@mui/material";

function ErrorAlert({ error }) {
  return (
    error && (
      <Box mt={2}>
        <Alert severity="error">{error}</Alert>
      </Box>
    )
  );
}

export default ErrorAlert;
