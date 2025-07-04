document.getElementById("wineForm").addEventListener("submit", async function(e) {
  e.preventDefault();

  const formData = new FormData(this);
  const data = {};
  formData.forEach((value, key) => {
    data[key] = parseFloat(value);
  });

  const response = await fetch("/wine/winepredict", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(data)
  });

  const result = await response.json();
  document.getElementById("result").innerText = `The wine quality is ${result}`;
});
