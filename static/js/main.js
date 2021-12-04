// expander menu
const showMenu = (toggleId,navbarId,tagsec)=>{
    const toggle = document.getElementById(toggleId),
    navbar = document.getElementById(navbarId),
    sectionpadding = document.getElementById(tagsec)

    if(toggle && navbar){
        toggle.addEventListener('click', ()=>{
            navbar.classList.toggle('expander')
            sectionpadding.classList.toggle('body-pd')
        })
    }
}
showMenu('nav-toggle', 'navbar','body-pd')


// link-active color
let linkColor = document.querySelectorAll('.nav__link')
function colorLink(){
  linkColor.forEach(l =>l.classList.remove('active'));
  this.classList.add('active');
}
linkColor.forEach(l =>l.addEventListener('click', colorLink))

