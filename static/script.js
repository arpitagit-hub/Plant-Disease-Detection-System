const slides = document.querySelectorAll(".slide");

let index = 0;

setInterval(() => {
  slides[index].classList.remove("active");
  index = (index + 1) % slides.length;
  slides[index].classList.add("active");
}, 1500);

const overlay = document.getElementById("overlay");
const loginModal = document.getElementById("loginModal");
const registerModal = document.getElementById("registerModal");
const successModal = document.getElementById("successModal");
const userName = document.getElementById("userName");
const loginBtn = document.getElementById("loginBtn");

/*================= AUTH ================= 


let isLoggedIn = false;

function openLogin() {
  loginModal.style.display = "flex";
  overlay.style.display = "block";
}

function closeLogin() {
  loginModal.style.display = "none";
  overlay.style.display = "none";
}

function openRegister() {
  registerModal.style.display = "flex";
  overlay.style.display = "block";
}

function closeRegister() {
  registerModal.style.display = "none";
  overlay.style.display = "none";
}

function switchToRegister() {
  closeLogin();
  openRegister();
}

function showSuccess(name) {
  isLoggedIn = true;
  userName.innerText = name;
  successModal.style.display = "flex";

  document.getElementById("uploadAfterLogin").classList.remove("hidden");
  document.getElementById("loginRequiredBox").style.display = "none";

  loginBtn.innerText = "📤 Upload";
  loginBtn.onclick = () => {
    document.getElementById("uploadAfterLogin")
      .scrollIntoView({ behavior: "smooth" });
  };

  setTimeout(() => {
    successModal.style.display = "none";
    overlay.style.display = "none";
  }, 2500);
}

/* ================= UPLOAD LOGIC ================= 


const fileInput = document.getElementById("fileInput");
const imagePreview = document.getElementById("imagePreview");
const progressBar = document.querySelector(".progress-bar");
const progressFill = document.getElementById("progressFill");
const aiResult = document.getElementById("aiResult");

fileInput.addEventListener("change", () => {
  if (!isLoggedIn) return;

  const file = fileInput.files[0];
  if (!file) return;

  // Preview
  imagePreview.src = URL.createObjectURL(file);
  imagePreview.classList.remove("hidden");

  // Progress
  progressBar.classList.remove("hidden");
  progressFill.style.width = "0%";

  let progress = 0;
  const interval = setInterval(() => {
    progress += 10;
    progressFill.style.width = progress + "%";

    if (progress >= 100) {
      clearInterval(interval);
      callAIModel(file);
    }
  }, 200);
});
*/
/* ================= AI CALL ================= */

function callAIModel(file) {
  aiResult.classList.remove("hidden");
  aiResult.innerHTML = "🔍 Analyzing image...";

  // Mock AI (replace with backend later)
  setTimeout(() => {
    aiResult.innerHTML = `
      🌿 <b>Disease Detected:</b> Leaf Blight<br>
      💊 <b>Recommendation:</b> Remove affected leaves and apply fungicide.
    `;
  }, 2000);
}
