let inactivityTime = function () {
    let time;
    window.onload = resetTimer;
    document.onmousemove = resetTimer;
    document.onmousedown = resetTimer;
    document.onkeydown = resetTimer;
    document.addEventListener('scroll', resetTimer, true);
    function requestPredictions() {
        console.log("Requesting predictions.")
        if (document.getElementById("gpt2textarea").value != "") {

            $.ajax({
                type: "POST",
                url: "/gpt2Test",
                data: {

                    inpString: document.getElementById("gpt2textarea").value,
                },
                success: function (result) {
                    // hideLoading();
                    var inpString = document.getElementById("gpt2textarea").value;
                    var genStr = result.outputString;
                    // genStr=genStr.substring(inpString.length);
                    console.log(genStr);
                    var suggestionText = genStr.substring(inpString.length);
                    console.log(suggestionText);
                },
                error: function (result) {
                    alert('error');
                }
            });
        }
    }
    function resetTimer() {
        clearTimeout(time);
        time = setTimeout(requestPredictions, 2000)
    }
};
inactivityTime();
// setInterval(() => {
//     var x = document.getElementById("gpt2textarea").value;
//     console.log(x);
// }, 2000);