document.addEventListener('DOMContentLoaded', function() {
    console.log('Theme toggle JS loaded!');
    const themeToggleBtn = document.getElementById('theme-toggle');
    console.log('Theme toggle button:', themeToggleBtn);
    
    if (!themeToggleBtn) {
        console.error('Theme toggle button not found!');
        return;
    }
    
    const moonIcon = themeToggleBtn.querySelector('.fa-moon');
    const sunIcon = themeToggleBtn.querySelector('.fa-sun');

    // Load saved theme from localStorage
    const savedTheme = localStorage.getItem('theme');
    console.log('Saved theme:', savedTheme);
    if (savedTheme === 'dark') {
        document.body.classList.add('dark-theme');
        moonIcon.style.display = 'none';
        sunIcon.style.display = 'block';
        console.log('Applied dark theme from localStorage');
    }

    // Toggle theme on button click
    themeToggleBtn.addEventListener('click', function() {
        console.log('Theme toggle clicked!');
        document.body.classList.toggle('dark-theme');

        if (document.body.classList.contains('dark-theme')) {
            localStorage.setItem('theme', 'dark');
            moonIcon.style.display = 'none';
            sunIcon.style.display = 'block';
            console.log('Switched to dark theme');
        } else {
            localStorage.setItem('theme', 'light');
            moonIcon.style.display = 'block';
            sunIcon.style.display = 'none';
            console.log('Switched to light theme');
        }
    });
});
