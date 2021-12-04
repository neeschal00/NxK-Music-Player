var elem = document.getElementById("aplayer");
if(elem.classList.contains("aplayer-narrow")){
elem.classList.remove("aplayer-narrow");
}
$(document).ready(function(){
    $('.aplayer-body').css({
      'width': '100%',
      'background-color': '#191922'
    });
});
