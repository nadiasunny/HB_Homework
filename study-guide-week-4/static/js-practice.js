'use strict';

/** ********************
 Make an Event Handler
********************* */
//when user clicks button log in(id=login-button) 
// test should update to "log out"
//if button clicked again, text should switch to 'Log in'
function popUp(){
  return alert('I am a poppin!');
}

document.querySelector('#popup-alert-button').addEventListener('click', popUp);

/** ***********************
Practice Your Times Tables
************************ */
//prevent from going to default route
//read values from form & create array 
//containing multiples of requested number up&include max
function timeTable(evt){
  evt.preventDefault();
 
  let num = document.querySelector('#mults-of').value;
  let max = document.querySelector('#max').value;
  console.log(num, max);
  num = Number(num);
  max = Number(max);
  let multiples = [];

    for(let i = 1; i<=max; i++){
      if(i*num <= max){
        multiples.push(num*i);
      }
    }

  console.log(multiples);
}

document.querySelector('#multiplying-form').addEventListener('submit', timeTable);
/** **************
An Agreeable Form
*************** */

//prevent default
//add text to div to be an agreeable sentence
//add event listener to form submission
function iAgree(evt){
  evt.preventDefault();
  let food = document.querySelector('#favorite-food-input').value;
  let sentence = `My favorite food is ${food}, as well!`;
  document.querySelector('#agreeable-text').innerHTML = sentence;
}
document.querySelector('#agreeable-form').addEventListener('submit', iAgree); 

/** ****************
Five colored primes
***************** */

const PRIME_COLORS = ['orange', 'midnightblue', 'darkgoldenrod', 'green', 'purple'];
function primeTime(evt){
  let box = document.querySelector('#prime-circle-area')
  for(let i=1; i <=11; i++){
    if(i%2!==0){
      box.insertAdjacentHTML('beforeend', 
      `<div class="prime-circle" style="background-color: ${PRIME_COLORS[Math.floor(Math.random()*5)]}">${i}</div>`);
    }
  }
}
document.querySelector('#make-prime-circles').addEventListener('click', primeTime);
// Your Code Here

/** *********
Got Puppies?
********** */

// NOTE: DO NOT CHANGE THE CODE OF THIS FUNCTION
function showPuppies(results) {
  // get the URL for the puppy photo out of the results object
  const puppyURL = results.url;
  const puppyDiv = document.querySelector('#puppies-go-here');
  // clear anything currently in the div
  puppyDiv.innerHTML = null;
  // add the img element
  puppyDiv.insertAdjacentHTML('beforeend', `<img src=${puppyURL} alt="puppy-image">`);
}

// Your Code Here
function puppers(evt){
  evt.preventDefault();
  
  let pupper = document.querySelector('#num-puppies').value;
  console.log(pupper)
  let url = `/puppies.json?num-puppies=${pupper}`;
  fetch(url)
  .then((response) => response.json())
  .then((responseData) => {
    return showPuppies(responseData);
  
  });
  }

document.querySelector('#puppy-form').addEventListener('submit', puppers)