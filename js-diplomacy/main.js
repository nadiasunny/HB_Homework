// 'use strict';
// let colChanBtn = document.querySelector('.color-changer');
// colChanBtn.addEventListener('click', () =>{
//     document.querySelector('.color-change').add('red');
// });

function returnMessage(evt){
    evt.preventDefault();
    const num = document.querySelector('#number-input');
    if (typeof num !== 'number' || num >= 10){
        document.querySelector('#formFeedback').innerHTML = 'Please enter a smaller number';
    }
    else {
        document.querySelector('#formFeedback').innerHTML = 'You are good to go!';

    }
};


function changeColor(){
    let toChange = document.querySelectorAll('.color-change');
    for (elem of toChange){
        elem.classList.add('red');
        //elem.style.color = red;
    }
}

document.querySelector('.number-form').addEventListener('click', returnMessage)
document.querySelector('.color-changer').addEventListener('click', changeColor);