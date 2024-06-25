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
import { Box, Typography } from "@mui/material";

const Graph = ({ data }) => {
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

  const chartData = years.map((year, index) => {
    const yearData = { year };
    Object.keys(Data).forEach((key) => {
      yearData[key] = Data[key][index];
    });
    return yearData;
  });

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
      <ResponsiveContainer width="100%" height={600}>
        <LineChart
          data={chartData}
          margin={{ top: 5, right: 20, left: 10, bottom: 5 }}
        >
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="year" />
          <YAxis />
          <Tooltip />
          <Legend />
          {Object.keys(Data).map((key, index) => (
            <Line
              key={key}
              type="monotone"
              dataKey={key}
              stroke={colors[index % colors.length]}
              activeDot={{ r: 8 }}
            />
          ))}
        </LineChart>
      </ResponsiveContainer>
    </Box>
  );
};

export default Graph;
