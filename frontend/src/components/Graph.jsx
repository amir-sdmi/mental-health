import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from "recharts";
import { Box, Grid, Typography } from "@mui/material";

const Graphs = ({ data }) => {
  if (!data) {
    return (
      <Box>
        <Typography variant="h4" gutterBottom>
          No Data Available
        </Typography>
      </Box>
    );
  }

  const { "Start Year": startYear, "End Year": endYear, Data } = data;

  const years = [];
  for (let year = startYear; year <= endYear; year++) {
    years.push(year);
  }

  const colors = [
    "#8884d8",
    "#82ca9d",
    "#ffc658",
    "#ff7300",
    "#387908",
    "#ff0000",
    "#00ff00",
    "#0000ff",
    "#800080",
    "#ff00ff",
    "#00ffff",
    "#000000",
    "#808080",
    "#008000",
    "#800000",
    "#808000",
    "#008080",
    "#000080",
  ];

  return (
    <Box>
      <Typography variant="h4" gutterBottom>
        Mental Health and Social Metrics Over Time
      </Typography>
      <Grid container spacing={2}>
        {Object.keys(Data).map((key, index) => {
          const chartData = years.map((year, idx) => ({
            year,
            value: Data[key][idx],
          }));

          return (
            <Grid item xs={12} md={6} key={key}>
              <Box>
                <Typography variant="h5" gutterBottom>
                  {key.replace(/-/g, " ")}
                </Typography>
                <ResponsiveContainer width="100%" height={300}>
                  <LineChart
                    data={chartData}
                    margin={{ top: 5, right: 20, left: 10, bottom: 5 }}
                  >
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis dataKey="year" />
                    <YAxis />
                    <Tooltip />
                    <Legend />
                    <Line
                      type="monotone"
                      dataKey="value"
                      stroke={colors[index % colors.length]}
                      activeDot={{ r: 8 }}
                    />
                  </LineChart>
                </ResponsiveContainer>
              </Box>
            </Grid>
          );
        })}
      </Grid>
    </Box>
  );
};

export default Graphs;
