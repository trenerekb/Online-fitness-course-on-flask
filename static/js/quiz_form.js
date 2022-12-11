// QUIZ FORM DAY 0

let form1 = document.getElementById('Form1');
let form2 = document.getElementById('Form2');
let form3 = document.getElementById('Form3');

let next1 = document.getElementById('Next1');
let next2 = document.getElementById('Next2');

let back1 = document.getElementById('Back1');
let back2 = document.getElementById('Back2');

let progress = document.getElementById('progress');

next1.onclick = function() {
   form1.style.left = '-1200px';
   form2.style.left = '0px';
   form2.style.position = 'relative';
   progress.style.width = '66%';
}

back1.onclick = function() {
   form1.style.left = '0px';
   form2.style.left = '1200px';
   progress.style.width = '33%';
}

next2.onclick = function() {
   form2.style.left = '-1200px';
   form3.style.left = '0';
   form3.style.top = '5rem';
   progress.style.width = '100%';
}

back2.onclick = function() {
   form2.style.left = '0px';
   form3.style.left = '1200px';
   progress.style.width = '66%';
}


