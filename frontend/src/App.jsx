import { Container, Grid } from "@mui/material";
import DataFrom from "./components/forms/DataFrom";
import Graph from "./components/Graph";
import "./App.css";

function App() {
  return (
    <Container>
      <Grid container spacing={2}>
        <Grid item xs={12} md={4}>
          <DataFrom />
        </Grid>
        <Grid item xs={12} md={8}>
          <Graph />
        </Grid>
      </Grid>
    </Container>
  );
}

export default App;
