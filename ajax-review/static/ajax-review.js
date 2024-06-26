// PART 1: SHOW A FORTUNE

function showFortune(evt) {
  // TODO: get the fortune and show it in the fortune-text div
  fortuneText = document.querySelector('#fortune-text');

  fetch('/fortune')
  .then((response) => response.text())
  .then((data) => {
    console.log(data)
    fortuneText.textContent = data;
  })
}

document.querySelector('#get-fortune-button').addEventListener('click', showFortune);

// PART 2: SHOW WEATHER

function showWeather(evt) {
  evt.preventDefault();
  const zipcode = document.querySelector('#zipcode-field').value;
  const url = `/weather.json?zipcode-field=${zipcode}`;
  // TODO: request weather with that URL and show the forecast in #weather-info
  fetch(url)
  .then((response) => response.json())
  .then((data) => {
    document.querySelector('#weather-info').innerHTML = data['forecast'];
  });
}

document.querySelector('#weather-form').addEventListener('submit', showWeather);
