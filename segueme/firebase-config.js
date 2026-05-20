// Importa as funções necessárias dos SDKs do Google
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.0.0/firebase-app.js";
import { getFirestore, collection, addDoc } from "https://www.gstatic.com/firebasejs/9.0.0/firebase-firestore.js";

// A configuração do Firebase do seu projeto (Suas Chaves exclusivas)
const firebaseConfig = {
    apiKey: "AIzaSyBigAjWkFd6mqKGoxJyQX4hBLTbCOMx4Is",
    authDomain: "segue-me-55296.firebaseapp.com",
    projectId: "segue-me-55296",
    storageBucket: "segue-me-55296.firebasestorage.app",
    messagingSenderId: "326941771035",
    appId: "1:326941771035:web:d1a60c2694536816deffbe",
    measurementId: "G-4KHGR7Q6KP"
};

// Inicializa o Firebase
const app = initializeApp(firebaseConfig);

// Inicializa o Banco de Dados (Firestore) e exporta para usar nos formulários
const db = getFirestore(app);
export { db, collection, addDoc };