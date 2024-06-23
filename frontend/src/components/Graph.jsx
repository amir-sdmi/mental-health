import { LineChart } from "@mui/x-charts/LineChart";

const data = {
  Country: "Germany",
  "Start Year": 2015,
  "End Year": 2017,
  Data: {
    "Anxiety-disorders": {
      2015: 6.566759,
      2016: 6.54799,
      2017: 6.540496,
    },
    "Alcohol-use-disorders": {
      2015: 1.927178,
      2016: 1.874791,
      2017: 1.806475,
    },
    "Eating-disorders": {
      2015: 0.522847,
      2016: 0.521596,
      2017: 0.522066,
    },
    "Drug-use-disorders": {
      2015: 0.893847,
      2016: 0.8909,
      2017: 0.883827,
    },
    Schizophrenia: {
      2015: 0.25172,
      2016: 0.251956,
      2017: 0.252269,
    },
    Depression: {
      2015: 3.946206,
      2016: 3.949598,
      2017: 3.959866,
    },
    "Bipolar-disorder": {
      2015: 0.779517,
      2016: 0.777822,
      2017: 0.776762,
    },
    GDP: {
      2015: 10.84269905,
      2016: 10.85668278,
      2017: 10.87939453,
    },
    "Freedom-to-make-life-choices": {
      2015: 0.889428854,
      2016: 0.870515049,
      2017: 0.840727866,
    },
    "Healthy-life-expectancy-at-birth": {
      2015: 70.09999847,
      2016: 70.30000305,
      2017: 70.5,
    },
    "Negative-affect": {
      2015: 0.20270516,
      2016: 0.187254936,
      2017: 0.196434811,
    },
    Generosity: {
      2015: 0.175080508,
      2016: 0.145733327,
      2017: 0.142413303,
    },
    "Confidence-in-national-government": {
      2015: 0.628003657,
      2016: 0.552613556,
      2017: 0.622935653,
    },
    "Perceptions-of-corruption": {
      2015: 0.412168294,
      2016: 0.445922136,
      2017: 0.414021194,
    },
    "Social-support": {
      2015: 0.925923228,
      2016: 0.906029284,
      2017: 0.892166078,
    },
    "Positive-affect": {
      2015: 0.72238481,
      2016: 0.709376156,
      2017: 0.707113683,
    },
    "Life-Ladder": {
      2015: 7.037137508,
      2016: 6.873763084,
      2017: 7.074324608,
    },
  },
};

const years = ["2015", "2016", "2017"];

const series = Object.keys(data.Data).map((key) => ({
  label: key,
  data: years.map((year) => data.Data[key][year]),
}));

const xLabels = years.map((year) => ({ label: year, value: year }));

export default function Graph() {
  return (
    <LineChart
      xAxis={[{ data: xLabels }]}
      series={series}
      width={1000}
      height={1000}
    />
  );
}
