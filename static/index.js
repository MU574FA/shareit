function shareToggle() {
  $("#share-bar").toggle();
}
function searchToggle() {
  $("#search-bar").toggle();
}
function filesToggle() {
  $("#files-bar").toggle();
}

function search() {
  var files = $(".card");
  var text = $("#search").val();

  for (let i = 0; i < files.length; i++) {
    if (files[i].innerHTML.indexOf(text) == -1) {
      files[i].style.display = "none";
    } else {
      files[i].style.display = "";
    }
  }
}

function generateQR(text) {
  document.getElementById("qrcode").innerHTML = "";
  var qrcode = new QRCode(document.getElementById("qrcode"), {
    text: text,
    width: 128,
    height: 128,
    colorDark: "#000000",
    colorLight: "#ffffff",
    correctLevel: QRCode.CorrectLevel.H,
  });
  document.getElementById("qrcode-text").innerHTML = text;
}

function loading() {
  if ($("#file-field").val().length != 0) {
    $("#loading").fadeIn();
  }
}
