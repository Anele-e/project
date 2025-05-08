// handdle form submission for register page
(function() {
    'use strict';
    window.addEventListener('load', function() {
      const forms = document.getElementsByClassName('needs-validation');
      Array.prototype.filter.call(forms, function(form) {
        form.addEventListener('submit', function(event) {
          if (form.checkValidity() === false) {
            event.preventDefault();
            event.stopPropagation();
          }
          form.classList.add('was-validated');
          
          // Check if passwords match
          const password = document.getElementById('password');
          const confirmPassword = document.getElementById('confirm_password');
          
          if (password.value !== confirmPassword.value) {
            confirmPassword.setCustomValidity("Passwords don't match");
            event.preventDefault();
            event.stopPropagation();
          } else {
            confirmPassword.setCustomValidity('');
          }
        }, false);
      });
    }, false);
  })();
  
  // Toggle password visibility
  function togglePasswordVisibility(inputId) {
    const input = document.getElementById(inputId);
    const icon = event.currentTarget;
    
    if (input.type === 'password') {
      input.type = 'text';
      icon.classList.replace('fa-eye', 'fa-eye-slash');
    } else {
      input.type = 'password';
      icon.classList.replace('fa-eye-slash', 'fa-eye');
    }
  }
  
  // Real-time password match validation
  document.getElementById('confirm_password').addEventListener('input', function() {
    const password = document.getElementById('password').value;
    const confirmPassword = this.value;
    
    if (password !== confirmPassword) {
      this.setCustomValidity("Passwords don't match");
    } else {
      this.setCustomValidity('');
    }
  });
