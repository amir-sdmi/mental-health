import { Container, Grid } from "@mui/material";
import DataForm from "./components/forms/DataForm";
import Graph from "./components/Graph";
import "./App.css";

function App() {
  return (
    <Container>
      <Grid container spacing={2}>
        <Grid item xs={12} md={4}>
          <DataForm />
        </Grid>
        <Grid item xs={12} md={8}>
          <Graph />
        </Grid>
      </Grid>
    </Container>
  );
}

export default App;
