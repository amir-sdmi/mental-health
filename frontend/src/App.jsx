import { useState } from "react";
import { Container, Grid } from "@mui/material";
import DataForm from "./components/forms/DataForm";
import Graphs from "./components/Graph";
import "./App.css";

function App() {
  const [resultData, setResultData] = useState(null);

  return (
    <Container>
      <Grid container spacing={2}>
        <Grid item xs={12} md={4}>
          <DataForm setResultData={setResultData} />
        </Grid>
        <Grid item xs={12} md={8}>
          {resultData && <Graphs data={resultData} />}
        </Grid>
      </Grid>
    </Container>
  );
}

export default App;
