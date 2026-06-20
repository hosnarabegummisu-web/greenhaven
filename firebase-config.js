// =====================================================================
//  GREEN HEAVEN — Firebase কনফিগারেশন
//  ---------------------------------------------------------------------
//  ⚠️  নিচের firebaseConfig অবজেক্টের ভেতরের মানগুলো আপনার নিজের Firebase
//      প্রজেক্টের কী (key) দিয়ে রিপ্লেস করুন।
//      কোথায় পাবেন তা SETUP-GUIDE.md ফাইলে ধাপে ধাপে দেওয়া আছে।
//
//  নোট: এই কী-গুলো গোপন কিছু নয়; ওয়েব Firebase অ্যাপে এগুলো পাবলিক থাকাই
//       স্বাভাবিক। আসল নিরাপত্তা আসে Firestore Security Rules থেকে
//       (firestore.rules ফাইল দেখুন)।
// =====================================================================

import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-app.js";
import { getAuth, GoogleAuthProvider, FacebookAuthProvider } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-auth.js";
import { getFirestore } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-firestore.js";

// 🔻🔻🔻 এখানে আপনার নিজের প্রজেক্টের তথ্য বসান 🔻🔻🔻
const firebaseConfig = {
  apiKey: "YOUR_API_KEY",
  authDomain: "YOUR_PROJECT_ID.firebaseapp.com",
  projectId: "YOUR_PROJECT_ID",
  storageBucket: "YOUR_PROJECT_ID.appspot.com",
  messagingSenderId: "YOUR_SENDER_ID",
  appId: "YOUR_APP_ID"
};
// 🔺🔺🔺 এখানে আপনার নিজের প্রজেক্টের তথ্য বসান 🔺🔺🔺

const app = initializeApp(firebaseConfig);

export const auth = getAuth(app);
export const db = getFirestore(app);

// সোশ্যাল লগইন প্রোভাইডার
export const googleProvider = new GoogleAuthProvider();
export const facebookProvider = new FacebookAuthProvider();

// প্রতিবার অ্যাকাউন্ট বাছাই করার সুযোগ দিতে
googleProvider.setCustomParameters({ prompt: 'select_account' });
facebookProvider.addScope('email');
