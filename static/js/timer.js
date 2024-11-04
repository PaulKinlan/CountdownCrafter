function initTimer(timerId) {
    function updateTimer(endDate) {
        const now = new Date().getTime();
        const distance = new Date(endDate).getTime() - now;

        if (distance < 0) {
            document.getElementById('countdown').innerHTML = "Event has ended!";
            return;
        }

        const months = Math.floor(distance / (1000 * 60 * 60 * 24 * 30));
        const days = Math.floor((distance % (1000 * 60 * 60 * 24 * 30)) / (1000 * 60 * 60 * 24));
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);

        let display = '';
        if (months > 0) display += `${months}M `;
        if (days > 0) display += `${days}d `;
        display += `${hours}h ${minutes}m ${seconds}s`;

        document.getElementById('countdown').innerHTML = display;
    }

    async function fetchTimerData() {
        const response = await fetch(`/api/timer/${timerId}`);
        const data = await response.json();
        updateTimer(data.end_date);
    }

    // Update immediately and then every second
    fetchTimerData();
    setInterval(fetchTimerData, 1000);
}

async function copyToClipboard() {
    // Get the current URL and remove any token parameter
    const url = new URL(window.location.href);
    url.searchParams.delete('token');
    const shareUrl = url.toString();
    
    // Get the event name from the page title
    const eventName = document.querySelector('h1').textContent;
    
    // Check if Web Share API is available
    if (navigator.share) {
        try {
            await navigator.share({
                title: `Countdown Timer: ${eventName}`,
                text: `Check out this countdown timer for ${eventName}!`,
                url: shareUrl
            });
        } catch (err) {
            // Fallback to clipboard if sharing was cancelled or failed
            fallbackToClipboard(shareUrl);
        }
    } else {
        // Fallback for browsers that don't support Web Share API
        fallbackToClipboard(shareUrl);
    }
}

function fallbackToClipboard(url) {
    navigator.clipboard.writeText(url)
        .then(() => {
            const shareButton = document.querySelector('[onclick="copyToClipboard()"]');
            const originalText = shareButton.textContent;
            shareButton.textContent = 'Copied!';
            setTimeout(() => {
                shareButton.textContent = originalText;
            }, 2000);
        })
        .catch(() => {
            alert('Failed to copy URL to clipboard');
        });
}
