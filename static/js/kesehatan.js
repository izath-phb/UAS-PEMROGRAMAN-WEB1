// Interaksi sederhana untuk form
document.getElementById("contactForm").addEventListener("submit", function(e) {
    e.preventDefault();
    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    alert(`Terima kasih ${name}, pesan Anda telah dikirim!`);
});
