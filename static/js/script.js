

let toggleBtn = document.getElementById('toggle-btn');
let body = document.body;
let darkMode = localStorage.getItem('dark-mode');

const enableDarkMode = () =>{
   toggleBtn.classList.replace('fa-sun', 'fa-moon');
   body.classList.add('dark');
   localStorage.setItem('dark-mode', 'enabled');
}

const disableDarkMode = () =>{
   toggleBtn.classList.replace('fa-moon', 'fa-sun');
   body.classList.remove('dark');
   localStorage.setItem('dark-mode', 'disabled');
}

if(darkMode === 'enabled'){
   enableDarkMode();
}

toggleBtn.onclick = (e) =>{
   darkMode = localStorage.getItem('dark-mode');
   if(darkMode === 'disabled'){
      enableDarkMode();
   }else{
      disableDarkMode();
   }
}

let profile = document.querySelector('.header .flex .profile');

document.querySelector('#user-btn').onclick = () =>{
   profile.classList.toggle('active');
   search.classList.remove('active');
}

let sideBar = document.querySelector('.side-bar');

document.querySelector('#menu-btn').onclick = () =>{
   sideBar.classList.toggle('active');
   body.classList.toggle('active');
}

document.querySelector('#close-btn').onclick = () =>{
   sideBar.classList.remove('active');
   body.classList.remove('active');
}

let addComment = document.querySelector('.box-reply-comment');

document.querySelector('#btn-comment').onclick = () =>{
   addComment.classList.toggle('box-reply-comment-active');
}



// UPLOAD FUNCTION
function upload(selector, options={}) {
   let files = []
   const images_report = document.querySelector('.images-report');
   const input = document.querySelector(selector)

   const open = document.createElement('button')

   if (options.multi) {
      input.setAttribute('multiple', true)
   }

   const triggerInput = () => input.click()

   const changeHandler = () => {
      if (!event.target.files.length) {
         return
      }
      
      files = Array.from(event.target.files)
      

      files.forEach(file => {
         if (!file.type.match('image')) {
            return
         }

         
         const reader = new FileReader()

         reader.onload = ev => {
            const img = document.createElement('img');
            

            images_report.insertAdjacentHTML('afterbegin', `<div class="img-report">
            <div class="preview-remove" data-name="${file.name}">&times;</div>
            <img src="${reader.result}" alt="${file.name}"/></div>`)
         }

         reader.readAsDataURL(file)

      })

   }

   const removeHandler = event => {
      if (!event.target.dataset.name) {
         return
      }

      const {name} = event.target.dataset
      files = files.filter(file => file.name !== name)

      const block = images_report.querySelector(`[data-name="${name}"]`).closest('.img-report')
      block.remove()
   }

   open.addEventListener('click', triggerInput)
   input.addEventListener('change', changeHandler)
   images_report.addEventListener('click', removeHandler )

}

upload('#file', {multi: true})  
// UPLOAD FUNCTION





// let images_report = document.querySelector('.images-report');

// function donwload(input) {
//    let files = input.files;
//    if(files) {
//       for (var i = 0; i < files.length; i++) {
//          let file = files[i]
//          console.log(file);
//          let reader = new FileReader();

//          reader.onload = function(file) {
         
//             console.log(file);
//             let img = document.createElement('img');
//             images_report.appendChild(img);
            
//             reader.readAsDataURL(file);
//             img.src = reader.result;
//             img.style.width = '25%';
//             img.style.height = '25%';
//          }
//       }
//    }


// window.onscroll = () =>{
//    profile.classList.remove('active');


//    if(window.innerWidth < 1200){
//       sideBar.classList.remove('active');
//       body.classList.remove('active');
//    }
// }



