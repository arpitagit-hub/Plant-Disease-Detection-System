import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
import {
  getAuth,
  createUserWithEmailAndPassword,
  signInWithEmailAndPassword
} from "https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js";

const firebaseConfig = {
  apiKey: "AIzaSyDhJnhB07wqJyMC48w_N9Yvj-7y5zty2M",
  authDomain: "leafguardai.firebaseapp.com",
  projectId: "leafguardai",
  storageBucket: "leafguardai.firebasestorage.app",
  messagingSenderId: "256267019538",
  appId: "1:256267019538:web:4f3b0c5b1bd262ca90bfcb"
};


const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

// GET INPUT ELEMENTS
const nameInput = document.getElementById("name");
const emailInput = document.getElementById("email");
const passwordInput = document.getElementById("password");
const loginEmail = document.getElementById("loginEmail");
const loginPassword = document.getElementById("loginPassword");

/* REGISTER */
window.register = function () {
  createUserWithEmailAndPassword(auth, emailInput.value, passwordInput.value)
    .then(() => {
      window.closeRegister();              // from script.js
      window.showSuccess(nameInput.value); // 🎉 success modal
    })
    .catch(err => alert(err.message));
};

/* LOGIN */
window.login = function () {
  signInWithEmailAndPassword(auth, loginEmail.value, loginPassword.value)
    .then(() => {
      window.closeLogin();
      document.getElementById("loginBtn").innerText = "📤 Upload Image";
    })
    .catch(err => alert(err.message));
};
