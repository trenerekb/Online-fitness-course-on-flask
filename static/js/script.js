

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


/* LIKED FUNCTION */
function like_report(reportId) {
  const likeCount = document.getElementById(`likes-count-${reportId}`);
  const likeButton = document.getElementById(`like-button-${reportId}`);

  fetch(`/report/like/${reportId}`, { method: "POST" })
    .then((res) => res.json())
    .then((data) => {
      likeCount.innerHTML = data["likes"];
      if (data["liked"] === true) {
        likeButton.className = "fas fa-heart";
      } else {
        likeButton.className = "far fa-heart";
      }
    })
 }


//function like(postId) {
//  const likeCount = document.getElementById(`likes-count-${postId}`);
//  const likeButton = document.getElementById(`like-button-${postId}`);
//
//  fetch(`/like-report/${postId}`, { method: "POST" })
//    .then((res) => res.json())
//    .then((data) => {
//      likeCount.innerHTML = data["likes"];
//      if (data["liked"] === true) {
//        likeButton.className = "fas fa-thumbs-up";
//      } else {
//        likeButton.className = "far fa-thumbs-up";
//      }
//    })
//    console.warn(xhr.responseText);
//}


// window.onscroll = () =>{
//    profile.classList.remove('active');


//    if(window.innerWidth < 1200){
//       sideBar.classList.remove('active');
//       body.classList.remove('active');
//    }
// }



