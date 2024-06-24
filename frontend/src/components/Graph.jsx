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

const sampleData = {
  Country: "Canada",
  "Start Year": 2010,
  "End Year": 2015,
  Data: {
    "Alcohol-use-disorders": [
      1.589404, 1.59254, 1.59601, 1.599727, 1.603801, 1.608215,
    ],
    "Eating-disorders": [
      0.47038, 0.470892, 0.471709, 0.472149, 0.473426, 0.474343,
    ],
    "Anxiety-disorders": [
      5.163625, 5.163595, 5.164413, 5.165811, 5.167921, 5.170797,
    ],
    "Drug-use-disorders": [
      2.19518, 2.188105, 2.187286, 2.19462, 2.207245, 2.22515,
    ],
    Depression: [3.911885, 3.913974, 3.919381, 3.926503, 3.936199, 3.949642],
    "Bipolar-disorder": [
      0.713705, 0.713801, 0.714027, 0.714322, 0.71471, 0.715199,
    ],
    Schizophrenia: [0.314014, 0.314082, 0.314213, 0.314388, 0.314617, 0.314901],
    "Confidence-in-national-government": [
      0.551076472, 0.553290546, 0.523448169, 0.505976021, 0.516953588,
      0.644104123,
    ],
    "Social-support": [
      0.953765452, 0.921669245, 0.948128343, 0.936239362, 0.917836308,
      0.939067066,
    ],

    "Negative-affect": [
      0.233112857, 0.247728661, 0.229332089, 0.262850314, 0.258602411,
      0.286280215,
    ],
    "Positive-affect": [
      0.791042447, 0.802899837, 0.775568783, 0.800634027, 0.790682673,
      0.791708946,
    ],

    "Perceptions-of-corruption": [
      0.412659585, 0.432991534, 0.465601832, 0.406236142, 0.441735327,
      0.427152246,
    ],
    "Freedom-to-make-life-choices": [
      0.933948815, 0.950925291, 0.917961121, 0.916013896, 0.93889761,
      0.931468964,
    ],
    Generosity: [
      0.22833468, 0.251015067, 0.287870497, 0.313492298, 0.267686814,
      0.250650674,
    ],
  },
};

const Graph = ({ data = sampleData }) => {
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
