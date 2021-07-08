$(document).ready(function () {
    $('.sidenav').sidenav();
    $('select').formSelect();
    $('.modal').modal();
    $('.carousel.carousel-slider').carousel({
        fullWidth: true,
        indicators: false,
    });
    $('#backButton').click(function () {
        $('.carousel').carousel('prev');
    });

    $('#nextButton').click(function () {
        $('.carousel').carousel('next');
    });

    $(".dropdown-trigger").dropdown({
        coverTrigger: false
    });
});

$(function () {
    setTimeout(function () {
        $('.flashMessages').slideUp(500);
    }, 1000);
});