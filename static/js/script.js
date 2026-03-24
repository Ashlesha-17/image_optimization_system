const slider = document.getElementById("slider");
const afterImage = document.getElementById("afterImage");

if (slider) {
    slider.addEventListener("input", function () {
        let value = slider.value;
        afterImage.style.clipPath = `inset(0 ${100 - value}% 0 0)`;
    });
}