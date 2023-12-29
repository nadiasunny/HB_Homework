function submitProfile(evt) {
  evt.preventDefault();

  const data = {
    name: document.querySelector('#name-field').value,
    age: document.querySelector('#age-field').value,
    occupation: document.querySelector('#occupation-field').value,
    //education: document.querySelector('education').value,
    //salary: document.querySelector('salary').value,
    //city: document.querySelector('city').value,
    //state: document.querySelector('#state-field').value,
    //garden: document.querySelector('garden').value,
    //tv: document.querySelector('tv').value,
    // fill in the rest
  };

  // make request to server to get the data
  // add the data the server returns to the document
  // (you can add it to the end of the div with ID "profiles")
  fetch('/api/profile', {
    method: 'POST',
    body: JSON.stringify(data),
    headers: {
      "Content-Type": "application/json",
    }
  })
  .then((response) => response.json())
  .then((profile) => {
    console.log(profile);
    
    let profiles = document.getElementById('profiles');
    profiles.insertAdjacentHTML('beforeend', `<p>${profile.fullname} is ${profile.age}, working as a ${profile.occupation}.</p>`)
  })
}

document.querySelector('#profile-form').addEventListener('submit', submitProfile);
