//setup materialize components
document.addEventListener('DOMContentLoaded', function() {
    var modals = document.querySelectorAll('.modal');
    M.Modal.init(modals);

    var items = document.querySelectorAll('.collapsible');
    M.Collapsible.init(items);
});



const loggedOutNav = document.querySelectorAll('.logged-out');
const loggedInNav = document.querySelectorAll('.logged-in');

const userEmail1 = document.querySelector('.user-email1');
const userEmail2 = document.querySelector('.user-email2');
const emailHTML = document.getElementById('account-details')
const usernameHTML = document.getElementById('account-username')
const goalHTML = document.getElementById('account-goal')


const setUpNav = (user) => {
    if (user) {
        // toggle UI
        loggedInNav.forEach(item => item.style.display = 'block');
        loggedOutNav.forEach(item => item.style.display = 'none');


        //account info
        db.collection('users').doc(user.uid).get().then(doc => {
            const userUsername = doc.data().username;
            console.log(userUsername);
            usernameHTML.innerHTML = userUsername;

            const userGoal = doc.data().goal;
            console.log(userGoal);
            goalHTML.innerHTML = userGoal;

            const userEmail = user.email;
            console.log(userEmail);
            emailHTML.innerHTML = userEmail;

            const hiddenEmailHTML = `<input hidden id="email" name="email" value="${user.email}">`;
            userEmail1.innerHTML = hiddenEmailHTML;
            userEmail2.innerHTML = hiddenEmailHTML;
        })









    }
    else{
        // toggle UI
        loggedInNav.forEach(item => item.style.display = 'none');
        loggedOutNav.forEach(item => item.style.display = 'block');
        userEmail1.innerHTML= '';
        userEmail2.innerHTML= '';

    }
}