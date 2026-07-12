function cambiarModo() {
    document.body.classList.toggle("dark-mode");

    if (document.body.classList.contains("dark-mode")) {
        localStorage.setItem("modo", "oscuro");
        document.getElementById("modoBtn").innerHTML = "☀️";
    } else {
        localStorage.setItem("modo", "claro");
        document.getElementById("modoBtn").innerHTML = "🌙";
    }
}

window.onload = function () {
    if (localStorage.getItem("modo") == "oscuro") {
        document.body.classList.add("dark-mode");
        document.getElementById("modoBtn").innerHTML = "☀️";
    }
};
