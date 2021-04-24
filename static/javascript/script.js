$(document).ready(function () {
    $('.sidenav').sidenav();
    $('.carousel').carousel();
    $('select').formSelect();
});
$('.carousel.carousel-slider').carousel({
    fullWidth: true,
    indicators: true
});

function navigate(event, item) {
    debugger;
    event.stopPropagation();
    console.log(event, item)
}