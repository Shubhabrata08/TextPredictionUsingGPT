// selecting dom element
const btn = document.querySelector("#generateBtn");

// adding event listener to button
btn.addEventListener("click", fetchHandler);

// selecting loading div
const loader = document.querySelector("#loading");

// showing loading
function displayLoading() {
    loader.classList.add("display");
    // to stop loading after some time
    // setTimeout(() => {
    //     loader.classList.remove("display");
    // }, 5000);
}
// hiding loading 
function hideLoading() {
    loader.classList.remove("display");
}
function fetchHandler(event) {
    displayLoading()
}
function printText(idx, genStr) {
    // console.log(idx);
    document.getElementById("generatedText").innerHTML += genStr[idx];
}

function delay(idx, genStr) {
    setTimeout(() => {
        document.getElementById("generatedText").innerHTML += genStr[idx];
        console.log(document.getElementById("generatedText").innerHTML);
    }, (idx + 1) * 50);
}
$("#generateBtn").click(function (e) {
    e.preventDefault();
    $.ajax({
        type: "POST",
        url: "/modelTest",
        beforeSend: displayLoading(),
        data: {
            num_char: $("#sliderVal").text(), // < note use of 'this' here
            // access_token: $("#access_token").val()
        },
        success: function (result) {
            hideLoading();
            var genStr = result.outputString;
            document.getElementById("generatedText").innerHTML = '';
            for (let i = 0; i < genStr.length; i++) {
                delay(i, genStr);
            }

        },
        error: function (result) {
            alert('error');
        }
    });
});