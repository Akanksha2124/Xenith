// Common JavaScript functions for Rural Health Portal

// Function to validate Aadhaar number
function validateAadhaar(aadhaar) {
  return /^\d{12}$/.test(aadhaar);
}

// Function for showing alerts/notifications
function showNotification(message, type = 'success') {
  // Create notification element
  const notification = document.createElement('div');
  notification.className = `fixed top-4 right-4 p-4 rounded shadow-lg ${
    type === 'error' ? 'bg-red-100 text-red-700' : 'bg-green-100 text-green-700'
  }`;
  notification.textContent = message;
  
  // Append to body
  document.body.appendChild(notification);
  
  // Remove after 3 seconds
  setTimeout(() => {
    notification.remove();
  }, 3000);
}

// Function to get geolocation
function getGeolocation(successCallback, errorCallback) {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(successCallback, errorCallback);
  } else {
    errorCallback({ message: "Geolocation is not supported by this browser." });
  }
}