const main = document.querySelector('#main');
const projects = document.querySelector('#projects');
const contact = document.querySelector('#contact');

main.onclick = function () {
    first.style.display = "block";
    second.style.display = "none";
    third.style.display = "none";
}
projects.onclick = function () {
    first.style.display = "none";
    second.style.display = "block";
    third.style.display = "none";
}
contact.onclick = function () {
    first.style.display = "none";
    second.style.display = "none";
    third.style.display = "block";
}