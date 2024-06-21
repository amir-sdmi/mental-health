import { useState, useEffect } from "react";
import { UserData } from "./Data";
import { Bar } from "react-chartjs-2";
function App() {
  const [userData, setUserData] = useState({
    labels: [],
    datasets: [],
  });

  useEffect(() => {
    const labels = Object.keys(UserData.Data);
    const data2015 = labels.map((label) => UserData.Data[label][2015]);
    const data2016 = labels.map((label) => UserData.Data[label][2016]);
    const data2017 = labels.map((label) => UserData.Data[label][2017]);
    setUserData({
      labels,
      datasets: [
        {
          label: 2015,
          data: data2015,
          backgroundColor: "rgba(255, 99, 132, 0.2)",
          borderColor: "rgba(255, 99, 132, 1)",
          borderWidth: 1,
        },
        {
          label: 2016,
          data: data2016,
          backgroundColor: "rgba(54, 162, 235, 0.2)",
          borderColor: "rgba(54, 162, 235, 1)",
          borderWidth: 1,
        },
        {
          label: 2017,
          data: data2017,
          backgroundColor: "rgba(255, 206, 86, 0.2)",
          borderColor: "rgba(255, 206, 86, 1)",
          borderWidth: 1,
        },
      ],
    });
  }, []);
  return (
    <div>
      <Bar data={userData} />
    </div>
  );
}

export default App;
