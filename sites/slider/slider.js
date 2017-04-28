var slideIndex = 1;
showSlides(slideIndex);

function plusSlide(n) {
	showSlides(slideIndex += n);
}

function currentSlide(n) {
	showSlides(slideIndex = n);
}

function showSlides(n) {
	var slides = document.getElementsByClassName("slide");
	var dots = document.getElementsByClassName("dot");
	if(n > slides.length) {
		slideIndex = 1;
	}
	if(n < 1) {
		slideIndex = slides.length;
	}
	for(var i = 0; i < slides.length; i++) {
		slides[i].style.display = "none";
	}
	slides[slideIndex - 1].style.display = "block";

	for(var i = 0; i < dots.length; i++) {
		dots[i].style.background = "#BBB";
	}
	dots[slideIndex - 1].style.background = "#666";
}
