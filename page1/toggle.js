window.onload = function () {
  var button = document.getElementById("toggle");

  button.onclick = function () {
    document.body.classList.toggle("light");
  };
};