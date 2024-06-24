import { LineChart } from "@mui/x-charts/LineChart";

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
