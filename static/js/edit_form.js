

// EDIT REPORT
window.onload = function() {
    let editActive = document.getElementById('edit-active')
    let firstReportCurrentUser = document.getElementById('first-report-current-user')
    document.getElementById('btn-edit-report').onclick = () => {
        firstReportCurrentUser.remove();
        editActive.style.display = 'block';
        }
    }


//window.onload = function() {
//    let addComment = document.querySelector('.box-reply-comment')
//    let editActive = document.querySelector('.edit-active')
//    let editReport = document.getElementById('edit-report')
//    document.getElementById('btn-edit-report').onclick = () => {
//    editReport.remove();
//    editActive.style.display = 'block';
//    }
//}