
let input = document.getElementById("gpt2textarea");
var inpLength=0;
// let suggestion = document.getElementById("suggestion");
//Enter key code
const enterKey = 13;
console.log("TextPredict Online");
window.onload = () => {
  input.value = "";
  clearSuggestion();
};

const clearSuggestion = () => {
  suggestion.innerHTML = "";
  console.log("Working");
};

//Execute function on input
input.addEventListener("input", (e) => {
  clearSuggestion();
});

//   Complete predictive text on enter key
input.addEventListener("keydown", (e) => {
  //When user presses enter and suggestion exists
  if (e.keyCode == enterKey && suggestion.innerText != "") {
    e.preventDefault();
    var str=suggestion.innerText.substring(inpLength);
    input.value += str;
    //clear the suggestion
    clearSuggestion();
  }
});

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
                    inpLength=inpString.length;
                    var genStr = result.outputString;
                    let suggestion=document.getElementById("suggestion");
                    suggestion.innerHTML="";
                    for(let i=0;i<inpString.length;i++)
                    {
                        suggestion.innerHTML+="&nbsp;";
                    }
                    suggestion.innerHTML+=genStr.substring(inpString.length);
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
$("textarea").each(function () {
  this.setAttribute("style", "height:auto;overflow-y:hidden;");
}).on("input", function () {
  this.style.height = "auto";
  this.style.height = (this.scrollHeight) + "px";
}).on("keydown", function (e) {
  if (e.key === "Enter") {
      // Adjust height after Enter key press
      this.style.height = "auto";
      this.style.height = (this.scrollHeight) + "px";
  }
});
// setInterval(() => {
//     var x = document.getElementById("gpt2textarea").value;
//     console.log(x);
// }, 2000);