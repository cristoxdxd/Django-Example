// Make a notification of register
const registerNotification = () => {
  alert('You have successfully register a post!');
  const registerNotification = document.getElementById('register-notification');
  registerNotification.classList.add('show');
  setTimeout(() => {
    registerNotification.classList.remove('show');
  }, 3000);
};