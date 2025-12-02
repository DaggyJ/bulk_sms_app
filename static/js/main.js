// ===============================
// GLOBAL VARIABLES
// ===============================
let balanceInterval = null;
let isLoggedIn = false;
let isAdmin = false;

// ===============================
// INITIALIZE PAGE
// ===============================
document.addEventListener('DOMContentLoaded', () => {
  fetchSessionStatus();

  // Update footer year
  const yearSpan = document.getElementById('year');
  if (yearSpan) yearSpan.textContent = new Date().getFullYear();
});

// ===============================
// FETCH USER STATUS FROM SERVER
// ===============================
function fetchSessionStatus() {
  fetch('/user_status')
    .then(res => res.json())
    .then(data => {
      isLoggedIn = data.isLoggedIn;
      isAdmin = data.isAdmin;
      updateNavbar(data.balance);

      // Load users table for admins
      if (isAdmin) loadUsers();
    })
    .catch(err => console.error('Session check failed:', err));
}

// ===============================
// UPDATE NAVBAR BUTTONS
// ===============================
function updateNavbar(balance = 0) {
  const adminUploadBtn = document.getElementById('adminUploadBtn');
  const adminUsersSection = document.getElementById('adminUsersSection');
  const balanceEl = document.getElementById('balance');
  const loginBtn = document.getElementById('loginLogoutBtn');

  if (isLoggedIn && isAdmin) {
    adminUploadBtn.style.display = 'inline-block';
    adminUsersSection.style.display = 'block';
    balanceEl.style.display = 'inline-block';
    balanceEl.textContent = `Balance: KES ${balance}`;

    if (!balanceInterval) balanceInterval = setInterval(updateBalance, 10000);
  } else {
    adminUploadBtn.style.display = 'none';
    adminUsersSection.style.display = 'none';
    balanceEl.style.display = 'none';
    if (balanceInterval) { clearInterval(balanceInterval); balanceInterval = null; }
  }

  loginBtn.textContent = isLoggedIn ? 'Logout' : 'Login';
  loginBtn.onclick = isLoggedIn ? logout : showLoginForm;
}

// ===============================
// UPDATE BALANCE (ADMIN ONLY)
// ===============================
function updateBalance() {
  if (!isAdmin) return;
  fetch('/user_status')
    .then(res => res.json())
    .then(data => {
      const balanceEl = document.getElementById('balance');
      if (data.balance !== undefined) balanceEl.textContent = `Balance: KES ${data.balance}`;
    })
    .catch(err => console.error('Error fetching balance:', err));
}

// ===============================
// LOGOUT
// ===============================
function logout() {
  fetch('/logout', { method: 'POST' })
    .then(res => res.json())
    .then(() => {
      isLoggedIn = false;
      isAdmin = false;
      updateNavbar();
      document.getElementById('dashboard').innerHTML = '';
      document.getElementById('upload').style.display = 'none';
      document.getElementById('adminUsersSection').style.display = 'none';
    })
    .catch(err => console.error('Logout failed:', err));
}

// ===============================
// LOAD USERS TABLE (ADMIN)
// ===============================
function loadUsers() {
  fetch('/get_all_users')
    .then(res => res.json())
    .then(data => {
      const tbody = document.querySelector('#usersTable tbody');
      tbody.innerHTML = '';

      data.users.forEach(user => {
        const pending = user.status === 'pending' ? user.username : '';
        const active = user.status === 'approved' ? user.username : '';

        let actionHTML = '';
        if (user.status === 'pending') {
          actionHTML = `
            <button class="approveBtn" data-id="${user.id}">Approve</button>
            <button class="rejectBtn" data-id="${user.id}">Reject</button>
          `;
        } else if (user.status === 'approved') {
          actionHTML = `<button class="disableBtn" data-id="${user.id}">Disable</button>`;
        }

        const tr = document.createElement('tr');
        tr.innerHTML = `<td>${pending}</td><td>${active}</td><td>${actionHTML}</td>`;
        tbody.appendChild(tr);
      });

      // Attach event listeners
      document.querySelectorAll('.approveBtn').forEach(btn =>
        btn.addEventListener('click', () => adminAction(btn.dataset.id, 'approve'))
      );
      document.querySelectorAll('.rejectBtn').forEach(btn =>
        btn.addEventListener('click', () => adminAction(btn.dataset.id, 'reject'))
      );
      document.querySelectorAll('.disableBtn').forEach(btn =>
        btn.addEventListener('click', () => adminAction(btn.dataset.id, 'disable'))
      );
    })
    .catch(err => console.error('Failed to load users:', err));
}

// Call on page load
loadUsers();

// ===============================
// ADMIN ACTION HANDLER
// ===============================
function adminAction(userId, action) {
  let url = '';
  if (action === 'approve') url = '/approve_user';
  else if (action === 'reject') url = '/reject_user';
  else if (action === 'disable') url = '/disable_user';
  else return;

  fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ user_id: userId })
  })
    .then(res => res.json())
    .then(data => {
      alert(data.status || 'Action completed');
      loadUsers(); // <-- refresh table correctly
    })
    .catch(err => console.error('Admin action failed:', err));
}


//Enable Button
function enableUser(userId) {
  fetch("/enable_user", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ user_id: userId })
  })
  .then(res => res.json())
  .then(data => {
    alert(data.status);
    loadUsers(); // Refresh table after enabling
  })
  .catch(err => console.error("Enable user error:", err));
}
