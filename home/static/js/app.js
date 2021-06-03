const sidebar = document.querySelector('.sidebar-custom');
const expandIcon = document.getElementsByClassName('expand-icon');

function navOpen() {
    sidebar.classList.toggle('open');

}

for (var i = 0; i < expandIcon.length; i++) {
    expandIcon[i].addEventListener('click', navOpen, false);
}

// expandIcon.addEventListener('click', () => {
//     sidebar.classList.toggle('open');
// });