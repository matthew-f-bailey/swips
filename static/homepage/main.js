
document.addEventListener("DOMContentLoaded", function(event) {

    init_game();

});

function init_js(){
    document.querySelectorAll('#startword .flip-card').forEach(item => {
        item.addEventListener('click', e => {
            // If any other one is already flipped
            document.querySelectorAll('#startword .flip-card').forEach(i => {
                i.classList.remove("flipped");
                i.value = "";
            });
            item.classList.toggle("flipped");
            item.querySelector("input").focus();
        })
    });
}

function init_game() {
    // Creating Our XMLHttpRequest object
    var xhr = new XMLHttpRequest();

    // Making our connection
    var url = '/init_game';
    xhr.open("GET", url, true);

    // function execute after request is successful
    xhr.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("game-container").innerHTML = this.responseText;
            init_js();
        }
    }
    // Sending our request
    xhr.send();
}

function focus_ltr() {
    // Clear all other ltrs
    document.querySelectorAll('#startword input').forEach(item => {
        item.value = '';
    })
}

function submit_guess() {

    // Gather up both words
    let guessed_word = "";  // The word the user typed in by changing a letter
    let past_word = "";  // The old word on the front of the card
    let final_word = document.getElementById('guess-word').innerText;
    let ltrs1 = document.querySelectorAll("#startword div.flip-card-inner");
    for (i = 0; i < ltrs1.length; ++i) {
        let l1 = ltrs1[i].querySelector('.flip-card-front').innerText;
        let l2 = ltrs1[i].querySelector('.flip-card-back input').value;
        if (l2) {
            guessed_word += l2;
        } else {
            guessed_word += l1;
        }
        past_word += l1
    }

    // Creating Our XMLHttpRequest object
    var xhr = new XMLHttpRequest();

    // Making our connection
    var url = '/guess?guessed_word='+guessed_word+'&past_word='+past_word+'&final_word='+final_word;
    xhr.open("GET", url, true);

    // function execute after request is successful
    xhr.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById('the-words').innerHTML = this.responseText;
            init_js();
        }
    }
    // Sending our request
    xhr.send();
}
