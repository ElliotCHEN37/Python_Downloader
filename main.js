console.log("welcome！");

const navLinks = document.querySelectorAll("nav ul li a");

navLinks.forEach((link) => {
  link.addEventListener("click", (e) => {
    e.preventDefault();
    console.log(`clicked ${link.textContent} `);
  });
});