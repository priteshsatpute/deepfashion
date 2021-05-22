$(document).ready(function() {
  const placeImage = document.getElementById("placeImage");

  $("#selectImageButton").click(function() {
    $("#selectImageInput").trigger("click");
  });

  $("#selectImageInput").change(function(event) {
    $(placeImage).css("display", "block");
    placeImage.src = URL.createObjectURL(event.target.files[0]);
    $(".card-text").hide();
    $("#selectImageButton").html("Change Image");
    $("#searchButton").removeClass("d-none");
  });

  $("#searchButton").click(event => {
    event.preventDefault();
    $.ajax({
      url: "/getdata",
      success: data => {
        console.log(data);
        $("#suggestions").removeClass("d-none");
        values = document.getElementById("row");
        data.forEach(info => {
          values.append(
            "<div class='col-lg-4 col-md-6 col-sm-12 text-center mt-4'>\
              <div class='card'>\
                <img src='" +
              info.img +
              "' alt=''/>\
                <div class='card-footer d-flex justify-content-around'>\
                  " +
              info.price +
              "\
                  <a href='" +
              info.site +
              "'' target='_new'\
                  >" +
              info.companyName +
              "</a>\
                </div>\
              </div>\
            </div>"
          );
        });
        $("#row").html(values);
      }
    });
  });
});
