console.log("custom.js loaded")

// Script start
var totalItems = $('.beritaitem').length;
var currentIndex = $('div.beritaitem.active').index() + 1;
var time = 5000;
var play = true;
var reset = false;

var berita1 = "A press on a button translates all images in the respective direction along the x-axis. An image on the edge, is set transparent outerImg.style.opacity = '0'; and translated to the other side. You can add or remove image elements in HTML and it still works.";
<<<<<<< HEAD
var berita2 = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived.";
=======
var berita2 = "This is only for getting your data models into JS. For manipulating them, you should create some views that will get called from JS (by AJAX). They should probably return JSON. Check out http://djangosnippets.org/snippets/622/ or http://djangosnippets.org/snippets/2102/ on how to simply return only JSON from a view.";
>>>>>>> 9ea83b64a1cba3cbec7e280f8f7500266953389a
var berita3 = "berita3";

$('#beritateks').html(berita1);


//menganti berita untuk + 1
function changenews() {
    currentIndex = $('div.beritaitem.active').index() + 1;
    if (currentIndex == 1) {
        $('#beritateks').html(berita2);
    }
    else if (currentIndex == 2) {
        $('#beritateks').html(berita3);
    }
    else {
        $('#beritateks').html(berita1);
    }
}

//mengganti berita untuk -1
function minusnews() {
    currentIndex = $('div.beritaitem.active').index() - 1;
    if (currentIndex == 1) {
        $('#beritateks').html(berita2);
    }
    else if (currentIndex == -1) {
        $('#beritateks').html(berita3);
    }
    else {
        $('#beritateks').html(berita1);
    }
}

//fungsi timer
function Timer(fn, t) {
    var timerObj = setInterval(fn, t);

    //stop
    this.stop = function () {
        if (timerObj) {
            clearInterval(timerObj);
            timerObj = null;
        }
        return this;
    }

    // saat mulai
    this.start = function () {
        if (!timerObj) {
            this.stop();
            timerObj = setInterval(fn, t);
        }
        return this;
    }

    //  reset
    this.reset = function (newT = t) {
        t = newT;
        return this.stop().start();
    }
}

//saat pointer tidak pada caraousel
function jalankan() {
    timer.reset(5000);
}

//saat pointer pada cararousel
function berhenti() {
    timer.stop();
}

var timer = new Timer(function () {
    changenews();
    timer.reset(5000);
}, 5000);

$(".next").click(function () {
    changenews();
    timer.reset(5000);
});

$(".prev").click(function () {
    minusnews();
    timer.reset(5000);
});